import os
import tkinter as tk
import webbrowser
from time import sleep

import PIL.ImageTk as pil_tk
import pyperclip

from .gui import ImageButton, RecorderWindow, style_button
from .snippingtool import get_screen, select_rect


"""
TODO
- Add middle click
- Add hover
"""


def activity_selection_window():
    window = RecorderWindow(67 * 10, 80)

    def select_action(action):
        window.destroy()
        sleep(0.5)
        screenshot = get_screen()
        target = select_rect(
            screenshot, info="Drag a box around the element on the screen"
        )
        add_anchors_window(screenshot, target, action)

    actions_grp = tk.LabelFrame(window, text="Actions", bg="white")

    icons_path = os.path.join(
        os.path.abspath(__file__).replace("recorder.py", ""), "icons"
    )

    click_btn = ImageButton(actions_grp, os.path.join(icons_path, "click_button.png"))
    click_btn.config(command=lambda: select_action('click("'))
    click_btn.pack(side=tk.LEFT)

    doubleclick_btn = ImageButton(
        actions_grp, os.path.join(icons_path, "double_click_button.png")
    )
    doubleclick_btn.config(command=lambda: select_action('double_click("'))
    doubleclick_btn.pack(side=tk.LEFT)

    right_click_btn = ImageButton(
        actions_grp, os.path.join(icons_path, "right_click_button.png")
    )
    right_click_btn.pack(side=tk.LEFT)
    right_click_btn.config(command=lambda: select_action('right_click("'))

    middle_click_btn = ImageButton(
        actions_grp, os.path.join(icons_path, "middle_click_button.png")
    )
    middle_click_btn.pack(side=tk.LEFT)
    middle_click_btn.config(command=lambda: select_action('middle_click("'))

    move_to_btn = ImageButton(
        actions_grp, os.path.join(icons_path, "move_to_button.png")
    )
    move_to_btn.pack(side=tk.LEFT)
    move_to_btn.config(command=lambda: select_action('move_mouse_to("'))

    type_into_btn = ImageButton(
        actions_grp, os.path.join(icons_path, "type_into_button.png")
    )
    type_into_btn.pack(side=tk.LEFT)
    type_into_btn.config(command=lambda: select_action('typing("Sample text", "'))

    actions_grp.pack(side=tk.LEFT)

    interpret_grp = tk.LabelFrame(window, text="Interpret", bg="white")

    read_text_btn = ImageButton(
        interpret_grp, os.path.join(icons_path, "read_text_button.png")
    )
    read_text_btn.pack(side=tk.LEFT)
    read_text_btn.config(command=lambda: select_action('read_text("'))

    is_visible_btn = ImageButton(
        interpret_grp, os.path.join(icons_path, "is_visible_button.png")
    )
    is_visible_btn.pack(side=tk.LEFT)
    is_visible_btn.config(command=lambda: select_action('is_visible("'))

    interpret_grp.pack(side=tk.LEFT)

    wait_grp = tk.LabelFrame(window, text="Wait", bg="white")

    wait_appear_btn = ImageButton(
        wait_grp, os.path.join(icons_path, "wait_appear_button.png")
    )
    wait_appear_btn.pack(side=tk.LEFT)
    wait_appear_btn.config(command=lambda: select_action('wait_appear("'))

    wait_vanish_btn = ImageButton(
        wait_grp, os.path.join(icons_path, "wait_vanish_button.png")
    )
    wait_vanish_btn.pack(side=tk.LEFT)
    wait_vanish_btn.config(command=lambda: select_action('wait_vanish("'))

    wait_grp.pack(side=tk.LEFT)

    tk.mainloop()


