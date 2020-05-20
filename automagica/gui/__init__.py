import logging
import os
import tkinter as tk
from tkinter import font

from .windows import FlowDesignerWindow, FlowPlayerWindow, TrayIcon
from ..models.bots import ThreadedBot
from ..models.flow import Flow

import tkinter


class FlowApp(tkinter.Tk):
    def __init__(
        self,
        *args,
        bot=None,
        file_path=None,
        run=False,
        headless=False,
        step_by_step=False,
        **kwargs
    ):

        super().__init__(*args, **kwargs)

        self.withdraw()

        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "automagica.ico",
        )

        from PIL import ImageTk, Image

        self.tk.call(
            "wm", "iconphoto", self._w, ImageTk.PhotoImage(Image.open(icon_path))
        )

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("automagica.flow")

        if not bot:
            bot = ThreadedBot()
        self.bot = bot

        if file_path:
            if run:
                self.run_flow(file_path, headless, step_by_step)
            else:
                self.open_flow(file_path)
        else:
            self.new_flow()

        # Run sounds better, right?
        self.run = self.mainloop

    def new_flow(self):
        _ = FlowDesignerWindow(self, bot=self.bot)

    def open_flow(self, file_path):
        _ = FlowDesignerWindow(self, bot=self.bot, flow=Flow(file_path))

    def run_flow(self, file_path, headless, step_by_step):
        _ = FlowPlayerWindow(
            self,
            flow=Flow(file_path),
            bot=self.bot,
            autoplay=True,
            step_by_step=step_by_step,
            autoclose=True,
            on_close=self.quit,
        )

    def report_callback_exception(self, exception, value, traceback):
        self.logger.exception(exception)


class TrayApp(tkinter.Tk):
    def __init__(self, *args, bot=None, file_path=None, run=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()
        _ = TrayIcon(self)

        # Run sounds better :-)
        self.run = self.mainloop


def style_button(button, font_size=10):
    from tkinter import font

    button.config(
        fg="white",
        bg="#1B97F3",
        activebackground="#0069c0",
        activeforeground="white",
        borderwidth=0,
        padx=5,
        pady=5,
    )

    custom_font = font.Font(family="Helvetica", size=font_size)

    button["font"] = custom_font

    return button


class RecorderWindow(tk.Tk):
    def __init__(self, width, height, resizable=False):
        super().__init__()

        # Hide the frame
        self.withdraw()

        # Configuratiions
        self.configure(bg="white")
        self.title("Automagica Wand")

        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "automagica.ico",
        )

        # Windows
        if "nt" in os.name:
            self.iconbitmap(icon_path)

        self.option_add("*Font", "Helvetica")

        # Center on screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.geometry("{}x{}+{}+{}".format(width, height, x, y))

        if not resizable:
            self.resizable(width=False, height=False)

        # Render the frame
        self.update()
        self.deiconify()


class ImageButton(tk.Button):
    def __init__(self, parent, fn):
        self.img = tk.PhotoImage(file=fn)
        super().__init__(parent, image=self.img, bd=0)
