import logging
import os
import tkinter as tk
from tkinter import font

from PIL import ImageTk

from automagica import config
from automagica.config import _
from automagica.models import Flow, ThreadedBot
from automagica.models.bots import ConsoleHandler
from automagica.config import _

from .buttons import Button, HelpButton, LargeButton, ToolbarImageButton
from .graphs import (
    ActivityNodeGraph,
    CommentNodeGraph,
    ConnectorGraph,
    DotPyFileNodeGraph,
    IfElseNodeGraph,
    LoopNodeGraph,
    PythonCodeNodeGraph,
    StartNodeGraph,
    SubFlowNodeGraph,
)
from .inputs import InputField


class LabelFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(
            bd=0,
            font=(config.FONT, 10),
            fg=config.COLOR_0,
            bg=config.COLOR_4,
            padx=5,
            pady=5,
        )


class ToolbarLabelFrame(LabelFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(
            font=(config.FONT, 8), fg=config.COLOR_1, bg=config.COLOR_0, padx=0, pady=0
        )


class ConsoleFrame(tk.Frame):
    def __init__(self, parent=None, bot=None, width=None, height=None):
        tk.Frame.__init__(self, parent, width=width, height=height)
        self.parent = parent
        self.bot = bot

        self.command_buffer = []

        self.console_frame = self.create_console_frame()
        self.console_frame.pack(fill="both", expand=True)

        logger = logging.getLogger("automagica.bot")
        logger.setLevel(logging.INFO)

        logger.addHandler(ConsoleHandler(self.write))

    def up(self, event):
        command = self.command_entry.get()

        if self.command_buffer:
            try:
                index = self.command_buffer.index(command)
            except ValueError:
                index = False

            if index:
                new_command = self.command_buffer[index - 1]
            else:
                new_command = self.command_buffer[-1]

            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, new_command)

    def create_console_frame(self):
        frame = tk.Frame(self, bg=config.COLOR_4)

        self.command_entry = InputField(
            frame, placeholder=_("Type command here and press <ENTER> to run...")
        )
        self.command_entry.configure(font=("TkFixedFont"))

        self.command_entry.bind("<Return>", self.enter)
        self.command_entry.bind("<Up>", self.up)

        from tkinter import scrolledtext

        self.console_text = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            relief=tk.FLAT,
            bg=config.COLOR_5,
            fg=config.COLOR_1,
            insertbackground=config.COLOR_1,
        )

        self.console_text.frame.configure(bd=0, highlightthickness=0, relief="ridge")

        self.command_entry.pack(fill="x", anchor="nw")
        self.console_text.pack(fill="both", padx=0, pady=0, expand=True)

        self.console_text.insert(
            "1.0",
            _(
                "Welcome to Automagica Flow!  \nUse this Interactive Console to your liking!\n\n"
            ),
        )
        self.console_text.configure(font="TkFixedFont", state="disabled")
        self.console_text.tag_config("error", foreground="red")

        button_frame = tk.Frame(frame, bg=config.COLOR_4)

        self.reset_bot_button = Button(
            button_frame, text=_("Reset Bot"), command=self.on_reset_bot_click
        )
        self.reset_bot_button.configure(font=("Helvetica", 8))
        self.reset_bot_button.pack(side="left")

        self.clear_button = Button(
            button_frame, text=_("Clear Output"), command=self.on_clear_click
        )
        self.clear_button.configure(font=("Helvetica", 8))
        self.clear_button.pack(side="left", padx=5)

        self.open_variable_explorer_button = Button(
            button_frame,
            text=_("Variable Explorer"),
            command=self.on_open_variable_explorer_click,
        )
        self.open_variable_explorer_button.configure(font=("Helvetica", 8))
        self.open_variable_explorer_button.pack(side="left")

        button_frame.place(anchor="ne", relx=1, rely=0)

        self.line_start = 0

        return frame

    def on_open_variable_explorer_click(self):
        from .windows import VariableExplorerWindow

        VariableExplorerWindow(self, bot=self.bot)

    def on_reset_bot_click(self):
        self.bot.reset()

    def on_clear_click(self):
        self.console_text.configure(state="normal")
        self.console_text.delete("1.0", tk.END)
        self.console_text.configure(state="disabled")

    def destroy(self):
        self.bot.stop()
        self.console_text.destroy()
        tk.Frame.destroy(self)

    def enter(self, e):
        command = self.command_entry.get()
        self.command_buffer.append(command)

        self.line_start += len(command)
        self.bot.run(command)
        self.command_entry.delete(0, tk.END)

    def write(self, record):
        self.console_text.configure(state="normal")

        if record.levelname == "ERROR":
            self.console_text.insert(tk.END, record.getMessage() + "\n", "error")
        else:
            self.console_text.insert(tk.END, record.getMessage() + "\n")

        self.console_text.see(tk.END)
        self.console_text.configure(state="disabled")


