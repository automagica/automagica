import os
import tkinter as tk
from tkinter import font, ttk

from PIL import ImageTk

from automagica import config
from automagica.config import _


def generate_icon(icon_path, width=20, height=20, color="#ffffff"):
    from PIL import Image

    color = tuple(int(color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))

    img = Image.open(os.path.join("automagica", icon_path)).resize((width, height))
    data = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if data[x, y][0] == data[x, y][1] == data[x, y][2] == 0:
                data[x, y] = (color[0], color[1], color[2], data[x, y][3])

    return img


def center_window(window, w=None, h=None):
    window.update()
    window.withdraw()

    if not w:
        w = window.winfo_width()

    if not h:
        h = window.winfo_height()

    if window.master:
        master_w = window.master.winfo_width()
        master_h = window.master.winfo_height()

        master_x = window.master.winfo_x()
        master_y = window.master.winfo_y()

        x = int((master_w / 2) - (w / 2)) + master_x
        y = int((master_h / 2) - (h / 2)) + master_y

    else:
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()

        x = int((sw / 2) - (w / 2))
        y = int((sh / 2) - (h / 2))

    window.geometry("{}x{}+{}+{}".format(w, h, x, y))

    window.update()
    window.deiconify()


class NodeGraph:
    def __init__(self, parent, node):
        self.parent = parent
        self.node = node
        self.mouse_x = self.mouse_y = None

        self.w = 125
        self.h = 75

        self.parent.canvas.tag_bind(self.node.uid, "<B1-Motion>", self.drag)
        self.parent.canvas.tag_bind(self.node.uid, "<ButtonPress-1>", self.mouse_down)
        self.parent.canvas.tag_bind(self.node.uid, "<ButtonRelease-1>", self.mouse_up)
        self.parent.canvas.tag_bind(self.node.uid, "<Button-3>", self.right_click)

        self.parent.canvas.tag_bind(
            self.node.uid, "<Shift-1>", lambda x: self.select(shift=True)
        )

        self.parent.canvas.tag_bind(
            self.node.uid, "<ButtonPress-2>", lambda e: self.delete()
        )

        self.parent.canvas.tag_bind(
            self.node.uid, "<Double-Button-1>", self.double_clicked
        )

        self.selected = False
        self.selection = None

    def right_click(self, event):
        self.menu = tk.Menu(self.parent, tearoff=0)
        self.menu.add_command(label=_("Delete"), command=self.delete_clicked)
        self.menu.add_command(label=_("Duplicate"), command=self.duplicate_clicked)

        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def delete_clicked(self):
        self.delete()

    def duplicate_clicked(self):
        pass

    @property
    def center_x(self):
        return self.node.x + self.w / 2

    @property
    def center_y(self):
        return self.node.y + self.h / 2

    @property
    def connector_points(self):
        top_center = (self.center_x, self.node.y)
        left_center = (self.node.x, self.center_y)
        right_center = (self.node.x + self.w, self.center_y)
        bottom_center = (self.center_x, self.node.y + self.h)
        return [top_center, left_center, right_center, bottom_center]

    def mouse_down(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

        self.select()
        self.update()

    def mouse_up(self, event):
        self.node.x = round(self.node.x / self.parent.gridsize) * self.parent.gridsize
        self.node.y = round(self.node.y / self.parent.gridsize) * self.parent.gridsize

        self.update()
        self.parent.update_connectors()

    def drag(self, event):
        self.node.x = self.node.x + (event.x - self.mouse_x)
        self.node.y = self.node.y + (event.y - self.mouse_y)

        self.mouse_x = event.x
        self.mouse_y = event.y

        self.update()
        self.parent.update_connectors()

    def double_clicked(self, event):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def add_highlight(self):
        self.highlight = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            outline=config.COLOR_7,
            width=4,
        )

    def remove_highlight(self):
        self.parent.canvas.delete(self.highlight)
        self.highlight = None

    def add_selection(self):
        if not self.selection:
            self.selection = self.parent.canvas.create_rectangle(
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
                tags=self.node.uid,
                outline=config.COLOR_0,
                width=4,
            )
            print(self.selection)
            self.selected = True

    def remove_selection(self):
        self.parent.canvas.delete(self.selection)
        self.selection = None
        self.selected = False

    def select(self, shift=False):
        if not self.selected:

            if shift:
                if self not in self.parent.selection:
                    self.parent.selection.append(self)

            else:
                for i in self.parent.selection:
                    i.remove_selection()
                self.parent.selection = [self]

            self.add_selection()


class StartNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.draw()

    def double_clicked(self, event):
        from .windows import StartNodePropsWindow

        StartNodePropsWindow(self.parent, self.node)

    def draw(self):
        # Rectangle
        self.rectangle = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_7,
            outline=config.COLOR_7,
            width=0,
        )

        # Text
        self.text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text=str(self.node),
            tags=self.node.uid,
            fill="white",
            width=self.w,
            font=(config.FONT, 10),
        )

        # Icon
        base_path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )
        icon_path = os.path.join(base_path, "icons", "play-circle.png")

        self.icon_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color=config.COLOR_1)
        )
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 10,
            self.node.y + 10,
            image=self.icon_img,
            tags=self.node.uid,
        )

    def update(self):
        # Rectangle
        self.parent.canvas.coords(
            self.rectangle,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Text
        self.parent.canvas.coords(self.text, self.center_x, self.center_y)

        # Icon
        self.parent.canvas.coords(
            self.icon, self.node.x + self.w - 10, self.node.y + 10
        )

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )

    def delete(self):
        self.parent.canvas.delete(self.rectangle)
        self.parent.canvas.delete(self.text)
        self.parent.canvas.delete(self.icon)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()


class ActivityNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.highlight = None

        self.draw()

    @property
    def text_label(self):
        return (
            self.node.label
            if self.node.label
            else config.ACTIVITIES[self.node.activity].get("name")
        )

    def draw(self):
        # Create bounding rectangle
        self.rect = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_1,
            outline=config.COLOR_0,
            width=0,
        )

        # Add label text
        self.label_text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text=self.text_label,
            tags=self.node.uid,
            fill=config.COLOR_0,
            width=self.w,
            font=(config.FONT, 10),
        )

        self.uid_text = self.parent.canvas.create_text(
            self.node.x + self.w - 3,
            self.node.y + self.h - 3,
            text=self.node.uid,
            tags=self.node.uid,
            fill=config.COLOR_8,
            font=(config.FONT, 8),
            anchor="se",
        )

        # Icon
        base_path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )
        icon_path = os.path.join(base_path, "icons", "magic-solid.png")

        self.icon_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color=config.COLOR_0)
        )
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 3,
            self.node.y + 3,
            image=self.icon_img,
            tags=self.node.uid,
            anchor="ne",
        )

        # Play button
        base_path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )
        icon_path = os.path.join(base_path, "icons", "play-solid.png")

        self.play_button_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color=config.COLOR_7, width=20, height=20)
        )
        self.play_button = self.parent.canvas.create_image(
            self.node.x + 3,
            self.node.y + 3,
            image=self.play_button_img,
            tags="play" + self.node.uid,
            anchor="nw",
        )
        self.parent.canvas.tag_bind(
            "play" + self.node.uid, "<ButtonPress-1>", self.run_click
        )

    def delete(self):
        self.parent.canvas.delete(self.rect)
        self.parent.canvas.delete(self.label_text)
        self.parent.canvas.delete(self.uid_text)
        self.parent.canvas.delete(self.icon)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()

    def run_click(self, event):
        self.add_highlight()

        # Minimize window
        self.parent.master.master.iconify()

        def on_close():
            # Resize original window
            self.remove_highlight()
            self.parent.master.master.deiconify()

        self.node.run(self.parent.master.master.bot, on_done=on_close)

    def double_clicked(self, event):
        from .windows import ActivityNodePropsWindow

        ActivityNodePropsWindow(self.parent, self.node)

    def update(self):
        # Update rectangle
        self.parent.canvas.coords(
            self.rect,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Update label text
        self.parent.canvas.coords(self.label_text, self.center_x, self.center_y)
        self.parent.canvas.itemconfig(self.label_text, text=self.text_label)

        # Update uid text
        self.parent.canvas.coords(
            self.uid_text, self.node.x + self.w - 3, self.node.y + self.h - 3
        )
        self.parent.canvas.itemconfig(self.uid_text, text=self.node.uid)

        # Icon
        self.parent.canvas.coords(self.icon, self.node.x + self.w - 3, self.node.y + 3)

        # Play button
        self.parent.canvas.coords(self.play_button, self.node.x + 3, self.node.y + 3)

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )


class IfElseNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.draw()

    def draw(self):
        # Create bounding rectangle
        self.rect = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_1,
            outline=config.COLOR_0,
            width=0,
        )

        # Add label text
        self.label_text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text=str(self.node),
            tags=self.node.uid,
            fill=config.COLOR_0,
            font=(config.FONT, 10),
        )

        self.uid_text = self.parent.canvas.create_text(
            self.node.x + self.w - 3,
            self.node.y + self.h - 3,
            text=self.node.uid,
            tags=self.node.uid,
            fill=config.COLOR_8,
            font=(config.FONT, 8),
            anchor="se",
        )

        # Icon
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "question-circle-solid.png",
        )

        self.icon_img = ImageTk.PhotoImage(generate_icon(icon_path, color="#2196f3"))
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 10,
            self.node.y + 10,
            image=self.icon_img,
            tags=self.node.uid,
        )

    def delete(self):
        self.parent.canvas.delete(self.rect)
        self.parent.canvas.delete(self.label_text)
        self.parent.canvas.delete(self.uid_text)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()

    def double_clicked(self, event):
        from .windows import IfElseNodePropsWindow

        IfElseNodePropsWindow(self.parent, self.node)

    def update(self):
        # Update rectangle
        self.parent.canvas.coords(
            self.rect,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Update label text
        self.parent.canvas.coords(self.label_text, self.center_x, self.center_y)

        # Update uid text
        self.parent.canvas.coords(
            self.uid_text, self.node.x + self.w - 3, self.node.y + self.h - 3
        )
        self.parent.canvas.itemconfig(self.uid_text, text=self.node.uid)

        # Icon
        self.parent.canvas.coords(
            self.icon, self.node.x + self.w - 10, self.node.y + 10
        )

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )


class LoopNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.draw()

    def draw(self):
        # Create bounding rectangle
        self.rect = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_1,
            outline=config.COLOR_0,
            width=0,
        )

        # Add label text
        self.label_text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text="Loop",
            tags=self.node.uid,
            fill=config.COLOR_0,
            font=(config.FONT, 10),
        )

        self.uid_text = self.parent.canvas.create_text(
            self.node.x + self.w - 3,
            self.node.y + self.h - 3,
            text=self.node.uid,
            tags=self.node.uid,
            fill=config.COLOR_8,
            font=(config.FONT, 8),
            anchor="se",
        )

        # Icon
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "redo-alt-solid.png",
        )

        self.icon_img = ImageTk.PhotoImage(generate_icon(icon_path, color="#2196f3"))
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 10,
            self.node.y + 10,
            image=self.icon_img,
            tags=self.node.uid,
        )

    def delete(self):
        self.parent.canvas.delete(self.rect)
        self.parent.canvas.delete(self.label_text)
        self.parent.canvas.delete(self.uid_text)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()

    def double_clicked(self, event):
        from .windows import LoopNodePropsWindow

        LoopNodePropsWindow(self.parent, self.node)

    def update(self):
        # Update rectangle
        self.parent.canvas.coords(
            self.rect,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Update label text
        self.parent.canvas.coords(self.label_text, self.center_x, self.center_y)

        # Update uid text
        self.parent.canvas.coords(
            self.uid_text, self.node.x + self.w - 3, self.node.y + self.h - 3
        )
        self.parent.canvas.itemconfig(self.uid_text, text=self.node.uid)

        # Icon
        self.parent.canvas.coords(
            self.icon, self.node.x + self.w - 10, self.node.y + 10
        )

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )


class DotPyFileNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.draw()

    def draw(self):
        # Create bounding rectangle
        self.rect = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_1,
            outline=config.COLOR_0,
            width=0,
        )

        # Add label text
        self.label_text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text=_("Python Script (.py)"),
            tags=self.node.uid,
            fill=config.COLOR_0,
            font=(config.FONT, 10),
        )

        self.uid_text = self.parent.canvas.create_text(
            self.node.x + self.w - 3,
            self.node.y + self.h - 3,
            text=self.node.uid,
            tags=self.node.uid,
            fill=config.COLOR_8,
            font=(config.FONT, 8),
            anchor="se",
        )

        # Icon
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "python.png",
        )

        self.icon_img = ImageTk.PhotoImage(generate_icon(icon_path, color="#2196f3"))
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 10,
            self.node.y + 10,
            image=self.icon_img,
            tags=self.node.uid,
        )

        # Play button
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "play-solid.png",
        )
        self.play_button_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color="#28a745", width=20, height=20)
        )
        self.play_button = self.parent.canvas.create_image(
            self.node.x + 3,
            self.node.y + 3,
            image=self.play_button_img,
            tags="play" + self.node.uid,
            anchor="nw",
        )
        self.parent.canvas.tag_bind(
            "play" + self.node.uid, "<ButtonPress-1>", self.run_click
        )

    def delete(self):
        self.parent.canvas.delete(self.rect)
        self.parent.canvas.delete(self.label_text)
        self.parent.canvas.delete(self.uid_text)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()

    def double_clicked(self, event):
        from .windows import DotPyFileNodePropsWindow

        DotPyFileNodePropsWindow(self.parent, self.node)

    def update(self):
        # Update rectangle
        self.parent.canvas.coords(
            self.rect,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Update label text
        self.parent.canvas.coords(self.label_text, self.center_x, self.center_y)

        # Update uid text
        self.parent.canvas.coords(
            self.uid_text, self.node.x + self.w - 3, self.node.y + self.h - 3
        )
        self.parent.canvas.itemconfig(self.uid_text, text=self.node.uid)

        # Icon
        self.parent.canvas.coords(
            self.icon, self.node.x + self.w - 10, self.node.y + 10
        )

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )

        # Play button
        self.parent.canvas.coords(self.play_button, self.node.x + 3, self.node.y + 3)

    def run_click(self, event):
        self.add_highlight()
        self.node.run(self.parent.master.master.bot, on_done=self.remove_highlight)


class PythonCodeNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.draw()

    def draw(self):
        # Create bounding rectangle
        self.rect = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_1,
            outline=config.COLOR_0,
            width=0,
        )

        # Add label text
        self.label_text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text="Python Code",
            tags=self.node.uid,
            fill=config.COLOR_0,
            font=(config.FONT, 10),
        )

        self.uid_text = self.parent.canvas.create_text(
            self.node.x + self.w - 3,
            self.node.y + self.h - 3,
            text=self.node.uid,
            tags=self.node.uid,
            fill=config.COLOR_8,
            font=(config.FONT, 8),
            anchor="se",
        )

        # Icon
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "python.png",
        )
        self.icon_img = ImageTk.PhotoImage(generate_icon(icon_path, color="#2196f3"))
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 10,
            self.node.y + 10,
            image=self.icon_img,
            tags=self.node.uid,
        )

        # Play button
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "play-solid.png",
        )
        self.play_button_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color="#28a745", width=20, height=20)
        )
        self.play_button = self.parent.canvas.create_image(
            self.node.x + 3,
            self.node.y + 3,
            image=self.play_button_img,
            tags="play" + self.node.uid,
            anchor="nw",
        )
        self.parent.canvas.tag_bind(
            "play" + self.node.uid, "<ButtonPress-1>", self.run_click
        )

    def run_click(self, event):
        self.add_highlight()

        self.node.run(self.parent.master.master.bot, on_done=self.remove_highlight)

    def delete(self):
        self.parent.canvas.delete(self.rect)
        self.parent.canvas.delete(self.label_text)
        self.parent.canvas.delete(self.uid_text)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()

    def double_clicked(self, event):
        from .windows import PythonCodeNodePropsWindow

        PythonCodeNodePropsWindow(self.parent, self.node)

    def update(self):
        # Update rectangle
        self.parent.canvas.coords(
            self.rect,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Update label text
        self.parent.canvas.coords(self.label_text, self.center_x, self.center_y)

        # Update uid text
        self.parent.canvas.coords(
            self.uid_text, self.node.x + self.w - 3, self.node.y + self.h - 3
        )
        self.parent.canvas.itemconfig(self.uid_text, text=self.node.uid)

        # Icon
        self.parent.canvas.coords(
            self.icon, self.node.x + self.w - 10, self.node.y + 10
        )

        # Play button
        self.parent.canvas.coords(self.play_button, self.node.x + 3, self.node.y + 3)

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )


class CommentNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.draw()

    def draw(self):
        # Create bounding rectangle
        self.rect = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_3,
            outline=config.COLOR_3,
            width=0,
        )

        # Add label text
        self.label_text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text=self.node.comment,
            tags=self.node.uid,
            fill=config.COLOR_1,
            width=self.w,
            font=(config.FONT, 8),
        )

        self.uid_text = self.parent.canvas.create_text(
            self.node.x + self.w - 3,
            self.node.y + self.h - 3,
            text=self.node.uid,
            tags=self.node.uid,
            fill=config.COLOR_8,
            font=(config.FONT, 8),
            anchor="se",
        )

        # Icon
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "comment-alt.png",
        )
        self.icon_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color=config.COLOR_1)
        )
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 10,
            self.node.y + 10,
            image=self.icon_img,
            tags=self.node.uid,
        )

    def delete(self):
        self.parent.canvas.delete(self.rect)
        self.parent.canvas.delete(self.label_text)
        self.parent.canvas.delete(self.uid_text)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()

    def double_clicked(self, event):
        from .windows import CommentNodePropsWindow

        CommentNodePropsWindow(self.parent, self.node)

    def update(self):
        # Update rectangle
        self.parent.canvas.coords(
            self.rect,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Update label text
        self.parent.canvas.coords(self.label_text, self.center_x, self.center_y)

        # Update uid text
        self.parent.canvas.coords(
            self.uid_text, self.node.x + self.w - 3, self.node.y + self.h - 3
        )
        self.parent.canvas.itemconfig(self.uid_text, text=self.node.uid)

        # Icon
        self.parent.canvas.coords(
            self.icon, self.node.x + self.w - 10, self.node.y + 10
        )

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )


class SubFlowNodeGraph(NodeGraph):
    def __init__(self, parent, node):
        super().__init__(parent, node)

        self.draw()

    @property
    def text_label(self):
        if self.node.label:
            return self.node.label
        else:
            return "Sub-flow"

    def draw(self):
        # Create bounding rectangle
        self.rect = self.parent.canvas.create_rectangle(
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
            tags=self.node.uid,
            fill=config.COLOR_1,
            outline=config.COLOR_0,
            width=0,
        )

        # Add label text
        self.label_text = self.parent.canvas.create_text(
            self.center_x,
            self.center_y,
            text=self.text_label,
            tags=self.node.uid,
            fill=config.COLOR_0,
            font=(config.FONT, 10),
        )

        self.uid_text = self.parent.canvas.create_text(
            self.node.x + self.w - 3,
            self.node.y + self.h - 3,
            text=self.node.uid,
            tags=self.node.uid,
            fill=config.COLOR_8,
            font=(config.FONT, 8),
            anchor="se",
        )

        # Icon
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "project-diagram-solid.png",
        )
        self.icon_img = ImageTk.PhotoImage(generate_icon(icon_path, color="#2196f3"))
        self.icon = self.parent.canvas.create_image(
            self.node.x + self.w - 10,
            self.node.y + 10,
            image=self.icon_img,
            tags=self.node.uid,
        )

        # Play button
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "play-solid.png",
        )
        self.play_button_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color="#28a745", width=20, height=20)
        )
        self.play_button = self.parent.canvas.create_image(
            self.node.x + 3,
            self.node.y + 3,
            image=self.play_button_img,
            tags="play" + self.node.uid,
            anchor="nw",
        )
        self.parent.canvas.tag_bind(
            "play" + self.node.uid, "<ButtonPress-1>", self.run_click
        )

    def run_click(self, event):
        self.add_highlight()
        from .windows import FlowPlayerWindow
        from ..models import Flow

        _ = FlowPlayerWindow(
            self.parent.master,
            flow=Flow(self.node.subflow_path.replace('"', "")),
            bot=self.parent.master.master.bot,
            autoplay=True,
            step_by_step=False,
            autoclose=True,
        )

        self.remove_highlight()

    def delete(self):
        self.parent.canvas.delete(self.rect)
        self.parent.canvas.delete(self.label_text)
        self.parent.canvas.delete(self.uid_text)

        self.parent.parent.master.flow.nodes.remove(self.node)
        self.parent.draw()

    def double_clicked(self, event):
        from .windows import SubFlowNodePropsWindow

        SubFlowNodePropsWindow(self.parent, self.node)

    def update(self):
        # Update rectangle
        self.parent.canvas.coords(
            self.rect,
            self.node.x,
            self.node.y,
            self.node.x + self.w,
            self.node.y + self.h,
        )

        # Update label text
        self.parent.canvas.coords(self.label_text, self.center_x, self.center_y)

        # Update uid text
        self.parent.canvas.coords(
            self.uid_text, self.node.x + self.w - 3, self.node.y + self.h - 3
        )
        self.parent.canvas.itemconfig(self.uid_text, text=self.node.uid)

        # Icon
        self.parent.canvas.coords(
            self.icon, self.node.x + self.w - 10, self.node.y + 10
        )

        # Play button
        self.parent.canvas.coords(self.play_button, self.node.x + 3, self.node.y + 3)

        # Selection
        if self.selected:
            self.parent.canvas.coords(
                self.selection,
                self.node.x,
                self.node.y,
                self.node.x + self.w,
                self.node.y + self.h,
            )


def distance(a, b):
    import math

    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))


def shortest_distance(from_coords, to_coords):
    distances = []

    for to_coord in to_coords:
        for from_coord in from_coords:
            distances.append((distance(to_coord, from_coord), from_coord, to_coord))

    distances.sort(key=lambda x: x[0])

    return distances[0][1], distances[0][2]


