from time import sleep

def Wait(seconds=None):
    sleep(seconds)


import pyautogui

# Renaming functions
PressHotkey = pyautogui.hotkey

def ClickOnPosition(x=None, y=None):
    return pyautogui.click(x, y)


def ClickOnImage(filename=None, double_click=False, right_click=False):
    x, y = pyautogui.locateCenterOnScreen(filename)
    clicks = 2 if double_click else 1
    if right_click:
        return pyautogui.rightClick(x, y)
    else:
        return pyautogui.click(x, y, clicks)

def Type(text=None, interval_seconds=None):
    return pyautogui.typewrite(text, interval=interval_seconds)

import pywinauto

def Launch(process_name=None):
    return pywinauto.Application().start(process_name)


def Failsafe(switch=True):
    pyautogui.FAILSAFE = switch
    return

def LaunchPaint():
    return pywinauto.Application().start('mspaint.exe')



