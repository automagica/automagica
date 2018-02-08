import os

from socketIO_client import SocketIO

from .auth import Auth
from .robot import Robot

def config():
    if not os.environ.get('AUTOMAGICA_ROBOT_ID'):
        automagica_robot_id = None
        while not automagica_robot_id:
            automagica_robot_id = input('Please provide the Automagica Robot ID: \n')
        os.environ['AUTOMAGICA_ROBOT_ID'] = automagica_robot_id
    if not os.environ.get('AUTOMAGICA_HOST'):
        automagica_host = input('Please provide the Automagica host (leave blank for https://automagica.io): \n')
        if not automagica_host:
            automagica_host = 'https://automagica.io'
        os.environ['AUTOMAGICA_HOST'] = automagica_host

def start():
    os.system('cls')
    config()
    print('Automagica Robot launched and waiting! Listening on port 7175 for commands.')
    socketIO = SocketIO(os.environ['AUTOMAGICA_HOST'], 7175)
    robot_namespace = socketIO.define(Robot, '/robot')
    socketIO.wait()


if __name__ == '__main__':
    start()
