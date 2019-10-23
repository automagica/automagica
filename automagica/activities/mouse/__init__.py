
def get_position():
    '''
    Displays a message box with the absolute coordinates of the current position of the mouse.
    '''
    from pyautogui import position
    from automagica.activities.utilities import display_message_box

    coord = position()
    coordstring = "x: " + str(coord[0]) + "\r\ny: " + str(coord[1]) + ""
    return display_message_box(coordstring, "Mouse Position")


def click(x=None, y=None):
    '''
    Clicks on a pixel position on the visible screen determined by x and y coördinates.
    '''
    from pyautogui import click

    return click(x, y)


def double_click(x=None, y=None):
    '''
    Double clicks on a pixel position on the visible screen determined by x and y coördinates.
    '''
    from pyautogui import doubleClick

    return doubleClick(x, y)


def right_click(x=None, y=None):
    '''
    Right clicks on a pixel position on the visible screen determined by x and y coördinates.
    '''
    from pyautogui import rightClick

    return rightClick(x, y)


def move_to(x=None, y=None):
    '''
    Moves te pointer to a x-y position.
    '''
    from pyautogui import moveTo

    return moveTo(x, y)


def move_relative(x=None, y=None):
    '''
    Moves the mouse an x- and y- distance relative to its current pixel position.
    '''
    from pyautogui import moveRel

    return moveRel(x, y)


def drag_to(x=None, y=None, button="left"):
    '''
    Drag the mouse from its current position to a entered x-y position, while holding a specified button.
    '''
    from pyautogui import dragTo

    return dragTo(x, y, 0.2, button=button)


def click_image(filename=None):
    from pyautogui import locateCenterOnScreen, click

    x, y = locateCenterOnScreen(filename)

    return click(x, y)

def double_click_image(filename=None):
    from pyautogui import locateCenterOnScreen, click

    x, y = locateCenterOnScreen(filename)

    return click(x, y, 2)

def right_click_image(filename=None):
    from pyautogui import locateCenterOnScreen, rightClick

    x, y = locateCenterOnScreen(filename)

    return rightClick(x, y)

def wait_for_image(filename=None, timeout=120):
    """
    Waits for an image to appear on the screen
    """
    from pyautogui import locateCenterOnScreen
    from time import sleep

    for _ in range(timeout):
        try:
            locateCenterOnScreen(filename)
            break
        except TypeError:
            sleep(1)
