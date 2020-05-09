import tkinter as tk
from tkinter import font
from PIL import ImageTk
from automagica import config
from automagica.config import _


class Button(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        custom_font = font.Font(family=config.FONT, size=10, weight="bold")

        self.configure(
            bg=config.COLOR_0,
            fg=config.COLOR_1,
            font=custom_font,
            relief="flat",
            borderwidth=0,
            padx=5,
            pady=5,
            highlightbackground=config.COLOR_0,
            highlightcolor=config.COLOR_1,
            highlightthickness=0,
        )

        self.configure(**kwargs)


class LargeButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        custom_font = font.Font(family=config.FONT, size=12)
        self.configure(font=custom_font, relief="flat")


class ToolbarImageButton(LargeButton):
    def __init__(self, *args, image_path="", **kwargs):
        super().__init__(*args, **kwargs)
        from .graphs import generate_icon

        self.image_path = image_path

        self.icon_img = ImageTk.PhotoImage(
            generate_icon(self.image_path, color=config.COLOR_1, width=15, height=15)
        )
        self.configure(font=(config.FONT, 8), image=self.icon_img, compound="top")


class HelpButton(tk.Button):
    def __init__(self, *args, message="", **kwargs):
        super().__init__(*args, **kwargs)

        from .graphs import generate_icon

        self.message = message
        self.icon_img = ImageTk.PhotoImage(
            generate_icon("gui/icons/question-circle.png", color=config.COLOR_0)
        )

        self.configure(image=self.icon_img, command=self.clicked, relief=tk.FLAT)

    def clicked(self):
        from tkinter import messagebox

        messagebox.showinfo(_("Information"), self.message)
