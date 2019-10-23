def home_path():
    """Returns the current user's home path
    :return: Path to the current user's home folder
    """
    from os.path import expanduser

    return expanduser("~")

def desktop_path():
    """Returns the current user's desktop path
    :return: Path to the current user's desktop folder
    """
    import os.path

    return os.path.join(os.path.expanduser('~'), 'Desktop')


def display_message_box(body, title="Message", type="info"):
    '''
    Shows a pop-up message with title and body. Three possible types, info, error and warning with the default value info.
    '''
    import tkinter
    from tkinter import messagebox

    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    if not body:
        messagebox.showwarning("Warning", "No input for message box")

    if type == "error":
        messagebox.showwarning(title, body)
    if type == "warning":
        messagebox.showwarning(title, body)
    if type == "info":
        messagebox.showinfo(title, body)
    return