from socketIO_client import BaseNamespace


class Robot(BaseNamespace):
    def on_code(self, code):
        exec(code)
