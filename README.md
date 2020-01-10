![](https://github.com/OakwoodAI/automagica/blob/master/images/logo.png)
# Automagica
Automagica is an open source Smart Robotic Process Automation (SRPA) platform. With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide a comprehensive and consistent wrapper around known and lesser known automation libraries .

![](https://github.com/OakwoodAI/automagica/blob/master/images/automagica_drawing.gif)

Refer to our [website](https://www.automagica.com) for more information, registered users can access the [portal](https://portal.automagica.com). For more info see the [documentation](https://portal.automagica.com).

## Important update!
- [Portal 2.0](https://portal.automagica.com) is now live!
- You can still access the old portal on [old portal](https://portal.automagica.io)
- Follow our [blog](https://automagica.com) to stay up to date with the latest changes!


## Need expert support?
We can support you end-to-end in all your automation needs, from estimating automation potential for processes to technical implementation and integration. Please send an e-mail to [sales@automagica.be](mailto:sales@automagica.be) for enquiries and rates.

## Getting started

## Installation

For Windows you can download the one-click installer on [portal](https://portal.automagica.com).

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

Browser working with Excel:

![](https://github.com/OakwoodAI/automagica/blob/master/images/browser_excel.gif)

SAP Automation (Production example, sensitive information is blurred):

![](https://github.com/OakwoodAI/automagica/blob/master/images/sap.gif)

Folder and File manipulation

<img src="https://github.com/OakwoodAI/automagica/blob/master/images/USPresidents.gif" width="800">


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

A special thanks goes out to all the above-mentioned repository contributers! :heart:
