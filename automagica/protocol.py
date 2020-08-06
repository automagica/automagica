import logging
import os
import sys
from tkinter import messagebox

from automagica.config import Config, _
from automagica.gui.apps import App, BotApp, FlowApp, LabApp, WandApp

if __name__ == "__main__":
    """
    Protocol handler for automagica://
    """
    url = sys.argv[1]

    url = url.replace("automagica://", "")

    parts = url.split("/")

    os.chdir(os.path.expanduser("~"))

    # Automagica Flow (automagica://flow/new)
    if parts[0] == "flow":
        if parts[1] == "new":
            app = FlowApp()
            app.run()

    # Automagica Lab (automagica://lab/new)
    if parts[0] == "lab":
        if parts[1] == "new":
            app = LabApp()
            app.new()

    # Automagica Wand (automagica://wand)
    if parts[0] == "wand":
        app = WandApp()
        app.run()

    # Automagica Bot (automagica://bot/bot_secret/ABCD12345)
    if parts[0] == "bot":
        config = Config()

        if parts[1] == "bot_secret":
            bot_secret = parts[2]

            config.values["bot_secret"] = bot_secret
            config.save()

        app = BotApp(config=config)

        app.run()
