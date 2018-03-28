![](https://github.com/OakwoodAI/automagica/blob/master/images/logo.png)
# Automagica Client
Automagica is an open source Smart Robotic Process Automation (SRPA) platform. With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide a comprehensive and consistent wrapper around known and lesser known automation libraries.

![](https://github.com/OakwoodAI/automagica/blob/master/images/automagica_drawing.gif)

Refer to our website for more information: https://portal.automagica.be

## Getting started

### Prerequisites
1. Python 3.6.4 from https://www.python.org
2. Automagica Bot ID - get one from https://portal.automagica.be

### Installation instructions
Install Automagica on the bot host machine:
```
pip install https://github.com/OakwoodAI/automagica/tarball/master
```

#### Optional (to enable Optical Character Recognition)
For _Windows_, install Tesseract 4 [from here](http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe).

For _Linux_ (Ubuntu):
```
sudo apt-get install tesseract-ocr
```
For _MacOS_:
```
brw install tesseract
```
## Running the Bot
1. Get your Automagica Bot ID from https://portal.automagica.be
2. In command line or terminal run following command. Replace `<bot_id>` with your Bot ID.
```
automagica <bot_id>
```
If you do not provide a Bot ID, the application will ask for it.

### Failsafe

As a safety feature, a failsafe mechanism is enabled by default. You can trigger this by moving your mouse to the upper left corner of the screen. You can disable this by running the following command in the editor:
```
Failsafe(False)
```

## Example

This is a simple example that opens Chrome and enters 'Hello world!' in the search bar.

```
PressHotkey('win','r')
Wait(seconds=1)
Type(text='chrome', interval_seconds=0)
PressHotkey('enter')
Wait(seconds=3)
Type(text='Hello world!', interval_seconds=0)
Wait(seconds=1)
PressHotkey('enter')
```

## Credits
Under the hood, Automagica is built on some of the greatest open source libraries. Within Automagica, the following libraries are currently included:
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [socketIO-client](https://pypi.python.org/pypi/socketIO-client)
- [Selenium](https://github.com/baijum/selenium-python)
- [PyWinAuto](https://github.com/pywinauto/pywinauto)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [OpenPyXL](https://bitbucket.org/openpyxl/openpyxl)
- [python-docx](https://github.com/python-openxml/python-docx)
- [pywin32](https://github.com/mhammond/pywin32)

A special thanks goes out to all the above-mentioned repository contributers! :heart:
