import sys

from .activities import *

import argparse

parser = argparse.ArgumentParser(description='Automagica CLI')

parser.add_argument('-f', '--file', default='',
                    type=str, help='Path to script file')

parser.add_argument('-s', '--script', default='', type=str,
                    help='Script string for the Automagica Bot (if no --file not specified)')

parser.add_argument('-p', '--parameters', default='', type=str,
                    help='Parameters string for the Automagica Bot')


def start():
    # Retrieve arguments
    args = parser.parse_args()

    # Run parameters first
    exec(args.parameters, globals())

    # Was a file specified?
    if args.file:
        with open(args.file) as f:
            script = f.read()
    else:
        script = args.script

    # Run script
    exec(script, globals())


if __name__ == '__main__':
    start()
