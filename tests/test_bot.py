"""Copyright 2020 Oakwood Technologies BVBA"""
from automagica.gui.apps import BotApp


def test_bot_app():
    """
    Testing scenario to test Automagica Bot application
    """
    app = BotApp()
    app.destroy()
    app.quit()

