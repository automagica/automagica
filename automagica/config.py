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
    def __init__(self, file_path="", ignore_warnings=False, debug=True):
        self.file_path = file_path
        self.ignore_warnings = ignore_warnings
        self.debug = debug

        # Custom config specified?
        if not self.file_path:
            self.file_path = os.path.join(os.path.expanduser("~"), "automagica.json")

        # Set up logging
        self._setup_logging(debug=debug)

        self.values = self.load()

        if not self.values.get("portal_url"):
            self.values["portal_url"] = os.environ.get(
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

        self.logger = logging.getLogger("automagica")
        self.logger.setLevel(log_level)

        # Log to file
        logging_path = os.path.join(os.path.expanduser("~"), "automagica.log")
        file_handler = logging.FileHandler(logging_path)
        file_handler.setFormatter(formatter)

        # Log to console
        stdout_handler = logging.StreamHandler(sys.stdout)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stdout_handler)

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.values, f)

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.values = json.load(f)

        except FileNotFoundError:
            self.values = {}
            self.save()

        return self.values

    def wizard(self):
        print("Automagica Configuration\n")
        print(
            "You can find your User Secret and Bot Secret at {}".format(
                self.values.get("portal_url")
            )
        )
        print(
            "Leave a value empty to enter the proposed or default value between [brackets]."
        )

        portal_url = input(
            "\nAutomagica Portal URL [{}]: ".format(self.values.get("portal_url"))
        )

        if portal_url:
            self.values["portal_url"] = portal_url

        user_secret = input(
            "\nAutomagica User Secret [{}]: ".format(self.values.get("user_secret"))
        )

        if user_secret:
            self.values["user_secret"] = user_secret

        bot_secret = input(
            "\nAutomagica Bot Secret [{}]: ".format(self.values.get("bot_secret"))
        )

        if bot_secret:
            self.values["bot_secret"] = bot_secret

        locale = input("\nLocale [{}]: ".format(self.values.get("locale", "en_GB")))

        if locale:
            self.values["locale"] = locale

        self.save()


def register_protocol_handler():
    if platform.system() == "Windows":
        import winreg as reg

        registry = reg.CreateKey(reg.HKEY_CLASSES_ROOT, "Automagica")

        registry = reg.OpenKey(reg.HKEY_CLASSES_ROOT, "Automagica", 0, reg.KEY_WRITE)

        reg.SetValueEx(registry, "", 0, reg.REG_SZ, "URL:automagica")
        reg.SetValueEx(registry, "URL Protocol", 0, reg.REG_SZ, "")

        registry = reg.CreateKey(
            reg.HKEY_CLASSES_ROOT, "Automagica\\shell\\open\\command"
        )

        # Register automagica:// protocol
        registry = reg.OpenKey(
            reg.HKEY_CLASSES_ROOT, "Automagica\\shell\\open\\command", 0, reg.KEY_WRITE,
        )

        reg.SetValueEx(
            registry,
            "",
            0,
            reg.REG_SZ,
            sys.executable.replace("python.exe", "pythonw.exe")
            + " -m automagica.protocol %1",
        )

        reg.CloseKey(registry)


if __name__ == "__main__":
    import sys
    import platform

    # This is used by automatic one-click installer for Windows to set-up a bot automatically
    cfg = Config()

    # Installer path is provided as command line argument
    installer_path = sys.argv[1]

    # Set configuration value. Bot secret is provided between brackets
    bot_secret = installer_path.split("[")[1].split("]")[0]
    cfg.values["bot_secret"] = bot_secret

    # Save configuration
    cfg.save()

    # Register protocol automagica:// in registry
    register_protocol_handler()

