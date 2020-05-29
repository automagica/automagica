import tkinter as tk
from tkinter import font, ttk, filedialog

from automagica import config
from automagica.config import _
from automagica.gui.buttons import Button


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


class FilePathInputWidget(tk.Frame):
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
        file_path = filedialog.asksaveasfilename(
            initialdir="./", title=_("Select File")
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

        webbrowser.open("https://automagica.id/{}".format(self.get().replace('"', "")))


class AutocompleteDropdown(ttk.Combobox):
    """
    Input widget that auto-completes with a dropdown
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.values = sorted(self["values"], key=str.lower)
        self["values"] = self.values

        self.matches = []
        self.match_index = 0
        self.pos = 0

        self.bind("<KeyRelease>", self.on_key_release)
        self.bind("<FocusIn>", self.on_focus_in)

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

    def on_focus_in(self, event=None):
        self.delete(0, tk.END)
        self.pos = self.index(tk.END)


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
            values=["{} ({})".format(node, node.uid) for node in self.nodes],
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
