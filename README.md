![](https://github.com/OakwoodAI/automagica/blob/master/images/logo.png)
# Automagica
Automagica is an open source Smart Robotic Process Automation (SRPA) platform. With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide a comprehensive and consistent wrapper around known and lesser known automation libraries .

![](https://github.com/OakwoodAI/automagica/blob/master/images/automagica_drawing.gif)

Refer to our [website](https://www.automagica.be) for more information, registered users can access the [portal](https://portal.automagica.be). For more info see the [documentation](https://automagica.readthedocs.io).

## Important update!
- We're on PyPi now!
- Follow our [blog](https://blog.automagica.dev) to stay up to date with the latest changes!


## Need expert support?
We can support you end-to-end in all your automation needs, from estimating automation potential for processes to technical implementation and integration. Please send an e-mail to [sales@automagica.be](mailto:sales@automagica.be) for enquiries and rates.

## Getting started

### Prerequisites
1. Python 3.7 from https://www.python.org

### Installation

1. Install the latest version Automagica on your machine:
```
pip install automagica --upgrade
```
2. In order to register your machine with the Automagica portal (sign up for free [here](https://portal.automagica.be)), run the following command: (optional)
```
automagica --login
```
Follow the setup process and Automagica will from then on run in the background and at startup!

### Uninstall procedure
To remove Automagica, run the following commands:
```
automagica --logout
pip uninstall automagica
```


### Importing the activities

Before getting started, don't forget to import the activities from automagica in your python script. If unsure, it is possible to import all the activities for development purposes by starting your script with:
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


### Example code

This is a simple example that opens Notepad and types 'Hello world!'.

```
PressHotkey('win','r')
Wait(seconds=1)
Type(text='notepad', interval_seconds=0)
PressKey('enter')
Wait(seconds=2)
Type(text='Hello world!', interval_seconds=0.15)
```

This is a simple example that opens Chrome and goes to Google.com.

```
browser = ChromeBrowser()
browser.get('https://google.com')
```

For more info and examples see the [documentation](https://automagica.readthedocs.io).

#### Running the other examples
Running the examples is easy:
```
cd examples
dir
cd <example-name>
automagica -f app.py
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

## Automagica with Natural Language

Wouldn't it be cool if we could write Robotic Process Automation scripts in plain ol' English rather than the already easy Python scripting language? Well it's possible with Automagica! We have cooked up a more human-friendly interface to get started with automation!

### How it works
Natural language for Automagica (.nla) looks like this:
```
open the browser
navigate to google.com
search for oranges
```

### Try it yourself

A Wit.ai key is included, so you can get a headstart! 

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
We are quickly expanding the Natural Language Understanding features of this part of Automagica to make automation accessible to all!

## Important notes
For the `Type`-function to work, you need to set the "United States-International" keyboard layout on your system. If the keyboard layout is not available, outcomes of the function might be different.


## Our Activities

| Script | Info |
| ------------- | ------------- |
|**Mouse**|
| GetMouseCoordinates() | Displays message box with absolute coordinates of the mouse position |
| ClickOnPosition(x=0, y=0) | Clicks on a specific (x,y) pixel coordinate on the screen. |
| DoubleClickOnPosition(x=None, y=None) | Double clicks on a specific (x,y) pixel coordinate on the screen. |
| RightClickOnPosition(x=None, y=None) | Right clicks on a specific (x,y) pixel coordinate on the screen. |
| MoveToPosition(x=None, y=None) | Moves te pointer to a x-y pixel position. |
| MoveRelative(x=None, y=None) | Moves the mouse an x- and y- distance relative to its current pixel position. |
| DragToPosition | Drag the mouse from its current position to a entered x-y position, while holding a specified button. |
| ClickOnImage("example.png") | Clicks on an image on the screen. Image path needs to be specified. |
|**Keyboard**|
| PressKey(key) | Press and release a specific key. |
| PressHotkey("ctrl","shift","c") | Press a hotkey (combination) |
| Type(text="Hello world!", interval_seconds=0.01) | Types text with a specified interval in seconds |
| CapsLock() | Press the Caps Lock key. |
| NumLock() | Press the Num Lock key. |
| Enter() | Press the Enter key. |
| SpaceBar() | Press the Space bar key. |
| Backspace() | Press the Backspace key. |
| Delete() | Press the delete key. |
| Endkey() | Press the End key. |
| Tab() | Press the Tab key. |
|**Monitoring**|
| TypeInRunWindow(text) | Type the entered text in the Windows "Run" window. |
| CreateUniqueKey(length) | Returns a UUID as a string with. "Length" determines the amount of characters returned. |
| CPULoad(measure_time=1) | Returns average CPU load for all cores over a measured time. |
| NumberOfCPU(logical=True) | Returns the number of CPU's in the current system. |
| CPUFreq() | Returns frequency at which CPU currently operates together with maximum and minimum frequency. |
| CPUStats() | Returns CPU statistics: Number of CTX switches, interrupts, soft-interrupts and systemcalls. |
| MemoryStats(mem_type='swap') | Returns memory statistics: total, used, free and percentage in use. |
| DiskStats() | Returns disk statistics of main disk: total, used, free and percentage in use. |
| DiskPartitions() | Returns tuple with info for every partition. |
| BootTime() | Returns time PC was booted in seconds after the epoch. |
| TimeSinceLastBoot() | Returns time since last boot in seconds. |
|**Windows Activities**|
| BeepSound(frequency=1000, duration=250) | Makes a beeping sound with a given frequency and duration. |
| ClearClipboard() | Removes everything from the clipboard. |
|**Delay**|
| Wait(seconds=5) | Wait for a specified time in seconds |
| WaitForImage("example.png") | Wait for an image to appear on the screen. Image path needs to be specified |
|**Browser**|
| browser = ChromeBrowser() | Opens the Chrome browser |
| browser.get("https://google.com/") | Browse to a specific URL. Browser needs to be opened first |
| GetGoogleSearchLinks(search_text) | Return a list of search results google returns when searching for search_text. |
|**Applications**|
| ProcessRunning(name) | Checks if given process name (name) is currently running on the system. Returns True or False. |
| ListRunningProcesses() | Returns a list with all names of unique processes currently running on the system. |
| ChromeRunning() | Returns True if Chrome is running. |
| WordRunning() | Returns True if Word is running.  |
| ExcelRunning() | Returns True if Excel is running. |
| PowerpointRunning() | Returns True if Powerpoint is running. |
| DropboxRunning() | Returns True if Dropbox is running. |
| FirefoxRunning() | Returns True is Firefox is running. |
| TeamviewerRunning() | Returns True is Teamviewer is running. |
| SkypeRunning() | Returns True is Skype is running. |
| EdgeRunning() | Returns True is Microsoft Edge is running. |
| OnedriveRunning() | Returns True is Onedrive is running. |
| IllustratorRunning() | Returns True is Illustrator is running. |
| LaunchProcess(process_executable="mspaint.exe") | Launches a process based on the executable |
| KillProcess(process=my_process) | Kills a process |
|**Control Flow**|
| For Loop | Perform a for-looping operation. |
| Condition | If a condition is true, run the indented code. |
| **Message Box** |
| input_variable = RequestUserInput() | Shows a pop-up message asking for user for input. |
| DisplayMessageBox(title=\"Title Text\", body=\"Body Text\", type=\"info\") | Shows an info pop-up message with title and body |
| DisplayMessageBox(title=\"Title Text\", body=\"Body Text\", type=\"warning\") | 
| ExcelCreateWorkbook(path="pathname") | Create new excel workbook and save it at the give path. | Shows a warning pop-up message with title and body |
| DisplayMessageBox(title=\"Title Text\", body=\"Body Text\", type=\"error\") | Shows an error pop-up message with title and body |
| **Excel** |
| ExcelOpenWorkbook(path="pathname") | Open an existing .xlsx file with Microsoft Excel. |
| ExcelSaveExistingWorkbook(path="pathname", new_path=None) | Save a existing .xlsx file to its current path or to a new path. |
| ExcelCreateWorkSheet(path="pathname", sheet_name=None) | Create a named worksheet in a existing .xlsx file specified by a path. |
| ExcelGetSheets(path="pathname") | Return a list with the names of the worksheets is a .xlsx file specified by the path variable. |
| ExcelReadCell(path="pathname", row=1, col=1) | Read cell value from Excel by row and col: first row is defined row number 1 and first column is defined column number 1. |
| ExcelReadCell(path="pathname", cell="A1") | Read cell value from Excel by cell name e.g. cell="A2" is the first cell |
| ExcelWriteCell(path="pathname", sheet="Sheet 1", row=1, col=1, write_value="Value") | Write value to Excel by row and col: first row is defined row number 1 and first column is defined column number 1 |
| ExcelWriteCell(path="pathname", cell=None, write_value="Value") | Write cell value from Excel by cell name e.g. cell="A2" is the first cell |
| ExcelPutRowInList(path="pathname", start_cell="B3", end_cell="E8", sheet=None) | Return the elements from a specified row in a list. |
| ExcelPutColumnInList(path="pathname", start_cell="A3", end_cell="A8", sheet=None) | Return the elements from a specified column in a list. |
| ExcelPutSelectionInMatrix(path="pathname", upper_left_cell="B2", bottom_right_cell="C3", sheet=None) | Return the elements of a specified selection in a matrix. |
|**Word**|
| OpenWordDocument(filename="pathname") | Open a Word document by referring to the absolute path |
| ReplaceText(absolute_document_path, text="[example_placeholder]", replace_with="Example Replacetext") | Replaces text in a Word document, for example to fill in certain fields in a form |
| ConvertWordToPDF(word_filename=absolute_word_path, pdf_filename=absolute_pdf_path) | Transforms a Word document to PDF |
|**PDF**|
| MergePDF(pdf1="pathname", pdf2="pathname", merged_path="pathname") | Adds the pages of pdf2 to pdf1 and saves it at merged_path. |
| ExtractTextFromPage(path, page=1) | Extracts all the text from a give page and returns it as a string. |
|**File Manipulation**|
| OpenFile(path="pathname") | Opens a file at the given path |
| RenameFile(path="pathname", new_name) | Changes the name of a file located by a specified path to new_name  |
| RemoveFile(path="pathname") | Removes the file with a specified pathname. |
| MoveFile(old_path="old_pathname", new_location="new_location_path") | Moves a file with a specified path to a new location. |
| FileExists(path="pathname") | Checks whether a file with the given path exists. |
| CopyFile(old_path="old_pathname",new_location="new_location_path") | Copies a file from a location specified by old_path to a new location.  |
| WaitForFile(path="pathname") | Waits for a file to be created and then opens it. |
| WriteListToFile(list_to_write, file="pathname") | Write the contents of a list to a specified .txt file. |
| WriteFileToList(file="pathname") | Returns the contents of a specified .txt file as a list. |
|**Folder Manipulation**|
| CreateFolder(path="pathname") | Creates new folder at the given path |
| OpenFolder(path="pathname") | Opens a folder at the given path |
| RenameFolder(path="pathname", new_folder_name="name") | Changes the name of a folder located by a specified path to new_name  |
| RemoveFolder(path="pathname", allow_root=False, delete_read_only=True) | Removes the folder with all its contents from a specified pathname. |
| MoveFolder(old_path="old_pathname", new_location="new_location_path") | Moves a folder from one specified path to a new path. |
| EmptyFolder(path="pathname", allow_root=False) | Removes all the folders and files from a given directory. |
| FolderExists(path="pathname") | Checks whether the folder with a given path exists.  |
| CopyFolder(old_path="old pathname", new_location="new_location_path") | Copies a folder located by old pathname to a new location specified by new pathname. |
| ZipFolder(folder_path="pathname_folder", new_path="pathname_compressed_folder") | Zips a folder specified by folder_path.  |
| UnZipFolder(path="pathname_zipped_folder", new_path="pathname_target_location") | Zips a folder specified by path and stores it at new_path.  |
| WaitForFolder(path="pathname") | Waits for a folder to be created and then opens it. |
|**Image Operation**]
| OpenImage(path="pathname") | Opens an image with the given path. |
| RotateImage(path="pathname", angle) | Rotate an image over a specified angle. |
| ResizeImage(path="pathname", size=(640, 480)) | Resizes an image. The new size is entered with a tuple of the form: (width, height) |
| ImageSize(path="Pathname") | Returns the pixel-size of an entered image in a message box. |
| CropImage(path="pathname", box=None) | Crops an image to a region specified by the box argument. |
| MirrorImageHorizontally(path="pathname") | Mirrors an image with a given path horizontally. |
| MirrorImageVertically(path="pathname") | Mirrors an image with a given path vertically. |
| ImageFormat(path="Pathname") | Returns a message box specifying the format of an image. |
|**Windows Applications**|
| OpenCalculator() | Open Windows Calculator. |
| OpenPaint() | Open MS Paint. |
| OpenNotepad() | Open Windows Notepad. |
| OpenSnippingTool() | Open Windows Snipping Tool. |
| OpenControlPanel() | Open Windows Control Panel. |
| OpenCleanManager() | Open Windows Clean Manager. |
| OpenDialer() | Open Windows Dialer. |
| OpenVolumeMixer() | Open Windows Volume Mixer. |
| OpenXPSViewer | Open Windows XPS Viewer. |
|**Email**|
| SendMailWithHotmail(user, password, destination, subject="", message="", port=587) | Send an email with a given text and subject with your Hotmail account. |
| SendMailWithGmail(user, password, destination, subject="", message="", port=587) | Send an email with a given text and subject with your Gmail account. |
| SendMailWithYahoo(user, password, destination, subject="", message="", port=587) | Send an email with a given text and subject with your Yahoo account. |
|**Math**|
| abs(x) | Calculates the absolute value of an integer or float |
| round(x) | Rounds up an integer or float to the closest number |
| exp(x) | The exponential of x |
| floor(x) | The floor of x: the largest integer not greater than x |
| log(x) | The natural logarithm of x, for x> 0 |
| max(x1, x2, ...) | The largest of its arguments: the value closest to positive infinity |
| min(x1, x2, ...) | The smallest of its arguments: the value closest to negative infinity |
| round(x) | x rounded to n digits from the decimal point. |
| abs(x) | Calculates the absolute value of an integer or float |
| sqrt(x) | The square root of x for x > 0 |

## Known issues
- Run after boot might not work for Linux/OSX systems. This will be fixed soon®.

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
- [PyPDF2](https://github.com/mstamy2/PyPDF2)
- [Psutil](https://pypi.org/project/psutil/)
- [py-trello](https://github.com/sarumont/py-trello)

A special thanks goes out to all the above-mentioned repository contributers! :heart:
