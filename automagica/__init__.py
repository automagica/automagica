import sys

from .activities import *

def start():
    exec(sys.argv[1], globals())
    
if __name__ == '__main__':
    start()