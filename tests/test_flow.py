"""Copyright 2020 Oakwood Technologies BVBA"""
import pytest

from automagica.gui.apps import FlowApp
from automagica.utilities import all_activities


@pytest.fixture
def flow_app():
    """Testing fixture for the Flow app"""
    app = FlowApp()

    # Let application render
    app.update()

    yield app

    # Clean-up
    app.destroy()
    app.quit()


@pytest.fixture
def flow_designer_window(flow_app):
    """Testing fixture for the FLow Designer window"""
    # Render application
    flow_app.update()

    # Get children of app
    windows = flow_app.winfo_children()

    # First child is the Flow designer window
    flow_designer_window = windows[0]

    # Render the window
    flow_designer_window.update()

    return flow_designer_window


@pytest.mark.smoke
def test_flow_app(flow_app):
    """Flow application smoke test"""

    # If the application starts normally without any errors
    flow_app.update()

    assert True


def test_all_activities_flow(flow_designer_window, tmp_path):
    """Create a simple flow using all Automagica activities"""
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


def test_console_frame(flow_designer_window):
    # Test variable explorer
    variable_explorer_window = (
        flow_designer_window.console_frame.on_open_variable_explorer_clicked()
    )
    variable_explorer_window.update()
    variable_explorer_window.destroy()

    # Test reset bot button
    flow_designer_window.console_frame.on_reset_bot_clicked()

    # Test clear button
    flow_designer_window.console_frame.on_clear_clicked()

    assert True


def test_flow_player(flow_designer_window):
    # Select start node
    flow_designer_window.flow.nodes[0].graph.add_to_selection()

    # Add a simple activity
    flow_designer_window.add_activity("automagica.activities.print_console")

    # Render window
    flow_designer_window.update()

    # Click run button
    flow_player_window = (
        flow_designer_window.toolbar_frame.clicked_run_button()
    )

    # Render Flow player window
    flow_player_window.update()

    assert True
