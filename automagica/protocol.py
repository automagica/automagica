"""Copyright 2020 Oakwood Technologies BVBA"""

import logging
import os
import sys
from tkinter import messagebox

from automagica.config import Config, _
from automagica.gui.apps import (
    App,
    AutomagicaTk,
    BotApp,
    FlowApp,
    LabApp,
    WandApp,
)

if __name__ == "__main__":
    """
    Protocol handler for URLS with the automagica://-protocol
    This allows to immediate launch Automagica Flow for example from a website URL
    """
    url = sys.argv[1]

    url = url.replace("automagica://", "")

    parts = url.split("/")

    os.chdir(os.path.expanduser("~"))

    # Automagica Flow (automagica://flow/new)
    if parts[0] == "flow":
        if parts[1] == "new":
            root = AutomagicaTk()
            _ = FlowApp(root)
            root.mainloop()

    # Automagica Lab (automagica://lab/new)
    if parts[0] == "lab":
        if parts[1] == "new":
            app = LabApp()
            app.new()

    # Automagica Wand (automagica://wand)
    if parts[0] == "wand":
        root = AutomagicaTk()
        _ = WandApp(root)
        root.mainloop()

    # Automagica Bot (automagica://bot/bot_secret/ABCD12345)
    if parts[0] == "bot":
        config = Config()

        # Bot secret specified
        if parts[1] == "bot_secret":
            bot_secret = parts[2]

            config.values["bot_secret"] = bot_secret
            config.save()

        root = AutomagicaTk(config=config)
        app = BotApp(root)
        app.run()
        root.mainloop()

