"""Copyright 2020 Oakwood Technologies BVBA"""


from automagica.activities import *
from pathlib import Path
import pytest

def test_activity_requirements():
    """
    Test whether all Automagica activities are defined correctly
    """
    from automagica.utilities import AUTOMAGICA_ACTIVITIES, all_activities

    # Test whether each function listed in AUTOMAGICA_ACTIVITIES

    assert len(all_activities()) == len(AUTOMAGICA_ACTIVITIES)

    for key, activity in all_activities().items():
    
        # Test that the activity has: 
    
        # - a name?
        assert activity.get('name')

        # - a description?
        assert activity.get('description')

        # - an icon?
        assert activity.get('icon')

        # - icon that begins with 'la' (line awesome)
        assert activity['icon'].startswith('la')

        # - keywords?
        assert activity.get('keywords')

        # - docstring parameters matching the function signature?
        import inspect 

        f = activity.get('function')

        signature = inspect.signature(f)
        params = signature.parameters

        function_signature_params = list(params.keys())

        if 'self' in function_signature_params:
            function_signature_params.remove('self')

        docstring_lines = [
            line.strip() for line in f.__doc__.split("\n") if line.strip()
        ]

        docstring_params = []

        for line in docstring_lines:
            if line.startswith(':parameter'):
                name = line.split(":")[1].replace("parameter ", "")
                docstring_params.append(name)

        print(key)
        assert set(function_signature_params) == set(docstring_params)

        # - a return paramater in docstring (if applicable)


def test_excel_activities():
    """
    Test scenario for testing Excel activities (requires Microsoft Excel)
    """
    from automagica.activities import Excel

    # Open Excel
    excel = Excel()

    # Write cell activity
    excel.write_cell(1, 1, "Testing")

    # Read the result
    result = excel.read_cell(1, 1)

    # Quit Excel
    excel.quit()

    assert result == "Testing"


@pytest.fixture
def chrome_browser():
    from automagica.activities import Chrome

    chrome = Chrome(headless=True)

    yield chrome

    chrome.quit()


def test_chrome_activities(chrome_browser):
    """
    Test scenario for testing Chrome browser activities (requires Google Chrome)
    """

    # Browse to Google
    chrome_browser.browse_to("https://google.com")

    # Save the page source
    source = chrome_browser.page_source

    assert "Google" in source


def test_wand_activities(monkeypatch):
    """
    Test wand activities
    """

    from automagica.activities import (
        click,
        double_click,
        right_click,
        move_mouse_to,
        drag_mouse_to,
    )

    # Mock test element
    test_element = "qf41"

    def patched_detect_vision(*args, **kwargs):
        """Patch detect vision function to return coordinates"""
        return [0, 0, 10, 10]

    # Apply patch
    monkeypatch.setattr(
        "automagica.activities.detect_vision", patched_detect_vision
    )

    # Test click
    click(test_element)

    # Test double_click
    double_click(test_element)

    # Test right_click
    right_click(test_element)

    # Test move_mouse_to
    move_mouse_to(test_element)

    # Test drag_mouse_to
    drag_mouse_to(test_element)

    assert True


def test_cryptography_activities():
    """
    Test scenario to test encrypting and decrypting activities
    """
    from automagica.activities import (
        generate_random_key,
        encrypt_text_with_key,
        decrypt_text_with_key,
    )

    # Generate a random key
    key = generate_random_key()

    # Encrypt text with generated key
    encrypted_text = encrypt_text_with_key("Testing", key)

    # Decrypt text with same key
    decrypted_text = decrypt_text_with_key(encrypted_text, key)

    assert decrypted_text == "Testing"


def test_generate_random_key():
    """
    Test Random key
    """
    from automagica.activities import generate_random_key

    # Generate a random key
    key = generate_random_key()

    assert type(key) is bytes


def test_encrypt_text_with_key():
    """
    Test Encrypt text
    """
    from automagica.activities import (
        generate_random_key,
        encrypt_text_with_key,
    )

    # Generate a random key
    key = generate_random_key()
    # Encrypt text with this key
    outcome = encrypt_text_with_key("Sample text", key)

    assert type(outcome) is bytes