class FlowFrame(tk.Frame):
    def __init__(self, parent, flow, height=None, width=None):
        super().__init__(parent, height=height, width=width)

        self.parent = parent
        self.width = width
        self.height = height
        self.flow = flow
        self.delta = 0.75

        self.gridsize = 25

        # Create canvas
        self.canvas = tk.Canvas(
            self, bg=config.COLOR_4, bd=0, highlightthickness=0, relief="ridge"
        )

        # # Windows/MacOSX
        # self.canvas.bind("<MouseWheel>", self.wheel)

        # # Linux
        # self.canvas.bind("<Button-5>", self.wheel)
        # self.canvas.bind("<Button-4>", self.wheel)

        self.canvas.pack(fill="both", expand=True)

        self.draw()

    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def create_grid(self):
        w = 10000  # Get current width of canvas
        h = 10000  # Get current height of canvas

        self.canvas.delete("grid_line")  # Will only remove the grid_line

        # Creates all vertical lines at intevals of 100
        for i in range(-10000, w, 25):
            self.canvas.create_line(
                i, -10000, i, h, dash=(4, 2), tag="grid_line", fill=config.COLOR_9
            )

        # Creates all horizontal lines at intevals of 100
        for i in range(-10000, h, 25):
            self.canvas.create_line(
                -10000, i, w, i, dash=(4, 2), tag="grid_line", fill=config.COLOR_9
            )

    def wheel(self, event):
        scale = 1.0

        # Linux
        if event.num == 5 or event.delta == -120:
            scale *= self.delta

        # Windows
        if event.num == 4 or event.delta == 120:
            scale /= self.delta

        # Rescale all canvas objects
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        self.canvas.scale("all", x, y, scale, scale)

    def clear(self):
        self.canvas.delete("all")

    def _get_node_graph_by_node(self, node):
        for graph in self.graphs:
            if graph.node == node:
                return graph

    def draw(self):
        self.clear()

        self.graphs = []
        self.connectors = []

        self.background = self.canvas.create_rectangle(
            -10000,
            -10000,
            10000,
            10000,
            tags="background",
            fill=config.COLOR_4,
            width=0,
        )

        self.create_grid()

        self.canvas.tag_bind("background", "<ButtonPress-1>", self.move_start)
        self.canvas.tag_bind("background", "<B1-Motion>", self.move_move)

        for node in self.flow.nodes:
            graph = eval(
                "{class_name}Graph(self, node)".format(
                    class_name=node.__class__.__name__
                )
            )
            node.graph = graph

            self.graphs.append(graph)

        for node in self.flow.nodes:
            for attr in dir(node):
                if attr.endswith("_node"):
                    next_node_uid = getattr(node, attr)
                    if next_node_uid:
                        next_node = self.flow.get_node_by_uid(next_node_uid)
                        if next_node:
                            connector = ConnectorGraph(
                                self, node.graph, next_node.graph, connector_type=attr
                            )
                            self.connectors.append(connector)

        self.set_canvas_layers()

    def set_canvas_layers(self):
        self.canvas.tag_lower("background")
        # self.canvas.tag_lower("arrows")

    def update_connectors(self):
        for connector in self.connectors:
            connector.update()
        self.set_canvas_layers()

    def add_node_graph(self, node):
        graph = eval("{}Graph(self, node)".format(node.__class__.__name__))
        graph.update()

        self.graphs.append(graph)

        self.draw()

        return graph


