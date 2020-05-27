import os
import tkinter as tk
from tkinter import font, messagebox

from PIL import ImageTk

from automagica import config
from automagica.config import _
from automagica.gui.graphs import generate_icon


class Button(tk.Button):
    """
    Default styled button
    """

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
    """
    Larger default button
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Larger button font
        custom_font = font.Font(family=config.FONT, size=12)

        # Override font size
        self.configure(font=custom_font)


class ToolbarImageButton(LargeButton):
    """
    Button with image, as used within the toolbar
    """

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

        # Override image and font size
        self.configure(font=(config.FONT, 8), image=self.icon_img, compound="top")


class HelpButton(tk.Button):
    """
    Help button which shows a pop-up information message on clicking it. 
    """

    def __init__(self, *args, message="", title="", **kwargs):
        super().__init__(*args, **kwargs)

        self.message = message

        if not title:
            title = _("Information")

        self.title = title

        base_path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )
        icon_path = os.path.join(base_path, "icons", "question-circle.png")

        self.icon_img = ImageTk.PhotoImage(
            generate_icon(icon_path, color=config.COLOR_0)
        )

        self.configure(
            image=self.icon_img,
            command=self.on_clicked,
            relief=tk.FLAT,
            bg=self.master.cget("bg"),  # Take parent's background
            takefocus=False,  # Do not include in 'TAB'-ing
        )

    def on_clicked(self):
        messagebox.showinfo(self.title, self.message)
