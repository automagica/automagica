from time import sleep
from socketIO_client import BaseNamespace

from .activities import *

class Bot(BaseNamespace):
    bot_id = None

    def on_code(self, code):
        try:
            exec(code)
            self.emit('success', {'bot_id': self.bot_id, 'schedule_id': ''})
        except Exception as e:
            self.emit('failure', {'bot_id': self.bot_id, 'exception': str(e)})