class ToolbarFrame(tk.Frame):
    def __init__(self, parent, height=None, width=None):
        super().__init__(parent, height=height, width=width)

        self.configure(bg=config.COLOR_0)
        self.parent = parent

        logo_canvas = tk.Canvas(
            self, bg=config.COLOR_0, width=175, height=45, bd=0, highlightthickness=0
        )
        logo_canvas.pack(side="left", padx=10, pady=10)

        logo_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "logo.png",
        )

        self.logo_image = ImageTk.PhotoImage(file=logo_path)
        logo_canvas.create_image(0, 0, image=self.logo_image, anchor="nw")

        open_button = LargeButton(
            self, text="Open", command=self.clicked_open_button, underline=0
        )
        self.parent.master.bind("<Alt-o>", lambda e: self.clicked_open_button())
        open_button.pack(side="left", padx=5, pady=5)

        save_button = LargeButton(
            self, text="Save", command=self.clicked_save_button, underline=0
        )
        self.parent.master.bind("<Alt-s>", lambda e: self.clicked_save_button())
        save_button.pack(side="left", padx=5, pady=5)

        save_as_button = LargeButton(
            self, text=_("Save As"), command=self.clicked_save_as_button, underline=5
        )
        self.parent.master.bind("<Alt-a>", lambda e: self.clicked_save_as_button())
        save_as_button.pack(side="left", padx=5, pady=5)

        run_button = LargeButton(
            self, text=_("Run (F5)"), command=self.clicked_run_button
        )
        self.parent.master.bind("<F5>", lambda e: self.clicked_run_button())
        run_button.pack(side="left", padx=5, pady=5)

        run_step_by_step_button = LargeButton(
            self,
            text=_("Run step-by-step (Shift+F5)"),
            command=self.clicked_run_step_by_step_button,
        )
        self.parent.master.bind(
            "<Shift-F5>", lambda e: self.clicked_run_step_by_step_button()
        )
        run_step_by_step_button.pack(side="left", padx=5, pady=5)

        # validate_button = LargeButton(
        #     self, text=_("Validate (F6)"), command=self.clicked_validate_button
        # )
        # self.parent.master.bind("<F6>", lambda e: self.clicked_validate_button())
        # validate_button.pack(side="left", padx=5, pady=5)

        empty_label = tk.Label(self, width=5, bg=config.COLOR_0)
        empty_label.pack(side="left")

        actions_frame = ToolbarLabelFrame(
            self, text=_("Automagica Wand (Powered by AI)")
        )

        record_click_button = ToolbarImageButton(
            actions_frame,
            image_path="mouse-pointer-solid.png",
            text=_("Click"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.click"
            ),
        )
        record_click_button.pack(side="left")

        record_double_click_button = ToolbarImageButton(
            actions_frame,
            image_path="mouse-pointer-solid.png",
            text=_("Double-Click"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.double_click"
            ),
        )
        record_double_click_button.pack(side="left")

        record_right_click_button = ToolbarImageButton(
            actions_frame,
            image_path="mouse-pointer-solid.png",
            text=_("Right-Click"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.right_click"
            ),
        )
        record_right_click_button.pack(side="left")

        record_move_to_button = ToolbarImageButton(
            actions_frame,
            image_path="mouse-solid.png",
            text=_("Move To"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.move_mouse_to"
            ),
        )
        record_move_to_button.pack(side="left")

        record_type_into_button = ToolbarImageButton(
            actions_frame,
            image_path="mouse-solid.png",
            text=_("Typing"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.typing"
            ),
        )
        record_type_into_button.pack(side="left")

        record_read_text_button = ToolbarImageButton(
            actions_frame,
            image_path="glasses-solid.png",
            text=_("Read Text"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.read_text"
            ),
        )
        record_read_text_button.pack(side="left")

        record_is_visible_button = ToolbarImageButton(
            actions_frame,
            image_path="eye.png",
            text=_("Is Visible"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.is_visible"
            ),
        )
        record_is_visible_button.pack(side="left")

        record_wait_appear_button = ToolbarImageButton(
            actions_frame,
            image_path="eye.png",
            text=_("Wait Appear"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.wait_appear"
            ),
        )
        record_wait_appear_button.pack(side="left")

        record_wait_vanish_button = ToolbarImageButton(
            actions_frame,
            image_path="eye.png",
            text=_("Wait Vanish"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.wait_vanish"
            ),
        )
        record_wait_vanish_button.pack(side="left")

        actions_frame.pack(side="left", padx=5, pady=5)

    def clicked_run_step_by_step_button(self):
        from .windows import Notification, FlowPlayerWindow

        # Minimize window
        self.master.master.iconify()

        def on_close():
            # Resize original window
            self.master.master.deiconify()

        # Run automation flow
        FlowPlayerWindow(
            self,
            flow=self.master.master.flow,
            bot=self.master.master.bot,
            autoplay=False,
            step_by_step=True,
            on_close=on_close,
        )

    def clicked_record_action_button(self, action):
        # Minimize window
        self.parent.master.iconify()

        from .windows import ActionRecorderWindow

        # Record action
        ActionRecorderWindow(self, action)

        # Restore window
        self.parent.master.deiconify()

    def clicked_validate_button(self):
        from .windows import FlowValidationWindow

        FlowValidationWindow(self, self.parent.master.flow)

    def clicked_open_button(self):
        from tkinter import filedialog

        file_path = filedialog.askopenfilename(
            initialdir="./",
            title=_("Select Automagica Flow"),
            filetypes=[("Flow (.json)", "*.json")],
        )

        if not file_path:
            return

        self.parent.master.file_path = file_path

        # Clear flow
        self.parent.master.flow_frame.clear()

        # Load flow
        self.parent.master.flow.load(self.parent.master.file_path)

        # Update title
        self.parent.master.title(
            "{} - Automagica Flow".format(self.parent.master.file_path)
        )

        # Render flow
        self.parent.master.flow_frame.draw()

        from .windows import Notification

        Notification(self, _("Flow opened."))

    def clicked_save_button(self):
        if not self.master.master.flow.file_path:
            self.master.master.flow.file_path = tk.filedialog.asksaveasfilename(
                defaultextension=".a8a"
            )

            if not self.master.master.flow.file_path:
                return

        self.master.master.flow.save(self.master.master.flow.file_path)

        from .windows import Notification

        Notification(self, _("Saved flow."))

    def clicked_save_as_button(self):
        from tkinter import filedialog

        self.master.master.file_path = filedialog.asksaveasfilename(
            defaultextension=".a8a"
        )

        if not self.master.master.file_path:
            return

        self.master.master.flow.save(self.master.master.file_path)

        # Update title
        self.master.master.title(
            "{} - Automagica Flow".format(self.master.master.file_path)
        )

        from .windows import Notification

        Notification(self, "Saved flow.")

    def clicked_run_button(self):
        from .windows import Notification, FlowPlayerWindow

        # Minimize window
        self.master.master.iconify()

        def on_close():
            # Resize original window
            self.master.master.deiconify()

        # Run automation flow
        FlowPlayerWindow(
            self,
            flow=self.master.master.flow,
            bot=self.master.master.bot,
            autoplay=True,
            step_by_step=False,
            on_close=on_close,
        )


