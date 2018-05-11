![](https://github.com/OakwoodAI/automagica/blob/master/images/logo.png)
# Automagica Client
Automagica is an open source Smart Robotic Process Automation (SRPA) platform. With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide a comprehensive and consistent wrapper around known and lesser known automation libraries.

![](https://github.com/OakwoodAI/automagica/blob/master/images/automagica_drawing.gif)

Refer to our [website](https://www.automagica.be) for more information, registered users can acces the [portal](https://portal.automagica.be). For more info see the [documentation](https://automagica.readthedocs.io).

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

### Failsafe

As a safety feature, a failsafe mechanism is enabled by default. You can trigger this by moving your mouse to the upper left corner of the screen. You can disable this by running the following command in the editor:
```
Failsafe(False)
```
## Examples

Browser working with Excel:

![](https://github.com/OakwoodAI/automagica/blob/master/images/browser_excel.gif)

SAP Automation (Real life example, sensitive information is blurred):

![](https://github.com/OakwoodAI/automagica/blob/master/images/sap.gif)


### Example code

This is a simple example that opens Notepad and types 'Hello world!'.

```
PressHotkey('win','r')
Wait(seconds=1)
Type(text='notepad', interval_seconds=0)
PressHotkey('enter')
Wait(seconds=2)
Type(text='Hello world!', interval_seconds=0.15)
```

This is a simple example that opens Chrome and goes to Google.com.

```
browser = ChromeBrowser()
browser.get('https://google.com')
```

For more info and examples see the [documentation](http://automagica.readthedocs.io/en/latest/).

## Important notes
For the `Type`-function to work, you need to set the "United States-International" keyboard layout on your system. If the keyboard layout is not available, outcomes of the function might be different.

## Credits
Under the hood, Automagica is built on some of the greatest open source libraries. Within Automagica, the following libraries are currently included:
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [Selenium](https://github.com/baijum/selenium-python)
- [PyWinAuto](https://github.com/pywinauto/pywinauto)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [OpenPyXL](https://bitbucket.org/openpyxl/openpyxl)
- [python-docx](https://github.com/python-openxml/python-docx)
- [pywin32](https://github.com/mhammond/pywin32)

A special thanks goes out to all the above-mentioned repository contributers! :heart:
