from time import sleep
from socketIO_client import BaseNamespace

from activities import TypeInto, ClickOnImage, ClickOnPosition


class Robot(BaseNamespace):
    def on_code(self, code):
        exec(code)
