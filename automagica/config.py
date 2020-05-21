import os
from gettext import translation, gettext

from .utilities import all_activities

ACTIVITIES = all_activities()

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
    lang = translation("messages", localedir=localedir, languages=[LOCALE])
    lang.install()
    _ = lang.gettext
else:
    _ = gettext


"""
Styling
"""
FONT = "Helvetica"

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
