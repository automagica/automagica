from socketIO_client import BaseNamespace


class Auth(BaseNamespace):
    def on_connect(self):
        self.emit('auth', 'robot')
