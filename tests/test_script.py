import pytest

from automagica.gui.apps import ScriptApp


@pytest.mark.smoke
def test_script_output(tmp_path, capsys):
    app = ScriptApp()

    d = tmp_path / "scripts"
    d.mkdir()

    with open(d / "script.py", "w") as f:
        f.write("print('Hello world')")

    app.run(d / "script.py")

    captured = capsys.readouterr()

    assert "Hello world" in captured.out
