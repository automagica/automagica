import logging
import os
import platform
import re
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

        try:
            self.destroy()
        except:
            pass

        try:
            self.quit()
        except:
            pass

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
            # on_close=self.close_app,
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

    def execute_notebook(self, filepath, cwd):
        import subprocess
        import sys

        process = subprocess.Popen(
            [sys.executable, "-m", "automagica.cli", "lab", "run", filepath],
            stdout=subprocess.PIPE,
            cwd=cwd,
        )

        out, err = process.communicate()

        return out.decode("utf-8")

    def execute_script(self, filepath, cwd):
        import subprocess
        import sys

        process = subprocess.Popen(
            [sys.executable, filepath], stdout=subprocess.PIPE, cwd=cwd
        )

        out, err = process.communicate()

        return out.decode("utf-8")

    def execute_flow(self, filepath, cwd):
        import subprocess
        import sys

        process = subprocess.Popen(
            [sys.executable, "-m", "automagica.cli", "flow", "run", filepath],
            stdout=subprocess.PIPE,
            cwd=cwd,
        )

        out, err = process.communicate()

        return out.decode("utf-8")

    def execute_command(self, command, cwd):
        import subprocess
        import sys

        process = subprocess.Popen([command], stdout=subprocess.PIPE, cwd=cwd,)

        out, err = process.communicate()

        return out.decode("utf-8")

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
            try:
                # Get next job
                r = requests.get(self.url + "/api/job/next", headers=headers)
                job = r.json()

                print(job)

                # We got a job!
                if job:
                    logging.info("Received job {}".format(job["job_id"]))

                    # Create directory to store job-related files
                    local_job_path = os.path.join(
                        os.path.expanduser("~"), ".automagica", job["job_id"]
                    )
                    os.makedirs(local_job_path)
                    os.makedirs(os.path.join(local_job_path, "input"))
                    os.makedirs(os.path.join(local_job_path, "output"))

                    # Download job input files
                    for job_file in job["job_files"]:

                        # Download file
                        r = requests.get(job_file["url"])

                        # Save locally in the input folder in the job folder
                        with open(
                            os.path.join(local_job_path, "input", job_file["filename"]),
                            "wb",
                        ) as f:
                            f.write(r.content)

                    try:
                        entrypoint = job["job_entrypoint"]

                        if entrypoint.endswith(".ipynb"):
                            output = self.execute_notebook(
                                os.path.join(local_job_path, "input", entrypoint,),
                                local_job_path,
                            )

                        elif entrypoint.endswith(".py"):
                            output = self.execute_script(
                                os.path.join(local_job_path, "input", entrypoint),
                                local_job_path,
                            )

                        elif entrypoint.endswith(".json"):
                            output = self.execute_flow(
                                os.path.join(local_job_path, "input", entrypoint),
                                local_job_path,
                            )

                        else:
                            output = self.execute_command(entrypoint, local_job_path)

                        # Write console output
                        with open(
                            os.path.join(local_job_path, "output", "console.txt"), "w"
                        ) as f:
                            f.write(output)

                        job["status"] = "completed"
                        logging.exception("Completed job {}".format(job["job_id"]))

                    except:
                        job["status"] = "failed"
                        logging.exception("Failed job {}".format(job["job_id"]))

                    # Make list of output files after job has ran
                    output_files = []

                    for filepath in os.listdir(os.path.join(local_job_path, "output")):
                        output_files.append({"filename": filepath})

                    # Prepare finished job package
                    data = {
                        "bot_secret": self.config["bot_secret"],
                        "job_id": job["job_id"],
                        "job_status": job["status"],
                        "job_output_files": output_files,
                        "job_output": output,
                    }

                    # Update Portal on job status and request S3 signed URLs to upload job output files
                    r = requests.post(
                        self.url + "/api/job/status", json=data, headers=headers
                    )

                    data = r.json()

                    print(data)

                    # Upload job output files
                    for output_file in data["output_files"]:
                        with open(
                            os.path.join(
                                local_job_path, "output", output_file["filename"]
                            ),
                            "rb",
                        ) as f:
                            _ = requests.post(
                                output_file["payload"]["url"],
                                data=output_file["payload"]["fields"],
                                files={
                                    "file": (
                                        os.path.join(
                                            local_job_path,
                                            "output",
                                            output_file["filename"],
                                        ),
                                        f,
                                    )
                                },
                            )

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
        import json

        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                exec("".join(cell["source"]))