def test_decrypt_text_with_key():
    """
    Test Decrypt text
    """
    from automagica.activities import (
        generate_random_key,
        encrypt_text_with_key,
        decrypt_text_with_key,
    )

    # Generate a random key
    key = generate_random_key()
    # Encrypt text with generated key
    encrypted_text = encrypt_text_with_key("Sample text", key)
    # Decrypt text with same key
    decrypted_text = decrypt_text_with_key(encrypted_text, key)

    assert "Sample text" == decrypted_text


def test_encrypt_file_with_key():
    """
    Test Encrypt file
    """
    from automagica.activities import (
        generate_random_key,
        make_text_file,
        encrypted_file,
    )

    # Generate a random key
    key = generate_random_key()

    # Create a text file to illustrate file encryption
    text_file_path = make_text_file()

    # Encrypt the text file
    encrypted_file = encrypt_file_with_key(text_file_path, key=key)

    assert Path(encrypted_file).is_file()


def test_decrypt_file_with_key():
    """
    Test Decrypt file
    """
    from automagica.activities import (
        generate_random_key,
        make_text_file,
        encrypt_file_with_key,
        decrypt_file_with_key,
    )

    # Generate a random key
    key = generate_random_key()

    # Create a text file to encrypt file
    text_file_path = make_text_file()

    # Encrypt the text file
    encrypted_text_file = encrypt_file_with_key(text_file_path, key=key)

    # Decrypt the newly encrypted file
    decrypted_file = decrypt_file_with_key(encrypted_text_file, key=key)

    assert Path(decrypted_file).is_file()


def test_generate_key_from_password():
    """
    Test Key from password
    """

    # Generate a key from password
    key = generate_key_from_password(password="Sample password")

    assert type(key) is bytes


def test_generate_hash_from_file():
    """
    Test Hash from file
    """

    # Generate a text file to illustrate hash
    text_file_path = make_text_file()

    # Get hash from text file
    hash_from_file = generate_hash_from_file(text_file_path)

    assert type(hash_from_file) is str


def test_generate_hash_from_text():
    """
    Test Hash from text
    """

    # Generate a hast from text
    hash_from_text = generate_hash_from_text("Sample text")

    assert type(hash_from_text) is str


def test_generate_random_number():
    """
    Test Random number
    """

    # Generate a random number
    random_number = generate_random_number()

    assert type(random_number) is int


def test_generate_random_data():
    """
    Test Random data
    """

    # Generate random data
    random_data = generate_random_data()

    assert type(random_data) is str


def test_generate_random_boolean():
    """
    Test Random boolean
    """

    # Generate a random boolean
    random_bool = generate_random_boolean()

    assert type(random_bool) is bool


def test_generate_random_name():
    """
    Test Random name
    """

    # Generate a random name
    rand_name = generate_random_name()

    assert type(rand_name) is str


def test_generate_random_words():
    """
    Test Random words
    """

    # Generate a random sentence
    random_words = generate_random_words()

    assert type(random_words) is str


def test_generate_random_address():
    """
    Test Random address
    """

    # Generate a random address
    random_address = generate_random_address()

    assert type(random_address) is str


def test_generate_random_beep():
    """
    Test Random beep
    """

    pass


def test_generate_random_date():
    """
    Test Random date
    """

    # Generate a random date
    random_date = generate_random_date()

    assert type(random_date) is str


def test_generate_date_today():
    """
    Test Today's date
    """

    # Generate a random date
    date_today = generate_date_today()

    assert type(date_today) is str


def test_generate_unique_identifier():
    """
    Test Generate unique identifier
    """

    # Generate unique identifier
    uuid = generate_unique_identifier()

    assert type(uuid) is str


@pytest.mark.skip(
    reason="This uses Tk() from tkinter, only one tkinter root object is \
    allowed per process. This needs a small rework before it can be tested."
)
def test_display_osd_message():
    """
    Test Display overlay message
    """

    # Display overlay message
    display_osd_message("testing", seconds=1)

    assert True


def test_print_console():
    """
    Test Print message in console
    """

    # Print in console
    print_console()

    assert True


