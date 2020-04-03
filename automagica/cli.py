import argparse
import json
import logging
import os
import subprocess
import sys
from time import sleep

__version__ = "2.1.11"

parser = argparse.ArgumentParser(
    description="Automagica Robot v" + __version__)

parser.add_argument(
    "--connect",
    default="",
    type=str,
    help="Connect to Automagica Portal with user secret",
)

parser.add_argument(
    "--disconnect",
    dest="disconnect",
    action="store_true",
    help="Disconnect from Automagica Portal",
)

parser.add_argument(
    "--bot",
    dest="bot",
    action="store_true",
    help="Run bot connected to Automagica Portal",
)

parser.add_argument(
    "--config", dest="config", action="store_true", help="Alternate path to config"
)

parser.add_argument("-f", "--file", default="",
                    type=str, help="Path to script file")

parser.add_argument(
    "-s",
    "--script",
    default="",
    type=str,
    help="Script string for the Automagica robot (if no --file not specified)",
)

parser.add_argument(
    "-p",
    "--parameters",
    default="",
    type=str,
    help="Parameters string for the Automagica Bot",
)

parser.add_argument(
    "--ignore-warnings",
    dest="ignore_warnings",
    default=False,
    action="store_true",
    help="Python warnings will not end up in stderr",
)

parser.add_argument(
    "--debug",
    dest="debug",
    default=False,
    action="store_true",
    help="Debug level logging",
)

parser.add_argument(
    "-e",
    "--edit",
    default="",
    type=str,
    help="Edit Automagica script in Automagica Lab using the script id",
)

subparsers = parser.add_subparsers(help='sub-command help', dest='command')

parser_recorder = subparsers.add_parser(
    'recorder', help='Recorder help')


