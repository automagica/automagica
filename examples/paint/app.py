from PIL import Image
from pyautogui import click, hotkey, moveTo, typewrite, locateCenterOnScreen, rightClick
import time
from automagica import *
from pywinauto import Application

app = Application().start('mspaint.exe')
app.Paint.move_window(x=0, y=0, width=740, height=580, repaint=True)


im = Image.open('example.jpg') 

X_total = im.size[0]
Y_total = im.size[1]
XY_total = X_total * Y_total


if X_total > Y_total:
    new_width  = 70
    new_height = int(new_width * (Y_total / X_total))
else:
    new_height = 70
    new_width  = int(new_height * (X_total / Y_total))

im= im.resize((new_width, new_height), Image.ANTIALIAS)

im = im.convert(mode='P', colors=16)
rgb_im = im.convert('RGB')

X_total = im.size[0]
Y_total = im.size[1]
XY_total = X_total * Y_total

instructions = []

x=1
y=1

while x < X_total-1:
    x = x + 1
    y = 1
    while y < Y_total-1:
        r, g, b = rgb_im.getpixel((x, y))
        instructions.append([4*x+30,4*y+165,r,g,b,3*r+4*g+6*b])
        y = y + 1

instructions.sort(key=lambda x: x[5], reverse=True)

print(instructions)

def colorpicker(r,g,b):
    click(624,83)
    click(624,83)
    click(555,362)
    click(555,362)
    time.sleep(0.1)
    typewrite(str(r))
    click(555,382)
    click(555,382)
    time.sleep(0.1)
    typewrite(str(g))
    click(555,412)
    click(555,412)
    time.sleep(0.1)
    typewrite(str(b))
    click(172,433)

    return

color = 1

#Select Paint window
click(325,17)

#Select correct tool
click(126,78)
time.sleep(0.1)

#Select thick line
click(125,167)
time.sleep(0.1)
click(271,16)
time.sleep(0.1)
click(270,78)
time.sleep(0.3)
click(312,267)

for item in instructions:
    if not (item[2] == 255 and item[3] == 255 and item[4] == 255): #drop white colors
        if not item[5] == color:
            colorpicker(item[2],item[3],item[4])
            color = item[5]
        click(item[0],item[1])
