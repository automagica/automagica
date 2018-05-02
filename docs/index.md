Automagica Documentation
======================================

This is the documentation for Automagica Robotic Process Automation.

Testsectie
======================================

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

# Browser Automation

Out-of-the box Automagica uses Chrome as automated browser. Go to advanced browser automation if you want to change the browser or for more in depth settings.

## Starting the browser

To open a browser choose 'Open Chrome browser' from menu or type the command:
```
browser = ChromeBrowser()
```

The browser function will wait until the page has fully loaded (that is, the “onload” event has fired) before continuing in the Automagica script. It’s worth noting that if your page uses a lot of AJAX on load then the browser function may not know when it has completely loaded.

Browse to a website by clicking 'Browse to URL' in the menu or use the command:
```
browser.get('https://mywebsite.com/')
```
An optional check to see if you are on the correct website is to check the title. For example if you are surfing to https://www.google.com, you might want to check if "Google" is in the title to make sure the bot surfed to the correct page.
```
browser = ChromeBrowser()
browser.get('https://google.com/')
assert "Python" in driver.title
```


## Navigating the browser





Selenium: http://selenium-python.readthedocs.io/
SAP
Basic Python
Mouse
Examples

### To Do:

- [ ] How to use different browser
- [ ] Add chrome options for headless browsing
- [ ] Add chrome options for not loading images
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 


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

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