def test_save_all_images(chrome_browser):
    """
    Test Save all images
    """

    # Go to a website
    chrome_browser.get("https://nytimes.com")

    # Save all images
    images = chrome_browser.save_all_images()

    assert type(images) is list


def test_find_elements_by_text(chrome_browser):
    """
    Test Find elements by text
    """

    # Go to a website
    chrome_browser.get("https://nytimes.com")

    # Find elements by text
    elements = chrome_browser.find_elements_by_text("a")

    assert type(elements) is list


def test_find_all_links(chrome_browser):
    """
    Test Find all links
    """
    # Go to a website
    chrome_browser.get("https://nytimes.com")

    # Find elements by text
    links = chrome_browser.find_all_links()

    assert type(links) is list


def test_find_first_link(chrome_browser):
    """
    Test Find first link on a webpage
    """

    # Go to a website
    chrome_browser.get("https://nytimes.com")

    # Find elements by text
    first_link = chrome_browser.find_first_link()

    assert type(first_link) is str


def test_get_text_on_webpage(chrome_browser):
    """
    Test Get all text on webpage
    """

    # Go to a website
    chrome_browser.get("https://nytimes.com")

    # Get text from page
    text_on_page = chrome_browser.get_text_on_webpage()

    assert type(text_on_page) is str


def test_highlight(chrome_browser):
    """
    Test Highlight element
    """

    # Go to a website
    chrome_browser.get("https://wikipedia.org")

    # Find first link on page
    first_link = chrome_browser.find_elements_by_xpath("//a[@href]")[0]

    # Highlight first link
    chrome_browser.highlight(first_link)

    assert True


def test_by_xpaths(chrome_browser):
    """
    Test Find all XPaths
    """

    # Go to a website
    chrome_browser.get("https://wikipedia.org")

    # Find elements by xpaths
    elements = chrome_browser.by_xpaths("//*[@id='js-link-box-en']")

    assert "elements" in locals()


def test_by_xpath(chrome_browser):
    """
    Test Find XPath in browser
    """
    # Go to a website
    chrome_browser.get("https://wikipedia.org")

    # Find element by xpath
    element = chrome_browser.by_xpath("//*[@id='js-link-box-en']")

    chrome_browser.quit()

    assert "element" in locals()


def test_by_class(chrome_browser):
    """
    Test Find class in browser
    """

    # Go to a website
    chrome_browser.get("https://wikipedia.org")

    # Find element by class
    element = chrome_browser.by_class("search-input")

    assert "element" in locals()


def test_by_classes(chrome_browser):
    """
    Test Find class in browser
    """
    # Go to a website
    chrome_browser.get("https://wikipedia.org")

    # Find elements by class
    elements = chrome_browser.by_classes("search-input")

    assert "elements" in locals()


def test_by_class_and_by_text(chrome_browser):
    """
    Test Find element in browser based on class and text
    """

    # Go to a website
    chrome_browser.get("https://wikipedia.org")

    # Find elements by class and text
    element = chrome_browser.by_class_and_by_text(
        "search-input", "Search Wikipedia"
    )

    assert "element" in locals()


def test_by_id(chrome_browser):
    """
    Test Find id in browser
    """

    # Go to a website
    chrome_browser.get("https://wikipedia.org")

    # Find element by class
    elements = chrome_browser.by_id("search-input")

    assert "elements" in locals()


def test_switch_to_iframe(chrome_browser):
    """
    Test Switch to iframe in browser
    """

    # Go to a website
    chrome_browser.get("https://www.w3schools.com/html/html_iframe.asp")

    url_before_switch = chrome_browser.current_url

    # Switch to iframe
    iframe = chrome_browser.switch_to_iframe()

    url_after_switch = chrome_browser.current_url

    assert url_before_switch == url_after_switch


def test_delete_credential():
    """
    Test Delete credential
    """
    set_credential("SampleUsername", "SamplePassword")
    delete_credential("SampleUsername", "SamplePassword")
    credential = get_credential("SampleUsername")

    assert "credential" in locals() and type(credential) is not str


def test_get_credential():
    """
    Test Get credential
    """
    set_credential("SampleUsername", "SamplePassword")
    credential = get_credential("SampleUsername")

    assert "SamplePassword" == credential


