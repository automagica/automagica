"""Copyright 2020 Oakwood Technologies BVBA"""
import pytest

from automagica.gui.apps import WandApp


@pytest.fixture
def wand_app():
    """Testing fixture for the Flow app"""
    app = WandApp(pytest.automagica_tk)

    app.update()

    yield app

    app.destroy()


@pytest.mark.smoke
def test_wand_app(wand_app):
    """Testing scenario to test Automagica Wand application"""
    wand_app.update()

    assert True
