import logging
import os
import platform
import subprocess
import sys
import tkinter as tk
from threading import Thread
from time import sleep

import requests
from PIL import Image, ImageTk

from automagica.bots import ThreadedBot
from automagica.config import Config
from automagica.flow import Flow
from automagica.gui.windows import (BotTrayWindow, FlowDesignerWindow,
                                    FlowPlayerWindow, Notification, WandWindow)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FlowApp(App):
    def __init__(
        self,
        *args,
        bot=None,
        file_path=None,
        run=False,
        headless=False,
        step_by_step=False,
        **kwargs,
    ):

        super().__init__(*args, **kwargs)

        self.withdraw()

        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "automagica.ico",
        )

        self.tk.call(
            "wm", "iconphoto", self._w, ImageTk.PhotoImage(Image.open(icon_path))
        )

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("automagica.flow")

        if not bot:
            bot = ThreadedBot()
        self.bot = bot

        if file_path:
            if run:
                self.run_flow(file_path, headless, step_by_step)
            else:
                self.open_flow(file_path)
        else:
            self.new_flow()

        # Run sounds better, right?
        self.run = self.mainloop

    def close_app(self):
        self.bot.stop()
        self.quit()
        self.destroy()

    def new_flow(self):
        FlowDesignerWindow(self, bot=self.bot)

    def open_flow(self, file_path):
        FlowDesignerWindow(self, bot=self.bot, flow=Flow(file_path))

    def run_flow(self, file_path, headless, step_by_step):
        FlowPlayerWindow(
            self,
            flow=Flow(file_path),
            bot=self.bot,
            autoplay=True,
            step_by_step=step_by_step,
            autoclose=True,
            on_close=self.quit,
        )

    def report_callback_exception(self, exception, value, traceback):
        self.logger.exception(exception)

        import requests


class BotApp(App):
    def __init__(self, *args, bot=None, file_path=None, config=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        self.config = config

        if not self.config:
            self.config = Config().config

        self.url = self.config["portal_url"]

        # Tray application
        _ = BotTrayWindow(self)

        # Runner Thread (polling Automagica Portal for jobs)
        self.runner_thread = Thread(target=self._runner_thread)
        self.runner_thread.start()

        # Alive Thread (polling Automagica Portal for health status)
        self.alive_thread = Thread(target=self._alive_thread)
        self.alive_thread.start()

        # Run sounds better :-)
        self.run = self.mainloop

    def execute_notebook(self, notebook):
        print(notebook)

    def execute_script(self, script):
        print(script)

    def execute_flow(self, flow):
        print(flow)

    def _alive_thread(self, interval=30):
        headers = {"bot_secret": self.config["bot_secret"]}

        while True:
            try:
                _ = requests.post(self.url + "/api/bot/alive", headers=headers)
                logging.info("Sent alive to Automagica Portal.")
            except:
                logging.exception("Could not reach Automagica Portal.")

            sleep(interval)

    def _runner_thread(self, interval=10, retry_interval=5 * 60):
        headers = {"bot_secret": self.config["bot_secret"]}

        Notification(self, message="Bot started")

        while True:
            # Get next job

            try:
                r = requests.get(self.url + "/api/job/next", headers=headers)
                job = r.json()

                # We got a job!
                if job:
                    logging.info("Received job {}".format(job["job_id"]))

                    headers = {
                        "process_id": job["process_id"],
                        "process_version_id": job.get("process_version_id"),
                        "bot_secret": self.config["bot_secret"],
                    }

                    # Retrieve process
                    r = requests.get(self.url + "/api/process", headers=headers)

                    # Download process files

                    try:
                        # Run
                        job["status"] = "completed"
                        logging.exception("Completed job {}".format(job["job_id"]))

                    except:
                        job["status"] = "failed"
                        logging.exception("Failed job {}".format(job["job_id"]))

                    headers = {
                        "bot_secret": self.config["bot_secret"],
                        "job_id": job["job_id"],
                        "job_status": job["status"],
                    }

                # We did not get a job!
                else:
                    sleep(interval)

            except:
                logging.exception(
                    f"Could not reach Automagica Portal. Waiting {interval} second(s) before retrying."
                )
                sleep(interval)


class WandApp(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        _ = WandWindow(self, standalone=True)

        # Run sounds better :-)
        self.run = self.mainloop


class TraceApp(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from automagica.capture import Capture

        self.capture = Capture()

        # Run sounds better :)
        self.run = self.mainloop


class LabApp:
    def new(self):
        self.edit()

    def edit(self, notebook_path=None):
        my_env = os.environ.copy()

        path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )

        my_env["JUPYTER_CONFIG_DIR"] = os.path.join(path, "lab\.jupyter")

        cmd = sys.executable + " -m notebook"

        if notebook_path:
            cmd += ' "{}"'.format(notebook_path)

        if platform.system() == "Linux":
            cmd += " --ip=127.0.0.1 --allow-root"
            subprocess.Popen(cmd, env=my_env, shell=True)
        else:
            subprocess.Popen(cmd, env=my_env)

    def run(self, notebook_path, parameters=None, cell_timeout=600):
        try:
            import nbconvert
        except:
            logging.exception(
                "Could not import nbconvert. It is required to run Automagica Lab notebooks. Do you have it installed?"
            )

        try:
            import nbformat
        except:
            logging.exception(
                "Could not import nbformat. It is required to run Automagica Lab notebooks. Do you have it installed?"
            )

        from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
        from nbformat.notebooknode import from_dict

        import json

        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        ep = ExecutePreprocessor(timeout=cell_timeout, kernel_name="python3")

        if parameters:
            parameter_node = from_dict(
                {
                    "cell_type": "code",
                    "metadata": {"tags": ["parameters"]},
                    "source": parameters,
                }
            )
            for i, cell in enumerate(notebook.cells):
                if cell.metadata:
                    if cell.metadata.tags:
                        if "default-parameters" in cell.metadata.tags:
                            break
            else:
                i = 0
            notebook.cells.insert(i, parameter_node)

        error = None

        try:
            ep.preprocess(notebook)

        except CellExecutionError as e:

            try:
                lines = [line.strip() for line in str(e.traceback).split("\n") if line]
                error = lines[-1]
            except:
                error = "Exception: unknown error."

        finally:
            return notebook, error
