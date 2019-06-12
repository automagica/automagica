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
        - [Coordinate System](#coordinate-system)
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
- [Process Activities](#process-activities)
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
    - [Example 1](#example-1)
    - [Example 2](#example-2)
- [Credits](#credits)

# Getting started


Refer to our [website](https://www.automagica.be) for more information, registered users can access the [portal](https://portal.automagica.be). More details also available on our [github](https://github.com/OakwoodAI/automagica).

Alternatively you can use Automagica locally by starting your Python script with:
```
from automagica import *
```

For a step-to-step tutorial on how to install and configure Python see [this video](https://www.youtube.com/watch?v=cpPG0bKHYKc).<br/>
For a step-to-step tutorial on how to build and run a Python script see [this video](https://www.youtube.com/watch?v=hFhiV5X5QM4).

## Prerequisites
- Python 3.7 from [www.python.org](https://www.python.org)

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

### Coordinate System

Most functions for mouse operations need coordinates as an input. These coordinates represent the absolute pixel position of the mouse on the computer screen. Following picuter gives the coördinate system for a 1920 x 1080 resolution screen. The x-coördinate starts at the left side and increases going right. The y-coördinate increases going down.
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
Following function returns the coordinates of the actual position of the mouse in a pop-up message box: 
```
GetMouseCoordinates()
```

### Functions

The different mouse functionalities are listed below. They all require a coördinate set as input to determine the mouse position where an operation needs to be executed. If no coordinates are entered, the operation is executed at the actual pointer position. 

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
#Move to absolute coordinates
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

Automagica can check wether a program is currently active on your computer. This can be done with a general function that requires the process name and returns True if the specified program is active:
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
Returns CPU statistics: Number of CTX switches, interrupts, soft-interrupts and systemcalls.
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
Open a .xlsx file with Microsoft Excel. Make sure you enter a valid path. This can be a path referencing an existing .xlsx file e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". This will open the existing file. You can also enter a completely new path. In this case, the function creates a new .xlsx file with that path and opens it with Excel.
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
The first variable contains the path of the file that should be moved (this includes the name of the file). The the second argument contains the path of the location that the file needs to be moved to (in this path, the file name should be omitted). If one of the two arguments contain a non-existing path, the function will return nothing. As an example, next piece of code moves the file "Automagica.txt" from C:\\Users\\Bob\\Desktop\\ to C:\\Users\\Bob\\Downloads\\:
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


## Folder Manipulation
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
The first variable contains the path of the folder that should be moved (this includes the name of the folder). The the second argument contains the path of the location that the folder needs to be moved to (in this path, the name of the moved folder should be omitted). If one of the two arguments contain a non-existing path, the function will return nothing. As an example, next piece of code moves the folder "Automagica" from C:\\Users\\Bob\\Desktop\\ to C:\\Users\\Bob\\Downloads\\:
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
Resizes the image specified by the path variable. The size is specified by the second argument. This is a tuple with the width and height in pixels. E.g. ResizeImage("C:\\Users\\Pictures\\Automagica.jpg", (300, 400)) gives the image a width of 300 pixels and a height of 400 pixels.
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

You can add all variables to a string. If you want, for example, to add an integer to a string you can do so by defining the integer as a string:

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
#accesing the different strings can be done by:
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

Down here is a list with basic math operations that can be used with both integers and floats. Before they can be used, the math module needs to be imported:

```
from math import *
```


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
x = 0.5555
round(x, 2)
>>> 0.56
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
The previous example will output the string *"Wear a warm hat!"* if the inputnumber was lower than 10. If the number was higher than 20, the output will be *Wear short pants!*. If the condition was still not met, which means the input number was between 10 and 20, the else statement will be activated. In that case the message will show *"You can wear normal clothes!"*.

### While loops

The while loop evaluates the test expression.

If the test expression is true (nonzero), codes inside the body of while loop are executed. The test expression is evaluated again. The process goes on until the test expression is false.

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

## Example 1

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

## Example 2

This example uses Automagica activities for Excel operations and file/folder manipulation. 
The code reads an Excel document specified by the path "C:\\Users\\Bob\\Downloads\\USPresidents.xlsx". This file contains in the first column a list of every US president together with some background informations. To begin, all the president names are added in a list. After that, the for loop creates for every president a named folder containing a .txt file with the extra information about that president.

```
from automagica import *

# Put the president names of the first column in a list.

names = ExcelPutColumnInList("C:\\Users\\Bob\\Downloads\\USPresidents.xlsx", "A2","A45")

# Create for every president a folder with his name and save a .txt file in that folder with his extra information.

for name in names:
    CreateFolder("C:\\Users\\Bob\\Documents\\Presidents\\" + name)
    row = names.index(name) + 2
    data = ExcelPutRowInList("C:\\Users\\Bob\\Downloads\\USPresidents.xlsx", "B"+str(row), "H" + str(row))
    WriteListToFile(data, "C:\\Users\\Bob\\Documents\\Presidents\\" + name + "\\" + name + ".txt")
```
Following gif illustrates the actions.

![Imgur](https://i.imgur.com/YKIoR4Y.gif)

| Icon | Name | Info |
| ------------- | ------------- | ------------- |
|**Mouse**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANPSURBVFiF7ZdBaFxVFIa/c+e9eSPTtKV1MkJKA4E62KIgXbjIRihIQ6k00UkEF0owi9q4KQHBjStBly6ShZTSLDR2oSJ20SJdTRZmFBcppAWbRJgmWiql1bTpZN7c4yI3ZabJJO+NM135w+W9d8+5//9z3rtn7qCqxBkm4U+YhD+x8Qz0uethoCcuX7xkyCFSRaQK5Nzcd8BLQAHoaqsBk/Cn9vQcLe/pOVo2CX/KGTgE3AQ+jiuuqhgiQkRy1oaDmSPHkpkjx5LWhoMiklPV34BF4FxUrjrEKP8gYAF1wwKDLvYN8GwzFRBHEBkicsEZf7dmTjQukUPkV7AdmhVvmYH/gv8NeE2uOygipxrEysCPqhpGIYq1C0TkZd/3rxpjOowxmxaurq767vZ1Vf0hEmmMPvCq53kP8vl8WCqVdHl5uW6Mjo5aY4wVEQucamkrBgaMMZWRkRG7tLRUJ1wqlXRoaCj0fT/s7+9Xz/PW4hjY8RsQkXdE5Hx3d7fJZDKMj4/XxQuFQlgsFhkYGPCy2WykqtdiRwNBkPwwnU5bsJWpqS/rYmFYlVLpVjKfz9OMeCQDIImTJ/u8Eyde25R7585fnDkzRjqdjiQmIvuBu7Wd86n2ASP8HohcF5E3RUSg+T6wE15x/E9iV+/ejucL9//52sBNETnbUgOzs7OEYegBp93YhNNdnfLirmcSn9+6nfNEPvNEJAtMAgngnKpebEa8WCzqzMyMAsOqOrlVjojo23PzVuFv4JNQdcJT1dvAcRG5BPzcjHihULALCwuhqr6hqpca5fnGXFyz9hdgQlUfgvsGROQ4cENVF7ZaODd3Y0vClZUVABYXFx+qap+qTm9ndK1afevJOWF9J1wF+lX1Xl1QZBj4IgiC+Uak1tp7lUrlPVW9tp2443t8cqq9fwH4CbgMfFDTfoeBkPV3Gvus16CljwN9wKdsnCcbJLZc3PF2Ab+y/h/CPDYAdACpdoo77iQwC0zW/RqmAqaTPvPAWLvEnYGPgLPA90DvRkd+TgR7oJMK6+f9sXaIO7FeV4Uu4NCGgff37ab8xxX0QCcVV4lUu0xsMpUKmM7uR/ftpiyCTQVMAx1Py4Akfa4Zw/1HZb4CvlXVP3faz63Ev9I70cKEH0/TAAAAAElFTkSuQmCC)|Get Mouse Coordinates | Displays message box with absolute coordinates of the mouse position |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEUAAABie6Jie6RjgKNhe6NVgKpifKNgfaNkeqZifKNhfaJjeqJifKNifKRggJ9jfaRggJ9jfKNifaNifqVbgKRifaJmgJljfKNje6VVcapjfKNifKNjfaQAAP9ifKNkfKJifKJhfKNkgKRifKNifKRifKNifKNifKNidp1ifKNhfaJgfaRifKNifKNhfKRjfaRhfKJhfKOAgIBje6JifKNjfaRjfKJifKRie6NifKNje6JmZpljfKNjfKNggJ9he6NmeqNifaJifKNheZ5hfKRifKNjfKNje6NifKNhe6NjfKNjfaJie6RhfqJie6JifaNifKJhe6JhfKRpeKVjfKJjfaJifKNje6JifKOAgL9ie6NlfaBifKNifaNifaFmgKZgfaRie6NifKNifKNifaJifKNifKNjfqRifKNddKJifKNifKNkfKNifKRifKNifKRifaNffKBifKNifKNhe6NifKNVVapifaRigKdqgKpifKJifKNjfKNifKMAAAAbs8LoAAAAfXRSTlMAPHgkkwbEPRfWPyzFxiCwGKO0QQ6PCsI+CW/MOwGeUslpHH270ejuDcA3Nefee2KlmAJNzVp5ZXLlfAW1UAi6GYfKFdQn3HTjOkhYcEc02ZpurRGEgdNVuQS8K+qNORQt2+SnYLf7Q/AL/thAov1t1SP0gFm9A5EaDLPgljs6ba0AAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4gcfDwIsJrDCrAAAAUdJREFUOMtjYEAFjEwM+AEzCwEFrGzsBFRwcHIRUMHNQ0ABAy8uCT6IB7j5sUsLCAoJs4oAGaKMWOXFxCUkpaRlGBhkeWSxKpCT51BQVFJWUVVTl2YTxDREg01SU0tbR1dP38CQwcjYRA9dgamZuYWGpZU1AwOTIYhvY4vuBDt7B0cnoO3OLuLMQL6rmzWaCll3WQ9PIO2l6e0D4ov6YjjDz58BSQFjAIaCwCBkBcGcGApCQpEVMIRhKAgIR1EQEYmugJ8bRHK4REWDuaIC6Ap4YmLjgHFhBnZdvGJYArqCxFogSLJ3SpZICU1Nq61NR1eQUYsKvNHkWdHkawPRFGRmoSmwQLciG01BDrqCXFT5PA10BfmoCgowQrKwCEVBMYYChhJk+dIyTAUM5Qh5D2cs8gxl5mpQB8pVMGAHlUxV1RlsNcjRAADCI22hLSPcLAAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wNy0zMVQxNTowMjo0NCswMjowMCovWKsAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDctMzFUMTU6MDI6NDQrMDI6MDBbcuAXAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg==)|Click on Position | Clicks on a specific (x,y) pixel coordinate on the screen. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEUAAABie6Jie6RjgKNhe6NVgKpifKNgfaNkeqZifKNhfaJjeqJifKNifKRggJ9jfaRggJ9jfKNifaNifqVbgKRifaJmgJljfKNje6VVcapjfKNifKNjfaQAAP9ifKNkfKJifKJhfKNkgKRifKNifKRifKNifKNifKNidp1ifKNhfaJgfaRifKNifKNhfKRjfaRhfKJhfKOAgIBje6JifKNjfaRjfKJifKRie6NifKNje6JmZpljfKNjfKNggJ9he6NmeqNifaJifKNheZ5hfKRifKNjfKNje6NifKNhe6NjfKNjfaJie6RhfqJie6JifaNifKJhe6JhfKRpeKVjfKJjfaJifKNje6JifKOAgL9ie6NlfaBifKNifaNifaFmgKZgfaRie6NifKNifKNifaJifKNifKNjfqRifKNddKJifKNifKNkfKNifKRifKNifKRifaNffKBifKNifKNhe6NifKNVVapifaRigKdqgKpifKJifKNjfKNifKMAAAAbs8LoAAAAfXRSTlMAPHgkkwbEPRfWPyzFxiCwGKO0QQ6PCsI+CW/MOwGeUslpHH270ejuDcA3Nefee2KlmAJNzVp5ZXLlfAW1UAi6GYfKFdQn3HTjOkhYcEc02ZpurRGEgdNVuQS8K+qNORQt2+SnYLf7Q/AL/thAov1t1SP0gFm9A5EaDLPgljs6ba0AAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4gcfDwIsJrDCrAAAAUdJREFUOMtjYEAFjEwM+AEzCwEFrGzsBFRwcHIRUMHNQ0ABAy8uCT6IB7j5sUsLCAoJs4oAGaKMWOXFxCUkpaRlGBhkeWSxKpCT51BQVFJWUVVTl2YTxDREg01SU0tbR1dP38CQwcjYRA9dgamZuYWGpZU1AwOTIYhvY4vuBDt7B0cnoO3OLuLMQL6rmzWaCll3WQ9PIO2l6e0D4ov6YjjDz58BSQFjAIaCwCBkBcGcGApCQpEVMIRhKAgIR1EQEYmugJ8bRHK4REWDuaIC6Ap4YmLjgHFhBnZdvGJYArqCxFogSLJ3SpZICU1Nq61NR1eQUYsKvNHkWdHkawPRFGRmoSmwQLciG01BDrqCXFT5PA10BfmoCgowQrKwCEVBMYYChhJk+dIyTAUM5Qh5D2cs8gxl5mpQB8pVMGAHlUxV1RlsNcjRAADCI22hLSPcLAAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wNy0zMVQxNTowMjo0NCswMjowMCovWKsAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDctMzFUMTU6MDI6NDQrMDI6MDBbcuAXAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg==)|Double Click on Position | Double clicks on a specific (x,y) pixel coordinate on the screen. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABlVBMVEUAAABifKNhfaJjfaNjfKNjeqJhfKNdgKJje6VifKNheZ5jfKNifKNmgKJjfKJifKRifKRjfKJkfKJifKJVcapmd6pVgKpifqVjfKNhfKJee6FkeqFifKRjfaRifKNhfKJddKJgfaNifKNhe6Nhe6JifKNifKNifKNifKNifKNjfaJjhKVhfKNigKdifKNie6Rhe6RifKNje6KAgIBhfKNifaRjfaRhfKRifKNifKNkfaVgfaRifKNjfKNidp1ie6RifKNmZplje6JifKNhe6JifKRie6RjfaSAgL9ie6NifKNjgKNifaIAAP9ifKNie6RggJ9mgJlkfqNifaJie6RjfaJjfKNie6Rie6JifaNifaNifKNpeKVhfKRhfaRifaNje6Jie6NmgKZlfaBie6NifKNkeqZifKNheaRifKJifaFifaNifKNifKNifKNifaJifKNifKNhe6RifKNie6NifKNkfKNifKNifaNifKNffKBVVapifKNhe6NifaRifKNgfaRjfKNifKNifKJqgKpifKMAAABuSHiZAAAAhXRSTlMAfzdsUCzHFj7YFWeKHqhzbXkhyQkPBkG1pRsuojvNcQs9xDqdwejy07mBH2kaTp9+zE0CmKpie97qMzXAwg1RgAV8425leFoE3Sck1wHKuAgKRY9wWEiXPNkv0BGtg7ZVmRQrvNYXryqaOY3F+7dgp9pX8HL+QP3V9CMDvVmRni2W4LMMdicdPwAAAAFiS0dEAIgFHUgAAAAJcEhZcwAADdcAAA3XAUIom3gAAAAHdElNRQfiBx8OOhgRWeDVAAABRklEQVQ4y2NgQAaMTAz4ATMLAQWsbOwEVHBwchFQwc1DQAEvHwEF/AJAQlAItwJhEQZRMXEJSSkc8tIyDAyycvIKikoKmJLKKqrCauoamlraOnK6evoY8gaGRsYMJqZm5haWVtY2IrZ2aPL2EiDSxIGBwdHJWcHF1c0dVd7D0wtIetv6AAPK18+Byz8gEFVBUDCIDAm1CQO5xoJB3hfNhvAIJAUMkVEYToyOQVYQy4yhQI4BWYFWHLq8bzyKgoREdAVJYDcyJKekpoFo1nR0BRkaOkkgOlOLgcEuK9syB12BeGtrbp5WPkeBnKZzKxAUoisoakUFxegKBNAUtIqhKShBky9Fj+0yNAWc6FbYlaMqkMEIyQpUBQIYChxQ5CurMBRU1yArqGXABFzOCPk6BmxAtx7qUDXXagbsoKFRqbip2a0FRRAAuxR3CVsTlh0AAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDctMzFUMTQ6NTg6MjQrMDI6MDBXo7QiAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTA3LTMxVDE0OjU4OjI0KzAyOjAwJv4MngAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII=)|Right Click on Position | Right clicks on a specific (x,y) pixel coordinate on the screen. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABnlBMVEUAAABkfaVjfqSAgIBVVapifaJifKNie6RmgKZheZ5ifKNifKJke6RifKNifKNifKNifKNmgJljfKNie6JifaNifKNigKdhfKRjgKNgeqVggJ9ifaNtbZJifKNgfKJifKJje6Vie6NifKNgfKVifKNifKNVgKpie6Rie6RjfaRhfKNhfKNifKNifKNkfKJie6NqgKpifKNifKNie6RifKNhfaNifaNjfaRifaNhfKNheqNjfKNifKNkfKNkeqZifKNjfKNifKNifaNhfaRifKFifKNie6Nmd6oAAP9mZplhfKRifKNifaNmgKJjfaJifKNifKNidp1ifKNjfaRifKNifKOAgL9ifKNifKNifKNje6NgfaRhe6JifaJkfKJlfaBje6JjfKNifaJbgKRjgKpifaRhfqJhfKRifKNddKJjfKNifKNVcapifKNifaNhfKNifKNdgKJifKNifKNhfKNjfaRifKNpeKVjfKNifaFifKNhe6NgeaZjfaRifqVifKNie6JhfaJifKNifKRhfKRje6VgfaNifaNifKMAAABCGDdQAAAAiHRSTlMAM0MCA4f+uBQVveI49vvy8Ap3vi+mGoYkMAiFB8xK7R+V8SXSywZR37C/kIjIKVMM+NFw94uuatWYMmf9QBfso7lmg0TzmQ8BBUznXh6B480N9GLg3gTEsfybNZ3XISt8z2gOEpFHrZwLUO4JglbhyhbA6GFarxHCOcM6KDtB9Tw/+qLUPj2sFsDMHwAAAAFiS0dEAIgFHUgAAAAJcEhZcwAADdcAAA3XAUIom3gAAAAHdElNRQfiBx8PBCPgVXi7AAABq0lEQVQ4y32SZVtCQRCFV0EwL2B3YGOAXdiioFjYHdid2F3nZzv3clcUFufD7uzOu/OcnRnGhBYRqWH/mDZKB310+HhMLMji4sMCeiRIMMBoCgckJiUbEZmSIo6mpqXTakQGY5lZEaHx7BxEcSAXefkhQAHMhRwwFaG4JCheCpSVk0mw0FoMVAQBlQiyKlZttf2uYA1q68jq0UBrI9DEmmFoaQ0QbbC3cw0dnehirFtOlNPzk6YLvRzoQxHVygpY7ICjX/2zNnfA6ZIBp8s5KD9zDcE9PDJKacbaxtUkngkjeianpv3HNMzQu8HZOUozvyDfLPo/sKTWYFmHFaXGq5N0u7buZdpKHXn6DS6rG5t+R7O1LQGenV22Z9aNBCbGiv0D7ncc0uM6GonCX8WRZXL/6Bg4OQ1ukCJTNu8ZcH7hDOkgl8kuAZ9XNCRcpq0KZuEkKjKvrn22ASJuBIAicxO4lQnDnYAgmfcSJJV4CAVI5hosj09+wvEskgl7MmtXiGZMiWSihbYXD27dr3gTyJx5j5H3Dw+1yecSyNSqvfl04EsUD1i1e/rP+RtzqoK0S6GtfwAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wNy0zMVQxNTowNDozNSswMjowMIuDKkEAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDctMzFUMTU6MDQ6MzUrMDI6MDD63pL9AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg==)|Move To Position | Moves te pointer to a x-y pixel position. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAt1BMVEUAAACAgIBhfKNifKNifKNifKNhe6NhfKRjfKNhe6difKNifaJigKdifKNifKNifKNjfKNigKVje6VgfaRjfKJhfKNifKNifKNifKNifaRifKNkfaVie6Rie6Rje6JjfKNhfKRhe6IAAP9ifKNifKJifKRifKNifaNifKNie6NifaNie6NjfKNifKRifaNjfaRifKNkgKRee6Fie6JifKJhfKNifKNifKNhe6NifaNje6NifKIAAACNe4HzAAAAPHRSTlMAAmHLnvuTVI4d+mAa3sjBtSIfLYSYxfjokfwzcHhd3IadAa+zu/DZypVeW5ZlhYn5HBs0jKDNwLqum8kaEYxVAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAAN1wAADdcBQiibeAAAAAd0SU1FB+IHHw8GAQcDW90AAAExSURBVDjLfZHbdoIwEEUHMKAoab1ANVK1tBY0Ihe1tPr//9VA5E6YBxjW3g9zDgDVkWRFkSUQjjRAqooGUg/XADShwbnYyLnQGOY8NYZtPtLH5cdYH7WEiW5g/JJurxgb+qSBpzOYL0zrLd2X2FzMYTat3rciZM3eNhfe2WNNyKq4lN2/2e7qwm67QR9OJR8264KJi7Q8P7Zs2/7kwhdbLZz38exn/53OMhXcbN3njcllP+3RkAyKCj2jKuAd+oSDB0dCxZySIzinzOg8kpITq4IbXTE5fxodReU8M3zjXBfOhl9wZgQhav4sFAZO5dwohsv15nHh53a9QBw1EsXITZLfdPtLEhfFrchR6Jcffhi1BAjKxigJOlp7NgZQyddtiHhuiHlm3O89nBn08aB1/g/vYyMbsj40/QAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wNy0zMVQxNTowNjowMSswMjowMPW22YwAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDctMzFUMTU6MDY6MDErMDI6MDCE62EwAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg==)|Move Relative | Moves the mouse an x- and y- distance relative to its current pixel position. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAt1BMVEUAAACAgIBhfKNifKNifKNifKNhe6NhfKRjfKNhe6difKNifaJigKdifKNifKNifKNjfKNigKVje6VgfaRjfKJhfKNifKNifKNifKNifaRifKNkfaVie6Rie6Rje6JjfKNhfKRhe6IAAP9ifKNifKJifKRifKNifaNifKNie6NifaNie6NjfKNifKRifaNjfaRifKNkgKRee6Fie6JifKJhfKNifKNifKNhe6NifaNje6NifKIAAACNe4HzAAAAPHRSTlMAAmHLnvuTVI4d+mAa3sjBtSIfLYSYxfjokfwzcHhd3IadAa+zu/DZypVeW5ZlhYn5HBs0jKDNwLqum8kaEYxVAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAAN1wAADdcBQiibeAAAAAd0SU1FB+IHHw8GAQcDW90AAAExSURBVDjLfZHbdoIwEEUHMKAoab1ANVK1tBY0Ihe1tPr//9VA5E6YBxjW3g9zDgDVkWRFkSUQjjRAqooGUg/XADShwbnYyLnQGOY8NYZtPtLH5cdYH7WEiW5g/JJurxgb+qSBpzOYL0zrLd2X2FzMYTat3rciZM3eNhfe2WNNyKq4lN2/2e7qwm67QR9OJR8264KJi7Q8P7Zs2/7kwhdbLZz38exn/53OMhXcbN3njcllP+3RkAyKCj2jKuAd+oSDB0dCxZySIzinzOg8kpITq4IbXTE5fxodReU8M3zjXBfOhl9wZgQhav4sFAZO5dwohsv15nHh53a9QBw1EsXITZLfdPtLEhfFrchR6Jcffhi1BAjKxigJOlp7NgZQyddtiHhuiHlm3O89nBn08aB1/g/vYyMbsj40/QAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wNy0zMVQxNTowNjowMSswMjowMPW22YwAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDctMzFUMTU6MDY6MDErMDI6MDCE62EwAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg==)|Drag | Drag the mouse from its current position to a entered x-y position, while holding a specified button. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeCAAAHggFwQHG1AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAXdQTFRF////VVVVMzMzQEBAQDNNPTFJOS9MPjFKPTBNVV5yVV1yPTNNPTJNVF9yVF50UFduUFVtPTJMPDJNPTFMPTJNQjxVPTJLPTNMPTJMWWJ3WWN4eYKSd3+Qc3yNTE1kSUZdipKgj5ekbW1/PjNNEZ+FEaCFE5qCG5aCHYF1HYJ2HZWCIZGBI4+AJY2AJrmZJ4p/J5mIJ7iYJ7iZKGZnKLWXKoh+K7CVLIV+LVlgLqmSL4J9MYB8MqGPN3t7N5eLOpuOOzZOPHZ5PTJMPYuGPzROQoKCQpmPRXyAR0JZR3h+S296TWV1T2h3UGJ0UWN1UmBzUmB0Up2WU19zU2B0VF5zVl9zWGFyW2NyW2RyXFRqYlpvam9va29vdndudn6LeoOTe3ttg5GdhYJriJCeioZrkLCxlY9plo9pn8fEoMfEpc3Jps3JtdXSvq1iwrBiyszS1Nnd3uLl38Zd4OTn48ld4+fq5Ojq5err5+vt6Ozt7PDx8tVa89VaeKdWIgAAACR0Uk5TAAMFCBQVGz5PV2BkcXSAiY2krb/S0tXe6+/x9PX29/n5+fv8FggocAAAAR1JREFUOE+F01VDwzAUhuGz4e7uEpzAcJdsuAxGcXd3GAPy40k6aFOaZO9Fbr7n8gQgVqnaUgCM8jJ1FSUMPH+peyrl4PP9VV44EgUfh4a807AAjs42tOCB0rctDdj7ppReasAuBxcaYNxT+rJpLUE3MPZP1q19oXHSDYSWWhAa1YCVVsQalgH/DHtC7cisP/QfrI1hHxO96LeOoBMsj2DMxBCyajsWweIg5vk6bYCmBTDfh7FLjNtgrgdjt7DBVBe2M0VTgwhWsSMuuicGmuv/QOTuxtnt9dU5IWT24DEKpNe4Q3jblfFgVNfIqjVBoCoRMuVl1bG9IDtD/aFyCSnMT1DvkEyK4nJ0wlucBh6tSPcCE3lqYOZJigEAfgBeXN5IKUhh3gAAAABJRU5ErkJggg==)|Click on Image | Clicks on an image on the screen. Image path needs to be specified. |
| **Keyboard** |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAA0lBMVEUAAABffKBjfKNifaFjfaJifKNifKNifKNifKNifaNhfKNifKNifKNifKNie6RhfaJjfaRjfKJhfKNheqNifKNifKNje6JifKNifaJmgJlggJ9ie6JifKRifKNifKNifKNifKNhfKJjfKNhfqJhe6JifaNifaJie6Nie6NjfKNhfaNggJ9ifKNifKNidp1ke6RmZplifKNifaNhfKNkgKRgfaRifKNifKNjfqRifKNifKNifKNhfKRie6NifqVifKRje6VgfaNifKNifKJifKMAAAAaoMKDAAAARHRSTlMAI1A5WP6esfasoKnz+bg/iaiQMvhOXehgChi+bfX37spCSEd2VtdyW8KLEPLwDTgFqy/HHC376kPO/OVU20HGPj2CmoKHyGIAAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4gcfDwoLS2P9zwAAAMJJREFUOMvl09cOgjAUgOEjuBW3orhxoii4cO/z/s8kGghQaHkA/5sm8IWS0xTAW4TzxBOvIRpDb3ECJBCTqbRdJosCAXKI+ULRrlRG9IFK1bVBTQwAnAvU/wg0JFdNP2i1vafTIUGXOD7fF8yl15edBkM/GI2RkgVk58lkGgIkoANFYYPZXGWBBQdLzUyngZVuzXpN22Kz3YnfDOo/7A/HkDmczlRwuVIGadzUH7g/5OCeL/PiCMhMgDgbvAF4jpEGH821q5ZoP5xyAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTA3LTMxVDE1OjEwOjExKzAyOjAw9Yx2lQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wNy0zMVQxNToxMDoxMSswMjowMITRzikAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC)|Press Key | Press and release a specific key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAhZQTFRF////SUlJQEBAOTk5KysrQEBAPT09MzM8NjY2NTU1Pjk+JycnMi4yOztCKyswKSktPDxCPTtAPDtBKiouKSgsKSgtJCQoOztBPDtBJiQoPDpCPDxBIyMnISElHx8iPDtBPDtBNzY9PDtBHh0gHx8iGxseHBwfHh0gGBgbGRkbGxseFxcZGxkZHBweHRoZHxwZIR0YJB4YKCQeKSktKyIYLCstMCUYODc8OTc9PDtBPjxBPzw+QTw8QT0/TEM6UTcXU0Y3VDkWVjkWVkc3WUk1WkQmXUs0YEwzYk8zY04vZkIVZlAxaVEwakUVa1EzbEYVb0cUcVEedEkUdVIbd1AgeFgpfVwri2QojmIckGcnkWcnkmQooGkgo3EiqGYRqGscsWoQs2sQt20QvIAivoEhw4QgxYUfxoYfxoYgzIogzIohzYog1XwM1nwM2n4M234L5oMK6Jsf6Zse6oUJ7p4f84gH9YgG+aUf+4oE/Kcf/YoD/ooC/osD/qgf/4gA/4kB/4oB/4oC/4sC/40E/5YJ/50O/6QS/6US/6cT/6kf/6kg/6sU/6si/6wW/6wi/6wj/60V/64m/7EY/7Iq/7YZ/7Yw/7ca/7k0/7o2/70b/8Mc/8RC/8RD/8Yc/8hJ/81P/84W/84X/88A/88U/9AH/9AK/9AN/9AP/9BT/9RY/9Va/9th/9xj/+Jq/+Jr/+Nt/+Rt/+ZwoiROiQAAACt0Uk5TAAcICQwYGR4hIi00PUlrcYSXmKzAwMHByMva4+bs8PLz9PX4+fv9/f7+/ruUxDEAAAHpSURBVBgZBcHdbttkAADQ4++LnZA69uI1i9iqqu3GBJO2978D7ngCLhjiAqHQorZZ0ib1T2xzTgJAkqdpzLR91z2PABKA7Kx4C2CzP7SABAhFtQYAd4/7AUSQrn7IQdkC8lXXDBBhfn4F+P66PwKWp75DRHp+CRC/LJMtoGzrgUhYXQE4fTytxi2gbI6jQHENwIz+/UeA64IgqwDwCuPVO4AqE5ytgQt4DePNCbA+E5ICqD7kXF6B2U8toEji4j1w8+7N/OJHOsi/DhEsvsX8HMw/ZVlVMk8bhM4xgm1IgXUO5OsplF+KFqQhAgUwWw43Karic91CDBmYlMAi0b3Bmbm6RRaAWIG0xCJAdq5uEVowARYTnGa+w5K61YYeROAViNkFetRtP+nACEQwXQ3ooR5CB55vUcYIqnCi34A2PG9gvMfkcgCDJ/YdnPZh3IN7NNMADI/8DR7G4HAHuz841IANj3/CcBD14woeJpVjHjXUjw4/j3C/E2m7JcaHdNm/TNMmPm28/NLC/r9RZGxOJcbbXTrbtfVmn/zzawfNvx0RQ9+WSPZ/dZPJt3H321fQ3r4gAenraxiO4cPi9wPw9HCABAhFtcZwHADj3XYACUB2VrxlOA7Q77Y1IAEgydM0TtO+aZrjCcD/QYnGEnUj7BIAAAAASUVORK5CYII=)|Hotkey | Press a hotkey (combination) |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAPrSURBVFiFvZVvTFV1GMc/zznnklgXLggDLM3NJspyhKPmaDnkBUy8pDajrfXGWHO5hpW8tulqhZM5Wbb1omVvWn+dTYEG6nWYWVvOWi665Au1W0Aw7mU0Arn3PL04l8u5DLZ7wct3OzvP7/k+v+f57jm/8/xEVUmguf6BMTHOKGxV5HjeyXPvkmEY7kUYeU6hHsgX9GjkjT2+ZRUA7HLZluq9+uUTsL/SIyI7klibZ5dNwFh2UTWQ4yZFZAf7Kz3LIkDVmG2/6tm4lRMXlnkBoA1xIyTKO/MKy5SASHN9BbAWQIWO3Pc7rwMDjgI7o+fAAkDEVUTPo6oc9HcCTYisiTTXV/jaO284fKMZ7l9XJdirnHC1Taygt7Q1uHgBGLvAGUii0ho56H8bKEhEOQJvAER+X3tYxD48m0KIESMSbBkBCUQxmgpKW8dTFWCMHtq9BrTC5SsDyoGHEx6d7ZAKpQvkKgB93sL+KNXiAIZEp2fbL1xV1c9nHuBO3L/FEZoMVV5U0Z2IHgKmnVBt4PIRK1UBFriGjcReymvvuj2zjDT7X0c44VDRBuAD9+aobQQKNx4bBDoj/S3bUfwKK0YfmSjOh1AqAgxByuP2Td+J2eIOKR0JW3XzQkkGrh9ZibIJQGAy/7GVf6dS3MmLvAx8ImrvnkvmnDz3hwiNoB+rYbfO5T2WfSESbPkl+6HxUWC949Uz8JadqgBJuo5TQDjY8pnACwtnZI9vw/GzC/JzMPc2TAuCfAv6DdCfcCqnRm815yy8Kxkpn9b5cC8m+wrL2gYBxoItpxQOAKvN6IqtQDdA45eYkcKhfYYtT6tBEWrfViXQU1P8lYIuSYAbqlxEOACgomVAd9W1ULa3wNMrSqWKxmedIMKrtYGh7+umqV3SJ0gSgLgH1BiAd9LTClTOOAVGXDFVeOTYkjpgGfb20eCbYROzXERfm/Hbtt0XN/fG3//apv1Uz7aSvtrLw0+I2j8BJqh/aYdQ+NTA6FL0PWC149Ur+ZvafvB/dzcPKHECCfRsK+kD6K4u/Bk474QylXYHRAki83OKdqtpNQHEolm5LiJpMJmWvhKNGV1qxnrTFuDbePdouH/dhcR1DAg6HjPpz1/f9mcqOTqfKR4GPoRF/YZfxPI2cCX9ffPjvv0Fi8V9mwPpQEDqLg0+mTWhNzPWgemY8V9ioeS6udrA4GkV+XHqQSOQ9mWUDuoCQ2HAJzAyJUUlgWqiVddC2d5JzxDgBYYzegYEegEUCrJ0KFQbGPzaO+kJxYujkNkO7Lw08GhUjF9nCs7BP1G1tmS0Ax01JXcstTeLymngFjCh8BvQblr6+MWaVX/9D48CdgjDk2lOAAAAAElFTkSuQmCC)|Type Text | Types text with a specified interval in seconds |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAArlBMVEUAAABifqVhfKRifKNhe6difKNhfaRie6RifKNifKNifaJjfaJhe6FigKdjfKNie6RifKNmgJlifKNifKJgfaNifKNjfKNifKRifKJifKNhfKNkfKNjfaRkfaVifKNifKNddKJjfKNdgKJie6RjfKJgeaZifaJifKRifKNifKNifKNifKNffKBifKNifKRjfKJjgKpVVapifKNgfKVkgKRifaJifaNifKNifKMAAABOmTqZAAAAOHRSTlMAQa37HfyDuP65YFhPGm942grukj3AUGWz+JBAWjP9ygtIFp+oKIei5NjqqSPgRnkSA9IlHI/VzUqSt1kAAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4ggDDxEmPxUV1gAAAMdJREFUOMvNk8kSgjAQRBsEgiiooHHBDXdU3Jf8/5cZEUWLQK6+Qw6ZV6mpVDegqCWWQ0lVAE1nBegaDFaIAcJPs2xVMlhlk49ILFRtp5bBsatvod5wRa+7jXoieE2+TcuhlLY73S+j6SVCz2esjxeDYSr4vVQYAeMgCCbAVCzMgDm/WlC6LBR++VNhFYZrsbABtlEU7YC9WHAPyU8eT2KBzc7x/HLN2YFzI4TcTZYvZPkr4Rk5EZ/ISUMrjX1xcaTVk5ZXVv8Hy/WmWw/A3AMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDgtMDNUMTU6MTc6MzgrMDI6MDBXSMdrAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTA4LTAzVDE1OjE3OjM4KzAyOjAwJhV/1wAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII=)|Press Caps Lock | Press the Caps Lock key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAolBMVEUAAABifqVhfKRifKNhe6difKNhfaRie6RifKNifKNifaJjfaJhe6FigKdjfKNie6RifKNmgJlifKNifKJgfaNifKNifKNifKNifKNifKNhfKNkfKNifaJifKNggJ9mZplifKNje6RVVapifaJje6IAAP9ifaJtbZJje6VkeqZggJ9ifKNieqRifKNhfKRifKOAgIBifKRie6NhfKRifKMAAADtyAz6AAAANHRSTlMAQa37HfyDuP65YFhPGm942grukj3zyPDyy5BAaMAQBd5fA9dVAY8HPhcIw0nNVNYCRnpMuLirZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAADdcAAA3XAUIom3gAAAAHdElNRQfiCAMPExdc/XduAAAAuklEQVQ4y83TxxaCMBAF0KEXAWlGJSo27Ipl/v/bRA6ykJDZ+hZZJPdk9R6AomrYE01VAHQDJTF0MFEaE6zqtB130Inr2NWTVQPPD4adBL73BWEUi36Po7ABSYo4YoyNESeMTVuRJg3IOCIDgBniHGDRAp79gHxJAFhRYL0hAGwpUOxkYH8AOMrA6Vz/IgF4ocC1IADeKFDee0HJ+aO6e3L+EgNR/gp8KidKWzmytGTt5cMhp0eOl5r/Gyf0lU4JF2BaAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTA4LTAzVDE1OjE5OjIzKzAyOjAwhyyjvAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wOC0wM1QxNToxOToyMyswMjowMPZxGwAAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC)|Press Num Lock | Press the Num Lock key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAA0lBMVEUAAABffKBjfKNifaFjfaJifKNifKNifKNifKNifaNhfKNifKNifKNifKNie6RhfaJjfaRjfKJhfKNheqNifKNifKNje6JifKNifaJmgJlggJ9ie6JifKRifKNifKNifKNifKNhfKJjfKNhfqJhe6JifaNifaJie6Nie6NjfKNhfaNggJ9ifKNifKNidp1ke6RmZplifKNifaNhfKNkgKRgfaRifKNifKNjfqRifKNifKNifKNhfKRie6NifqVifKRje6VgfaNifKNifKJifKMAAAAaoMKDAAAARHRSTlMAI1A5WP6esfasoKnz+bg/iaiQMvhOXehgChi+bfX37spCSEd2VtdyW8KLEPLwDTgFqy/HHC376kPO/OVU20HGPj2CmoKHyGIAAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4gcfDwoLS2P9zwAAAMJJREFUOMvl09cOgjAUgOEjuBW3orhxoii4cO/z/s8kGghQaHkA/5sm8IWS0xTAW4TzxBOvIRpDb3ECJBCTqbRdJosCAXKI+ULRrlRG9IFK1bVBTQwAnAvU/wg0JFdNP2i1vafTIUGXOD7fF8yl15edBkM/GI2RkgVk58lkGgIkoANFYYPZXGWBBQdLzUyngZVuzXpN22Kz3YnfDOo/7A/HkDmczlRwuVIGadzUH7g/5OCeL/PiCMhMgDgbvAF4jpEGH821q5ZoP5xyAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTA3LTMxVDE1OjEwOjExKzAyOjAw9Yx2lQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wNy0zMVQxNToxMDoxMSswMjowMITRzikAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC)|Press Enter | Press the Enter key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAA7VBMVEUAAABifqVhfKRifKNhe6difKNhfaRie6RifKNifKNifaJjfaJhe6FigKdjfKNie6RifKNmgJlifKNifKJgfaNifKNhfKJleaFggJ9meqNjfKNifKRifKNhfKNkfKNifKNddKJifaNie6RhfaJifKNjfaRifKNifaJifKJifKNifKNigKVjfKNifaNmgKJifKNje6NggJ8AAP9ifaNie6NifKNifKJVVaptbZJifKNifaJje6JpeKVhfKNhfKNifKNifKNhfaJjfKKAgL9ifKNie6NifaNVcapgeqVifKNifKNifKNifKNifKMAAAAffb+/AAAATXRSTlMAQa37HfyDuP65YFhPGm942grukj3McSYYGVCi+pBA5QuFcDeIavZo4vd1IrXZHsp0CAFW2+NjAwek100Rv5jQ8D+oBPRyrAkwgvP4+Q2HcRMAAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4ggDDxIKJuAq9gAAAPhJREFUOMvN01dTwkAUBeBDCSXUBBQQCcVQLChVBaRXgfv//w6LRM3AbvaV85CX/WZzZudewOX2kCAetwvwKuQQxQsfOcYHP/sGgmroImowwI78PyAcicYuEo2Ef0Fc03m361rcAokk0c1tKp3O3GXvbSKZsEDOoHwBpxRtwMj9gxLwYJplQKvwgQpUiWqs2yMfPAHPL+ct7aD+yv5vvIkB6Y0m0Gp3hICo+/4BfPbEgKg/AL4UPhiORkOiMSsy4YMqMJ3NTGC+4IP+3HrJpajDarBmx5vvrbikstvtHd6Bl6sCx5Hj5W/kpEMrHXvnxZGunnR5Zet/AOS93hzGiKnAAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTA4LTAzVDE1OjE4OjEwKzAyOjAw14nV/AAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wOC0wM1QxNToxODoxMCswMjowMKbUbUAAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC)|Press Space Bar | Press the Space bar key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAApVBMVEUAAABifqVhfKRifKNhe6difKNhfaRie6RifKNifKNifaJjfaJhe6FigKdjfKNie6RifKNmgJlifKNifKJgfaNjfKNjfaRifKNifKNhfKNkfKNggJ9VgKpje6JifKNifaNifaNifKNifaJgeqVhfKRddKJifKNgfKVifKNjfKJifaNifKRgeaZke6Rje6Vie6Nmd6pifKNjfaRjfKNifKNifKMAAADLEAQGAAAANXRSTlMAQa37HfyDuP65YFhPGm942grukj21sLfykEAQBk34hazwhzBMC8Ul6qheZSg4H1sP5Gpn9O6JV9wAAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4ggDDxMNoZ+OFAAAALxJREFUOMvNk8cOglAQRQfpSAcL2MCOin3+/9fkIZYEHrNw41m8vGROJrO4F0DoiMhB7AgAkowtyBIo2IoCavFqutGtYehaMVJLwbRsp4ZtmS/B9fym7b7nVkIQIvb6jMHw2wiDSohixBGUjCfTjxBHdQFgxheSNJ0DLPgC+7UKzw1L4obVmhA2W77gZNkOYP/DkaRwyPMjwIk48nzhCFeDcUvuyBGa+CuBRa6Jd+TI0JKxby8OWT2yvFT9Hzt6mG3OxEGhAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTA4LTAzVDE1OjE5OjEzKzAyOjAwCaOkXwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wOC0wM1QxNToxOToxMyswMjowMHj+HOMAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC)|Press Backspace | Press the Backspace key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAkFBMVEUAAABifqVhfKRifKNhe6difKNhfaRie6RifKNifKNifaJjfaJhe6FigKdjfKNie6RifKNmgJlifKNifKJgfaNifKNifKNifKNhfKNkfKNlfaBifaJifaNVgKpifKNifaNhfKRggJ9ifKNjfKNVVapifaJhfaJhfKNifKNifKNgeqVhe6NjfaJifKNifKMAAACy4TRgAAAALnRSTlMAQa37HfyDuP65YFhPGm942grukj302OOQQCuHtgbAZkwIiEgDaDdh4MUwOoHWBsSESQAAAAFiS0dEAIgFHUgAAAAJcEhZcwAADdcAAA3XAUIom3gAAAAHdElNRQfiCAMPEwDfLvKpAAAAqUlEQVQ4y92TxxKCMBRFL70ISFPBEkWN3fz/5wkRywwpW8ezyGSSM1m83AsYpsUkWKYB2A5T4NhwmRIXXrv6QTgaEAZ+e+VxIYqT8YAkjl5CmuWi1/Ms7YWiZGwy5cy+jbLoharuNk/mi49QVwIBWEqFFSFkDWykQtOebYHdnwt7SukBOGom2ZzEwvnCud7ukr8Q8VNCFzkR78hpQ6uNvbo42uppy6ur/wPSKoc8yA0EyQAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wOC0wM1QxNToxOTowMCswMjowMPThvlwAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDgtMDNUMTU6MTk6MDArMDI6MDCFvAbgAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg==)|Press Delete | Press the delete key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAilBMVEUAAABifqVhfKRifKNhe6difKNhfaRie6RifKNifKNifaJjfaJhe6FigKdjfKNie6RifKNmgJlifKNifKJgfaNifKNifKNie6NhfKNkfKNhfKNggJ9heaRifKNifKRke6RtbZJggJ9ifKNifKNifKNdgKJifaJjfaNggJ9ifKNgeqVje6VifKMAAACntH0CAAAALHRSTlMAQa37HfyDuP65YFhPGm942grukj3v2NuQQJgYKsDGOAcg1tDmFmhsCKswNrCAMdAAAAABYktHRACIBR1IAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4ggDDx0D2KSOnQAAAKpJREFUOMvNk8kOgjAURR/zIEUmFZwHcHz//30Wi4ZI2xcWJp5FNz1pbpp7AQzTQgWWaQDYDmpwbHBRiwseP/0gnAwIA59feS8hYvF0QMyit5Ckmez1LE06IS8QZ3PBomcUeSeUFeISBKueUJUjhfWGs9UIu++Uo4X9gXOkQp40Amv/r/5pyObMuVAhryrhdhc8VIKMvxLaysn4VI4sLVl7/XDI6ZHjpeb/BD+wha8hV0UXAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTA4LTAzVDE1OjI5OjAzKzAyOjAwXOvCwAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wOC0wM1QxNToyOTowMyswMjowMC22enwAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC)|Press End | Press the End key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAaVBMVEUAAABifqVhfKRifKNhe6difKNhfaRie6RifKNifKNifaJjfaJhe6FigKdjfKNie6RifKNmgJlifKNifKJgfaNjfaRifKNhfKNkfKNje6NggJ9eeaFVgKphfKNgeqVifKNhfKJifKMAAAAgBlLQAAAAIXRSTlMAQa37HfyDuP65YFhPGm942grukj2wgJBAdCATBpgw0qUQSuUJAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAAN1wAADdcBQiibeAAAAAd0SU1FB+IIAw8cDSYHktsAAACVSURBVDjL7ZPLDoJADEUvbxgBeelgfWD//yedGEYxA9PElQvPopueNF3cCwRhxBtEYQDECXtIYqTsJUVmZl6onYMqcrPKnkJZ1XuHuiqt0LTd2vWubWahH/hwtCyMoZ8FPbKCZSGM+i2ciM7AhYg2BMMVuH0+8Re+Eyat717B5acEE7lVXpETQyvG3l8csXpieaX6PwA4C2rRdSrKwgAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wOC0wM1QxNToyODoxMyswMjowMH+DqWAAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDgtMDNUMTU6Mjg6MTMrMDI6MDAO3hHcAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg==)|Press Tab | Press the Tab key. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAfpAAAH6QGUejxAAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAVZQTFRF////29vb6+vi5eXTzb/I6Ojg6enf6urfwrTFuae/4uLX3dzQ6eng3NrOo4ewl3eomHiomHipmHmpmnuqm3yqm3yrnH6sn4Gun4OuoIOwoYSwoYSxoYWvooWxo4aypYqxpYq0pYuypou1p4y2qI6zqY+3qZC1qpG1q5G4q5O2rJK5rJO6rJW2rpW7rpe4r5a8r5i4sJq5sZm+spy6tJ3BtJ+8tKC8tqK9t6O+uKW/uaa/uqXGvKfHvKjHvanIvqrJv6vJwK/Ew7HNxLbHxbPOxrjIx7nJyLfRyLjRy7/My8DMzr7WzsPO0MfP0cfP1MzS1cjc18ve2Mzf2c3f2c7g2dfK2tTV29rN3NfX3djY3tTk3tnY3trZ39zZ4N/U4eDW4t/b4+Dc5OHc5OLd5OPd5d3q5uXe5+bf5+ff6Off6eng7Obv7ejw8ezz8e3z8u709vP3/f3+Bb+anQAAAA90Uk5TAA4aHThCR0htfNnr7PP7HqL7KAAAATBJREFUOE+tzvk3AlEUwPFBVJYuZcoWso41xkQI0TBCYazJUra4Y/3/f9FjTmaa+45ffH+YO+e8z3nvCoIg1DZjVY11grWG6nO8brEJtxOc2AQFbIIEVkEDi3CCmzNWUw0XmNVzQSr9Pdx2kJ7ti5mgJ0uAhUA8e4538TziafujE2Rac2xcduwjrs+hEyzNYKXIDgHmFyvnef8tAbbEezbYDqlJJEApMrL3/LPD6CYFsBgLwBj7KbRdkQDxKVdkIzOEHGBWKvwBfvs/4Jnm5DGBFzh5raBT0zRpYBn6E5DUtKQTSIYsh8W30PEaGKvyBAEe2Hfj4MUPxiD1hPSh690Q/NwGMC70BPeGI4N7w6uqDovv4cPyDrvqihMEFUXpDU1B1zhEFSVqAy4fkPlc5cMvjuvkA0Hh2hAAAAAASUVORK5CYII=)|Type In Run Window | Type the entered text in the Windows "Run" window. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAGVAAABlQEMTY6IAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAOpQTFRF//////8A/4AA//+AqqpVv4BA/79AzJkz/8xm379g48ZV6NFdzp0x8chg7Mdd7sVd8cZe7chg7slc78Zf78hf8Mhf8MZe78he78de78hfyp8vyp8v8MZeyqAw7sZey58x78ddyp8w78deyp8w8Mde8MdfyZ8x7sZd7sdeyZ8xz6M0y54wyp8wyp4wyp8x78he8Mhe78Ze78de78df8Mde78de78de78de78de78de78de78de78de78de78de78de78de78de3LNG78deyp8wzKEy0qc63LNH3rRJ4bhN5LtR68NZ7sZd78deCBVgzgAAAER0Uk5TAAECAgMEBAUFCAkLGiUpLDY4PV5hZmd9gIGCh4eLi42OkJOUlpeYmZqdnqGlqa3BxsvMzdfZ3OHj6+3w8/X2+fz9/v75BNv9AAABFElEQVQ4jXXR2VaDQAwG4LgvoGhV6lKt4ob7gsWlqEUGVDTv/zp21IGkE/4LOGfynSQDAL/x/DBKotD3QIwTZPiXLHCEeivGOnHLrqdIk44KJ0aeeGRKoA/LIi9KIwJW9/R+pdIxImN38fVRobpuVxWmhU9BqE9y5YKrcgNCCiKhQ0RBgtYO+ELBLVq3wAcKjtHONQVrAtigYDG1Af+nuzboMDDfs8UKE8sDC/QYgKU7Uvv6HD6eOIC5HbPp90eu3ofv5LHNycLqwc3z/VX7VH9RLbAPYmYujejPTohi6qLqgeuimDyvxKs8ZfzMiGy6QZxUPQYdUYwd1XscymK/FvIU2KtEA4BtI5oAbP2LRgCbWrzhD6LNhybH0Wi3AAAAAElFTkSuQmCC)|Create Unique Key | Returns a UUID as a string with. "Length" determines the amount of characters returned. |
| **Monitoring** |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAPmSURBVFiF7Vc9TCNHFP52ZxbRnAQnJ3fgv1UiErmIlMKHCwoqXCAFRIloLFpMCtMQKXVKZAlCBaJPQ0FDh6BFsoKuhMR/wjj742Aj2cbe2ZcCFi3eBeMj190nWfK8N/Pem3nvfbMDIsJzP13XM6ZpztyPua7rBy7dkq7rS67xARFxIoJpmjO6rmf62ZfRB5IkRYQQQQAoFAocwAeXLixJUtg1/cP9HAghgpIkRfrZ7xvA58aXACQi8gjn5+fniOgXAKOpVOrrYrF4e3R0VFcURdrY2PhmdXX1LwBYWFh4CwD7+/s1ANjc3Pw2k8n83e12aXJyUo1EInxnZ0dwzv8dGhr6+fDw8I9eX9wvKiLaBhAEgHw+j0qlAgDvhRDI5XIA8D0AFItFZ8lXAJDL5SCE+O729hbFYhG2bcO2bdbpdN4R0e8APAH4nsDc3JxX+EIQEa6vr9FrV5Zl6+TkROmdzw3DyPS2y+LiIiqVCo6PjwcOoNVqeZwnk0lEo1HZNM1sT7AlLsvyRyFEza0olUrQNG1g50IItNttj7xcLjvp+NMtZ4xd/q8paDQasCzLV/dkCgBwh70cKIoCIQRs236x806n85xzKIqCQqEw7JarqmpJuq4fwEWv9zt5d3Z2hr29vUeGAoEAVlZWPA6ICJVKBZZlYXt725OGdDqNeDyOkZGRf3qWnvJAIPBTr8Hl5eWBUlCv15/cPQBsbW05KXjfq3s1E1qWhUaj8cnruWEYSz03GmZnZ1GtVh3SeRa1Ws3Tdr1IJBIIh8OyaZrrbjkRlV91As1mE61W6zUmBmNCdxG6C88NvyIEnm7DTz6BfoX3UnDDMDxtmM1m4deGDgYtvPs25IZhVHtUpxIReYhobW2t5UdEjDGMjo7CsiwwxnydXVxc+F1EUBTF2t3dfeOWq6pqcQCWqqqPzrLb7foaF0Lg6uoKNzc3T2/XB7Zto9vtQlVVT3HwWq0243x0OpiamoKmaTg/P/cYazabAzkHgFgshmAwKOu6nnLLGWOX3LbtH2RZfnQdRyIRcM49AbTbbQghBg4gHA4jGo1CluUf3XLbtt++uA1t20a9Xu9LOk9h0DasO3+mp6cxMTGBZrMJSZKQTqcfJiUSCSQSiYdxOp2GLN+ZjMViSCaT7gB8Gcs3AEmSfgVwDQDj4+MIBALodDrgnCMejz/MC4VCCIVCD+N4PA7O7xpqbGwM4fAdwzPGuoqi/Oa71X5PJ8MwspqmpYgI+Xx+WNf1qku3bhjGuutpVs3n88NEBE3TUoZhZF/9NPvc+BJA3wCIqMQYuwTuqBPAqUtXJqKya/qpw6qMsUsiKvWz/x9uEJRGaoWMHQAAAABJRU5ErkJggg==)|CPU Load | Returns average CPU load for all cores over a measured time. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAPmSURBVFiF7Vc9TCNHFP52ZxbRnAQnJ3fgv1UiErmIlMKHCwoqXCAFRIloLFpMCtMQKXVKZAlCBaJPQ0FDh6BFsoKuhMR/wjj742Aj2cbe2ZcCFi3eBeMj190nWfK8N/Pem3nvfbMDIsJzP13XM6ZpztyPua7rBy7dkq7rS67xARFxIoJpmjO6rmf62ZfRB5IkRYQQQQAoFAocwAeXLixJUtg1/cP9HAghgpIkRfrZ7xvA58aXACQi8gjn5+fniOgXAKOpVOrrYrF4e3R0VFcURdrY2PhmdXX1LwBYWFh4CwD7+/s1ANjc3Pw2k8n83e12aXJyUo1EInxnZ0dwzv8dGhr6+fDw8I9eX9wvKiLaBhAEgHw+j0qlAgDvhRDI5XIA8D0AFItFZ8lXAJDL5SCE+O729hbFYhG2bcO2bdbpdN4R0e8APAH4nsDc3JxX+EIQEa6vr9FrV5Zl6+TkROmdzw3DyPS2y+LiIiqVCo6PjwcOoNVqeZwnk0lEo1HZNM1sT7AlLsvyRyFEza0olUrQNG1g50IItNttj7xcLjvp+NMtZ4xd/q8paDQasCzLV/dkCgBwh70cKIoCIQRs236x806n85xzKIqCQqEw7JarqmpJuq4fwEWv9zt5d3Z2hr29vUeGAoEAVlZWPA6ICJVKBZZlYXt725OGdDqNeDyOkZGRf3qWnvJAIPBTr8Hl5eWBUlCv15/cPQBsbW05KXjfq3s1E1qWhUaj8cnruWEYSz03GmZnZ1GtVh3SeRa1Ws3Tdr1IJBIIh8OyaZrrbjkRlV91As1mE61W6zUmBmNCdxG6C88NvyIEnm7DTz6BfoX3UnDDMDxtmM1m4deGDgYtvPs25IZhVHtUpxIReYhobW2t5UdEjDGMjo7CsiwwxnydXVxc+F1EUBTF2t3dfeOWq6pqcQCWqqqPzrLb7foaF0Lg6uoKNzc3T2/XB7Zto9vtQlVVT3HwWq0243x0OpiamoKmaTg/P/cYazabAzkHgFgshmAwKOu6nnLLGWOX3LbtH2RZfnQdRyIRcM49AbTbbQghBg4gHA4jGo1CluUf3XLbtt++uA1t20a9Xu9LOk9h0DasO3+mp6cxMTGBZrMJSZKQTqcfJiUSCSQSiYdxOp2GLN+ZjMViSCaT7gB8Gcs3AEmSfgVwDQDj4+MIBALodDrgnCMejz/MC4VCCIVCD+N4PA7O7xpqbGwM4fAdwzPGuoqi/Oa71X5PJ8MwspqmpYgI+Xx+WNf1qku3bhjGuutpVs3n88NEBE3TUoZhZF/9NPvc+BJA3wCIqMQYuwTuqBPAqUtXJqKya/qpw6qMsUsiKvWz/x9uEJRGaoWMHQAAAABJRU5ErkJggg==)|Number Of CPU | Returns the number of CPU's in the current system. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAPmSURBVFiF7Vc9TCNHFP52ZxbRnAQnJ3fgv1UiErmIlMKHCwoqXCAFRIloLFpMCtMQKXVKZAlCBaJPQ0FDh6BFsoKuhMR/wjj742Aj2cbe2ZcCFi3eBeMj190nWfK8N/Pem3nvfbMDIsJzP13XM6ZpztyPua7rBy7dkq7rS67xARFxIoJpmjO6rmf62ZfRB5IkRYQQQQAoFAocwAeXLixJUtg1/cP9HAghgpIkRfrZ7xvA58aXACQi8gjn5+fniOgXAKOpVOrrYrF4e3R0VFcURdrY2PhmdXX1LwBYWFh4CwD7+/s1ANjc3Pw2k8n83e12aXJyUo1EInxnZ0dwzv8dGhr6+fDw8I9eX9wvKiLaBhAEgHw+j0qlAgDvhRDI5XIA8D0AFItFZ8lXAJDL5SCE+O729hbFYhG2bcO2bdbpdN4R0e8APAH4nsDc3JxX+EIQEa6vr9FrV5Zl6+TkROmdzw3DyPS2y+LiIiqVCo6PjwcOoNVqeZwnk0lEo1HZNM1sT7AlLsvyRyFEza0olUrQNG1g50IItNttj7xcLjvp+NMtZ4xd/q8paDQasCzLV/dkCgBwh70cKIoCIQRs236x806n85xzKIqCQqEw7JarqmpJuq4fwEWv9zt5d3Z2hr29vUeGAoEAVlZWPA6ICJVKBZZlYXt725OGdDqNeDyOkZGRf3qWnvJAIPBTr8Hl5eWBUlCv15/cPQBsbW05KXjfq3s1E1qWhUaj8cnruWEYSz03GmZnZ1GtVh3SeRa1Ws3Tdr1IJBIIh8OyaZrrbjkRlV91As1mE61W6zUmBmNCdxG6C88NvyIEnm7DTz6BfoX3UnDDMDxtmM1m4deGDgYtvPs25IZhVHtUpxIReYhobW2t5UdEjDGMjo7CsiwwxnydXVxc+F1EUBTF2t3dfeOWq6pqcQCWqqqPzrLb7foaF0Lg6uoKNzc3T2/XB7Zto9vtQlVVT3HwWq0243x0OpiamoKmaTg/P/cYazabAzkHgFgshmAwKOu6nnLLGWOX3LbtH2RZfnQdRyIRcM49AbTbbQghBg4gHA4jGo1CluUf3XLbtt++uA1t20a9Xu9LOk9h0DasO3+mp6cxMTGBZrMJSZKQTqcfJiUSCSQSiYdxOp2GLN+ZjMViSCaT7gB8Gcs3AEmSfgVwDQDj4+MIBALodDrgnCMejz/MC4VCCIVCD+N4PA7O7xpqbGwM4fAdwzPGuoqi/Oa71X5PJ8MwspqmpYgI+Xx+WNf1qku3bhjGuutpVs3n88NEBE3TUoZhZF/9NPvc+BJA3wCIqMQYuwTuqBPAqUtXJqKya/qpw6qMsUsiKvWz/x9uEJRGaoWMHQAAAABJRU5ErkJggg==)|CPU frequency | Returns frequency at which CPU currently operates together with maximum and minimum frequency. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAPmSURBVFiF7Vc9TCNHFP52ZxbRnAQnJ3fgv1UiErmIlMKHCwoqXCAFRIloLFpMCtMQKXVKZAlCBaJPQ0FDh6BFsoKuhMR/wjj742Aj2cbe2ZcCFi3eBeMj190nWfK8N/Pem3nvfbMDIsJzP13XM6ZpztyPua7rBy7dkq7rS67xARFxIoJpmjO6rmf62ZfRB5IkRYQQQQAoFAocwAeXLixJUtg1/cP9HAghgpIkRfrZ7xvA58aXACQi8gjn5+fniOgXAKOpVOrrYrF4e3R0VFcURdrY2PhmdXX1LwBYWFh4CwD7+/s1ANjc3Pw2k8n83e12aXJyUo1EInxnZ0dwzv8dGhr6+fDw8I9eX9wvKiLaBhAEgHw+j0qlAgDvhRDI5XIA8D0AFItFZ8lXAJDL5SCE+O729hbFYhG2bcO2bdbpdN4R0e8APAH4nsDc3JxX+EIQEa6vr9FrV5Zl6+TkROmdzw3DyPS2y+LiIiqVCo6PjwcOoNVqeZwnk0lEo1HZNM1sT7AlLsvyRyFEza0olUrQNG1g50IItNttj7xcLjvp+NMtZ4xd/q8paDQasCzLV/dkCgBwh70cKIoCIQRs236x806n85xzKIqCQqEw7JarqmpJuq4fwEWv9zt5d3Z2hr29vUeGAoEAVlZWPA6ICJVKBZZlYXt725OGdDqNeDyOkZGRf3qWnvJAIPBTr8Hl5eWBUlCv15/cPQBsbW05KXjfq3s1E1qWhUaj8cnruWEYSz03GmZnZ1GtVh3SeRa1Ws3Tdr1IJBIIh8OyaZrrbjkRlV91As1mE61W6zUmBmNCdxG6C88NvyIEnm7DTz6BfoX3UnDDMDxtmM1m4deGDgYtvPs25IZhVHtUpxIReYhobW2t5UdEjDGMjo7CsiwwxnydXVxc+F1EUBTF2t3dfeOWq6pqcQCWqqqPzrLb7foaF0Lg6uoKNzc3T2/XB7Zto9vtQlVVT3HwWq0243x0OpiamoKmaTg/P/cYazabAzkHgFgshmAwKOu6nnLLGWOX3LbtH2RZfnQdRyIRcM49AbTbbQghBg4gHA4jGo1CluUf3XLbtt++uA1t20a9Xu9LOk9h0DasO3+mp6cxMTGBZrMJSZKQTqcfJiUSCSQSiYdxOp2GLN+ZjMViSCaT7gB8Gcs3AEmSfgVwDQDj4+MIBALodDrgnCMejz/MC4VCCIVCD+N4PA7O7xpqbGwM4fAdwzPGuoqi/Oa71X5PJ8MwspqmpYgI+Xx+WNf1qku3bhjGuutpVs3n88NEBE3TUoZhZF/9NPvc+BJA3wCIqMQYuwTuqBPAqUtXJqKya/qpw6qMsUsiKvWz/x9uEJRGaoWMHQAAAABJRU5ErkJggg==)|CPU Stats | Returns CPU statistics: Number of CTX switches, interrupts, soft-interrupts and systemcalls. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAATtQTFRF////LYctK4ArKYAtKYEvKTE5KYIuKYIuKIEwKIIwKIIvJ4EuKTI5KIEvKIEvJ4AuKTI5KYEwcKBCcKBDb51BcZ9BdKFCfKRFgqdGhKhGiapIJ4EvKIIvnrJNpLVPKIEvp7VQq7dQKIEwKIEvKDI4KGwxKIEuKIEvKIEvKIEvKIEvKIEvKIEvKDI4KIEvKoIvKoIwLoQxL2s7MGg9MG06Ml1CN0lNOEVPOok0PYo1P4s1Q4w2RI02R2ZISI43SmVJSmtHS5A4TmtJTnJGUnJIVJM6WW9LWZY8XZc9YXdLZZs/Z5s/Z5w/aHlOaH9LaJtAaJw/bZ5BcqBCc4NOdqJDeaNEeqNEe6REfo1PgKZFhKhHka1Kl69LnbJNoLNOo7ROqbdQrrlRsrtStbxTyMRY1Mlb2sxc4M5e7NNh+0K73QAAAC10Uk5TABEYPl1eXmRlZmxvcHOOj5CQq6usrK2xs7W3vL3Dx8jJy8zNztTs9fb4+/3+KwNVbwAAAQtJREFUOMtjYIAAAV1dVS0mBkZ1PQhQY2ZABawquqp6yrzyYFkdJW09PjQFDDxABfrulo6OFnp63AzseoLYFBhmhCYnB+npcTKwYFdgEuHi5+esp6cpo4ldgak5EJgBHREYFSWGV0FUfLwUNgXGvvZubrZABXEpKbL4HKnnHxYmhE2BQZCdh4cNUEFSeroiNgVwEBIdLY5XQWRsrCTWkPSydnW1AipISE2Vw+tI79BQEWwKjIKdPD0dgAoS09IU8AZUeEyMBFkKCFoBd6RPaKgwWd4kGFAEg5pgZMEdGRAWJkpWgiGY5AgmWliy15LW0OPHn3HYsOcLWNbjYuDAUICSebWVtTAyL87sDwAH1W5FFYuAgAAAAABJRU5ErkJggg==)|Memory Stats | Returns memory statistics: total, used, free and percentage in use. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAT1SURBVFiFtZdbbBRVGMd/M7Ozt2Zv9AKltEIBlxRIFTBADJemWKJWIzaIgUajBjVKjPFBY3w0MUETgzHxgZuJASMkWMEUqYKAsSoRwcamstArdbttybbdNm23s7szPmy73WFml7bG/+P/fPN9v3POnJugaRpTunqr6wbg53+Qqqp0tLUiy1bl6Ue22KZ8iy5Kw44AwxNRlHg8ZeeIFoRZFtSAUXU6h0WUkr6miulxeoBJPdr6M4o92SSoGhUHryDG1VkBqBaRiy+vRxOT6NZonC+sJYY40eAAqjjd3/yOgVkXBxDjKvkdA6Y502U6AlOSYgmKm0KmbS6Pm6LS+wAItncxEhk2xBQ3hQiXeEnIUsYpNAUoahvA0T9CYeAOkpJI+d7ceWzf9RSL/cvwzPPqvokMDNEZaKXhxDcMhZM99/UMs/nzq4T8+YwXuMBfPDOA1Y23iUYndN5DWx/msT012Ox205545nkp37iOFQ+u4uzxU/x+qREASUmw6K9e7PZB8JfPDOBu7XrtRco3rptJKDa7nR0v7aG0zM+Jz47eM970J0zXmk0bZlw8XeUb17Fm04b/BuD2eamu3Tnr4lOqrt2J2+fNGpN1CrbVVGN3Ogy+GI3iO1OPo+UGAONlKxh88nHUu/4Pu9PBtppqvj58bG4AJctLjcUnJij64CPkvv6UZw314mxuIfje26g2my7eLIcuX6YGm91OfuF8g+8925AqHkqohBLJTUru68d7tsEQn184P+PKyQpQtKQEQTBuH47ALQDCqsa+yCj7IqOEVU3Xli5BEChaYtyCp5RxCuJph1G6NEvyUJEFsE8CyoK+baa5sgKEurpREyqipB+ksZVl2G+14RYEDnlzAHBOgoytLDPkURMqoa5uJNF8sDNOQUyJ0RfsMfiRqkqiy5emCk8Vjy5fSqSq0hDfF+whpsQylcm+CtpbblJYskjnaZJE6K03cF+8jKMlAMB4mZ/hii1oJr1sb7mZrUR2gAt19axevxa3z6OHEEUilRVEKit0vqyOoCESF5NTMzwY4UJdfVaArDthdGycuiPHsybQJdMmuH/wMLZEGIC6I8eJjo0D4PG5Zw8AEGhq5vK3xvVtJkXyYVFHKB36ksb67wg0NQOQm+fj+b3PzA0AoOHkaY7u/5RIeDBrnIZEmCXYEmEWjF5MFd/7ei0ej8v0mxkdxwCtzX9z4N332fLEdhb7l1G0uBjZagUgpigEO7vpDLQSuv4n+1/NYcdmJ00dVrbV7MHjdRGLme8FpgC+XC+hYJ/BnxiP8v3J0wCIokhB0QIA+oO9qOr0vbG53cqqUpl3nsujTc7h18ZrXDr/Czt3Vxlymk7BC688S35BbtYRUVWV3u4eert7dMUBfriWTJsjDRHtPMeZU+cMN6ysAC5XDnv31d4Twky5eT7WVu1mguQ94IGFQRbmSZD2ALonwFwhnDmO5A/ndXGl3Y2mwfVAlJqtTrTZAswFwuNx4fG6uN0Z5OODfxC8k2BRgYU7Qyrm5TMA/PTjbxz48BCKEpvTSAwORlBiGm9+MsD+YyN8dX509lOQrplCSJPHcW6eD4tFYiyq0fpPHE2D0mX3mX4j6F7HN7s6ETCPBBIJlZiiZAGwIMvJla0oMdTE9KPGIst0dbRhsVjiNVUVcsrX4xDN2kNJRHJkvl6ly2qVgVSd1FIVBFG3Zv8FQwDFpyPx1wAAAAAASUVORK5CYII=)|Disk Stats | Returns disk statistics of main disk: total, used, free and percentage in use. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAT1SURBVFiFtZdbbBRVGMd/M7Ozt2Zv9AKltEIBlxRIFTBADJemWKJWIzaIgUajBjVKjPFBY3w0MUETgzHxgZuJASMkWMEUqYKAsSoRwcamstArdbttybbdNm23s7szPmy73WFml7bG/+P/fPN9v3POnJugaRpTunqr6wbg53+Qqqp0tLUiy1bl6Ue22KZ8iy5Kw44AwxNRlHg8ZeeIFoRZFtSAUXU6h0WUkr6miulxeoBJPdr6M4o92SSoGhUHryDG1VkBqBaRiy+vRxOT6NZonC+sJYY40eAAqjjd3/yOgVkXBxDjKvkdA6Y502U6AlOSYgmKm0KmbS6Pm6LS+wAItncxEhk2xBQ3hQiXeEnIUsYpNAUoahvA0T9CYeAOkpJI+d7ceWzf9RSL/cvwzPPqvokMDNEZaKXhxDcMhZM99/UMs/nzq4T8+YwXuMBfPDOA1Y23iUYndN5DWx/msT012Ox205545nkp37iOFQ+u4uzxU/x+qREASUmw6K9e7PZB8JfPDOBu7XrtRco3rptJKDa7nR0v7aG0zM+Jz47eM970J0zXmk0bZlw8XeUb17Fm04b/BuD2eamu3Tnr4lOqrt2J2+fNGpN1CrbVVGN3Ogy+GI3iO1OPo+UGAONlKxh88nHUu/4Pu9PBtppqvj58bG4AJctLjcUnJij64CPkvv6UZw314mxuIfje26g2my7eLIcuX6YGm91OfuF8g+8925AqHkqohBLJTUru68d7tsEQn184P+PKyQpQtKQEQTBuH47ALQDCqsa+yCj7IqOEVU3Xli5BEChaYtyCp5RxCuJph1G6NEvyUJEFsE8CyoK+baa5sgKEurpREyqipB+ksZVl2G+14RYEDnlzAHBOgoytLDPkURMqoa5uJNF8sDNOQUyJ0RfsMfiRqkqiy5emCk8Vjy5fSqSq0hDfF+whpsQylcm+CtpbblJYskjnaZJE6K03cF+8jKMlAMB4mZ/hii1oJr1sb7mZrUR2gAt19axevxa3z6OHEEUilRVEKit0vqyOoCESF5NTMzwY4UJdfVaArDthdGycuiPHsybQJdMmuH/wMLZEGIC6I8eJjo0D4PG5Zw8AEGhq5vK3xvVtJkXyYVFHKB36ksb67wg0NQOQm+fj+b3PzA0AoOHkaY7u/5RIeDBrnIZEmCXYEmEWjF5MFd/7ei0ej8v0mxkdxwCtzX9z4N332fLEdhb7l1G0uBjZagUgpigEO7vpDLQSuv4n+1/NYcdmJ00dVrbV7MHjdRGLme8FpgC+XC+hYJ/BnxiP8v3J0wCIokhB0QIA+oO9qOr0vbG53cqqUpl3nsujTc7h18ZrXDr/Czt3Vxlymk7BC688S35BbtYRUVWV3u4eert7dMUBfriWTJsjDRHtPMeZU+cMN6ysAC5XDnv31d4Twky5eT7WVu1mguQ94IGFQRbmSZD2ALonwFwhnDmO5A/ndXGl3Y2mwfVAlJqtTrTZAswFwuNx4fG6uN0Z5OODfxC8k2BRgYU7Qyrm5TMA/PTjbxz48BCKEpvTSAwORlBiGm9+MsD+YyN8dX509lOQrplCSJPHcW6eD4tFYiyq0fpPHE2D0mX3mX4j6F7HN7s6ETCPBBIJlZiiZAGwIMvJla0oMdTE9KPGIst0dbRhsVjiNVUVcsrX4xDN2kNJRHJkvl6ly2qVgVSd1FIVBFG3Zv8FQwDFpyPx1wAAAAAASUVORK5CYII=)|Disk Partitions | Returns tuple with info for every partition. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAdiAAAHYgE4epnbAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAPxQTFRF////AAD/gICAUGCAVWOAVWGGWWSFVWCCVV+BVGGAVmCBV2GCWGKFVmKDV2GCV2KFWGOGV2OEV2OEV2KDVmGCVmKEV2KDVmCCW2eMV2OFYG2XYm+bVWGBVWCBWWWKVWCAVmGCWWSDWmaLW2aMW2eMW2eNXWmRXmqTYG2XYW6ZYW6aYm+cY3CdZnSkZ3WnaHaoaXeqaXiranmsa3mta3qubHuwbXyybXyzbneSbn20bn21b362coK9coK+c4K+c4O+c4O/dYXAdn+ZdobBfYWef43Ei5jKjZSqkZ3NpK/WqbPYqrTYvcThvsXh8PH08PL49PX39vf7+Pn8+vr8gyzqRwAAAB90Uk5TAAECEBIVFy1LTHd+gIKTvr/B3ujp7O329/j4+fv8/qyjigcAAAGdSURBVDjLdVNnY4IwEI24B7hRQYl1DwQnFKkaq7XWllr1//+XomIIqPclueTlcuM9ALBRYSaRyuVSCSZMgXsL0GxB6CudjtIXCiwdcF17oiVO1WsIiSJCNV3lSlEPee9L5isyQm8ITSaXRa7kkz77PpjhZ5qKCFO1GZ8J4veZ8hjd2bicsWJ4kvxIvh1vNredPOKT1zyi+Zn9zjDs/SwfvdRXquiPAXqldK6W5iT1MUCRONrsH+tInwSYxbAUCBf05wC9EAaMUJ0/A8yrAgMSffQ8AuonQEohD3bH0zfpKymQ64gT7K8O2+3JMIyfj4s7ETs5J2C5326PLoDzi6/9Yef6wpXkcuVOkhHqdpmLXrPZW9hl1s0yHY1qvEAIG85Gka2W4O+niZAcrTaHJWuW34LrvzWELcudyudhkeNuQ/j+CmHbOW4QwYQZwIsNMGEiV87F+fEAh8ABBmM+bpHWm8akHXa7Q0zatJekvT4lG6TpJO2xcOZX4czvhHOWXtGUXv0qvbopvaJTeqb5Y1lbvNmY/4G+qdBN/iFC/v+lrK3wtSxuQAAAAABJRU5ErkJggg==)|Boot Time | Returns time PC was booted in seconds after the epoch. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAdiAAAHYgE4epnbAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAPxQTFRF////AAD/gICAUGCAVWOAVWGGWWSFVWCCVV+BVGGAVmCBV2GCWGKFVmKDV2GCV2KFWGOGV2OEV2OEV2KDVmGCVmKEV2KDVmCCW2eMV2OFYG2XYm+bVWGBVWCBWWWKVWCAVmGCWWSDWmaLW2aMW2eMW2eNXWmRXmqTYG2XYW6ZYW6aYm+cY3CdZnSkZ3WnaHaoaXeqaXiranmsa3mta3qubHuwbXyybXyzbneSbn20bn21b362coK9coK+c4K+c4O+c4O/dYXAdn+ZdobBfYWef43Ei5jKjZSqkZ3NpK/WqbPYqrTYvcThvsXh8PH08PL49PX39vf7+Pn8+vr8gyzqRwAAAB90Uk5TAAECEBIVFy1LTHd+gIKTvr/B3ujp7O329/j4+fv8/qyjigcAAAGdSURBVDjLdVNnY4IwEI24B7hRQYl1DwQnFKkaq7XWllr1//+XomIIqPclueTlcuM9ALBRYSaRyuVSCSZMgXsL0GxB6CudjtIXCiwdcF17oiVO1WsIiSJCNV3lSlEPee9L5isyQm8ITSaXRa7kkz77PpjhZ5qKCFO1GZ8J4veZ8hjd2bicsWJ4kvxIvh1vNredPOKT1zyi+Zn9zjDs/SwfvdRXquiPAXqldK6W5iT1MUCRONrsH+tInwSYxbAUCBf05wC9EAaMUJ0/A8yrAgMSffQ8AuonQEohD3bH0zfpKymQ64gT7K8O2+3JMIyfj4s7ETs5J2C5326PLoDzi6/9Yef6wpXkcuVOkhHqdpmLXrPZW9hl1s0yHY1qvEAIG85Gka2W4O+niZAcrTaHJWuW34LrvzWELcudyudhkeNuQ/j+CmHbOW4QwYQZwIsNMGEiV87F+fEAh8ABBmM+bpHWm8akHXa7Q0zatJekvT4lG6TpJO2xcOZX4czvhHOWXtGUXv0qvbopvaJTeqb5Y1lbvNmY/4G+qdBN/iFC/v+lrK3wtSxuQAAAAABJRU5ErkJggg==)|Time Since Last Boot | Returns time since last boot in seconds. |
| **Windows Activities** |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAYlQTFRF////SUlJQEBANUBKM0dSOURPOEZQOEZPOEVPN0VPN0VPOEVPOEVQOEVPOERPOEVPOEVPOEVPOUZROkdPOkdSO0hUO0hVPEhPPEpXPUlPPkpPPktaP0pPP01dQEtPQE1eQk1PQk9iRE5PRFJnRU9PRlBPR1BPR1VsSFFPSlhxS1lzTVt3TlVOTlZOT1ZOUFdOUF58UmCAUmGBU1lOVVpOVmSHV1xOWF1OWWiOWmiPXGBOXWBOXWyWX26ZYG+bYWROYXCcYmROYmVOZHOiZHOjZHSjZ3aoaXmta2tOa3uwbX20b25Nb363b3+3cIC6cXBNcYG7cYG8coK9c3FNc4O/dHJNdXNNe3dNe3hNgHtNg31Nhn9NioJNi4NNkIdNlYtMmI1Mmo5MopVMqppMrp5MsZ9MsaBMsqBMtKJMu6dLvKhLvahLvalLv6pLwKtLzLRLzbRLzrVLz7ZL0LdL1LpL17xL2r5L279L3cFK3sFK38JK4MNK4cRK4sRK5sdK6MlK68tK7MxK7cxK0mXPnQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAABeklEQVQ4y4WT1XbDMBBEN1AnDk+ZU2ZImZnZbVVmZmaGL+9DLclJnJN50vFcW+vdWSIhi6K6PH6/x6UqFoqW3emDkM9pj7CtjgDCFHBYjb7NjSi5bdJP8MrnTbP1+smbIN43+G2MDfKzV/+GVX4/sZMxNgQAOOgA3P91OISf3MsEsPVYBjiIiOyi/tQBJoG0mzMgYCciJ/fTh5kANvbR/jMKOIksvD85I4wDDY3FrzPYugZ8FlKAiklN0zTGNYiFh9z5l6LMnxZAIRXoZmEaAk53cbyN201AJRfQGwXU/GYvX2DvHHCRxwzAU1/LB9buAA/5TYGT1aSv6p53wB8DuJoRgOkVad9VzfwK0yLX7rF0qRepAm2RQO1nPw539N9UgJTKUCgUapWNWtnGxFuJ3ijRalTOySILnhd5q+WwUK4JYP1IDMswbpROcyAvQ47bEBgUTpkExhg55I9z4ERGLiy0wTHWFRna8Nhn1QWjYh9/ceKvXvzljb3+f9DtjCD/3H6zAAAAAElFTkSuQmCC)|Beep Sound | Makes a beeping sound with a given frequency and duration. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADhAAAA4QFwGBwuAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAL1QTFRF///////V/9vb39/f7u7d7+ff7uneU2KA8OndU1+AVWCBZG+J8Ord7+rdVGCAtbW5tba6w8PDVWCAVGCA7+rd7urd6eTZVGCAVGCA7+rd7+rdVGCA7+HU7+fZ7+jb7+nc7+rd8M/B8NLD8NXH8NjK8NrM8NrN8bKi8b2t8cW18peF8p2L8p+O8qaV8qyb84d084d184l2845785OB9I589JB+9JSD9JSE9ZeG+L6z+s7G/OTg/e7r/fDt/vj3vPTr0wAAABt0Uk5TAAYHCB4gLkREbm+Ptrq/wMDAx8jL2Nny+fz+OgMRSgAAAQxJREFUOMvFk1d3gkAQhbGgJpZYo4Jl7WC7YNkoov//Z2WWnACGIa/eF5j5vrMDC6tp8bz1TLP3rqWnZlJqabTYbHWV0G01i0ma1/WyGaas6/knXOoIIT4ioU5lpxQT2tQQ9WdBtCOeVbVoREIjaGRDIRfU/c8w/aCR+yMk8iJhNJuN/hHmWxdwt/M0wSKs4lq8MEGYCScMj7jcJCBvFxyHjDAFHM+X0vccYMoIFpRxvysOixFWarh8PL7UdcUItuK+R1PoxmaEBXCi+fQcJ2DBveYO5yvNd65n7Nh9GBx+t+Ew4Hdyufnhm2Xatxjb+/V6b49f8cNkDI4bmehgVDmhGjtZhUpiDaNSCNA3kY5X0ny9FscAAAAASUVORK5CYII=)|Clear Clipboard | Removes everything from the clipboard. |
| **Delay** |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAMDSURBVFiFtZdPSJNxGMc/z7vNxKEEweYyyT8IHirCCiHnRVA204MHERSSIkjDW4eO0bFDNyG7FEbz4sFD2jx5cXWpIDJMEA9B5ByIIk20be+vw7v5b+/ed27zCw/s/T3P8/1++f2e3/ZOlFKcRNuLT5clqV6D6shKFgRZUE65//Hx7V8nM5ppeSL1sHTiAKrD4MyGuQGRldKJW3M6zRYje/53/vLIVrAxMeE+py4WIxzf5094rWwksuefMzVmNgMH2Ai/B3qKMQDM4g325kqaHsERrBcpbsthbUDxvWh5Gw4bA6oEBqw5bI5A/wLsFCG/k+bICdNbcABfzy7RcAhhFD0J8TxHwu0DzQmKEL6e3cINAIh6CfIAzeli8yf8XrSuv9QOlbUACaPXGna3ALzdS4gMAEnquqCmLXdtTRvUdQEkERnA271UvAEAT2AGJYNAivoA+Fqza3ytUB8ASKFkEE9gJh/q/AwAVAemEYYBnYbuzDYbqKyFhm4AHWGY6sB0vrT5GwDwBEMIY4gGdZ2H63WdIBoIY3iCodNQns6AYWICWKWy1ph0zZnZjdV07lSwvwW5oDmhrPLwc6E0p+6IhUeAJuNB0gFAUzp3hgZi4SEU4wfPIkZkoBgnFh46GwPR+X4Uk8d69IQRR/kUk0Tn+0trIDbfh6gpwHGwtrkM+ztGbC4frXYgaorYfF8+1NYvJAAbH66CfAVcqBRsrkD0M2yvHa873wjVt+BCM4gDIAHqht23of34KhlFcBHfgB9vIBE3r9teM8Llhiv3wO11oWQUeGRFb70D67MVaI519GQV3yZgd8PWLwAVXrg+AppzBz3ls/pFtJkB7SZQxdZq/uJg1G6tAlSlOXIrWBKJXAPyfw84ikxPhqMwAxjNfwswkOnJcBRkAHxAcTuQ4cgB01sgz9D85ZE7wcbyFneZDusF/kvTy4j/k5bwWqQ3suefU0/Rs7TMbkH788hdBZOFqZpDYHjxif/tyXXTI1BKNZdS3IrT3IDL8QpkoXTysmBwZuM/IIj31SOcmiQAAAAASUVORK5CYII=)|Wait | Wait for a specified time in seconds |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAdiAAAHYgE4epnbAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAYZQTFRF////VVWAUGBwk7ricY+ts9LsVVtzsdPwsdPvsNXwkrriU11zsdPukLnisdPvstTwkbrhsdPuk63IsdTvkbrhkLjfnLnUrM/skbrhqczskbnghIybgYmYhI+fqczrYmx+iZy0mq7EjazLkLTYkbrhpMblEaCFEp+FE56EE56FFJ2EFZyEF5qDG5qFHKKNJriZJrmZJ7iZKJqIKJuJKLWYKZqIKrGWLqqTLrCWL5mKL6+WMIF9MKqaMaSQM358NZuMNnx7OXl6O3d6O5CIPnN5PoWDPq6jP3N5QYSDQoGCQ294Q6qpRnl+RqiZR2t3S3F7TGZ1Tml4U190U2F0VF5zVV9zVmJ3WmJyXLi3XWuDXa+7Y2lxa36Ma6qzbbDFbnJvcL7EcXmLfJu7gYBshqrOjcTZkLrgkYxpkbrhmb/iocjnpMXkpcnppsrqrMrmsKNktM7mttDoxtjn0OLw2N3g3MRe3ODj4ufp4urv5urs5uvu5u3w5+zt6Ozu6u7v7PDx8NNa89VaAjYoZAAAACZ0Uk5TAAYQGiIoKkVSVGBoaGpzh5epr7Cyv8LZ3+3x9PX19fj4+fv+/v72WgpIAAABOUlEQVQ4T4XT5zvDQADH8dij9ib2uFrh7K02rc1VURRFY9Zo7dH8526kEnI53xd58/s8WU8iSf/lEJYqSahStq/GgcHTl30yBe+PEX6fOng5QvwiJuALhXwi4I1qWtQrAEENFxSAAAEBAUDhWCxsLGtWgPx+Yx9v81iBqUkAmue5YIMeZ5wAAOcUB6wPuPHR0wJoExaw2g+hG620Ar2RP2CpF+Jm28k2uk3av3+oK8iIg4UuSOshYO7w9AJ3dd1UkqODaRivm55/V6U16JfYdEEjKhYZqGdgb8y0w84+DDrOKKhlYHnwV8NDiqIckP28ioIPXq+3qnr5LIu+ybubN/Ye+G0dq+rJDsIgkV8xuYeK5AS73ympkT5Fpt0uZbP3UGQL8hgos5nT80uraeWFuVyQkvVTGheY+wbSNPGqGcWrQgAAAABJRU5ErkJggg==)|Wait for Image | Wait for an image to appear on the screen. Image path needs to be specified |
|**Browser**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAATxSURBVFjDtZdtTFtVGMcbE3X6QZN98ZMfjNNs8wvGmC37MNqhQTOXTF5K14n0BQryIkPasbjgwGUONZlhY1GMQ7ZoFhbdBoUEJkszmAX6XjpeSim0pR3U8dJCX2/b+3junZ3QXe+9Bdfkn6bNPef/e577nOecwwEADis1NDzlKBfsc1YIm5C6HBVCM/r2z5QLIrYygddaKhgcL+FfHSvhS3Qy2fNs52V8YK4m/zlnufAUMltAAiZNlRXAveL88GhxXr9FdvjVLQE4K4X5rgqhk40xFYhRmptAIO1pA8yVf7TDVXFEtRnj9ZotPwIIAMzS3EWrLHcnKwDCHA32bNV8vSZkfDBJ8sJUEBt+OCoLX0EDXP+neVKoOEkIe0nB65QAtqr3n0UP3nsS5klZ0OswSfMeUAKc7ni31vapIPgkAYia0EtywSLjt20AqPvjnRflSu7yxbb3BtKZ0PWZBFzVRWlBWEsLQC/Owa0lBW8/Aqjt4n2BAAApYq7ju+kmmG86uYi5ZnU4Fp1FYxMAeByi3lVYGYjBpCKKmkCESSGdOBHUiS0kQMO1/GeQ8co/APBlR5aG0ryqENYG+s1oELYSjkHf9DJ8fXcOztxxwC/meVgKYogFC4P7UhyZAJ0wkwRWR4pgabjqBU5tz4H9SfOkbp/OMacCBDR/TiFzuDG5CHt+MsKui7oN2tuqgUt6D5Afz+UlOgDcUkwChPTi4xxFd2ZjKkDdTd60o1KYSJp7z5+xEeluNy08ZrxeO5uH4AeNi0DwgfX4DB1EUCuCkEE0wkGGqlQAQr9eOHg3CRBfWbI7fRF4s9VAC0Aoo0UNC2tRgOCUng4gbBBDQCvyEwBTVAAKtCqsNQKfq/rjOIoo2qLxMJqTWTg/DGfvzKB6iE7TAUQQAMpCAAFkLlEBEPruSvbg/Lf1BADIlDZWALtaNMC/aiKGxGG8ghYgoC0KERnA/gsAKW5r/2qemO3o9UmWAFo4dEX/sBgnjtEDaERhIgMeGgA4qzw8iqbCm9CSY/sKTvRNEe3Bw/QKUA1EiAzo6AAIhWMB97B7lRXA7mY1aN1+gIh7lEUR+jiKrsxWJoDfR8/9RWT089uz9NFfGIFPOseA7JCz33jpAALEMtSK1Rx5N+8gEwCh+377TBBLwIl+aog3UPEV3xiDGI4D7jeq2TSisF7UwGlQcbehOggyATTe+hC8ay47Ed6A0wenVA7IuzYO/GtjUNtrg5vjXrLu7A+0k9Gx0hBTK17TFOF+tXQ7uRkhg+tssqBQ8qB7/Pt5LB5ZhpQPqhPPZW39okqdO8y0F5BdUC/WPtoN5T28PWwANmYkB37Wnlz5cUi+XN/7Aflffc+BMZzBPD4qJdMfM4gzNxxI2BQjg3C7VmhljF6HoteJJh47ET2sBa5pswDn+rLVTOZRo4Rc+yGN+GXKQ6lCuf+19WeDNBTwmUWLTIWHOh8WMIoyaI/lih5uBtqIFtIB6FAdGqQzj5kJ86IYZi7ey+piUtPJ3YEmnmRjXtfNm4tZpBjlev+35a7GjOJ9aV3NZLq3npZ3c48Rh1U6gCE1X08dtZTY7XBUcAOgEm3b9OW0pjd7O2pUzVS7ZmNPlinVOIGWGerzUWQ8FDWId2/5dpxUdWfWS7VK7lG5ktemUGbaUVMKOnWFE6it3kemVswkNURNkt8iBkkZXcSp+hvVyR7B5rfKEAAAAABJRU5ErkJggg==)|Open Chrome browser | Opens the Chrome browser |
| ![](data:image/png;base64,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)|Browse to URL | Browse to a specific URL. Browser needs to be opened first |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAQOSURBVFiFvZdbTFxlFIW/fc4AA8jVGGwlQsMQoEUrCTZUW6ORay9EILWNpok+SOKDjbZRmthETeMz1Zroi40xMVW0qZRLaSnipZq21igBCqU2Ek0rpQ9cLIVh5pztA1hhOmdmwI7r4Tyctc5e6/+T8/97i6oSEYqLYybSXNWirEXUg+JB8KDEAqPANYTzYhmdPrd+nd5+ZjKSshIuwPgTRammGVtvwy6B+yJLyw0VfTslZqyR9kve5QV4S4zJ7x5+A2Q3cFeExoG4LCJ7kjrPNC8pwFhZcYqprsOgVcs0DkRHspVQQ3f3TCDhCnwxWV6Sa9quY4jm3yHzCdR+N5g5BOzAVGlJhqXai3DPHTIfEtuuTvrqx4tOgkU7YIkegvDmCldEGUR0EBUbEQ9oPrBqgeyEbc3uSO3+eTxUrVsBJsrWvSgqm0KJBbpR3Zfcde6HYPx42frHDbX3AEPJ6Vmv0dRkhVuMqCregxk53pasHmxJdNDdFNUdSV3nWsIVXCoMADN/tD5u+8VEifcHNVdlazTMAUSbMP1p/A6s1PE4vEdysa8nLBBQm9R19mg0zAEM627KgZUAkurFvXMAM28MAIVvo2kOYKhF5aI3sRZxNZdwrRu5JiIN0TQHEF8nzUB1EG7EVaorwhWoOTDzqahsX6b/9waQ7UAOLLNo5BDuNYCsoJxwIer+Ohcg+HWoc79oNKFgG8CwA/lgtAMAVx0DAIX/RwCXU4B+Oznp1c4NxSfLTp8PVUHQd8D40llhrwXZG/xb+sXfyWaF1oVEu72Cfb5Cexaje3BzR2m4ZYRCbaP3NPBoME7FKDLMMTqAKwA2QqM/lwbfA/gQQ9AnC1orti7XvK5x9hknc0HOHn055heDbWoBH93AxS7fQxyyVgUqP1ndXvHYUs2fapzZqNgHnXhb7Q9g/jacst0f1s4+cv0bO2gvkqTK8YL2ii2RmtcdmNlpIKdA0h0k4zHi/uxWgJTy6d/+VPf+EDUTUFoK2ipOFrRWrXcSrWmr3FjYUvfFlPvCx0CsczlpbHqFaQjoCQvaKptBg90LgRhGGEJ1aK4l0xyQ1cy3ZKImGaP1pE0EaapVDx/d7X5W5w/ART2h6eJ5y08PkBkmQDZKNkg5Asw9/vUQi5GM9/G6h8kYrUfU/Ifqdv3lfk4XnL63zQWFxyo9lmk3z6/oPyNheg2ZV/di+lP6XL64DU0NTCzkbzvv+6o7flUrvkTAcZpZCm7G9/NH5ps/SYxdFWgOIUYzQSSvvfx1URpY5mgmcFlFGgY2dRxx1IQbTnNOlaXEeo0XgJeA+yMxVhgX1f3mdOp7fduaZkOGjHQ8l8+fNvMSJ7eIrUVArggeBQ+KH+gD+sTQXkT7Ykyjt6f8xFQkdf8GbfON88yeJlUAAAAASUVORK5CYII=)|Google Search Links | Return a list of search results google returns when searching for search_text. |
|**Applications**|
| ![](data:image/png;base64,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)|Process Running | Checks if given process name (name) is currently running on the system. Returns True or False. |
| ![](data:image/png;base64,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)|List Running Processes | Returns a list with all names of unique processes currently running on the system. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAGFAAABhQFFWZ5CAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAjdQTFRF////AP////8AAICAQL+AzGYz/8xmK6qq1VVV20lJQL+f32BA379gOaqq41VV6NFdQKqVO7Gd605ON7ak3VVE8MNa5llNOq6iIabTQ7GbJ6fO68Ri7MZe5FtJ7cph78Va31hQPrKbPLSe4VpL8Mti4ldJ8MVfQLGc41VOPrOfO7GdQLOf7chb41lO5FdM78lc78VgPbOeP7KfPLWe7chgPbGg4lhL7slcPbKePrKe8MdePrOdPLKe41hMPrSf8Mhf4VhM8Mhe8MZdPrKdPrOe7shd4lZN7sZfJqXRPrSeJabSJqfS7sdf4lhM7shd4VdLPrKePLSf7sdd4lhL78he78de4lhMPrSePbKd4lZNPLOf41dMPbOf7she4ldNPbOd78dePLOf78ZfPrSd4lhMPrKe7sZd7sdePLSf4ldLPbSf78de4lhL7sdeJqbSPrOeJ6bRJqfR41ZN8MdeJabRPbOe7sheJqbQJabS4lhM78dePbOePrOe78dePbOe78dd4ldM4ldM78de4ldNPLOe4ldM78dePbOe7shePbOe78ZdPbOfPbSe4ldL78de41dM4lZM78deJqbRJqbSPbOf4lZN78ZePbOe8Mde4ldM78df41ZMPbOePbOePbOe78he78dePbOePbOePbOe78de4ldM78dePbOe4ldM78dePbOe4ldM8MdePbOePbOe4ldNPbOe4ldM78dePbOe4ldMPbOePbOe4ldM78deJqbRPbOe4ldM78de2NHQUwAAALl0Uk5TAAEBAgQFBQYGBwgICAkJCwwNDQ4PERQWFxcaGhscHR8gISIiIiMjJCQlJygqLi8vMDI1Nzg7PT0/QkRGTFFSU1RUVVZXWFlZXl9hZWlra3B0d3t9fX+DhIWFh4eKioyNk5SUlZeZmZqcnJ+jpqiurrKztLW4uLi6v8DAw8fJysrN0dHS09PT1Nja3d7f39/g4+Pk5ubm5ufn6Ojp7e7v7/Dx8vPz9PT19fX39/f4+fr7+/v8/P3+/v4kxybzAAABzUlEQVQYGW3BCV9MURgH4P8NEVPKVrJFCJF937KnQfYlZclSWdIQDSK7LIVuJNmXkH2M5bzn/XDuvefMMfObeR78N6Bw18n7f8Kdl6pXD0K83IPvpPGpegJipe0Jyxjh3SmIMu6qjHM9B0ZBp0zg4RRoaR0yoY4caMdkYpf7wJWPER9kYtvhGP06H1ukp7lkzhDEOUSn0e+elPLb+l5IIP0N0SIUSvljMSx/wLYDfgsLXrxUbgMriOhWb5yVJcgOCk8wGxWsTcZ+cmxEQXOKFRRa0PI1sbIODeR4lYlc+IXhRzkrx9FGrioAAWEEsJSVB+gm16/pgC0MG8NZeYtu8pwHbGHYGMnKZ7STMhu1wqjFKlaeoIGUvSgWRjH2sdKIA6Tc6YF6odUjuYmVCqwkbQey6oSnLguVrC1HxntSfi8BimpaW2uKgA2sfewPVJH2dWcqlKkh1ioB5H2niLubFg4dmAmcYy00Ho5SijEfyzhiK1x9r1GUE/C1sHYqCZ68p2R8GYPNrLUMhjbjGUWUYlgXK4+nwZh4k5S2dBxl5cYoREkt+0mutZj1l12hch9iTTrynOiilXSBHV2HxyJez3llM7Hm0ZUz2+Ymw/gHCcDUlYiUSq8AAAAASUVORK5CYII=)|Chrome Running | Returns True if Chrome is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAJPSURBVFiF5ZfBaxNBFMZ/06SNSWgSCYlWLaKEgqGtUQ9GBYMXPdSLIkYUBU89NEdB/Au8eKwiOXloESnipQj1JCikVakHoYJtaT2YYtK0SbRpmjYZD0sXw65Ns+xaxA8GHo+373188zGzI6SU7CTszRSLqyM2v3dPl0BGEEQERJD0IkhlkrHLphLYe+uVW7ocvUgiKIMiAV+wG6SrnhUAl4wMVwkE+t90CFlTBm2uXY4QNVqMNt42gWD/60EhxYDVg/5IAJOG5/LF5t0sGbNc4i0huLCzBMB6kzVCU+fAVui5/7VhzZnDTh7Hg3W5f0+BoYEwUkpuPvpcl/9076D5BISABzdCANwZnsHjtHMu7KNUqRoati0Cw4kwArg+OEU05OXaKWXPnr/LsvRzHYCF5YqmkWkeOHGondgRH4H2VuLRgJqPR4Ps2+1QCOS1BIxCo8B8tkxPp5vwATd9x/1s3tZ9x/xMfVtRCCyvaRoZ9YBGgfnsKgCJ8/txtdkYnykyMVvE2dbC7VgHAGkrFZjLlAE43eUFYGQiA0A05KHTr2xBWkcB0zwwly2rcalSZXQyx+hkrs75aR0TGoWOAqtq/PLjEitrVTW+clIx5ULeQg/8rsCz8YxubKkCiz/WGXr7nVabIDVdUPOp6QIv3i9S2ahRKG1oGhn1gO5JePfprCYnJSSefGk4pFmYdhua5oG/jf+cgGTMjpAPzfgz9vs8wsh3Qkqp/zCBEE0olEnGjBPQg97TTEI34NKrN52AbrHe4xSOgviQSZ69aDkBK/ALoL3X0FprEyAAAAAASUVORK5CYII=)|Word Running | Returns True if Word is running.  |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK3SURBVFiF5ZdbSFRRFIa/deZMMSMNRRcpsQKjJM05mV0eIqKo6AoFaYZRCdFDPVRUlGbSRFDRTSsiSrrQg0gXoqsS1psPOVJaVEZQUJAPQcRgZTirFx3IOQ7M8agPfU+bzdp7/ftn7X3OElVlMDGTCc7Pz/e8mfJhsmGoJSpWFCyBHIWG5lB4jasCgnuCKerz5IgalohaKmqRKdkG+FFBAemKFVjtJHlMQF5p3tgOM2pJ1LBU1BLEwmdOEjAQRQFUEu/kVIBVPuOcetgmKiDadaqBqwtTlW1ubPTt+4/kVSu1hhvJHSMsGVwBwKALSOodSMSKK8tj49y0XEKLDwNwsK6Mpi9NcfPdJOWAz+vj8qaLVBae7qveGLYOnFl3kpShKeys3k3kdyQ2X7ayBCs9yKsvr+PW3N/8wDZBzxP3xNaBgC/A9PEWJ/KP4fV4ASicVcDirEW0d7RTfjeUcNNkkJyy3Lj7mxpI5WpxFaOHjeJRSy23m+5wYcM5TMNk78391L95GreRf4Q/Nu5zDbT9aGNH9S7aO36ydNoSzhedxTRMrjfcsE3eF2wd6Gbe5LmcKjgBQGvbe4oubSSqUdvY+l3OhCW8BVZ6MDaeNCaDORmzHSVJRK8OLMicz/G1R+mMdlL/9hmLpi6kveMnW65t5d3X1rh4V2tgwsgJlK8qA6DiyVn23yrlYctj/EN8VBSeIjWQ6uSwttg6cLW4iuy0LOpeP6Hk9gEAvB4vletPM3NiHs2fWyi+suWfNa7WQOR3hOcfGzl870hs7k/nH/bU7CP8qYnIr4jdMkckvAXJ4GoNDCSuOdAv78BA8J8LUGpNEc678Wc8cnjAUeNgvDgU3u7tlHEqugyVEoUakFbA/qvjMtJbc2rbmqlkA367+JehsCMHehVgh31zqkFFGptD4RX9LqA/+As0xAKOOpJXugAAAABJRU5ErkJggg==)|Excel Running | Returns True if Excel is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAJSSURBVFiF5ZfPaxNBFMc/s7vZpD/QgBTbIuIhSA6lLtRY0OJF0B7EooKX3vWgBBsxxx7qTdRKo4f+AUJPQkou9VhapI3eewgIHhqlFmtIiKTJjgdrNNlJskmT9OD3tLPz5r3Pvpk3OyOklByljKas7wh9d4Czmo6FxAIsDUYlvPfH5K22Anx9LPo8eUYFWAgsARYnGdGhl3+SdvB4s5XgZYBvM2JILx58lYYlJJYXAgi0Vh27BtgLi1eG5D4AAujykjD4E/yQ2t3LNI8uWel4iutKcK3jAL7FIGZ8Gm17Q9nfcQCRTaOnEniXJjE25zsLoG1vYMan8S0GnZ3SxrM258hE2wCMzXm8S5PoqQQim1YbSRsjuVA5rpZD390EevDq37GZNKXUKoXlKDLjDOBZmwNpNwTVvnysaIvvD9SV3/eioHQgszvkn513QJj+Srv8ox8NYcDFFOQiJrmISf7lJUqf1hH9A5g3nrpy7kauf0b25ySFeJSeh+vogcsN7XueH69oy/4hft7bcth1bSOyB8eU710DaKdDmFO/U19KrToNRB1XQqMYCiu7Gk5B9WKU2R0Ky1GH3f7ErLoShMb+xCz28HhrAOXADcqweGEG+9RFjORCudTswTGKoXDN4K4AchHTLSP28DiFqTeu7aGLi7CWmjsT1lF12alUOnOFwu237gBKW+8OT+VCNbfiZlV64m7rrdaRr4H/HECyYiB43Y6T8Qn/MdHKOCGlVF5MgABNZMgfk60DqKS8msEI0NsVAKUUl1MB54AP/pi83nmADugXDe3JaeTa3qgAAAAASUVORK5CYII=)|Powerpoint Running | Returns True if Powerpoint is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAD+AAAA/gFPwqL+AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAUFQTFRF////AID/AKr/AID/AJn/AID/JJLbIIDfHI7jFYDqFInrEoDtEYjuEIDvD4fwDIbzDIvoF4voFoXpFYDqFYrqFIXrE4TsF4PoF4fpE4bsF4XoF4joFYfqFIfrE4fsF4boFojpFYjqFYjqE4fsFofpFYjqFIjrFofpFIjrFobpFojpFYfqFofpFYjqFIbrFIfrFIbrFobpFYfqFIfrFIjrFobpFofpFYbqFYfqFofpFYfqFYbqFYfqFIbrFIfrFojpFYfqFofpFYfqFYfqFYfqFYfqFYbqFIfrFIjrFofpFYfqFYfqFIfrFobpFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYjqFYfqFIfrFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqFYfqB9umyQAAAGp0Uk5TAAIDBAUGBwgJDA0ODxARFRYWFxgYGRshIigsLTEzNTc6PD5CRklNU1pdXmBob3BxcnR3fX6BgoOEjJCSlZaXmqCmqLK0tbq7vL3Fx8jJytHT1tfZ293e3+Dj5Obp7O7x8vT19vf4+vv9/sqCUaEAAAGISURBVBgZfcEJQ9JgAAbgl5UzL2yFoHgxsZlXSiTeigdgljQxlVQ0sIZ7//8PaOfXNzyeB6HkACQDSUSpa+1GFkK20V5TIcnUSLYXEVhsk6xlEOrZfKCn2A1Hd5Geh80eeKbrDFWTQLLKUH0aQLxIyXVv7zUlxThMyg4V5ZAyEzmbQmMWjtkGBTsHGHcM7GvwaPsM3BlwjJzRdWVAMK7oOhuBp79E2jt9kPTt2GSpH4HYytEUOkwdrcQgJHQ8oicg6DesDCNiuMIbHYEFi2RrWYGgLLdIWgtwde3SVx1FYLRK324XkDhmyFpV4VBXLYaOEzApOc0AmVNKTOQsSqx43KLEygHpEwp2QVEKNoWTNByxpRZ9zZmx+q+JmSZ9raUYfKkyXefpj/fkn7n0OV3lFP6bvyXLg+v0bLwtk7fzkKnvt/NahYGvWn77HSLM7+OTFxQuJ8e/lSDbYif7CyI+/GTEDx0d1Pw9hd+fXuGx1AEDe0N4mnFBRy2LZ70p/G1+fo2XDGmI+gcE+cSpR+i0owAAAABJRU5ErkJggg==)|Dropbox Running | Returns True if Dropbox is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAGFAAABhQFFWZ5CAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAjdQTFRF//////8A/6pVK4CqIJ+/34BA44455oBN64k7JJK27YBJII+/8Ic8KJS8JJK26opA64lF7IRC7YQ+8Is+6YdE6YpCI5W/7IZA7Ik+7YhB7otD6oc+7IlChJKAIpK8IZS8JJW97YhB64hB7Ic/7IlB64hB7IhAI5S8I5W97IdA64g/64dB64dAIpO8IpS9JJS8I5O97IhAJJS8I5O97YhB7YlA64dA64g/7IhAvotb7IlA7Ig/7IhA7Ig/7YlB64lAy4tU7IhA7Ic/7IhAI5O97YdAI5S87Ig/54lD7IlA7IhA7IhA7IhA64hBI5S85IhF7IhA7IhA7Yg/64dA64lB64dA7Ig/6ohBLJO2JJS8pYxsI5S864hA7IhA7IhAI5S86ohB64lB7IlB7IhB7IhAI5S87IhA7IlBI5S87IhB54lDI5S8JZS7JpS6J5S6KJS5KZS4LJO3LpO1L5O1MJO0MZOzMpOzNJOxNJOyOJOvOpOuO5OtPZKsP5KqQZKqRpKnTZKiTpGhVZGdV5GcXpCYX5CXYZCWZ5CSb4+Nc4+Keo+Ge4+GgI6Dgo6Cho5/iY59jI57jY56jY57j455kY14lY12mI10mY1znI1yn41woI1vooxupIxsqIxqq4xorYxnsYxksotktItjtotivYtdv4tcw4pZyopVzIpUz4pS0IpR0opQ04pQ1IlP1YlO2IlM2YlM24lK24lL3YlJ3olJ4IlH4YlH44lG5ohE54hD6IhC6ohB7IhAnHmEdAAAAGt0Uk5TAAEDBggICQoNDg4QERMVGBobHSEiIyQoKSsuMTY4REVGR0tRUlpcX2BgZWZob3BydHh5e35/gIGDhoiJo6WmqKursbLAwsPFxsbL0tTV1tbW2t3i4uTl6Ozt7e7u7/D2+Pj4+fv8/Pz9/f4/cRJLAAABsklEQVQYGW3Bh0OMYRwH8O+dkb2SPVNky6ouZIVCRdlbVn7VOaKMEIpIJUoRmVmJznbfP87zvveOp3OfD3TDpiUtWTxr6lBENXjhhlNiOr5+/kDoPAD6LtojtpLKa7sX9IHDmwKMyRHdza7g3smwzTngnbJPRMob6v0SVt1Gnl49BGGbmXZIzsitYEeJWMrqv5PMHQTTQYbaP/APeV1cgUckN/WDEkPLj4Do7pNMhxJH29vzomsiD48C4KPjy5NacV0mmQGMP0ZNi7ia35P7PUinprlUXJ1U4pBJ113RtVNZini6HouugUo2kmn5++rzG9FcaKGShyxaWkXOiqbxJZWd2ELLx4vSS1cPle1YQ9unKyJSeadKwr7SsBGpdPxsa+wk+VRM32hYgURG6KgTxV8RomE2Youo664RQ+BhLU0jgJW0BVsf3CgWg//1s24a1gEYW0Tbi0tiKn7O3zQUjoayio5f966Wyrnb72hJhWHcUWpCPXQUxMA04ySjS4BlLqM5MhOOeYX8z65J0EzcxgjZI9HLgOU7qNma3B+RvPFrT9CU75uA6IYnpvh8y6Z7oPkHHsPKXk8cBH8AAAAASUVORK5CYII=)|Firefox Running | Returns True is Firefox is running. |
| ![](data:image/png;base64,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)|Teamviewer Running | Returns True is Teamviewer is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAEbAAABGwGN907lAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAVNQTFRF////AP//AKr/AJn/AKr/AJ//ALPmAKrqAKTtAKruAKXwAKbyAKrzAKb0AKr0AKf2AKruAK3vAKfvAK3wAKjyAKjzAKrzAKzzAKjzAKz0AKj0AKrwAKjxAKrxAKzxAKjxAKryAKvyAKvzAKrzAKn0AKrwAKnxAKnyAKvyAKnyAKryAKnzAKnzAKvzAKrxAKnxAKnyAKnzAKnxAKvxAKnxAKryAKvyAKrzAKvzAKrxAKvxAKnyAKryAKvyAKryAKrzAKvxAKnxAKnyAKryAKryAKnyAKnzAKnxAKryAKryAKryAKryAKryAKryAKryAKrzAKryAKryAKryAKryAKrzAKrzAKrxAKryAKryAKryAKryAKryAKryAKryAKryAKryAKryAKryAKrzAKryAKryAKryAKryAKryAKrzAKryAKryAKryAKryAKryAKryAKryAKryzXR4aAAAAHB0Uk5TAAEDBQYICgwODxEUFRcYHR4fICImKSorLC4vMzU2Nzg8PUBCREVKTU9QUVNWWFpcYmhucHF1eX5/gYKGh4iKkJSVmJmcoaSnqq6vsrO0t7nAwcTFzM3O0dPW19jZ2tvc3uDh4+fr7/H19/j6+/z9/suB3zgAAAF/SURBVBgZrcFdWxJRGAXQLY3SF5KYmCWhlZJZllZoSfldkYIB1ViUFYJCzeT+/1e+75wz4DwPl66FCxLPpJyhxMRCodRoueV8GlFzNY9Rbg49zhb7qCQRWmXEPxrNLIyMz5C38/zB8MDow7UORSeLwDpDh5OwbnygaCahDmj9iKNnjaIC1ab1FOdtUuQg6jTaMQCj76qfXw5D3KFwIYo0DiG+UvivAdyjSgOYpuHFATz5TbU/+ahOlYeo0piFur1c89hVhliiUYrBuPLiiJYLMULrfQzWpU0aLagWrW/PHBgD2zRGIFx2nXxcvA41+JeBJYgy1emX3VMKf38e4hMDVYg81RvgboPKHwPwisY0gDRVCkBi5z/J75cBbNAoQrgUj6Guzkxdg/pFow6Rozi6hXNu0mpDVSiO76Nr7CetA6hkk6o4jkBs/oShdQSyHQb+7BVW3haP2eVnYGSb7GsVoWSFfWw56Mm5jPJqc4hK58tuq1EqLEwkhpxUJo6LcQbYjd5sezi/RQAAAABJRU5ErkJggg==)|Skype Running | Returns True is Skype is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAP8SURBVFiFxZddaJtVGMd/z2myrG3iytq6XXQlaazWC3FzVWxXv5gUkXpZh+iwiMy2rih6NSd4N0pBKJTFtuImKIOpF4plTBAmOoWCgzFXUPqRbE7RrtV1Sbqszfs+XqTp0uRNm3UN/iGQ9/Cc5/97z8dzziuqSqG6JxRttow8YOB+VRpAG0DuBq4Al1TlsoiOlumNExe7q2OF5JRCAIJH43vVcAT0kQJZo6KcwJajkwfLf1k3QHBovlHV7kXZW6BxtixFD0e6fH0KjkZ5AQKh+DMi+hWwaZ3mt0zgS5NceHm8Z+v1ggACg7EnRTkFlN6peYbOa6m3KdxBIrPRZEf5h6JNony9weYAO818rD+7ccUIBD5msyRi4yg1Dglugl4QMWNqM2aLjJWY5IRYUm1Bi4i8AOxcE0PYN9Xp/cwRIPhB/C1F38/qMqdIqES0f6LTO904jPvnAyzm5kX8odjzIhwDylZBmNvkSez49ZWqKGRMQcOxGZ+ihzIC/xXRQyXJhdpwV/k7k5Xe2UAo/sasHdvjlFVBw93ek0a0FbBWAdiyuOBpTz8sAywmNr8NVC09nldJPjTZ6esd79l63T84vyswExtF9PFwp/e7VZIz0en7EfhitRhV6cgBUGH/0r9PFxPe5nBnRQQgGJp/2Kj9PbDbqOldLfGyjHy0RsRj9cNzQQAXQP3AjRpc1AFHprp8h9NRwaPRe9XIKcALXJ26WnauEH9bZcY4151lWUnXHmDSBWC77SdQToa7vO+mAwL91yrE4/4GdGlaZNS/7VptYHBtAMG1Ze0o3QFLI6Bql2qpryOzXIqnpBvUn9GhTdTVtnbiwiSS2uougHCV77i231q59QN4cEnPRpk5SZEaWFqEmeYAliu6H9heTID01OaU4pTk6eKaA4jkB1Bqiw+QksupUYTa7E2kMGmEkY0ytpUIOBzHjcO4/7FiCXJGR0anusof3SiAtHKm4NwBkrDyzE5J76sfwFN0gFQt0DGH2ArbHX2x6AApCHPRsV2lzz8UbSo6gMH+IU98pbHl27pQ9LnbNQoORtvqQrGfAqH4ivrieCdMLcT4b6CBPPksgc8RGblp2aevvO6bzQ6oH8CjJdHdNqYZ0ZeABwFwy/apV8v/XhUAIBCKdojI8QJezgYuADEgmfqJD3QXTjfqLADHOgAQqfZ9EpiJvblMnl+GnLtg/qNYF5Dszs6B7VhJyzwLElkD4I6UFwDg8sGyP8VYrcD0/wIAMPnaXeOW4Sng7Ab4/cXC4ooiV9DHaVqBUGyfCH1wW4eVraqnET70T/tGzrxHct0AkNpetom3UEKrrdoCbBOoJPUl9YdCBOQSaERUIgZzZqK79Pd8+f4DwVuK+TWw7IgAAAAASUVORK5CYII=)|Edge Running | Returns True is Microsoft Edge is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAMkSURBVFiF7ZdLaFxVGMd/38nNJFEsWhBfYMFNxFeFoCK2iFilYsFSMhUlbSJ1oQhRCBLaZOZ2Oi2KFaF05cIHYyuYa6uIYkGxpdCFGyFUmaRYoQ+hFKGaxskknTl/F96WdB5hEifERf+ry/0e/x+He879jkliKeWW1P0awP8BIFhooQ1+dQNtxefcmZNrUbnoPXmMUaY6D2skWW64z3x3gWWOBJTP70LWD7Tb6bHKlLy8bdMnw182BcC2fnoTQWIl+HvBPPAisOpKvBoAAMmGlRvetWAA6/+2jWWTgxhbgfY69SU7e2IC7x1wYzUELymX+njeAJaJEpT4AXisRo1H5EBfU7Lv9XbyLwDbkrkd3/KAeQ0Aa+Lcc5ryKzQSztQDqP0RXrI9mKrNxW84bVZ247EYdLn17ngCs/MU7hnTSPIQcMh6d64z9CqwgvaWdcDBhlfAhg7ehiufpXqLjhKwSmFy0tLR48AgYo2dHmuN4wXgsEruNe0fOlXPsFLVK+BKG8AqzS9S9huVfX7SUtHrwLs1aq8DnrXAr7a+ndvxuoA4ifyo9oUT9QCurIClP3sIuTeA9XGz2Wn9ynbvtVTUDURXRersglmaNrHbd/i39H5YqAlg6ZEeZB8AiRoNygSlWylcP01iOg/cMU+AOJHvVLj7mcpDylkq6pzDHMQRhS/8QaL4ZKX5vCSeomN8W+VrBxbWNYdfaOWV+Pn+BZvHMvSyGVYBoIfrZB+gWHxEYfJXS3++GmzDfwUA7nS9O3bblsxdswC4uUbiKVr+7mFiasZSUQ7pKPBgEwCQbMBKLm+bs32XAY5XZ9mQwr4ityzfDmxqhnGFEmZ8aL3ZRx3oQFW4NfjGMvuXIQ0sgvllmUHoCPJ7gGOzAr8rXP8nl9ruA9oWEQCgyykMPQFrwfbFL0sAOE0vsjlA0QEoTE4q272Jsu8EsgC0cJx/z/fFk/hxzoHEUtGbwDtz9Wj4JKzWjOS75h5Kx3kPtBdo9u3lgqQe5cKfG5oJLR11IXs6Hsuu+gvamfEOE1ON+eqiN/sJK3+hj8JzsIChtNla8nvBNYAlB/gHWcJGuLAG05AAAAAASUVORK5CYII=)|Onedrive Running | Returns True is Onedrive is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAiEAAAIhAENVwL6AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAPZQTFRF////aFEXbEsSbU0TbksTbUwUbUwTbUwTbkwTbk0TcE4UcU8UdFIUdlMVeFQVelYVe1cWflkWglwXg10XhF4XhV8XiGEYimIYimMYi2MZjGQZjWUZkWgak2oalWsalmwbl20bmm8bnHAcnXEco3YdpHcdpXcdqnserX4frn4fr38fsIAfsoIgtYMgtoQgtoUhuYchvosiwo4jw44jw48jxI8jx5Ikz5gl1p4m2J8n2qEn26En3KIo3aIo4aYo46cp5qop6awq6q0q660q7a8r7rAr77Er8bIr8rMs+Lct+Lgt+bgt+bkt/Lot/bsu/bwu/r0u/70uBe2RrwAAAAd0Uk5TABZVhbrr7HZg8t4AAAEASURBVDjLhdNXU8MwEATgdd3QIfQWqsGEHkro4FBCDez//zM82DCeiWTt083pe5A0dwDgBWHMvsRh4AEA4Ee0JPIBwGdFfMCLqkDkIWBlAoTVIETp/uOL9aKaa/y/BSV9rqyoOh8Df80SqHWlybxc2qABzOtTzb5LlMCB9nRTBe56Iw/foyTJ1TUDGPu54pE2SZLZqwFsqckFte2grSnWuu9DNjD49kjyTCs2sKzbJElOdWIDx8rzYgOd3k6apmmmWTOo65okua9DM0i1S5Kc0b0ZXGo6L541YQLDX09Fo6VtE1hXq2g0dGH5SUsQV5/H7qF1jr1zcZyr515ex/r/Ak3GNhQFU55qAAAAAElFTkSuQmCC)|Illustrator Running | Returns True is Illustrator is running. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAUWSURBVFiFzVdrbBRVFP7undc+utvFrbu8i8q2lmytPEK2YCItAVISJTHR1KipMUZi1CiYgEGFBBOjif4A/xjhj0aURDE2ShBMWkMkNsGI6Lo8WqWopbRY2W63szuzO/f6g+7szs7ADiYmfr/mnHvmnG/unHvuOYRzDjeIDcWUAAt1EkY3AWgBMAfAnKGfFvqpwIqCwFRRNkZERT+Y09N7JroGMm78kloEEslEVBf4LkLwKIBA9fr5U4ts71CBca9fS9VJWvfQ+qPJf0UgnorLHuLbzgnZBqDueg6cCFQSqQuo/QWvuml8TX/W0cZJmUgmojKt6+OE7L5R8FpgBiWZdF0nmwyNLD62Ie6KwIqzq1oLEj9JwFfXCuAnQcz2RmoS0VQ5OJEJ/Liov+uB6jXLL0gkE9GCxE+CY0Etp8vlTjzu24GMJuLo5WPY/9tHNYmIkmGEg1N3V+aFuQPxVFzWRRxyExwA1indkIgCAFgbXePmFRQLgpDO+U5Evukwf6tJwEN8291sewlBOst8Fono9jVoqhyUcr5eC4FEMhGdyXYLfKQO9yj3IULnuw5QwtJZcWxp3oyIEratZad8HaWkFAFAF/guUpXtUWEBXgrsg5f4keWT2DnZDZU7niQbIkoYO1peBECwKtyO18+8hVNXy+WAGZRkC8pBAHEaG4opM0XGgvs9T8JL/ACAOlKPecIdbj8eK8PLABBTfmbxEzab3LSyJHwkEaQBFupEVYVbKDRhmdxhyirPYtg445pA//gJi1wv3YJ7I+0WHTMo8cqh5+lMbbdgg+cRkIovOJY/gALXXROYLqr4JWOtwI81PmizK2pyN8W1i8WCBWJT2RnPoE/71HXwEt4+9y6Aco0JSvV2Arowj+LarWZChIQGOteU/zAGofP8TROYKmSRZ6opEwjwCB6LjWFQn41ARJgPWlGhLxsXbzp4CX/raYvcFrJuNjOoaLsLDBQtsgjJ0fmFYsp8niykHW1EYnWvs4LdBsAogFhJMW78iTyfhmfmCDaKdzo6/zz3HgBgVqEVewf3OdqE5QaLfPpqyiJTgRVtBDg4fjfOo0lcCgCYK9wGici2U3CFjWDf9K7r9gN+0QeBlHdPYyoYmMVGEJhKAdgO+MXiubIRRKxTHnYMciNsb3nWIo/lx202omyMUE5Zb/VCsvCdRd7o7cFc4XbXwdvDy9ESWGLRHb8yYCeg6AfpFE33AZiqXDhX/AHfal+UDSHhKf9uVyTaw8vxQvPTFt24Noreka8sOiowntPTe+jg4kGNc3xY7eiT3Dv4i42a8myhETuC+7HR0wOJyLbAftGH3a3bsLX5OVCUr2cOhld+fsNm7/VrqYmugQzhnF/rhEQ+hKobMSa2YWtgL0hV52agiEvGBVwsnkU4vxRhucGScJV4f/gAvrz0te3rbw1l7hpafzRptmQrzqx8daYJtSAmtqHH/zIa6JzqJQDARN5w1HMwfDD8sS04AARD2b6RrsNrgYqOKM/VNznIiWrjweJpvJbpseRELYxro9j8/RbH4IpPzxS8qnkB3lRT2iwuQ1xqR6PYjIVCEzzEb+6AxnIYy4/h+JUBW8KV4NSU2gaTFWdXtXJiHK7VnBIQRIT5yP7ahtNXU7Yi4xS8Pjz90HDHkc8sfpwmo0QyEdVFHHLTpN5oMipB8emZkFdd7TSmOU5GA/GBMZ1lOwnnOwG4awQdQAXGg6FsH61Pz7vejPj/HU6r8V+N5/8AlNIVFq+Rn+gAAAAASUVORK5CYII=)|Launch Process | Launches a process based on the executable |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAASeSURBVFiFzVdLbFRVGP7OuY9O78yQybR2OrSUV0vjMG2RBUzalXXBIyFsKjSVEkOCcUO6QlZqYgzBYDCNGyPRaClQsRixKq7qqoQgC2NIjdA0pdiO0jt1ntdh7uO4mM7jzr1t7zQh8VvNf87//98395zzn/8Qxhgcoa2tBj5fLyg9CuBFAEEAQeX+fTcEQaM8rxBBWCCiOCZq2jBisaSTtGRdAZFIAIy9C+AEAG/ldObePWtSjmPU652mXm+/OD//YGMCwmERknQOhLwFwLNaAjsBxeSUMurz/eziuKN4+jRt50NtIyORADyeSRDy3lrk64EZBtGXl3uzirKQa2kJ24q0fIHu7g7o+g8AtqyVXG1vBxMExA2AKBlIN75aUwwRBJ2vrz8mLi5+s7qA/Hr/sh45ACxdvgy9oQGynADHDLR0htYLyYtobNxTvi9KSxAOiwBuOiHfKJiqcsby8hQaGorLWhIgSefAWM/zIi9Az2Q2ZXX9lllAJBJY2e0m5EIhpI8f3zBZbGQUymsnLONGPP5yYVPyALByzk27nYkiEmfOQN+8GaAUnuvXqyKXR68h1bUXma6XsOX7CZBEopTbMIiRSo0BCFO0tdUgX2RMSA8O5skBpPv7oRw+7Jj8n+GPkeraCwDQKQf5ixGLj5FKhVBXt4nC5+tFRYVTd+1C5siR0oCuQ5yediyg9vaPJjvd2o5/Xz1mGmO6TnI8P0RXarsJ2Z4egJCi7RkfBz8351iA66fb8P72q1lE/4DFj+Vy/RT5i8UEtbW1+JtoGtzj447JC6h78w2TnWu2nm6mqk0U+VutBEKg7thRNPnHj0FyuaoFkFQSglqKUyU3QM2V39A0ySJACwbBJKloCzMzVZMXY/+KFn8zAM+6K8qMqvL8RpO/cPo0AMC7xm3oBBRAtHyAj0ZBFKVol++HaqE2lj4uAVBzZ8rsIAiaRQAYgzA7WzS1rVvBRLFqcubdBFUoxQlKBjAMkw/leYUC+L0yuHzdGc8j09dXtYDYJ5+abPHPJxYfIggLFIZxq3LCNTUFlF3T6b4+aNu2OSbPHjyEVOce05hn7JpVgCiOUcTjkwBS5RPCw4dwT0yUBjgO8bNnHYnIHjyEpQsXzeQzf6D26xtmco5joqYNUzx69AzAaGUiz5Ur4BYXi7bW3Az50iWkBwZMx7QAvbER8tUxRC9+BI0rHS7O0FH/+kmLP/V6pxGLJfMdUb4TmkHFjZgLhbB8/rypLAMAGAMXjUKYnYVcH4Dqr4NOOdsvErjwPqSr5v9HKGV8U1OnOD//oNSS7dv39koTakJu924khoagBwK2BLKcsB3nmIH6Dz+ANPKldc7vn3TFYq8A5T1hOCzC45m064qYy4XUqVNQDhxwJEB6Mof6k4Pg5CUrududdElSU6FNr6opzXV0ILt/P7SdO6Fu3w5WWwtZToAAELIKhIUFuL/7Fu7PP7MLt21KN9yWgxBowSCScixf4SqKjC35um15AZFIAMBNJ03qWi+jAji3O0n9/h67Z5r9y+ju3b+RTveCsXcA2D6pnIBQyji/f9IlSU2rvRH/x4/TSjyn5/l/iVjk5sAr/CUAAAAASUVORK5CYII=)|Kill Process | Kills a process |
|**Control Flow**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAM0SURBVFiFxZdNaFRXFMd/5+ZN3ozRLFI/uvBroWuJoqDVSWqiVLC0GLQgShErgiAURGlRTFRcFUHoqqiItAgiKS0WBDVqxjRZxeBObBf1Y1FFszAmMy8z804X8U0y5r75eDPQ/+7d8/H/v3sO594rqkok9McvAPNp9PazXkejJQGJLCAVDwJHiHmdUUWYaOxFaCXr3mFIWv4vATWJKF+Cu4llOLoToQNlKbAYaA7xrroc4QIGGlfhm3NAR6XJSopIxQ8CK3jpfcdOzQfLzqzwYYkx4Z5DzSGgoUpygFZybi/w6TR5ogfoBmChq8CxwFTcA7ekiXH3D5TDEclnI5XoAe0ufAtHeeB2FT4LJbgvDg3uPZSNNVJOlyCV2A960eIzhq/raPceT++AxE/WlRwA/+MQv3kYcwqCHehvXIuYIUK3XUZBfwEdhIZBkhPPZwyiEHKm+mncvQ20WZK+w/cWTDWhmOMlyIfJ0cXmzNOQv7GTA6zRLH3NXcSyT0A/nBFzEXeLIRVfCXwekvh3xjOfsDldPXmAjrdvQH+2h+oOA/oV9omYxZdv2aaePZaLKL9VNHjEv2pflzYHZHVI2GXa0/+EJm3LHChJOhN5mQgZ+nEDtNqjzJWKCcrBaMxu0EYDOs9uzKXrJgAnYV+XMQMyabX5kq2fAP/rEMOIA2SspgadUzbvkLQw6V4CXof2xP3Ecgz77An0oUG1324zu8uSZ907CF8ifGP1uSkuRs8Dth7wQa4ZkF/tDLKXvuaPSpKHNjBT94im+J/AFyEeN0hm/nJQ7zbivgPmFtu1hdhkL8OyhTU63Q+lyFNzlkB+A8gGHNljmX4B8qh/FoKzIJW4BrrL7qsnSHpnK/7zSqByhrb0SQgmoO93A2N2b/NvXcmFATRzupAdgHbvMaKWTpVTJNOXAN7fcmojh1ukvc9o11yxAIBNXi/KDx+Q99RIGCCP8CNN3na26vhMQ/Gd8JX3PYtcAf4mmf6pyOZ4XRFL0Ifxj7Bx8pHNWN3LqHwfvAVeIDxD6SMn18sc5RGeZmEikhmpLtEUqn8ZrddRYl4nMBKFsHYBdRYx+2FSjYgh6SwcRhHxH4JZSGO+f4eQAAAAAElFTkSuQmCC)|For Loop | Perform a for-looping operation |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK7SURBVFiF7ZZLaBNBGMf/s9lsstk8GqT1QVFqa9G2ClqQFhF7LCh4EQUf0EsPBQXBg2lAUqHgsSIiWooePHhSQQ/VS0F6qUoo4gONbaRK+gKbpOnm0XT38yCb2MalszHFS7/TfI/9z2+/ndkZRkTgtUAgdBIQLgHUyoAqAPgWnQQACIJAdkmK2yX7vaGhO0FeTcYLEAz03SAgsDZuAPxpLkUZu//gbjuPrsBT1Nt7vYPArq6NMwIEvbQ+rapt3d0XL/NoizxFRDjPQMzw/ck8jo/8RN33DCLZeWhOCY/bPIhW2wrPrCznewDcXE+bqwMAHTRGSlpDz8MY9k6ocCzr0EFg2RzOvFrA1sViOzRtpZZHmQuAgSnG+NhYHK6MVlKjkY5Tb9SCr+s6V3c5O1C02pmcac6zlLcqZx0g7bKZ5jSbZTnrAB8bFdPc5A7nxgOMN3sQ3u8tiec8Mp60WgfgWihr7WlnNd41uVE/lQGLLOFTrYTRPVI5UuUBAEB0p4wPDTZ8bXbAm7CXK1MewLQ/gRcH3mPemwLmqmBjOg6FvdgdMV8fFQNIKGk8an+NvK34L9BIwNvWFNwpETUzDkt6lhfhWH101eQFI4bw4YRVOesAc75F01xa/svJVGkAX8Z8q0l5Zpr7R4DipaHlh/kZUxeVNwiAYcIYNszV4OiXRgi0+m1r4gJaxn0FXxTFOI801y5gxEYJdMLwj0Qa0BTbjqktC/iszWLXpAvbpld/GlEUwxUDcMi4lc2wLoD2GTG/qsCvKvBFl0vq7aI95/E5z/Foc32CUCiUJaATwMi6sA5n3KO4OwYGBrj2JPelFAAYYywY7GtOJdWubC59BQCSyeTviSVHWFbk/sHB28+IiHs/WgIw7OzpC506MAwAsVgMAOB2K9eGXz7vt6pl/QZRYdsE2ATYBPjvAL8AOIXef+sqD0EAAAAASUVORK5CYII=)|Condition | If a condition is true, run the indented code |
|**Message Box**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAblQTFRF////AAAAAAAAAAAAAAAAAAAAAAAAA6ysAAAAAAICAAQEAo2LCgoKDAwMDg4ODhAQACoqABcXAAkJAAwM9GsvDAUBDAYEAAgIAAsLAAsLAAYGAAkJCwsLCQoKAnV0/m4uABgYACQkBQUFBgYGBwIBBwMCBgcHFBgYBwQCBwUEExgYExgYR0dHVVVVAAEBAAICAoqJAwQEExgYExkZVVVVFBkZISEhFBoaEBgXFBoaFBsbHSEhjqOjqamp/mwtAAAAAVJRAXp5AltaAl9eAmxrAn18AoSDAoaFAoeGAoqJAouKAoyLAo2MAo6NApGQApKRApSUAqGgAqmoAqyrA2loA2ppBAQDBQQCBwgGBwkICAsJCAwKCQwKCQ0LCgsJCg0KCg4MCwwJDiEdDiMgFBsbLS0tSktLUlNTWlpaZCYLZDQeeoqJjY6Ojo6Oj4+PoVMwoz4So0EXo0cfo04oo1QypEcdpFUyqKioqampxsbGx8fH0Gs/0l8u0mxA1NTU1tbW2V0m2XBC3Nzc31MX33NE4Pj45lYY5ndG62Ak63lH7HpI9n9L+oFM/m0t/nI1/n1E/oJL/oNN////QOoNSgAAAD90Uk5TAAYQERYzOFBcdnZ9l5e4vMLFzc3Z2trf3+Lm5ujp7e3z8/b29/f4+Pn5+fr6+vv7+/v7+/v8/P3+/v7+/v7+/lINWQAAAUJJREFUOI1jYEAAMXsoEGXADlRbukFApFkFl4L2iSAg30ZAgR0hBb14FDRO7Oqa2IBHQVlPdXVPKSVWYFfAyCEsAQSC7JowBRrsghISkuJCHIxgBVyKjh5AEBAcCVMQERzg7u7u6qDACVYg7RsMBKHJyWGdYAV9HeFJSSFAITdnKbAC/UCQAt/orNqJUFCTGQXS5Omih6Qg2DehBCrfXxAPNhRNQbAPVMWEwnifYGwKgr1jwSqKYryDsSuAqCiGyWNRAFKRHweTx6Yg2Cs20SsYn4Jgf/9g/AqQAfUUCAThUGAAVcDthwPIOYEVsKqpa2lrGxmbmptbpaAASwtDNgYGJhnbSbhAq40sMwOfWR5OkJNtzc9gb5KBDFJTkXnpafYMylVNyCA3F5lXWa7EwKtbVY8L1FXo8DCw8Crb4wRKPCwA8AQNnzJzUC4AAAAASUVORK5CYII=)|User input message box | Shows a pop-up message asking for user for input |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAPZQTFRF////JLbbIL/fILXVKbjWKLXSJrbSJbjTJbbTJbfTJbjTJbjSJbbTJbfTJbfTJbfTJbfTJbfTJrfTJ7jTKLjULLnULbrVLrrVMLvVMrvWNr3WOr7XO77XPL/YP7/YRMHZR8LaSMPaS8PbU8bcVcfdWcjeW8neXcneXcreY8vfY8zgZczgac3hb8/idNHjetPkgdXmg9bmitjnjNnokdvpldzqmN3qmd3qmt7rnt/sqeLuquPutObwuOjxu+nxvOnyvuryx+z00O/20fD20/D21fH31/L33fT44fX55Pb68Pr88/v99fz9+v3+/P7+/f7//v//////MZEFEQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAABO0lEQVQ4y4VTV1vCUAxNS+migwDujRNRcSPiHihOzv//Mz4gvUn5lPPU5KRJbnJClMFygzBK0ygMXIvG4fgJZ0h8J0fbXpkVyp4t+UKJx1AqGL4YC6LSOJhiZua4mP0veb4ETodf8W8OW+Wf/gC6oyrDPjxVutLH9/rI8IiInFz/9bNV8xaHiHz+Bz6RlSjP0tF9tyYmZpEr6WpnAGBbeFwKhDVzAwCDeeEKKDTGwlP/+AroyZwhRcZo7VW5B3RkQESp6nERQFM60lxAC/ia1QGRCrgGHlmXCKVZewcuWDcpn8lbAHZVQKAH1c63wK4e9TPwoPjEUsuqfQLt/LLkutcANKrNu7patxDMPoDz17cdVoIRkjsBgJcVI2w7J9oNYHA7l/FxYUz2m4fLpkEj+8mHM/n0Jh/v3+f/AxHgSjy/wBsUAAAAAElFTkSuQmCC)|Display Info Box | Shows an info pop-up message with title and body |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAASbSURBVFiFxZdtTJVlGMd/1/2cl+cgHOSgCKjTlGFEFDrUGAIBQ8DICeopRXHK8syXWetbH3RuuvVFp261am2t1Rc3+yK51cS5UEcvY9ZW0idbrJjhS04BhfN29eEArgx4Dtj6f7xf/tfvvq77fp77FlXl/5RruhM3bg/laDTccOtmX0Qi5sKlS1/emI6PJJuB9aFQimcw8plCA0D/jd8THcoXw2n2pu729gf/GUAwGPTF3KnngOq56bBqmZDlvc+ZzkGu98cALsaHBxu7uroeOvVMqgRRz6xDolQ/lS0c3m5ItQFm0/BCKvuO/8FPfbFq4007BLzl1NNxBja1tC1RtMcyeE+ELObP+Xv/3b4hmt6+TTTOiFj6zOWOjl+c+BqnpKp6DPA2rJTHggNkZKfwymoPgFejcsypryOA5q27qhGa/CkQrJhgiiW01ftJ9wkITWU1ddVPBCAYDFpGOAmwpcowy060D4fh9FdxPmi/x8ORRBk9gRT2vOgdNdaTwWDQmjFA3J26W6Fo8TyhdrmMt3dcVc5cVk5ffMDZKwOJRkt4qSyNvCyDKkV9d+7unhFAY0tLhsIRgF11gjyKz683E6s2xuJ6X2S8XdJ9vLk2kSZROVJe3pgxbQAb72Egs7RAKFwkkw19JEt4rmAWVctcAJm4w4enBdD86msFCnvdLthR6/iwJOS32V9j43GBwt7SytqCpAHEip0AXBtKhbnpycXHMsyb72PrKg+Ay2XJiaQAmrftagTqMv3QVJbk6sfkt9lW6iUrTVCoK6+qa3QEEAqF3KJyHGB7jcHrnl58LIMdsNlTmTiWKnq8pKTkMbfHAG4PRQ+A5i9bIJQ/63DjTSS/TW2hm6L5FkC+Ly1wYFKA5tbWLFQPCtBWP8PgAJYBv83rNV4EQDhYVleXNSGAibqPAulVxcLSnMkBvGP/UVVszyRj/TZP51isK3KjkG4iHP1XgKaWncUq2ubzQEvV1BuvuliYZYPHFWNdaerEA0ezEKrwkOIRFG0rq1pbPNY9fh8wcAowm8oNsyfxG1NervDhGxaqOZNnAMBvE7g/zI5SN+91ho0Ip4DK0bjQ3LJzM0hFdgAaVzuvvdfN1MFhPAvBEg8LMgxARXnN2s0AVm9vrx2OSTswe/96w8K5zgDuDcG7n8c5d+UOK/K9+LxTlM1jYQ2OkO0XLvwcBVj16ccfvW8GwqYVWPT8EmFlvvPVn7+qdPUo3/REOXt5cOoJo1lYk+di5WILYFFUPK1GVesBNq5J7tjl5YIAqnEKFnucTUpLfJR2lCbGq2q9C6HSCOQvSA5g+VLhnX0WkWgWC7Mc3m1dFhihMNfCCMSh0iD0xxV6epN/IWUHcB4cIBKDuPL9bzHiCiL0G1HtBDj7tTISmcphhhoYZjiinP4uDIDG6ZSXt+ye45bINSDL54XKIiE303k5HgxNvQEDPojcH+Fab5jz16IMhRXgplsjhaKqbNi2s8il8olC8VRm/9T40yw5/RCPaWtXZ8eP4w+TUCjkvjUQXY3oCkECTlxU1XWrvy/qNGpc+dNo/OrDgbvfdnd3R2Aaj9Mnrb8A0TtykI+7cqgAAAAASUVORK5CYII=)|Display Warning Box | Shows a warning pop-up message with title and body |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA+QAAAPkBHYYEgQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAATBSURBVFiFtZfNbxNHGMafeWfWieOES5AaonyhpiUR4lYpiX1hkSKhBFG4gARK/4eUlqQq4oCQSNxDRXvkjFS4EC4uxEDEAX+ot1ZKDnCgakk4xD1kk6w/5qMH2xuv7U2sKDyn9cz4fX47M+87s8wYg1b0bmqqrV3gnNH0NQijMDgB4ESlewMMG9BYY6Sf5iVeDScShVbisoMA/j5//gRZ/LYBu86ArlaCGsBhMA91Sd0ZfPZs41AA7227nUcit8AwC6CjFeMm2oXBz2pn5+7Qykq+ZYD309M9nLMlGIwd0rjOBdntfHFmdHn57YEA/05PnzHEEgD6jsS8oqKUOWgz8/nz578HAryfnu7hxP44avOqHNctMEZnR5PJTLWNPHPbbuecLX0qcwBos6w2pdXLVdvubADgkcitI1vzAIWEADHWwS3+tNrGjDGVVBPv0GS3i54eHLtyFXJ9Hc7SExgp9zVhQqDr0mWI3l5sPX4E+fGjr78oJXbyeViCTYwmVzICAMjit5uZA8CxK1cRmZwsv8HICHIL9wIhmBDonv8B4bG9ifzvl/u+MZzKk85ADwCcoXdTU20G7HrQG8n1de85PDaG7rl5MCGam8/N+8xr/1sVVQBKSp9ete1Oahc4t1+Fc5aewM1m9yDGx9F9c84HwYRA9805hMfHvTY3m4Wz9KQRFOVZMMYwERI3+OwXp74Dw1dBANAabioFa2gIVl85Qaz+flgDA9hNpwAiHL85h3A0umeeySC3uBC4VFIpKK3BQJ/x2ZEvvwcwGAhQhUinYA0Owurv9yBCAwPoiMUQjsb2zNNp5OKL+25WpTWkUiAGQZVT7UAZKZGLL8JNpby2cLTOPJU60BwAqsVPAxECWgOoQmzGF+Gm3jT0uak32GzBHAB0BcBobdEBYz+JtNbeMwHY97yuFROisuFiDX3haAzH67KjmYwxUBUAxpgksNYAvFSr3e2pN77lCEejDSlar5JS3jMR7RI01loyn5tHeGKixjyFzXgcm/G4f2NOTAQWK6Bcir24YB/4tyPDCvtUQq+81haZdBq5n+KAUoAxcDNpf4r29cE6ebIMVrPeSmu4hb2roiXoV8pLvDKAEwTQdemyr7y6mUxDqnkpmvGOeYTHxtB16bIvVq05AwwXofs0nEgUGMzDIADR27sXIJsNrHBGSuQWF3xlu/a/RSl96y84Xx1OJLYEAOiSukOW+AZNTsStx48AoKXj2EiJ3MI933EMlKd+t+C/pRPYNaDmSvbPhQt3wfBjYPRDyhiDLdf15X5IWK9HksmzZZCK1M7OXTBkG0McXkrrBnNB5AjHuVj97QEMrazkt/PFmaKUuaMwL0oJp86cMaaIeGw4k9lqAACA0eXlt9BmxnHdQrGFmt5MSmtsuy528nnU3rgZY6qdiysjyeRfteObfpisTU6OK61eEmMdbZYFTgQiAgswNcagpFR5pzcBF0QOEY/VmwcCAMCqbXdyiz8tlOS5ahsn8mCMMdDGQGvt1fZmCgnrtXCci7XT3hJAVWuT9jgDPSgpfdoYEzQJ/qCAEZyvEti1Uy9e/Lnv2FY/z1dtu1OExA2lzFVjdI8GIkZrC6icakS7DOwDEX7jInR/OJFo+sb1+h9ZRUoxCF3PpgAAAABJRU5ErkJggg==)|Display Error Box | Shows an error pop-up message with title and body |
|**Excel**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAfpAAAH6QGUejxAAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAQhQTFRF////29vb6+vi5eXTyN/E6Ojg6enf6urfwNzAtdi54uLX3dzQ6eng3NrOndGpkc2gks2hks6hk86ilM6ilM+jlc+kmtGnm9Kpn9OsodStodSuotWvpNaxpdaxp9ezqtWyq9m2q9m3rNm3rtq5sNu6sNu7sdy8s9y9td2/t97BvOHFwePKwuPKw+TLx+bPyL24yObQyb+6yufRy8C7y8G7zMK9zcS+z8bA0MfB0MjC0cnD0uvY1Oza1c/I1tDJ1uzc2NLL2dfK29bO29rN3O/h3dnR3fDi3/Dj4N3V4N/U4eDW4fHl4vLm4+HY4/Ln5OLa5fPo5+bd6PTr6eng7Pbu7Pbv7ffv7vfwyAytUwAAAA90Uk5TAA4aHThCR0htfNnr7PP7HqL7KAAAARJJREFUOE+V0GlTwjAQgOGoKOBBinjghWcVrYi19jAqYL3wQAQ8/v8/cUuZkk2WUd9PmeaZZFPGGBuf7SlNTzC5KXW/9zSHRFoHN0hQAAkSyIIGkgDQaffrDMDzbdTM2BCE1X4hPmhSAiL6IBSQloDtQfa5N+weA78J+dfNJD/EwK1B7kUtyf0v+PUKbUhbAdozhQKqWgoIoj8dNNpJgQIcATmeSHIwaIVaLQTo/gwymyPKDECWjygrg3xl3jhe2CrBsnhWIQCvH5Yf+KkFq4/yDgWK7931GHyXqCs4f+nyGKy+XuWpEz7fNmLA+eM2AepHBzDDnWUtXp58LRNgt2DsGSumaRbW9pfwDKkcJ8ulYPMHpgGnXd/VNfEAAAAASUVORK5CYII=)|Create Excel Workbook | Create new excel workbook and save it at the give path. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAHowAAB6MBMC+yxQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAGiSURBVFiF7ZfLSkJRFIb/tc8FPZgZ3rCMHDRL6Egv4CShB+k9urxDD5BFgaMc2G0QNJZwlkQQQUWiVIhg0MnVoDQ9KmQc92nQmu0b38fea2/WJmaGmyFcpf8FAbV2GskDlPnJZAJWg8uVrJMCVD2JjJIE9XcmM5p5vHFKYNQj8KvEO8iR4pTAqDvQjk3WeGvURRY0K5a+rzkh8PtgrIcylbV2041bYHY3XL+GrguowwYI9MTETceJQm2+lFYSANBoTlQGJyHpRS2YTDKEx3GBbgxQHngEin9WGTccABhoDBJ4IG1qcdzwr8j2CZA+eQU5yWmp4L0+kOKdiUuAA4xjX6pQ7RUgcQnNmJfBJ3AWsG01eUIVGXAA9ed688AuYCne2IIkgVwiffbaI0CKfgGhheXwuVPUdASEN/omB47bQOrw3C5QJ084JYNOTLvAdyn+KaAaJUAYMgQsFj01pQAAxZj2yYADKAaX8mW7wB3pAXPIAoeDtu09gvSAxKe3tW/vVBUjLufpJRz5zEK1T4BU7zWD58aMrwm0NgZ6/X9O3Rb4AAx4bYSh+ftFAAAAAElFTkSuQmCC)|Open Excel Workbook | Open an existing .xlsx file with Microsoft Excel. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAlsAAAJbAHGUoNyAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAL1QTFRF////VVVVQklgQUpgQklhQkpgRk5jSlJmVVxvVl5wV15wWFxjWmFzZm5/aXB+cXeEdnyIgH1qgIWQg39okZadk4tom5Bnqq6ws7i+trq6t7q6uby8u76+u8DFx8rHyczJzdHS1trZ2N3g4+jp5enq5erq5+zt6MA66b0o67oW67wb678p7Lwc7L4i7L4l7cAs7cEu7sQ57sU68MtQ8c9d8c9e89Zz9t+S9+Oh+eq5+eu7+eu8/PTb/ffk////4p7yfQAAAAV0Uk5TAAaPqLHX0bArAAAAtElEQVQ4T9XQxw7CMBBF0UDwQOi9d0jovdf//yxcYmkc7Oxz10dvpLFswup5tFEflSaJmMVCYDpQgC8Q8CeSANBmQAgMxAQUyqTFARcYiAmoNiRgQgF8AgMSVwGfUIAdAC6dgHzRDNhE1nGcjhG48hcB0JzIhl1RSgXGogRqdU0ZBOYLTRUVHE+0vRksP1/aM2Rhs6OtQ8D1xjtvL4YTrzfvfngYFv7DYLbSVEJg7GnKRQf8AJqfUqUW0vwkAAAAAElFTkSuQmCC)|Save Excel File | Save a existing .xlsx file to its current path or to a new path. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK3SURBVFiF5ZdbSFRRFIa/deZMMSMNRRcpsQKjJM05mV0eIqKo6AoFaYZRCdFDPVRUlGbSRFDRTSsiSrrQg0gXoqsS1psPOVJaVEZQUJAPQcRgZTirFx3IOQ7M8agPfU+bzdp7/ftn7X3OElVlMDGTCc7Pz/e8mfJhsmGoJSpWFCyBHIWG5lB4jasCgnuCKerz5IgalohaKmqRKdkG+FFBAemKFVjtJHlMQF5p3tgOM2pJ1LBU1BLEwmdOEjAQRQFUEu/kVIBVPuOcetgmKiDadaqBqwtTlW1ubPTt+4/kVSu1hhvJHSMsGVwBwKALSOodSMSKK8tj49y0XEKLDwNwsK6Mpi9NcfPdJOWAz+vj8qaLVBae7qveGLYOnFl3kpShKeys3k3kdyQ2X7ayBCs9yKsvr+PW3N/8wDZBzxP3xNaBgC/A9PEWJ/KP4fV4ASicVcDirEW0d7RTfjeUcNNkkJyy3Lj7mxpI5WpxFaOHjeJRSy23m+5wYcM5TMNk78391L95GreRf4Q/Nu5zDbT9aGNH9S7aO36ydNoSzhedxTRMrjfcsE3eF2wd6Gbe5LmcKjgBQGvbe4oubSSqUdvY+l3OhCW8BVZ6MDaeNCaDORmzHSVJRK8OLMicz/G1R+mMdlL/9hmLpi6kveMnW65t5d3X1rh4V2tgwsgJlK8qA6DiyVn23yrlYctj/EN8VBSeIjWQ6uSwttg6cLW4iuy0LOpeP6Hk9gEAvB4vletPM3NiHs2fWyi+suWfNa7WQOR3hOcfGzl870hs7k/nH/bU7CP8qYnIr4jdMkckvAXJ4GoNDCSuOdAv78BA8J8LUGpNEc678Wc8cnjAUeNgvDgU3u7tlHEqugyVEoUakFbA/qvjMtJbc2rbmqlkA367+JehsCMHehVgh31zqkFFGptD4RX9LqA/+As0xAKOOpJXugAAAABJRU5ErkJggg==)|Create Excel Worksheet | Create a named worksheet in a existing .xlsx file specified by a path. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK3SURBVFiF5ZdbSFRRFIa/deZMMSMNRRcpsQKjJM05mV0eIqKo6AoFaYZRCdFDPVRUlGbSRFDRTSsiSrrQg0gXoqsS1psPOVJaVEZQUJAPQcRgZTirFx3IOQ7M8agPfU+bzdp7/ftn7X3OElVlMDGTCc7Pz/e8mfJhsmGoJSpWFCyBHIWG5lB4jasCgnuCKerz5IgalohaKmqRKdkG+FFBAemKFVjtJHlMQF5p3tgOM2pJ1LBU1BLEwmdOEjAQRQFUEu/kVIBVPuOcetgmKiDadaqBqwtTlW1ubPTt+4/kVSu1hhvJHSMsGVwBwKALSOodSMSKK8tj49y0XEKLDwNwsK6Mpi9NcfPdJOWAz+vj8qaLVBae7qveGLYOnFl3kpShKeys3k3kdyQ2X7ayBCs9yKsvr+PW3N/8wDZBzxP3xNaBgC/A9PEWJ/KP4fV4ASicVcDirEW0d7RTfjeUcNNkkJyy3Lj7mxpI5WpxFaOHjeJRSy23m+5wYcM5TMNk78391L95GreRf4Q/Nu5zDbT9aGNH9S7aO36ydNoSzhedxTRMrjfcsE3eF2wd6Gbe5LmcKjgBQGvbe4oubSSqUdvY+l3OhCW8BVZ6MDaeNCaDORmzHSVJRK8OLMicz/G1R+mMdlL/9hmLpi6kveMnW65t5d3X1rh4V2tgwsgJlK8qA6DiyVn23yrlYctj/EN8VBSeIjWQ6uSwttg6cLW4iuy0LOpeP6Hk9gEAvB4vletPM3NiHs2fWyi+suWfNa7WQOR3hOcfGzl870hs7k/nH/bU7CP8qYnIr4jdMkckvAXJ4GoNDCSuOdAv78BA8J8LUGpNEc678Wc8cnjAUeNgvDgU3u7tlHEqugyVEoUakFbA/qvjMtJbc2rbmqlkA367+JehsCMHehVgh31zqkFFGptD4RX9LqA/+As0xAKOOpJXugAAAABJRU5ErkJggg==)|Get Excel Worksheets | Return a list with the names of the worksheets is a .xlsx file specified by the path variable. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAYNQTFRF////////YGBgYk5iiYmJgICSWlppVVVjXlFrhoaUWFhsh4KRWlJrhYWRhoOQiISRhoaSXFNshoOShoaSh4SQhYWRXFRriYaUh4eTW1RqY1twY1xwh4eViYmViYuYiY2aiYqXiIuYiYyYiYyZh4mXiIuXXFRqXFRqiY2aiIqXiIuXbGZ5bGZ5h4qXXVRqXFRqhYeVXFRqhYeVXFRrXFRqiIqXiYqXiIuXiIqXiImWiImWiImWjJSih4iWkaGvkaKwc26AjJKgjpmnkaGvkaKvdHCBiY2ai5KgjZmmjpuoiYuZjpmnh4eUiIeUXFRqh4aUh4iWiIuYiIiVh4eUlq+8lq++l7PAi5urlK27lK28lrG/g4GOhoaUnL/NnL/OXFRqX1htYFhuc25/c2+BncfYn8jXos/eotDfo9Hgo9Lho9PipNTjpdjnptrpptrqp9vrqN/uq+j4rez8ru7+ru//sfD/ufH/vPL/vfL/x/T/yPT/zPX/4Pn/4vn/8Pz/8/3/////FiVGzgAAAF90Uk5TAAEIDQ0OERITExozPkFOT1JTVFRVWmRwcXOJi5OTra+xsrO0tbbAwsLJytTV1dfY2Nra4eXl5ebn6erw8PHy8vPz8/Pz9PT09PT19fb29/f39/j5+fr6+/v7+/7+/v4d+WzOAAABSUlEQVQ4T93QV1fCQBAF4KEJQaKi0hTsEsAGglKs2LBiw15iQ1QslFXs7k93kw0cXoK+6n37Zu7ZM2cB/kmqfljZOPkCZwMw+vTyBb3PCJxBfg9g4ICvtAey/l1BbbK7HCZ1cao2OVx2SlJQArDh8aPL45kIS/dsZJpwIkyoJIUBZ8/6FRJyM9cAOh3ULVJer/U6+3nw8yeHt4SPb8/obqw5EGgaoSygi4NT3g/m+Pm+0P/E+BXtzapUk7sCvzB+QTtncTOAti9NBk8Y4w+UGgTwpggLhO8o7dUKNy1nSy9kV4sUX8iuiEcPZZB0A8qEAIYlFihJWpKomGQnQGsZ28VCTTQnDXKxRoDaWInRevoxbYk8nWx3C+zYoswnuqSfZdzz92T2sOBhRHqWRE65GakACktwc3QjZFVItIYIgxYFlEVTranAP59vjw1xvdJmgZAAAAAASUVORK5CYII=)|Read Cell from Excel (by row and col) | Read cell value from Excel by row and col: first row is defined row number 1 and first column is defined column number 1 |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAYNQTFRF////////YGBgYk5iiYmJgICSWlppVVVjXlFrhoaUWFhsh4KRWlJrhYWRhoOQiISRhoaSXFNshoOShoaSh4SQhYWRXFRriYaUh4eTW1RqY1twY1xwh4eViYmViYuYiY2aiYqXiIuYiYyYiYyZh4mXiIuXXFRqXFRqiY2aiIqXiIuXbGZ5bGZ5h4qXXVRqXFRqhYeVXFRqhYeVXFRrXFRqiIqXiYqXiIuXiIqXiImWiImWiImWjJSih4iWkaGvkaKwc26AjJKgjpmnkaGvkaKvdHCBiY2ai5KgjZmmjpuoiYuZjpmnh4eUiIeUXFRqh4aUh4iWiIuYiIiVh4eUlq+8lq++l7PAi5urlK27lK28lrG/g4GOhoaUnL/NnL/OXFRqX1htYFhuc25/c2+BncfYn8jXos/eotDfo9Hgo9Lho9PipNTjpdjnptrpptrqp9vrqN/uq+j4rez8ru7+ru//sfD/ufH/vPL/vfL/x/T/yPT/zPX/4Pn/4vn/8Pz/8/3/////FiVGzgAAAF90Uk5TAAEIDQ0OERITExozPkFOT1JTVFRVWmRwcXOJi5OTra+xsrO0tbbAwsLJytTV1dfY2Nra4eXl5ebn6erw8PHy8vPz8/Pz9PT09PT19fb29/f39/j5+fr6+/v7+/7+/v4d+WzOAAABSUlEQVQ4T93QV1fCQBAF4KEJQaKi0hTsEsAGglKs2LBiw15iQ1QslFXs7k93kw0cXoK+6n37Zu7ZM2cB/kmqfljZOPkCZwMw+vTyBb3PCJxBfg9g4ICvtAey/l1BbbK7HCZ1cao2OVx2SlJQArDh8aPL45kIS/dsZJpwIkyoJIUBZ8/6FRJyM9cAOh3ULVJer/U6+3nw8yeHt4SPb8/obqw5EGgaoSygi4NT3g/m+Pm+0P/E+BXtzapUk7sCvzB+QTtncTOAti9NBk8Y4w+UGgTwpggLhO8o7dUKNy1nSy9kV4sUX8iuiEcPZZB0A8qEAIYlFihJWpKomGQnQGsZ28VCTTQnDXKxRoDaWInRevoxbYk8nWx3C+zYoswnuqSfZdzz92T2sOBhRHqWRE65GakACktwc3QjZFVItIYIgxYFlEVTranAP59vjw1xvdJmgZAAAAAASUVORK5CYII=)|Read Cell from Excel (by cell name) | Read cell value from Excel by cell name e.g. cell="A2" is the first cell |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAD2AAAA9gFrSKqbAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAgdQTFRF////AP//AAAAgID/VVVVVVWqQIC/M2aZZmZmVarV1dUASUlJYJ+/YJ/fv78gVY7jZpnmVVVqVYC/VZXVYp3YW5LbVYi7Woe0VYC4Y46448YAXl5eZoCzXXSXXYCiyLEW07EL58IAYGBgYGBgxagYXGFuWVlhX5TdWlpiWVlZYJTeWlpgXWBnXFxfXofAWlpgWVlfWFhbXoa/Xl5e07YM5cQAW1teXmBp0rUNWlpfXFxewqkZXFxe5cUAX5TcXpXdWlpf5cQAWVlb4cQGXV1fXpTe0LUM0rYOwakYXYS8XoW8W19mYJbcW1tfwagZXXyovagdXoa85sMAYJXdW1teXoa85sQAX5bcX5XdXXOVwacaXoW8XpTd5sUAwKcZXoa7XoW8X5XdXG2IWVlbXYS7X5Xe5cMAX5XdWlpaX5XdwKgaX5XdXYa6X5XdX5XdW1tbX5XeWlpcXoW6v6cbXoW6X4W6XYW5XoW6W1tcXoW5XoGxXoW6Xoe/WVlaXpXd5cQAZJbWXXebXXulWVlbXoS4YozCvaUbYoOu2L8WX5XesJ8uXoS45cQA5cQA5cQAvKUcvKUcvKUdX5XdXoS35cQAXoS3X5Xdu6QcWVlaWVlbWlpcXHOUXHSVXXmhXXqhXX6rXX+tXn+uXn+vXoO2XoO3Xoa9XozKX4/QX5XcX5Xdu6Qd0LQO5cQAEAW3WgAAAJh0Uk5TAAECAgMDBAUFBgYHCAgICQoMDAwNDg8REhISExQWFhcXKi01NTpCQ0RFRUpKTlFSU1RUV1dXWlphZmdobG1ub3R0dnh5enx+gIGChIWGh4yMjY2QlZiYm5ydoKOlqqutrq6vt7e3uLm7u7u+v8HDxcbHx8fIys3P0NHS09PU2Nnb3N3f4uLj5urs8PHz9PX29/j7/P3+/v6uil2oAAABRklEQVQ4y33RVVNDMRAF4BR3d3d3d4q7u7u7u7trixQopQF60/sjabl566bnLfPtnNkkCOlJ+MBWvh72ih59fjlge+hZTcbM6xzTc+45aVvjajyDzVs5jvuR9Fcx3HpE6xhfVNiDbjsm+ENMIeh2E4Ljssg4yB2nqPeGiY0Ad5qmvhiVbga48yz1pdRYqN99UyX4cnAiuP+6/Ful9RVvsSX0PkO/n/IvJcZrLiGBgJv0cdzvh+xdueGKUjx13bBTu5/iTbbvhlCWgY6LWoT9FXs+mlOAbkEDvd+8A/xBldQnrWAvoj5oCnsu9R5j2COkgneIYEfbgjcx2KNg99/rYPZvvuZPjzCWlMOezGuiPj85TGD05/GPV2pCahEr9Xy23y2582UODF+mlT6RbqZb7JTcEEKCmANdxccL7dWZTEdJ4zZIX/4A0dyRlVJ/y0gAAAAASUVORK5CYII=)|Write Cell to Excel (by row and col) | Write value to Excel by row and col: first row is defined row number 1 and first column is defined column number 1 |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAD2AAAA9gFrSKqbAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAgdQTFRF////AP//AAAAgID/VVVVVVWqQIC/M2aZZmZmVarV1dUASUlJYJ+/YJ/fv78gVY7jZpnmVVVqVYC/VZXVYp3YW5LbVYi7Woe0VYC4Y46448YAXl5eZoCzXXSXXYCiyLEW07EL58IAYGBgYGBgxagYXGFuWVlhX5TdWlpiWVlZYJTeWlpgXWBnXFxfXofAWlpgWVlfWFhbXoa/Xl5e07YM5cQAW1teXmBp0rUNWlpfXFxewqkZXFxe5cUAX5TcXpXdWlpf5cQAWVlb4cQGXV1fXpTe0LUM0rYOwakYXYS8XoW8W19mYJbcW1tfwagZXXyovagdXoa85sMAYJXdW1teXoa85sQAX5bcX5XdXXOVwacaXoW8XpTd5sUAwKcZXoa7XoW8X5XdXG2IWVlbXYS7X5Xe5cMAX5XdWlpaX5XdwKgaX5XdXYa6X5XdX5XdW1tbX5XeWlpcXoW6v6cbXoW6X4W6XYW5XoW6W1tcXoW5XoGxXoW6Xoe/WVlaXpXd5cQAZJbWXXebXXulWVlbXoS4YozCvaUbYoOu2L8WX5XesJ8uXoS45cQA5cQA5cQAvKUcvKUcvKUdX5XdXoS35cQAXoS3X5Xdu6QcWVlaWVlbWlpcXHOUXHSVXXmhXXqhXX6rXX+tXn+uXn+vXoO2XoO3Xoa9XozKX4/QX5XcX5Xdu6Qd0LQO5cQAEAW3WgAAAJh0Uk5TAAECAgMDBAUFBgYHCAgICQoMDAwNDg8REhISExQWFhcXKi01NTpCQ0RFRUpKTlFSU1RUV1dXWlphZmdobG1ub3R0dnh5enx+gIGChIWGh4yMjY2QlZiYm5ydoKOlqqutrq6vt7e3uLm7u7u+v8HDxcbHx8fIys3P0NHS09PU2Nnb3N3f4uLj5urs8PHz9PX29/j7/P3+/v6uil2oAAABRklEQVQ4y33RVVNDMRAF4BR3d3d3d4q7u7u7u7trixQopQF60/sjabl566bnLfPtnNkkCOlJ+MBWvh72ih59fjlge+hZTcbM6xzTc+45aVvjajyDzVs5jvuR9Fcx3HpE6xhfVNiDbjsm+ENMIeh2E4Ljssg4yB2nqPeGiY0Ad5qmvhiVbga48yz1pdRYqN99UyX4cnAiuP+6/Ful9RVvsSX0PkO/n/IvJcZrLiGBgJv0cdzvh+xdueGKUjx13bBTu5/iTbbvhlCWgY6LWoT9FXs+mlOAbkEDvd+8A/xBldQnrWAvoj5oCnsu9R5j2COkgneIYEfbgjcx2KNg99/rYPZvvuZPjzCWlMOezGuiPj85TGD05/GPV2pCahEr9Xy23y2582UODF+mlT6RbqZb7JTcEEKCmANdxccL7dWZTEdJ4zZIX/4A0dyRlVJ/y0gAAAAASUVORK5CYII=)|Write Cell to Excel (by cell name) | Write cell value from Excel by cell name e.g. cell="A2" is the first cell |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK3SURBVFiF5ZdbSFRRFIa/deZMMSMNRRcpsQKjJM05mV0eIqKo6AoFaYZRCdFDPVRUlGbSRFDRTSsiSrrQg0gXoqsS1psPOVJaVEZQUJAPQcRgZTirFx3IOQ7M8agPfU+bzdp7/ftn7X3OElVlMDGTCc7Pz/e8mfJhsmGoJSpWFCyBHIWG5lB4jasCgnuCKerz5IgalohaKmqRKdkG+FFBAemKFVjtJHlMQF5p3tgOM2pJ1LBU1BLEwmdOEjAQRQFUEu/kVIBVPuOcetgmKiDadaqBqwtTlW1ubPTt+4/kVSu1hhvJHSMsGVwBwKALSOodSMSKK8tj49y0XEKLDwNwsK6Mpi9NcfPdJOWAz+vj8qaLVBae7qveGLYOnFl3kpShKeys3k3kdyQ2X7ayBCs9yKsvr+PW3N/8wDZBzxP3xNaBgC/A9PEWJ/KP4fV4ASicVcDirEW0d7RTfjeUcNNkkJyy3Lj7mxpI5WpxFaOHjeJRSy23m+5wYcM5TMNk78391L95GreRf4Q/Nu5zDbT9aGNH9S7aO36ydNoSzhedxTRMrjfcsE3eF2wd6Gbe5LmcKjgBQGvbe4oubSSqUdvY+l3OhCW8BVZ6MDaeNCaDORmzHSVJRK8OLMicz/G1R+mMdlL/9hmLpi6kveMnW65t5d3X1rh4V2tgwsgJlK8qA6DiyVn23yrlYctj/EN8VBSeIjWQ6uSwttg6cLW4iuy0LOpeP6Hk9gEAvB4vletPM3NiHs2fWyi+suWfNa7WQOR3hOcfGzl870hs7k/nH/bU7CP8qYnIr4jdMkckvAXJ4GoNDCSuOdAv78BA8J8LUGpNEc678Wc8cnjAUeNgvDgU3u7tlHEqugyVEoUakFbA/qvjMtJbc2rbmqlkA367+JehsCMHehVgh31zqkFFGptD4RX9LqA/+As0xAKOOpJXugAAAABJRU5ErkJggg==)|Put Row In A List | Return the elements from a specified row in a list. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK3SURBVFiF5ZdbSFRRFIa/deZMMSMNRRcpsQKjJM05mV0eIqKo6AoFaYZRCdFDPVRUlGbSRFDRTSsiSrrQg0gXoqsS1psPOVJaVEZQUJAPQcRgZTirFx3IOQ7M8agPfU+bzdp7/ftn7X3OElVlMDGTCc7Pz/e8mfJhsmGoJSpWFCyBHIWG5lB4jasCgnuCKerz5IgalohaKmqRKdkG+FFBAemKFVjtJHlMQF5p3tgOM2pJ1LBU1BLEwmdOEjAQRQFUEu/kVIBVPuOcetgmKiDadaqBqwtTlW1ubPTt+4/kVSu1hhvJHSMsGVwBwKALSOodSMSKK8tj49y0XEKLDwNwsK6Mpi9NcfPdJOWAz+vj8qaLVBae7qveGLYOnFl3kpShKeys3k3kdyQ2X7ayBCs9yKsvr+PW3N/8wDZBzxP3xNaBgC/A9PEWJ/KP4fV4ASicVcDirEW0d7RTfjeUcNNkkJyy3Lj7mxpI5WpxFaOHjeJRSy23m+5wYcM5TMNk78391L95GreRf4Q/Nu5zDbT9aGNH9S7aO36ydNoSzhedxTRMrjfcsE3eF2wd6Gbe5LmcKjgBQGvbe4oubSSqUdvY+l3OhCW8BVZ6MDaeNCaDORmzHSVJRK8OLMicz/G1R+mMdlL/9hmLpi6kveMnW65t5d3X1rh4V2tgwsgJlK8qA6DiyVn23yrlYctj/EN8VBSeIjWQ6uSwttg6cLW4iuy0LOpeP6Hk9gEAvB4vletPM3NiHs2fWyi+suWfNa7WQOR3hOcfGzl870hs7k/nH/bU7CP8qYnIr4jdMkckvAXJ4GoNDCSuOdAv78BA8J8LUGpNEc678Wc8cnjAUeNgvDgU3u7tlHEqugyVEoUakFbA/qvjMtJbc2rbmqlkA367+JehsCMHehVgh31zqkFFGptD4RX9LqA/+As0xAKOOpJXugAAAABJRU5ErkJggg==)|Put Column In A List | Return the elements from a specified column in a list. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAK3SURBVFiF5ZdbSFRRFIa/deZMMSMNRRcpsQKjJM05mV0eIqKo6AoFaYZRCdFDPVRUlGbSRFDRTSsiSrrQg0gXoqsS1psPOVJaVEZQUJAPQcRgZTirFx3IOQ7M8agPfU+bzdp7/ftn7X3OElVlMDGTCc7Pz/e8mfJhsmGoJSpWFCyBHIWG5lB4jasCgnuCKerz5IgalohaKmqRKdkG+FFBAemKFVjtJHlMQF5p3tgOM2pJ1LBU1BLEwmdOEjAQRQFUEu/kVIBVPuOcetgmKiDadaqBqwtTlW1ubPTt+4/kVSu1hhvJHSMsGVwBwKALSOodSMSKK8tj49y0XEKLDwNwsK6Mpi9NcfPdJOWAz+vj8qaLVBae7qveGLYOnFl3kpShKeys3k3kdyQ2X7ayBCs9yKsvr+PW3N/8wDZBzxP3xNaBgC/A9PEWJ/KP4fV4ASicVcDirEW0d7RTfjeUcNNkkJyy3Lj7mxpI5WpxFaOHjeJRSy23m+5wYcM5TMNk78391L95GreRf4Q/Nu5zDbT9aGNH9S7aO36ydNoSzhedxTRMrjfcsE3eF2wd6Gbe5LmcKjgBQGvbe4oubSSqUdvY+l3OhCW8BVZ6MDaeNCaDORmzHSVJRK8OLMicz/G1R+mMdlL/9hmLpi6kveMnW65t5d3X1rh4V2tgwsgJlK8qA6DiyVn23yrlYctj/EN8VBSeIjWQ6uSwttg6cLW4iuy0LOpeP6Hk9gEAvB4vletPM3NiHs2fWyi+suWfNa7WQOR3hOcfGzl870hs7k/nH/bU7CP8qYnIr4jdMkckvAXJ4GoNDCSuOdAv78BA8J8LUGpNEc678Wc8cnjAUeNgvDgU3u7tlHEqugyVEoUakFbA/qvjMtJbc2rbmqlkA367+JehsCMHehVgh31zqkFFGptD4RX9LqA/+As0xAKOOpJXugAAAABJRU5ErkJggg==)|Put Selection In A Matrix | Return the elements of a specified selection in a matrix. |
|**Word**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAfpAAAH6QGUejxAAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAXdQTFRF////29vb6+vi5eXTksjf6Ojg6enf6urffMLhYbni4uLX3dzQ6eng3NrOIqLlAJbmApfmA5fmBJjmBZjmC5vnD5znEZ3oE57oFZ/oFp/oGqHpJKXqJqbqKKbqK6jqLqnrL6nrOK3rOq7sQLDsQa3kR7PtSLTtSbTtSrTtULfuVrnuYr7wZcDwacHwa8LwbsPxccXxcsXxeMfyfMnyfcnyfsrygMvzg8zzhpfLhs3zh5jLi5vMi8/0jND0jdD0k6LOlaTOlqXOmNX1nqvQntf1n6zQn9f2oq7Rotn2o6/RqbTSqdz3qrXTq7bTrrjTs+D4tr/Vt+H4uMDWuOL4vsXXv8bXwcjXwub5xef5x83Zyun6zdLaztLaztPa0NTb0ez61O371dnc1e7719rc1+/72Nvc2O/72dfK2dzd2vD729rN293d3d/d3d/e3+He4N/U4eDW4eLe4ePe4uPf5OTf5OXf5ebf5fT85ubf5+fg6Ojg6eng6fb9GVaodwAAAA90Uk5TAA4aHThCR0htfNnr7PP7HqL7KAAAAUVJREFUOE9jYGBgYOKpRgNczAzIgA1dvjqfF0UFO6aCdBQV2BSgqMCqAFkFdgVIKoAKsj3d3X0r4QoKskCAmxGhoCw0JCQSwyBWnFZAATtCQaqjAxAEVPuUhoEYXtUBjqkoCqpio4Egtzq1uhDEyKjOja1CUUDQimQrCwSwzrO3sLBKRjUhOwMBcqrzMjKyq9EVFFWXgKWhdDaGFc7VfmALoDS6FYQcWVFcnQjyXxkuBXFBla6gEIrBpQA7oJ4CDhUcgAOqgJMfB+BEViBlZKguwM8vb6YtyM8vZ6YjjK5AMUrDJlBALkHNzolfNkVDXwxDQTA/v7+arS6/YI2QpQEWK0AKPHTcNPn50yRdtHAoyFQyNeYXLec3MsGmIEk/wptfIt48XI9fPN7cWxJdgaiaqgKQElGWBpMyyCaw8PFjBXwsQEkAUY/45mfGYL0AAAAASUVORK5CYII=)|Open Word Document | Open a Word document by referring to the absolute path |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAT3SURBVFiFpZZfTFN3FMe/51J620JLTIsynUwgDhYnxWypuhdj5pjJNt78M002FUxG/Le5zckmuCEKcTObmSYmhuBc5hKXZQtL9sA0kwdNwCUKeyDOAYkIammjtEILvb1nD6Vw/1Pnebq/3z2/3/dzz++c87vEzDCy/lUVa8FyXklX76+GDhlarKbmEyLaA+A3x9jYPly8OKV8LxgtGgj4a0nmy8T0y0CgvPn/iserq5sJaAHzIjC/F/N4fsLGjXZLgIGAvxbAaQCUmqGDAwH/sScVj+2sPg6ig8o5Aqq0ECqAzvLSC1FJUojPWF3/Sv/RTMVvfL30K1mQ3jd6p4WgdA4MBPy1UUk6fScWp8VOBzw2m24xM46WXO85ZCV+7cwznxPxYWfMjaV9rySyktnZRn4MtDsjkQ3EzKqwRyQJQ7E4zCAI1FTUfbPeaNOe7wpOTsSxNz2eCwJEZ+jflf61JPNlKMI+NwQfKerubVDOhToWHGfGhyMPSJiIzc5bQhANC2A5D5oz99hsWOx0YCgWR0SSdOsYVD8YKG9Mj0c7CppB+JgECAsXsOxyzvrGnFHcfuFadjIrkdDtw/zt9BGUNwPqjM0kEgA3upuCdiJWrWUZ8pyRYG5xtLbWKZPwGIC6J4EQK6MQ14wbgFlDCLLtG+fZ1gOAogoAoH+l/ygxPs0EwkocAJJJYPgegQQgHp+dd0y4T6z44PZH6bGqD5R09XzGDF29a3MiE/G7IwSHA3i2YDYnmOkLpbguAmkbDFQcYbCu3iOSBFoXwaLXpnRrtOJOJzDfl9qbZcgj9+mU/937+7T+hgApiPJGBqnqPdMvV4qnCPClr/LBAaM1hpcRABR19zYQ+MjTijNTi5m4JUAaAuDGjMUdevH8yvu6ylKaUXGrbLrOMxPPn/Wb7MzBZEcu8iut97eMwGhHQbO2yRiJOwzF3Uhd5db/E6YATyK+wFA8bdYQhgBziQOpJqMVH/7DjtHfnQbe5hA6gPClwkNziQOAdx7rvhyXPKYXGEAHB9cEdL1FBRAKXXXbK85uJtu8oJFoMgk8fJR6zsmZnU+H3W2zodDkFhW8eUHfj02bQ6GrbtW8ciAKiU0gcZl9+anHWoj0mSck9d+a9syNIARvXtDb1vAYon2ZKCQ2mQKAsQMAQLZiJYQq2zV1PtmR26KNlBJi3OMa87Y1PEa2rTi1iLYrfWdacTR8pQxAnxpIGpi4uctz986YT5twyiZj9j8xnpczVth2OCI4xcXqfbnM7Vt7SxMBNVk6ElnFdTFXrjhhJg4Axd29dQCrIiF484JLvm8M68QBgGibJgJXbNEwhgAU6JynIzH19+5clh7Ot2qv6UjMnHk67HqCEbc3WAhsSAoAEA1hvak4MJ0TJ0eJxHqr3l7c3VtHTrHe23po1FwcAHhhZNT3OjB9BG/vOrclGIqa+OIqCDWTyF3tXXenyXzTlBV1djdN2nNWg7AToGtGPsFQlLfv/2EHANDzL73lE7J52OfNmTp3YmvufJ8bAIYBPg+Wz7l9r/4zl6iVRUN/lqbOnN4BeGEwFMXWPefDY9G4W07Qoizfc6U1BLw5EUugt2+kvWr98v0eb+du0bXtkugqDj+NOACIrqKw6FpyWXRdPzk57uraW/+za+jeoxcB2JFFw1S26o02hnCDE7hw66/20NMKZmKlL1f5KBtbCPKK/wAGOI4jKi0o3QAAAABJRU5ErkJggg==)|Replace Text | Replaces text in a Word document, for example to fill in certain fields in a form |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAFuAAABbgGEUF8kAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAVBQTFRF////AP///4CAv0AgQLOZ3F1RQ7GbO7Gd41VMtTgq4VZOtzcrszgo41hM5FZLzkk7PLKfPLOdPbKdPLOePbOfzEU4zUg64ldM4ldL41dNPrOe4lZMPrOe4ldMPbOePbOePrOe4ldMPbOePLSePbOePbOdPbOetTYp4ldLtjYp4ldMtTcpwj8ztjUp41dMtTYp4lZMPrOe4ldMPbOf4lZN4ldN4ldM4ldM11BD4ldN4ldM4ldMwD0x4ldM4ldMPbOetTYptjcqtzgrvz0ww+fhxuniyerk4ldM4lpP5GBW5GJX5WVb5Wlf53Vs53du6oN76oZ/6oiA646G7ZeQ7ZmS7p2W76Od76Wf8Kii8Kmj8Kqk8a2o87iz87y39s7K99DM+NTR+NXT+NfU+dnX+dvY+d3a+d3b+uDe+uPh++Xk++fm++nn/Ovq/O3s/vr6////kQlsrwAAAD90Uk5TAAECCBQWFxobNzs8QEBBSV1eYGFlaH+TlaqusbKys7W2tri6u7y/wcTGx8nMzc7R4+Tl5ubw+Pn6+vv8/f3+lASLvgAAASNJREFUOI3l0NdWwkAQBuBBFHvHrth7F00kMWFRYcQG2LD3Lmbe/87diOcoTvAB/C/m5v+2AshUjWmaput6JGIYhmmalmXZNiIur4xWqh4mkM+aEOMu8OhRCDH9B5itKQr8foCiAOAfgmvnPoU3zvtFEu+cWwY4mbMHpMP9XBYps82B1OkTUhqzj0g7Gxyg57QCRy9IdM6BXTnoYO/t2GOHyy05cvR6solXScTFno4Z72fa7RXwPYX9Qp0vGAqHu5s8gF0bGIq66StlQZtvOJpPLwvKgqqLr6vZwIA5CKmKSM1OBnRBWK4nGbnHPAP6FUgoEOfBUsmPI6onRUFi9e4lE3E1G+FXL8SUb+TrmQPAgVhreV4MBoA5QojVls+vbpb3+wBkgtxo6h4uQAAAAABJRU5ErkJggg==)|Convert Word to PDF | Transforms a Word document to PDF |
|**PDF**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAEHSURBVFiF7ZZNTsMwEIU/R1UNG+JUpOfhNL0AUlfddctNOARn4AK9QBJUpxKNpVphkf5QCagHJcrGbz3y+8Z+Hls9r99a+pV7WT3dhRYnPZuLFQEiQASIAKMDTCTFm807cJncdlvgvSebzVEqwbk9ta30Ylk0gwBAS9t2ANaW+MMBk80BRdN8UtuS1OQAOnTFfx3Bd/MkOXVe8pA+ovW9aC0xQJ/mYgC7LW6aO7cfDsB7/7f5MQcSiUKYzbrA/WpeV5guhMES7cDlqv1snpqc6ZAhvGk+Df6JnTUBXGhxbSudmvwqcLvdB+aqcyUCUKfBEqLF8rVBMGRCNPpbEAEiQASIAKMDfAHZRpDbmRa42gAAAABJRU5ErkJggg==)|Merge PDF | Adds the pages of pdf2 to pdf1 and saves it at merged_path. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAPrSURBVFiFvZVvTFV1GMc/zznnklgXLggDLM3NJspyhKPmaDnkBUy8pDajrfXGWHO5hpW8tulqhZM5Wbb1omVvWn+dTYEG6nWYWVvOWi665Au1W0Aw7mU0Arn3PL04l8u5DLZ7wct3OzvP7/k+v+f57jm/8/xEVUmguf6BMTHOKGxV5HjeyXPvkmEY7kUYeU6hHsgX9GjkjT2+ZRUA7HLZluq9+uUTsL/SIyI7klibZ5dNwFh2UTWQ4yZFZAf7Kz3LIkDVmG2/6tm4lRMXlnkBoA1xIyTKO/MKy5SASHN9BbAWQIWO3Pc7rwMDjgI7o+fAAkDEVUTPo6oc9HcCTYisiTTXV/jaO284fKMZ7l9XJdirnHC1Taygt7Q1uHgBGLvAGUii0ho56H8bKEhEOQJvAER+X3tYxD48m0KIESMSbBkBCUQxmgpKW8dTFWCMHtq9BrTC5SsDyoGHEx6d7ZAKpQvkKgB93sL+KNXiAIZEp2fbL1xV1c9nHuBO3L/FEZoMVV5U0Z2IHgKmnVBt4PIRK1UBFriGjcReymvvuj2zjDT7X0c44VDRBuAD9+aobQQKNx4bBDoj/S3bUfwKK0YfmSjOh1AqAgxByuP2Td+J2eIOKR0JW3XzQkkGrh9ZibIJQGAy/7GVf6dS3MmLvAx8ImrvnkvmnDz3hwiNoB+rYbfO5T2WfSESbPkl+6HxUWC949Uz8JadqgBJuo5TQDjY8pnACwtnZI9vw/GzC/JzMPc2TAuCfAv6DdCfcCqnRm815yy8Kxkpn9b5cC8m+wrL2gYBxoItpxQOAKvN6IqtQDdA45eYkcKhfYYtT6tBEWrfViXQU1P8lYIuSYAbqlxEOACgomVAd9W1ULa3wNMrSqWKxmedIMKrtYGh7+umqV3SJ0gSgLgH1BiAd9LTClTOOAVGXDFVeOTYkjpgGfb20eCbYROzXERfm/Hbtt0XN/fG3//apv1Uz7aSvtrLw0+I2j8BJqh/aYdQ+NTA6FL0PWC149Ur+ZvafvB/dzcPKHECCfRsK+kD6K4u/Bk474QylXYHRAki83OKdqtpNQHEolm5LiJpMJmWvhKNGV1qxnrTFuDbePdouH/dhcR1DAg6HjPpz1/f9mcqOTqfKR4GPoRF/YZfxPI2cCX9ffPjvv0Fi8V9mwPpQEDqLg0+mTWhNzPWgemY8V9ioeS6udrA4GkV+XHqQSOQ9mWUDuoCQ2HAJzAyJUUlgWqiVddC2d5JzxDgBYYzegYEegEUCrJ0KFQbGPzaO+kJxYujkNkO7Lw08GhUjF9nCs7BP1G1tmS0Ax01JXcstTeLymngFjCh8BvQblr6+MWaVX/9D48CdgjDk2lOAAAAAElFTkSuQmCC)|Extract Text From Page | Extracts all the text from a give page and returns it as a string. |
|**File Manipulations**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAO1QTFRF////AAAAAACA///MOTlVQCtV7+/fOi5RQDVK5dzKOjFKgHmGPTROPTJNPTJLPDFMPjJMRz5VPjJMPTJMPTFM7uvePDJMPzRO4d7N4NvKPTJM2dXBPTJNPTJMPTJMQDZPQTZPSD5VVUtfV01hZVttdm17hHuGhX2HkouSlY2UpqCis62tuLKxx8G91dC71tHE1tHJ19K92dXB2dXM2tXB29bC3NjF3djG3tnH4NvJ4NvK4dzL4d3L4t7N497O49/U5ODQ5eDQ5+LT5+PT6OPU6OTU6ubX6uba7Ofb7Oja7ejb7enc7urc7urd7+ve8M8MaQAAAB50Uk5TAAECBQkMEBYYHR8mO2BwcoCEnZ6/yNfc4OTn8/3+6DSEYQAAAM5JREFUOE+l0OUOgzAUhmFmzN2tc3d35sKE+7+cAcuS07WFhL1/edIvHI6LSj8lnBwWAeZpXJCgiwsKwAUNYIIKoKADIFQgjJUEFQhTtaQFAvGkJGIv8awJY+Cygx1JsJ/BlgYm/gerLmxIgtcd9jQwoQsOC9iGBOc1rNe66kwUC7WOJmgghEpBFwCPC0zsI6VsxGv7gvUANpHKqkj5rKzfbMqfM34r+w7bPMrFQyaNQ1VQ1R0Lm9mgnRvxjo+gg1tdvoMjFmAC6aUcyu7h3hgM0xOjQKpIAAAAAElFTkSuQmCC)|Open File | Opens a file at the given path |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeLAAAHiwGGjZs0AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAUFQTFRF////7e3b8ubZ1lxH2V5M7+ffo0dA4t3K8cWH39/H5N/N4ODKoklB7+vgoUdAqk474Ywl4ook4owk5qVU7uvf1llLpUdB7+re11tK3NnNzcnA3GdB0WFA4Ism11pKrlQ7zVdI8p4l75kh4Ysl75sl4Y0lpEdB8psi5N/P4o0ncXFv4d3Mo0ZAo0dA4Ywl4Ywm2NPA19O/g355lJGMo0dA1dC71sSw11pK19K+19O+2ci22dTA2dTB29bD3M+93NfF39rI4NzK4Ywl4Y8s4d3L4pU24tbG4t3M469v47Fy497N497O5ODQ5uLS6OHS6OTV6eTV6eXW6trG6ubX6ubY69Kt69Ku6+fY6+fZ7OjZ7Oja7ejb7uDN7uLJ7uTT7urc7urd76Q57+PL7+XQ7+ve8KM58Lpr8pwh8qc88qg98qg+EJkP/wAAADJ0Uk5TAA4UGRsgJDU1Nzg6P0FERUVGR1toanqgpqivvMbX2t3d3d7i4ujp6err7O/29/f3+vtf74FqAAABA0lEQVQ4y2MQSUEDGuwMKABDgYsBOwEFpgacBBSYGnARUGBqyEVAgakhNwEFSCrACgIsLYDAHqzA1wEMtBlRTAgJBoIoFJNYcVlBnoJIR2TgnoChIMoFGXgl0MANEG/CQASmAkhAwYBNPLXcwCIhilcBs5y5ghhUQaA1MrAFu4FD2lxBzYQHoiAhwB8JBIOEkhTVZdRMdNhwWZGUla4kK6/Lh8sNSZnpKqpOyvwwR0Z7IwOflKSM9ERNJz0huDfDHZCBY2xGeqqrk54grnBIBsvrC+AMqLg0oLyzMO6QjAnydHIOxR3U8XZWZh5huOMiwdjIzS8BEVm84mhASksSTDNB5AHSbAq+H1vdKgAAAABJRU5ErkJggg==)|Rename File | Changes the name of a file located by a specified path to new_name  |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAATVQTFRF/////4CA/1VV/21t7m9e8HFi7+rf7XBi7nBj7XFg7nBh5eHQ7XJh7XFh7XFi7uve7+LT3dnI7HFh7XFh7XFh7nFi7XFi7oJy7XFh7XFh7XFh1dC719C719K919K+2NTA2tXB2tXC29fE3NjF3djG39rI4NvJ4dPB4d3L497O5N/P5ODQ5uLS5+PT6OPU6OTV6ZSE6eXW6ubX6+fZ7JCA7XFh7XJi7XRk7XVl7Xdn7X1t7YR07YZ37Yt87ejb7enc7nhp7npr7paH7puM7qWW7q2e7rCi7rqs7sGz7urc7urd735w739w74Fz74R279HE79PF79XI7+bZ7+rd7+vd7+ve8IV38Ih68It+8ZGE8ZKG8paK8paL86SZ9Kui9bGo9rau+MfB+c/J/vTz/vX0/vj3////q6XFbwAAABt0Uk5TAAIDBx4iMDlLb3aHi5maqK2vwMLIzNnu8vr9USbcyAAAARJJREFUOE+l0ddSwkAUgOEgir13scSOLZb4xy7Yjb2wiiKiQnz/R/ACEzZm4zj4X39zzs5ZLSZ+lGzXfAVB3C8UwC9UwCeUQBZqIIkQUBYxIYSwx3Rd10dNIYSwx0s1+iYsG4ZhLPomtYatqBDMz8mZAWBPTsgtVLDi38AejsvNBickd+XSf1hxd9P2GzjZtqCnocoDZ4kpqelVSnVVuyA9k5Bawq0zolpxCnsvwPM51KvAPlwU8+ScR+h2gblSbhPIFD6cLNAf/T7UyJDXoAXw9vkOQI1ixRaQc14LeaAvogAH8OBkyRSfoEP1yGuL9SvgMgV1ykseeXdoUZ/6/ngNgIGmaNhf3B7ubPQ212qapn0BM+fidWEezeYAAAAASUVORK5CYII=)|Remove File | Removes the file with a specified pathname. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAANtQTFRF////K6pVIK9gIK9g7+rf5eHQ7uve3dnIyeDGIa5eJK9gJK9hJq9hJrBiJ7BhJ7BiKLFjK7FlLbJnMbRpNbVtObdwPLhyQbp1Rrt5R7x6g9Klh9SoiNOpkNevnNu3s+PIuOXMuubNwejSze3a0+/f1O/g1dC71ePO1uTO19K919K+2NTA2tXB2tXC29fE3NjF3djG39rI4NvJ4PTp4d3L4fTq497O5N/P5ODQ5uLS5vbt5+PT6OPU6OTV6eXW6ubX6+fZ6/jw6/jx7ejb7enc7urc7urd7+vd7+veQ+YvegAAAAl0Uk5TAAYgMDCHqK+zA//U2wAAAMhJREFUOE+l0NcSgjAQQFEUG/beFSv2jr2hgvj/X2QIzrgxBEe8DwwPZ3aTcJ7HR6qfI6KBRAoLQAorQAhLAIU1AIIB3gIDbTxEjRT8PzHzEhNOB9SRmORjrXAIthuYQgFtNoXtHaz4G2h9CbamJ6g3mP77CrJuxyjgNnKZ4C7PQWEBlckbX4E3gb6SQRgURQjIYk6AcgZFaaANeiB0hiAGIeaKcj2CQKXGBKlWoyRWLwX2IZPNxXKXs7tFon3N2l8znv7yDq/4J0l2t8Q30wM1AAAAAElFTkSuQmCC)|Move File | Moves a file with a specified path to a new location. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeCAAAHggFwQHG1AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAWhQTFRF////////////gIC/gI/PhJXKg5vJh5bLhpnMiJjJ7+zd7uvdhZbKhZfKh5fLhpfM7uzdiprMhpbMhpfLhpjMhpjLh5fM5eHQiZrM7+ve6+jd7+veipzN39rJjZ7P3NfFi53Pi53Oi5zOrbXShpfMhpfKhpfLlKXTiJrMkKHRi53OiJnMo7bcm6vWiJnMprreiZrMjJzNjp7Ojp/PkaLQlqjTmKnUnKnQn6vNoa3Mo7bcprneqLjdq7/ircLjsL/gsbrTs8jntcrotrvMucDUuc/ru9HsvNLtwMbWwdjwxdbtxsrXx9ftyN/0ys3UyuD1zdDYzeX3ztHYz+f40Oj50ej50uDx1dC719K919K+2tXB3e763/D74NvJ4NzK4dzL4t3M497O49/O4+Hc4/L85eDQ5ePc5uHS5uLS5+LT6OPU6OTV6Obd6eXW6fX96vb96+fZ7Oja7enc7ere7urc7urd7ure7+velq3F9wAAADB0Uk5TAAECBBAdISIoL1JaXGBseHh+gYmLjZ+fprCywMjKztTY2tzc5Ont8vT19/j7/P7+MsgC3wAAAQZJREFUOI1jkC5HA7JMDCgAQ0GkPBMBBeGoKrAoQFWBTQGKCqwKkFVgV4CkAqwgLgIEUsEK4mPBQBxFQUkhCJQiGySJ0wryFKTHIoNMTAXZicgglxZuKMxCBoWYChKikEESMVYUS+FTUOZhbqCnIMiMS0Gauamrr7+PriIrWmTBgIVVcEhoSn6evRwjTEFRARLwMwkEyefnR2vyYLXCwRYiHxNiJ4FVgbkrVD7ETQmmIAM5riwdofIhTjIwBVkJSMDZBiofoiOK1YpkwzCIvKc2G/Zw8Db2Asm7a4ngCskAIzNrfXUNMTVOXHGRE+SizMvCwKfKQSA98KuwM3ALYAdc4JgSEgYAAoU+jTu4WA0AAAAASUVORK5CYII=)|File Exists | Checks whether a file with the given path exists. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeCAAAHggFwQHG1AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAaFQTFRF////AP//////Var/VarVTp3YRKLdRqLYSaHbSJ/b8OreSaDcSaDdSKHbR6DcSJ/c7uzd3+XdSKHc5eHQSKDcSJ/c7+veSKDc7uzegLrdSKDc39rJSaDc3NfFkcHdY6zcSKDcTaPcSaHdSqHdS6LdSKDcSaDcSqHcS6LdTaPcTqPdUqXeVKbfVqjfV6jfWangXavhXqrcXqzhX6zhY67iZrDiabHjaq7YbLPkbbPkbrHcbrTkb7XkcLXldrLWebrmerrmfLznfbzng7/phsHpicLqi8Tqjb/djcTrjsXrkMDclMjslcnslsrtmMrtmsvtnMbdn8fdqdPxq9XxrNXxrtbysM/dstjzs9nztNnztdnytdrzttr0t9v0udz0utz0vN71weD2wtfdwuH2xuP3x9vhyeT3yeT4y9vey+X4zOb4z+j50OXy1dC719K919K+2tXB3dvN39rI4NvJ4NzK4dzL4t3M497O49/O5Obe5eDQ5eHR5uHS5uLS5urm6OPU6OTU6OTV6eXW6une6+fZ7Oja7enc7ere7urc7urd7+vecW4iEgAAACV0Uk5TAAECAwYNHiExQFZeaXJzdXh+kp+msLC0uLm+ytPU1djj8PT0902MouoAAAEgSURBVDiNY5DoQgPSTAwoAENBviwTAQW5qCqwKEBVgU0BigqsCpBVYFeApAKsoCQPBKrACkqLwUAYRUFHKwh0IhskhtMK8hRUFyGDWkwFjeXIoIkWbmitRwatmArKCpBBBTXcUJkkx8fJilNBe6CmqZO9kRIPI2pkwUChlUVcdnhISoSBODNUQVsLMvCyznTRU1VVd00z4cdmRYZWiqcqGDjHqbBhURDgFKsBUaAWb8sNUVBTjATsdLRVocDPQwiioKEMCZirwoGHnwgWK9yDs7KyfMEKghz5sSgIC8201AfbYpyuz4lFQXNUYgJYXjfGVYoRW0jmOHgn+9lYuqX4KLNjDeq6VENr7+hIfzMZDmBQcwlgAYKS8ooKorwsQHkAgUdq5YOagO0AAAAASUVORK5CYII=)|Copy File | Copies a file from a location specified by old_path to a new location.  |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeCAAAHggFwQHG1AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAARpQTFRF////gID/qqr/gL//n7/fVVWOjsbjUGCA8+jcVWCAa3OU6OjY7+rf7e3fu76+j7nikbni493Mkrngkbvh7uzdkbrikbrhkbrhkLrihYydVWCAVWCAkbrhkrvh5+PTkbrh4dzKVWCBVmGCV2KCkbri19K9VWCAWGODWWSDi7LYkbrhlbzhmb7hm7/hncDhn8HhpKewqMbgsMXXus/gwNLgwtTf0dvf1dC719K919K+19O+2NO+2N/f2dTA2tXB2tbC29bD2+Hf3uLf39rI39vJ3+Pf4NvJ4NzK4d7V4t3M497N497O49/O5N/P5eHR5ebe6OPU6OTV6eXW6+fZ6+jc7OfZ7OjZ7Oja7ejb7enb7enc7urc7urd7+ve9Z348AAAACZ0Uk5TAAIDBAgJCRAWGB8hMDhLUFhaW3h4lKKrrbzg6O7v8/T3+Pz9/f7mJ3I+AAAA/ElEQVQ4jWPgiUUDcoIMKABDgZ+qIAEF5qgqsChAVYFNAYoKrAqQVWBXgKQCrCDS2gIIbKNB7CA3MFDgRjEhHAQiUUzixWUFeQqi3JyRgEskhoIYX28k4BNDAzfEBgYggUBMBREOdkjAPpyAFSEeIMDHCQTsWBUYaKgDgbKSkpKiFCt2RxprQQAL3A1WFkjAMtwUIi/DCHdDWDASCI11gigQwx0OemAF/LgV2OgA5UWZEZHl7oYE3IGR5W8oK4QcWd6eSMALGFmu+irC+OLCTBtohQQbbgW6YEcK4FTgCPGmOE4FJhAF8ky4IstIEwK4gJHFIYIBJNXgQJoVAEDK+Bh97JvfAAAAAElFTkSuQmCC)|Wait For File | Waits for a file to be created and then opens it. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAGxQTFRF////d4i7QFBgcIC/Tlp2VmKJXpGKarCea7WgUnJ5cpS5aXerRExjccKpRlRncoG8QkphccOpQkpgT1Zra3GCccOpc4O/dXuKmqXMo6zPs7vVvMLYwcfazM/d0tXf1Nfg2dvi3t/j4+Pl5ubmy3bLFgAAABJ0Uk5TAA8QEMDAwMbKzdTa2+ns9/j+a68FFAAAAHpJREFUOE/t08cOhDAMRdEMbegMpgy9/v8/omyAhIQnseauj2R7YcZQxtHHVMToyC4VncEvAIDCBACy/EsiILeQk0AcAUBeCgA5X7ELkHvBc5D99zIlyNe9XAP6quqWetSDqWmGtZ1vAW+6G8HrtQAsCc8Uw8AAoednGxKCQxnLbH7rAAAAAElFTkSuQmCC)|Write List To File | Write the contents of a list to a specified .txt file. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAGxQTFRF////d4i7QFBgcIC/Tlp2VmKJXpGKarCea7WgUnJ5cpS5aXerRExjccKpRlRncoG8QkphccOpQkpgT1Zra3GCccOpc4O/dXuKmqXMo6zPs7vVvMLYwcfazM/d0tXf1Nfg2dvi3t/j4+Pl5ubmy3bLFgAAABJ0Uk5TAA8QEMDAwMbKzdTa2+ns9/j+a68FFAAAAHpJREFUOE/t08cOhDAMRdEMbegMpgy9/v8/omyAhIQnseauj2R7YcZQxtHHVMToyC4VncEvAIDCBACy/EsiILeQk0AcAUBeCgA5X7ELkHvBc5D99zIlyNe9XAP6quqWetSDqWmGtZ1vAW+6G8HrtQAsCc8Uw8AAoednGxKCQxnLbH7rAAAAAElFTkSuQmCC)|Write File To List | Returns the contents of a specified .txt file as a list. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAd1AAAHdQEjKi9uAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAANtQTFRF////YGCAQEBQVV6AV2OASFFmPERQVGCAT1dyYo2CZJSDVWCAX3+CVmCAYISCbLSFbLaERE1gRExeQktcaquFTFZva6yEVWCAb72FcL6GbriGbrmFPURRVF18ccKGVF9/VWCAccGGPURRVWCAVWGAVmKAWGuBWWyBWW6BWnGBYIaCYIeCYYuDYo2DYo+DY5KDZJSDZJaDaaeEaqmEaqqEbriFb72GcL6GcMCGcMGGccKGccOGd8aLeMaMeceNeseOfMePfsmRf8mShsyY9Pr29vv3+v37+/37////mBh8MwAAACJ0Uk5TAAgQHiw8QEBeYGl4j5KVsbW/wMHIysvS2Nvj5uvr9vf3+WM4ONIAAADESURBVDiN3dPHDoJAEIBhbKBi772tXVEUUWRVBBvv/0RmOBggQ/bAzf8wl/myGzaB40JHfg3iDEDqEQYgWRYgSd5f1Au6nZEv3gtIlQVImQX6xZKnhB/4E/4aTLd7VZHngWB5pJC2DgAr2F5hSCiYnWD3vMAZKQzIzvm2ATOPAcUFGhhQ6e1lQx+L9jBwoNQwTfth3iltYmDnuqKAgYUGqzd8p55G30ECYMGQ8Ycab87OLbo8ETgRLVNpDdu1nCjGwv/cX6d2dbbN5MFoAAAAAElFTkSuQmCC)|Make New Folder | Creates new folder at the given path |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeWAAAHlgHGqeZtAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAL1QTFRF////VVWqVWqAr9PwV2CAVWGCVGCAPEVSPUVRVGCBR1FnU158VWCAR09kQEhYPURSS1VuVWCAWGODfpSyTVhyZnOTaHaWjqfFVWCAPUVRpsbhVF99VWCAPURRPURRVWCAV2KCV2ODWGSEXWmJXmyLYnCQZXOTZ3eWbn+ec4WkdYmneY6sfZKwf5WzgJWzhp27hp68jqfElbDNlrHOl7PQnLnWn7zZob/cpsXip8bjq8vnrM3pr9HtsNLusdPvC0szVAAAAB50Uk5TAAMMIzg/QFFof6GlsMHGyMjIyczQ0NHa3OXn8Pz9gXxMGwAAAJtJREFUOI3t07UaAjEQhdHgFtx1sMUhOAS57/9YdMu3gWQKWv76FHOLEYIr7hcLfQX0LsWBTpQB1AgzgDJJs0QQUK5nlDdAu8kAqnQZQIVsoPQHMCr+wW9gM2XAFpf12AUmAJ7HxdB+wxkAcN/VbGAFALguSzYwegBQfcfMPXDQngPMcSKlPTsY3GZESleFtFWWUsp6i/vtCAfEC6QbY4axo4E7AAAAAElFTkSuQmCC)|Open Folder | Opens a folder at the given path |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeNAAAHjQEGjt+vAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAOdQTFRF////YGCAUV2AXV1dX19fVWKAVmCAVWCAPUVSVl+AVGCAenyHT1p2VV+APURSPUVRVGCAVl9/W15nc1ZoUl15RExdi09UPkVST1l2UFt3UV15VWCAZGRknUlFPURRVF9+PURRVWCAVmCAW2B+XGaDYGB8YV97YmV4a1lucm96c190fGxnfWxmfnx/goWVnEpGnFtfoUhCoV9Jol1Go0dApJ6esZBpsaWau5JlwFhPwVtTwltTwpxtxW1KyLmsyrus0Y8104gu1pEy11pK2JAw2Mm724op3Ysn3Yso3ZMt4Ywl6dnF8pwhMVoetQAAACB0Uk5TAAgWFjs8SmBkbnCGkZOeoKChrbq9wNjZ2d3i6e709fhDjEOaAAAAt0lEQVQ4y2NgIAS44ICTEasCRQTgJaRAkY2QAmkmAgoURfj40QAHqgJFUQU0wI+mQF6cgAJFSTkCChSlJFAAD4YCNCAw9BUoaynhVaBm7WwgiEeBqpWzpb4YbgXqDraW+iayOBWoO/m4GJkYCjPglvd0dDPWwOVIsLyXuzYub0LldXCFA0IehwIzuDx2BSreNo5eHjq4g1rP1d4CKo9dga65nakmPLLYMYCQDDeCw4olK7EwM5ACABMnbbWUe+PLAAAAAElFTkSuQmCC)|Rename Folder | Changes the name of a folder located by a specified path to new_name  |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAd1AAAHdQEjKi9uAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAPxQTFRF////YGCAQEBQVV6AV2OASFFmPERQVGCAT1dyl2hypWhwVWCAhGZ2VmCAjGd0129l2G5lRE1gRExeQktcyGxpTFZvym1oVWCA5HBj5HBj3W9k3m9kPURRVF1863FhVF9/VWCA6XFhPURRVWCAVmCAWGB/ZmJ9aGJ8a2J8b2N7j2d0kWd0l2dzmmhym2hynmhxomlwpGlwpWlwqGlvwmxqxGxpx21p3G9k3G9l5HBj5XBj6HBi6XFi63Fh7XFh7XNj7XRl7XVl7nho7nxt731v74J074R28Y2A8ZCD8ZKG8pmO85yR86CV86SZ9bSr972198G6/vb1/vf2////lYhKUQAAACJ0Uk5TAAgQHiw8QEBeYGl4j5KVsbW/wMHIysvS2Nvj5uvr9vf3+WM4ONIAAADTSURBVDiN3dPJUsJAGEXhgApKBGdkEBwamRyAKCoSjiI4EBCkef93cQVVSf1UL9hx1t/qVl3LWjm16GLTANRpyABU3ATUdiRY2A9yZ1eBIn6gTkxAHZnA+cGhr60gCBZda1CsP740nfJSUG0B0L4tyOCGeXciKL3y1gd677g7EnCgrz0G0y/Yk0AT8PR4OgJSEngGGM8mAHkJPAED/ac9IC2BB+jpX4b6E/YlUHHp/gDfH3Ri4g73ix0a8lCFmgtAx7mOWrbY7nHmMptM2PbG6uf+B+nvd9E69Zz5AAAAAElFTkSuQmCC)|Remove Folder | Removes the folder with all its contents from a specified pathname. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeWAAAHlgHGqeZtAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAKtQTFRF////IJ9gVWGGVWKDVGGBVGCATml6VWCAIq5eVGCAPUVSPURSPURRVWCAUVt4Rk5kPURSVWCAP0dVVF58UFt3N49sUl17Ul18PUVRVWCAVWCAIa5eOYpuPURRPrhzQ7p3Rrt5S718Tb5+UmV+U2J/VWCAbsqWc8yZe8+gftCihtOnidSpi9Wrltmzl9mzl9m0nty5reHEr+LF5/bu7Pjx7vny8Pr0+P36+f37KfPDEQAAABt0Uk5TAAgVJ2dweYeIiImssLKzwMjIzs/e5efp7vX+JEdy2wAAAJJJREFUOI1jYCAEOOGAnQmrAlUE4CWkQJWFkAJJZgIKVIW5edAAF6oCVX5ZNCCApkBKiIACVTEJAgpUxUVQAB+GAjQgOIIVqMgggCg2BcrSIKCuBqZwKzDQH2AFSnIgBQoKOBXoGcsb6CuaauO2QtfEyNBMG58bdMwtNPE7UksD4khWTMAmjQSwZTZGDiRAMPcDAPdLbmhwE+yVAAAAAElFTkSuQmCC)|Move Folder | Moves a folder from one specified path to a new path. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAeWAAAHlgHGqeZtAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAW5QTFRF////ttv/r8/vVWGGVWKDsdPws9HwVWGBstLwVGGBVGCAWmeGsdPwVWCAVGCAPUVSh567PURSPURRVWCAUVt4l7PQRk5kPURSVWCAP0dVVF58aHaVeY2rUFt3Ul17kKjGUl18lbDNPUVRn73Zr8/rVWCApcThrc7qr9LuVWCAPURRVWCAVmGBVmKCV2KCWGODWGSEWWWEWWWFWmaGW2iHXWmJXWqKXmuKX22MYW6OYnCQY3KRZHKSZHOSZnWUaHiXaXmYa3uaa3ybbH2cbn+eboCecYOicoSic4Wkc4aldYindomod4upeIyqeY2seo6tfJGvfpOxfpSyg5m3hJq4hZy6hp68iqPAi6PBjaXDjabDj6jGj6nGkqzKkq3KlK7MlbDNlrHOl7LPl7PQmLPRmbXSmrbTn7zZoL7bosDdosHdo8Heo8LepcXhpsXip8bjqMfkqMjkqMjlq8zorM3prc7qrs/rrtDssNLusdPv+pNMsgAAACp0Uk5TAAcQFSc0Q1dmZ3B0dYeIiaGssLKzvcDIyM7P0dve5+fp6+7y9PX2/P3+YwCKVwAAAQFJREFUOMtjYCAE+OCAlxmrAm0EECakQJuTkAJVFgIKtKUEhdAAP6oCbTEtNCCOpkBTkoACbTklAgq0FWRRgAiGAjQgMbQVGFvgU2ASnl1RXhRvh0uBa0Gsg6G+U0hJoA5WBbalbpbRufkRTvbJRtgU6KYHOJRVAkGFh5GZNBYFznkGBSD5vLQkczN5LAqCwrxA8pWR1tbWjspYFMQUllTCgToWBaGJwcHBUWDpdDc1LAo8/HV8/MPACvwCFbEoMPXV9qwAy6cZ58hgCwdrb2ufTKAvo0ziErCHpFexu56Vi6lNapa5BAMXNiCgUpoSk6Ehys3FjiNLM7Jy8LAxMRADAFwboghkvrTsAAAAAElFTkSuQmCC)|Empty Folder | Removes all the folders and files from a given directory. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAd1AAAHdQEjKi9uAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAASZQTFRF////SW2SN0lJU1+CO0RSSFFmPERQVGCATld0VWCAjanGVF+Af5WyRE1gRExeQkpbTFVurc/rVWCAUl17PURRVF9+VWCAVWCAPURRVWCAVmGBWGSDWGSEWWWFW2iHXWmJYW6OYnGQZHKSZHOSZXSUaHiYaXmYbH2cbn+ecoSidIeleIuqeo6seo6tfZKwgJWzgJa0hp67jKTCkKnGkavIla/Mob7aob/bo8HdpMLep8biq8vnrMvnrMzorM3pr8/qr9DssNDrsNDssNHssdHssdLtsdLus9HrttTtttXuutfvv9zzwdzywd70x+L2yOL2yeL1yuT3y+P1y+X3y+X4zOT2zeb4zub4z+f5z+j50Oj50en50un50+j42e365vT86PX96vb91hQwQgAAABh0Uk5TAAcOKzg8QEBYeHmOn7/AwcnL0ejt9vf+KYdyqAAAANBJREFUOI1jYKAYSMKBGDMBBZJCjAQUSHITUiDOwYIOmFAUSAqLSKABNlQFkgKEFEjyE1IgysuHAljRFaAD9iGsQMXEysHcUBanAgMHb/+QUB8bVRwKNJ2Do6LiEhNj7eWwKpC28wPLJ8Z7GWNVoOoIlY8JtMaqQMcDKh8V6SaPTYGWO1Q+KtxNBpsCRdcEiHyUnxV2X5gFQOQjXHSxK1BwDooGyod5WuIKKCULRy9fDydTa21cQS2loW+kpyypZqtFILLU7bgYOPECHkHKMzcADGFkClIg2mAAAAAASUVORK5CYII=)|Folder Exists | Checks whether the folder with a given path exists.  |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAd1AAAHdQEjKi9uAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAVZQTFRF////gICAs8zmVWqAWGGEQEhQr8/vVWCAsNXxT1h1VWGCbYKePERQVGCAVWCAVl+Agpq4hqC+mbPRPkRSTldxpMLfqMjjpMLeVWCASVFpTVdxTllyPkVTrMzoq8zors/rUVt4VWCAr9HtPURQsNHtVV9+sNPuPURRVWCAVmGBV2KCV2ODWGODWGSEWWWEWWWFWmeHW2eHW2iIXGmIXWqKXmuLX2yMX22NYG6NYnCPY3GQY3GRaHiXaHiYanuabHybbX6dbn+eb4Cfb4Ggc4WkdIemd4qpd4upeo6te5CufZKwfZOxfpOygpm3hJu5hZy5hZy6iaC+iaG/iqLAi6PBi6TBi6TCjaXDjabEj6jGkKrHkqzKkq3KlrHOmLTRmrbTnLnWnrvXnrvYocDco8LepMPgpsXip8fjqMjlqcnlq8voq8zorM7qrc7rrs/rrs/sr9DssdPvjMtU3wAAACd0Uk5TAAIKDB0gIDA3PT8/QEBIVmhudYCQsLCzv8PQ0tbX2trf7u/09fr9naOAwgAAAPZJREFUOMtjYCAE+OCAC7sCDQTgJ6RAkYWAAg0JRgIKNESE0QErqgJVGXU0wIOqQENBmYACDUlCCjSkpVAAJ4YCNMA7tBXoW+BToBuQXJCdFWePS4FNSqyttoalZ1awFlYFxpleJl4JeUlupon+WBVEB+mnFoJAqGWOABYFBgWmIYUQ4BwgikWBQ64fVL4w0kkWiwLPQjhIMlfBosAxztXV1QOsIMpRDosCozAN98BwsAIXX3FsvvDUNE0Dy8eYZQtiU2Do7GMdll6Y6m0UH4w9JK0yIux0DAxd0mP0eBnYsQFuMaX8NDV5IXZ2ZpyZmo2DiYEoAAC7OpYyby+8cQAAAABJRU5ErkJggg==)|Copy Folder | Copies a folder located by old pathname to a new location specified by new pathname. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAfpAAAH6QGUejxAAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAASBQTFRF////29vb6+vi5eXTsra76Ojg6enf6urfpKiykpin4uLX3dzQ6eng3NrOanSNVWCAVmGBWWSDX2mHYGqIYmyKZW+MZnCMZnCNZ3GNanOPbHaRc3yWd4CZeICaeoOcfYWefoabgoqihY2kho6kho6lipGnjJOpjparkJeslZywmJ+ypKq7pau8rbLCsLXEsrfFwMTQyL24yb65yb+6ysC7y8G7y8G8y87YzMK8zMO9zM/ZzcS+z8bA0MfB0NPc0cnD0svF1c7I1c/I1tDJ1tjg2NLL2dTN2dfK29bO29bP29rN3NjQ3dnR39vT4N3V4N/U4d7W4eDW4t/X4uTq4+HY4+HZ5OLa5OPa5eTb5efs5ujt5+bd6Ofe6Ojf6eng6+zw8RAhTwAAAA90Uk5TAA4aHThCR0htfNnr7PP7HqL7KAAAARBJREFUOI2l0OlOAjEUBeAquwsF9xV1BNdRrICgVRBQQJaiguO44fu/BZ2BxNuZTkPi+dM0/ZJ7bhFCaHpu4MiMD8EEne+D7rwgQm5QFwQENWMEBAFAI1fpjwAUAJQyt50xAAIA47r1xY+XppXZKTcghDT+bgFJScrAJeQG9LLQVgJWqJlKUM3eP/8HfDM+ghnewCCU0mxVBawpCmCSV1IpPypK3j29m7k3BWBXNFNWrvnTAf8kA2ImBuFdj4THIII9EhHBpq7r26uH+OQ0FZOCNU373EsU8cfBeVoKMD6+wBZY3niQg5Xeog3Obo7kIJ/ENthfkpfUfnlJe4THFryktr6whXfiTuCPyr8h6uePQ7tsxuGhDl24AAAAAElFTkSuQmCC)|Zip Folder | Zips a folder specified by folder_path.  |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAfpAAAH6QGUejxAAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAASBQTFRF////29vb6+vi5eXTsra76Ojg6enf6urfpKiykpin4uLX3dzQ6eng3NrOanSNVWCAVmGBWWSDX2mHYGqIYmyKZW+MZnCMZnCNZ3GNanOPbHaRc3yWd4CZeICaeoOcfYWefoabgoqihY2kho6kho6lipGnjJOpjparkJeslZywmJ+ypKq7pau8rbLCsLXEsrfFwMTQyL24yb65yb+6ysC7y8G7y8G8y87YzMK8zMO9zM/ZzcS+z8bA0MfB0NPc0cnD0svF1c7I1c/I1tDJ1tjg2NLL2dTN2dfK29bO29bP29rN3NjQ3dnR39vT4N3V4N/U4d7W4eDW4t/X4uTq4+HY4+HZ5OLa5OPa5eTb5efs5ujt5+bd6Ofe6Ojf6eng6+zw8RAhTwAAAA90Uk5TAA4aHThCR0htfNnr7PP7HqL7KAAAARBJREFUOI2l0OlOAjEUBeAquwsF9xV1BNdRrICgVRBQQJaiguO44fu/BZ2BxNuZTkPi+dM0/ZJ7bhFCaHpu4MiMD8EEne+D7rwgQm5QFwQENWMEBAFAI1fpjwAUAJQyt50xAAIA47r1xY+XppXZKTcghDT+bgFJScrAJeQG9LLQVgJWqJlKUM3eP/8HfDM+ghnewCCU0mxVBawpCmCSV1IpPypK3j29m7k3BWBXNFNWrvnTAf8kA2ImBuFdj4THIII9EhHBpq7r26uH+OQ0FZOCNU373EsU8cfBeVoKMD6+wBZY3niQg5Xeog3Obo7kIJ/ENthfkpfUfnlJe4THFryktr6whXfiTuCPyr8h6uePQ7tsxuGhDl24AAAAAElFTkSuQmCC)|UnZip Folder | Zips a folder specified by path and stores it at new_path.  |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAd1AAAHdQEjKi9uAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAOdQTFRF////gICAWGGEQEhQv7/HvsTKVWCAT1h1VWGCPERQVGCAVWCAvMPGVl+AjJWmPkRSTldxrbS8u8HGq7O8VWCASVFpTVdxTllyPkVTuL7EUVt4vMXKVWCAvsbMPURQv8fNVV9+PURRVWCAVmGBVmKBV2OCXGeHYGyLYm6MY2+OZnCManeUcoGddIKedYOfeYKZg4yghpawiJiyjZ63mavDm63FnK/GoKezobTLpKy4pa25pq+6p7vRqLzSqr7UrMHWsMTZscDQs8fcutDkvc3bvdPmvtTnxdzuxt3vydvoz+b40Of50Oj5QlUYKAAAACF0Uk5TAAIdICArMD0/QEBISFZqgJCZpau/w9DS1tnf7e7x9Pb6R7AY+QAAALpJREFUOI3V09UOwjAUgOHh7jpsUFyHD3cdff/ngbXJyEbPes1/2y9pT5MjCLwCel42QN9CPFCwcwBK2jgARSPmHEZQzlZM+YwA5UocgFI8gDJpQ54fYMr/v2CoLNeklZJggo58fJIuchi4YoNJZ/ANYwpmIGi9COjDUyy081PNYsyJiud1q39obA9tZAG6N4wfAxhU79ob1CYIenTMEQimFOxBsKPg+gFuRjExL5GKYpy5js6gnou7/W+FPXVTiaPZUAAAAABJRU5ErkJggg==)|Wait For Folder | Waits for a folder to be created and then opens it. |
|**Image Operations**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAO1QTFRF////AAAAAACA///MOTlVQCtV7+/fOi5RQDVK5dzKOjFKgHmGPTROPTJNPTJLPDFMPjJMRz5VPjJMPTJMPTFM7uvePDJMPzRO4d7N4NvKPTJM2dXBPTJNPTJMPTJMQDZPQTZPSD5VVUtfV01hZVttdm17hHuGhX2HkouSlY2UpqCis62tuLKxx8G91dC71tHE1tHJ19K92dXB2dXM2tXB29bC3NjF3djG3tnH4NvJ4NvK4dzL4d3L4t7N497O49/U5ODQ5eDQ5+LT5+PT6OPU6OTU6ubX6uba7Ofb7Oja7ejb7enc7urc7urd7+ve8M8MaQAAAB50Uk5TAAECBQkMEBYYHR8mO2BwcoCEnZ6/yNfc4OTn8/3+6DSEYQAAAM5JREFUOE+l0OUOgzAUhmFmzN2tc3d35sKE+7+cAcuS07WFhL1/edIvHI6LSj8lnBwWAeZpXJCgiwsKwAUNYIIKoKADIFQgjJUEFQhTtaQFAvGkJGIv8awJY+Cygx1JsJ/BlgYm/gerLmxIgtcd9jQwoQsOC9iGBOc1rNe66kwUC7WOJmgghEpBFwCPC0zsI6VsxGv7gvUANpHKqkj5rKzfbMqfM34r+w7bPMrFQyaNQ1VQ1R0Lm9mgnRvxjo+gg1tdvoMjFmAC6aUcyu7h3hgM0xOjQKpIAAAAAElFTkSuQmCC)|Open Image | Opens an image with the given path. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAdiAAAHYgE4epnbAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAg1QTFRF////gP//v7//s8zmUGBwZnOMsdP0rdbrrdHtVVtzstXtVGGAsdTustPwZ3WVstTuU11zsNLvsdPuU196sdPvsdTvsdLvsdPvYG6Nj6nGstPvsdPwstPvsdPvsdPvhIybgYmYYmx+kaK3V2KClrHPY3GRsdPvWmaHEaCFEp+FE56EE56FFJ2EFZyEF5qDF6KJJriZJrmZJ7iZKJqIKJuJKLWYKZqIKrGWLIZ+LqqTLrCWL6+WMIF9MaSQM358NZuMNaydNnx7OXl6O3d6O5CIPnN5PoWDP3N5QYSDQoGCQ294Rnl+RqiZR2t3S3F7TGZ1Tml4TrSuU190U2F0VF5zVV9zVWCAWmJyWmaGWmeHW2eHXGmJXWmJX2yMX22NYG6NYnCQY2lxZXSKZXSUZnaVZ3aVaXmYa36Ma73AbH2cbX6dbnJvboCecIGgcIKhcXmLcoSjdIemeIyqeY2seo6te4+uf5SygJWzgMPPgYBsgcTPgpi2hp27hp68iaG/i8fWjqjFkYxpkarIkqzKk67LlrLPl7LPl7PQmbXSmrbTnrvYnrzYns3jn7zZob/bocDcoszkpMPgpcThpcXhpsXip8biqMjlqsvnrc7qrc7rr9DssKNksNHtsNLusdPvs9LftNTu2N3g2+jw3MRe3ODj4ufp4+ru5urs5u3x5+zt6Ozu6u7v7PDx8NNa89Va5YyJKwAAACh0Uk5TAAIEChAUFxkcKis6O1ZZWWh+ipmjsLHAwcTM1+3w8/T1+Pj5+vz8/u53oN8AAAFvSURBVDjLY2AgBATwAk4GhhAFedxAUQCoYOka3EAerGDlkoXYwWqoguX5IdjBQiQF4Y2N4fgUhC5et25xKB4FleuAoBKPgmyQgmx8bpi9du1shIw/poKQxESEvJ2uF6YCJOCkoaHljlVBEJh01dTQ0NB0xqIgwNITSHppa4CBI4YCP3NDQ88QXx0NKLBBU+BtaggEbnoacGCBosDDyBAMTCCSDhn1PVXzVyAUuBjCgDFQWj9jenVOSmnzAiVhiIJge0NDZBUVrdGFTR1lCbl9ymAF6bZI8oYGZoG9Ue3zgGBuXpw6B0iBjxUKsJ6QWQeSnzG5PyFSCKhgFRpYNjVyJkhBS2RkZLw4ljS5aE7XPDiQZcBMaUmTaoAALD2xQJqBBQOwqoRllZSAFZQXi2DLS5Jh8dPA8t2RvbzYFPCpFqW2z5o3tyGmQQxrbuSWkKmNjUiLSO6UYsORYdlF1Sa2TZETZMKdp5l5+LkYGYgBADJKK9c+ssxkAAAAAElFTkSuQmCC)|Rotate Image | Rotate an image over a specified angle. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAEhQTFRFF0RhGUZjHUtoH01qIE5sK1p5NmeHN2iIPG6ORXeYUIOlW5CzbaXJda3Sdq/UeLHWebLXerPYerPZgrzihb/mkc30ltL6mtf/hxWUFwAAAJlJREFUOMvN0+sKwyAMBeCj1cVL66xT+/5vOgrbKBk1YzBYfil8oMYTbEKB7dd1DJoxbQgCEEagKkDVAXDaWu3OQUIkikinIPtO1C/X0TOJhD78DqTMQU4HUB08Bx6uPkALSsfOQY9ahbaDmwEsPWuaXksLmPIJEI+QL7nXMnMwL3/3F8fA+Px95MTQyrEXB0ceva0UoQ9vdQftaE/zVb4YBQAAAABJRU5ErkJggg==)|Resize Image | Resizes an image. The new size is entered with a tuple of the form: (width, height) |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAEhQTFRFF0RhGUZjHUtoH01qIE5sK1p5NmeHN2iIPG6ORXeYUIOlW5CzbaXJda3Sdq/UeLHWebLXerPYerPZgrzihb/mkc30ltL6mtf/hxWUFwAAAJlJREFUOMvN0+sKwyAMBeCj1cVL66xT+/5vOgrbKBk1YzBYfil8oMYTbEKB7dd1DJoxbQgCEEagKkDVAXDaWu3OQUIkikinIPtO1C/X0TOJhD78DqTMQU4HUB08Bx6uPkALSsfOQY9ahbaDmwEsPWuaXksLmPIJEI+QL7nXMnMwL3/3F8fA+Px95MTQyrEXB0ceva0UoQ9vdQftaE/zVb4YBQAAAABJRU5ErkJggg==)|Image Size | Returns the pixel-size of an entered image in a message box. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAEhQTFRFF0RhGUZjHUtoH01qIE5sK1p5NmeHN2iIPG6ORXeYUIOlW5CzbaXJda3Sdq/UeLHWebLXerPYerPZgrzihb/mkc30ltL6mtf/hxWUFwAAAJlJREFUOMvN0+sKwyAMBeCj1cVL66xT+/5vOgrbKBk1YzBYfil8oMYTbEKB7dd1DJoxbQgCEEagKkDVAXDaWu3OQUIkikinIPtO1C/X0TOJhD78DqTMQU4HUB08Bx6uPkALSsfOQY9ahbaDmwEsPWuaXksLmPIJEI+QL7nXMnMwL3/3F8fA+Px95MTQyrEXB0ceva0UoQ9vdQftaE/zVb4YBQAAAABJRU5ErkJggg==)|Crop Image | Crops an image to a region specified by the box argument. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAkZQTFRF////AAAAAAAAgICAAEBAQEBAVVVVAAAAAAAAAAAATWZmAAAAVVVVAAAAAAAAWVlZAAAAUlJaVVVVAAAAUFdXAAAAAAAAVVtbAAAAAAAAAAAAE1dIAAAAAAAAUVFUAAAATlBTAAADAAMDAAADAAMDAwMDTk5RAAAATE9RAgICS01QTU1RAgICAgIES01PAAAAEExASExMSEpMR0tLR0lNRkhLRUdKREdJREZJAwMFAwUHQ0VIAwMFBQUIAwMFBQUIQkRFQENFQUJFBAQGBAYJP0JDAwQGBAYHDUI3BAQFBQUIPD4/BAUHBQcJOTo9BAQGBQYIBAUGBQYIAwUGBQYIAwMEBAQILC0uKSssAwMFBAUIJicoAwMEBAQGJCYnISIjHh8fHh8gAgIDAwMFHR4fAgIDAwMFBgcKCQoQCgsQDxAYEhUbFRggGBwoHBwdHSEwAgMDAwQFBgcJCAkMCAkOCwwTGBskGRwlGhscGxwdICU2ISY4AAABAAEBAgIDAwMEBQYHBwcKBwgLCQoPGRoaHB8pJSo+AgIDAwMEAwMFBAQGGBkZFhcXHB8pJSo+Jyw6NDtWKzFAOkJgLTNFLjRHPUZmPkhpCgsLDA0NMTdKQktuAAAAAQEBAwMDBQYGBgYGNDpONTxQP0deQUlhQkpjQ0xlRk9qRlB0SFJ3S1RwTFZzTlh2T1p3UFp4UVt5VF5+VF9/VWB/VWCAVWGNV2SRWWWUW2iXX2yeZXOoZ3asanmwa3qybHuzbXy1cYG8coK+c4K+c4O/2oGVIQAAAJt0Uk5TAAECAgQEBgcJCgoLDA0RFBUfISIjJioqLi81NTxQUldcX19kZGZoa2ttcHF3d3p+f3+GiIySlJeZmpqgo6Ompqanqqurr7Cwsbq6usPDxdXV2trf3+Pj4+fo6Ozt7e7y9PT19fX29vb29vb29vb29vf39/f39/f39/f39/j4+Pj4+Pj4+Pj4+fn5+fn6+vr7+/z8/f39/f7+/v4bhFpOAAABwElEQVQ4jWNgQAYiatbWaiIMOACzUcK8ivDwinkJRszY5OUqW8zYQAw2s5ZKOUx5jRlOrDA2q9MMDQYGBx5kea3pxshc4+na4nMFkQS4us0hDBYWCG3aY5GIrMM1Hsrw8ABZ4W0iFJ3iBxGRBJMRClAF0tIg0jFuft4cPYh0rSqKWyEKGBj4DeNAXlKtYZjd7MKNpABsBQxwOzfOZpi9ozpEDCEGcyQIiAWXrwQq2HNwWqESXNDAAM5ULJiyaS1YwcGtGbYc6Ao4bNKXbIIpOLgrP0gU1QrRwJzVmxAKDu6flCaP7Ej51IkbNiErOHhwc5MVO8yb7JYNizZtQlNwcGdugDBEgbB/9qpNmAoO7puQLAuyQjapf/0mbAoOHlw+W52FRX32gk2bsCvYUmLPaWDAaVe0GKuCA1PrVSDhoFw3eSOmgt1VYRKwcJAILVuDrmBbqTsvIhx43YqXoiqY1amJGt2a7TORFOxti5JCSw8MUpGt62AKtmd58WGmBz7PzGUQBSu6dBmxpQdGnY6FIAV9sTJIiQgpPTAwyMT0AhX4CjDgUsAg4DObQZ8JWQQlyQEBkz4DGkBJtNgA3JswAAAo4vGDvITebwAAAABJRU5ErkJggg==)|Mirror Image Left To Right | Mirrors an image with a given path horizontally. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAklQTFRF////AAAAAAAAgICAAEBAQEBAVVVVAAAAAAAAAAAATWZmAAAAAAAAYGBgAAAAWVlZAAAAUV1dAAAAUFdXU1paAAAAV1deAAAAAAAAAAAAU1hYAAAAE1dIAAAAAAAAUVFUAAAATlBTAAADAAMDAAADAAMDAwMDTk5RAAAATE9RAgICS01QTU1RAgICAgIESkxOAAAAEExASkpOSEpMR0tLRUhKRUdKRkdJREdJAwMFAwUHQ0ZIQ0VIAwMFBQUIAwMFBQUIQENFQUJFBAQGBAYJP0JDAwQGBAYHDUI3PkBDBAQFBQUIBAUHBQcJODk7BAQGBQYIBAUGBQYIAwUGBQYIAwMEBAQILC0uKSssAwMFBAUIJygrJicoAwMEBAQGIiQlICEjISIjHh8fAgIDAwMFHR4eAgIDAwMFBgcKCQoQCgsQDxAYEhUbFRggGBwoHSEwAgMDAwQFBgcJCAkMCAkOCwwTGBskGRwlGhscGxwdICU2ISY4AAABAAEBAgIDAwMEBQYHBwcKBwgLCQoPGRoaHB8pJSo+AgIDAwMEAwMFBAQGGBkZFhcXHB8pJSo+ExMUJyw6NDtWKzFAOkJgLTNFLjRHPUZmPkhpCgsLDA0NMTdKQktuAAAAAQEBAgICBQYGBgYGNDpONTxQP0deQUlhQkpjQ0xlRk9qRlB0SFJ3S1RwTFZzTlh2T1p3UFp4UVt5VF5+VF9/VWB/VWCAVWGNV2SRWWWUW2iXX2yeZXOoZ3asanmwa3qybHuzbXy1cYG8coK+c4K+c4O/uukxCQAAAJx0Uk5TAAECAgQEBgcJCgoLDRARFBUWIiMlJiYqLi8xNTU8UFJXXF9fZGRmaGtrbXBxd3d5fn+DhoiRlJaXmpqcoKOjpqanqqurr7CwsbS6usPDyNXV2trf3+Pj4+fo6Ors7e3w8vL09fX19vb29vb29vb29vf39/f39/f39/f39/j4+Pj4+Pj4+Pj4+fn5+fn6+vr7+/v8/P39/f3+/v7+WGF9DgAAAYNJREFUOMtjYGAwmIMF1EoywAGTb99eNLCzWY0BCQjErTyECqpdGFCAbNcOFPnpIdyoChj0svchyW8rFEeTZ2D0bkPI785UZsAAfFGzYfIH8u1AIhGuXCgqpDu3QxVMDuIACSgmdmujqNAq3QOW35IuChWxmKGJosK96iBQfleTAlzEZKY8sgKesGmHDu3Ps0IScqpkRlYhUb/10MQAdiQR1hZjFEtUS1akCKGImCWhetZhjhyqANt8YRQ+pwZ6+FSoM8h4sBgasnjIYKGBCsJtCCsgaAUysCfgSJWihcn4vClRt2TzBH/cAcUTOmXz5g05llCutSd6ULuVbdq8efPqBmhkxVigRZZW8drNILA4DRzdvAukzFGiW7p92WYImBQISjD6/fE9OshJLnIWVH7zxlxboED03ARTMaRE69W6GQ7WZCgxMAga+aXOc4Qr0M1aj1CweWkBJNmL8MMzTsfyzchgajBqxhGIXbQZFZQ7I8sz+fSuQwOrGpEzL9bsXwPL/gDJJfMYjc+fyAAAAABJRU5ErkJggg==)|Mirror Image Vertically | Mirrors an image with a given path vertically. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAfpAAAH6QGUejxAAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAYZQTFRF////29vb6+vi5eXTm8276Ojg6enf6urf1eXYfseydcSweM22bb+rd8634uLX3dzQ6eng3NrOM6uSFKCFFaCFGKGHGqOIHaSKJrmaJ6iPKKiQKLqbKqmQKrqbK7qcLbucL6uTMryeM7yfN66XOa+YOr6hPbCaQLCZQLGZQcCkQ8CkRsGmR7SfR8GmSbWgSrahTrejT7ikT8OpUbmlVMSqVcSrXceuZMCvZcGvZcixbMqzcsa2c8a2ds23eMi5ecm6fsu8f8+6gcy9g82+iNG9itDCj9LFk9PHmNXJmdbKndjMntfFoNnOpNjHq93TrdrLr9/VsuDXs+DYtOHYt93OuOLau97QvN7QvuXdvuXev+XexeDTx+HUy+LVz+zm0OPX0ePX0ezn0+3o1+Xa2OXa2dfK2uXb29rN4N/U4eDW5Oje5+jf6Ong6ene6enf6eng6ubM6ubP6ufS6ufU6+TC6/f07OO37OS87uCh796V796W8NuD8NyJ8dlz8tdp89Vb89Vc89Vdl1DK2wAAABN0Uk5TAA4aHThCR0hOcXh7fHzZ6+zz+6LlvY4AAAE+SURBVDjLfdD3N8NQFMDxoNSo1Yde0VJae6Qxo2pvitp7FUWNmLWF/9xLRb2XvOT7Q07Ou5/zbk44juPSi2RdBRkcWZZ+Lp8VU8JuBCeUYAFKMAEpNPBwRwFCJMH9h/L9+gfOT9UK00jwrCjK1y29KZME7xgoCRrYSfCE559XFuA68fZykxptGwHVQsWwJVirAui/NAc71YALXhjBetcRfh7UQrLeuB7MVULzsRxrAq3ubBqMqYet++2QKp8E8eDvoed/DnkEiHWCMeKG3UawBCs1YAlmPWAJchrq2eVqwIFMcujAkL9ufNSHkDAZKmWCDVFaDBy626JCn8sMhNG8GO4xW4FBdGqzbElsiYSYYCsgRbwlaGIQSdNGUL4688jjFQi590aWBxg3eDt4xPvUN5fgp7/B5mT/BqcND38AfqfFzITjckMAAAAASUVORK5CYII=)|Image Format | Returns a message box specifying the format of an image. |
|**Windows Applications**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Open Calculator | Open Windows Calculator. |
| ![](data:image/png;base64,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)|Open Paint | Open MS Paint. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAJxQTFRF////MTVEWGSNRE5pQkpgQkpgY3CgUl1/Qkpgb363MDZEQkpgT1dqVFttZW+ObXJ/c4O/eHyGfYGKkpqynaK1yMnIz8qv0Mux1M+21tG52dS92dW+2tW+2ta/3trF39vG39zH4NzH4N3I4d3I4t/L5ODN5OHO5eHO5eLP5+PR5+TS6ebU6ebV6ufW6+jX6+jY7OjY7OnY7enZ7eraccUAvwAAAAp0Uk5TAHjb3ODo6+/4/b2GWfIAAAC2SURBVDhPvc3bDoIwDIBhQERQwKHg+awgzIGK7/9udk4N1i1mN35XTfOnNYwmswtMA7PbXMfzPIsHFgydx8p+Bq7fByEhxGkBB4aQb3z3FUQ3EJOGmG+izyAZNiSS4JtecM2EUhUcJ8JOFcjoBekISfGFE6L9opgJyyor2ByGAgXlRtjXlF22MJS6L6oDUqEgnyK57oufAVshDAV0gVDdFzUVzqogHQtrVSDz1yAYSAXvoKfAgztSE3AT6DJyHQAAAABJRU5ErkJggg==)|Open Notepad | Open Windows Notepad. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAS9QTFRF////VVWqQECAZmaZVVWARl2LS1qHSWGGT2GESmOEUGCAT2GATWGATl2ATWCCUF6AT12CTWCATF6CT2GATl+CTV6AT2CCTV+AT12BTmCATV6ATWCAT2CATl6BT1+BTmCBT16BTl+ATl+ATl+ATl+AT1+ATl6ATl+AT1+ATmCATl+ATV+ATl+ATl+ATl+ATl+ATl5/Tl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+ATl+BTl6ATl+ATl+ATl+ATl+ATl+AT1+ATl+ATl+AXXiaXXmaXXmbX3udYX+hYYChYYCiY4KkcJm8e6zPfK3Qfa7RgLTXgLXYgbXYgrfagrjbhLrdkM7yktL2ltn9ltr+l9v/e8cNfAAAAE10Uk5TAAMEBQYLERUdHyAqMjQ1Njc4OTo7PD1GR0hMUFpfYWVndomkpqytrq+wsbKztLe7w8vP0dXX3d7h4uXm6evs7u/w8fLy8/P09vf9/f5P234UAAAB3ElEQVQ4T22S7VraQBCFh1hQq7VYalRUWtTQxrbSz1gioiFt1NgTpR+gsdYAe//X0N3NRgJkfmXP++aZzUyIeG1bRZqqorWdPC74cKaMpw78BfW8i+aUwXkTu+pg4/HehMH5Xgl2fCigRY/GjSUH5ox2ioI8zaFB44bkRA3MxecjzI4ZSyd4zfksjtQL+9iklPHkBK84p03sK6GCw8LISHjhEJWkZx21XGJwXhM8V0M94TTfxo4yvn9DTRN8B+35B4FWPGV8AAzFvRVK1XNXGls/8DWTE5WEwTk+bWlZnOhZG+8551XJ5ETLp4Le3uJjNqdFF43PuL8X2vFiBj/m83khe3j1CSNfNW3vDG81mnn5BXBL2hucebZZzcdct+R7aK3F81mmtVacWLrkPjph1L/7BX+Vc7zLrfr4+bcfhR343Mhb6A6ZqC6aBhwHRhNdGQy7sPJURWc4uL4MegP2B3xZRQf4zQa94PJ6MOygSgZCdiMa9tg/nPN1F89xx3oiuWEhDDpAxK6wUUbA+nDFpVz0WYDyBq5YhAMllNe5EMW/sc2TAOtlJaRahDCFYPIk1WJ0SXklXjIZXfLhM+OPIppK4kGJsVzoarQXSeLr6VFberKcyUQsa7SaieQ/79yW+3pjKakAAAAASUVORK5CYII=)|Open Snipping Tool | Open Windows Snipping Tool. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAejAAAHowEwL7LFAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAO1QTFRFVWCAVmGBV2KBWWSDWmSDWmaLXGeFXGiOXWmRX2mGYGuHYGuJYWuIYmyJYm2JYm2KY22JY3CeZG6LZnGLZnSkZ3GMZ3GNZ3KOaHaobniTcHqTcnyTdH6XeYOZeYObeoObfIWafYWbfYaagouhho6kh5Cmh5Gsi5axjJWkjJWnkJiqkJq1lZ2vlqC9m6Ounqa2oaiyoamzrLS7r7bDsbi9srm9tbzBt77KuL/Fv8bPwcfMwcjRwsjMw8nNxMvOxs3XzNLV0Nbb1Nnc1drd193f2d7g2d7i3eLm3uPl4ebo4ufp4+jp5err5uvs5+ztbHe1TgAAAN9JREFUOMu909UOwkAQBdAWLUWLFXd3dynu+/+fA8umSZHbN5iXnWTOw9xJluP+VGZB7axWtbOYNEAKqZ3fz155ersO7RgYV+RRYwwS5FleCCoMxCBIX+n8FIDANnmIy4jHKTKDxbwf1YnJBYoF1+cdDLXlsmZgfUj6cqguXa2LgczCyRBkGchCEGcgDoGo0Lki4iVLs/V6VtJJwaeazRSvAzSHegHOaj2oB5IHQs55DPg93f3shiDM0ucgiDBQhkDc0vkxgpdsb25k1zFi4Gj0+i3f+8cRzJpDiZ4ffts7uOgtBiOqjDcAAAAASUVORK5CYII=)|Open Control Panel | Open Windows Control Panel. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAL4SURBVFiFxdVPaBRXHMDx73tvdje7m8TYgrYV71r6B/zTtKhYBNuiUVBjinosVFBEBPEQ6MFScmkPFaW3ngVtPdgY0ZZIFA9iI9RKsV4qFbSCpcb94/x57/16WE1dNTbuzMY5DcwM38+892aeEhFm+lgyONKL5nNsfkDNNGDJ4EgvilPALBSnZxTQFIcJhA/1i4z/PLTmwowApooDtB3wrHjbAf8XbytgOvG2AaYbbwvgeeKZA543nimglXhmgFbjmQDSxFMDVg0eW5Ymngpw8tudX3yz4PC5efm7LccBprcbHh0wYVcyP7D2VefsW/VIr7PWry3rmD/jl2TH1S0rRoc2nm/hPQimunB3/4YeieN9hTfNa/WzbmvwisqVFmvECQUfUtBQ83n+SOYMtRqHp43A+PZcdPvmp1j1WW3MzxWB0lJNddSRm68oLIwQ5wGIdMcPswdOrG81Do+tgXh4XX/8163flahDyjC3vFKjFNQvejpXGZIbQvjLf48UtL2SJg4Pp+DogElK4ZcotefRi8pAeaWmNuapX/SUlnvqZ00j/oZFK/ktLUBzom92UgpPivg9vlaBx6bkIUIpuD8OxXdj7C1DdCXAYS6nBiTo70X8aleZQBBQ6qmI0nsOpSH8NddA/K0pvxxmMALCXle9ZzEGU+7G16u4eqX5LhG8Syi+E08iSsvkGu+fsakBub7jl3SQ32DK3f/4ehVJYkyxE7HJ5Ei4MGqcayYR9roaTxuHB19Bof+nYUmibeKsNV09iLO46gTiLD5JEOuanij2xmKM2p0FoOk/kAyvX+RtNOZqlU5T7gYUrlYBU2hW54KRjk2n1mYBaPoP5PqOX1Iu+cSUu6qN+ERjUT4qVirp8LM+ziL+BAAgv2n0iAnyH7javcby13lwEfgYADHmKzYfqWYFmHIzuv/d6l3i/AFspEDAFFBBcLXYf3phVnF4xnZc7P/xoNKyF2jEjbldlJ63s4zDNLbj8NhHW73zXzubvN615cydrAH/AkZllNlVgvz7AAAAAElFTkSuQmCC)|Open Clean Manager | Open Windows Clean Manager. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAebAAAHmwHPmYv+AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAQJQTFRF////mcz/udHoUV55s9nyVV5xrdHtstHwtNLwr9PwU2BzsNXtVGB0r9PvYG2IU1xzVV50stPvaXmbsNLvVF5zsNTwcICmVF1zanecstLwVF50sdTvcX+msdLusNPusdTvqsrnsdPvsdPvsdPvVF5zVF5zsdPvsdPvVF5zsNPvsdPvsdPvq8voVF5zVF5zsdPvsNHtVF5zVF5zVF5zsdPvMjpFMztGNDxHNT1JN0BMOkNQO0RRPUZUQElYQktbTldqT1ltUFpuUVtvUVtwU1xxU11xVF5zV2J3XWl/Ym6MdIeed4WwhpfLhpy5jqLSj6PSl7LMmrPcn7ngqcjpsNLusdPvR9UxywAAADV0Uk5TAAULExQbHCEiIygqQEBNUFpdYWFkZHB2dneCgoeJi42otLvAzM/a3uDg4eLr7O/z9fj8/f02VUZYAAAAuklEQVQ4y2NgAAJxXTdkoCfFgApYjUDCLpYWVg6WzmAlXKgKeCAaHewd3RwgTH5UBULe6EACVYGYDzqQGVUwqoB6CgKD/PEr8AsN1ZFkw2dFcGhoqImSIBNcAZ8nKvANBQN9YbR8AQceISB5ZV70jONmZ24LYQQA5RUxc5armampE5jlFRoqrSmPocDNxtQawnA3UGdk15KDK2A2hKpwhNLGCqIMDBzasnAVAioayEBVhJsRKMqpxgIkAQ6fpxKgXarXAAAAAElFTkSuQmCC)|Open Dialer | Open Windows Dialer. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAV9QTFRF////SW1tYGBgWV5vRERVRUZXSUlaV1lrV1psWFttWlxuWl1vWl5vW15wW19wXF9xXWFyXmJzX2J0X2N0YGN1Y2d4ZWl6Z2t8aGx9aW1/aW6Aam6Ba2+BbHCBbHCCbnKEbnOFb3KCb3OFcHSGcHWGcXWHc3iJdnuMe4CSfYKTfoOVfoOWgIWWg4mZhYubipCgi5GijpOjkJamkZiokpenkpmpk5qtlpyslp2xl5+ymJ+vmZ+vmqCxnaW4nqW2oKe3o6u+qbHFq7XIrLbJrbXFrbbKsLnNsLrOsbnJsbvPsrrKs7vLtL3Mt8DPuMDQuMLWucHRucLRvMXUwcvfwczgw87hxM3dxM/ixM/jx9LlyNHgyNLlyNPmydTmy9Xky9Xny9bnzNbozNfozdbmzdfmzdfozdfpztjnztnqz9joz9nqz9rq0Nnp0Nrp0Nrq0tvr0tzr0tzs093s1N3t1N7tcMEp+AAAAAR0Uk5TAAcIscJjeQ0AAAGmSURBVDjLhdPpNwJRAAXwJOurVCShFNmV7EsUaZT2rI8WpmQpqhn3/z9UjqN5M9xPb/l9eMu5KlUz3UQm3aqfdBHSL93+Wuj6AWrS1zPQXB3ZCoW2hpujgZ4+ov4FSGvffl27v69d21uCdIJmdJky/Uo5o2vPGTAj0tPBwVMqzigAT40uO53LtOZRAPMCPertPaLCvAIw3uVpKkXzd0YFQBbrxdvbYn2RKAEyGykUIi6iDDojBwxzcwZloN84rwP18w29PLClIbw8PLwISNvkwOQz+Ivj7e3jCx7PkyzQJZE9Gbe63dbxkyySOgasg+dMgQ/gI2DieKwzICNcTvjRin/iUshIwdBbJWgR8bi29gjREqy8DUmAC/zuCrCp0WwCK7s8XBIwDX5vCdjRaHaApT0e0xKgf61wow28+3zvaIxylVe99JAJ8WrqoH3Ig6krMcHcwoty2LTfABr7pnAZXgZoY8idOcwLC2bHWQ4xLfvUYwU83YQPD8M3TyiMyX2WJQqxWixWRUQt7Ge1irMaLwGl+KpMcb6rR7Q2m5aw1fu3vH/V/xOXHm4HxPcQKAAAAABJRU5ErkJggg==)|Open Volume Mixer | Open Windows Volume Mixer. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAehAAAHoQFP0XFMAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAdFQTFRF////AP//gICAVVWqgIC/VVVVgICqcY7GgICzaoC/d4i7cIC/WWaAbYbCdIC5d4C7c4S9dYPBdoO+c4a/V12DcYK+S1dudYW/RlBkcoS/dILAVWGAdIO9V1+DdYO9dIW+bHyxc4O/coS+c4O/VWGBcoK/c4TAcoK/dIPAdIS+VGCAdIO/coO/dIO/RlBlRk9mVWGBdIO/c4LAcoLAdIO+coO+coG8Vl+Ac4O+dIO/dIO/dIK/c4PAVF6AdIPAdIO/c4S/X2uUYGyWXWmRXWqRYG2XYW2ZUVt7XGiPW2eNZHGfTFZySVJrWmWLZHKhWWWLWWaKZ3Skc4O/Z3WnTlh1WGOGVWCAbXuwc4O/SFFoaXirc4O/V2OEZnSmRk9mRk9mbHqvV2GCc4O/c4LAbHuyR1BpbX20bn21bn61coPAVmCBbn+3b3+3c4PAU119c4O/c4O/VmGBb4C5cIC5dIO/cIC5VWGBcIC6c4PAVmCBc4O/VWCBcoG7coG8coK9VV+AcYG7cYG6c4O/U19+VWCAcoPAVWCBc4O/VWCAcoG8coK9Rk9mVWCAc4PAVWCBc4O/Rk9mVWGAc4O/VWCBc4O+VWCARk9mc4O/Rk9mVWCAc4O/YRLwTgAAAJh0Uk5TAAECAwQGBgkKDA8QFBUWHh8lJygpKywwMzg5QkJGRktOUFNUV1xdYGVucHd7gIOEhISJkZaanJ6eo6qssbS1t76/v8DAwMDBwcLCw8TExMXGxsbIysvMzMzNzs/R0dLT1dfY2dve3t/h4eLl5eXm5ufo6Orq7O3t7e7u8PDy8vPz9PT19fX29vf4+Pn5+fr6+/v7/Pz9/v4CLqP4AAABNklEQVQYGdXBhULCABAA0EPFQAW7W1EREyxMMDGwu7s7sVuxW3b3tQ4GDKZ+gO/B/ycKToA/BSSrtL3thfAbaXxWxRbRlKGF4kBAEqMsnSeLmdbxWVp2A55XlEIzYSbOnOFdf0ekAo5HeHrB4Bs5LDa87nUSKxRAFCRXd9yQsw39Aw4tEasPAORr5Gqz2oSfug+yUADLW7lPvN2aS8T1AbJ69gcrSd45cQ51J4jYvU2cMrCTqh+J6LTqABGf6sxkkwQ8WfFx7Q6yFsbIzugJznLRou2IHPLBRQoiXjeSk0hwEYKI5bfEmwRX7iZcYaaHySETBHqwiWG+6s+IY5aBQBH2MwwzGltJVloQyri4Z15yxACpRmKlgVB0FzMSARbSEqIrHxDya84Wg03iqgZ+CgOebyD8I9/m1rRjchq3GQAAAABJRU5ErkJggg==)|Open XPS Viewer | Open Windows XPS Viewer. |
|**Email**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAALzSURBVFiFzZdPSBRhGMZ/78y2+J+CJN0It1r7u26DIGQQepC6BGX0x6PHzOgUanToVmqdIgs6dS3DuhaCRYRBIWULHaQ0aLdCI9BozXb27TBuajMaLq7bcxq+eT6eZ57vfV/mE1Ull/Athyy9mBXj37eZiIWBpaoWEBFl8N3poqMraqDs6pfCvOKCiKliqWKBWJvRMEKBojAvOBUaMxH/YyB460c5NpaJbamKhWAVFBaGSGHM6WTnqHxbbn6/bkCrIyEgWdFZFAaz4rmCkUtxWGYXLIVA+5sMikQe5jgBPbhiCcS7qpYsXznRa5YFd1wSoW3++qoksOFCdEN5cEe/CG0Cv1Q4808DFSVCd72PgSY/A01+uut9VJQs/pHlHcMtIu4m3tgR3WckdQihHiEmKeo+dVb1LGmgNmBw74ifwyGTQJEQKBIOh0zuHfFTG/D2LCo3ytuGnwbaozv/iLdHz6L6WCAg6EDK1uqPV6oGF+zbfGNqQfXm+6D/pJ/1+cL9EZueIRuA1mqTxkqTiYTScGeGRHKhgekPozGUjcCMoJdTGNsFbQIQ5Ep89O15vXvcTvPTXeMqwuawyfp8YXhc6Xgyp9LxJMnWtQaRUqE5bHLzlb1g388f+bvy8qY7VfSUIhfFGd1TIM2xrnAfhD2Tc+W5dzbiR2O2i5xe2+txDF+vhSZj3eHTosZ+4DXwUtCaeFe4z1N5Fq4EKtc5ddQ/lnKR+8dSnKuZ43gh1r37GWAtJTofOR/FLgMj35yabAi6vaXX0pysGHged6I/EDRd5PRampMVA7ejNhMJJVIqdNb52FQsbCp2niOlwkRCuR11F2imcBVhIgnnBpJca1hDY6XT+2lMzjjv/p4BK2oAYDCe4tiDGVqrTWrKnJBefE7RM2TzYXJlf81ckzBTTI+NZrQvx20oD1ftf2Ax/BeDqOefrCxCVNXzYgKEWEZC71uKMjoCWexy6nU1Aw0DBatiwJPsdTlV9iDy8n1L4aGsG8gGfgM1OA5jF9TjyAAAAABJRU5ErkJggg==)|Hotmail send mail | Send an email with a given text and subject with your Hotmail account. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA3QAAAN0BcFOiBwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAALwSURBVFiF7ZdNSFRRFMd/9857M+loM+NX0qJIFCMLKiP7IjLDwIoIXEkGKkJNuRArEkxCKI1qUYQtpEiYhVEQtGhTCzdCC1u0EFy4MAlRRFKbkXE+3m2hlW8+chyVWdTZPe55///vvHPue/cJpRSpDJlS9/8AgFClpbrPoV1EKDdwIHyqimDDNdD19XUKBtGfP8Xy8T3AIEp022dDHuE9WVaHUC+W5xqFOwneaEdl566Lt5ieQn/QgRwZNi8oUS+XKjeFHBnGeuMKcujLms3l0JdFrUhzAKHcwltxMP4+lJJQbSOhc9VJmWvv3qB5esAw4ub8HWApwkdPEHS3gG1TYs4LfvTuR1gG+ldMjdoF4cPHo5IsA/3YWpsQE+MrCoqJcWytTTHNA2XHVgYIttwmWOcGi2YWHhvFdtON/Pwprrn8/AnbTTdibDSiAo25mga+Xooat9jvgfCZCwQ6HqKycswL8z6sXe1or3ph+StcKbRXvVi72mHeZ7pFZeUwef0Ok0crYkPHq8YoLiHw4BnGnn3mBaXQXnuwdrYhfF6Ez4u1sw3ttccMBYR272Xs1j3mthXEs4keQv+bDxEkBlrfS7S3fVEGKn/rokjkbAiB72w145XnQZprLLpaY7o2NzpWSEmoph6jeBf6k/sIn/ePT4yhVPYMphua+F68Z0VpWMW3wCg9tNiSgqK4OeEdhXxr7UzYfFUAACovn8Ddx4RPVUWt+ctPM9rcjt+VvRrJBFoQGbpO8HIzRnEJes8TAGZqG5naf2TVUskBLEW4vBKjoJCZHz7mcvOTlUkeAEBtLyBTKQKzc/gXAklprPlAIoUg1+lgsz09NQC/wpFhJ8fpQAqRGgCANJuVLdkudC3xzq77mVCzWNiS5SR9ky01AABCCLIdm3FmZiQEMLgREACZ6WnkuZxIGbfOQYkS3RsFAGCz6uRnubDqMeZCiW5pnw15UKKeDXwSFoskz+XEnvb7SDeIEvX22ZBH/P83/OcBfgKOKuVWsq6gzAAAAABJRU5ErkJggg==)|Gmail send mail | Send an email with a given text and subject with your Gmail account. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAGFAAABhQFFWZ5CAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAPNQTFRF////bQCSgACfdQufcAqZcQufcw6dcg6ecw6fcg2ecg+fcQ6ecQ6ecQ2ecg6ecg6ecg6ecg6edBKgdhWhdhahdxeheBiieRmjeRqjehujex2kex6kfSGmfiKmgCaogyuqhS6rhjCsijivizmvjTyxjj2xjz+ykEGzmE64mE+4mlK5mlO6pmfCqGrDqm3ErXPHrnXHs37Lv5HTxZzXz63e0K/f1Lbi2b/l28Hm38np4czq4s7r48/s49Ds6Njv6drw6tvx7N7y7eDy8OX09O349u/59vD59/L6+PP6+vb8+/j8/Pn9/fv9/fz+/v3+/v7/////UZtl0gAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAABL0lEQVQ4y4VT53qCQBA8UOkCm5BGTDO9mWK66ZqiiXHe/2kCBxxEJTd/mG9nuL3d22VMQNFMy/E8xzI1hU2iargk4BrVMVnVffoDX1eLesWmCdiVXK/VaQrqNfH/VD1ypGeoNpXATu6hUyl0Xp9fbvDjag36B0bUP94fpAjGDK7CNE6CYPMDo71ID0KOpdShMTMzHwzxMk90NPgCfgZnadRkljjuFGhHn8UbXIQiaDEnT9gG9qnR6beIbl+vkpjDvNwwc41u8/F9N6IPuExiXtFA4ROGve2Y3aOVGQopiHaALU46WMtSWEXDOrDAyd2zuKRZNGwAy5yc52VquTy3egiscHrcFI1SxCg24l6Pvvufs0RvJ6LV0seSP7d0YOQjJx1a+djLF0e+evLlLV//X6kiRqMR0d/8AAAAAElFTkSuQmCC)|Yahoo send mail | Send an email with a given text and subject with your Yahoo account. |
|**Math**|
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Absolute | Calculates the absolute value of an integer or float |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Ceiling | Rounds up an integer or float to the closest number |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Exponential | The exponential of x |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Floor | The floor of x: the largest integer not greater than x |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Log | The natural logarithm of x, for x> 0 |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Maximum | The largest of its arguments: the value closest to positive infinity |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Minimum | The smallest of its arguments: the value closest to negative infinity |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Round | x rounded to n digits from the decimal point. |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Absolute | Calculates the absolute value of an integer or float |
| ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADdAAAA3QFwU6IHAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAchQTFRF////yNDikperyM/ixs/iwcjchYmchImdcXWHx9DiZ2p7W11uXmBxXmFyYWR1YmR1Y2Z3b3KDcHSHcXSGcXWGcnaHc3aHc3eKdnmLdnqLd3uMf4OUgoaYhImbhYmbh4yeio+gio+hjZKkj5askZitkpepkpmvk5iqk5qwlJmrlZqslZyylpyul5yul560maC2mqCym6K4nKO4naS5nqS2nqW6n6W3n6e8oKa3oam+oqi6oqm+oqq/o6u/pKvApqy/p67Bp6/EqK7AqbHFqrLGq7LFrLLFrLPFrLPGrLTIrbXJrrXIrrbKsLfJsLfKsLfMsrnMsrrOs7rOtLvOtLvPtLzQtbzQtr7Qt77SuMDUucHUucHVusDQusDRusHSusHVusLWu8LVu8PXvMPVvMTYvcTWvcXYwMfXwMfbwMjbwcfXwcjbwcnbwcncwsrdwsrew8vew8vfxMzfxc3gxc3hxs7hx8/iytLky9PlzNTlzNTmzcTVzdXmztXlztXnztbnz9blz9bn0Nfn0Nfo0Njp0djp0dnp0tnp0tnq1LfF1dzr1dzs1d3s1t3s17G+197t4Z2n45qk5Zaf83t/83uA9Hh89Xh7/2RkUGE35QAAAAt0Uk5TAGGdr7C05ufx9/j2Bdh2AAABsUlEQVQ4y5XQ1VMCARDH8bNjTeyORexATBQRsbBR7MIWA/Xw1sJWVBDP9t/1wZO5AW8cvq/7efjNMgzDBKbI/iwlkPkpVCZRqADCZDlrGz6t5cjCPKDBdXzDn9l5x5HTeeRwdve651ovGsTglg7cRK5Dur6mw1PEu2pc8g882h385Tl/b3e57PfugSF+peNKDLJmZn2ayRIBiX5BeJxE4QKIBIkiBRCyJVGIAIJJomAP6E9LLeE0qvqdUZVqdKdepeFKUtP6RaAYIH4PEaeaEJumEHEvHqDYH7CQl6ulPl27bVGnW7S16/pIm5u3IAK7avU4zZsmyGoyWWnCNE/javWuCJQDJLKIaG5BbDEjIpsIUO7PBm10VOZ+hbxo3SCXG9aL5BX7mVHRWhH491FtsTHZXKWi1NKjUPRYShWVXHZMbJs/G8oAElhENGsQNWZEZL2Ata5mhCaNY7RtNG7TmHGSvMDJ6+sTDeoN3LJev8wW5ld5g+evrw8WEaebEZu7AGDTF3x6RnYCgMULPLy/vXCNylrrsFI5vJqelGErSEru9YAgqUcFCSAg4u97RADDMN/r39ZZblPymgAAAABJRU5ErkJggg==)|Square root | The square root of x for x > 0 |


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
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
