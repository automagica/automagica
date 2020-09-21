import pytest

from automagica.gui.apps import AutomagicaTk

# This is required to launch a single instance of the Tkinter interpreter
# as launching the Tkinter interpreter multiple times from within the same
# Python process causes problems.
pytest.automagica_tk = AutomagicaTk()
