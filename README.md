![](https://github.com/OakwoodAI/automagica/blob/master/images/logo.png)
# Automagica
Automagica is an open source Smart Robotic Process Automation (SRPA) platform. With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide a comprehensive and consistent wrapper around known and lesser known automation libraries .

<align="center" img src="https://github.com/OakwoodAI/automagica/blob/master/images/automagica_drawing.gif">

Refer to our [website](https://www.automagica.com) for more information, registered users can access the [portal](https://portal.automagica.com). For more info see the [documentation](https://portal.automagica.com).

## Important update!
- [Portal 2.0](https://portal.automagica.com) is now live!
- You can still access the old portal on [old portal](https://portal.automagica.io)
- Follow our [blog](https://automagica.com) to stay up to date with the latest changes!


## Need expert support?
We can support you end-to-end in all your automation needs, from estimating automation potential for processes to technical implementation and integration. Please send an e-mail to [sales@automagica.be](mailto:sales@automagica.be) for enquiries and rates.

## Getting started

## Installation

For Windows you can download the one-click installer on the [Automagica Portal](https://portal.automagica.com/register).

![](https://github.com/OakwoodAI/automagica/blob/master/images/portal_screenshots.JPG)

#### Developers 

#### Developer Installation

If you wish to only install the open source component without the portal functionalities:

Download and install [Python 3.7](https://www.python.org)

Install the latest version Automagica on your machine:
```
pip install automagica --upgrade
```

#### Developer Uninstall procedure

To remove Automagica, run the following commands:
```
pip uninstall automagica
```

#### Importing the activities

Before getting started in development mode, don't forget to import the activities from automagica in your python script. If unsure, it is possible to import all the activities for development purposes by starting your script with:
```
from automagica import *
```
### Support

Automagica officially supports Windows 10. Linux and MacOS are not officially supported.

## Examples

Try out the one-click examples:
* [Webscraping in Chrome](https://portal.automagica.com/register)
* [Read and write data in Excel](https://portal.automagica.com/register)
* [Automatically make a PowerPoint presentation](https://portal.automagica.com/register)
* [Change your Windows wallpaper](https://portal.automagica.com/register)
* [Manipulate files and folders](https://portal.automagica.com/register)
* [Use OCR to read images and click buttons](https://portal.automagica.com/register)

Browser working with Excel:

![Excel Example Automagica](https://github.com/OakwoodAI/automagica/blob/master/images/browser_excel.gif)

SAP Automation (Production example, sensitive information is blurred):

![Sap Example Automagica](https://github.com/OakwoodAI/automagica/blob/master/images/sap.gif)

Folder and File manipulation

<img src="https://github.com/OakwoodAI/automagica/blob/master/images/USPresidents.gif" width="800">

## Activities

An overview of all official Automagica activities:

Cryptography | Description
------------ | -----------
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/key-solid.svg" width="20"> Random key | Generate random Fernet key. Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-solid.svg" width="20"> Encrypt text | Encrypt text with (Fernet) key,
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/open-solid.svg" width="20"> Decrypt text | Dexrypt bytes-like object to string with (Fernet) key
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-solid.svg" width="20"> Encrypt file | Encrypt file with (Fernet) key. Note that file will be unusable unless unlocked with the same key.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/open-solid.svg" width="20"> Decrypt file | Decrypts file with (Fernet) key
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-solid.svg" width="20"> Key from password | Generate key based on password and salt. If both password and salt are known the key can be regenerated.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/fingerprint-solid.svg" width="20"> Hash from file | Generate hash from file
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/fingerprint-solid.svg" width="20"> Hash from text | Generate hash from text


Random | Description
------ | -----------
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/dice-solid.svg" width="20"> Random number | Random numbers can be integers (not a fractional number) or a float (fractional number).
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/coins-solid.svg" width="20"> Random boolean | Generates a random boolean (True or False)
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/comment-solid.svg" width="20"> Random name | Generates a random name. Adding a locale adds a more common name in the specified locale. Provides first name and last name.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/map-solid.svg" width="20"> Random address | Generates a random address. Specifying locale changes random locations and streetnames based on locale.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/up-solid.svg" width="20"> Random beep | Generates a random beep, only works on Windows
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/calendar-solid.svg" width="20"> Random date | Generates a random date.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/random-solid.svg" width="20"> Generate unique identifier | Generates a random UUID4 (universally unique identifier). While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible.


User Input | Description
---------- | -----------
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/maximize-solid.svg" width="20"> Ask user for input | Prompt the user for an input with a pop-up window.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/maximize-solid.svg" width="20"> Ask user for password | Prompt the user for a password. The password will be masked on screen while entering.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/maximize-solid.svg" width="20"> Ask user for credentials | Prompt a popup which asks user for username and password and returns in plain text. Password will be masked.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/maximize-solid.svg" width="20"> Shows message box | A pop-up message with title and message.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/tv-solid.svg" width="20"> Display overlay message | Display custom OSD (on-screen display) message. Can be used to display a message for a limited amount of time. Can be used for illustration, debugging or as OSD.

## Credits
Under the hood, Automagica is built on some of the greatest open source libraries. Within Automagica, the following libraries are currently included:
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [Selenium](https://github.com/baijum/selenium-python)
- [PyWinAuto](https://github.com/pywinauto/pywinauto)
- [OpenPyXL](https://bitbucket.org/openpyxl/openpyxl)
- [python-docx](https://github.com/python-openxml/python-docx)
- [pywin32](https://github.com/mhammond/pywin32)
- [PyPDF2](https://github.com/mstamy2/PyPDF2)
- [Psutil](https://pypi.org/project/psutil/)
- [py-trello](https://github.com/sarumont/py-trello)
- [plyer](https://pypi.org/project/plyer/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Faker](https://github.com/joke2k/faker)
- [Psutil](https://pypi.org/project/psutil/)
- [Keyring](https://pypi.org/project/keyring/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [Cryptography](https://pypi.org/project/cryptography/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pyad](https://pypi.org/project/pyad/)
- [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/)
- [Icons8 Line Awesome](https://github.com/icons8/line-awesome)

A special thanks goes out to all the above-mentioned repository contributers! :heart:
