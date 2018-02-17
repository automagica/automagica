import os
import platform

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

def LaunchExcel():
    PressHotkey('win','r')
    Type('Excel')
    PressHotkey('enter')
    return

def LaunchWord():
    PressHotkey('win','r')
    Type('Word')
    PressHotkey('enter')
    return

def LaunchOutlook():
    PressHotkey('win','r')
    Type('Outlook')
    PressHotkey('enter')
    return

def LaunchPowerpoint():
    PressHotkey('win','r')
    Type('Powerpoint')
    PressHotkey('enter')
    return

from selenium.webdriver import Chrome

def ChromeBrowser():
    if platform.system() == 'Linux':
        chromedriver_path = '\\bin\\webdriver\\linux64\\chromedriver'
    elif platform.system() == 'Windows':
        chromedriver_path = '\\bin\\win32\\chromedriver.exe'
    else:
        chromedriver_path = '\\bin\\mac64\\chromedriver.exe'
    return Chrome(os.path.abspath(__file__).replace('activities.py','') + chromedriver_path)

