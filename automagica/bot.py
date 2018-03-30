from time import sleep
from socketIO_client import BaseNamespace
from .activities import *

class Bot(BaseNamespace):
    bot_id = None

    def on_run(self, data):
        try:
            print('Received job #' + str(data['job_id']))
            exec(data['code'])
            print('Finished job #' + str(data['job_id']) +' successfully.')
            self.emit('finish', {'type': 'success', 'bot_id': self.bot_id, 'job_id': data['job_id']})
        except Exception as e:
            print('Failed job #' + str(data['job_id']))
            print('Exception: ' + str(e))
            self.emit('finish', {'type': 'failure', 'bot_id': self.bot_id, 'job_id': data['job_id'], 'exception': str(e)})

    def on_connect(self):
        self.emit('auth', {'bot_id' : self.bot_id})
        print('Connected!')

    def on_disconnect(self):
        print('Disconnected!')

    def on_reconnect(self):
        self.emit('auth', {'bot_id' : self.bot_id})
        print('Reconnected!')