"""Copyright 2020 Oakwood Technologies BVBA"""
import pytest

from automagica.gui.apps import FlowApp
from automagica.utilities import all_activities


@pytest.fixture
def flow_app():
    """ Testing fixture for the Flow app """
    app = FlowApp()

    app.update()

    yield app

    app.destroy()
    app.quit()


@pytest.mark.smoke
def test_flow_app(flow_app):
    """Flow application smoke test"""

    # If the application starts normally without any errors
    flow_app.update()

    assert True


def test_all_activities_flow(flow_app, tmp_path):
    """Create a simple flow using all Automagica activities"""

    # Render application
    flow_app.update()

    # Get children of app
    windows = flow_app.winfo_children()

    # Check if we have child windows
    assert len(windows) > 0

    # First child is the Flow designer window
    flow_designer_window = windows[0]
    flow_designer_window.update()

    # Add all Automagica activities to the flow
    for key in all_activities().keys():
        flow_designer_window.add_activity(key)
        flow_designer_window.update()

    # Save the flow
    d = tmp_path / "flows"
    d.mkdir()
    flow_designer_window.flow.save(d / "simple_flow.json")

    assert len(list(tmp_path.iterdir())) == 1

    # Open properties window for every block
    for node in flow_designer_window.flow.nodes:
        window = node.graph.double_clicked(None)
        window.update()
        window.destroy()

    assert True