class Automagica:
    def __init__(self):
        # Process arguments
        args = parser.parse_args()

        self.args = args

        # Set up logging
        self._setup_logging(debug=args.debug)

        # Environment variable override Automagica Portal URL
        self.url = os.environ.get(
            "AUTOMAGICA_PORTAL_URL", "https://portal.automagica.com"
        )

        # Custom config specified?
        if args.config:
            self.config_path = args.config
        else:
            self.config_path = os.path.join(
                os.path.expanduser("~"), "automagica.json")

        self.config = self._load_config()

        # Download and run Jupyter Notebook (.ipynb)
        if args.edit:
            self.edit(args.edit)

        # Connect to Automagica Portal
        if args.connect:
            user_secret = args.connect.split("[")[1].split("]")[0]
            self.connect(user_secret)

        # Disconnect from Automagica Portal
        if args.disconnect:
            self.disconnect()

        # Start Automagica Bot manually
        if args.bot:
            self.bot()

        if args.command == 'recorder':
            from .recorder import recorder
            recorder()

        # Was a file specified?
        if args.file:
            with open(args.file, newline="") as f:
                script = f.read()
        else:
            script = args.script

        # Ignore warnings
        if args.ignore_warnings:
            import warnings

            warnings.simplefilter("ignore")

        # Parameters specified
        if args.parameters:
            exec(args.parameters, globals())

        # Run script
        exec(script, globals())

    def _setup_logging(self, debug=False):
        if debug:
            log_level = logging.INFO
        else:
            log_level = logging.WARNING

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s]: %(message)s")

        logger = logging.getLogger()
        logger.setLevel(log_level)

        # Log to file
        logging_path = os.path.join(os.path.expanduser("~"), "automagica.log")
        file_handler = logging.FileHandler(logging_path)
        file_handler.setFormatter(formatter)

        # Log to console
        stdout_handler = logging.StreamHandler(sys.stdout)

        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)

    def edit(self, url):
        """Edit a script from the Automagica Portal
        """
        from time import sleep
        import requests
        import re
        import subprocess
        import sys

        try:
            script_id = None
            script_version_id = None

            if url.startswith("automagica://"):
                ids = url.replace("automagica://", "").split("/")

            if len(ids) == 1:
                script_id = ids[0]

            if len(ids) == 2:
                script_id = ids[0]
                script_version_id = ids[1]

            # Check if Automagica folder exists
            target_folder = os.path.join(
                os.path.expanduser("~"), ".automagica")

            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

            # Retrieve URL
            headers = {
                "user_secret": self.config["user_secret"],
                "script_id": script_id,
            }

            if script_version_id:
                headers["script_version_id"] = script_version_id

            r = requests.get(self.url + "/api/script", headers=headers)

            import re

            d = r.headers["content-disposition"]
            fname = re.findall("filename=(.+)", d)[0]

            path = os.path.join(target_folder, fname)

            with open(path, "wb") as f:
                f.write(r.content)

            notebook_path = path

            # Run notebook server
            import subprocess

            my_env = os.environ.copy()

            path = os.path.abspath(__file__).replace("cli.py", "")

            my_env["JUPYTER_CONFIG_DIR"] = os.path.join(path, "lab/.jupyter")

            cmd = sys.executable + ' -m notebook "{}"'.format(notebook_path)

            if not self.args.debug:
                self.try_to_hide_console()

            import platform

            if platform.system() == "Linux":
                process = subprocess.Popen(cmd, env=my_env, shell=True)

            else:
                process = subprocess.Popen(cmd, env=my_env)

            # While server is running, check for changes of the path
            last_known_modification = os.path.getmtime(notebook_path)

            with open(notebook_path, "r") as f:
                last_known_binary = f.read()

            print(
                "Automagica's Jupyter Notebook server running. Do not close this window."
            )

            while not process.poll():
                last_modification = os.path.getmtime(notebook_path)

                if last_known_modification < last_modification:

                    last_known_modification = last_modification

                    with open(notebook_path, "r", encoding="utf-8") as f:
                        last_binary = f.read()

                    if last_known_binary != last_binary:
                        last_known_binary = last_binary

                        r = requests.post(
                            self.url + "/api/script", headers=headers
                        ).json()

                        with open(notebook_path, "rb") as f:
                            files = {"file": (notebook_path, f)}
                            _ = requests.post(
                                r["url"], data=r["fields"], files=files)

                sleep(1)

            print("Automagica's Jupyter Notebook server closed.")

        except:
            logging.exception("Something went wrong...")
            input()

    def _save_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.config, f)

    def _load_config(self):
        try:
            with open(self.config_path, "r") as f:
                config = json.load(f)

        except FileNotFoundError:
            config = {}
            self.config = config
            self._save_config()

        return config

    def notification(self, message):
        from plyer import notification

        app_icon = os.path.abspath(__file__).replace("cli.py", "icon.ico")
        notification.notify(
            title="Automagica Robot",
            message=message,
            app_name="Automagica Robot",
            app_icon=app_icon,
            ticker="Automagica",
        )

    def _alive(self):
        import requests
        import os
        from time import sleep

        headers = {"bot_secret": self.config["bot_secret"]}

        while True:
            try:
                _ = requests.post(self.url + "/api/bot/alive", headers=headers)
                print(_.content)
            except:
                logging.exception("Could not reach Automagica Portal.")
            sleep(30)

    def run(self, notebook, parameters=None, cell_timeout=600):
        from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
        from nbformat.notebooknode import from_dict

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
            out = ep.preprocess(notebook)

        except CellExecutionError as e:

            try:
                lines = [line.strip()
                         for line in str(e.traceback).split('\n') if line]
                error = lines[-1]
            except:
                error = 'Exception: unknown error.'

        finally:
            return notebook, error

    def bot(self):
        global CURRENT_JOB

        from threading import Thread
        import requests

        # Start seperate thread to let portal know I'm alive
        t = Thread(target=self._alive)

        t.start()

        if not self.args.debug:
            self.try_to_hide_console()

        while True:
            # Get next job
            headers = {"bot_secret": self.config["bot_secret"]}

            try:
                r = requests.get(self.url + "/api/job/next", headers=headers)
                job = r.json()

                # We got a job!
                if job:
                    logging.info("Received job {}".format(job["job_id"]))

                    CURRENT_JOB = job["job_id"]

                    headers = {
                        "script_id": job["script_id"],
                        "script_version_id": job.get("script_version_id"),
                        "bot_secret": self.config["bot_secret"],
                    }

                    # Retrieve notebook
                    r = requests.get(
                        self.url + "/api/script", headers=headers, stream=True
                    )

                    from io import BytesIO
                    import nbformat

                    notebook = nbformat.read(BytesIO(r.content), as_version=4)

                    output, error = self.run(
                        notebook,
                        parameters=job.get("parameters"),
                        cell_timeout=-1,  # No timeout
                    )

                    if not error:
                        # Completed without exceptions
                        job["status"] = "completed"
                        logging.exception(
                            "Completed job {}".format(job["job_id"]))

                    else:
                        # Exceptions occured
                        job["status"] = "failed"
                        job['error'] = error
                        logging.exception(
                            "Failed job {}".format(job["job_id"]))

                    headers = {
                        "bot_secret": self.config["bot_secret"],
                        "job_id": job["job_id"],
                        "job_status": job["status"],
                    }

                    if error:
                        headers['job_error'] = error

                    # Request S3 upload URL for Job Notebook
                    r = requests.post(self.url + "/api/job",
                                      headers=headers).json()

                    from io import BytesIO

                    data = nbformat.writes(output, version=4)

                    fileobj = BytesIO()

                    fileobj.write(data.encode("utf-8"))

                    fileobj.seek(0)

                    files = {"file": ("notebook.ipynb", fileobj)}

                    _ = requests.post(r["url"], data=r["fields"], files=files)

                    CURRENT_JOB = None

                    if error:
                        # Request S3 Upload URL for screenshot
                        r = requests.post(
                            self.url + "/api/job/screenshot", headers=headers).json()

                        # We should upload
                        if r.get('url'):
                            import mss

                            with mss.mss() as sct:
                                sct.compression_level = 9
                                filename = sct.shot(mon=-1)

                            with open(filename, 'rb') as fileobj:
                                files = {"file": ("screenshot.png", fileobj)}
                                _ = requests.post(
                                    r["url"], data=r["fields"], files=files)

                # We did not get a job!
                else:
                    sleep(10)

            except:
                logging.exception("Could not reach portal.")
                sleep(10)

    def _kill_processes_by_name(self, name):
        import psutil

        for proc in psutil.process_iter():
            if proc.name() == name or proc.name() == name + ".exe":
                if proc.pid != os.getpid():  # Don't kill yourself
                    proc.kill()
                    proc.wait()

    def connect(self, user_secret):
        import requests
        import socket
        import os

        headers = {"user_secret": user_secret}
        data = {"name": socket.gethostname()}

        print(headers)
        print(data)

        r = requests.post(self.url + "/api/bot/setup",
                          json=data, headers=headers)

        if r.status_code != 200:
            raise Exception("Could not connect to Automagica Portal")

        data = r.json()

        self.config["user_secret"] = user_secret
        self.config["bot_secret"] = data["bot_secret"]
        self._save_config()

        self.add_startup()
        self._kill_processes_by_name("python")

        sleep(3)

        cmd = sys.executable + " -m automagica --bot"

        if self.args.debug:
            cmd += "  --debug"

        subprocess.Popen(cmd)

        if not self.args.debug:
            self.try_to_hide_console()

        import webbrowser

        webbrowser.open(self.url)

    def try_to_hide_console(self):
        if os.name == "nt":
            import ctypes

            ctypes.windll.user32.ShowWindow(
                ctypes.windll.kernel32.GetConsoleWindow(), 0
            )

    def disconnect(self):
        self._kill_processes_by_name("python")
        self.remove_startup()

    def add_startup(self):
        import platform

        cmd = sys.executable + " -m automagica --bot"

        if platform.system() == "Windows":
            import winreg as reg

            # Add to start-up
            registry = reg.OpenKey(
                reg.HKEY_CURRENT_USER,
                "Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                reg.KEY_WRITE,
            )
            reg.SetValueEx(registry, "Automagica", 0, reg.REG_SZ, cmd)
            reg.CloseKey(registry)

            registry = reg.CreateKey(reg.HKEY_CLASSES_ROOT, "Automagica")

            registry = reg.OpenKey(
                reg.HKEY_CLASSES_ROOT, "Automagica", 0, reg.KEY_WRITE
            )

            reg.SetValueEx(registry, "", 0, reg.REG_SZ, "URL:automagica")
            reg.SetValueEx(registry, "URL Protocol", 0, reg.REG_SZ, "")

            registry = reg.CreateKey(
                reg.HKEY_CLASSES_ROOT, "Automagica\\shell\\open\\command"
            )

            # Register automagica:// protocol
            registry = reg.OpenKey(
                reg.HKEY_CLASSES_ROOT,
                "Automagica\\shell\\open\\command",
                0,
                reg.KEY_WRITE,
            )

            reg.SetValueEx(
                registry, "", 0, reg.REG_SZ, sys.executable + " -m automagica -e %1"
            )

            reg.CloseKey(registry)

        if platform.system() == "Linux":
            # Create Automagica.desktop file in ~/.config/autostart/
            path = os.path.join(
                os.path.expanduser("~"), ".config/autostart/Automagica.desktop"
            )
            with open(path, "w") as f:
                contents = (
                    """[Desktop Entry] 
                            Type=Application
                            Exec="""
                    + cmd
                )
                f.write(contents)

        if platform.system() == "Darwin":
            # Create com.automagica.robot.plist file in ~/Library/LaunchAgents
            path = os.path.join(
                os.path.expanduser("~"),
                "Library/LaunchAgents/com.automagica.robot.plist",
            )
            with open(path, "w") as f:
                contents = (
                    """<?xml version="1.0" encoding="UTF-8"?>
                            <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
                            <plist version="1.0">
                            <dict>
                            <key>Label</key>
                            <string>com.automagica.robot</string>
                            <key>ProgramArguments</key>
                            <array>
                            <string>"""
                    + cmd
                    + """</string>
                            </array>
                            <key>RunAtLoad</key>
                            <true/>
                            </dict>
                            </plist>"""
                )

    def remove_startup(self):
        import platform

        if platform.system() == "Windows":
            import winreg as reg

            registry = reg.OpenKey(
                reg.HKEY_CURRENT_USER,
                "Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                reg.KEY_WRITE,
            )
            reg.DeleteValue(registry, "Automagica")
            reg.CloseKey(registry)

        if platform.system() == "Linux":
            path = os.path.join(
                os.path.expanduser("~"), ".config/autostart/Automagica.desktop"
            )
            os.remove(path)

        if platform.system() == "Darwin":
            path = os.path.join(
                os.path.expanduser("~"),
                "/Library/LaunchAgents/com.automagica.robot.plist",
            )
            os.remove(path)


def main():
    app = Automagica()


if __name__ == "__main__":
    main()
else:
    from .activities import *
