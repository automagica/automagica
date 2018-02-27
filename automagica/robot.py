from time import sleep
from socketIO_client import BaseNamespace

from .activities import *

class Robot(BaseNamespace):
    robot_id = None

    def on_code(self, code):
        try:
            exec(code)
            self.emit('success', {'robot_id': self.robot_id, 'schedule_id': ''})
        except Exception as e:
            self.emit('failure', {'robot_id': self.robot_id, 'exception': str(e)})