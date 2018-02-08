import os

from socketIO_client import SocketIO

from .auth import Auth
from .robot import Robot


def start():
    os.system('cls')
    print('Automagica Robot launched and waiting!')
    socketIO = SocketIO('localhost', 8000)
    robot_namespace = socketIO.define(Robot, '/robot')
    socketIO.wait()


if __name__ == '__main__':
    start()
