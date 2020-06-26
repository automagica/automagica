import os
from gettext import gettext, translation
import logging

import sys
import pyglet
import json

from automagica.utilities import all_activities

ACTIVITIES = all_activities()


"""
Localization
"""

LOCALE = "en"

# TODO: this needs a rewrite
localedir = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            )
        )
    ),
    "locale",
)

if LOCALE != "en":
    lang = translation("messages", localedir=localedir, languages=[LOCALE])
    lang.install()
    _ = lang.gettext
else:
    _ = gettext


"""
Styling
"""

fontdir = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__).replace(
                os.path.basename(os.path.realpath(__file__)), ""
            )
        )
    ),
    "automagica",
    "gui",
    "fonts",
)

# Add font files
pyglet.font.add_file(os.path.join(fontdir, "roboto.ttf"))
pyglet.font.add_file(os.path.join(fontdir, "roboto-mono.ttf"))

FONT = "Roboto"
FONT_MONO = "Roboto Mono"

COLOR_0 = "#2196f3"  # Automagica Blue
COLOR_1 = "#ffffff"  # White
COLOR_2 = "#AAAAAA"  # Light grey
COLOR_3 = "#555555"  # Less light grey
COLOR_4 = "#f0f0f0"  # Lightest grey
COLOR_5 = "#092740"  # Dark Blue
COLOR_6 = "#ff0000"  # Full Red
COLOR_7 = "#28a745"  # Green
COLOR_8 = "#000000"  # Black
COLOR_9 = "#cccccc"  # Pretty light grey
COLOR_10 = "#ffffff"  # Background menus white
COLOR_11 = "#000000"  # Label text
COLOR_12 = "#000000"
COLOR_13 = "#ffffff"
COLOR_14 = "#FFCCCB"  # Light red

# Dark mode
# COLOR_0 = "#092740"  # Automagica Blue
# COLOR_1 = "#ffffff"  # White
# COLOR_2 = "#121212"  # Light grey
# COLOR_3 = "#212121"  # Less light grey
# COLOR_4 = "#121212"  # Lightest grey
# COLOR_5 = "#071F33"  # Dark Blue
# COLOR_6 = "#ff0000"  # Full Red
# COLOR_7 = "#28a745"  # Green
# COLOR_8 = "#000000"  # White
# COLOR_9 = "#212121"  # Pretty light grey
# COLOR_10 = "#212121"
# COLOR_11 = "#ffffff"  # White
# COLOR_12 = "#121212"
# COLOR_13 = "#121212"


class Config:
    def __init__(self, file_path="", ignore_warnings=False, debug=False):
        self.file_path = file_path
        self.ignore_warnings = ignore_warnings
        self.debug = debug

        # Custom config specified?
        if not self.file_path:
            self.file_path = os.path.join(os.path.expanduser("~"), "automagica.json")

        # Set up logging
        self._setup_logging(debug=debug)

        self.config = self.load()

        if not self.config.get("portal_url"):
            self.config["portal_url"] = os.environ.get(
                "AUTOMAGICA_PORTAL_URL", "https://portal.automagica.com"
            )

        self.save()

        # Ignore warnings
        if ignore_warnings:
            import warnings

            warnings.simplefilter("ignore")

    def _setup_logging(self, debug=False):
        if debug:
            log_level = logging.INFO
        else:
            log_level = logging.WARNING

        formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")

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

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.config, f)

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                config = json.load(f)

        except FileNotFoundError:
            config = {}
            self.config = config
            self.save()

        return config

    def wizard(self):
        print("Automagica Configuration\n")
        print(
            "You can find your User Secret and Bot Secret at {}".format(
                self.config.get("portal_url")
            )
        )
        print(
            "Leave a value empty to enter the proposed or default value between [brackets]."
        )

        portal_url = input(
            "\nAutomagica Portal URL [{}]: ".format(self.config.get("portal_url"))
        )

        if portal_url:
            self.config["portal_url"] = portal_url

        user_secret = input(
            "\nAutomagica User Secret [{}]: ".format(self.config.get("user_secret"))
        )

        if user_secret:
            self.config["user_secret"] = user_secret

        bot_secret = input(
            "\nAutomagica Bot Secret [{}]: ".format(self.config.get("bot_secret"))
        )

        if bot_secret:
            self.config["bot_secret"] = bot_secret

        locale = input("\nLocale [{}]: ".format(self.config.get("locale", "en_GB")))

        if locale:
            self.config["locale"] = locale

        self.save()


if __name__ == "__main__":
    import sys

    # This is used by automatic one-click installer for Windows to set-up a bot automatically
    cfg = Config()

    # Installer path is provided as command line argument
    installer_path = sys.argv[1]

    # Set configuration value. Bot secret is provided between brackets
    bot_secret = installer_path.split("[")[1].split("]")[0]
    cfg.config["bot_secret"] = bot_secret

    # Save configuration
    cfg.save()