def add_anchors_window(screenshot, target, action):
    window = RecorderWindow(800, 750, resizable=True)

    target_frame = tk.LabelFrame(window, text="Target", bg="white")
    target_frame.grid(row=2, column=0, sticky="ewns", pady=10, padx=10)

    def resize_to_fit(image, fit_w, fit_h):
        w, h = image.size

        if w >= h:
            image = image.resize((fit_w, int(h / w * fit_w)))
            factor = fit_w / w
        else:
            image = image.resize(((int(w / h * fit_h), fit_h)))
            factor = fit_h / h

        return image, factor

    target_image, _ = resize_to_fit(screenshot.crop(target), 156, 156)

    target_img = pil_tk.PhotoImage(target_image)
    target_image_frame = tk.Frame(
        target_frame,
        highlightbackground="red",
        highlightcolor="red",
        highlightthickness=4,
        bd=0,
    )
    target_image_frame.pack()
    target_label = tk.Label(target_image_frame, image=target_img)
    target_label.pack()

    anchors_frame = tk.LabelFrame(window, text="Anchors", bg="white", padx=10, pady=10)

    anchors_content_lbl = tk.Label(
        anchors_frame,
        text="Add anchors to make the element detection more reliable.",
        bg="white",
    )
    anchors_content_lbl.pack()
    anchors_frame.grid(row=2, column=1, sticky="ewns", pady=10, padx=10)

    minimap_frame = tk.LabelFrame(window, text="Screenshot", bg="white")
    minimap_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    sshot_img, factor = resize_to_fit(screenshot, 192 * 4, 108 * 4)

    screenshot_canvas = tk.Canvas(minimap_frame, width=192 * 4, height=108 * 4)
    screenshot_canvas.pack()
    screenshot_img = pil_tk.PhotoImage(sshot_img)
    screenshot_canvas.create_image((0, 0), image=screenshot_img, anchor="nw")
    screenshot_canvas.create_rectangle(
        int(target[0] * factor),
        int(target[1] * factor),
        int(target[2] * factor),
        int(target[3] * factor),
        outline="red",
        width=2,
    )

    anchors = []

    anchor_imgs = []

    def add_anchor():
        anchor = select_rect(screenshot, info="Select an anchor on the screen")
        anchors.append(anchor)

        anchor_image = screenshot.crop(anchor)
        anchor_image, _ = resize_to_fit(anchor_image, 128, 128)

        anchor_frame = tk.Frame(
            anchors_frame,
            highlightbackground="green",
            highlightcolor="green",
            highlightthickness=4,
            bd=0,
        )
        anchor_frame.pack(side="left")
        anchor_img = pil_tk.PhotoImage(anchor_image)
        anchor_lbl = tk.Label(anchor_frame, image=anchor_img)
        anchor_lbl.pack()
        anchor_imgs.append(anchor_img)

        screenshot_canvas.create_rectangle(
            int(anchor[0] * factor),
            int(anchor[1] * factor),
            int(anchor[2] * factor),
            int(anchor[3] * factor),
            outline="green",
            width=2,
        )

        if len(anchors) == 3:
            add_anchor_btn.pack_forget()

    add_anchor_btn = tk.Button(anchors_frame, text="Add anchor", command=add_anchor)
    style_button(add_anchor_btn)
    add_anchor_btn.pack()

    def save():
        window.destroy()

        import json

        config_path = os.path.join(os.path.expanduser("~"), "automagica.json")

        def save_config(config):
            with open(config_path, "w") as f:
                json.dump(config, f)

        try:
            with open(config_path, "r") as f:
                config = json.load(f)

        except FileNotFoundError:
            config = {}
            save_config(config)

        if not config.get("accepted_recorder_terms"):
            from tkinter import messagebox

            accept_terms_window = tk.Tk()
            accept_terms_window.withdraw()
            accepted = messagebox.askyesno(
                "Important",
                "By continuing, the information you provided in the previous steps will be uploaded to Automagica's Vision service. You can find the full terms on https://portal.automagica.com/tos. Do you accept the terms? You will only be prompted once on this machine.",
                parent=accept_terms_window,
            )

            if not accepted:
                accept_terms_window.quit()
                accept_terms_window.destroy()
                return
            else:
                config["accepted_recorder_terms"] = True
                save_config(config)

        import requests
        import base64
        from io import BytesIO

        buffered = BytesIO()
        screenshot.save(buffered, format="PNG")
        image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        data = {
            "api_key": "sample",
            "image_base64": image_base64,
            "anchors": anchors,
            "target": target,
        }

        url = (
            os.environ.get("AUTOMAGICA_VISION_URL", "https://vision.automagica.com")
            + "/train/element"
        )

        r = requests.post(url, json=data)

        try:
            data = r.json()
        except:
            print(url)
            print(r.content)

        if data.get("sample_id"):
            element_id = data["sample_id"]
            snippet_window(action, element_id)
        else:
            try:
                tk.messagebox.showerror("Error", data["error"])
            except:
                tk.messagebox.showerror("Unknown error", data)

    def reset():
        window.destroy()
        activity_selection_window()

    reset_btn = tk.Button(window, text="Back", command=reset)
    style_button(reset_btn, font_size=15)
    reset_btn.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    save_btn = tk.Button(window, text="Next", command=save)
    style_button(save_btn, font_size=15)
    save_btn.grid(row=0, column=1, sticky="e", padx=10, pady=10)

    window.mainloop()


def snippet_window(activity, element_id):
    window = RecorderWindow(550, 190)

    snippet_lbl = tk.Label(window, text="Python code snippet", bg="white")
    snippet_lbl.grid(row=0, column=0)

    snippet_input = tk.Text(window, height=6, width=60)
    snippet_input.grid(row=1, column=0, sticky="ew")
    url = "{}/{}".format(
        os.environ.get("AUTOMAGICA_ID_URL", "https://automagica.id"), element_id
    )
    snippet = 'from automagica import *\n\n# {}\n{}{}")'.format(
        url, activity, element_id
    )
    snippet_input.insert(tk.END, snippet)
    snippet_input.config(state=tk.DISABLED)
    snippet_input.configure(font=("Consolas", 12))

    buttons_frame = tk.Frame(window, bg="white")
    buttons_frame.grid(row=3, column=0)

    copy_snippet_to_clipboard_btn = tk.Button(
        buttons_frame,
        text="Copy to clipboard",
        command=lambda: pyperclip.copy(snippet),
        anchor="w",
    )
    style_button(copy_snippet_to_clipboard_btn)
    copy_snippet_to_clipboard_btn.pack(side="left", pady=10, padx=10)

    view_btn = tk.Button(
        buttons_frame,
        text="Show element",
        command=lambda: webbrowser.open(url),
        anchor="w",
    )
    style_button(view_btn)
    view_btn.pack(side="left", pady=10, padx=10)

    def record_another():
        window.destroy()
        activity_selection_window()

    record_another_btn = tk.Button(
        buttons_frame, text="Record another element", command=record_another, anchor="w"
    )
    style_button(record_another_btn)
    record_another_btn.pack(side="left", pady=10, padx=10)

    window.mainloop()


def recorder():
    from threading import Thread

    print("Launching Automagica Recorder")

    t = Thread(target=activity_selection_window)

    t.start()


if __name__ == "__main__":
    recorder()