def test_download_file():
    """
    Test Download file
    """

    # This example uses the Rebex FPT test server.

    # Take caution uploading and downloading from this server as it is public
    ftp = FTP("test.rebex.net", "demo", "password")

    # Download Rebex public file 'readme.txt'
    downloaded_file = ftp.download_file("readme.txt")

    assert Path(downloaded_file).is_file()


def test_upload_file():
    """
    Test Upload file
    """

    # This example uses the Rebex FPT test server.

    # Take caution uploading and downloading from this server as it is public
    ftp = FTP("test.rebex.net", "demo", "password")

    # Create a .txt file for illustration
    text_file = make_text_file()

    # Upload file to FTP test server
    # Note that this might result in a persmission error for public FPT's
    try:
        ftp.upload_file(input_path=text_file)
    except PermissionError:
        assert True


def test_enumerate_files():
    """
    Test List FTP files
    """

    # This example uses the Rebex FPT test server.

    # Take caution uploading and downloading from this server as it is public
    ftp = FTP("test.rebex.net", "demo", "password")

    # Show all files in main directory
    message = ftp.enumerate_files()

    assert "Transfer complete" in message


def test_directory_exists():
    """
    Test Check FTP directory
    """

    # This example uses the Rebex FPT test server.

    # Take caution uploading and downloading from this server as it is public
    ftp = FTP("test.rebex.net", "demo", "password")

    # Check if 'pub' folder exists in main directory
    directory = ftp.directory_exists("\\pub")

    assert directory


def test_create_directory():
    """
    Test Create FTP directory
    """

    # This example uses the Rebex FPT test server.

    # Trying to create a directory will most likely fail due to permission
    ftp = FTP("test.rebex.net", "demo", "password")

    # Create directory
    ftp.create_directory("brand_new_directory")

    assert True


def test_press_key():
    """
    Test Press key
    """

    # Open notepad to illustrate typing
    run("notepad.exe")

    # Press some keys
    press_key("x")

    press_key_combination("ctrl", "a")
    press_key_combination("ctrl", "c")

    kill_process("notepad.exe")

    clipboard = get_from_clipboard()

    assert "x" == clipboard


def test_typing():
    """
    Test typing
    """

    run("notepad.exe")

    # Press some keys
    typing("hello world!")

    press_key_combination("ctrl", "a")
    press_key_combination("ctrl", "c")

    kill_process("notepad.exe")

    clipboard = get_from_clipboard()

    assert "hello world!" == clipboard


def test_get_mouse_position():
    """
    Test Get mouse coordinates
    """
    mouse_position = get_mouse_position()

    assert type(mouse_position) is tuple


def test_display_mouse_position():
    """
    Test Display mouse position
    """
    display_mouse_position()

    assert True

def test_click_coordinates():
	"""
	Test Mouse click coordinates
	"""

	# Click on pixel position
	click_coordinates(x=1, y=1)
	
	assert get_mouse_position() == (1,1)

def test_double_click_coordinates():
	"""
	Test Double mouse click coordinates
	"""

	# Click on coordinates
	double_click_coordinates(x=1, y=1)
	
	assert get_mouse_position() == (1,1)

def test_right_click_coordinates():
	"""
	Test Right click coordinates
	"""

	# Right click on coordinates
	right_click_coordinates(x=1, y=1)
	
	assert get_mouse_position() == (1,1)

def test_move_mouse_to_coordinates():
	"""
	Test Move mouse coordinates
	"""

	# Move mouse to coordinates
	move_mouse_to_coordinates(x=1, y=1)
	
	assert get_mouse_position() == (1,1)

def test_move_mouse_relative():
	"""
	Test Move mouse relative
	"""
	move_mouse_to_coordinates(x=1, y=1)
	wait(1)
	move_mouse_relative(x=1, y=1)
	
	assert get_mouse_position() == (2,2)

def test_drag_mouse_to_coordinates():
	"""
	Test Drag mouse
	"""

	# Use coordinates to move and drag mouse
	move_mouse_to_coordinates(x=100, y=100)
	drag_mouse_to_coordinates(x=1, y=1)
	
	assert get_mouse_position() == (1,1)

