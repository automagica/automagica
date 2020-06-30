import sys
import os


def try_to_hide_console():
    if os.name == "nt":
        import ctypes

        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


if __name__ == "__main__":
    url = sys.argv[1]

    url = url.replace("automagica://", "")

    parts = url.split("/")

    os.chdir(os.path.expanduser("~"))

    try_to_hide_console()

    if parts[0] == "flow":
        if parts[1] == "new":
            from automagica.gui.apps import FlowApp

            app = FlowApp()
            app.run()

    if parts[0] == "lab":
        if parts[1] == "new":
            from automagica.gui.apps import LabApp

            app = LabApp()
            app.new()

    if parts[0] == "wand":
        from automagica.gui.apps import WandApp

        app = WandApp()
        app.run()

    if parts[0] == "config":
        from automagica.config import Config

        cfg = Config()

        if parts[1] == "bot_secret":
            bot_secret = parts[2]
            cfg.config["bot_secret"] = bot_secret

        cfg.save()
