import os
import tkinter as tk
from tkinter import filedialog, font, ttk

from PIL import ImageTk

from automagica import config
from automagica.config import _, ICONS
from automagica.gui.buttons import Button, ToolbarImageButton
from automagica.gui.graphs import generate_icon


class KeycombinationEntry(tk.Frame):
    """
    Input widget for a keyboard key combination
    """

    def __init__(self, *args, key_combination=[], **kwargs):
        super().__init__(*args, **kwargs)

        self.key_combination = key_combination
        self.layout()

    def layout(self):
        self.ctrl = tk.BooleanVar()
        self.ctrl_checkbutton = tk.Checkbutton(
            self, text=_("Control"), variable=self.ctrl
        )
        self.ctrl_checkbutton.pack(side="left")

        if "ctrl" in self.key_combination:
            self.ctrl_checkbutton.select()

        self.shift = tk.BooleanVar()
        self.shift_checkbutton = tk.Checkbutton(
            self, text=_("Shift"), variable=self.shift
        )
        self.shift_checkbutton.pack(side="left")

        if "shift" in self.key_combination:
            self.shift_checkbutton.select()

        self.alt = tk.BooleanVar()
        self.alt_checkbutton = tk.Checkbutton(self, text=_("Alt"), variable=self.alt)
        self.alt_checkbutton.pack(side="left")

        if "alt" in self.key_combination:
            self.alt_checkbutton.select()

        keys = ["F1", "F2", "F3", "F4", "F5", "F6"]
        self.key_combobox = ttk.Combobox(self, values=keys)
        self.key_combobox.pack(side="left")

        if self.key_combination:
            self.key_combobox.current(keys.index(self.key_combination[-1]))

    def get(self):
        result = []

        if self.ctrl:
            result.append("ctrl")

        if self.shift:
            result.append("shift")

        if self.alt:
            result.append("alt")

        result.append(self.key_combobox.get())

        return result


class InputField(tk.Entry):
    """
    Default styled input field with placeholder functionality
    """

    def __init__(self, *args, placeholder="", **kwargs):
        super().__init__(*args, **kwargs)

        # Save placeholder value
        self.placeholder = placeholder

        # Default styling
        self.configure(
            fg=config.COLOR_12,
            bg=config.COLOR_13,
            relief=tk.FLAT,
            font=font.Font(family=config.FONT, size=10),
            bd=2,
            width=30,
        )

        # Keybinds
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        # Assume the input widget is not focused
        self.on_focus_out()

    def on_focus_in(self, event=None):
        if self.placeholder:  # Clear the field if a placeholder is defined
            self.delete("0", tk.END)

    def on_focus_out(self, event=None):
        if self.placeholder:
            if self.get() == "":  # If the field is empty, set the placeholder value
                self.insert(tk.END, self.placeholder)


class InputWidget(tk.Frame):
    """
    Default input widget
    """

    def __init__(self, parent, *args, value=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.value = value
        self.layout()

    def layout(self):
        self.input_field = InputField(self)
        self.input_field.pack(side="left")

        if self.value:
            self._set(str(self.value))

    def get(self):
        return self.input_field.get()

    def _set(self, value):
        self.value = value
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.value)


