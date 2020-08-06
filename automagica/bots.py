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

    def runcode(self, code):
        try:
            exec(code, self.locals)
            return True

        except SystemExit:
            raise
        except:
            self.showtraceback()

        return False


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

        self._running = True

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

        except:
            pass

        while self._running:
            try:
                command, on_done, on_fail = queue.get(timeout=1)

            except Empty:
                command = None
                on_done = None
                on_fail = None

            if command:
                self._run_command(command, on_done=on_done, on_fail=on_fail)

            else:
                sleep(0.1)

    def _run_command(
        self, command, on_done=None, on_fail=None,
    ):
        from io import StringIO

        succesful = False

        with StringIO() as temp:
            old_stdout = sys.stdout  # Keep reference to old stdout

            sys.stdout = temp  # Redirect stdout to temp

            try:
                succesful = self.interpreter.runcode(command)
            except:
                self.logger.error("Unknown error occured.")

            sys.stdout = old_stdout  # Redirect to old stdout

            temp.seek(0)  # Go back to start

            stdout = temp.read().strip()

            if stdout:
                self.logger.info(stdout)

        if succesful:
            if on_done:
                on_done()
        else:
            if on_fail:
                on_fail()

    def reset(self):
        self.interpreter.locals = {"__name__": "__console__", "__doc__": None}

    def run(self, command, on_done=None, on_fail=None):
        self.logger.info(
            "\n".join([">>> " + line for line in command.split("\n") if line.strip()])
        )

        self.command_queue.put((command, on_done, on_fail))

    def stop(self):
        self._running = False
