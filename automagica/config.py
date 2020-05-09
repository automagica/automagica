from gettext import translation

from .utilities import all_activities

ACTIVITIES = all_activities()

"""
Localization
"""

LOCALE = "en"
lang = translation("messages", localedir="locale", languages=["fr"])
lang.install()
_ = lang.gettext


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
