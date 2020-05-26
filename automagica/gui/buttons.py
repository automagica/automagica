import os
import tkinter as tk
from tkinter import font, messagebox

from PIL import ImageTk

from automagica import config
from automagica.config import _
from automagica.gui.graphs import generate_icon


class Button(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Button font
        custom_font = font.Font(family=config.FONT, size=10, weight="bold")

        # Default button styling
        self.configure(
            bg=config.COLOR_0,
            fg=config.COLOR_1,
            font=custom_font,
            relief="flat",
            borderwidth=0,
            padx=5,
            pady=5,
            activebackground=config.COLOR_1,
            activeforeground=config.COLOR_0,
            highlightbackground=config.COLOR_0,
            highlightcolor=config.COLOR_1,
            highlightthickness=0,
        )

        # Allow overwriting style
        self.configure(**kwargs)


class LargeButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Larger button font
        custom_font = font.Font(family=config.FONT, size=12)

        # Override font size
        self.configure(font=custom_font)


class ToolbarImageButton(LargeButton):
    def __init__(self, *args, image_path="", **kwargs):
        super().__init__(*args, **kwargs)

        base_path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )
        icon_path = os.path.join(base_path, "icons", image_path)

        # Icon image
        self.icon_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color=config.COLOR_1, width=15, height=15)
        )

        self.configure(font=(config.FONT, 8), image=self.icon_img, compound="top")


class HelpButton(tk.Button):
    def __init__(self, *args, message="", **kwargs):
        super().__init__(*args, **kwargs)

        self.message = message

        base_path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )
        icon_path = os.path.join(base_path, "icons", "question-circle.png")

        self.icon_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color=config.COLOR_0)
        )

        self.configure(
            image=self.icon_img,
            command=self.clicked,
            relief=tk.FLAT,
            bg=self.master.cget("bg"),
            takefocus=False,
        )

    def clicked(self):
        messagebox.showinfo(_("Information"), self.message)
