"""Copyright 2020 Oakwood Technologies BVBA"""
import pytest

from automagica.gui.apps import WandApp


@pytest.fixture
def wand_app():
    """ Testing fixture for the Flow app """
    app = WandApp()

    yield app

    app.destroy()
    app.quit()


def test_wand_app(wand_app):
    """
    Testing scenario to test Automagica Wand application
    """
    wand_app.update()

    assert True
