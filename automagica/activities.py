from time import sleep

def Wait(seconds=None):
    sleep(seconds)


from pyautogui import click, hotkey, moveTo, typewrite, locateCenterOnScreen, rightClick

# Renaming functions
PressHotkey = hotkey

def ClickOnPosition(x=None, y=None):
    click(x, y)


def ClickOnImage(filename=None, double_click=False, right_click=False):
    x, y = locateCenterOnScreen(filename)
    clicks = 2 if double_click else 1
    if right_click:
        rightClick(x, y)
    else:
        click(x, y, clicks)

def TypeInto(text=None, interval_seconds=None):
    typewrite(text, interval=interval_seconds)


from selenium.webdriver import Chrome as Browser
