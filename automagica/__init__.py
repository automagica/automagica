import os
import sys
from sty import bg, rs
from socketIO_client import SocketIO

from .auth import Auth
from .robot import Robot


def start():
    os.system('cls')

    if len(sys.argv) > 1:
        robot_id = sys.argv[1]
    else:
        robot_id = input('Please provide your Automagica Robot ID: \n')

    if len(sys.argv) > 2:
        host = sys.argv[2]
    else:
        host = 'automagica.be'

    if len(sys.argv) > 3:
        port = sys.argv[3]
    else:
        port = None

    print(bg.blue + 'Automagica Robot (' + robot_id +
          ') launched and waiting! Listening to ' + host + '.' + rs.bg)
    socketIO = SocketIO(host, port)
    robot_namespace = socketIO.define(Robot, '/robot')

    robot_namespace.emit('auth', {'robot_id' : robot_id})

    socketIO.wait()


if __name__ == '__main__':
    start()