class SidebarFrame(tk.Frame):
    def __init__(self, parent, height=None, width=None):
        super().__init__(parent, height=height, width=width)
        self.parent = parent

        self.configure(bg=config.COLOR_4,)

        # Activities
        self.activities_frame = self.create_activities_frame()
        self.activities_frame.place(relx=0, rely=0, relheight=0.65, relwidth=1)

        help_button = HelpButton(
            self,
            message=_(
                "Activities are t he basic building blocks of Automagica. By tieing activities together, you get a Flow."
            ),
        )
        help_button.place(relx=1, rely=0, anchor="ne")

        # Nodes
        self.nodes_frame = self.create_nodes_frame()
        self.nodes_frame.place(relx=0, rely=0.65, relheight=0.25, relwidth=1)

        help_button = HelpButton(
            self,
            message=_(
                "Special nodes allow you to control the way the Flow runs. It also allows you to extend the capabilities of your Flow beyond the activities that Automagica has to offer."
            ),
        )
        help_button.place(relx=1, rely=0.65, anchor="ne")

        # Instructions
        self.instructions_frame = self.create_instructions_frame()
        self.instructions_frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)

    def create_instructions_frame(self):
        frame = tk.Frame(self, bg=config.COLOR_4)

        self.instructions_label = tk.Label(
            frame,
            text=_("Instructions"),
            anchor="w",
            font=(config.FONT, 10),
            justify="left",
            fg=config.COLOR_0,
            bg=config.COLOR_4,
        )
        self.instructions_label.pack()

        self.instructions = tk.Label(
            frame,
            font=(config.FONT, 8),
            text=_(
                "Left-click drag: move node\nDouble-click: properties\nMiddle-click: remove"
            ),
            anchor="w",
            fg=config.COLOR_11,
            bg=config.COLOR_4,
        )
        self.instructions.pack()

        return frame

    def create_activities_frame(self):
        frame = tk.Frame(self, bg=config.COLOR_4)

        self.results = []
        self.query = tk.StringVar()

        self.instructions_label = tk.Label(
            frame,
            text=_("Activities"),
            anchor="w",
            font=(config.FONT, 10),
            justify="left",
            fg=config.COLOR_0,
            bg=config.COLOR_4,
        )
        self.instructions_label.pack()

        self.search_entry = InputField(
            frame, textvariable=self.query, placeholder=_("Search activities..."),
        )
        self.query.trace("w", self.search_activities)

        self.search_entry.focus()
        self.search_entry.bind("<Return>", self.search_activities)

        self.search_entry.pack(fill="x")

        self.activities_list = tk.Listbox(frame)
        self.activities_list.configure(
            bd=0,
            relief="flat",
            selectbackground=config.COLOR_0,
            selectforeground=config.COLOR_1,
            highlightthickness=0,
            fg=config.COLOR_11,
            bg=config.COLOR_10,
            activestyle="none",
        )

        for key, activity in config.ACTIVITIES.items():
            if activity.get("class"):
                name = "{} - {}".format(activity["class"], activity["name"])
            else:
                name = activity["name"]

            self.activities_list.insert(tk.END, name)
            self.results.append(key)

        self.activities_list.bind("<Double-Button-1>", lambda e: self.select_activity())
        scrollbar = tk.Scrollbar(
            self.activities_list, orient="vertical", command=self.activities_list.yview
        )

        scrollbar.pack(side="right", fill="y")

        self.activities_list.config(yscrollcommand=scrollbar.set)

        self.activities_list.pack(fill="both", expand=True, padx=5, pady=5)

        return frame

    def create_nodes_frame(self):
        frame = tk.Frame(self, bg=config.COLOR_4)
        from automagica.config import _

        self.nodes_label = tk.Label(
            frame,
            text=_("Special Nodes"),
            anchor="w",
            justify="left",
            font=(config.FONT, 10),
            fg=config.COLOR_0,
            bg=config.COLOR_4,
        )
        self.nodes_label.pack()

        self.nodes_list = tk.Listbox(frame)
        self.nodes_list.configure(
            bd=0,
            relief="flat",
            selectbackground=config.COLOR_0,
            selectforeground=config.COLOR_1,
            highlightthickness=0,
            fg=config.COLOR_11,
            bg=config.COLOR_10,
            activestyle="none",
        )

        self.node_types = [
            ("Start", _("Start")),
            ("IfElse", _("If Else")),
            ("Loop", _("Loop")),
            ("DotPyFile", _("Python Script (.py)")),
            ("SubFlow", _("Sub-flow")),
            ("PythonCode", _("Python Code")),
        ]

        for _, label in self.node_types:
            self.nodes_list.insert(tk.END, label)

        self.nodes_list.bind("<Double-Button-1>", lambda e: self.select_node())

        self.nodes_list.pack(fill="both", expand=True, padx=5, pady=5)

        return frame

    def select_activity(self):
        selection_index = self.activities_list.curselection()
        
        if selection_index:
            self.parent.master.add_activity(self.results[selection_index[0]])

    def select_node(self):
        selection_index = self.nodes_list.curselection()
        self.parent.master.add_node(self.node_types[selection_index[0]][0])

    def search_activities(self, *args):
        query = self.search_entry.get()
        query = query.strip()
        query = query.lower()

        self.activities_list.delete(0, tk.END)
        self.results = []

        for key, val in config.ACTIVITIES.items():
            if (
                any([query in keyword.lower() for keyword in val["keywords"]])
                or query == _("Search activities...").lower()
            ):

                if val.get("class"):
                    name = "{} - {}".format(val["class"], val["name"])
                else:
                    name = val["name"]

                self.activities_list.insert(tk.END, name)
                self.results.append(key)
