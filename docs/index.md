Automagica Documentation

This is the documentation for automating in Automagica Smart Automation.
Automagica is based on the Python language.

![Automagica](https://raw.githubusercontent.com/OakwoodAI/automagica/master/images/logo.png)

# Table of contents

- [Getting Started](#getting-started)
	- [Prerequisites](#Prerequisites)
	- [Installing instructions](#installing-instructions)
	- [Failsafe](#failsafe)
	- [Examples](#examples)
	- [Automagica with Natural Language](#automagica-with-natural-language-for-prototyping)
- [Mouse And Keyboard Automation](#mouse-and-keyboard-automation)
    - [Mouse](#mouse)
        - [Coördinate Sysem](#coordinate-system)
        - [Functions](#functions)
    - [Keyboard](#keyboard)
- [Browser Automation](#browser-automation)
	- [Basic functions](#basic-functions)
	- [Navigating](#navigating)
		- [Quick start](#quick-start)
		- [Selecting elements](#selecting-elements)
			- [Selection by name](#selection-by-name)
			- [Selection by Id](#selection-by-id)
		- [Selection by Xpath](#selection-by-xpath)
		- [Browsing Example](#browsing-example)
- [Process Acivities](#process-activities)
    - [Standard Windows Applications](#windows-applications)
    - [General Commands](#general-commands)
    - [Running Programs](#running-programs)
- [Monitoring](#monitoring)
- [Office Automation](#office-automation)
    - [Entering Pathnames](#entering-pathnames)
	- [Word](#word)
	- [Excel](#excel)
        - [Reading And Writing](#reading-and-writing)
        - [Basic Operations](#basic-operations)
- [PDF Manipulation](#pdf-manipulation)
    - [Merge PDF Files](#merge-pdf-files)
    - [Extract Text From PDF](#extract-text-from-pdf)
- [File And Folder Manipulation](#file-folder-automation)
    - [Files](#files)
        - [Open A File](#open-a-file)
        - [Renaming Files](#renaming-files)
        - [Moving Files](#moving-files)
        - [Copying Files](#copying-files)
        - [Removing Files](#removing-files)
        - [Check If A File Exists](#check-if-a-file-exists)
    - [Folders](#folders)
        - [Creating Folders](#creating-folders)
        - [Open A Folders](#opening-folders)
        - [Renaming Folders](#renaming-folders)
        - [Moving Folders](#moving-folders)
        - [Copying Folders](#copying-folders)
        - [Removing Folders](#removing-folders)
        - [Empty A Folder](#empty-a-folder)
        - [Check If A Folder Exists](#check-if-a-folder-exists)
        - [Zip Folder](#zip-folder)
        - [UnZip Folder](#unzip-folder)
- [Image Operations](#image-operations)
- [Email Operations](#email-operations)
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

## Automagica with Natural Language for prototyping

Wouldn't it be cool if we could write Robotic Process Automation scripts in plain ol' English rather than the already easy Python scripting language? Well it's possible with Automagica! We have cooked up a more human-friendly interface to get started with automation !

### How it works
Natural language for Automagica (.nla) looks like this:
```
open the browser
navigate to google.com
search for oranges
```

### Try it yourself

NLP is handled by Wit.ai. A Wit.ai key is included, so you can get a headstart!

Install (in addition to the above) the following required package:
```
pip install https://github.com/OakwoodAI/understanding/tarball/master
```
Then install Natural Language for Automagica:
```
git clone https://github.com/OakwoodAI/natural-language-automagica
cd natural-language-automagica
pip install .
```

Then you can get started by running the examples:
```
cd examples
nla google.nla
nla wikipedia.nla
nla youtube.nla
```

Automagica with natural language is still in development and it's main goal for now is to speed up prototyping.
Not all Automagica activities are supported as natural language and we do not recommend this for production builds for now.

# Mouse And Keyboard Automation

Next section explains which functions automagica offers to automate mouse movements and keystrokes.

## Mouse

### Coördinate System

Most functions for mouse operations need coördinates as an input. These coördinates represent the absolute pixel position of the mouse on the computer screen. Following picuter gives the coördinate system for a 1920 x 1080 resolution screen. The x-coördinate starts at the left side and increases going right. The y-coördinate increases going down.
```
0,0       X increases -->
+---------------------------+
|                           | Y increases
|                           |     |
|   1920 x 1080 screen      |     |
|                           |     V
|                           |
|                           |
+---------------------------+ 1919, 1079
```
Following function returns the coördinates of the actual position of the mouse in a pop-up message box: 
```
GetMouseCoordinates()
```

### Functions

The different mouse functionalities are listed below. They all require a coördinate set as input to determine the mouse position where an operation needs to be executed. If no coördinates are entered, the operation is executed at the actual pointer position. 

There are three functions to perform a click on a desired location on the screen.

Left click:
```
ClickOnPosition(x, y)
```
Double click:
```
DoubleClickOnPosition(x, y)
```
Right click:
```
RightClickOnPosition(x, y)
```
Moving the pointer to a certain location. This can be done to a position determined by a absolute coördinate pair or relative to the current mouse position:
```
#Move to absolute coördinates
MoveToPosition(x, y)

#Move relative to current position
MoveRelative(x, y)
```
To move the mouse from its current position to a specified position while holding a button, e.g. to drag an object across the screen, following function can be used:
```
DragToPosition(x, y, button="left")
```
The third argument specifies which mouse button needs to be held down. This can be a string: "left", "middle" or "right". Following example moves the mouse to the position of the "chrome" icon and drags it to a different location.
```
MoveToPosition(180, 240)                    # Move mouse to chrome icon
DragToPosition(x, y, "left")                # Drag to new position
```  
![Imgur](https://i.imgur.com/LDoBMrZ.gif)

## Keyboard

To press and release a certain key on the keyboard you can use following function:
```
PressKey(key="Keyname")
```
The argument should be a string. Following list contains every possible keyname. :
```
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
```
A hotkey combination of two or three keys can be executed with next function:
```
PressHotkey(first_key,second_key,third_key=None)
```
The arguments are the keys that need to be pressed. If only two keys should be pressed, the third argument can be omitted. Next example opens the task manager with the key combination "Ctrl+Shift+Esc":
```
PressHotkey("ctrl","shift","esc")
```
Text can be typed in the selected field using the function:
```
Type(text, interval_seconds=0.001)
```
The first argument is the text entered as a string, while variable is the time between key strokes. Pay attention that you can only press single character keys. Keys like ":", "F1",... can not be part of the first argument.  Following example types "automagica.be/" in the selected field (in this case is that the chrome search bar) and presses enter:
```
Type("automagica.be/", interval_seconds=0.01)
PressKey("enter")
```
![Imgur](https://i.imgur.com/ibeLf7f.gif)

Frequently used keys can also be pressed with a key-specific functions. In what follows, the available functions are listed.

```
Capslock()
Numlock()
Enter()
SpaceBar()
Backspace()
Delete()
Endkey()
Tab()
```

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
# Process Activities

## Entering Pathnames

In many of the following functions, pathnames are required as input arguments. It is important that these are entered in the correct manner to prevent malfunction of the desired operations. The pathname specifies the directories in which a file, folder, executable,... is located. An example of such a pathname is: "C:\\Users\\Bob\\Desktop\\Automagica.pptx". A pathname needs to be a string when entered in a function. Because of this, every backslash needs to be doubled in the input. The next snippet of code illustrates how a pathname needs to be entered in a function.
```
# Pathname:
C:\Users\Bob\Desktop\Automagica.pptx

# As a string:
"C:\\Users\\Bob\\Desktop\\Automagica.pptx"

# In a function:
Openfile("C:\\Users\\Bob\\Desktop\\Automagica.pptx")
``` 
In Windows Explorer, a path can be determined by pressing shift + right click on a file, folder,... A menu pops up, where you can select "copy as path" (see image). This copies te path as a string to the clipboard, e.g. "C:\Program Files (x86)\Dropbox\Client\Dropbox.exe". This path still needs all its backslashes doubled for it to be in correct form for a function input: "C:\\\Program Files (x86)\\\Dropbox\\\Client\\\Dropbox.exe".

![Imgur](https://i.imgur.com/9xI2mbk.png?2)

## Standard Windows Applications

Windows has an couple of standard applications which can be opened with functions from Automagica. Following list sums up all the available functions. If the program you want to open is in this list, it is recommended to use one of these function instead of the more general functions described in next subsection.

Open Windows Calculator:

```
OpenCalculator()
```
Open MS Paint:
```
OpenPaint()
```
Open Notepad:
```
OpenNotepad()
```
Open Windows Snipping Tool:
```
OpenSnippingTool()
```
Open Windows Control Panel:
```
OpenControlPanel()
```
Open Windows Clean Manager:
```
OpenCleanManager()
```
Open Windows Dialer:
```
OpenDialer()
```
Open Windows Volume Mixer:
```
OpenVolumeMixer()
```
Open Windows XPS Viewer:
```
OpenXPSViewer()
```

## General Commands

The above functions are all program specific. It is possible to run a program or shut it down if the exact path is known. Following function can open an executable located at a specified path:
```
#Start Process
LaunchProcess(process_executable=\"pathname\")
```
Following example explains the usage of the function. The code will open Dropbox.
```
LaunchProcess("C:\\Program Files (x86)\\Dropbox\\Client\\Dropbox.exe")
```
A (slow) alternative is to use:
```
OpenProgramByName(name, main_drive = "C:\\")
```
This function does not require a full path as input in the first variable. Returning to the example above, Dropbox can aswell be opened in the following way:
```
OpenProgramByName("Dropbox")
```
## Running Programs

Automagica can check wheter a program is currently active on your computer. This can be done with a general function that requires the process name and returns True if the specified program is active:
```
ProcessRunning(name="program_name")
```
Next to that there are a couple of functions that are program specific who return True if that program is currently running. Those are listed below:
```
ChromeRunning()
WordRunning()
ExcelRunning()
PowerpointRunning()
DropboxRunning()
FirefoxRunning()
TeamviewerRunning()
SkypeRunning()
EdgeRunning()
OnedriveRunning()
IllustratorRunning()
```
Finally, a list of every active program can be displayed as follows:
```
ListRunningProcesses()
```

# Monitoring

Following list of functions can be used to return information about the current status of your CPU, disk, memory etc.
```
CPULoad(measure_time=1)
```
Returns average CPU load for all cores. Measures once every second, adjust measure_time (seconds) to get a longer averaged measured time. Standard measure_time is 1 second.
```
NumberOfCPU(logical=True)
```
Returns the number of CPU's in the current system. The parameter 'logical' determines if only logical units are added to the count, default value is True.
```
CPUFreq()
```
Returns frequency at which CPU currently operates. Also shows minimum and maximum frequency.
```
CPUStats()
```
Returns CPU statistics: Number of CTX switches, intterupts, soft-interrupts and systemcalls.
```
MemoryStats(mem_type='swap')
```
Returns memory statistics: total, used, free and percentage in use. Choose mem_type = 'virtual' for virtual memory, and mem_type = 'swap' for swap memory (standard).
```
DiskStats()
```
Returns disk statistics of main disk: total, used, free and percentage in use.
```
DiskPartitions()
```
Returns tuple with info for every partition.
```
BootTime()
```
Returns time PC was booted in seconds after the epoch.
```
TimeSinceLastBoot()
```
Returns time since last boot in seconds.

# Office Automation

A lot of automation processes involve Microsoft Office. Automagica packs some useful functions to make automating office as easy as possible. 

## Word

To open a Word document:
```
document = OpenWordDocument('example.docx')
```

Replace words in a Word document. This can be particularly useful when using templates for forms. Make sure the template contains unique placeholder variables so that automated filling doesn't cause ambiguities.

```
document = ReplaceTextInDocument(document, text='[placeholder]', replace_with='My text')
```

Converting a Word document to PDF:
```
ConvertWordToPDF(word_filename='C:\\document.docx', pdf_filename='C:\\document.pdf')
```

## Excel

### Reading And Writing

Automation in Excel most of the time requires reading and writing cells. In Automagica, this is very easy.

There are two functions for reading a cell.
```
#Using cell value
ExcelReadCell(path="\pathname\", cell="A1", sheet=None)
```
Read a cell from an Excel file and return its value. Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". The cell you want to read needs to be defined by a cell name e.g. "A2". The third variable is a string with the name of the sheet that needs to be read. If omitted, the function reads the entered cell of the current active sheet. 
```
#Using row column
ExcelReadRowCol(path="\pathname\", r=1, c=1, sheet=None)
```
Read a Cell from an Excel file and return its value. Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". The cell you want to read needs to be row and a column. E.g. r = 2 and c = 3 refers to cell C3. The third variable is string with the name of the sheet that needs to be read. If omitted, the function reads the entered cell of the active sheet. First row is defined row number 1 and first column is defined column number 1

Similar to reading a cell, there are two functions for writing a value to a cell.
```
#Using cell value
ExcelWriteCell(path="\pathname\", sheet=None, cell="A1", write_value="Value")
```
Write a Cell to an Excel file. Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". The cell should be defined by a cell name. E.g. "B6". Value can be anything, standard is "Value". When executing the code, make sure .xlsx file you want to write is closed.
```
#Using row and column
ExcelWriteCell("C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx",1,1,value="Robot")
```
Read a Cell from an Excel file and return its value. Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". The cell you want to read needs to be row and a column. E.g. r = 2 and c = 3 refers to cell C3. The third variable needs to be a string with the name of the sheet that needs to be read. If omitted, the function reads the entered cell of the active sheet. First row is defined row number 1 and first column is defined column number 1.

### Basic Operations

Next to reading and writing, Automagica offers some basic operations for .xlsx files. These are listed below.
```
ExcelCreateWorkbook(path=\"pathname\")
```
Create a new .xlsx file and save it under a specified path. If the entered path already exists, the function does nothing.
```
ExcelOpenWorkbook(path=\"pathname\")
```
Open a .xlsx file with Microsoft Excel. Make sure you enter a valid path. This can be a path referencing an existing .xlsx file e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". This will open the existing file. You can also enter a comletely new path. In this case, the function creates a new .xlsx file with that path and opens it with Excel.
```
ExcelSaveExistingWorkbook(path=\"pathname\", new_path=None)
```
Save (as) an existing .xlsx file. The second variable is the new path the file needs to be saved at. You can ignore this variable if you just want to save the file and do not want to "save as". For the function to work properly, it is important that the file you want to save is not opened.
```
ExcelCreateWorkSheet(path=\"pathname\", sheet_name=None)
```
Create a new worksheet with a specified name in an existing workbook specified by the path variable. If no sheet_name is entered, the new sheet is named "sheet1", "sheet2", "sheet3", ..., depending on the sheets that already exist. Make shure you enter a valid path referencing a .xlsx file e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". For the function to work properly, it is important that the .xlsx file is closed during the execution.
```
ExcelGetSheets(path=\"pathname\")
```
Return a list containing the sheet names of an Excel file. Make shure you enter a valid path referencing a .xlsx file e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
```
ExcelPutRowInList(path=\"pathname\", start_cell=\"B3\", end_cell=\"E8\", sheet=None)
```
Put the elements of a specified row in a list. The .xlsx file and sheet that needs to be read are specified by respectively the path- and sheet variable. If no sheet is specified, the sheet-variable is set to the current active sheet. Also make shure to enter a valid path e.g. 
"C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". The row is specified by strings referring to the first and final cell. E.g. the row in the image below is defined by start_cell = "C4" and end_cell = "G4". Calling the function with these two cells returns a list: [8,"RPA",None,19,"Automagica]. For the function to work, the two cells need to be of the same row and start_cell needs to be the cell at the left hand side.

![Imgur](https://i.imgur.com/S4xJWBh.png)

```
ExcelPutColumnInList(path=\"pathname\", start_cell=\"A3\", end_cell=\"A8\", sheet=None)
```
Put the elements of a specified column in a list. The .xlsx file and sheet that needs to be read are specified by respectively the path- and sheet variable. If no sheet is specified, the sheet-variable is set to the current active sheet. Also make shure to enter a valid path e.g. 
"C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". The column is specified by strings referring to the first and final cell. E.g. the region in the image below is defined by start_cell = "C4" and end_cell = "C7". Calling the function returns with this two cells returns a list: [8, "RPA", 19, "Automagica"]. For the function to work, the two entered cells need to be of the same column and start_cell needs to be the upper cell.

![Imgur](https://i.imgur.com/XOft1RL.png)

```
ExcelPutSelectionInMatrix(path=\"pathname\", upper_left_cell=\"B2\", bottom_right_cell=\"C3\", sheet=None)
```
Put the elements of a specified selection in a matrix. The .xlsx file and sheet that needs to be read are specified by respectively the path- and sheet variable. If no sheet is specified, the sheet-variable is set to the current active sheet. Also make shure to enter a valid path e.g. 
"C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". The selection is specified by strings referring to the upper left and bottom right cell. E.g. in the image below, the region is defined by upper_left_cell = "C4" and bottom_right_cell = "E6". The function will return a matrix with values: [[8,"Automagica",12],["RPA",15,None],[19,None,55]. If a cell is empty, its value is set to "None".

![Imgur](https://i.imgur.com/fUfHd0M.png)

# PDF Manipulation

## Merge PDF Files
```
MergePDF(pdf1=\"pathname\", pdf2=\"pathname\", merged_pdf=\"pathname\")
```
This function can merge two existing PDF files. The first two arguments are the PDF's that need to be merged, entered as a path. The pages from pdf2 are added to pdf2. The merged PDF receives a new path specefied by the third argument.

## Extract Text From PDF

```
ExtractTextFromPDFPage(path=\"pathname\", page=1)
```

This function extracts all the text from a given page and returns it as a string. The pdf needs to be entered as a path. Pay attention that the entered page needs to be greater than 0.

# File and folder manipulations

In many automation processes it is useful to control the stored files and directories. Automagica has some functions to make the manipulation of files and folders as easy as possible.

## File Manipulation

In the following sections the functions that Automagica offers for manipulating files are described. The arguments for this functions mostly consist of a path. In this path, it is important to always use the full file-name in a path. E.g. if a png-file named "Automagica" needs manipulation, a possible path could be: "C:\\Users\\Bob\\Desktop\\Automagica.png". For the functions to work, .png needs to be included in the name.

### Open A File

To open a file, Automagica offers following function:
```
OpenFile(path=\"pathname\")
```
An example path can be "C:\\Users\\Bob\\Desktop\\Automagica.xlsx".
### Renaming Files

A file can be renamed with the following code:
```
RenameFile(path=\"pathname\", new_name)
```
The first argument is the path of the file that needs its name changed. The second variable is just the name that the file has to receive, so this does not need to be a full path. E.g. next line of code changes the name of a file named "Automagica.pptx" to "Automagica123.pptx":
```
RenameFile("C:\\Users\\Bob\\Desktop\\Automagica.pptx", "Automagica123.pptx")
```
Note that it is not possible to change change the file-type: if the path in the first argument ends in ".pptx", the new name also needs to end in ".pptx".

### Moving Files

The following function can be used to move a file from one to an other directory:
```
MoveFile(old_path=\"old_pathname\", new_location=\"new_location_path\")
```
The first variable contatains the path of the file that should be moved (this includes the name of the file). The the second argument contains the path of the location that the file needs to be moved to (in this path, the file name should be omitted). If one of the two arguments contain a non-existing path, the function will return nothing. As an example, next piece of code moves the file "Automagica.txt" from C:\\Users\\Bob\\Desktop\\ to C:\\Users\\Bob\\Downloads\\:
```
MoveFile("C:\\Users\\Bob\\Desktop\\Automagica.txt", "C:\\Users\\Bob\\Downloads")
```
If the target location already contains a folder with exactly the same name as the folder that needs to be moved, a random uid of eight characters will be added to the name. E.g., if in the previous example the location C:\\Users\\Bob\\Downloads already contains a file named "Automagica.txt" and the code is executed, it will move the folder "Automagica" from C:\\Users\\Bob\\Desktop to C:\\Users\\Bob\\Downloads and change its name to "(be8e4c88) Automagica.txt". Note that the added characters are completely random.
As a final note for the function to work optimal, it is important that the file that needs to be moved is closed.
### Copying Files

If a file needs to be copied from one to an other directory, the following function can be used:
```
MoveFile(old_path=\"old_pathname\", new_location=\"new_location_path\")
```
The inputs work in exactly the same way as in the MoveFile function and the copied file needs to be closed for the function to work properly. Also keep in mind that if the new location already contains a file with exactly the same name as the copy,it will be overwritten by the copied file.   

### Removing Files

Following function is used to delete a file from a folder:
```
RemoveFile(path=\"pathname\")
```
It will delete a file with a given pathname. With this code it is again important that the file that needs to be removed is closed.
### Check If A File Exists

Next function returns True if the path of a certain file exists and False if the path does not exist or refers to a folder instead of a file.
```
FileExists(path=\"pathname\")
```
### Wait For A File

Following function waits until a file with the entered path is created.
```
WaitForFile(path=\"pathname\")
```

### Writing To And From Files

It is possible to write a list to a .txt file or to write a .txt file to a list. This can be done with following functions.
```
WriteListToFile(list_to_write, file)
```
This function writes a list to a .txt file. Every element of the entered list is written on a new line in the text file. The .txt file is entered with a path. If the path does not exist yet, the function will create a new .txt file at the specified path and write it. If the path does exist, the function writes the list in the existing file.
```
WriteFileToList(file)
```
This function writes the content of a entered .txt file to a list and returns that list. Every new line from the .txt file becomes a new element of the list. The function will not work if the entered path is not attached to a .txt file.


## Folder Manipulaion
Most of the manipulations that can be done on files can be executed on folders as well. Automagica offers a selection of functions that make it easy to perform manipulations on folders.

### Creating Folders

To create a folder in a desired locations, the following function can be used:
```
CreateFolder(path=\"pathname\")
```
This function creates a folder with its name and location specified in the path. Next snippet of code illustrates this principle by creating a folder named "Automagica" at location C:\\Users\\Bob\\Desktop.
```
CreateFolder("C:\\Users\\Bob\\Desktop\\Automagica")
```
One note to keep in mind is that entered path needs to be unique. If there is already a folder with the same name in the same location, the function does nothing.


### Open A Folder

A folder can be opened with the function:
```
OpenFolder(path=\"pathname\")
```

### Renaming Folders

Renaming a folder happens with the following function:
```
RenameFolder(path=\"pathname\", new_name)
```
The first variable is the path of the folder that needs to be renamed. The second variable is the new name that the folder has to receive. Next example of code changes the name of a folder from "Automagica" to "Automagica123". The folder is located at C:\\Users\\Bob\\Desktop.
```
RenameFolder("C:\\Users\\Bob\\Desktop\\Automagica", "Automagica123")
```
The code will return nothing if the new path already exists.

### Moving Folders

It is possible to move a folder from one to an other location using next function:
```
MoveFolder(old_path=\"pathname\", new_location=\"pathname\")
```
The first variable contatains the path of the folder that should be moved (this includes the name of the folder). The the second argument contains the path of the location that the folder needs to be moved to (in this path, the name of the moved folder should be omitted). If one of the two arguments contain a non-existing path, the function will return nothing. As an example, next piece of code moves the folder "Automagica" from C:\\Users\\Bob\\Desktop\\ to C:\\Users\\Bob\\Downloads\\:
```
MoveFolder("C:\\Users\\Bob\\Desktop\\Automagica", "C:\\Users\\Bob\\Downloads")
```
If the target location already contains a folder with exactly the same name as the folder that needs to be moved, a random uid of eight characters will be added to the name. E.g. if in the previous example the location C:\\Users\\Bob\\Downloads already contains a folder named "Automagica" and the code is executed, it will move the folder "Automagica" from C:\\Users\\Bob\\Desktop to C:\\Users\\Bob\\Downloads and change its name to "Automagica (be8e3c88)". Note that the added characters are completely random.
As a final note for the function to work optimal, it is important that all files in a moved folder are closed.

### Copying Folders

A folder can be copied from one to an other location. The difference with the moving of folders is that in this case the copied folder also remains in the original location. The principle of the inputs is completely analogous to the moving of a folder. E.g. next code would copy a folder named "Automagica" from C:\\Users\\Bob\\Desktop\\ to C:\\Users\\Bob\\Downloads\\. 
```
CopyFolder("C:\\Users\\Bob\\Desktop\\Automagica", "C:\\Users\\Bob\\Downloads\\")
```
If the target location already has a folder with the same name, the function will add a random uid of eight characters to the name of the copied folder. This works in exactly the same way as in MoveFolder function. Next to that, for the code to work properly, all files of the copied folder need to be closed.

### Removing Folders

Next function can delete a folder together with all its contents (files, read-only files, folders, ...).
```
RemoveFolder(path=\"pathname\", allow_root=False, delete_read_only=True)
```
The first argument should be the path of the folder that needs to be removed. The safety variable "allow_root" makes sure that the first argument is longer than 10 characters. This safety prevents entering for example "\\" as a path resulting in deleting the root and all of its subdirectories. To turn off this safety, explicitly set allow_root to True. The third argument makes it possible to make sure the function does not delete a folder if it contains read-only files. When "delete_read_only" is explicitly set to False, the function will not delete folders with read-only files. A final requirement for the code to work optimal is that all the files in the folder need to be closed. Next examples illustrate the usage of the function.
Next line of code removes the folder with C:\\Users\\Bob\\Desktop\\Automagica as path. Also read only files will be removed, because the variable delete_read_only is True unless explicitly entered otherwise. Finally notice that the code would not do anything if the path was less than 10 characters long.  

```
RemoveFolder("C:\\Users\\Bob\\Desktop\\Automagica")
```
The following example deletes the folder at a given path unless it contains read only files. The safety variable remains False, so the path should be longer than 10 characters.
```
RemoveFolder("C:\\Users\\Bob\\Desktop\\Automagica", delete_read_only=False)
```

### Empty A Folder

Alle the contents of folder can be deleted using the following function:
```
EmptyFolder(path=\"pathname\", allow_root=False)
```
The first argument specifies again the path of the folder that needs to be emptied. The allow_root safety-variable has the same functionality as in the function for removing a folder. The following line of code gives an example for how a folder with a path C:\\Users\\Bob\\Desktop\\Automagica can be emptied:
```
"EmptyFolder("C:\\Users\\Bob\\Desktop\\Automagica")
```
For the function to work, it is important that all the files that the folder contain are closed.

### Check If A Folder Exists

Next function can check if a specified path exists.
```
FolderExists(path=\"pathname\")
```
If the entered path does not exist, the function will return False. If it does exist, True will be returned. E.g. next snippet checks if the folder with a path C:\\Users\\Bob\\Desktop\\Automagica exists:
```
FolderExists("C:\\Users\\Bob\\Desktop\\Automagica")
```

### Zip Folder

Following function can be used to create a zipped folder of an existing directory:
```
ZipFolder(folder_path=\"pathname_folder\", new_path=\"pathname_compressed_folder\")
```
The first argument is the pathname of the directory that needs to be compressed. The second argument specifies the location and name of the zipped folder with a pathname. E.g. the following function zips the directory with pathname "C:\\Users\\Bob\\Desktop\\Automagica". The zipped directory is specified by the second argument.   
```
ZipFolder("C:\\Users\\Bob\\Desktop\\Automagica","C:\\Users\\Bob\\Downloads\\Automagica")
```
Pay attention, because if there already exists a zipped directory with new_path as pathname, it will be overwritten.

### Unzip Folder

The opposite of the ZipFolder function can be achieved with:
```
UnZipFolder(path=\"pathname_zipped_folder\", new_path=\"pathname_target_location\")
```
The first argument is the pathname of compressed folder that needs to be unzipped. The second argument is optional. It is the path of the directory where the unzipped folder will be stored. If omitted, the unzipped folder is stored in the same location as the original zipped folder.

### Wait For A Folder

Following function waits until a folder with the entered path is created.
```
WaitForFolder(path=\"pathname\")
```

# Image Operations

Images can be manipulated in many ways with Automagica. The available functions are listed below.
```
OpenImage(path=\"pathname\")
```
Displays an image specified by the path variable on the default imaging program.
```
RotateImage(path=\"pathname\", angle)
```
Rotate an image over a specified angle. E.g. Entering "C:\\Users\\Pictures\\Automagica.jpg" as path and an a angle of 90 rotates the picture with the given path over 90 degrees. Pay attention, because angles other than 90, 180, 270, 360 can deform the picture. 
```
ResizeImage(path=\"pathname\", size=(1024, 768))
```
Resizes the image specified by the path variable. The size is specifie by the second argument. This is a tuple with the width and height in pixels. E.g. ResizeImage("C:\\Users\\Pictures\\Automagica.jpg", (300, 400)) gives the image a width of 300 pixels and a height of 400 pixels.
```
ImageSize(path=\"pathname\")
```
Returns the size in pixels of an image specified by a path. The size is returned in a message box of the form: "(height, width)
```
CropImage(path=\"pathname\",box=None)
```
Crops the image specified by path to a region determined by the box variable. This variable is a 4 tuple who defines the left, upper, right and lower pixel coördinate e.g.: (left, upper, right, lower).
```
ImageFormat(path=\"pathname\")
```
Returns the format of an image specified by the input path. E.g. entering "C:\\Users\\Pictures\\Automagica.jpg" returns a message box saying JPEG.
```
MirrorImageHorizontally(path=\"pathname\")
```
Mirrors an image with a given path from left to right.
```
MirrorImageVertically(path=\"pathname\")
```
Mirrors an image with a given path from top to bottom.

# Email Operations

Automagica makes it possible to send an email with your Hotmail, Gmail or Yahoo mail address. The input for the three functions works in the same way. The first and second arguments are respectively your email address and user password. The destination variable is the email address you want to contact. The subject and message variable contain respectively the subject and the text message. The port variable is standard 587. In most cases this argument can be ignored, but in some cases it needs to be changed to 465. When using a Gmail account, there is one exception. Google has a safety feature that blocks lessecure apps. For this function to work properly, this needs to be turned off, which can be done at the following link: https://myaccount.google.com/lesssecureapps. 

```
SendMailWithHotmail(user="user@hotmail.com", password, destination, subject="", message="", port=587)
SendMailWithGmail(user="user@gmail.com", password, destination, subject="", message="", port=587)
SendMailWithYahoo(user="user@yahoo.com", password, destination, subject="", message="", port=587)
```

# Basic Operations

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
exp(x)
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
log(x)
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

Note that the links differ depending on your location, as google search results are location dependent.


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
- [PyPDF2](https://github.com/mstamy2/PyPDF2)
