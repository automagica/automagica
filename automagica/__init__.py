import sys

from .activities import *

import argparse

parser = argparse.ArgumentParser(description='Automagica CLI')

parser.add_argument('script', type=str,
                    help='Script for the Automagica Bot')

parser.add_argument('--parameters', default='',
                    help='Parameters for the Automagica Bot')

def start():
    # Retrieve arguments
    args = parser.parse_args()
    # Run parameters first
    exec(args.parameters, globals())
    # Run script
    exec(args.script, globals())

if __name__ == '__main__':
    start()