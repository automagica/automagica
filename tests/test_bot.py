"""Copyright 2020 Oakwood Technologies BVBA"""
import pytest

from automagica.gui.apps import BotApp


@pytest.fixture
def bot_app():
    """Testing fixture for the Flow app"""
    pytest.automagica_tk.update()

    app = BotApp(pytest.automagica_tk)

    app.update()

    yield app

    app.destroy()


@pytest.mark.smoke
def test_bot_app(bot_app):
    """Testing scenario to test Automagica Bot application"""
    bot_app.update()

    assert True


def test_config_window(bot_app):
    """Test configuration window"""
    window = bot_app.bot_tray_window.settings_clicked()
    window.update()
    window.destroy()

    assert True
