![](https://automagica.com/wp-content/uploads/2020/06/logo.png)
# Automagica - Open Source Robotic Process Automation
[Website](https://www.automagica.com) | [Portal](https://portal.automagica.com) | [Documentation](https://automagica.readthedocs.io) | [YouTube](https://automagi.ca/youtube) | [Roadmap](https://automagi.ca/roadmap) | [Discord](https://discord.gg/PbY85WA) | [Telegram](https://t.me/automagica)

[![Downloads](https://pepy.tech/badge/automagica/month)](https://pepy.tech/project/automagica/month)

__[Automagica](https://automagica.com)__ is an open source __automation suite__ for fully automating tedious, manual tasks on any screen. Our vision is that __people should not be doing a robot's job__. Our mission is to make these automation tools as accessible as possible to empower everyone to automate (almost) anything. 

_"Let __bots__ handle the __clicks__ so __people__ can handle the __business__."_

![Love Automagica Example](https://i.imgur.com/uU2OX1X.gif)

## Get started

### Windows

The easiest way to install Automagica is by using our __one-click installer for Windows__ which you can get at the [Automagica Portal](https://portal.automagica.com).

![Portal and Flow](https://i.imgur.com/ps1Uhck.png)

### Linux
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
#### Importing activities

Before getting started in development mode, don't forget to import the activities from automagica in your Python script. If unsure, it is possible to import all the activities for development purposes by starting your script with:
```
from automagica import *
```

Important: for some activities (mainly OCR-related) an Automagica API-key is required. In order to acquire an API-key, you need to register at the [Automagica Portal](https://portal.automagica.com).

## Components
The Automagica suite consists of the following components:
- __Automagica Bot__: runtime/agent responsible for performing the automated tasks.
- __Automagica Flow__: a visual flow designer to build automations quickly with full support for Python code.
- __Automagica Wand__: UI element picker powered by AI.
- __Automagica Lab__: Notebook-style automation development environment based on Jupyter Notebooks (requires Jupyter to be installed).
- __Automagica Portal__: management of bots, credentials, automations, logs, ...

Some activities access external services hosted on our servers, such as the AI and OCR-related capabilities.

The Automagica Portal is currently not available under an open source license. We offer a free environment for evaluation purposes at https://portal.automagica.com. If you would like to use the Automagica Portal within your company or organization, please contact us at sales@automagica.com.

## Automagica & Docker
All Automagica components can run inside Docker containers. Find out more in our [documentation](https://automagica.readthedocs.io/docker.html).

## Example

Browser working with Excel:

![Excel Example Automagica](https://automagica.com/wp-content/uploads/2020/06/browser_excel.gif)


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
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/chrome.svg" width="20"> [Open Chrome Browser](https://automagica.readthedocs.io/activities.html#automagica.activities.Chrome) | Open the Chrome Browser with the Selenium webdriver. Canb be used to automate manipulations in the browser.Different elements can be found as:
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
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/keyboard-solid.svg" width="20"> [Press key combination](https://automagica.readthedocs.io/activities.html#automagica.activities.press_key_combination) | Press a combination of two or three keys simultaneously. Make sure your keyboard is on US layout (standard QWERTY).
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
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/search-solid.svg" width="20"> [List files in folder](https://automagica.readthedocs.io/activities.html#automagica.activities.get_files_in_folder) | List all files in a folder (and subfolders)Checks all folders and subfolders for files. This could take some time for large repositories.
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
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/file-word-solid.svg" width="20"> [Start Word Application](https://automagica.readthedocs.io/activities.html#automagica.activities.Word) | For this activity to work, Microsoft Office Word needs to be installed on the system.
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
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Send e-mail](https://automagica.readthedocs.io/activities.html#automagica.activities.send_mail) | Send an e-mail using Outlook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Retrieve folders](https://automagica.readthedocs.io/activities.html#automagica.activities.get_folders) | Retrieve list of folders from Outlook
<img src="https://cdn.jsdelivr.net/npm/line-awesome@1.3.0/svg/mail-bulk-solid.svg" width="20"> [Retrieve e-mails](https://automagica.readthedocs.io/activities.html#automagica.activities.get_mails) | Retrieve list of messages from Outlook
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
You can also reach out directly to one of the founders: Koen ([koen@automagica.com](mailto:koen@automagica.com)) or Thomas ([thomas@automagica.com](thomas@automagica.com)).