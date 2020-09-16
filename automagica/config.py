"""Copyright 2020 Oakwood Technologies BVBA"""

import os
from gettext import gettext, translation
import logging

import sys
import pyglet
import json

from automagica.utilities import all_activities
from PIL import ImageTk, Image


ACTIVITIES = all_activities()


class IconGraph:
    def __init__(self, icon_size=20, color="#2196f3"):
        icons_path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__).replace(
                        os.path.basename(os.path.realpath(__file__)), ""
                    )
                )
            ),
            "automagica",
            "gui",
            "icons",
        )

        self.icon_names = os.listdir(icons_path)

        self.icon_paths = [
            os.path.join(icons_path, fn) for fn in self.icon_names
        ]

        self.icons_pil = []
        self.icons_tk = []

        self.color = tuple(
            int(color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4)
        )

    def generate_icons(self):
        for path in self.icon_paths:
            img = Image.open(path)

            data = img.load()

            if data:
                for x in range(img.size[0]):
                    for y in range(img.size[1]):
                        if (
                            data[x, y][0]
                            == data[x, y][1]
                            == data[x, y][2]
                            == 0
                        ):
                            data[x, y] = (
                                self.color[0],
                                self.color[1],
                                self.color[2],
                                data[x, y][3],
                            )

            self.icons_pil.append(img)
            self.icons_tk.append(ImageTk.PhotoImage(img))

    def tkinter(self, icon_name):
        index = self.icon_names.index(icon_name)

        return self.icons_tk[index]


ICONS = IconGraph()


"""
Localization
"""

LOCALE = "en"

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
    print(LOCALE)
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
            self.file_path = os.path.join(
                os.path.expanduser("~"), "automagica.json"
            )

        # Set up logging
        self._setup_logging(debug=debug)

        self.values = self.load()

        if not self.values.get("portal_url"):
            self.values["portal_url"] = os.environ.get(
                "AUTOMAGICA_PORTAL_URL", "https://portal.automagica.com"
            )

        if self.values.get("avoid_lockscreen") == None:
            self.values["avoid_lockscreen"] = True

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

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s]: %(message)s"
        )

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

        except:
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

        portal_url = input(  # nosec
            "\nAutomagica Portal URL [{}]: ".format(
                self.values.get("portal_url")
            )
        ).strip()

        if portal_url:
            self.values["portal_url"] = portal_url

        user_secret = input(  # nosec
            "\nAutomagica User Secret [{}]: ".format(
                self.values.get("user_secret")
            )
        ).strip()

        if user_secret:
            self.values["user_secret"] = user_secret

        bot_secret = input(  # nosec
            "\nAutomagica Bot Secret [{}]: ".format(
                self.values.get("bot_secret")
            )
        ).strip()

        if bot_secret:
            self.values["bot_secret"] = bot_secret

        locale = input(  # nosec
            "\nLocale [{}]: ".format(self.values.get("locale", "en_GB"))
        ).strip()

        if locale:
            self.values["locale"] = locale

        self.save()

    def add_bot_to_startup(self):
        import platform

        cmd = sys.executable + " -m automagica.cli bot"

        if platform.system() == "Windows":

            cmd = cmd.replace("python.exe", "pythonw.exe")

            import winreg as reg

            # Add to start-up
            registry = reg.OpenKey(
                reg.HKEY_CURRENT_USER,
                "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                0,
                reg.KEY_WRITE,
            )
            reg.SetValueEx(registry, "Automagica", 0, reg.REG_SZ, cmd)
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

    def remove_bot_from_startup(self):
        import platform

        if platform.system() == "Windows":
            import winreg as reg

            registry = reg.OpenKey(
                reg.HKEY_CURRENT_USER,
                "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
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


def register_protocol_handler():
    if platform.system() == "Windows":
        import winreg as reg

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
