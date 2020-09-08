"""Copyright 2020 Oakwood Technologies BVBA"""
from automagica.gui.apps import WandApp


def test_wand_app():
    """
    Testing scenario to test Automagica Wand application
    """
    app = WandApp()
    app.destroy()
    app.quit()
