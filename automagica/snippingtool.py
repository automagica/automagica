class SnippingTool():
    def __init__(self, image, info=''):
        """
        Starts a full screen snipping tool for selecting coordinates
        """
        import tkinter as tk
        from tkinter.font import Font
        from PIL import ImageTk

        self.root = tk.Tk()

        self.root.bind("<Escape>", self._quit)

        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()

        # Change window to size of full screen
        self.root.geometry("{}x{}".format(w, h))

        # Bring window to full screen and top most level
        self.root.attributes('-fullscreen', True)
        self.root.attributes("-topmost", True)

        # Keep reference of some things
        self.x = self.y = 0
        self.rect = None
        self.start_x = None
        self.start_y = None

        # Create the canvas
        self.canvas = tk.Canvas(
            self.root,
            width=w,
            height=h,
            cursor="crosshair")

        self.canvas.pack()

        # Add the screenshot
        img = ImageTk.PhotoImage(image, master=self.root)

        self.canvas.create_image(
            (0, 0), image=img, anchor="nw")

        # Connect the event handlers
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        if info:
            font = Font(family='Helvetica', size=30)

            self.canvas.create_text(
                int(w/2), int(h*2/3), text=info, fill='#1B97F3', font=font
            )

        self.root.mainloop()

    def _quit(self):
        self.root.destroy()

    def on_button_press(self, event):
        # Update coordinates
        self.start_x = event.x
        self.start_y = event.y

        # If no rectangle is drawn yet, draw one
        if not self.rect:
            self.rect = self.canvas.create_rectangle(
                self.x, self.y, 1, 1, outline="#1B97F3",
                fill="#1B97F3", stipple="gray12")

    def on_move_press(self, event):
        # Update coordinates
        self.end_x, self.end_y = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x,
                           self.start_y, self.end_x, self.end_y)

    def on_button_release(self, event):
        # Update global variable
        global coordinates

        coordinates = (
            min(self.start_x, self.end_x),
            min(self.start_y, self.end_y),
            max(self.start_x, self.end_x),
            max(self.start_y, self.end_y)
        )

        # Close the window
        self.root.quit()
        self.root.destroy()


def get_screen():
    """
    Captures the screen to a Pillow Image object
    """
    from PIL import Image
    import mss

    with mss.mss() as sct:

        # Find primary monitor
        for monitor in sct.monitors:
            if monitor["left"] == 0 and monitor["top"] == 0:
                break

        sct_img = sct.grab(monitor)

    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

    return img


def select_rect(screenshot, info=''):
    """
    Presents the user with a window which allows him/her to select
    a rectangle on the screen and returns the coordinates in the carthesian
    coordinate system
    """
    global coordinates

    try:
        SnippingTool(screenshot, info=info)
        return coordinates

    except KeyboardInterrupt:
        return None
