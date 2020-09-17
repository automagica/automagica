"""Copyright 2020 Oakwood Technologies BVBA"""

import logging
import os
import tkinter as tk
from tkinter import filedialog, font, scrolledtext

from PIL import ImageTk

from automagica import config
from automagica.bots import ConsoleHandler, ThreadedBot
from automagica.config import _
from automagica.flow import Flow
from automagica.gui.buttons import (
    Button,
    HelpButton,
    LargeButton,
    ToolbarImageButton,
)
from automagica.gui.graphs import (
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
from automagica.gui.inputs import (
    ActivitySelectionFrame,
    InputField,
    SettingContextMenu,
)


class LabelFrame(tk.LabelFrame):
    """
    Default styled LabelFrame
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set default configuration
        self.configure(
            bd=0,
            font=(config.FONT, 10),
            fg=config.COLOR_0,
            bg=config.COLOR_4,
            padx=5,
            pady=5,
        )

        # If overriding options are given, apply them
        self.configure(**kwargs)


class ToolbarLabelFrame(LabelFrame):
    """
    LabelFrame styled for the toolbar
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adjusted font size, foreground and background colors and padding
        self.configure(
            font=(config.FONT, 8),
            fg=config.COLOR_1,
            bg=config.COLOR_0,
            padx=0,
            pady=0,
        )

        # If overriding options are given, apply them
        self.configure(**kwargs)


class ConsoleFrame(tk.Frame):
    """
    Interactive console frame
    """

    def __init__(self, parent=None, bot=None, width=None, height=None):
        super().__init__(parent, width=width, height=height)

        self.parent = parent

        # Have the bot closely availble
        self.bot = bot

        # In this buffer we keep the previous commands
        self.buffer = []

        # Console frame
        self.console_frame = self.create_console_frame()
        self.console_frame.pack(fill="both", expand=True)

        # Buttons in upper-right corner
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.place(anchor="ne", relx=1, rely=0)

        # Connect to the bot's logger
        self.logger = logging.getLogger("automagica.bot")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(ConsoleHandler(self.write))

    def on_up_press(self, event):
        """
        When the user presses up in the command line box, the previous command should be prefilled in the command line box.
        """
        command = self.command_entry.get()

        # Only do something if we have a buffer
        if self.buffer:
            try:
                index = self.buffer.index(command)

            except ValueError:
                index = False

            # Found an index?
            if index:
                buffered = self.buffer[index - 1]

            else:
                buffered = self.buffer[-1]

            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, buffered)

    def create_console_frame(self):
        """
        Console frame
        """
        frame = tk.Frame(self, bg=config.COLOR_4)

        self.command_entry = InputField(
            frame,
            placeholder=_("Type command here and press <ENTER> to run..."),
        )
        self.command_entry.configure(font=(config.FONT_MONO, "10"))

        self.command_entry.bind("<Return>", self.on_enter_pressed)
        self.command_entry.bind("<Up>", self.on_up_press)

        self.console_text = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            relief=tk.FLAT,
            bg=config.COLOR_5,
            fg=config.COLOR_1,
            insertbackground=config.COLOR_1,
        )

        self.console_text.frame.configure(
            bd=0, highlightthickness=0, relief="ridge"
        )

        self.command_entry.pack(fill="x", anchor="nw")
        self.console_text.pack(fill="both", padx=0, pady=0, expand=True)

        self.console_text.insert(
            "1.0",
            _(
                "Welcome to Automagica Flow!  \nUse this Interactive Console to your liking!\n\n"
            ),
        )
        self.console_text.configure(
            font=(config.FONT_MONO, "10"), state="disabled"
        )

        self.console_text.tag_config("error", foreground=config.COLOR_14)

        self.line_start = 0

        return frame

    def create_buttons_frame(self):
        """
        Buttons frame
        """
        frame = tk.Frame(self, bg=config.COLOR_4)

        self.reset_bot_button = Button(
            frame, text=_("Reset Bot"), command=self.on_reset_bot_clicked
        )
        self.reset_bot_button.configure(font=(config.FONT, 8))
        self.reset_bot_button.pack(side="left")

        self.clear_button = Button(
            frame, text=_("Clear Output"), command=self.on_clear_clicked
        )
        self.clear_button.configure(font=(config.FONT, 8))
        self.clear_button.pack(side="left", padx=5)

        self.open_variable_explorer_button = Button(
            frame,
            text=_("Variable Explorer"),
            command=self.on_open_variable_explorer_clicked,
        )
        self.open_variable_explorer_button.configure(font=(config.FONT, 8))
        self.open_variable_explorer_button.pack(side="left")

        return frame

    def on_open_variable_explorer_clicked(self):
        from .windows import (
            VariableExplorerWindow,
        )  # To avoid circular imports

        return VariableExplorerWindow(self, bot=self.bot)

    def on_reset_bot_clicked(self):
        self.bot.reset()

    def on_clear_clicked(self):
        self.console_text.configure(state="normal")
        self.console_text.delete("1.0", tk.END)
        self.console_text.configure(state="disabled")

    def destroy(self):
        """
        Override tk.Frame.destroy
        """
        # Additional clean-up pre-destroy
        self.bot.stop()
        self.console_text.destroy()

        # Call original method to destroy
        tk.Frame.destroy(self)

    def on_enter_pressed(self, e):
        command = self.command_entry.get()
        self.buffer.append(command)

        self.line_start += len(command)
        self.bot.run(command)
        self.command_entry.delete(0, tk.END)

    def write(self, record):
        """
        Write to the console itself
        """
        self.console_text.configure(state="normal")

        if record.levelname == "ERROR":
            self.console_text.insert(
                tk.END, record.getMessage() + "\n", "error"
            )
        else:
            self.console_text.insert(tk.END, record.getMessage() + "\n")

        self.console_text.see(tk.END)
        self.console_text.configure(state="disabled")