class TextInputWidget(tk.Frame):
    """
    Default input widget
    """

    def __init__(self, parent, *args, value=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.value = value
        self.layout()

    def layout(self):
        self.input_field = tk.Text(self, height=10)
        self.input_field.pack(side="left")

        if self.value:
            self._set(str(self.value))

    def get(self):
        return self.input_field.get("1.0", tk.END)

    def _set(self, value):
        self.value = value
        self.input_field.delete("1.0", tk.END)
        self.input_field.insert("1.0", self.value)


class FilePathInputWidget(tk.Frame):
    """
    Input widget for a file path
    """

    def __init__(self, parent, *args, value=None, extensions=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.value = value

        if extensions:
            self.filetypes = ((ext, f"*.{ext}") for ext in extensions)
        else:
            self.filetypes = None

        self.layout()

    def layout(self):
        self.input_field = InputField(self)
        self.input_field.pack(side="left")

        self.browse_button = Button(
            self, text=_("Browse"), command=self.browse_button_click
        )
        self.browse_button.pack(side="left")

        if self.value:
            self._set(self.value)

    def get(self):
        return self.input_field.get()

    def _set(self, value):
        self.value = value
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.value)

    def browse_button_click(self):
        if self.filetypes:
            file_path = filedialog.askopenfilename(
                initialdir="./", title=_("Select File"), filetypes=self.filetypes
            )
        else:
            file_path = filedialog.askopenfilename(
                initialdir="./", title=_("Select File")
            )

        self._set('"{}"'.format(file_path))


class FilePathOutputWidget(FilePathInputWidget):
    """
    Output widget for a file path
    """

    def browse_button_click(self):
        file_path = filedialog.asksaveasfilename(
            initialdir="./", title=_("Select File")
        )

        self._set('"{}"'.format(file_path))


class DirWidget(tk.Frame):
    """
    Input widget for a file path
    """

    def __init__(self, parent, *args, value=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.value = value
        self.layout()

    def layout(self):
        self.input_field = InputField(self)
        self.input_field.pack(side="left")

        self.browse_button = Button(
            self, text=_("Browse"), command=self.browse_button_click
        )
        self.browse_button.pack(side="left")

        if self.value:
            self._set(self.value)

    def get(self):
        return self.input_field.get()

    def _set(self, value):
        self.value = value
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.value)

    def browse_button_click(self):
        file_path = filedialog.askdirectory(
            initialdir="./", title=_("Select Directory")
        )

        self._set('"{}"'.format(file_path))


class IntegerInputWidget(tk.Frame):
    """
    Input widget for an integer
    """

    def __init__(self, parent, *args, value=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.value = value
        self.layout()

    def layout(self):
        self.input_field = ttk.Spinbox(self)
        self.input_field.pack(side="left")

        if self.value:
            self._set(self.value)

    def get(self):
        return self.input_field.get()

    def _set(self, value):
        self.value = value
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.value)


class BooleanInputWidget(tk.Frame):
    """
    Input widget for a boolean (checkbox)
    """

    def __init__(self, parent, *args, value=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.variable = tk.IntVar(self)
        self.value = value
        self.layout()

    def layout(self):
        self.checkbox = ttk.Checkbutton(self, variable=self.variable)
        self.checkbox.pack(side="left")

        if self.value != None:
            self._set(self.value)

    def get(self):
        if self.variable.get() == 1:
            return True
        else:
            return False

    def _set(self, value):
        if self.value == True:
            self.variable.set(1)
        else:
            self.variable.set(0)


class AutomagicaIdInputWidget(tk.Frame):
    """
    Input widget for an Automagica ID (generated by Automagica Wand)
    """

    def __init__(self, parent, *args, value=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.value = value
        self.layout()

    def layout(self):
        self.input_field = InputField(self)
        self.input_field.pack(side="left")

        self.browse_button = Button(
            self, text=_("View"), command=self.view_button_click, font=(config.FONT, 10)
        )
        self.browse_button.pack(side="left")

        self.record_button = Button(
            self,
            text=_("Record"),
            command=self.record_button_click,
            font=(config.FONT, 10),
        )
        self.record_button.pack(side="left")

        if self.value:
            self._set(self.value)

    def get(self):
        return self.input_field.get()

    def _set(self, value):
        self.value = value
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.value)

    def view_button_click(self):
        import webbrowser

        automagica_id = self.get().replace('"', "")
        automagica_id = self.get().replace("'", "")

        url = os.environ.get("AUTOMAGICA_PORTAL_URL", "https://portal.automagica.com")

        webbrowser.open(f"{url}/ui-element/{automagica_id}")

    def record_button_click(self):
        from .windows import WandWindow

        def on_finish(automagica_id):
            self._set(f'"{automagica_id}"')

        _ = WandWindow(self, on_finish=on_finish)


class AutocompleteDropdown(ttk.Combobox):
    """
    Input widget that auto-completes with a dropdown
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, width=30, **kwargs)
        self.values = sorted(self["values"], key=str.lower)
        self["values"] = self.values

        self.matches = []
        self.match_index = 0
        self.pos = 0

        self.bind("<KeyRelease>", self.on_key_release)

    def filter_values(self, delta=0):
        if delta:
            self.delete(self.pos, tk.END)
        else:
            self.pos = len(self.get())

        matches = []

        for element in self.values:
            if element.lower().startswith(self.get().lower()):
                matches.append(element)

        if matches != self.matches:
            self.match_index = 0
            self.matches = matches

        if matches == self.matches and self.matches:
            self.match_index = (self.match_index + delta) % len(self.matches)

        if self.matches:
            self.delete(0, tk.END)
            self.insert(0, self.matches[self.match_index])
            self.select_range(self.pos, tk.END)

    def on_key_release(self, event):
        if event.keysym == "Right":
            self.pos = self.index(tk.END)

        elif event.keysym == "Left":
            if self.pos < self.index(tk.END):
                self.delete(self.pos, tk.END)
            else:
                self.pos = self.pos - 1
                self.delete(self.pos, tk.END)

        elif event.keysym == "BackSpace":
            self.delete(self.index(tk.INSERT), tk.END)
            self.pos = self.index(tk.END)

        if len(event.keysym) == 1:
            self.filter_values()

    def _set(self, value):
        for i, val in enumerate(self["values"]):
            if value in val:
                self.current(i)
                break


class NodeSelectionInputWidget(tk.Frame):
    """
    Dropdown widget for selecting a node
    """

    def __init__(self, parent, nodes, *args, value=None, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.nodes = nodes
        self.value = value
        self.layout()

    def layout(self):
        self.node_menu = AutocompleteDropdown(
            self,
            values=["{} ({})".format(node, node.uid) for node in self.nodes] + [""],
            font=(config.FONT, 10),
        )

        self.node_menu.pack(side="left")

        if self.value:
            self._set(self.value)

    def get(self):
        if self.node_menu.get():
            return self.node_menu.get().split("(")[1].split(")")[0]
        else:
            return None

    def _set(self, value):
        for i, val in enumerate(self.node_menu["values"]):
            if self.value in val:
                self.node_menu.current(i)
                break

    def browse_button_click(self):
        file_path = filedialog.asksaveasfilename(
            initialdir="./", title=_("Select File")
        )

        self._set('"{}"'.format(file_path))


class SettingContextMenu(tk.Frame):
    def __init__(self, parent, *args, text="", options=[], **kwargs):
        """
        Options should be a list of tupes ('Description', value)
        """
        super().__init__(parent, *args, **kwargs)

        self.options = options
        self.selected_option = self.options[0]

        # Variable for Tkinter based on the description
        self.selected_option_description = tk.StringVar()
        self.selected_option_description.set(self.selected_option[0])

        self.menu = tk.Menu(self, tearoff=0)
        for item in self.options:
            self.menu.add_radiobutton(
                label=item[0],
                variable=self.selected_option_description,
                command=self.change_selected_option,
                foreground=config.COLOR_0,
                selectcolor=config.COLOR_0,
                font=(config.FONT, 10),
            )

        self.button = ToolbarImageButton(self, text=text, image_path="clock.png")
        self.button.bind("<Button-1>", self.show_context_menu)
        self.button.pack()

    def get(self):
        return self.selected_option

    def show_context_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

    def change_selected_option(self):
        selected_option_description = self.selected_option_description.get()
        for item in self.options:
            if item[0] == selected_option_description:
                self.selected_option = item


class ActivityBlock:
    def __init__(self, canvas, activity, x, y):
        self.canvas = canvas

        if activity.get("class"):
            name = "{} - {}".format(activity["class"], activity["name"])
        else:
            name = activity["name"]

        self.canvas.create_text(
            x + 25,
            y + 2,
            text=name,
            anchor=tk.NW,
            font=(config.FONT, 10),
            tags=activity.get("key"),
        )

        icon_name = str(activity["icon"].split("la-")[-1])

        if icon_name not in ["html5", "trello", "salesforce", "chrome", "readme"]:
            icon_name = icon_name + "-solid.png"
        else:
            icon_name = icon_name + ".png"

        self.icon_img = ICONS.tkinter(icon_name)

        self.icon = self.canvas.create_image(
            x, y, image=self.icon_img, anchor=tk.NW, tags=activity.get("key")
        )

        self.canvas.tag_bind(
            activity.get("key"),
            "<Double-Button-1>",
            lambda e: self.select_activity(activity.get("key")),
        )

    def select_activity(self, key):
        self.canvas.master.master.master.master.add_activity(key)


class ActivitySelectionFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        from automagica.utilities import all_activities

        self.activities = all_activities()

        self.nodes_label = tk.Label(
            self,
            text=_("Activities"),
            anchor="w",
            justify="left",
            font=font.Font(family=config.FONT, size=12),
            fg=config.COLOR_0,
            bg=config.COLOR_4,
        )
        self.nodes_label.pack()

        self.query = tk.StringVar()
        self.search_entry = InputField(
            self, textvariable=self.query, placeholder=_("Search activities..."),
        )
        self.query.trace("w", self.search_activities)
        self.search_entry.focus()
        self.search_entry.bind("<Return>", self.search_activities)
        self.search_entry.pack(fill="x")

        self.canvas = tk.Canvas(
            self, bg="white", scrollregion=(0, 0, 300, 35 * len(self.activities)),
        )

        self.render_activity_blocks([val for key, val in self.activities.items()])

        self.vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vertical_scrollbar.config(command=self.canvas.yview)

        self.canvas.config(yscrollcommand=self.vertical_scrollbar.set)
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.bind("<Enter>", self._bound_to_mousewheel)
        self.bind("<Leave>", self._unbound_to_mousewheel)

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 60)), "units")

    def render_activity_blocks(self, activities):
        self.activity_blocks = []

        for i, activity in enumerate(activities):
            activity_block = ActivityBlock(self.canvas, activity, 5, (22 * i) + 5)
            self.activity_blocks.append(activity_block)

        self.canvas.config(scrollregion=(0, 0, 300, 22 * len(self.activity_blocks)))

    def search_activities(self, *args):
        """
        Search for activities by their keywords, name or description
        """
        query = self.search_entry.get()

        # Clean query
        query = query.strip()
        query = query.lower()

        # Clear canvas
        self.canvas.delete("all")

        results = []

        for key, val in self.activities.items():
            if (
                any(
                    [query in keyword.lower() for keyword in val["keywords"]]
                )  # Matches keywords
                or query in val["name"].lower()  # Matches name
                or query in val["description"].lower()  # Matches description
                or query == _("Search activities...").lower()
            ):

                if val.get("class"):
                    name = "{} - {}".format(val["class"], val["name"])
                else:
                    name = val["name"]

                results.append(val)

        self.render_activity_blocks(results)