class ConnectorGraph:
    def __init__(
        self, parent, from_nodegraph, to_nodegraph, connector_type="next_node"
    ):
        self.parent = parent
        self.from_nodegraph = from_nodegraph
        self.to_nodegraph = to_nodegraph

        self.fill = config.COLOR_7
        self.connector_type = connector_type

        if self.connector_type == "else_node":
            self.fill = config.COLOR_6

        if self.connector_type == "on_exception_node":
            self.fill = "orange"

        if self.connector_type == "loop_node":
            self.fill = config.COLOR_3

        self.draw()

    def draw(self):
        from_, to_ = shortest_distance(
            self.from_nodegraph.connector_points, self.to_nodegraph.connector_points
        )

        self.line = self.parent.canvas.create_line(
            from_[0],
            from_[1],
            to_[0],
            to_[1],
            arrow="last",
            fill=self.fill,
            width=2,
            smooth=True,
            arrowshape="10 12 5",
            tags=("arrows"),
        )

        if self.connector_type == "next_node" and isinstance(
            self.from_nodegraph, IfElseNodeGraph
        ):
            self.text_rectangle = self.parent.canvas.create_rectangle(
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) - 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                - 10,
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) + 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                + 10,
                fill=config.COLOR_7,
                outline=config.COLOR_7,
            )
            self.text = self.parent.canvas.create_text(
                (self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2,
                (
                    (self.from_nodegraph.node.y + self.from_nodegraph.h)
                    + self.to_nodegraph.node.y
                )
                / 2,
                text=_("Yes"),
                fill=config.COLOR_1,
                font=(config.FONT, 8),
            )

        if self.connector_type == "next_node" and isinstance(
            self.from_nodegraph, LoopNodeGraph
        ):
            self.text_rectangle = self.parent.canvas.create_rectangle(
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) - 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                - 10,
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) + 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                + 10,
                fill=config.COLOR_7,
                outline=config.COLOR_7,
            )
            self.text = self.parent.canvas.create_text(
                (self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2,
                (
                    (self.from_nodegraph.node.y + self.from_nodegraph.h)
                    + self.to_nodegraph.node.y
                )
                / 2,
                text=_("Done"),
                fill=config.COLOR_1,
            )

        if self.connector_type == "else_node":
            self.text_rectangle = self.parent.canvas.create_rectangle(
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) - 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                - 10,
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) + 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                + 10,
                fill=config.COLOR_6,
                outline=config.COLOR_6,
            )
            self.text = self.parent.canvas.create_text(
                (self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2,
                (
                    (self.from_nodegraph.node.y + self.from_nodegraph.h)
                    + self.to_nodegraph.node.y
                )
                / 2,
                text=_("No"),
                fill=config.COLOR_1,
            )

        if self.connector_type == "on_exception_node":
            self.text_rectangle = self.parent.canvas.create_rectangle(
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) - 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                - 10,
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) + 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                + 10,
                fill="orange",
                outline="orange",
            )
            self.text = self.parent.canvas.create_text(
                (self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2,
                (
                    (self.from_nodegraph.node.y + self.from_nodegraph.h)
                    + self.to_nodegraph.node.y
                )
                / 2,
                text=_("Error"),
                fill=config.COLOR_1,
            )

        if self.connector_type == "loop_node":

            self.text_rectangle = self.parent.canvas.create_rectangle(
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) - 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                - 10,
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) + 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                + 10,
                fill=config.COLOR_3,
                outline=config.COLOR_3,
            )

            self.text = self.parent.canvas.create_text(
                (self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2,
                (
                    (self.from_nodegraph.node.y + self.from_nodegraph.h)
                    + self.to_nodegraph.node.y
                )
                / 2,
                text=_("Repeat"),
                fill=config.COLOR_1,
            )

    def __repr__(self):
        return "<ConnectorGraph {}-{}>".format(
            self.from_nodegraph.node.uid, self.to_nodegraph.node.uid
        )

    def update(self):
        from_, to_ = shortest_distance(
            self.from_nodegraph.connector_points, self.to_nodegraph.connector_points
        )
        self.parent.canvas.coords(self.line, from_[0], from_[1], to_[0], to_[1])

        if (
            (self.connector_type == "on_exception_node")
            or (self.connector_type == "loop_node")
            or (
                self.connector_type == "next_node"
                and isinstance(self.from_nodegraph, IfElseNodeGraph)
            )
            or (self.connector_type == "else_node")
            or (
                self.connector_type == "next_node"
                and isinstance(self.from_nodegraph, LoopNodeGraph)
            )
            or (self.connector_type == "on_exception_node")
        ):
            self.parent.canvas.coords(
                self.text_rectangle,
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) - 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                - 10,
                ((self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2) + 20,
                (
                    (
                        (self.from_nodegraph.node.y + self.from_nodegraph.h)
                        + self.to_nodegraph.node.y
                    )
                    / 2
                )
                + 10,
            )
            self.parent.canvas.coords(
                self.text,
                (self.from_nodegraph.center_x + self.to_nodegraph.center_x) / 2,
                (
                    (self.from_nodegraph.node.y + self.from_nodegraph.h)
                    + self.to_nodegraph.node.y
                )
                / 2,
            )
