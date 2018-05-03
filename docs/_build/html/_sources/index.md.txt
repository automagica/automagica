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

## Basic functions

To open a browser choose 'Open Chrome browser' from menu or type the command:
```
browser = ChromeBrowser()
```

The browser function will wait until the page has fully loaded (that is, the “onload” event has fired) before continuing in the Automagica script. It’s worth noting that if your page uses a lot of AJAX on load then the browser function may not know when it has completely loaded.

Browse to a website by clicking 'Browse to URL' in the menu or use the command:
```
browser.get('https://mywebsite.com/')
```

Closing the browser can be done by:
```
browser.close()
```

An optional check to see if you are on the correct website is to check the title. For example if you are surfing to https://www.google.com, you might want to check if "Google" is in the title to make sure the bot surfed to the correct page.
```
browser = ChromeBrowser()
browser.get('https://google.com/')
if not "Google" in browser.title:
    errorbox("Site is not correct")
```

## Navigating

To navigate and perform actions in the browser it is crucial to locate elements. Elements can be everything in the html files of a website like text, titles, buttons, text fields, tables, etc...

### Quick start

There are two methods to finding elements, *find_element* to find a single element and *find_elements* to find multiple.
Arguably the easiest way to find a certain element is by copying it's xpath.

To do this in Chrome right click on the element you want to find, in the example below this is the "Google Search" button on Google.com. Click *inspect element* and a side tab with the html code opens with the element you selected highlighted in blue.

![Imgur](https://i.imgur.com/A2xdvUP.png)

In the html code, right click the highlighted block and select *Copy* -> *Copy Xpath*.

![Imgur](https://i.imgur.com/WRD46Xi.png)

You can now use the absolute Xpath to manipulate the element. However this is a fast method for prototyping, we do not recommend using absolute paths in production environments. Slight changes in the html code would cause the absolute path to change and to likely cause errors. A more in-depth overview in the next section.

### Selecting elements

#### Selection by name

Use this when you know name attribute of an element. With this strategy, the first element with the name attribute value matching the location will be returned. If no element has a matching name attribute, a NoSuchElementException will be raised.

For instance, consider these elements on a webpage:

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>

&nbsp;

The corresponding html code would be:

    <html>
     <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="loginbutton" type="submit" value="Login" />
      <input name="clearbutton" type="button" value="Clear" />
      </form>
     </body>
    <html>

The username and password field can be found by:

```
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
```

To fill in the fields:

```
username.send_keys("Automagica_User1")
password.send_keys("thisismypassword123")
```

To find and click on the login button:

```
login = driver.find_element_by_name('loginbutton')
login.click()
```

##### Side note

In case of double naming, finding by name always finds the first element. Imagine the following html code:

    <html>
     <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
      </form>
     </body>
    <html>

The following command will find the first element with the name "continue" and thus selecting the Login button:

```
continue = browser.find_element_by_name('continue')
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
- [ ] Add menu functionality for pop up boxes
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
