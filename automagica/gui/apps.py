import json
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
from automagica.config import ICONS, Config
from automagica.flow import Flow
from automagica.gui.windows import (
    BotTrayWindow,
    FlowDesignerWindow,
    FlowPlayerWindow,
    NotificationWindow,
    WandWindow,
)


class App(tk.Tk):
    def __init__(self, *args, config=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Hide Tkinter root window
        self.withdraw()

        # Load config
        self.config = config

        if not self.config:
            self.config = Config()

        # On Windows, set DPI awareness
        if platform.system() == "Windows":
            self._windows_set_dpi_awareness()

        # Set Automagica icon
        icon_path = os.path.join(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            ),
            "icons",
            "automagica.ico",
        )
        self.tk.call(
            "wm",
            "iconphoto",
            self._w,
            ImageTk.PhotoImage(Image.open(icon_path)),
        )

        ICONS.generate_icons()

    def _windows_set_dpi_awareness(self):
        import ctypes

        awareness = ctypes.c_int()
        error_code = ctypes.windll.shcore.GetProcessDpiAwareness(
            0, ctypes.byref(awareness)
        )
        error_code = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        success = ctypes.windll.user32.SetProcessDPIAware()

    def report_callback_exception(self, exception, value, traceback):
        """ 
        Override default tkinter method to log errors 
        """
        self.config.logger.exception(exception)

    def exit(self):
        os._exit(0)


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

        if not bot:
            bot = ThreadedBot()

        self.bot = bot

        if file_path:

            # Run a flow
            if run:

                # Run parameters
                if os.path.isfile("input/parameters.py"):
                    with open(
                        "input/parameters.py", "r", encoding="utf-8"
                    ) as f:
                        code = f.read()

                    bot.run(code)

                # Run Flow
                FlowPlayerWindow(
                    self,
                    flow=Flow(file_path),
                    bot=self.bot,
                    autoplay=True,
                    step_by_step=step_by_step,
                    autoclose=True,
                )

            # Edit the flow
            else:
                FlowDesignerWindow(self, bot=self.bot, flow=Flow(file_path))

        # New flow
        else:
            FlowDesignerWindow(self, bot=self.bot)

        # Run sounds better, right?
        self.run = self.mainloop

    def close_app(self, exit_code=0):
        self.bot.stop()
        os._exit(exit_code)


