"""Copyright 2020 Oakwood Technologies BVBA"""


from automagica.gui.apps import FlowApp


def test_flow_app():
    """
    Testing scenario to test Automagica Flow application
    """
    app = FlowApp()
    app.destroy()
    app.quit()

