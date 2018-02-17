from time import sleep
from socketIO_client import BaseNamespace

from .activities import *

class Robot(BaseNamespace):
    def on_code(self, code):
        exec(code)
