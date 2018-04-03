import os
import sys
from socketIO_client import SocketIO

from .auth import Auth
from .bot import Bot
from .activities import *


def start():
    os.system('cls')

    if len(sys.argv) > 1:
        bot_id = sys.argv[1]
    else:
        bot_id = input('Please provide your Automagica Bot ID: \n')

    if len(sys.argv) > 2:
        host = sys.argv[2]
    else:
        host = 'https://portal.automagica.be'

    if len(sys.argv) > 3:
        port = sys.argv[3]
    else:
        port = None

    
    socketIO = SocketIO(host, port)
    bot = Bot
    bot.bot_id = bot_id
    
    while True:
        try:
            bot_namespace = socketIO.define(bot, '/bot')
            break
        except:
            os.system('cls')
            print('Connecting...')
            pass
    
    socketIO.wait()
    
if __name__ == '__main__':
    start()
