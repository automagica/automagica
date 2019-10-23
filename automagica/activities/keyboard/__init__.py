
def press_key(key=None):
    '''Press and release an entered key.
    '''
    from pyautogui import press

    if key:
        return press(key)


def press_key_combination(first_key, second_key, third_key=None):
    '''Press a combination of two or three keys simultaneously.
    '''
    from pyautogui import hotkey

    if not third_key:
        return hotkey(first_key, second_key)
    if third_key:
        return hotkey(first_key, second_key, third_key)


def type_keys(text=None, interval_seconds=0.001):
    '''
    Type text in the current active field. The first argument represent the text and is entered as a string. 
    The second variable is the time between two keystrokes. Pay attention that you can only press single 
    character keys. Keys like ":", "F1",... can not be part of the text argument.
    '''
    from pyautogui import typewrite
    import platform
    
    # Set keyboard layout for Windows platform
    if platform.system() == 'Windows':
        from win32api import LoadKeyboardLayout
        LoadKeyboardLayout('00000409', 1)
    return typewrite(text, interval=interval_seconds)
