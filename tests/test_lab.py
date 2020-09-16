import pytest
from automagica.gui.apps import LabApp


@pytest.mark.smoke
def test_lab_app():
    app = LabApp()
    assert True
