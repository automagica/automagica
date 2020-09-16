"""Copyright 2020 Oakwood Technologies BVBA"""
import json
import os
import sys
from datetime import datetime
from subprocess import check_output
from time import sleep, time
from uuid import uuid4

from mss import mss

try:
    from win32api import (
        GetCursorPos,
        GetKeyState,
        GetSystemMetrics,
        OpenProcess,
    )
    from win32clipboard import CloseClipboard, GetClipboardData, OpenClipboard
    from win32con import PROCESS_QUERY_INFORMATION, PROCESS_VM_READ
    from win32gui import GetForegroundWindow, GetWindowText
    from win32process import GetModuleFileNameEx, GetWindowThreadProcessId
except ImportError:
    pass


class Capture:
    def __init__(self, name=""):
        # fmt: off
        self.virtual_keys = [(0x01, "left mouse click"), (0x02, "right mouse click"), (0x04, "middle mouse click"), (0x08, "backspace"), (0x09, "tab"), (0x0D, "enter"), (0x10, "shift"), (0x11, "ctrl"), (0x12, "alt"), (0x13, "pause"), (0x1B, "esc"), (0x20, " "), (0x21, "page up"), (0x22, "page down"), (0x23, "end"), (0x24, "home"), (0x25, "left"), (0x26, "up"), (0x27, "right"), (0x28, "down"), (0x2C, "printscreen"), (0x2D, "insert"), (0x2E, "delete"), (0x70, "f1"), (0x71, "f2"), (0x72, "f3"), (0x73, "f4"), (0x74, "f5"), (0x75, "f6"), (0x76, "f7"), (0x77, "f8"), (0x78, "f9"), (0x79, "f10"), (0x7A, "f11"), (0x7B, "f12"), (0x30, "0"), (0x31, "1"), (0x32, "2"), (0x33, "3"), (0x34, "4"), (0x35, "5"), (0x36, "6"), (0x37, "7"), (0x38, "8"), (0x39, "9"), (0x41, "a"), (0x42, "b"), (0x43, "c"), (0x44, "d"), (0x45, "e"), (0x46, "f"), (0x47, "g"), (0x48, "h"), (0x49, "i"), (0x4A, "j"), (0x4B, "k"), (0x4C, "l"), (0x4D, "m"), (0x4E, "n"), (0x4F, "o"), (0x50, "p"), (0x51, "q"), (0x52, "r"), (0x53, "s"), (0x54, "t"), (0x55, "u"), (0x56, "v"), (0x57, "w"), (0x58, "x"), (0x59, "y"), (0x5A, "z"), (0xBE, ".")]
        self.letters = [" ",".","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","u","z"]
        # fmt: on

        # Set initial state
        self.states = self.get_key_states()
        self.letter_sequence = ""
        self.typing = False
        self.clipboard = self.get_clipboard()

        self.name = name

        if not name:
            self.name = "Recording " + datetime.now().strftime("%Y%m%d-%H%M%S")

        os.makedirs("recordings", exist_ok=True)
        os.makedirs("recordings/{}".format(self.name))
        os.makedirs("recordings/{}/screenshots".format(self.name))

        self.machine_id = self.get_machine_id()

    def get_key_states(self):
        return [
            GetKeyState(virtual_key[0]) for virtual_key in self.virtual_keys
        ]

    def get_machine_id(self):
        return (
            check_output("wmic csproduct get uuid")
            .decode()
            .split("\n")[1]
            .strip()
        )

    def get_current_foreground_app_process_name(self):
        try:
            hwnd = GetForegroundWindow()
            pid = GetWindowThreadProcessId(hwnd)
            handle = OpenProcess(
                PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid[1],
            )
            path = GetModuleFileNameEx(handle, 0)
            name = path.split("\\")[-1]
            return name
        except:
            return None

    def get_current_foreground_app_title(self):
        try:
            hwnd = GetForegroundWindow()
            title = GetWindowText(hwnd)
            return title
        except:
            return None

    def log(self, event, content=None):
        uid = str(uuid4())

        with mss() as sht:
            fn = "recordings/{}/screenshots/{}.png".format(self.name, uid)
            sht.shot(mon=-1, output=fn)

        data = {
            "uid": uid,
            "machine_id": self.machine_id,
            "timestamp": time(),
            "mouse_x": GetCursorPos()[0],
            "mouse_y": GetCursorPos()[1],
            "screen_res_x": GetSystemMetrics(0),
            "screen_res_y": GetSystemMetrics(1),
            "foreground_app_process": self.get_current_foreground_app_process_name(),
            "foreground_app_title": self.get_current_foreground_app_title(),
            "event": event,
        }

        if content:
            data["content"] = content

        with open("recordings/{}/actions.json".format(self.name), "a") as f:
            f.write(json.dumps(data) + "\n")

    def get_clipboard(self):

        try:
            OpenClipboard()
            clipboard = GetClipboardData()
            CloseClipboard()

            return clipboard

        except:
            return ""

    def record(self):
        i = 0

        while True:
            if GetCursorPos() == (0, 0):
                break

            new_states = self.get_key_states()

            for state, new_state, virtual_key in zip(
                self.states, new_states, self.virtual_keys
            ):
                if state != new_state:
                    if state < 0:
                        if virtual_key[1] not in self.letters:
                            self.log(virtual_key[1])
                    else:
                        if virtual_key[1] in self.letters:
                            self.letter_sequence += virtual_key[1]
                            typing = True
                        else:
                            typing = False

                        if len(self.letter_sequence) > 2 and not typing:
                            self.log("typing", content=self.letter_sequence)
                            self.letter_sequence = ""
                            typing = False

            if i == 100:
                new_clipboard = self.get_clipboard()

                if self.clipboard != new_clipboard:
                    self.log("clipboard", content=new_clipboard)
                    self.clipboard = new_clipboard

                i = 0

            self.states = new_states

            sleep(0.01)

            i += 1

    def convert(self, format_):
        if format_ == "python":
            return self.to_python()

        if format_ == "html":
            return self.to_html()

    def convert_to_python(self):
        code = []

        code.append("from automagica import *")

        code.append("")

        for i, action in enumerate(self.actions):
            # Do we need to wait?
            if i > 0:
                delay = action["timestamp"] - self.actions[i - 1]["timestamp"]
                code.append("wait({})".format(round(delay, 1)))

            # What to do?
            if action["event"] == "left mouse click":
                code.append(
                    "click({}, {})".format(
                        action["mouse_x"], action["mouse_y"]
                    )
                )

            if action["event"] == "right mouse click":
                code.append(
                    "right_click({}, {})".format(
                        action["mouse_x"], action["mouse_y"]
                    )
                )

            if action["event"] == "typing":
                code.append('type_text("{}")'.format(action["content"]))

            code.append("")

        return code

    def convert_to_html(self):
        html = "<html><body>"

        for i, action in enumerate(self.actions):
            # Do we need to wait?
            if i > 0:
                delay = action["timestamp"] - self.actions[i - 1]["timestamp"]
                html += "<p>wait {} seconds</p>".format(round(delay, 1))

            # What to do?
            if action["event"] == "left mouse click":
                # Find button or element
                img = Image.open(
                    "recordings/{}/screenshots/{}.png".format(
                        self.name, action["uid"]
                    )
                )

                left = action["mouse_x"] - 50
                top = action["mouse_y"] - 50
                right = action["mouse_x"] + 50
                bottom = action["mouse_y"] - 50

                element = img.crop((left, top, right, bottom))

                pass

            if action["event"] == "right mouse click":
                # Find button or element
                pass

            if action["event"] == "typing":
                # Run diff between before and after typing (screenshot last action and typing finish action)
                pass

        html += "</body></html>"
