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

        import queue

        self.command_queue = queue.Queue()

        t = Thread(target=self.bot_thread, args=(self.command_queue,))
        t.start()

    def bot_thread(self, queue):
        from time import sleep
        from queue import Empty

        try:
            import pythoncom

            # Required for win32com
            pythoncom.CoInitialize()

        except:  # TODO: not very elegant way, but this is required for Linux/MacOSX as pythoncom obviously is not supported on those platforms
            pass

        while True:
            try:
                command, on_done, return_value_when_done = queue.get(timeout=1)
            except Empty:
                command = None
                on_done = None
                return_value_when_done = False

            if command:
                self._run_command(
                    command,
                    on_done=on_done,
                    return_value_when_done=return_value_when_done,
                )
            else:
                sleep(0.1)

    def _run_command(self, command, on_done=None, return_value_when_done=False):
        from io import StringIO

        with StringIO() as temp:
            old_stdout = sys.stdout  # Keep reference to old stdout

            sys.stdout = temp  # Redirect stdout to temp

            if return_value_when_done:
                command = "AUTOMAGICA_RETURN_VALUE = (" + command + ")"

            self.interpreter.runcode(command)

            sys.stdout = old_stdout  # Redirect to old stdout

            temp.seek(0)  # Go back to start

            stdout = temp.read().strip()

            if stdout:
                self.logger.info(stdout)

        if on_done:
            if return_value_when_done:
                return_value = self.interpreter.locals.get("AUTOMAGICA_RETURN_VALUE")
                on_done(return_value=return_value)
            else:
                on_done()

    def reset(self):
        self.interpreter.locals = {"__name__": "__console__", "__doc__": None}

    def run(self, command, on_done=None, return_value_when_done=False):
        self.logger.info(
            "\n".join([">>> " + line for line in command.split("\n") if line.strip()])
        )

        self.command_queue.put((command, on_done, return_value_when_done))

    def stop(self):
        pass
