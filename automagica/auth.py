from socketIO_client import BaseNamespace
import os


class Auth(BaseNamespace):
    def on_connect(self):
        self.emit('auth', os.environ['AUTOMAGICA_ROBOT_ID'])
