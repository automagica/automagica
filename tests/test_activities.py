"""Copyright 2020 Oakwood Technologies BVBA"""


from automagica.activities import *
from pathlib import Path

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


def test_chrome_activities():
	"""
	Test scenario for testing Chrome browser activities (requires Google Chrome)
	"""
	# Open Chrome
	chrome = Chrome(auto_update_chromedriver=True)

	# Browse to Google
	chrome.browse_to("https://google.com")

	# Save the page source
	source = chrome.page_source

	# Quit the browser
	chrome.quit()

	assert "Google" in source

def test_wand_activities():
	"""
	Test wand activities
	"""
	# Testing element, could be a black pixel for example
	# Element can be white listed to be always available
	test_element = 'qf41'

	click(test_element)
	double_click(test_element)
	right_click(test_element')
	move_mouse_to(test_element)
	drag_mouse_to(test_element)

	assert True

def test_cryptography_activities():
	"""
	Test scenario to test encrypting and decrypting activities
	"""
	#from automagica.activities import generate_random_key, encrypt_text_with_key, decrypt_text_with_key

	# Generate a random key
	key = generate_random_key()
	
	# Encrypt text with generated key
	encrypted_text = encrypt_text_with_key('Testing', key)

	# Decrypt text with same key
	decrypted_text = decrypt_text_with_key(encrypted_text, key)

	assert decrypted_text == 'Testing'

def test_generate_random_key():
	"""
	Test Random key
	"""

	# Generate a random key
	key = generate_random_key()
	
	assert str(key)

def test_encrypt_text_with_key():
	"""
	Test Encrypt text
	"""

	# Generate a random key
	key = generate_random_key()
	# Encrypt text with this key
	outcome = encrypt_text_with_key('Sample text', key)
	
	assert type(outcome) is bytes


def test_decrypt_text_with_key():
	"""
	Test Decrypt text
	"""

	# Generate a random key
	key = generate_random_key()
	# Encrypt text with generated key
	encrypted_text = encrypt_text_with_key('Sample text', key)
	# Decrypt text with same key
	decrypted_text = decrypt_text_with_key(encrypted_text, key)
	
	assert 'Sample text' == decrypted_text

def test_encrypt_file_with_key():
	"""
	Test Encrypt file
	"""

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
	key = generate_key_from_password(password='Sample password')
	
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
	hash_from_text = generate_hash_from_text('Sample text')
	
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

def test_display_osd_message():
	"""
	Test Display overlay message
	"""

	# Display overlay message
	display_osd_message('testing', seconds=1)
	
	assert True


def test_print_console():
	"""
	Test Print message in console
	"""

	# Print in console
	print_console()
	
	assert True

def test_save_all_images():
	"""
	Test Save all images
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://nytimes.com')

	# Save all images
	images = browser.save_all_images()

	browser.quit()
	
	assert type(images) is list

def test_find_elements_by_text():
	"""
	Test Find elements by text
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://nytimes.com')

	# Find elements by text
	elements = browser.find_elements_by_text('a')

	# Quit the browser
	browser.quit()
	
	assert type(elements) is list

def test_find_all_links():
	"""
	Test Find all links
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://nytimes.com')

	# Find elements by text
	links = browser.find_all_links()

	# Quit the browser
	browser.quit()
	
	assert type(links) is list

def test_find_first_link():
	"""
	Test Find first link on a webpage
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://nytimes.com')

	# Find elements by text
	first_link = browser.find_first_link()

	# Quit the browser
	browser.quit()
	
	assert type(first_link) is str


def test_get_text_on_webpage():
	"""
	Test Get all text on webpage
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://nytimes.com')

	# Get text from page
	text_on_page = browser.get_text_on_webpage()

	# Quit the browser
	browser.quit()
	
	assert type(text_on_page) is str

def test_highlight():
	"""
	Test Highlight element
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://wikipedia.org')

	# Find first link on page
	first_link = browser.find_elements_by_xpath("//a[@href]")[0]

	# Highlight first link
	browser.highlight(first_link)

	browser.quit()
	
	assert True

def test_by_xpaths():
	"""
	Test Find all XPaths
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://wikipedia.org')

	# Find elements by xpaths
	elements = browser.by_xpaths('//*[@id=\'js-link-box-en\']')
	
	browser.quit()

	assert 'elements' in locals()

def test_by_xpath():
	"""
	Test Find XPath in browser
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://wikipedia.org')

	# Find element by xpath
	element = browser.by_xpath('//*[@id=\'js-link-box-en\']')

	browser.quit()
	
	assert 'element' in locals()

def test_by_class():
	"""
	Test Find class in browser
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://wikipedia.org')

	# Find element by class
	element = browser.by_class('search-input')

	browser.quit()
	
	assert 'element' in locals()


def test_by_classes():
	"""
	Test Find class in browser
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://wikipedia.org')

	# Find elements by class
	elements = browser.by_classes('search-input')

	browser.quit()
	
	assert 'elements' in locals()

def test_by_class_and_by_text():
	"""
	Test Find element in browser based on class and text
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://wikipedia.org')

	# Find elements by class and text
	element = browser.by_class_and_by_text('search-input', 'Search Wikipedia')

	browser.quit()
	
	assert 'element' in locals()


def test_by_id():
	"""
	Test Find id in browser
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://wikipedia.org')

	# Find element by class
	elements = browser.by_id('search-input')

	browser.quit()
	
	assert 'elements' in locals()


def test_switch_to_iframe():
	"""
	Test Switch to iframe in browser
	"""

	# Open the browser
	browser = Chrome()

	# Go to a website
	browser.get('https://www.w3schools.com/html/html_iframe.asp')

	url_before_switch = browser.current_url

	# Switch to iframe
	iframe = browser.switch_to_iframe()

	url_after_switch = browser.current_url

	browser.quit()
	
	assert url_before_switch == url_after_switch

def test_delete_credential():
	"""
	Test Delete credential
	"""
	set_credential('SampleUsername', 'SamplePassword')
	delete_credential('SampleUsername', 'SamplePassword')
	credential = get_credential('SampleUsername')
	
	assert 'credential' in locals() and type(credential) is not str


def test_get_credential():
	"""
	Test Get credential
	"""
	set_credential('SampleUsername', 'SamplePassword')
	credential = get_credential('SampleUsername')
	
	assert 'SamplePassword' == credential


def test_download_file():
	"""
	Test Download file
	"""

	# This example uses the Rebex FPT test server.

	# Take caution uploading and downloading from this server as it is public
	ftp = FTP('test.rebex.net', 'demo', 'password')

	# Download Rebex public file 'readme.txt'
	downloaded_file = ftp.download_file('readme.txt')
	
	assert Path(downloaded_file).is_file()


def test_upload_file():
	"""
	Test Upload file
	"""

	# This example uses the Rebex FPT test server.

	# Take caution uploading and downloading from this server as it is public
	ftp = FTP('test.rebex.net', 'demo', 'password')

	# Create a .txt file for illustration
	text_file = make_text_file()

	# Upload file to FTP test server
	# Note that this might result in a persmission error for public FPT's
	try:
		ftp.upload_file(input_path = text_file)
	except PermissionError:
		assert True


def test_enumerate_files():
	"""
	Test List FTP files
	"""

	# This example uses the Rebex FPT test server.

	# Take caution uploading and downloading from this server as it is public
	ftp = FTP('test.rebex.net', 'demo', 'password')

	# Show all files in main directory
	message = ftp.enumerate_files()
	
	assert 'Transfer complete' in message


def test_directory_exists():
	"""
	Test Check FTP directory
	"""

	# This example uses the Rebex FPT test server.

	# Take caution uploading and downloading from this server as it is public
	ftp = FTP('test.rebex.net', 'demo', 'password')

	# Check if 'pub' folder exists in main directory
	directory = ftp.directory_exists('\\pub')
	
	assert directory


def test_create_directory():
	"""
	Test Create FTP directory
	"""

	# This example uses the Rebex FPT test server.

	# Trying to create a directory will most likely fail due to permission
	ftp = FTP('test.rebex.net', 'demo', 'password')

	# Create directory
	ftp.create_directory('brand_new_directory')      
	
	assert True


def test_press_key():
	"""
	Test Press key
	"""

	# Open notepad to illustrate typing
	run('notepad.exe')

	# Press some keys
	press_key('x')

	press_key_combination('ctrl', 'a')
	press_key_combination('ctrl', 'c')

	kill_process('notepad.exe')

	clipboard = get_from_clipboard()
	
	assert 'x' == clipboard

def test_typing():
	"""
	Test typing
	"""

	run('notepad.exe')

	# Press some keys
	typing('hello world!')

	press_key_combination('ctrl', 'a')
	press_key_combination('ctrl', 'c')

	kill_process('notepad.exe')

	clipboard = get_from_clipboard()
	
	assert 'hello world!' == clipboard

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






