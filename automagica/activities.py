from time import sleep

def Wait(seconds=None):
    sleep(seconds)


from pyautogui import click, hotkey, moveTo, typewrite, locateCenterOnScreen, rightClick

# Renaming functions
PressHotkey = hotkey

def ClickOnPosition(x=None, y=None):
    return click(x, y)


def ClickOnImage(filename=None, double_click=False, right_click=False):
    x, y = locateCenterOnScreen(filename)
    clicks = 2 if double_click else 1
    if right_click:
        return rightClick(x, y)
    else:
        return click(x, y, clicks)

def TypeInto(text=None, interval_seconds=None):
    return typewrite(text, interval=interval_seconds)


from selenium.webdriver import Chrome as Browser

from pywinauto import Application

def Launch(process_name=None):
    return Application().start(process_name)

from pyautogui import FAILSAFE

def Failsafe(switch=True):
    FAILSAFE = switch
    return

def LaunchPaint():
    return Application().start('mspaint.exe')