class FlowFrame(tk.Frame):
    """
    Flow design frame
    """

    def __init__(self, parent, flow, height=None, width=None):
        super().__init__(parent, height=height, width=width)

        self.parent = parent
        self.width = width
        self.height = height
        self.flow = flow

        # Scrolling scale
        self.delta = 0.75

        # Size of the grid
        self.gridsize = 25

        self.selection = []

        # Create canvas
        self.canvas = tk.Canvas(
            self, bg=config.COLOR_4, bd=0, highlightthickness=0, relief="ridge"
        )

        self.canvas.pack(fill="both", expand=True)

        self.draw()

    def delete_selection(self, event):
        for i in self.selection:
            i.delete()

        self.selection = []
        self.draw()

    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

        for i in self.selection:
            i.remove_selection()

        self.selection = []

    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def create_grid(self):
        w = 10000  # Get current width of canvas
        h = 10000  # Get current height of canvas

        self.canvas.delete("grid_line")  # Will only remove the grid_line

        # Creates all vertical lines at intevals of 100
        for i in range(-10000, w, 25):
            self.canvas.create_line(
                i,
                -10000,
                i,
                h,
                dash=(4, 2),
                tag="grid_line",
                fill=config.COLOR_9,
                tags="background",
            )

        # Creates all horizontal lines at intevals of 100
        for i in range(-10000, h, 25):
            self.canvas.create_line(
                -10000,
                i,
                w,
                i,
                dash=(4, 2),
                tag="grid_line",
                fill=config.COLOR_9,
                tags="background",
            )

    def on_mouse_wheel(self, event):
        """
        Scroll to zoom
        """
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
        """
        Clear the design area
        """
        self.canvas.delete("all")

    def _get_node_graph_by_node(self, node):
        """
        Utility function
        """
        for graph in self.graphs:
            if graph.node == node:
                return graph

    def draw(self):
        """
        Main draw function that gets called every time
        """
        self.clear()

        self.graphs = []
        self.connectors = []

        # Make a very very large background object, which can be bound to later
        # This is necessary as the canvas background by default can not be bound to
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

        # Keybinds to the background
        self.canvas.tag_bind("background", "<ButtonPress-1>", self.move_start)
        self.canvas.tag_bind("background", "<B1-Motion>", self.move_move)

        for node in self.flow.nodes:
            graph = eval(  # nosec
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
                                self,
                                node.graph,
                                next_node.graph,
                                connector_type=attr,
                            )
                            self.connectors.append(connector)

        self.set_canvas_layers()

    def set_canvas_layers(self):
        """
        Set background to lowest layer
        """
        self.canvas.tag_lower("background")

    def update_connectors(self):
        """
        Redraw connectors only
        """

        for connector in self.connectors:
            connector.update()

        self.set_canvas_layers()

    def add_node_graph(self, node):
        """
        Add a node graph
        """
        graph = eval(
            "{}Graph(self, node)".format(node.__class__.__name__)
        )  # nosec

        graph.update()

        self.graphs.append(graph)

        self.draw()

        return graph


