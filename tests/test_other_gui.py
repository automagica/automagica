import pytest

from automagica.gui.windows import NotificationWindow, KeybindsOverviewWindow


def test_notification_window():
    """Test notification window"""

    windows = [
        NotificationWindow(
            pytest.automagica_tk, f"Hello world nr. {i}", duration=2
        )
        for i in range(10)
    ]

    for window in windows:
        window.update()
        window.destroy()

    assert True


def test_keybind_window():
    """Test keybind window"""
    window = KeybindsOverviewWindow(pytest.automagica_tk)
    window.update()

    keybind_window = window.add_button_clicked()
    keybind_window.update()

    keybind_window.destroy()
    window.destroy()

    assert True