def test_random_screen_snippet():
	"""
	Test Random screen snippet
	"""
	random_screen_snippet()
	
	assert True

def test_take_screenshot():
	"""
	Test Screenshot
	"""
	new_screenshot = take_screenshot()
	
	assert type(new_screenshot) is str

def test_get_files_in_folder():
	"""
	Test List files in folder
	"""

	# List all files in the homedirectory
	files = get_files_in_folder()
	
	assert type(files) is str

def test_create_folder():
	"""
	Test Create folder
	"""

	# Create folder in the home directory
	new_folder = create_folder()
	
	assert type(new_folder) is str and 'new_folder' in new_folder

def test_rename_folder():
	"""
	Test Rename folder
	"""

	# Make new folder in home directory for illustration
	testfolder = create_folder()

	# Rename the folder
	renamed_folder = rename_folder(testfolder, output_name='unit_test_folder')
	
	assert type(renamed_folder) is str and 'unit_test_folder' in renamed_folder

def test_move_folder():
	"""
	Test Move a folder
	"""
	import os

	# Make new folder in home directory for illustration

	# If no new_folder exists in home dir this will be called new_folder
	testfolder = create_folder()

	# Make a second new folder

	# Since new_folder already exists this folder will get a random id added (in this case abc1)
	testfolder_2 = create_folder()

	# Move testfolder in testfolder_2
	move_folder(testfolder, testfolder_2)

	assert not os.path.exists(testfolder) and os.path.exists(testfolder_2)

def test_remove_folder():
	"""
	Test Remove folder
	"""
	import os

	# Make new folder in home directory for illustration
	testfolder = create_folder()

	# Remove folder
	remove_folder(testfolder)

	assert not os.path.exists(testfolder)

def test_empty_folder():
	"""
	Test Empty folder
	"""

	# Make new folder in home directory for illustration
	testfolder = create_folder()

	# Make new text file in this folder
	text_file_location = make_text_file(output_path = testfolder)

	# Print all files in the testfolder
	get_files_in_folder(testfolder) 

	# Empty the folder
	empty_folder(testfolder)

	# Check what is in the folder
	files = get_files_in_folder(testfolder)
	
	assert len(files) == 0

def test_folder_exists():
	"""
	Test Checks if folder exists
	"""
	import os

	# Make new folder in home directory for illustration
	testfolder = create_folder()

	# Check if folder exists
	
	assert folder_exists(testfolder) == os.path.exists(testfolder)

def test_copy_folder():
	"""
	Test Copy a folder
	"""

	# Make new folder in home directory for illustration
	testfolder = create_folder()

	# Copy this folder

	# Since new_folder already exists in home dir this folder will get a random id added (in this case abc1)
	copied_folder = copy_folder(testfolder)
	
	assert type(copied_folder) is str and 'copied' in copied_folder and testfolder in copied_folder

def test_zip_folder():
	"""
	Test Zip
	"""

	# Make new folder in home directory for illustration
	testfolder = create_folder()

	# Zip this folder
	zipped_folder = zip_folder(testfolder)
	
	assert type(zipped_folder) is str and testfolder in zipped_folder and 'zipped' in zipped_folder

def test_unzip():
	"""
	Test Unzip
	"""

	# Make new file in home directory for illustration
	testfolder = create_folder()

	# Add some files to this folder
	make_text_file(output_path = testfolder)

	# Zip this folder
	zipped_folder = zip_folder(testfolder)

	# Unzip this folder
	unzipped = unzip(zipped_folder)
	
	assert type(unzipped) is str

def test_most_recent_file():
	"""
	Test Return most recent file in directory
	"""

	# Find most recent file in homedir
	recent_file = most_recent_file()
	
	assert type(recent_file) is str

def test_wait():
	"""
	Test Wait
	"""
	wait()
	
	assert True

def test_wait_folder_exists():
	"""
	Test Wait for folder
	"""

	# Create a random folder
	testfolder = create_folder()

	# Wait for the snippet to be visible
	folder_existence = wait_folder_exists(testfolder)
	
	assert folder_existence

@pytest.fixture
def word_test():
    from automagica.activities import Word

    word = Word()

    yield word

    word.quit()



