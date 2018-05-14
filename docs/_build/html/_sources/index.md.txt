Automagica Documentation

This is the documentation for automating in Automagica Smart Automation.
Automagica is based on the Python language.

![Automagica](https://raw.githubusercontent.com/OakwoodAI/automagica/master/images/logo.png)

# Table of contents

- [Getting Started](#getting-started)
	- [Prerequisites](#Prerequisites)
	- [Installing instructions](#installing-instructions)
- [Browser Automation](#browser-automation)
	- [Basic functions](#basic-functions)
	- [Navigating](#navigating)
		- [Quick start](#quick-start)
		- [Selecting elements](#selecting-elements)
			- [Selection by name](#selection-by-name)
			- [Selection by Id](#selection-by-id)
		- [Selection by Xpath](#selection-by-xpath)
		- [Browsing Example](#browsing-example)
- [Office Automation](#office-automation)
	- [Word](#word)
	- [Excel](#excel)
- [Basic operations](#basic-operations)
	- [Variables and Types](#variables-and-types)
		- [Strings](#strings)
			- [String manipulation](#string-manipulation)
				- [Adding variables to a string](#adding-variables-to-a-string)
				- [Slicing strings](#slicing-strings)
				- [String replacing](#string-replacing)
				- [Upper and lower cases in strings](#upper-and-lower-cases-in-strings)
				- [Splitting strings](#splitting-strings)
		- [Numbers](#numbers)
			- [Integers](#integers)
			- [Floats](#floats)
		- [Math operations](#math-operations)
	- [Lists](#lists)
	- [Logic operations](#logic-operations)
		- [If statement](#if-statement)
		- [While loops](#while-loops)
		- [For loops](#for-loops)
- [Examples](#examples)
- [Credits](#credits)

# Getting started


Refer to our [website](https://www.automagica.be) for more information, registered users can acces the [portal](https://portal.automagica.be). More details also available on our [github](https://github.com/OakwoodAI/automagica).

Alternatively you can use Automagica locally by starting your Python script with:
```
from automagica import *
```

For a step-to-step tutorial on how to install and configure Python see [this video](https://www.youtube.com/watch?v=cpPG0bKHYKc).<br/>
For a step-to-step tutorial on how to build and run a Python script see [this video](https://www.youtube.com/watch?v=hFhiV5X5QM4).

## Prerequisites
- Python 3.6.4 from [www.python.org](https://www.python.org)

## Installation instructions
Install Automagica on the bot host machine:
```
pip install https://github.com/OakwoodAI/automagica/tarball/master
```

### Optional Optical Character Recognition
For _Windows_, install Tesseract 4 [from here](http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe).

For _Linux_ (Ubuntu):
```
sudo apt-get install tesseract-ocr
```
For _MacOS_:
```
brw install tesseract
```

## Failsafe

As a safety feature, a failsafe mechanism is enabled by default. You can trigger this by moving your mouse to the upper left corner of the screen. You can disable this by running the following command:
```
Failsafe(False)
```
## Examples

For some animated examples see: [Browser working with Excel](https://raw.githubusercontent.com/OakwoodAI/automagica/master/images/browser_excel.gif) and [SAP Automation](https://github.com/OakwoodAI/automagica/blob/master/images/sap.gif)

# Browser Automation

Out-of-the box Automagica uses Chrome as automated browser. The following sections will explain how to find, read and manipulate web elements.

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

To move backward and forward in your browser’s history:
```
browser.forward()
browser.back()
```

To click on an element:
```
element.click()
```

To enter text into a text field:
```
element.send_keys("some text")
```

To clear an element:
```
element.clear()
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
Arguably the easiest way to find a certain element is by copying it's XPath.

To do this in Chrome right click on the element you want to find, in the example below this is the "Google Search" button on Google.com. Click *inspect element* and a side tab with the html code opens with the element you selected highlighted in blue.

![Imgur](https://i.imgur.com/A2xdvUP.png)

In the html code, right click the highlighted block and select *Copy* -> *Copy XPath*.

![Imgur](https://i.imgur.com/WRD46Xi.png)

You can now use the absolute XPath to manipulate the element. However this is a fast method for prototyping, we do not recommend using absolute paths in production environments. Slight changes in the html code would cause the absolute path to change and to likely cause errors. A more in-depth overview in the next section.

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
login = browser.find_element_by_name('loginbutton')
login.click()
```

**Side note**

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

#### Selection by Id

You can select elements by Id when this is known. This is a robust method, yet generally nog every element had a known id tag. Consider the html code below:

    <html>
     <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="continue" type="submit" value="Login" />
      </form>
     </body>
    <html>

In this case the form has an id "loginForm". Hence the form can be selected with the Id by:

```
loginform = browser.find_element_by_id('loginForm')
```

### Selection by Xpath

XPath (XML Path Language) is a query language for selecting nodes from an XML document. Since HTML can be an implementation of XML (referred to as XHTML), this language can be used to find and manipulate target elements in web applications.

The advantage of using XPath is the possibility to reach every element within an HTML structure. See [Quick start](#quick-start) for a visual introduction on how to find and use an element with XPath.
The disadvantage of using a full XPath is that it is not very robust. Even the slightest changes in a HTML page would cause absolute XPaths to change, which in result will likely cause your robot unable to find the correct elements. Note that this is different from using an element name or id, as elements will still be able to be found with changes in the HTML page as long as the name or id remains the same.

Therefore, when working with Xpath the robustness can be increased by finding a nearby element with an id or name attribute (ideally a parent element), so you can locate your target element based on the relationship.

Consider the following structure on a HTML page:

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

With the following source code:

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


**Selecting the username:**

1. Absolute path (note that this would break if the HTML was changed only slightly)
2. Point to the first element in the form
3. First input element with attribute named ‘name’ and the value username
```
username = browser.find_element_by_xpath("//form[input/@name='username']")
username = browser.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = browser.find_element_by_xpath("//input[@name='username']")
```

**The "clear" button can be located by:**

1. Fourth input element of the form element with attribute named id and value loginForm
2. Input with attribute named name and the value continue and attribute named type and the value button
```
clear_button = browser.find_element_by_xpath("//form[@id='loginForm']/input[4]")
clear_button = browser.find_element_by_xpath("//input[@name='continue'][@type='button']")
```

**The form can be selected by:**

1. Absolute path (note that this would break if the HTML was changed only slightly):
2. First form element in the HTML
3. The form element with attribute named id and the value loginForm
```
login_form = browser.find_element_by_xpath("/html/body/form[1]")
login_form = browser.find_element_by_xpath("//form[1]")
login_form = browser.find_element_by_xpath("//form[@id='loginForm']")
```

### Browsing Example

The following example browses to Google, searches for Automagica, opens the first Google Search result link

```
# Open Chrome
browser = ChromeBrowser()

# Browse to Google
browser.get('https://google.com')

# Enter Search Text
browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('automagica')

# Submit
browser.find_element_by_xpath('//*[@id="lst-ib"]').submit()

# Click the first link
browser.find_elements_by_class_name('r')[0].click()
```

# Office Automation

A lot of automation processes involve Microsoft Office. Automagica packs some useful functions to make automating office as easy as possible.

## Word

To open a Word document:
```
document = OpenWordDocument('example.docx')
```

Replace words in a Word document. This can be particularly useful when using templates for forms. Make sure the template contains unique placeholder ariables so that automated filling doesn't cause ambiguities.

```
document = ReplaceTextInDocument(document, text='[placeholder]', replace_with='My text')
```

Converting a Word document to PDF:
```
ConvertWordToPDF(word_filename='C:\\document.docx', pdf_filename='C:\\document.pdf')
```

## Excel

Automation in Excel most of the time requires reading and writing cells. In Automagica, this is very easy.

You can either enter a row and a cell e.g. row = 1, cell = 1 or define a cell name e.g. cell="A2".
Note that the first row is defined as row number 1 and the first column is defined column number 1.
```
#Using row and column
ExcelReadCell(C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx,1,1)
#Using cell value
ExcelReadCell(C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx,cell=A1)
```

And similar for writing a cell:
```
#Using row and column
ExcelWriteCell(C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx,1,1,value="Robot")
#Using cell value
ExcelWriteCell(C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx,cell=A1,value="Robot")
```


# Basic operations

## Variables and Types

Variables are used to store information to be referenced and manipulated in an automation script. They also provide a way of labeling data with a descriptive name, so the automation script can be understood more clearly by the reader. It is helpful to think of variables as containers that hold information. Variables come in a great variety of types. Automagica supports all variable types from the Python language, but down here are some of the most prominent.

### Strings


A string is any finite sequence of characters (i.e., letters, numerals, symbols and punctuation marks).
Strings are defined either with a single quote or a double quotes.

```
automagica_string = "robots"
DisplayMessageBox(automagica_string)
```

#### String manipulation

##### Adding variables to a string

You can add all variables to a string. If you want, for example, to add an interger to a string you can do so by defining the integer as a string:

```
automagica_string = "robot number "
automagica_integer = 100

automagica_string2 = automagica_string + int(100)
DisplayMessageBox(automagica_string2)
```

##### Slicing strings

Adding **[n]** to a string will select the nth character:
```
x = "automagica"
x[2]
>>> t
```

Adding **[n:p]** will slice the string from character n to p. By leaving n or p out it will select the first and last character respectively:
```
x = "Hello Robot!"
x[:5]
>>> Hello
```
##### String replacing
```
x = "Robots are evil!"
x.replace('evil', 'friendly')
>>>Robots are friendly!
```

##### Upper and lower cases in strings
```
x = "Robots"
#Convert to upper case
x.upper()
#Convert to lower case
x.lower()
#Capitalize
x.capitalize()
```

##### Splitting strings

You can choose to split a string at a certain word or character. Don't forget to indicate if you want to keep the first or second part of the string by adding [0] or [1] as splitting causes your string to turn in to a list of multiple strings:
```
x = "Robots will take over the world!"
x.split(" over ")
>>>['Robots will take', 'the world!']
#Accesing the different strings can be done by:
x[0]
>>>Robots will take
x[1]
>>>the world!"
```

### Numbers

#### Integers

An integer (of int in short) is a whole number, not a fractional number, that can be positive, negative, or zero.

To declare and display an integer:
```
automagica_integer = 5
DisplayMessageBox(automagica_integer)
```

You can do basic math manipulations with integers:

```
automagica_int1 = 5
automagica_int2 = 10

automagica_int3 = automagica_int1 + automagica_int2 = 15
DisplayMessageBox(automagica_int3)
```

#### Floats

Floats represent real numbers and are written with a decimal point dividing the integer and fractional parts.
```
automagica_float = 3.1
DisplayMessageBox(automagica_float)
```

### Math operations

Down here is a list with basic math operations that can be used with both intergers and floats:


**abs(x)** : The absolute value of x (the (positive) distance between x and zero)
```
x = -3
abs(x)
>>> 3
```
**ceil(x)** : The ceiling of x (the smallest integer not less than x)
```
x = 4.1
ceil(x)
>>> 5
```
**exp(x)** : The exponential of x: e<sup>x</sup>
```
x = 3
ceil(x)
>>> 20.085536923187668
```
**floor(x)** : The floor of x: the largest integer not greater than x
```
x = 4.1
floor(x)
>>> 4
```
**log(x)** : The natural logarithm of x, for x> 0
```
x = 10
floor(x)
>>> 2.302585092994046
```
**max(x1, x2,...)** and **max(x1, x2,...)** :  The smallest and largest of its arguments: the value closest to positive infinity
```
x1 = 2
x2 = 3
max(x1,x2)
>>> 3
```
**round(x)** : x rounded to n digits from the decimal point.
```
x = 0.5
round(0.5)
>>> 1
```
**sqrt(x)** : The square root of x for x > 0
```
x = 9
sqrt(9)
>>> 3
```

## Lists

Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Down here some examples of list usage:

```
list = ["R2-D2", "Terminator", "Optimus Prime","WALL-E", "RoboCop"]
list.append("WALL-E")
list.append("RoboCop")
>>>["R2-D2", "Terminator", "Optimus Prime","WALL-E", "RoboCop"]
list[0]
>>>R2-D2
```

## Logic operations

### If statement

An *if statement* is used for decision making. It will run the body of code only when if statement is true.
The conditional block of code has to be intended.

if condition :
    indentedStatementBlock



An example would be:

```
temperature = RequestUserInput()
if temperature > 20:
    DisplayMessageBox("Wear short pants!")
```

Expanding this example to multiple if statements:

```
temperature = RequestUserInput()
if temperature < 10:
    DisplayMessageBox("Wear a warm hat!")
if temperature > 20:
    DisplayMessageBox("Wear short pants!")
else:
    DisplayMessageBox("You can wear normal clothes!")
```
The previous example will ouptut the string *"Wear a warm hat!"* if the inputnumber was lower than 10. If the number was higher than 20, the output will be *Wear short pants!*. If the condition was still not met, which means the input number was between 10 and 20, the else statement will be activated. In that case the message will show *"You can wear normal clothes!"*.

### While loops

The while loop evaluates the test expression.

If the test expression is true (nonzero), codes inside the body of while loop are exectued. The test expression is evaluated again. The process goes on until the test expression is false.

When the test expression is false, the while loop is terminated.

![Imgur](https://i.imgur.com/rh3OUdh.jpg)

An example of a while loop:
```
automagica_count = 0
while (automagica_count < 3):
   display_string = "Current count is: " + str(automagica_count)
   DisplayMessageBox(display_string)
   count = count + 1
```


### For loops

The initialization statement is executed only once.

Then, the test expression is evaluated. If the test expression is false (0), for loop is terminated. But if the test expression is true (nonzero), codes inside the body of for loop is executed and the update expression is updated.

This process repeats until the test expression is false.

The for loop is commonly used when the number of iterations is known.

![Imgur](https://i.imgur.com/V3p8spl.jpg)

An example of a for loop:
```
for x in range(0, 2):
    display_string = "We are currently at number " + str(x)
    DisplayMessageBox(display_string)
```

# Examples

The following example opens Excel and reads a worksheet with the following layout:

![Imgur](https://i.imgur.com/jMj2ypX.png)

It opens Chrome and surfs to google.com where the robot enters the searchterm. It then collects all the urls from the first page and writes these urls in Excel in the correct cell.

```
excel_path = "Enter Path to Excel Here" #example: C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx

# Read information from the excel in the second row, for columns 2 to 10
lookup_terms = []
for col in range(2,10):
    try:
        lookup_terms.append(ExcelReadCell(excel_path, 2, col))
    except:
        pass

# Open Chrome
browser = ChromeBrowser()

for j,item in enumerate(lookup_terms):

    # Browse to Google
    browser.get('https://google.com')
    # Lookup the searchterm
    browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(item)
    # Search
    browser.find_element_by_xpath('//*[@id="lst-ib"]').submit()
    # Get all found items
    articles = browser.find_elements_by_class_name("g")
    # Parse the headertexts to find the urls
    urls = []
    for article in articles:
        try:
            import re
            urls.append(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', article.text)[0])
        except:
            pass

    # Write found urls to Excel
    for i,url in enumerate(urls):
        ExcelWriteCell(excel_path, row=i+2, col=j+2, write_value=url)

# Exit the browser
browser.quit()
```

If you open the Excel file, the result should look something like this:

![Imgur](https://i.imgur.com/7gSv7gc.png)

Note that the links differ depending on your location, as google search results are location dependant.


## Credits
Under the hood, Automagica is built on some of the greatest open source libraries as listed down below. Large parts of the documentation is based on theirs. Special thanks to all contributors of these great libraries!

- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [Selenium](https://github.com/baijum/selenium-python)
- [PyWinAuto](https://github.com/pywinauto/pywinauto)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [OpenPyXL](https://bitbucket.org/openpyxl/openpyxl)
- [python-docx](https://github.com/python-openxml/python-docx)
- [pywin32](https://github.com/mhammond/pywin32)