class ToolbarFrame(tk.Frame):
    """
    Toolbar frame
    """

    def __init__(self, parent, height=None, width=None):
        super().__init__(parent, height=height, width=width)

        self.configure(bg=config.COLOR_0)
        self.parent = parent

        logo_canvas = tk.Canvas(
            self,
            bg=config.COLOR_0,
            width=175,
            height=45,
            bd=0,
            highlightthickness=0,
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

        file_frame = ToolbarLabelFrame(self, text=_("File"))

        open_button = ToolbarImageButton(
            file_frame,
            text="Open",
            command=self.clicked_open_button,
            image_path="folder-open.png",
        )
        self.parent.master.bind(
            "<Alt-o>", lambda e: self.clicked_open_button()
        )
        open_button.pack(side="left")

        save_as_button = ToolbarImageButton(
            file_frame,
            text=_("Save As"),
            command=self.clicked_save_as_button,
            image_path="save.png",
        )
        self.parent.master.bind(
            "<Alt-a>", lambda e: self.clicked_save_as_button()
        )
        save_as_button.pack(side="left")

        file_frame.pack(side="left", padx=20, pady=5)

        run_frame = ToolbarLabelFrame(self, text=_("Run"))

        run_button = ToolbarImageButton(
            run_frame,
            text=_("Run Flow"),
            command=self.clicked_run_button,
            image_path="play-solid.png",
        )
        run_button.config(bg=config.COLOR_7)
        self.parent.master.bind("<F5>", lambda e: self.clicked_run_button())
        run_button.pack(side="left")

        run_step_by_step_button = ToolbarImageButton(
            run_frame,
            text=_("Step-by-Step"),
            command=self.clicked_run_step_by_step_button,
            image_path="google-play.png",
        )
        self.parent.master.bind(
            "<Shift-F5>", lambda e: self.clicked_run_step_by_step_button()
        )

        run_step_by_step_button.pack(side="left")

        run_frame.pack(side="left", padx=20, pady=5)

        wand_frame = ToolbarLabelFrame(
            self, text=_("Automagica Wand (Powered by AI)")
        )

        record_click_button = ToolbarImageButton(
            wand_frame,
            image_path="mouse-pointer-solid.png",
            text=_("Click"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.click"
            ),
        )
        record_click_button.pack(side="left")

        record_double_click_button = ToolbarImageButton(
            wand_frame,
            image_path="mouse-pointer-solid.png",
            text=_("Double-Click"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.double_click"
            ),
        )
        record_double_click_button.pack(side="left")

        record_right_click_button = ToolbarImageButton(
            wand_frame,
            image_path="mouse-pointer-solid.png",
            text=_("Right-Click"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.right_click"
            ),
        )
        record_right_click_button.pack(side="left")

        record_move_to_button = ToolbarImageButton(
            wand_frame,
            image_path="mouse-solid.png",
            text=_("Move To"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.move_mouse_to"
            ),
        )
        record_move_to_button.pack(side="left")

        record_type_into_button = ToolbarImageButton(
            wand_frame,
            image_path="mouse-solid.png",
            text=_("Typing"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.typing"
            ),
        )
        record_type_into_button.pack(side="left")

        record_read_text_button = ToolbarImageButton(
            wand_frame,
            image_path="glasses-solid.png",
            text=_("Read Text"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.read_text"
            ),
        )
        record_read_text_button.pack(side="left")

        record_is_visible_button = ToolbarImageButton(
            wand_frame,
            image_path="eye.png",
            text=_("Is Visible"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.is_visible"
            ),
        )
        record_is_visible_button.pack(side="left")

        record_wait_appear_button = ToolbarImageButton(
            wand_frame,
            image_path="eye.png",
            text=_("Wait Appear"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.wait_appear"
            ),
        )
        record_wait_appear_button.pack(side="left")

        record_wait_vanish_button = ToolbarImageButton(
            wand_frame,
            image_path="eye.png",
            text=_("Wait Vanish"),
            command=lambda: self.clicked_record_action_button(
                "automagica.activities.wait_vanish"
            ),
        )
        record_wait_vanish_button.pack(side="left")

        wand_frame.pack(side="left", padx=20, pady=5)

        wand_settings_frame = ToolbarLabelFrame(self, text=_("Settings"))

        self.delay_menu = SettingContextMenu(
            wand_settings_frame,
            text="Delay",
            options=[
                ("No Delay", 0),
                ("1 second", 1),
                ("2 seconds", 2),
                ("3 seconds", 3),
                ("4 seconds", 4),
                ("5 seconds", 5),
            ],
        )
        self.delay_menu.pack(side="left")

        def my_ui_elements_button_clicked():
            import webbrowser

            webbrowser.open(
                os.environ.get(
                    "AUTOMAGICA_PORTAL_URL", "https://portal.automagica.com"
                )
                + "/ui-element/"
            )

        self.my_ui_elements_button = ToolbarImageButton(
            wand_settings_frame,
            text="My UI Elements",
            image_path="magic-solid.png",
            command=my_ui_elements_button_clicked,
        )

        self.my_ui_elements_button.pack(side="left")

        wand_settings_frame.pack(side="left", padx=5, pady=5)

    def clicked_run_step_by_step_button(self):
        from .windows import NotificationWindow, FlowPlayerWindow

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

        from .windows import WandWindow

        def on_finish(automagica_id):
            self.parent.master.add_activity(
                action, args_={"automagica_id": f"'{automagica_id}'"}
            )

            # Restore window
            self.parent.master.deiconify()

        # Record action
        WandWindow(
            self.parent.master.master,
            action=action,
            delay=self.delay_menu.get()[1],
            on_finish=on_finish,
        )

    def clicked_validate_button(self):
        from .windows import FlowValidationWindow

        FlowValidationWindow(self, self.parent.master.flow)

    def clicked_open_button(self):
        """
        Open file
        """
        from .windows import NotificationWindow

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

        NotificationWindow(self, _("Flow opened."))

    def clicked_save_as_button(self):
        """
        Save as file
        """
        from .windows import NotificationWindow

        self.master.master.flow.file_path = filedialog.asksaveasfilename(
            defaultextension=".json"
        )

        if not self.master.master.flow.file_path:
            return

        self.master.master.flow.save(self.master.master.flow.file_path)

        # Update title
        self.master.master.title(
            "{} - Automagica Flow".format(self.master.master.flow.file_path)
        )

        NotificationWindow(self, "Saved flow")

    def clicked_run_button(self):
        """
        Run all
        """
        from .windows import NotificationWindow, FlowPlayerWindow

        # Minimize window
        self.master.master.iconify()

        def on_close():
            # Resize original window
            self.master.master.deiconify()

        # Run automation flow
        return FlowPlayerWindow(
            self,
            flow=self.master.master.flow,
            bot=self.master.master.bot,
            autoplay=True,
            step_by_step=False,
            on_close=on_close,
            autoclose=True,
        )


class SidebarFrame(tk.Frame):
    """
    Sidebar frame
    """

    def __init__(self, parent, height=None, width=None):
        super().__init__(parent, height=height, width=width)

        self.parent = parent

        self.configure(bg=config.COLOR_4,)

        # Activities
        self.activities_frame = ActivitySelectionFrame(self, bg=config.COLOR_4)
        self.activities_frame.place(relx=0, rely=0, relheight=0.65, relwidth=1)

        HelpButton(
            self,
            message=_(
                "Activities are the basic building blocks of Automagica. By tieing activities together, you get a Flow."
            ),
        ).place(relx=1, rely=0, anchor="ne")

        # Nodes
        self.nodes_frame = self.create_nodes_frame()
        self.nodes_frame.place(relx=0, rely=0.65, relheight=0.20, relwidth=1)

        HelpButton(
            self,
            message=_(
                "Special nodes allow you to control the way the Flow runs. It also allows you to extend the capabilities of your Flow beyond the activities that Automagica has to offer."
            ),
        ).place(relx=1, rely=0.65, anchor="ne")

        # Instructions
        self.instructions_frame = self.create_instructions_frame()
        self.instructions_frame.place(
            relx=0, rely=0.85, relheight=0.1, relwidth=1
        )

    def create_instructions_frame(self):
        """
        Instructions frame
        """
        frame = tk.Frame(self, bg=config.COLOR_4)

        self.instructions_label = tk.Label(
            frame,
            text=_("Instructions"),
            anchor="w",
            font=font.Font(family=config.FONT, size=12),
            justify="left",
            fg=config.COLOR_0,
            bg=config.COLOR_4,
        )
        self.instructions_label.pack()

        self.instructions = tk.Label(
            frame,
            font=font.Font(family=config.FONT, size=10),
            text=_(
                "Left-click drag: move node\nDouble-click: properties\nMiddle-click: remove"
            ),
            anchor="w",
            fg=config.COLOR_11,
            bg=config.COLOR_4,
        )
        self.instructions.pack()

        return frame

    def create_nodes_frame(self):
        """
        Nodes frame
        """
        frame = tk.Frame(self, bg=config.COLOR_4)

        from automagica.config import _

        self.nodes_label = tk.Label(
            frame,
            text=_("Special Nodes"),
            anchor="w",
            justify="left",
            font=font.Font(family=config.FONT, size=12),
            fg=config.COLOR_0,
            bg=config.COLOR_4,
        )
        self.nodes_label.pack()

        self.nodes_list = tk.Listbox(frame)
        self.nodes_list.bind(
            "<B1-Leave>", lambda event: "break"
        )  # Disable horizontal scrollling

        self.nodes_list.configure(
            bd=0,
            relief="flat",
            selectbackground=config.COLOR_0,
            selectforeground=config.COLOR_1,
            highlightthickness=0,
            fg=config.COLOR_11,
            bg=config.COLOR_10,
            activestyle="none",
            font=font.Font(family=config.FONT, size=10),
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

    def select_node(self):
        selection_index = self.nodes_list.curselection()

        if selection_index:  # Fix sometimes empty value for selection index
            self.parent.master.add_node(self.node_types[selection_index[0]][0])
