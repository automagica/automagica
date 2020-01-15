![](https://github.com/OakwoodAI/automagica/blob/master/images/logo.png)
# Automagica
Automagica is an open source Smart Robotic Process Automation (SRPA) platform. With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide a comprehensive and consistent wrapper around known and lesser known automation libraries .

![Love Automagica Example](https://github.com/OakwoodAI/automagica/blob/master/images/automagica_drawing.gif)

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

Process | Description
------- | -----------
**Cryptography** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/key-solid.svg" width="20"> Random key | Generate random Fernet key. Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-solid.svg" width="20"> Encrypt text | Encrypt text with (Fernet) key,
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-open-solid.svg" width="20"> Decrypt text | Dexrypt bytes-like object to string with (Fernet) key
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-solid.svg" width="20"> Encrypt file | Encrypt file with (Fernet) key. Note that file will be unusable unless unlocked with the same key.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-open-solid.svg" width="20"> Decrypt file | Decrypts file with (Fernet) key
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/lock-solid.svg" width="20"> Key from password | Generate key based on password and salt. If both password and salt are known the key can be regenerated.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/fingerprint-solid.svg" width="20"> Hash from file | Generate hash from file
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/fingerprint-solid.svg" width="20"> Hash from text | Generate hash from text
**Random** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/dice-solid.svg" width="20"> Random number | Random numbers can be integers (not a fractional number) or a float (fractional number).
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/coins-solid.svg" width="20"> Random boolean | Generates a random boolean (True or False)
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/comment-solid.svg" width="20"> Random name | Generates a random name. Adding a locale adds a more common name in the specified locale. Provides first name and last name.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/map-solid.svg" width="20"> Random address | Generates a random address. Specifying locale changes random locations and streetnames based on locale.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/volume-up-solid.svg" width="20"> Random beep | Generates a random beep, only works on Windows
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/calendar-solid.svg" width="20"> Random date | Generates a random date.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/random-solid.svg" width="20"> Generate unique identifier | Generates a random UUID4 (universally unique identifier). While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible.
**User Input** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/window-maximize-solid.svg" width="20"> Ask user for input | Prompt the user for an input with a pop-up window.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/window-maximize-solid.svg" width="20"> Ask user for password | Prompt the user for a password. The password will be masked on screen while entering.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/window-maximize-solid.svg" width="20"> Ask user for credentials | Prompt a popup which asks user for username and password and returns in plain text. Password will be masked.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/window-maximize-solid.svg" width="20"> Shows message box | A pop-up message with title and message.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/tv-solid.svg" width="20"> Display overlay message | Display custom OSD (on-screen display) message. Can be used to display a message for a limited amount of time. Can be used for illustration, debugging or as OSD.
**Browser** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/chrome-solid.svg" width="20"> Open Chrome Browser | Open the Chrome Browser with the Selenium webdriver. Canb be used to automate manipulations in the browser.Different elements can be found as:
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/images-solid.svg" width="20"> Save all images | Save all images on current page in the Browser
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/align-center-solid.svg" width="20"> Find elements by text | Find all elements by their text. Text does not need to match exactly, part of text is enough.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/align-center-solid.svg" width="20"> Find element by text | Find one element by text. Text does not need to match exactly, part of text is enough.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/window-restore-solid.svg" width="20"> Find all links | Find all links on a webpage in the browser
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/highlighter-solid.svg" width="20"> Highlight element | Highlight elements in yellow in the browser
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/window-close-solid.svg" width="20"> Exit the browser | Quit the browser by exiting gracefully. One can also use the native 'quit' function, e.g. 'browser.quit()'
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/times-solid.svg" width="20"> Find all XPaths | Find all elements with specified xpath on a webpage in the the browser. Can also use native 'find_elements_by_xpath' function e.g. browser.find_elements_by_xpath()You can easily
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/times-solid.svg" width="20"> Find XPath in browser | Find all element with specified xpath on a webpage in the the browser. Can also use native 'find_elements_by_xpath' function e.g. browser.find_element_by_xpath()
**Credential Management** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/key-solid.svg" width="20"> Set credential | Add a credential which stores credentials locally and securely. All parameters should be Unicode text.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/key-solid.svg" width="20"> Delete credential | Delete a locally stored credential. All parameters should be Unicode text.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/key-solid.svg" width="20"> Get credential | Get a locally stored redential. All parameters should be Unicode text.
**FTP** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-open-solid.svg" width="20"> Create FTP connection | Can be used to automate activites for FTP
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/download-solid.svg" width="20"> Download file | Downloads a file from FTP server. Connection needs to be established first.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/upload-solid.svg" width="20"> Upload file | Upload file to FTP server
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/list-ol-solid.svg" width="20"> List FTP files | Generate a list of all the files in the FTP directory
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/list-ol-solid.svg" width="20"> Check FTP directory | Check if FTP directory exists
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-plus-solid.svg" width="20"> Create FTP directory | Create a FTP directory. Note that sufficient permissions are present
**Keyboard** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/keyboard-solid.svg" width="20"> Press key | Press and release an entered key. Make sure your keyboard is on US layout (standard QWERTY).If you are using this on Mac Os you might need to grant acces to your terminal application. (Security Preferences > Security & Privacy > Privacy > Accessibility)
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/keyboard-solid.svg" width="20"> Press key combination | Press a combination of two or three keys simultaneously. Make sure your keyboard is on US layout (standard QWERTY).
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/keyboard-solid.svg" width="20"> Type text | Types text in the current active field by simulating keyboard typing.  Make sure your keyboard is on US layout (standard QWERTY).
**Mouse** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mouse-solid.svg" width="20"> Get mouse coordinates | Get the x and y pixel coordinates of current mouse position.These coordinates represent the absolute pixel position of the mouse on the computer screen. The x-coördinate starts on the left side and increases going right. The y-coördinate increases going down.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/search-location-solid.svg" width="20"> Display mouse position | Displays mouse position in an overlay. Refreshes every two seconds. Can be used to find mouse position of element on the screen.These coordinates represent the absolute pixel position of the mouse on the computer screen. The x-coördinate starts on the left side and increases going right. The y-coördinate increases going down.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mouse-pointer-solid.svg" width="20"> Mouse click | Clicks on a pixel position on the visible screen determined by x and y coordinates.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mouse-pointer-solid.svg" width="20"> Double mouse click | Double clicks on a pixel position on the visible screen determined by x and y coordinates.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mouse-pointer-solid.svg" width="20"> Right click | Right clicks on a pixel position on the visible screen determined by x and y coordinates.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/arrows-alt-solid.svg" width="20"> Move mouse | Moves te pointer to a x-y position.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/arrows-alt-solid.svg" width="20"> Move mouse relative | Moves the mouse an x- and y- distance relative to its current pixel position.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/arrows-alt-solid.svg" width="20"> Drag mouse | Drag the mouse from its current position to a entered x-y position, while holding a specified button.
**Image** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/crop-alt-solid.svg" width="20"> Random screen snippet | Take a random square snippet from the current screen. Mainly for testing and/or development purposes.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/expand-solid.svg" width="20"> Screenshot | Take a screenshot of current screen.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/image-solid.svg" width="20"> Click on image | This function searches the screen for a match with template image and clicks directly in the middle. Note that this only finds exact matches.For a more advanced and robust vision detection method see Automagica AI functionality.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/image-solid.svg" width="20"> Double click image | Double click on similar image on the screen. This function searches the screen for a match with template image and doubleclicks directly in the middle.Note that this only finds exact matches. For a more advanced and robust vision detection method see Automagica AI functionality.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/image-solid.svg" width="20"> Right click image | Right click on similar image on the screen. This function searches the screen for a match with template image and right clicks directly in the middle.Note that this only finds exact matches. For a more advanced and robust vision detection method see Automagica AI functionality.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/image-solid.svg" width="20"> Locate image on screen | Find exact image on the screen. This function searches the screen for a match with template image and clicks directly in the middle.Note that this only finds exact matches. For a more advanced and robust vision detection method see Automagica AI functionality.
**Folder Operations** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/search-solid.svg" width="20"> List files in folder | List all files in a folder (and subfolders)Checks all folders and subfolders for files. This could take some time for large repositories.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-plus-solid.svg" width="20"> Create folder | Creates new folder at the given path.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-solid.svg" width="20"> Rename folder | Rename a folder
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-open-solid.svg" width="20"> Open a folder | Open a folder with the default explorer.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-solid.svg" width="20"> Move a folder | Moves a folder from one place to another.If the new location already contains a folder with the same name, a random 4 character uid is added to the name.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-minus-solid.svg" width="20"> Remove folder | Remove a folder including all subfolders and files. For the function to work optimal, all files and subfolders in the main targetfolder should be closed.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-minus-solid.svg" width="20"> Empty folder | Remove all contents from a folderFor the function to work optimal, all files and subfolders in the main targetfolder should be closed.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-solid.svg" width="20"> Checks if folder exists | Check whether folder exists or not, regardless if folder is empty or not.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/folder-solid.svg" width="20"> Copy a folder | Copies a folder from one place to another.If the new location already contains a folder with the same name, a random 4 character id is added to the name.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/archive-solid.svg" width="20"> Zip | Zia folder and it's contents. Creates a .zip file.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/archive-solid.svg" width="20"> Unzip | Unzips a file or folder from a .zip file.
**Delay** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/hourglass-solid.svg" width="20"> Wait | Make the robot wait for a specified number of seconds. Note that this activity is blocking. This means that subsequent activities will not occur until the the specified waiting time has expired.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/hourglass-solid.svg" width="20"> Wait for image | Waits for an image to appear on the screenNote that this activity waits for an exact match of the template image to appear on the screen.Small variations, such as color or resolution could result in a mismatch.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/hourglass-solid.svg" width="20"> Wait for folder | Waits until a folder exists.Not that this activity is blocking and will keep the system waiting.
**Word Application** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Start Word Application | For this activity to work, Microsoft Office Word needs to be installed on the system.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Append text | Append text at end of Word document.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Replace text | Can be used for example to replace arbitrary placeholder value. For example whenusing template document, using 'XXXX' as a placeholder. Take note that all strings are case sensitive.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Read all text | Read all the text from a document
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-pdf-solid.svg" width="20"> Export to PDF | Export the document to PDF
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/html5-solid.svg" width="20"> Export to HTML | Export to HTML
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/heading-solid.svg" width="20"> Set footers | Set the footers of the document
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/subscript-solid.svg" width="20"> Set headers | Set the headers of the document
**Word File** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Read and Write Word files | These activities can read, write and edit Word (docx) files without the need of having Word installed.Note that, in contrary to working with the :func: 'Word' activities, a file get saved directly after manipulation.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Read all text | Read all the text from the document
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Append text | Append text at the end of the document
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Save | Save document
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Save as | :Example:
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Set headers | Set headers of Word document
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-word-solid.svg" width="20"> Replace all | Replaces all occurences of a placeholder text in the document with a replacement text.
**Outlook Application** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Start Outlook Application | For this activity to work, Outlook needs to be installed on the system.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Send e-mail | Send an e-mail using Outlook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Retrieve folders | Retrieve list of folders from Outlook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Retrieve e-mails | Retrieve list of messages from Outlook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Delete e-mails | Deletes e-mail messages in a certain folder. Can be specified by searching on subject, body or sender e-mail.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Move e-mails | Move e-mail messages in a certain folder. Can be specified by searching on subject, body or sender e-mail.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Save attachments | :parameter folder_name: Name of the Outlook folder, can be found using `get_folders`.:parameter target_folder_path: Path where attachments will be saved. Default is the home directory.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Retrieve contacts | :parameter fields: Fields can be specified as a tuple with their exact names. Standard value is None returning "LastName", "FirstName" and "Email1Address".
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Add a contact | Add a contact to Outlook contacts
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Quit | Close the Outlook application
**Excel Application** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Start Excel Application | For this activity to work, Microsoft Office Excel needs to be installed on the system.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Add worksheet | Adds a worksheet to the current workbook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Activate worksheet | Activate a worksheet in the current Excel document by name
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Save | Save the current workbook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Save as | Save the current workbook to a specific path
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Write cell | Write to a specific cell in the currently active workbook and active worksheet
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Read cell | Read a cell from the currently active workbook and active worksheet
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Write range | Write to a specific range in the currently active worksheet in the active workbook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Read range | Read a range of cells from the currently active worksheet in the active workbook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Run macro | Run a macro by name from the currently active workbook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Get worksheet names | Get names of all the worksheets in the currently active workbook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Get table | Get table data from the currently active worksheet by name of the table
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Activate range | Activate a particular range in the currently active workbook
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Activate first empty cell down | Activates the first empty cell going down
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Activate first empty cell right | Activates the first empty cell going right
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Activate first empty cell left | Activates the first empty cell going left
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Activate first empty cell up | Activates the first empty cell going up
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Write cell formula | Write a formula to a particular cell
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Read cell formula | Read the formula from a particular cell
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Insert empty row | Inserts an empty row to the currently active worksheet
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Insert empty column | Inserts an empty column in the currently active worksheet. Existing columns will shift to the right.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Delete row in Excel | Deletes a row from the currently active worksheet. Existing data will shift up.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Delete column | Delet a column from the currently active worksheet. Existing columns will shift to the left.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Export to PDF | :parameter path: Output path where PDF file will be exported to. Default path is home directory with filename 'pdf_export.pdf'.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Insert data as table | Insert list of dictionaries as a table in Excel
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Read worksheet | Read data from a worksheet as a list of lists
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Quit Excel | This closes Excel, make sure to use :func: 'save' or 'save_as' if you would like to save before quitting.
**Excel File** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Read and Write xlsx files. | This activity can read, write and edit Excel (xlsx) files without the need of having Excel installed.Note that, in contrary to working with the :func: 'Excel' activities, a file get saved directly after manipulation.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Activate worksheet | Activate a worksheet. By default the first worksheet is activated.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Save as | :parameter path: Path where workbook will be saved
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Write cell | :parameter column: Column number (integer) to write:parameter row: Row number (integer) to write:parameter value: Value to write to specific cell:parameter auto_save: Save document after performing activity. Default value is True
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Read cell | :parameter column: Column number (integer) to read:parameter row: Row number (integer) to read
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Add worksheet | :parameter name: Name of the worksheet to add:parameter auto_save: Save document after performing activity. Default value is True
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-excel-solid.svg" width="20"> Get worksheet names | :return: List of worksheet names
**PowerPoint Application** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Start PowerPoint Application | For this activity to work, PowerPoint needs to be installed on the system.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Save PowerPoint | Save PowerPoint Slidedeck
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Close PowerPoint Application | Close PowerPoint
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Add PowerPoint Slides | Adds slides to a presentation
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Slide count | :return: The number of slides
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Text to slide | Add text to a slide
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Delete slide | :parameter index: Slide index to be deleted. If none is specified, last slide will be deleted
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Replace all occurences of text in PowerPoint slides | Can be used for example to replace arbitrary placeholder value in a PowerPoint.For example when using a template slidedeck, using 'XXXX' as a placeholder.Take note that all strings are case sensitive.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> PowerPoint to PDF | Export PowerPoint presentation to PDF file
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-powerpoint-solid.svg" width="20"> Slides to images | Export PowerPoint slides to seperate image files
**Office 365** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/envelope-solid.svg" width="20"> Send email Office Outlook 365 | :parameter client_id: Client id for office 365 account:parameter client_secret: Client secret for office 365 account:parameter to_email: E-mail to send to:parameter subject: Optional subject:parameter body: Optional body of the email
**Salesforce** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/salesforce.svg" width="20"> Salesforce API | Activity to make calls to Salesforce REST API.
**E-mail (SMTP)** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mail-bulk-solid.svg" width="20"> Mail with SMTP | This function lets you send emails with an e-mail address.
**Windows OS** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/passport-solid.svg" width="20"> Set Windows password | Sets the password for a Windows user.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/passport-solid.svg" width="20"> Check Windows password | Validates a Windows user password if it is correct
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/user-lock-solid.svg" width="20"> Lock Windows | Locks Windows requiring login to continue.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/user-solid.svg" width="20"> Check if Windows logged in | Checks if the current user is logged in and not on the lockscreen. Most automations do not work properly when the desktop is locked.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/user-solid.svg" width="20"> Check if Windows is locked | Checks if the current user is locked out and on the lockscreen. Most automations do not work properly when the desktop is locked.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/user-solid.svg" width="20"> Get Windows username | Get current logged in user's username
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/clipboard-check-solid.svg" width="20"> Set clipboard | Set any text to the Windows clipboard.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/clipboard-list-solid.svg" width="20"> Get clipboard | Get the text currently in the Windows clipboard
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/clipboard-solid.svg" width="20"> Empty clipboard | Empty text from clipboard. Getting clipboard data after this should return in None
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/cogs-solid.svg" width="20"> Run VBSscript | Run a VBScript file
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/volume-up-solid.svg" width="20"> Beep | Make a beeping sound. Make sure your volume is up and you have hardware connected.
**Text-to-Speech** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/microphone-alt-solid.svg" width="20"> Speak | Use the Text-To-Speech engine available on your system to read text
**Active Directory** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/audio-description-solid.svg" width="20"> AD interface | Interface to Windows Active Directory through ADSI
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/audio-description-solid.svg" width="20"> Get AD object by name | Interface to Windows Active Directory through ADSI
**Utilities** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/home-solid.svg" width="20"> Get user home path | Returns the current user's home path
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/desktop-solid.svg" width="20"> Get desktop path | Returns the current user's desktop path
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-solid.svg" width="20"> Open file | Opens file with default programs
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/desktop-solid.svg" width="20"> Set wallpaper | Set Windows desktop wallpaper with the the specified image
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/cloud-download-alt-solid.svg" width="20"> Download file from a URL | :parameter url: Source URL to download file from:parameter filename::parameter path: Target path. If no path is given will download to the home directory
**Trello** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/trello.svg" width="20"> Add Trello Card | Add a card to the Trello board. For this you need a Trello API key, secret and token.
**System** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-contract-solid.svg" width="20"> Rename a file | This activity will rename a file. If the the desired name already exists in the folder file will not be renamed.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-export-solid.svg" width="20"> Move a file | If the new location already contains a file with the same name, a random 4 character uid will be added in front of the name before the file is moved.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/trash-solid.svg" width="20"> Remove a file | :parameter path: Full path to the file that will be deleted.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/tasks-solid.svg" width="20"> Check if file exists | This function checks whether the file with the given path exists.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/list-alt-solid.svg" width="20"> Wait until a file exists. | Not that this activity is blocking and will keep the system waiting.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/list-solid.svg" width="20"> List to .txt | Writes a list to a  text (.txt) file.Every element of the entered list is written on a new line of the text file.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/th-list-solid.svg" width="20"> Read .txt file | This activity writes the content of a .txt file to a list and returns that list.Every new line from the .txt file becomes a new element of the list. The activity willnot work if the entered path is not attached to a .txt file.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/tasks-solid.svg" width="20"> Append to .txt | Append a text line to a file and creates the file if it does not exist yet.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/file-alt-solid.svg" width="20"> Make text file | Initialize text file
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/copy-solid.svg" width="20"> Copy a file | Copies a file from one place to another.If the new location already contains a file with the same name, a random 4 character uid is added to the name.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/info-solid.svg" width="20"> Get file extension | Get extension of a file
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/print-solid.svg" width="20"> Print | Send file to default printer to priner. This activity sends a file to the printer. Make sure to have a default printer set up.
**PDF** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/glasses-solid.svg" width="20"> Text from PDF | Extracts the text from a PDF. This activity reads text from a pdf file. Can only read PDF files that contain a text layer.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/object-ungroup-solid.svg" width="20"> Merge PDF | Merges multiple PDFs into a single file
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/cut-solid.svg" width="20"> Extract page from PDF | Extracts a particular range of a PDF to a separate file.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/icons-solid.svg" width="20"> Extract images from PDF | Save a specific page from a PDF as an image
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/stamp-solid.svg" width="20"> Watermark a PDF | :parameter file_path: Filepath to the document that will be watermarked. Should be pdf file.:parameter watermark_path: Filepath to the watermark. Should be pdf file.:parameter output_path: Path to save watermarked PDF. If no path is provided same path as input will be used with 'watermarked' added to the name
**System Monitoring** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/microchip-solid.svg" width="20"> CPU load | Get average CPU load for all cores.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/calculator-solid.svg" width="20"> Count CPU | Get the number of CPU's in the current system.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/wave-square-solid.svg" width="20"> CPU frequency | Get frequency at which CPU currently operates.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/server-solid.svg" width="20"> CPU Stats | Get CPU statistics
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/memory-solid.svg" width="20"> Memory statistics | Get  memory statistics
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/save-solid.svg" width="20"> Disk stats | Get disk statistics of main disk
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/save-solid.svg" width="20"> Partition info | Get disk partition info
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/clock-solid.svg" width="20"> Boot time | Get most recent boot time
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/clock-solid.svg" width="20"> Uptime | Get uptime since last boot
**Image Processing** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/images-solid.svg" width="20"> Show image | Displays an image specified by the path variable on the default imaging program.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/undo-solid.svg" width="20"> Rotate image | Rotate an image
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/expand-arrows-alt-solid.svg" width="20"> Resize image | Resizes the image specified by the path variable.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/expand-arrows-alt-solid.svg" width="20"> Get image width | Get with of image
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/arrows-alt-v-solid.svg" width="20"> Get image height | Get height of image
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/crop-solid.svg" width="20"> Crop image | Crops the image specified by path to a region determined by the box variable.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/caret-up-solid.svg" width="20"> Mirror image horizontally | Mirrors an image with a given path horizontally from left to right.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/caret-right-solid.svg" width="20"> Mirror image vertically | Mirrors an image with a given path vertically from top to bottom.
**Process** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/cog-solid.svg" width="20"> Windows run | Use Windows Run to boot a processNote this uses keyboard inputs which means this process can be disrupted by interfering inputs
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/play-solid.svg" width="20"> Run process | Use subprocess to open a windows process
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/cogs-solid.svg" width="20"> Check if process is running | Check if process is running. Validates if given process name (name) is currently running on the system.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/list-solid.svg" width="20"> Get running processes | Get names of unique processes currently running on the system.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/window-close-solid.svg" width="20"> Kill process | Kills a process forcefully
**Optical Character Recognition (OCR)** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/readme.svg" width="20"> Get text with OCR | This activity extracts all text from the current screen or an image if a path is specified.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/glasses-solid.svg" width="20"> Find text on screen with OCR | This activity finds position (coordinates) of specified text on the current screen using OCR.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mouse-pointer-solid.svg" width="20"> Click on text with OCR | This activity clicks on position (coordinates) of specified text on the current screen using OCR.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mouse-pointer-solid.svg" width="20"> Double click on text with OCR | This activity double clicks on position (coordinates) of specified text on the current screen using OCR.
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/mouse-pointer-solid.svg" width="20"> Right click on text with OCR | This activity Right clicks on position (coordinates) of specified text on the current screen using OCR.
**UiPath** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/robot-solid.svg" width="20"> Execute a UiPath process | This activity allows you to execute a process designed with the UiPath Studio. All console output from the Write Line activity (https://docs.uipath.com/activities/docs/write-line) will be printed as output.
**AutoIt** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/robot-solid.svg" width="20"> Execute a AutoIt script | This activity allows you to run an AutoIt script. If you use the ConsoleWrite function (https://www.autoitscript.com/autoit3/docs/functions/ConsoleWrite.htm), the output will be presented to you.
**Robot Framework** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/robot-solid.svg" width="20"> Execute a Robot Framework test case | This activity allows you to run a Robot Framework test case. Console output of the test case will be printed.
**Blue Prism** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/robot-solid.svg" width="20"> Run a Blue Prism process | This activity allows you to run a Blue Prism process.
**Automation Anywhere** | ‌‌ 
<img src="https://github.com/OakwoodAI/automagica/blob/master/images/icons/robot-solid.svg" width="20"> Run an Automation Anywhere task | This activity allows you to run an Automation Anywhere task.
|<img width=100/>|  ‌‌|

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
