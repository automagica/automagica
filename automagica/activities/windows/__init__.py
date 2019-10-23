
def set_user_password(username, password):
    """Sets the password for a Windows user.

    :parameter username: Username
    :parameter password: New password
    """
    from win32com import adsi

    user = adsi.ADsGetObject("WinNT://localhost/%s,user" % username)
    user.SetPassword(password)



def check_user_password(username, password):
    """Checks a password for a Windows user
    
    :parameter username: Username
    :parameter password: New password

    :return: True if the password is correct
    """
    from win32security import LogonUser
    from win32con import LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT
    try:
        LogonUser(username, None, password, LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT)
    except:
        return False
    return True


def is_logged_in():
    """Checks if the current user is logged in and not on the lockscreen. A lot of automations do not work properly when the desktop is locked.

    :return: True if the user is logged in
    """
    import subprocess

    output = subprocess.check_output('TASKLIST')

    if 'LogonUI.exe' in str(output):
        return False
    else: 
        return True


def desktop_locked():
    """Checks if the current user is locked out and on the lockscreen. A lot of automations do not work properly when the desktop is locked.

    :return: True when the lockscreen is active
    """
    return not is_logged_in()


def set_to_clipboard(text):
    """Set any text to the Windows clipboard. 
    Credit to Cees Timmerman (https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python)

    :parameter text: Text to put in the clipboard
    """
    import win32clipboard 

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

def get_from_clipboard():
    """Get the text currently in the Windows clipboard
    Credit to Cees Timmerman (https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python)

    :return: Text currently in the clipboard
    """
    import win32clipboard 

    win32clipboard.OpenClipboard()
    try:
        data = str(win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT))
        return data

    except Exception as e:
        raise e

    finally:
        win32clipboard.CloseClipboard()


def clear_clipboard():
    """Empty the clipboard
    """
    set_to_clipboard('')