class BotApp(App):
    def __init__(self, *args, bot=None, file_path=None, config=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Tray application
        self.bot_tray_window = BotTrayWindow(self)

        # Runner Thread (polling Automagica Portal for jobs)
        self.runner_thread = Thread(target=self._runner_thread)
        self.runner_thread.start()

        # Alive Thread (polling Automagica Portal for health status)
        self.alive_thread = Thread(target=self._alive_thread)
        self.alive_thread.start()

        # Run sounds better :-)
        self.run = self.mainloop

    def run_notebook(self, file_path, cwd):
        process = subprocess.Popen(
            [sys.executable, "-m", "automagica.cli", "lab", "run", file_path],
            stdout=subprocess.PIPE,
            cwd=cwd,
        )

        stdout, stderr = process.communicate()

        return stdout.decode("utf-8"), process.returncode

    def run_script(self, file_path, cwd):
        process = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "automagica.cli",
                "script",
                "run",
                file_path,
            ],
            stdout=subprocess.PIPE,
            cwd=cwd,
        )

        stdout, stderr = process.communicate()

        return stdout.decode("utf-8"), process.returncode

    def run_flow(self, file_path, cwd):
        process = subprocess.Popen(
            [sys.executable, "-m", "automagica.cli", "flow", "run", file_path],
            stdout=subprocess.PIPE,
            cwd=cwd,
        )

        stdout, stderr = process.communicate()

        return stdout.decode("utf-8"), process.returncode

    def run_command(self, command, cwd):
        process = subprocess.Popen([command], stdout=subprocess.PIPE, cwd=cwd,)

        stdout, stderr = process.communicate()

        return stdout.decode("utf-8"), process.returncode

    def _alive_thread(self, interval=30):
        headers = {"bot_secret": self.config.values["bot_secret"]}

        while True:
            try:
                _ = requests.post(
                    self.config.values["portal_url"] + "/api/bot/alive",
                    headers=headers,
                )
                self.config.logger.info("Sent alive to Automagica Portal.")
            except:
                self.config.logger.exception(
                    "Could not reach Automagica Portal."
                )

            sleep(interval)

    def _runner_thread(self, interval=10, retry_interval=5 * 60):
        headers = {"bot_secret": self.config.values["bot_secret"]}

        NotificationWindow(self, message="Bot started!")

        while True:
            try:
                # Get next job
                r = requests.get(
                    self.config.values["portal_url"] + "/api/job/next",
                    headers=headers,
                )

                job = r.json()

                # We got a job!
                if job:
                    NotificationWindow(
                        self, message=f"Received job {job['job_id']}"
                    )
                    self.config.logger.info(f"Received job {job['job_id']}")

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
                            os.path.join(
                                local_job_path, "input", job_file["filename"]
                            ),
                            "wb",
                        ) as f:
                            f.write(r.content)

                    if job.get("parameters"):
                        with open(
                            os.path.join(
                                local_job_path, "input", "parameters.py"
                            ),
                            "w",
                        ) as f:
                            f.write(job["parameters"])

                    entrypoint = job["job_entrypoint"]

                    # IPython Notebook / Automagica Lab
                    if entrypoint.endswith(".ipynb"):
                        output, returncode = self.run_notebook(
                            os.path.join(local_job_path, "input", entrypoint,),
                            local_job_path,
                        )

                    # Python Script File
                    elif entrypoint.endswith(".py"):
                        output, returncode = self.run_script(
                            os.path.join(local_job_path, "input", entrypoint),
                            local_job_path,
                        )

                    # Automagica FLow
                    elif entrypoint.endswith(".json"):
                        output, returncode = self.run_flow(
                            os.path.join(local_job_path, "input", entrypoint),
                            local_job_path,
                        )

                    # Other command
                    else:
                        output, returncode = self.run_command(
                            entrypoint, local_job_path
                        )

                    # Write console output
                    with open(
                        os.path.join(local_job_path, "output", "console.txt"),
                        "w",
                    ) as f:
                        f.write(output)

                    if returncode == 0:
                        job["status"] = "completed"
                        NotificationWindow(
                            self, message=f"Completed job {job['job_id']}"
                        )
                        self.config.logger.info(
                            f"Completed job {job['job_id']}"
                        )

                    else:
                        job["status"] = "failed"
                        NotificationWindow(
                            self, message=f"Failed job {job['job_id']}"
                        )
                        self.config.logger.info(f"Failed job {job['job_id']}")

                    # Make list of output files after job has ran
                    output_files = []

                    for file_path in os.listdir(
                        os.path.join(local_job_path, "output")
                    ):
                        output_files.append({"filename": file_path})

                    # Prepare finished job package
                    data = {
                        "bot_secret": self.config.values["bot_secret"],
                        "job_id": job["job_id"],
                        "job_status": job["status"],
                        "job_output_files": output_files,
                        "job_output": output,
                    }

                    # Update Portal on job status and request S3 signed URLs to upload job output files
                    r = requests.post(
                        self.config.values["portal_url"] + "/api/job/status",
                        json=data,
                        headers=headers,
                    )

                    data = r.json()

                    # Upload job output files
                    for output_file in data["output_files"]:
                        with open(
                            os.path.join(
                                local_job_path,
                                "output",
                                output_file["filename"],
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
                NotificationWindow(self, message="Connection error")
                self.config.logger.exception(
                    f"Could not reach Automagica Portal. Waiting {interval} second(s) before retrying."
                )
                sleep(interval)


class WandApp(App):
    def __init__(self, *args, delay=0, on_finish=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        # Open the main window
        self.wand_window = WandWindow(
            self, standalone=True, delay=delay, on_finish=on_finish
        )

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
    def __init__(self, config=None):
        # Load config
        self.config = config
        if not self.config:
            self.config = Config()

    def new(self):
        self.edit()

    def edit(self, notebook_path=None):
        # Get current path
        path = os.path.abspath(__file__).replace(
            os.path.basename(os.path.realpath(__file__)), ""
        )

        # Read environment variables and override Jupyter configuration directory setting
        my_env = os.environ.copy()
        my_env["JUPYTER_CONFIG_DIR"] = os.path.join(path, "lab\.jupyter")

        # Build command
        cmd = sys.executable + " -m notebook"

        if notebook_path:
            cmd += ' "{}"'.format(notebook_path)

        if platform.system() == "Linux":
            # This is required within Linux
            cmd += " --ip=127.0.0.1 --allow-root"
            subprocess.Popen(cmd, env=my_env, shell=True)  # nosec

        else:
            subprocess.Popen(cmd, env=my_env)

    def run(self, notebook_path, cell_timeout=600):
        # Run parameters
        if os.path.isfile("input/parameters.py"):
            with open("input/parameters.py", "r", encoding="utf-8") as f:
                self.config.logger.info(
                    f'Loading parameters from "{os.path.realpath(f.name)}"'
                )
                code = f.read()
            try:
                exec(code)  # nosec
                self.config.logger.info(f"Completed loading parameters")

            except Exception as e:
                self.config.logger.exception("Failed loading parameters")
                raise e

        # Open the notebook
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        # Run all cells
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                try:
                    exec("".join(cell["source"]))  # nosec
                    self.config.logger.info(
                        f'Completed notebook "{notebook_path}"'
                    )

                except Exception as e:
                    self.config.logger.exception(
                        f'Failed notebook "{notebook_path}"'
                    )
                    raise e


class ScriptApp:
    def __init__(self, config=None):
        # Load config
        self.config = config

        if not self.config:
            self.config = Config()

    def run(self, script_path):
        self.config.logger.info(f'Started script "{script_path}"')

        # Load parameters
        if os.path.isfile("input/parameters.py"):
            with open("input/parameters.py", "r", encoding="utf-8") as f:
                self.config.logger.info(
                    f'Loading parameters from "{os.path.realpath(f.name)}"'
                )
                code = f.read()
            try:
                exec(code)  # nosec
                self.config.logger.info(f"Completed loading parameters")

            except Exception as e:
                self.config.logger.exception("Failed loading parameters")
                raise e

        # Run script
        with open(script_path, "r", encoding="utf-8") as f:
            self.config.logger.info(
                f'Running script "{os.path.realpath(f.name)}"'
            )
            code = f.read()

        try:
            code_obj = compile(code, "script.py", "exec")
            d = dict(locals(), **globals())
            exec(code_obj, d, d)  # nosec
            self.config.logger.info(f'Completed script "{script_path}"')
            os._exit(0)

        except Exception as e:
            self.config.logger.exception(f'Failed script "{script_path}"')
            raise e
