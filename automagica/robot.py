from time import sleep

from pyautogui import click, hotkey, moveTo, typewrite
from socketIO_client import BaseNamespace


class Robot(BaseNamespace):
    def on_code(self, code):
        exec(code)
