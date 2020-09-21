import pytest
from automagica.gui.apps import LabApp


@pytest.mark.smoke
def test_lab_app():
    """Test launching of Automagica Lab application"""
    app = LabApp()
    assert True
