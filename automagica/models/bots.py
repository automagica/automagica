import code
import logging
import os
import sys
from threading import Thread


class ConsoleHandler(logging.Handler):
    def __init__(self, write_handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.write_handler = write_handler

    def emit(self, record):
        self.write_handler(record)


class ModifiedInterpreter(code.InteractiveInterpreter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("automagica.bot")
        self.logger.setLevel(logging.INFO)

    def write(self, output):
        self.logger.error(output)


class Bot:
    def __init__(self, locals_=None):
        self.locals_ = locals_
        self.logger = logging.getLogger("automagica.bot")

    def run(self, command, on_done=None):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError


class ThreadedBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interpreter = ModifiedInterpreter(locals=self.locals_)

    def run_thread_target(self, command, on_done=None):
        from io import StringIO

        with StringIO() as temp:
            old_stdout = sys.stdout  # Keep reference to old stdout

            sys.stdout = temp  # Redirect stdout to temp

            self.interpreter.runcode(command)

            sys.stdout = old_stdout  # Redirect to old stdout

            temp.seek(0)  # Go back to start

            stdout = temp.read().strip()

            if stdout:
                self.logger.info(stdout)

        if on_done:
            on_done()

    def reset(self):
        self.interpreter.locals = {"__name__": "__console__", "__doc__": None}

    def run(self, command, on_done=None):
        self.logger.info(
            "\n".join([">>> " + line for line in command.split("\n") if line.strip()])
        )

        t = Thread(target=self.run_thread_target, args=(command, on_done))
        t.start()

    def stop(self):
        pass
