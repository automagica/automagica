"""Copyright 2020 Oakwood Technologies BVBA"""
import pytest

from automagica.gui.apps import BotApp


@pytest.fixture
def bot_app():
    """ Testing fixture for the Flow app """
    app = BotApp()

    yield app

    app.destroy()
    app.quit()


@pytest.mark.smoke
def test_bot_app(bot_app):
    """
    Testing scenario to test Automagica Bot application
    """
    bot_app.update()

    assert True
