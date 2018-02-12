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
        port = 7175

    print(bg.blue + 'Automagica Robot (' + robot_id +
          ') launched and waiting! Listening to ' + host + ' on port ' + str(port) +'.' + rs.bg)
    socketIO = SocketIO(host, 7175)
    robot_namespace = socketIO.define(Robot, '/robot')
    socketIO.wait()


if __name__ == '__main__':
    start()
