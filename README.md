![](https://automagica.com/wp-content/uploads/2020/06/logo.png)
# Automagica - Open Source Robotic Process Automation [![Downloads](https://pepy.tech/badge/automagica/month)](https://pepy.tech/project/automagica/month)
Automagica is an open source automation suite for fully automating tedious, manual tasks on any screen. Our vision is that __people should not be doing a robot's job__. Our mission is to make these automation tools as accessible as possible to empower everyone to automate (almost) anything. 

_Let bots handle the clicks so people can handle the business._

[![Github Signup Automagica](https://i.imgur.com/PKvMCSl.jpg)](https://portal.automagica.com/github/login)

![Love Automagica Example](https://automagica.com/wp-content/uploads/2020/06/automagica_drawing.gif)

## Our mission

With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide you with:
- the tools to build amazing software robots
- a comprehensive and consistent wrapper around known and lesser known (Python) automation libraries and

## Important links
- [Website](https://www.automagica.com)
- [Portal](https://portal.automagica.com)
- [Documentation](https://automagica.readthedocs.io)
- [YouTube Channel](https://automagi.ca/youtube)
- [Public Roadmap](https://automagi.ca/roadmap)

## Community
- Our __[roadmap](https://trello.com/b/qXHf5YqD/automagica-roadmap)__ is public (feel free to add suggestions to the Ideas column!)
- Join our __[Discord](https://discord.gg/PbY85WA)__ channel (this is a great place to ask questions)
- __[Telegram](https://t.me/automagica)__ group (good for getting the latest updates)

## What's open source?
### Automagica Activities
### Automagica Lab
### Automagica Flow
### Automagica Capture


## Need professional support?
Please send an e-mail to [sales@automagica.com](mailto:sales@automagica.com).

## Getting started

### Installation

The easiest way to install Automagica is by using the installer for Windows which can be downloaded from the [Automagica Portal](https://portal.automagica.com).

![](https://automagica.com/wp-content/uploads/2020/06/portal_screenshots.JPG)

### Other OSes than Windows
#### Fedora-like distributions of Linux such as Red Hat Enterprise Linux or CentOS
You can install Automagica by running the following commands:

```
sudo yum install python3-devel chromium -y
sudo pip3 install automagica -U
```
#### Debian-like distributions of Linux such as Ubuntu
You can install Automagica by running the following commands:
```
sudo apt-get install python3-devel chromium -y
sudo pip3 install automagica -U
```

### Developers and other platforms

If you wish to only install the Automagica Python library (without registering for the Automagica Portal), follow the below steps.

- Download and install [Python 3.7](https://www.python.org)

- Install the latest version Automagica on your machine:
```
pip install automagica --upgrade
```
#### Importing the activities

Before getting started in development mode, don't forget to import the activities from automagica in your python script. If unsure, it is possible to import all the activities for development purposes by starting your script with:
```
from automagica import *
```

Important: for some activities (mainly OCR-related) an Automagica API-key is required. In order to acquire an API-key, you need to register at the [Automagica Portal](https://portal.automagica.com).

## Components
The Automagica suite consists of the following components:
- __Automagica Bot__: runtime/agent responsible for performing the automated tasks.
- __Automagica Wand__: UI element picker powered by AI.
- __Automagica Flow__: a visual flow designer to build automations quickly.
- __Automagica Lab__: Notebook-style automation development environment based on Jupyter Notebooks (requires Jupyter to be installed).
- __Automagica Portal__: management of bots, credentials, automations, logs, ...

Some activities access external services hosted on our servers, such as the AI and OCR-related capabilities.

The Automagica Portal is currently not available under an open source license. We offer a free environment for evaluation purposes at https://portal.automagica.com. If you would like to use the Automagica Portal within your company or organization, please contact us at sales@automagica.com.


## Examples

Try out the one-click examples:
* [Webscraping in Chrome](https://portal.automagica.com/register)
* [Read and write data in Excel](https://portal.automagica.com/register)
* [Automatically make a PowerPoint presentation](https://portal.automagica.com/register)
* [Change your Windows wallpaper](https://portal.automagica.com/register)
* [Manipulate files and folders](https://portal.automagica.com/register)
* [Use OCR to read images and click buttons](https://portal.automagica.com/register)

Browser working with Excel:

![Excel Example Automagica](https://automagica.com/wp-content/uploads/2020/06/browser_excel.gif)

SAP Automation (Production example, sensitive information is blurred):

![Sap Example Automagica](https://automagica.com/wp-content/uploads/2020/06/sap.gif)

Folder and File manipulation

<img src="https://github.com/automagica/automagica/blob/master/images/USPresidents.gif" width="800">

## Docker
As Automagica is fully cross-platform and built with Python, it's quite easy to run or build Automagica bots inside containers. We've added an example `Dockerfile` with the minimum reuirements for running an Automagica bot:
```
git clone https://github.com/automagica/automagica
cd automagica
docker build . -t automagica
docker run -it -p 8080:8080 automagica
```
Then browse to http://localhost:8080/vnc.html to access the Automagica desktop.

## Activities

An overview of all official Automagica activities:

Process | Description
------- | -----------
**Cryptography** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/key-solid.svg" width="20"> [Random key](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_key) | Generate random Fernet key. Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/lock-solid.svg" width="20"> [Encrypt text](https://automagica.readthedocs.io/activities.html#automagica.activities.encrypt_text_with_key) | Encrypt text with (Fernet) key,
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/lock-open-solid.svg" width="20"> [Decrypt text](https://automagica.readthedocs.io/activities.html#automagica.activities.decrypt_text_with_key) | Dexrypt bytes-like object to string with (Fernet) key
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/lock-solid.svg" width="20"> [Encrypt file](https://automagica.readthedocs.io/activities.html#automagica.activities.encrypt_file_with_key) | Encrypt file with (Fernet) key. Note that file will be unusable unless unlocked with the same key.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/lock-open-solid.svg" width="20"> [Decrypt file](https://automagica.readthedocs.io/activities.html#automagica.activities.decrypt_file_with_key) | Decrypts file with (Fernet) key
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/lock-solid.svg" width="20"> [Key from password](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_key_from_password) | Generate key based on password and salt. If both password and salt are known the key can be regenerated.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/fingerprint-solid.svg" width="20"> [Hash from file](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_hash_from_file) | Generate hash from file
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/fingerprint-solid.svg" width="20"> [Hash from text](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_hash_from_text) | Generate hash from text
**Random** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/dice-solid.svg" width="20"> [Random number](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_number) | Random numbers can be integers (not a fractional number) or a float (fractional number).
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/coins-solid.svg" width="20"> [Random boolean](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_boolean) | Generates a random boolean (True or False)
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/user-tag-solid.svg" width="20"> [Random name](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_name) | Generates a random name. Adding a locale adds a more common name in the specified locale. Provides first name and last name.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/comment-solid.svg" width="20"> [Random sentence](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_sentence) | Generates a random sentence. Specifying locale changes language and content based on locale.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/map-solid.svg" width="20"> [Random address](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_address) | Generates a random address. Specifying locale changes random locations and streetnames based on locale.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/volume-up-solid.svg" width="20"> [Random beep](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_beep) | Generates a random beep, only works on Windows
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/calendar-solid.svg" width="20"> [Random date](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_random_date) | Generates a random date.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/calendar-solid.svg" width="20"> [Today's date](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_date_today) | Generates today's date.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/random-solid.svg" width="20"> [Generate unique identifier](https://automagica.readthedocs.io/activities.html#automagica.activities.generate_unique_identifier) | Generates a random UUID4 (universally unique identifier). While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible.
**Output** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/tv-solid.svg" width="20"> [Display overlay message](https://automagica.readthedocs.io/activities.html#automagica.activities.display_osd_message) | Display custom OSD (on-screen display) message. Can be used to display a message for a limited amount of time. Can be used for illustration, debugging or as OSD.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/tv-solid.svg" width="20"> [Print message in console](https://automagica.readthedocs.io/activities.html#automagica.activities.print_console) | Print message in console. Can be used to display data in the Automagica Flow console
**Browser** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/chrome.svg" width="20"> [self,](https://automagica.readthedocs.io/activities.html#automagica.activities.Chrome) | headless=False,incognito=False,disable_extension=False,maximize_window=True,focus_window=True,):"""Open Chrome Browser
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/images-solid.svg" width="20"> [Save all images](https://automagica.readthedocs.io/activities.html#automagica.activities.save_all_images) | Save all images on current page in the Browser
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/chrome.svg" width="20"> [Browse to URL](https://automagica.readthedocs.io/activities.html#automagica.activities.browse_to) | Browse to URL.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/align-center-solid.svg" width="20"> [Find elements by text](https://automagica.readthedocs.io/activities.html#automagica.activities.find_elements_by_text) | Find all elements by their text. Text does not need to match exactly, part of text is enough.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Find all links](https://automagica.readthedocs.io/activities.html#automagica.activities.find_all_links) | Find all links on a webpage in the browser
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Find first link on a webpage](https://automagica.readthedocs.io/activities.html#automagica.activities.find_first_link) | Find first link on a webpage
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Get all text on webwpage](https://automagica.readthedocs.io/activities.html#automagica.activities.get_text_on_webpage) | Get all the raw body text from current webpage
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/highlighter-solid.svg" width="20"> [Highlight element](https://automagica.readthedocs.io/activities.html#automagica.activities.highlight) | Highlight elements in yellow in the browser
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-close-solid.svg" width="20"> [Exit the browser](https://automagica.readthedocs.io/activities.html#automagica.activities.exit) | Quit the browser by exiting gracefully. One can also use the native 'quit' function
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/times-solid.svg" width="20"> [Find all XPaths](https://automagica.readthedocs.io/activities.html#automagica.activities.by_xpaths) | Find all elements with specified xpath on a webpage in the the browser. Can also use native 'find_elements_by_xpath'
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/times-solid.svg" width="20"> [Find XPath in browser](https://automagica.readthedocs.io/activities.html#automagica.activities.by_xpath) | Find all element with specified xpath on a webpage in the the browser. Can also use native 'find_elements_by_xpath'
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/times-solid.svg" width="20"> [Find class in browser](https://automagica.readthedocs.io/activities.html#automagica.activities.by_class) | Find element with specified class on a webpage in the the browser. Can also use native 'find_element_by_class_name'
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/times-solid.svg" width="20"> [Find class in browser](https://automagica.readthedocs.io/activities.html#automagica.activities.by_classes) | Find all elements with specified class on a webpage in the the browser. Can also use native 'find_elements_by_class_name' function
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/times-solid.svg" width="20"> [Find element in browser based on class and text](https://automagica.readthedocs.io/activities.html#automagica.activities.by_class_and_by_text) | Find all elements with specified class and text on a webpage in the the browser.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/times-solid.svg" width="20"> [Find id in browser](https://automagica.readthedocs.io/activities.html#automagica.activities.by_id) | Find element with specified id on a webpage in the the browser. Can also use native 'find_element_by_id' function
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/times-solid.svg" width="20"> [Switch to iframe in browser](https://automagica.readthedocs.io/activities.html#automagica.activities.switch_to_iframe) | Switch to an iframe in the browser
**Credential Management** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/key-solid.svg" width="20"> [Set credential](https://automagica.readthedocs.io/activities.html#automagica.activities.set_credential) | Add a credential which stores credentials locally and securely. All parameters should be Unicode text.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/key-solid.svg" width="20"> [Delete credential](https://automagica.readthedocs.io/activities.html#automagica.activities.delete_credential) | Delete a locally stored credential. All parameters should be Unicode text.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/key-solid.svg" width="20"> [Get credential](https://automagica.readthedocs.io/activities.html#automagica.activities.get_credential) | Get a locally stored redential. All parameters should be Unicode text.
**FTP** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-open-solid.svg" width="20"> [Create FTP connection](https://automagica.readthedocs.io/activities.html#automagica.activities.FTP) | Can be used to automate activites for FTP
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/download-solid.svg" width="20"> [Download file](https://automagica.readthedocs.io/activities.html#automagica.activities.download_file) | Downloads a file from FTP server. Connection needs to be established first.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/upload-solid.svg" width="20"> [Upload file](https://automagica.readthedocs.io/activities.html#automagica.activities.upload_file) | Upload file to FTP server
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/list-ol-solid.svg" width="20"> [List FTP files](https://automagica.readthedocs.io/activities.html#automagica.activities.enumerate_files) | Generate a list of all the files in the FTP directory
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/list-ol-solid.svg" width="20"> [Check FTP directory](https://automagica.readthedocs.io/activities.html#automagica.activities.directory_exists) | Check if FTP directory exists
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-plus-solid.svg" width="20"> [Create FTP directory](https://automagica.readthedocs.io/activities.html#automagica.activities.create_directory) | Create a FTP directory. Note that sufficient permissions are present
**Keyboard** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/keyboard-solid.svg" width="20"> [Press key](https://automagica.readthedocs.io/activities.html#automagica.activities.press_key) | Press and release an entered key. Make sure your keyboard is on US layout (standard QWERTY).If you are using this on Mac Os you might need to grant acces to your terminal application. (Security Preferences > Security & Privacy > Privacy > Accessibility)
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/keyboard-solid.svg" width="20"> [first_key, second_key, third_key=None, compatibility=False, delay=1](https://automagica.readthedocs.io/activities.html#automagica.activities.press_key_combination) | """Press key combination
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/keyboard-solid.svg" width="20"> [Type text](https://automagica.readthedocs.io/activities.html#automagica.activities.typing) | Simulate keystrokes. If an element ID is specified, text will be typed in a specific field or element based on the element ID (vision) by the recorder.
**Mouse** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-solid.svg" width="20"> [Get mouse coordinates](https://automagica.readthedocs.io/activities.html#automagica.activities.get_mouse_position) | Get the x and y pixel coordinates of current mouse position.These coordinates represent the absolute pixel position of the mouse on the computer screen. The x-coördinate starts on the left side and increases going right. The y-coördinate increases going down.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/search-location-solid.svg" width="20"> [Display mouse position](https://automagica.readthedocs.io/activities.html#automagica.activities.display_mouse_position) | Displays mouse position in an overlay. Refreshes every two seconds. Can be used to find mouse position of element on the screen.These coordinates represent the absolute pixel position of the mouse on the computer screen. The x-coördinate starts on the left side and increases going right. The y-coördinate increases going down.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Mouse click](https://automagica.readthedocs.io/activities.html#automagica.activities.click) | Clicks on an element based on the element ID (vision)
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Mouse click coordinates](https://automagica.readthedocs.io/activities.html#automagica.activities.click_coordinates) | Clicks on an element based on pixel position determined by x and y coordinates. To find coordinates one could use display_mouse_position().
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Double mouse click coordinates](https://automagica.readthedocs.io/activities.html#automagica.activities.double_click_coordinates) | Double clicks on a pixel position determined by x and y coordinates.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Double mouse click](https://automagica.readthedocs.io/activities.html#automagica.activities.double_click) | Double clicks on an element based on the element ID (vision)
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Right click](https://automagica.readthedocs.io/activities.html#automagica.activities.right_click) | Right clicks on an element based on the element ID (vision)
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Right click coordinates](https://automagica.readthedocs.io/activities.html#automagica.activities.right_click_coordinates) | Right clicks on an element based pixel position determined by x and y coordinates.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/arrows-alt-solid.svg" width="20"> [Move mouse](https://automagica.readthedocs.io/activities.html#automagica.activities.move_mouse_to) | Moves te pointer to an element based on the element ID (vision)
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/arrows-alt-solid.svg" width="20"> [Move mouse coordinates](https://automagica.readthedocs.io/activities.html#automagica.activities.move_mouse_to_coordinates) | Moves te pointer to an element based on the pixel position determined by x and y coordinates
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/arrows-alt-solid.svg" width="20"> [Move mouse relative](https://automagica.readthedocs.io/activities.html#automagica.activities.move_mouse_relative) | Moves the mouse an x- and y- distance relative to its current pixel position.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/arrows-alt-solid.svg" width="20"> [Drag mouse](https://automagica.readthedocs.io/activities.html#automagica.activities.drag_mouse_to_coordinates) | Drags mouse to an element based on pixel position determined by x and y coordinates
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/arrows-alt-solid.svg" width="20"> [Drag mouse](https://automagica.readthedocs.io/activities.html#automagica.activities.drag_mouse_to) | Drags mouse to an element based on the element ID (vision)
**Image** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/crop-alt-solid.svg" width="20"> [Random screen snippet](https://automagica.readthedocs.io/activities.html#automagica.activities.random_screen_snippet) | Take a random square snippet from the current screen. Mainly for testing and/or development purposes.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/expand-solid.svg" width="20"> [Screenshot](https://automagica.readthedocs.io/activities.html#automagica.activities.take_screenshot) | Take a screenshot of current screen.
**Folder Operations** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/search-solid.svg" width="20"> [input_path=None, extension=None, show_full_path=True, scan_subfolders=False](https://automagica.readthedocs.io/activities.html#automagica.activities.get_files_in_folder) | """List files in folder
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-plus-solid.svg" width="20"> [Create folder](https://automagica.readthedocs.io/activities.html#automagica.activities.create_folder) | Creates new folder at the given path.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-solid.svg" width="20"> [Rename folder](https://automagica.readthedocs.io/activities.html#automagica.activities.rename_folder) | Rename a folder
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-open-solid.svg" width="20"> [Open a folder](https://automagica.readthedocs.io/activities.html#automagica.activities.show_folder) | Open a folder with the default explorer.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-solid.svg" width="20"> [Move a folder](https://automagica.readthedocs.io/activities.html#automagica.activities.move_folder) | Moves a folder from one place to another.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-minus-solid.svg" width="20"> [Remove folder](https://automagica.readthedocs.io/activities.html#automagica.activities.remove_folder) | Remove a folder including all subfolders and files. For the function to work optimal, all files and subfolders in the main targetfolder should be closed.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-minus-solid.svg" width="20"> [Empty folder](https://automagica.readthedocs.io/activities.html#automagica.activities.empty_folder) | Remove all contents from a folderFor the function to work optimal, all files and subfolders in the main targetfolder should be closed.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-solid.svg" width="20"> [Checks if folder exists](https://automagica.readthedocs.io/activities.html#automagica.activities.folder_exists) | Check whether folder exists or not, regardless if folder is empty or not.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/folder-solid.svg" width="20"> [Copy a folder](https://automagica.readthedocs.io/activities.html#automagica.activities.copy_folder) | Copies a folder from one place to another.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/archive-solid.svg" width="20"> [Zip](https://automagica.readthedocs.io/activities.html#automagica.activities.zip_folder) | Zia folder and it's contents. Creates a .zip file.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/archive-solid.svg" width="20"> [Unzip](https://automagica.readthedocs.io/activities.html#automagica.activities.unzip) | Unzips a file or folder from a .zip file.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/clock-solid.svg" width="20"> [Return most recent file in directory](https://automagica.readthedocs.io/activities.html#automagica.activities.most_recent_file) | Return most recent file in directory
**Delay** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/hourglass-solid.svg" width="20"> [Wait](https://automagica.readthedocs.io/activities.html#automagica.activities.wait) | Make the robot wait for a specified number of seconds. Note that this activity is blocking. This means that subsequent activities will not occur until the the specified waiting time has expired.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/hourglass-solid.svg" width="20"> [Wait for folder](https://automagica.readthedocs.io/activities.html#automagica.activities.wait_folder_exists) | Waits until a folder exists.Not that this activity is blocking and will keep the system waiting.
**Word Application** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [self, file_path=None, visible=True,](https://automagica.readthedocs.io/activities.html#automagica.activities.Word) | """Start Word Application
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Save](https://automagica.readthedocs.io/activities.html#automagica.activities.save) | Save active Word document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Save As](https://automagica.readthedocs.io/activities.html#automagica.activities.save_as) | Save active Word document to a specific location
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Append text](https://automagica.readthedocs.io/activities.html#automagica.activities.append_text) | Append text at end of Word document.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Replace text](https://automagica.readthedocs.io/activities.html#automagica.activities.replace_text) | Can be used for example to replace arbitrary placeholder value. For example whenusing template document, using 'XXXX' as a placeholder. Take note that all strings are case sensitive.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Read all text](https://automagica.readthedocs.io/activities.html#automagica.activities.read_all_text) | Read all the text from a document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-pdf-solid.svg" width="20"> [Export to PDF](https://automagica.readthedocs.io/activities.html#automagica.activities.export_to_pdf) | Export the document to PDF
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/html5.svg" width="20"> [Export to HTML](https://automagica.readthedocs.io/activities.html#automagica.activities.export_to_html) | Export to HTML
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/heading-solid.svg" width="20"> [Set footers](https://automagica.readthedocs.io/activities.html#automagica.activities.set_footers) | Set the footers of the document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/subscript-solid.svg" width="20"> [Set headers](https://automagica.readthedocs.io/activities.html#automagica.activities.set_headers) | Set the headers of the document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Quit Word](https://automagica.readthedocs.io/activities.html#automagica.activities.quit) | This closes Word, make sure to use 'save' or 'save_as' if you would like to save before quitting.
**Word File** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Read and Write Word files](https://automagica.readthedocs.io/activities.html#automagica.activities.WordFile) | These activities can read, write and edit Word (docx) files without the need of having Word installed.Note that, in contrary to working with the :func: 'Word' activities, a file get saved directly after manipulation.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Read all text](https://automagica.readthedocs.io/activities.html#automagica.activities.read_all_text) | Read all the text from the document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Append text](https://automagica.readthedocs.io/activities.html#automagica.activities.append_text) | Append text at the end of the document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Save](https://automagica.readthedocs.io/activities.html#automagica.activities.save) | Save document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Save as](https://automagica.readthedocs.io/activities.html#automagica.activities.save_as) | Save file on specified path
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Set headers](https://automagica.readthedocs.io/activities.html#automagica.activities.set_headers) | Set headers of Word document
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Replace all](https://automagica.readthedocs.io/activities.html#automagica.activities.replace_text) | Replaces all occurences of a placeholder text in the document with a replacement text.
**Outlook Application** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Start Outlook Application](https://automagica.readthedocs.io/activities.html#automagica.activities.Outlook) | For this activity to work, Outlook needs to be installed on the system.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [self, to_address, subject="", body="", html_body=None, attachment_paths=None](https://automagica.readthedocs.io/activities.html#automagica.activities.send_mail) | """Send e-mail
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Retrieve folders](https://automagica.readthedocs.io/activities.html#automagica.activities.get_folders) | Retrieve list of folders from Outlook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Retrieve e-mails](https://automagica.readthedocs.io/activities.html#automagica.activities.get_mails) | Retrieve list of messages from Outlook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [self,](https://automagica.readthedocs.io/activities.html#automagica.activities.delete_mails) | limit=0,subject_contains="",body_contains="",sender_contains="",):"""Delete e-mails
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [self,](https://automagica.readthedocs.io/activities.html#automagica.activities.move_mails) | target_folder_name="Archive",limit=0,subject_contains="",body_contains="",sender_contains="",):"""Move e-mails
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Save attachments](https://automagica.readthedocs.io/activities.html#automagica.activities.save_attachments) | Save all attachments from certain folder
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Retrieve contacts](https://automagica.readthedocs.io/activities.html#automagica.activities.get_contacts) | Retrieve all contacts
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Add a contact](https://automagica.readthedocs.io/activities.html#automagica.activities.add_contact) | Add a contact to Outlook contacts
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Quit](https://automagica.readthedocs.io/activities.html#automagica.activities.quit) | Close the Outlook application
**Excel Application** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Start Excel Application](https://automagica.readthedocs.io/activities.html#automagica.activities.Excel) | For this activity to work, Microsoft Office Excel needs to be installed on the system.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Add worksheet](https://automagica.readthedocs.io/activities.html#automagica.activities.add_worksheet) | Adds a worksheet to the current workbook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Activate worksheet](https://automagica.readthedocs.io/activities.html#automagica.activities.activate_worksheet) | Activate a worksheet in the current Excel document by name
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Save](https://automagica.readthedocs.io/activities.html#automagica.activities.save) | Save the current workbook. Defaults to homedir
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Save as](https://automagica.readthedocs.io/activities.html#automagica.activities.save_as) | Save the current workbook to a specific path
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Write cell](https://automagica.readthedocs.io/activities.html#automagica.activities.write_cell) | Write to a specific cell in the currently active workbook and active worksheet
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Read cell](https://automagica.readthedocs.io/activities.html#automagica.activities.read_cell) | Read a cell from the currently active workbook and active worksheet
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Write range](https://automagica.readthedocs.io/activities.html#automagica.activities.write_range) | Write to a specific range in the currently active worksheet in the active workbook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Read range](https://automagica.readthedocs.io/activities.html#automagica.activities.read_range) | Read a range of cells from the currently active worksheet in the active workbook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Run macro](https://automagica.readthedocs.io/activities.html#automagica.activities.run_macro) | Run a macro by name from the currently active workbook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Get worksheet names](https://automagica.readthedocs.io/activities.html#automagica.activities.get_worksheet_names) | Get names of all the worksheets in the currently active workbook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Get table](https://automagica.readthedocs.io/activities.html#automagica.activities.get_table) | Get table data from the currently active worksheet by name of the table
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Activate range](https://automagica.readthedocs.io/activities.html#automagica.activities.activate_range) | Activate a particular range in the currently active workbook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Activate first empty cell down](https://automagica.readthedocs.io/activities.html#automagica.activities.activate_first_empty_cell_down) | Activates the first empty cell going down
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Activate first empty cell right](https://automagica.readthedocs.io/activities.html#automagica.activities.activate_first_empty_cell_right) | Activates the first empty cell going right
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Activate first empty cell left](https://automagica.readthedocs.io/activities.html#automagica.activities.activate_first_empty_cell_left) | Activates the first empty cell going left
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Activate first empty cell up](https://automagica.readthedocs.io/activities.html#automagica.activities.activate_first_empty_cell_up) | Activates the first empty cell going up
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Write cell formula](https://automagica.readthedocs.io/activities.html#automagica.activities.write_cell_formula) | Write a formula to a particular cell
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Read cell formula](https://automagica.readthedocs.io/activities.html#automagica.activities.read_cell_formula) | Read the formula from a particular cell
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Insert empty row](https://automagica.readthedocs.io/activities.html#automagica.activities.insert_empty_row) | Inserts an empty row to the currently active worksheet
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Insert empty column](https://automagica.readthedocs.io/activities.html#automagica.activities.insert_empty_column) | Inserts an empty column in the currently active worksheet. Existing columns will shift to the right.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Delete row in Excel](https://automagica.readthedocs.io/activities.html#automagica.activities.delete_row) | Deletes a row from the currently active worksheet. Existing data will shift up.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Delete column](https://automagica.readthedocs.io/activities.html#automagica.activities.delete_column) | Delete a column from the currently active worksheet. Existing columns will shift to the left.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Export to PDF](https://automagica.readthedocs.io/activities.html#automagica.activities.export_to_pdf) | Export to PDF
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Insert data as table](https://automagica.readthedocs.io/activities.html#automagica.activities.insert_data_as_table) | Insert list of dictionaries as a table in Excel
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Read worksheet](https://automagica.readthedocs.io/activities.html#automagica.activities.read_worksheet) | Read data from a worksheet as a list of lists
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Quit Excel](https://automagica.readthedocs.io/activities.html#automagica.activities.quit) | This closes Excel, make sure to use 'save' or 'save_as' if you would like to save before quitting.
**Excel File** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Read and Write xlsx files.](https://automagica.readthedocs.io/activities.html#automagica.activities.ExcelFile) | This activity can read, write and edit Excel (xlsx) files without the need of having Excel installed.Note that, in contrary to working with the :func: 'Excel' activities, a file get saved directly after manipulation.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Export file to dataframe](https://automagica.readthedocs.io/activities.html#automagica.activities.to_dataframe) | Export to pandas dataframe
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Activate worksheet](https://automagica.readthedocs.io/activities.html#automagica.activities.activate_worksheet) | Activate a worksheet. By default the first worksheet is activated.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Save as](https://automagica.readthedocs.io/activities.html#automagica.activities.save_as) | Save file as
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Save as](https://automagica.readthedocs.io/activities.html#automagica.activities.save) | Save file
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Write cell](https://automagica.readthedocs.io/activities.html#automagica.activities.write_cell) | Write a cell based on column and row
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Read cell](https://automagica.readthedocs.io/activities.html#automagica.activities.read_cell) | Read a cell based on column and row
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Add worksheet](https://automagica.readthedocs.io/activities.html#automagica.activities.add_worksheet) | Add a worksheet
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-excel-solid.svg" width="20"> [Get worksheet names](https://automagica.readthedocs.io/activities.html#automagica.activities.get_worksheet_names) | Get worksheet names
**PowerPoint Application** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Start PowerPoint Application](https://automagica.readthedocs.io/activities.html#automagica.activities.PowerPoint) | For this activity to work, PowerPoint needs to be installed on the system.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Save PowerPoint](https://automagica.readthedocs.io/activities.html#automagica.activities.save_as) | Save PowerPoint Slidedeck
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Save PowerPoint](https://automagica.readthedocs.io/activities.html#automagica.activities.save) | Save PowerPoint Slidedeck
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Close PowerPoint Application](https://automagica.readthedocs.io/activities.html#automagica.activities.quit) | Close PowerPoint
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Add PowerPoint Slides](https://automagica.readthedocs.io/activities.html#automagica.activities.add_slide) | Adds slides to a presentation
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Slide count](https://automagica.readthedocs.io/activities.html#automagica.activities.number_of_slides) | Returns the number of slides
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [self,](https://automagica.readthedocs.io/activities.html#automagica.activities.add_text) | index=None,font_size=48,font_name=None,bold=False,margin_bottom=100,margin_left=100,margin_right=100,margin_top=100,):"""Text to slide
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Delete slide](https://automagica.readthedocs.io/activities.html#automagica.activities.delete_slide) | Delete a slide
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Replace all occurences of text in PowerPoint slides](https://automagica.readthedocs.io/activities.html#automagica.activities.replace_text) | Can be used for example to replace arbitrary placeholder value in a PowerPoint.For example when using a template slidedeck, using 'XXXX' as a placeholder.Take note that all strings are case sensitive.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [PowerPoint to PDF](https://automagica.readthedocs.io/activities.html#automagica.activities.export_to_pdf) | Export PowerPoint presentation to PDF file
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-powerpoint-solid.svg" width="20"> [Slides to images](https://automagica.readthedocs.io/activities.html#automagica.activities.export_slides_to_images) | Export PowerPoint slides to seperate image files
**Office 365** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/envelope-solid.svg" width="20"> [Send email Office Outlook 365](https://automagica.readthedocs.io/activities.html#automagica.activities.send_email_with_outlook365) | Send email Office Outlook 365
**Salesforce** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/salesforce.svg" width="20"> [Salesforce API](https://automagica.readthedocs.io/activities.html#automagica.activities.salesforce_api_call) | Activity to make calls to Salesforce REST API.
**E-mail (SMTP)** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [smtp_host, smtp_user, smtp_password, to_address, subject="", message="", port=587](https://automagica.readthedocs.io/activities.html#automagica.activities.send_mail_smtp) | """Mail with SMTP
**Windows OS** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/readme.svg" width="20"> [Find window with specific title](https://automagica.readthedocs.io/activities.html#automagica.activities.find_window_title) | Find a specific window based on the name, either a perfect match or a partial match.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/passport-solid.svg" width="20"> [ip, username, password=None, desktop_width=1920, desktop_height=1080](https://automagica.readthedocs.io/activities.html#automagica.activities.start_remote_desktop) | """Login to Windows Remote Desktop
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/passport-solid.svg" width="20"> [Stop Windows Remote Desktop](https://automagica.readthedocs.io/activities.html#automagica.activities.close_remote_desktop) | Stop Windows Remote Desktop
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/passport-solid.svg" width="20"> [Set Windows password](https://automagica.readthedocs.io/activities.html#automagica.activities.set_user_password) | Sets the password for a Windows user.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/passport-solid.svg" width="20"> [Check Windows password](https://automagica.readthedocs.io/activities.html#automagica.activities.validate_user_password) | Validates a Windows user password if it is correct
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/user-lock-solid.svg" width="20"> [Lock Windows](https://automagica.readthedocs.io/activities.html#automagica.activities.lock_windows) | Locks Windows requiring login to continue.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/user-solid.svg" width="20"> [Check if Windows logged in](https://automagica.readthedocs.io/activities.html#automagica.activities.is_logged_in) | Checks if the current user is logged in and not on the lockscreen. Most automations do not work properly when the desktop is locked.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/user-solid.svg" width="20"> [Check if Windows is locked](https://automagica.readthedocs.io/activities.html#automagica.activities.is_desktop_locked) | Checks if the current user is locked out and on the lockscreen. Most automations do not work properly when the desktop is locked.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/user-solid.svg" width="20"> [Get Windows username](https://automagica.readthedocs.io/activities.html#automagica.activities.get_username) | Get current logged in user's username
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/clipboard-check-solid.svg" width="20"> [Set clipboard](https://automagica.readthedocs.io/activities.html#automagica.activities.set_to_clipboard) | Set any text to the Windows clipboard.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/clipboard-list-solid.svg" width="20"> [Get clipboard](https://automagica.readthedocs.io/activities.html#automagica.activities.get_from_clipboard) | Get the text currently in the Windows clipboard
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/clipboard-solid.svg" width="20"> [Empty clipboard](https://automagica.readthedocs.io/activities.html#automagica.activities.clear_clipboard) | Empty text from clipboard. Getting clipboard data after this should return in None
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cogs-solid.svg" width="20"> [Run VBSscript](https://automagica.readthedocs.io/activities.html#automagica.activities.run_vbs_script) | Run a VBScript file
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/volume-up-solid.svg" width="20"> [Beep](https://automagica.readthedocs.io/activities.html#automagica.activities.beep) | Make a beeping sound. Make sure your volume is up and you have hardware connected.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/ethernet-solid.svg" width="20"> [Get all network interface names](https://automagica.readthedocs.io/activities.html#automagica.activities.get_all_network_interface_names) | Returns a list of all network interfaces of the current machine
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/ethernet-solid.svg" width="20"> [Enable network interface](https://automagica.readthedocs.io/activities.html#automagica.activities.enable_network_interface) | Enables a network interface by its name.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/ethernet-solid.svg" width="20"> [Disable network interface](https://automagica.readthedocs.io/activities.html#automagica.activities.disable_network_interface) | Disables a network interface by its name.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/print-solid.svg" width="20"> [Get default printer](https://automagica.readthedocs.io/activities.html#automagica.activities.get_default_printer_name) | Returns the name of the printer selected as default
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/print-solid.svg" width="20"> [Set default printer](https://automagica.readthedocs.io/activities.html#automagica.activities.set_default_printer) | Set the default printer.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/print-solid.svg" width="20"> [Remove printer](https://automagica.readthedocs.io/activities.html#automagica.activities.remove_printer) | Removes a printer by its name
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cog-solid.svg" width="20"> [Get service status](https://automagica.readthedocs.io/activities.html#automagica.activities.get_service_status) | Returns the status of a service on the machine
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cog-solid.svg" width="20"> [Start a service](https://automagica.readthedocs.io/activities.html#automagica.activities.start_service) | Starts a Windows service
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cog-solid.svg" width="20"> [Stop a service](https://automagica.readthedocs.io/activities.html#automagica.activities.stop_service) | Stops a Windows service
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Set window to foreground](https://automagica.readthedocs.io/activities.html#automagica.activities.set_window_to_foreground) | Sets a window to foreground by its title.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Get foreground window title](https://automagica.readthedocs.io/activities.html#automagica.activities.get_foreground_window_title) | Retrieve the title of the current foreground window
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Close window](https://automagica.readthedocs.io/activities.html#automagica.activities.close_window) | Closes a window by its title
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Maximize window](https://automagica.readthedocs.io/activities.html#automagica.activities.maximize_window) | Maximizes a window by its title
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Restore window](https://automagica.readthedocs.io/activities.html#automagica.activities.restore_window) | Restore a window by its title
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Minimize window](https://automagica.readthedocs.io/activities.html#automagica.activities.minimize_window) | Minimizes a window by its title
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Resize window](https://automagica.readthedocs.io/activities.html#automagica.activities.resize_window) | Resize a window by its title
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-restore-solid.svg" width="20"> [Hide window](https://automagica.readthedocs.io/activities.html#automagica.activities.hide_window) | Hides a window from the user desktop by using it's title
**Terminal** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/terminal-solid.svg" width="20"> [Run SSH command](https://automagica.readthedocs.io/activities.html#automagica.activities.run_ssh_command) | Runs a command over SSH (Secure Shell)
**SNMP** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/ethernet-solid.svg" width="20"> [SNMP Get](https://automagica.readthedocs.io/activities.html#automagica.activities.snmp_get) | Retrieves data from an SNMP agent using SNMP (Simple Network Management Protocol)
**Active Directory** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/audio-description-solid.svg" width="20"> [AD interface](https://automagica.readthedocs.io/activities.html#automagica.activities.ActiveDirectory) | Interface to Windows Active Directory through ADSI. Connects to the AD domain to which the machine is joined by default.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/audio-description-solid.svg" width="20"> [Get AD object by name](https://automagica.readthedocs.io/activities.html#automagica.activities.get_object_by_distinguished_name) | Interface to Windows Active Directory through ADSI
**Utilities** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/home-solid.svg" width="20"> [Get user home path](https://automagica.readthedocs.io/activities.html#automagica.activities.home_path) | Returns the current user's home path
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/desktop-solid.svg" width="20"> [Get desktop path](https://automagica.readthedocs.io/activities.html#automagica.activities.desktop_path) | Returns the current user's desktop path
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/download-solid.svg" width="20"> [Get downloads path](https://automagica.readthedocs.io/activities.html#automagica.activities.downloads_path) | Returns the current user's default download path
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-solid.svg" width="20"> [Open file](https://automagica.readthedocs.io/activities.html#automagica.activities.open_file) | Opens file with default programs
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/desktop-solid.svg" width="20"> [Set wallpaper](https://automagica.readthedocs.io/activities.html#automagica.activities.set_wallpaper) | Set Windows desktop wallpaper with the the specified image
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cloud-download-alt-solid.svg" width="20"> [Download file from a URL](https://automagica.readthedocs.io/activities.html#automagica.activities.download_file_from_url) | Download file from a URL
**System** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-contract-solid.svg" width="20"> [Rename a file](https://automagica.readthedocs.io/activities.html#automagica.activities.rename_file) | This activity will rename a file. If the the desired name already exists in the folder file will not be renamed. Make sure to add the exstention to specify filetype.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-export-solid.svg" width="20"> [Move a file](https://automagica.readthedocs.io/activities.html#automagica.activities.move_file) | If the new location already contains a file with the same name.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/trash-solid.svg" width="20"> [Remove a file](https://automagica.readthedocs.io/activities.html#automagica.activities.remove_file) | Remove a file
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/tasks-solid.svg" width="20"> [Check if file exists](https://automagica.readthedocs.io/activities.html#automagica.activities.file_exists) | This function checks whether the file with the given path exists.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/list-alt-solid.svg" width="20"> [Wait until a file exists.](https://automagica.readthedocs.io/activities.html#automagica.activities.wait_file_exists) | Not that this activity is blocking and will keep the system waiting.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/list-solid.svg" width="20"> [List to .txt](https://automagica.readthedocs.io/activities.html#automagica.activities.write_list_to_file) | Writes a list to a  text (.txt) file.Every element of the entered list is written on a new line of the text file.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/th-list-solid.svg" width="20"> [Read list from .txt file](https://automagica.readthedocs.io/activities.html#automagica.activities.read_list_from_txt) | This activity reads the content of a .txt file to a list and returns that list.Every new line from the .txt file becomes a new element of the list. The activity willnot work if the entered path is not attached to a .txt file.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/th-list-solid.svg" width="20"> [Read .txt file](https://automagica.readthedocs.io/activities.html#automagica.activities.read_from_txt) | This activity reads a .txt file and returns the content
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/tasks-solid.svg" width="20"> [Append to .txt](https://automagica.readthedocs.io/activities.html#automagica.activities.append_line) | Append a text line to a file and creates the file if it does not exist yet.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-alt-solid.svg" width="20"> [Make text file](https://automagica.readthedocs.io/activities.html#automagica.activities.make_text_file) | Initialize text file
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/copy-solid.svg" width="20"> [Read .txt file with newlines to list](https://automagica.readthedocs.io/activities.html#automagica.activities.read_text_file_to_list) | Read a text file to a Python list-object
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/copy-solid.svg" width="20"> [Copy a file](https://automagica.readthedocs.io/activities.html#automagica.activities.copy_file) | Copies a file from one place to another.If the new location already contains a file with the same name, a random 4 character uid is added to the name.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/info-solid.svg" width="20"> [Get file extension](https://automagica.readthedocs.io/activities.html#automagica.activities.get_file_extension) | Get extension of a file
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/print-solid.svg" width="20"> [Print](https://automagica.readthedocs.io/activities.html#automagica.activities.send_to_printer) | Send file to default printer to priner. This activity sends a file to the printer. Make sure to have a default printer set up.
**PDF** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/glasses-solid.svg" width="20"> [Text from PDF](https://automagica.readthedocs.io/activities.html#automagica.activities.read_text_from_pdf) | Extracts the text from a PDF. This activity reads text from a pdf file. Can only read PDF files that contain a text layer.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/object-ungroup-solid.svg" width="20"> [first_file_path, second_file_path, third_file_path=None, output_path=None](https://automagica.readthedocs.io/activities.html#automagica.activities.join_pdf_files) | """Merge PDF
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cut-solid.svg" width="20"> [Extract page from PDF](https://automagica.readthedocs.io/activities.html#automagica.activities.extract_page_range_from_pdf) | Extracts a particular range of a PDF to a separate file.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/icons-solid.svg" width="20"> [Extract images from PDF](https://automagica.readthedocs.io/activities.html#automagica.activities.extract_images_from_pdf) | Save a specific page from a PDF as an image
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/stamp-solid.svg" width="20"> [Watermark a PDF](https://automagica.readthedocs.io/activities.html#automagica.activities.apply_watermark_to_pdf) | Watermark a PDF
**System Monitoring** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/microchip-solid.svg" width="20"> [CPU load](https://automagica.readthedocs.io/activities.html#automagica.activities.get_cpu_load) | Get average CPU load for all cores.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/calculator-solid.svg" width="20"> [Count CPU](https://automagica.readthedocs.io/activities.html#automagica.activities.get_number_of_cpu) | Get the number of CPU's in the current system.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/wave-square-solid.svg" width="20"> [CPU frequency](https://automagica.readthedocs.io/activities.html#automagica.activities.get_cpu_frequency) | Get frequency at which CPU currently operates.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/server-solid.svg" width="20"> [CPU Stats](https://automagica.readthedocs.io/activities.html#automagica.activities.get_cpu_stats) | Get CPU statistics
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/memory-solid.svg" width="20"> [Memory statistics](https://automagica.readthedocs.io/activities.html#automagica.activities.get_memory_stats) | Get  memory statistics
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/save-solid.svg" width="20"> [Disk stats](https://automagica.readthedocs.io/activities.html#automagica.activities.get_disk_stats) | Get disk statistics of main disk
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/save-solid.svg" width="20"> [Partition info](https://automagica.readthedocs.io/activities.html#automagica.activities.get_disk_partitions) | Get disk partition info
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/clock-solid.svg" width="20"> [Boot time](https://automagica.readthedocs.io/activities.html#automagica.activities.get_boot_time) | Get most recent boot time
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/clock-solid.svg" width="20"> [Uptime](https://automagica.readthedocs.io/activities.html#automagica.activities.get_time_since_last_boot) | Get uptime since last boot
**Image Processing** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/images-solid.svg" width="20"> [Show image](https://automagica.readthedocs.io/activities.html#automagica.activities.show_image) | Displays an image specified by the path variable on the default imaging program.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/undo-solid.svg" width="20"> [Rotate image](https://automagica.readthedocs.io/activities.html#automagica.activities.rotate_image) | Rotate an image
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/expand-arrows-alt-solid.svg" width="20"> [Resize image](https://automagica.readthedocs.io/activities.html#automagica.activities.resize_image) | Resizes the image specified by the path variable.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/expand-arrows-alt-solid.svg" width="20"> [Get image width](https://automagica.readthedocs.io/activities.html#automagica.activities.get_image_width) | Get with of image
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/arrows-alt-v-solid.svg" width="20"> [Get image height](https://automagica.readthedocs.io/activities.html#automagica.activities.get_image_height) | Get height of image
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/crop-solid.svg" width="20"> [Crop image](https://automagica.readthedocs.io/activities.html#automagica.activities.crop_image) | Crops the image specified by path to a region determined by the box variable.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/caret-up-solid.svg" width="20"> [Mirror image horizontally](https://automagica.readthedocs.io/activities.html#automagica.activities.mirror_image_horizontally) | Mirrors an image with a given path horizontally from left to right.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/caret-right-solid.svg" width="20"> [Mirror image vertically](https://automagica.readthedocs.io/activities.html#automagica.activities.mirror_image_vertically) | Mirrors an image with a given path vertically from top to bottom.
**Process** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cog-solid.svg" width="20"> [Windows run](https://automagica.readthedocs.io/activities.html#automagica.activities.run_manual) | Use Windows Run to boot a processNote this uses keyboard inputs which means this process can be disrupted by interfering inputs
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/play-solid.svg" width="20"> [Run process](https://automagica.readthedocs.io/activities.html#automagica.activities.run) | Use subprocess to open a windows process
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/cogs-solid.svg" width="20"> [Check if process is running](https://automagica.readthedocs.io/activities.html#automagica.activities.is_process_running) | Check if process is running. Validates if given process name (name) is currently running on the system.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/list-solid.svg" width="20"> [Get running processes](https://automagica.readthedocs.io/activities.html#automagica.activities.get_running_processes) | Get names of unique processes currently running on the system.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/window-close-solid.svg" width="20"> [Kill process](https://automagica.readthedocs.io/activities.html#automagica.activities.kill_process) | Kills a process forcefully
**Optical Character Recognition (OCR)** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/readme.svg" width="20"> [Get text with OCR](https://automagica.readthedocs.io/activities.html#automagica.activities.extract_text_ocr) | This activity extracts all text from the current screen or an image if a path is specified.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/glasses-solid.svg" width="20"> [Find text on screen with OCR](https://automagica.readthedocs.io/activities.html#automagica.activities.find_text_on_screen_ocr) | This activity finds position (coordinates) of specified text on the current screen using OCR.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Click on text with OCR](https://automagica.readthedocs.io/activities.html#automagica.activities.click_on_text_ocr) | This activity clicks on position (coordinates) of specified text on the current screen using OCR.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Double click on text with OCR](https://automagica.readthedocs.io/activities.html#automagica.activities.double_click_on_text_ocr) | This activity double clicks on position (coordinates) of specified text on the current screen using OCR.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mouse-pointer-solid.svg" width="20"> [Right click on text with OCR](https://automagica.readthedocs.io/activities.html#automagica.activities.right_click_on_text_ocr) | This activity Right clicks on position (coordinates) of specified text on the current screen using OCR.
**UiPath** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/robot-solid.svg" width="20"> [Execute a UiPath process](https://automagica.readthedocs.io/activities.html#automagica.activities.execute_uipath_process) | This activity allows you to execute a process designed with the UiPath Studio. All console output from the Write Line activity (https://docs.uipath.com/activities/docs/write-line) will be printed as output.
**AutoIt** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/robot-solid.svg" width="20"> [Execute a AutoIt script](https://automagica.readthedocs.io/activities.html#automagica.activities.run_autoit_script) | This activity allows you to run an AutoIt script. If you use the ConsoleWrite function (https://www.autoitscript.com/autoit3/docs/functions/ConsoleWrite.htm), the output will be presented to you.
**Robot Framework** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/robot-solid.svg" width="20"> [Execute a Robot Framework test case](https://automagica.readthedocs.io/activities.html#automagica.activities.execute_robotframework_test) | This activity allows you to run a Robot Framework test case. Console output of the test case will be printed.
**Blue Prism** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/robot-solid.svg" width="20"> [process_name,](https://automagica.readthedocs.io/activities.html#automagica.activities.run_blueprism_process) | password="",sso=False,inputs=None,automatec_exe_path=None,):"""Run a Blue Prism process
**Automation Anywhere** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/briefcase-solid.svg" width="20"> [Run an Automation Anywhere task](https://automagica.readthedocs.io/activities.html#automagica.activities.run_automationanywhere_task) | This activity allows you to run an Automation Anywhere task.
**SAP GUI** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/briefcase-solid.svg" width="20"> [Quit SAP GUI](https://automagica.readthedocs.io/activities.html#automagica.activities.quit) | Quits the SAP GUI completely and forcibly.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/briefcase-solid.svg" width="20"> [Log in to SAP GUI](https://automagica.readthedocs.io/activities.html#automagica.activities.login) | Logs in to an SAP system on SAP GUI.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/briefcase-solid.svg" width="20"> [Click on a sAP GUI element](https://automagica.readthedocs.io/activities.html#automagica.activities.click_sap) | Clicks on an identifier in the SAP GUI.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/briefcase-solid.svg" width="20"> [Get text from a SAP GUI element](https://automagica.readthedocs.io/activities.html#automagica.activities.get_text) | Retrieves the text from a SAP GUI element.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/briefcase-solid.svg" width="20"> [Set text of a SAP GUI element](https://automagica.readthedocs.io/activities.html#automagica.activities.set_text) | Sets the text of a SAP GUI element.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/briefcase-solid.svg" width="20"> [Highlights a SAP GUI element](https://automagica.readthedocs.io/activities.html#automagica.activities.highlight) | Temporarily highlights a SAP GUI element
**Portal** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/robot-solid.svg" width="20"> [process_name, process_version_id=None, priority=0, parameters=None](https://automagica.readthedocs.io/activities.html#automagica.activities.create_new_job_in_portal) | """Create a new job in the Automagica Portal
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/key-solid.svg" width="20"> [Get a credential from the Automagica Portal](https://automagica.readthedocs.io/activities.html#automagica.activities.get_credential_from_portal) | This activity retrieves a credential from the Automagica Portal.
**Vision** | ‌‌ 
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/eye-solid.svg" width="20"> [Check if element is visible on screen](https://automagica.readthedocs.io/activities.html#automagica.activities.is_visible) | This activity can be used to check if a certain element is visible on the screen.Note that this uses Automagica vision and uses some advanced an fuzzy matching algorithms for finding identical elements.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/eye-solid.svg" width="20"> [Wait for an element to appear](https://automagica.readthedocs.io/activities.html#automagica.activities.wait_appear) | Wait for an element that is defined the recorder
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/eye-solid.svg" width="20"> [Detect and click on an element with the Automagica Vision API](https://automagica.readthedocs.io/activities.html#automagica.activities.wait_vanish) | This activity allows the bot to detect and click on an element by using the Automagica Vision API with a provided sample ID.
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/eye-solid.svg" width="20"> [Detect and click on an element with the Automagica Vision API](https://automagica.readthedocs.io/activities.html#automagica.activities.read_text) | This activity allows the bot to detect and click on an element by using the Automagica Vision API with a provided sample ID.
|<img width=150/>|  ‌‌|

## Credits
Under the hood, Automagica is built on some of the greatest open source libraries. Within Automagica, the following libraries are currently included:
- [requests](https://github.com/psf/requests) 
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [Selenium](https://github.com/baijum/selenium-python) 
- [OpenPyXL](https://bitbucket.org/openpyxl/openpyxl)
- [python-docx](https://github.com/python-openxml/python-docx)
- [pywin32](https://github.com/mhammond/pywin32)
- [PyPDF2](https://github.com/mstamy2/PyPDF2)
- [Psutil](https://pypi.org/project/psutil/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Faker](https://github.com/joke2k/faker)
- [Psutil](https://pypi.org/project/psutil/)
- [Keyring](https://pypi.org/project/keyring/)
- [Cryptography](https://pypi.org/project/cryptography/)
- [pyad](https://pypi.org/project/pyad/)
- [Icons8 Line Awesome](https://github.com/icons8/line-awesome)
- [pysnmp](https://github.com/etingof/pysnmp) and special thanks to [quicksnmp](https://github.com/alessandromaggio/quicksnmp)
- [pandas](https://github.com/pandas-dev/pandas)
- Keyboard
- Babel
- Click

## Contributing


### Developers
You can contribute in the following ways:
- Pull requests with code and/or documentation
- Feature requests, bug squatting, feel free to [create an issue](https://github.com/automagica/automagica/issues)!
- If you're interested in joining our team, [send us an e-mail](mailto:koen@automagica.com).
 

### Not a developer?
No problem! You can contribute in the following ways:
- __Star our repository__ by clicking the star icon at the top right of this page. This allows us to get more exposure within the GitHub community. The more people we can get involved the better!
- Miss a particular feature? [Create an 'issue'](https://github.com/automagica/automagica/issues)
- Something not working? [Create an issue](https://github.com/automagica/automagica/issues)
- Don't have a GitHub account? Feel free to send us an e-mail at [koen@automagica.com](mailto:koen@automagica.com) or [thomas@automagica.com](mailto:thomas@automagica.com).


#### Special contributor mentions
- [ygxiao](https://github.com/ygxiao)
- [jjlehtinen](https://github.com/jjlehtinen)
- [gopal-y](https://github.com/gopal-y)


A special thanks goes out to all the above-mentioned libraries, repositories and contributers! :heart:

<img src="https://i.imgur.com/eQYywRd.png" width="300">

## Licensing

### Copyright and licensing
All source code and other files in this repository, unless stated otherwise, are copyright of Oakwood Technologies BVBA.

### Commercial license
Need a commercial license for Automagica or would you like to embed Automagica or its capabilities in your software offerings or services? Contact us at [sales@automagica.com](mailto:sales@automagica.com).
