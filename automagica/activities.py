def activity(func):
    """Wrapper for Automagica activities
    """
    from functools import wraps
    import logging

    @wraps(func)
    def wrapper(*args, **kwargs):
        if func.__doc__:
            name = func.__doc__.split("\n")[0]
        else:
            name = func.__name__
        logging.info("Automagica (activity): {}".format(name))
        telemetry(func)
        return func(*args, **kwargs)

    return wrapper


def telemetry(func):
    """Automagica Activity Telemetry
    This allows us to collect information on the usage of 
    certain Automagica functionalities in order for us to keep improving 
    the software. If you would like to disable telemetry, make sure the 
    environment variable 'AUTOMAGICA_NO_TELEMETRY' is set. That way no
    information is being shared with us.
    """
    import requests
    from uuid import getnode
    import os
    import platform

    if not os.environ.get("AUTOMAGICA_NO_TELEMETRY") and not os.environ.get(
        "AUTOMAGICA_URL"
    ):
        if func.__doc__:
            name = func.__doc__.split("\n")[0]
        else:
            name = func.__name__

        data = {
            "activity": name,
            "machine_id": getnode(),
            "os": {
                "name": os.name,
                "platform": platform.system(),
                "release": platform.release(),
            },
        }

        try:
            r = requests.post(
                "https://telemetry.automagica.io/api", json=data, timeout=1
            )
        except:
            pass


"""
Cryptography
"""

@activity
def generate_random_key():
    """Generates a random Fernet key. 

    Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography
    """
    import os
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()

    return key

@activity
def encrypt_text_with_key(text, key):
    """Encrypts string with (Fernet) key, returns bytes-like object.

    :param text: Text to be encrypted.
    :param path: Path where key is stored.
    """
    from cryptography.fernet import Fernet
    f = Fernet(key)

    return f.encrypt(text.encode('utf-8'))

@activity
def decrypt_text_with_key(encrypted_text, key):
    """Decrypts bytes-like object to string with (Fernet) key
    
    :param encrypted_text: Text to be encrypted.
    :param path: Path where key is stored.
    """
    from cryptography.fernet import Fernet
    f = Fernet(key)

    return f.decrypt(encrypted_text).decode("utf-8") 

@activity
def encrypt_file_with_key(input_file, output_file, key):
    """Encrypts file with (Fernet) key
    
    :param input_file: File to be encrypted.
    :param output_file: Outputfile, returns a bytes-like can be an arbitrary .
    """
    from cryptography.fernet import Fernet

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

@activity
def decrypt_file_with_key(input_file, output_file, key):
    """Decrypts file with (Fernet) key
    
    :param input_file: Bytes-like file to be decrypted.
    :param output_file: Outputfile, make sure to give this the same extension as basefile before encryption.
    """
    from cryptography.fernet import Fernet

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

@activity
def generate_key_from_password(password, salt=None):
    """Generates (Fernet) key based on password and salt.
    
    :param text: text to be encrypted.
    :param salt: Salt to generate key in combination with password. Default value is the hostname. Take in to account that hostname is necessary to generate key, e.g. when files are encrypted with salt 'A' and password 'B', both elements are necessary to decrypt files.
    """
    import base64
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import socket

    # If no salt is set, use hostname as salt
    if not salt:
        salt = socket.gethostname().encode('utf-8')
    
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=500000,backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8'))) 
    
    return key

@activity
def generate_hash_from_file(file, method='md5', buffer_size = 65536):
    """Generate hash from file. Can be used to create unique identifier for file validation or comparison.

    :param file: File to hash
    :param method: Method for hashing, choose between 'md5', 'sha256' and 'blake2b'. Note that different methods generate different hashes.
    :param buffer_size: Buffer size for reading file in chunks, default value is 64kb
    """
    import sys
    import hashlib

    # Arbitrary buffer size. 64kb for compatibility with most systems
    buffer_size = 65536  

    if method == 'md5':
        hash_list = hashlib.md5()
    if method == 'sha256':
        hash_list = hashlib.sha1()
    if method == 'blake2b':
        hash_list = hashlib.blake2b()

    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if data:
                hash_list.update(data)
            else:
                return hash_list.hexdigest()

@activity			
def generate_hash_from_text(text, method='md5'):
    """Generate hash from text.
    
    :param file: Text to hash
    :param method: Method for hashing, choose between 'md5', 'sha256' and 'blake2b'. Note that different methods generate different hashes.
    """
    import sys
    import hashlib

    encoded_text = text.encode('utf-8')

    if method == 'md5':
        return hashlib.md5(encoded_text).hexdigest()
    if method == 'sha256':
        return hashlib.sha256(encoded_text).hexdigest()
    if method == 'blake2b':
        return hashlib.balke2b(encoded_text).hexdigest()

"""
Random
"""

@activity
def generate_random_number(lower_limit=0,upper_limit=10, fractional=False):
    """Generates a random number. Can be integers (not a fractional number) or a float (fractional number).

    :param lower_limit: Lower limit for random number
    :param upper_limit: Upper limit for random number
    :param fractional: Setting this to True will generate fractional number. Default value is False and only generates whole numbers.
    """
    import random 
    if fractional:
        return random.uniform(lower_limit, upper_limit)
    else:
        return random.randrange(lower_limit,upper_limit,1)

@activity
def generate_random_boolean():
    """Generates a random boolean (True or False)
    """
    import random 
    return bool(random.getrandbits(1))

@activity
def generate_random_name(locale=None):
    """Generates a random name.

    :param locale: Add a locale to generate popular name for selected locale.
        ar_EG - Arabic (Egypt)
        ar_PS - Arabic (Palestine)
        ar_SA - Arabic (Saudi Arabia)
        bg_BG - Bulgarian
        bs_BA - Bosnian
        cs_CZ - Czech
        de_DE - German
        dk_DK - Danish
        el_GR - Greek
        en_AU - English (Australia)
        en_CA - English (Canada)
        en_GB - English (Great Britain)
        en_NZ - English (New Zealand)
        en_US - English (United States)
        es_ES - Spanish (Spain)
        es_MX - Spanish (Mexico)
        et_EE - Estonian
        fa_IR - Persian (Iran)
        fi_FI - Finnish
        fr_FR - French
        hi_IN - Hindi
        hr_HR - Croatian
        hu_HU - Hungarian
        hy_AM - Armenian
        it_IT - Italian
        ja_JP - Japanese
        ka_GE - Georgian (Georgia)
        ko_KR - Korean
        lt_LT - Lithuanian
        lv_LV - Latvian
        ne_NP - Nepali
        nl_NL - Dutch (Netherlands)
        no_NO - Norwegian
        pl_PL - Polish
        pt_BR - Portuguese (Brazil)
        pt_PT - Portuguese (Portugal)
        ro_RO - Romanian
        ru_RU - Russian
        sl_SI - Slovene
        sv_SE - Swedish
        tr_TR - Turkish
        uk_UA - Ukrainian
        zh_CN - Chinese (China)
        zh_TW - Chinese (Taiwan)
    """
    from faker import Faker
    if locale:
        seed = Faker(locale)
    else:
        seed = Faker()
    return seed.name()

def generate_random_sentence(locale=None):
    """Generates a random sentence.

    :param locale: Add a locale to generate sentences for selected locale (language).
        ar_EG - Arabic (Egypt)
        ar_PS - Arabic (Palestine)
        ar_SA - Arabic (Saudi Arabia)
        bg_BG - Bulgarian
        bs_BA - Bosnian
        cs_CZ - Czech
        de_DE - German
        dk_DK - Danish
        el_GR - Greek
        en_AU - English (Australia)
        en_CA - English (Canada)
        en_GB - English (Great Britain)
        en_NZ - English (New Zealand)
        en_US - English (United States)
        es_ES - Spanish (Spain)
        es_MX - Spanish (Mexico)
        et_EE - Estonian
        fa_IR - Persian (Iran)
        fi_FI - Finnish
        fr_FR - French
        hi_IN - Hindi
        hr_HR - Croatian
        hu_HU - Hungarian
        hy_AM - Armenian
        it_IT - Italian
        ja_JP - Japanese
        ka_GE - Georgian (Georgia)
        ko_KR - Korean
        lt_LT - Lithuanian
        lv_LV - Latvian
        ne_NP - Nepali
        nl_NL - Dutch (Netherlands)
        no_NO - Norwegian
        pl_PL - Polish
        pt_BR - Portuguese (Brazil)
        pt_PT - Portuguese (Portugal)
        ro_RO - Romanian
        ru_RU - Russian
        sl_SI - Slovene
        sv_SE - Swedish
        tr_TR - Turkish
        uk_UA - Ukrainian
        zh_CN - Chinese (China)
        zh_TW - Chinese (Taiwan)
    """
    from faker import Faker
    if locale:
        seed = Faker(locale)
    else:
        seed = Faker()
    return seed.sentence()

@activity
def generate_random_address(locale=None):
    """Generates a random address.

    :param locale: Add a locale to generate addresses for selected locale.
        ar_EG - Arabic (Egypt)
        ar_PS - Arabic (Palestine)
        ar_SA - Arabic (Saudi Arabia)
        bg_BG - Bulgarian
        bs_BA - Bosnian
        cs_CZ - Czech
        de_DE - German
        dk_DK - Danish
        el_GR - Greek
        en_AU - English (Australia)
        en_CA - English (Canada)
        en_GB - English (Great Britain)
        en_NZ - English (New Zealand)
        en_US - English (United States)
        es_ES - Spanish (Spain)
        es_MX - Spanish (Mexico)
        et_EE - Estonian
        fa_IR - Persian (Iran)
        fi_FI - Finnish
        fr_FR - French
        hi_IN - Hindi
        hr_HR - Croatian
        hu_HU - Hungarian
        hy_AM - Armenian
        it_IT - Italian
        ja_JP - Japanese
        ka_GE - Georgian (Georgia)
        ko_KR - Korean
        lt_LT - Lithuanian
        lv_LV - Latvian
        ne_NP - Nepali
        nl_NL - Dutch (Netherlands)
        no_NO - Norwegian
        pl_PL - Polish
        pt_BR - Portuguese (Brazil)
        pt_PT - Portuguese (Portugal)
        ro_RO - Romanian
        ru_RU - Russian
        sl_SI - Slovene
        sv_SE - Swedish
        tr_TR - Turkish
        uk_UA - Ukrainian
        zh_CN - Chinese (China)
        zh_TW - Chinese (Taiwan)
    """
    from faker import Faker
    if locale:
        seed = Faker(locale)
    else:
        seed = Faker()
    return seed.address()


@activity
def generate_random_beep(max_duration=2000, max_frequency=5000):
    """Generates a random beep, only works on Windows

    :param max_duration: Maximum random duration in miliseconds. Default value is 2 miliseconds
    :param max_frequency: Maximum random frequency in Hz. Default value is 5000 Hz.
    """
    import winsound
    import random
    frequency = random.randrange(5000)
    duration = random.randrange(2000)
    winsound.Beep(frequency, duration)

@activity
def generate_random_date(format='%m/%d/%Y %I:%M', days_in_past=1000):
    """Generate a random date. 

    :param days_in_past: Days in the past for which oldest random date is generated, default is 1000 days
    :param format: Formatting of the dates, replace with 'None' to get raw datetime format. 
    e.g. format='Current month is %B' generates 'Current month is Januari' and format='%m/%d/%Y %I:%M' generates format 01/01/1900 00:00. 
    %a	Abbreviated weekday name.	 
    %A	Full weekday name.	 
    %b	Abbreviated month name.	 
    %B	Full month name.	 
    %c	Predefined date and time representation.	 
    %d	Day of the month as a decimal number [01,31].	 
    %H	Hour (24-hour clock) as a decimal number [00,23].	 
    %I	Hour (12-hour clock) as a decimal number [01,12].	 
    %j	Day of the year as a decimal number [001,366].	 
    %m	Month as a decimal number [01,12].	 
    %M	Minute as a decimal number [00,59].	 
    %p	AM or PM.
    %S	Second as a decimal number [00,61].	
    %U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(3)
    %w	Weekday as a decimal number [0(Sunday),6].	 
    %W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(3)
    %x	Predefined date representation.	 
    %X	Predefined time representation.	 
    %y	Year without century as a decimal number [00,99].	 
    %Y	Year with century as a decimal number.
    %Z	Time zone name (no characters if no time zone exists).
    """

    import random
    import datetime

    latest  = datetime.datetime.now()
    earliest = latest - datetime.timedelta(days=days_in_past)
    delta_seconds = (latest - earliest).total_seconds()

    random_date = earliest + datetime.timedelta(seconds = random.randrange(delta_seconds))

    if format:
        return random_date.strftime(format)
    else:
        return random_date


@activity
def generate_unique_identifier():
    """Generates a random UUID4
    """
    from uuid import uuid4

    return str(uuid4())

@activity
def random_animal_picture(preferred_animal=None):
    """Returns url for a random picture

    Note that this service uses an external database, we can not garantuee the quality and availability. 
    The purpose of this activity is mainly for testing to generate dummy data. Will most likely return a picture of a cat, dog or fox.

    :parameter preferred_animal: Return a preferred animal, if not specified will return what is available at the moment. Options are 'cat', 'dog' or 'fox'.
    """
    import requests
    import random

    api_options = [ {'animal' : 'cat', 'url' :'https://aws.random.cat/meow', 'image_tag' : 'file'}, 
                    {'animal' : 'dog', 'url' :'https://random.dog/woof.json', 'image_tag' : 'url'}, 
                    {'animal' : 'fox', 'url' :'https://randomfox.ca/floof/', 'image_tag' : 'image'}
                    ]
    
    if preferred_animal:
        if preferred_animal in ['dog', 'cat', 'fox']:
            option = list(filter(lambda api_option: api_option['animal'] == preferred_animal, api_options))[0]
            response = requests.get(option['url'])
            if response.status_code != 200:
                raise Exception('Could not retreive image from external database')
            return response.json()[option['image_tag']]
    
    random.shuffle(api_options)
    for item in api_options:
        response = requests.get(item['url'])
        if response.status_code != 200:
            continue
        else:
            return response.json()[item['image_tag']]


"""
Ask user input
"""

@activity
def ask_user_input(title="Title", label="Input", password=False):
    """Ask user for input
    Prompt the user for an input

    :param title: Title for the pop-up window
    :param message: The message to be shown to the user
    """
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel("SystemDefault")

    text = sg.Text(label, background_color="#2196F3", text_color="white")

    input_field = sg.InputText(justification="center", focus=True)

    if password:
        input_field = sg.InputText(
            password_char="*", justification="center", focus=True
        )

    submit_button = sg.Submit(button_color=("white", "#0069C0"))

    layout = [[text], [input_field], [submit_button]]

    window = sg.Window(
        title,
        layout,
        icon="icon.ico",
        no_titlebar=True,
        background_color="#2196F3",
        element_justification="center",
        use_default_focus=False,
    )
    _, values = window.Read()
    window.Close()
    value = values[0]

    return value

@activity
def ask_user_password(label="Password"):
    """Ask user for password
    Prompt the user for a password. The password will be masked on screen while entering.

    :param title: Title for the pop-up window
    :param message: The message to be shown to the user
    """
    return ask_user_input(title="Password", label=label, password=True)


@activity
def ask_credentials(
    title="Credentials required",
    dialogue_text_username="Username:",
    dialogue_text_password="Password:",
):
    """Ask a user for credentials
    Prompt a popup which asks user for username and password and returns in plain text. Password will be masked.

    :param title: Title for the popup
    :param dialogue_text: Dialogue text for username
    :param dialogue_text: Dialogue text for password
    """
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel("SystemDefault")

    layout = [
        [
            sg.Text(
                dialogue_text_username, background_color="#2196F3", text_color="white"
            )
        ],
        [sg.InputText(justification="center", focus=True)],
        [
            sg.Text(
                dialogue_text_password, background_color="#2196F3", text_color="white"
            )
        ],
        [sg.InputText(password_char="*", justification="center")],
        [sg.Submit(button_color=("white", "#0069C0"))],
    ]

    window = sg.Window(
        title,
        layout,
        icon="icon.ico",
        no_titlebar=True,
        background_color="#2196F3",
        element_justification="center",
        use_default_focus=False,
    )
    _, values = window.Read()

    window.Close()
    username = values[0]
    password = values[1]

    return username, password

def display_message_box(title="Title", message="Example message"):
    """Shows a pop-up message with title and message. 

    :param title: Title for the pop-up window
    :param message: The message to be shown to the user
    """
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel("SystemDefault")

    text = sg.Text(message, background_color="#2196F3", text_color="white")

    ok_button = sg.OK(button_color=("white", "#0069C0"))

    layout = [[text], [ok_button]]

    window = sg.Window(
        title,
        layout,
        icon="icon.ico",
        no_titlebar=True,
        background_color="#2196F3",
        element_justification="center",
        use_default_focus=False,
    )
    _, values = window.Read()
    window.Close()
    value = values[0]

    return value

@activity
def display_osd_message(message, seconds=5):
    """Display custom overlay message

    Can be used to display a message for a limited amount of time. Can be used for illustration, debugging or as OSD.

    :param message: Message to be displayed
    """
    if "DISABLE_AUTOMAGICA_OSD" in globals():
        return

    import tkinter, win32api, win32con, pywintypes
    from win32api import GetSystemMetrics

    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)

    root = tkinter.Tk()
    label = tkinter.Label(
        text=message, font=("Helvetica", "30"), fg="white", bg="black", borderwidth=10
    )
    label.master.overrideredirect(True)
    label.config(anchor=tkinter.CENTER)
    label.master.geometry(
        "+{}+{}".format(int(screen_width / 2), int(screen_height - 250))
    )
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "black")

    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))

    exStyle = (
        win32con.WS_EX_COMPOSITED
        | win32con.WS_EX_LAYERED
        | win32con.WS_EX_NOACTIVATE
        | win32con.WS_EX_TOPMOST
        | win32con.WS_EX_TRANSPARENT
    )
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    label.after(seconds * 1000, lambda: root.destroy())
    label.pack()
    label.mainloop()


"""
Browsers
"""

import selenium.webdriver
class Chrome(selenium.webdriver.Chrome):
    def __init__(self, load_images=True, headless=False):
        """Opens the Chrome Browser with the Selenium webdriver.
        Args:
            load_images (bool): do not load images
            headless (bool): run without a window

        Returns:
            webdriver: Selenium Webdriver

        Example:
            browser = ChromeBrowser(ignore_iamges=True)
            browser.get('https://automagica.io')

        """
        import platform
        import os

        # Check what OS we are on
        if platform.system() == "Linux":
            chromedriver_path = "\\bin\\webdriver\\linux64\\chromedriver"
        elif platform.system() == "Windows":
            chromedriver_path = "\\bin\\win32\\chromedriver.exe"
        else:
            chromedriver_path = "\\bin\\mac64\\chromedriver.exe"

        chrome_options = selenium.webdriver.ChromeOptions()

        if headless:
            chrome_options.add_argument("--headless")

        if not load_images:
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
        
        selenium.webdriver.Chrome.__init__(self, os.path.abspath("") + chromedriver_path, options=chrome_options)

    @activity
    def save_all_images(self, target_folder_path):
        """Save all images on current page in the Browser
        """
        import requests
        import os
        from urllib.parse import urlparse
        
        paths = []
        
        images = self.find_elements_by_tag_name('img') 

        for image in images:
            url = image.get_attribute('src')
            a = urlparse(url)
            filename = os.path.basename(a.path)
            
            with open(os.path.join(target_folder_path, filename), 'wb') as f:
                try:
                    r = requests.get(url)
                    f.write(r.content)
                    paths.append(os.path.join(target_folder_path, filename))
                except:
                    pass
        
        return paths
    
    @activity
    def find_elements_by_text(self, text):
        """Find elements by text in the Browser
        """
        return self.find_elements_by_xpath("//*[contains(text(), '" + text + "')] | //*[@value='" + text + "']")
    
    @activity
    def find_element_by_text(self, text):
        """Find element by text in the Browser
        """
        return self.find_element_by_xpath("//*[contains(text(), '" + text + "')] | //*[@value='" + text + "']")
    
    @activity
    def highlight(self, element):
        """Highlight element in the Browser
        """
        driver = element._parent
        
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)
        original_style = element.get_attribute('style')
        
        apply_style("background: yellow; border: 2px solid red;")

"""
Credential Management
"""


@activity
def set_credential(username=None, password=None, system="Automagica"):
    """Add a credential which stores credentials locally. All parameters should be Unicode text. 

    :param username: Username for which credential will be added.
    :param password: Password to add
    :param system: Name of the system for which credentials are stored. Extra safety measure and method for keeping passwords for similar usernames on different applications a part. Highly recommended to change default value.
    """
    import keyring

    keyring.set_password(system, username, password)


@activity
def delete_credential(username=None, password=None, system="Automagica"):
    """Delete a locally stored credential. All parameters should be Unicode text. 

    :param username: Username for which credential (username + password) will be deleted.
    :param system: Name of the system for which password will be deleted. 
    """
    import keyring

    keyring.delete_password(system, username)


@activity
def get_credential(username=None, system="Automagica"):
    """Get a saved credential. All parameters should be Unicode text. 

    :param username: Username to get password for.
    :param system: Name of the system for which credentials are retreived.
    """
    import keyring

    return keyring.get_password(system, username)


"""
FTP
"""


class FTP:
    def __init__(self, server, username, password):
        """Create FPT connection

        :param server: Name of the server
        :param username: Username 
        :param password: Password
        """
        import ftplib

        self.connection = ftplib.FTP(server)
        self.connection.login(username, password)

    @activity
    def download_file(self, from_path, to_path=None):
        """Download file from FTP server

        :param from_path: Path to the file on the FPT server to download
        :param to_path: Destination path for downloaded files. Standard is the home directory

        :return: 
        """
        # Set to user home if no path specified
        if not to_path:
            to_path = os.path.expanduser("~")

        self.connection.retrbinary("RETR " + from_path, open(to_path, "wb").write)

    @activity
    def upload_file(self, from_path, to_path=None):
        """Upload file to FTP server

        :param from_path: Path file that will be uploaded
        :param to_path: Destination path for uploade files. Standard is the main directory

        :return: 
        """
        # Set to user home if no path specified
        if not to_path:
            to_path = "/"

        self.connection.retrbinary("RETR " + from_path, open(to_path, "wb").write)

    @activity
    def enumerate_files(self, path="/"):
        """Generate a list of all the files in the FTP directory

        :return: List object
        """
        self.connection.cwd(path)
        lines = self.connection.retrlines("LIST")
        return lines

    @activity
    def directory_exists(self, path):
        """Check if FTP directory exists

        :return: Boolean
        """
        try:
            self.connection.cwd(path)
            return True
        except IOError:
            return False

    @activity
    def create_directory(self, directory_name, path="/"):
        """Create FTP directory
        
        :param directory_name: Name of the new directory, should be a string e.g. 'my_directory'
        """
        self.connection.cwd(path)
        try:
            self.connection.mkd(directory_name)
        except error_perm as e:
            if not e.args[0].startswith("550"):  # Exists already
                raise


"""
Keyboard
"""

def easy_key_translation(key):
    """Acitivy supporting key translations
    """
    
    if not key:
        return ''

    key_translation = {'backspace' : '{BACKSPACE}',
    'break' : '{BREAK}',
    'capslock' : '{CAPSLOCK}',
    'delete' : '{DELETE}',
    'alt' : '%',
    'ctrl': '^',
    'shift': '+',                   
    'downarrow' : '{DOWN}',
    'end' : '{END}',
    'enter' : '{ENTER}',
    'escape' : '{ESC}',
    'help' : '{HELP}',
    'home' : '{HOME}',
    'insert' : '{INSERT}',
    'win' : '^{Esc}',
    'leftarrow' : '{LEFT}',
    'numlock' : '{NUMLOCK}',
    'pagedown' : '{PGDN}',
    'pageup' : '{PGUP}',
    'printscreen' : '{PRTSC}',
    'rightarrow' : '{RIGHT}',
    'scrolllock' : '{SCROLLLOCK}',
    'tab' : '{TAB}',
    'uparrow' : '{UP}',
    'f1' : '{F1}',
    'f2' : '{F2}',
    'f3' : '{F3}',
    'f4' : '{F4}',
    'f5' : '{F5}',
    'f6' : '{F6}',
    'f7' : '{F7}',
    'f8' : '{F8}',
    'f9' : '{F9}',
    'f10' : '{F10}',
    'f11' : '{F11}',
    'f12' : '{F12}',
    'f13' : '{F13}',
    'f14' : '{F14}',
    'f15' : '{F15}',
    'f16' : '{F16}',
    '+' : '{+}',
    '^' : '{^}',
    '%' : '{%}',
    '~' : '{~}',
    '(' : '{(}',
    ')' : '{)}',
    '[' : '{[}',
    ']' : '{]}',
    '{' : '{{}',
    '}' : '{}}'
    }


    if key_translation.get(key):
        return key_translation.get(key)
    
    return key

@activity
def press_key(key=None):
    """Press and release an entered key.

    Supported keys:
    [ ' ', '!', '"', '#', '$', '%', '&', "'", '(', ,')', '*', '+', ',', '-', 
    '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<',
     '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 
    'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
     't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'alt', 'backspace', 
     'ctrl', 'delete' 'downarrow', 'rightarrow', 'leftarrow', 'uparrow', 'enter',
    'escape', 'f1', 'f2', f3', 'f4', 'f5', 'f6', 'f7', 'f8',  'f9', 'f10', 'f11',
    'f12', 'f13', 'f14', 'f15', 'f16', 'home', 'insert', 'pagedown', 'pageup', 
    'help', 'printscreen', 'space', 'scrollock', 'tab', shift, 'win']


    If you are using this on Mac Os you might need to grant acces to your terminal application.
    (Security Preferences > Security & Privacy > Privacy > Accessibility)


    """
    import platform

    # Check if system is not running Windows
    if platform.system() != "Windows":
        from pyautogui import press

        if key:
            return press(key)

    import win32com.client
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys(easy_key_translation(key), 0)


@activity
def press_key_combination(first_key, second_key, third_key=None, force_pyautogui=False):
    """Press a combination of two or three keys simultaneously.

    Supported keys:
    [ ' ', '!', '"', '#', '$', '%', '&', "'", '(', ,')', '*', '+', ',', '-', 
    '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<',
     '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 
    'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
     't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'alt', 'backspace', 
     'ctrl', 'delete' 'downarrow', 'rightarrow', 'leftarrow', 'uparrow', 'enter',
    'escape', 'f1', 'f2', f3', 'f4', 'f5', 'f6', 'f7', 'f8',  'f9', 'f10', 'f11',
    'f12', 'f13', 'f14', 'f15', 'f16', 'home', 'insert', 'pagedown', 'pageup', 
    'help', 'printscreen', 'space', 'scrollock', 'tab', shift, 'win']

    :param first_key: First key to press
    :param second_key: Second key to press
    :param third_key: Third key to press, this is optional.
    :param force_pyautogui: Set parameter to true to force the use of pyautogui. This could help when certain keypresses do not work correctly.
    """
    
    import platform

    # Check if system is not running Windows
    if first_key == 'win' or second_key == 'win' or third_key == 'win':
        force_pyautogui = True
    if platform.system() != "Windows" or force_pyautogui:
        from pyautogui import hotkey

        if not third_key:
            return hotkey(first_key, second_key)
        if third_key:
            return hotkey(first_key, second_key, third_key)

    import win32com.client
    shell = win32com.client.Dispatch("WScript.Shell")
    key_combination = easy_key_translation(first_key) + easy_key_translation(second_key) + easy_key_translation(third_key)
    shell.SendKeys(easy_key_translation(key_combination), 0)
    


@activity
def type_keys(text='', interval_seconds=0.01):
    """Keyboard typing
    
    Types text in the current active field by simulating keyboard typing. 

    :param text: Text in string format to type. Note that you can only press single character keys. Special keys like ":", "F1",... can not be part of the text argument.
    :param interval_seconds: Time in seconds between two keystrokes. Defautl value is 0.01 seconds.
    """
    
    import platform

    # Set keyboard layout for Windows platform
    if platform.system() != "Windows":
        from pyautogui import typewrite
        return typewrite(text, interval=interval_seconds)

    shell = win32com.client.Dispatch("WScript.Shell")
    import time
    for character in text:
        shell.SendKeys(easy_key_translation(character), 0)
        time.sleep(interval_seconds)


"""
Mouse
"""

@activity
def get_mouse_position(delay=None, to_clipboard=False):
    """Get the x and y pixel coördinates of current mouse position.

    These coördinates represent the absolute pixel position of the mouse on the computer screen. 
    The x-coördinate starts on the left side and increases going right. The y-coördinate increases going down.

        0,0       X increases -->
    +---------------------------+
    |                           | Y increases
    |                           |     |
    |   1920 x 1080 screen      |     |
    |                           |     V
    |                           |
    |                           |
    +---------------------------+ 1919, 1079

    :param delay: Delay in seconds before capturing mouse position.
    :param to_clipboard: Put the coördinates in the clipboard e.g. 'x=1, y=1'

    :return: Tuple with (x, y) coördinates
    """
    from pyautogui import position
    from time import sleep

    if delay:
        sleep(delay)

    coord = position()

    if to_clipboard:
        set_to_clipboard("x=" + str(coord[0]) + ", y=" + str(coord[1]))

    return coord[0], coord[1]

@activity
def display_mouse_position(duration=10):
    """Display mouse position
    
    Displays mouse position in an overlay. Refreshes every two seconds.
    Can be used to find mouse position of element on the screen

    :param duration: Duration to show overlay.
    """

    if duration < 1 or type(duration) != int:
        return

    from pyautogui import position
    from time import sleep

    duration_half = int(duration / 2)
    for i in range(0,duration_half, 2):
        coord = position()
        message = "x=" + str(coord[0]) + ", y=" + str(coord[1])
        display_osd_message(message, seconds=2)
        sleep(2)


@activity
def click(x=None, y=None):
    """Clicks on a pixel position on the visible screen determined by x and y coördinates.
    """
    from pyautogui import click

    return click(x, y)


@activity
def double_click(x=None, y=None):
    """Double clicks on a pixel position on the visible screen determined by x and y coördinates.

    :param x: 
    """
    from pyautogui import doubleClick

    return doubleClick(x, y)


@activity
def right_click(x=None, y=None):
    """Right clicks on a pixel position on the visible screen determined by x and y coördinates.
    """
    from pyautogui import rightClick

    return rightClick(x, y)


@activity
def move_mouse_to(x=None, y=None):
    """Moves te pointer to a x-y position.
    """
    from pyautogui import moveTo

    return moveTo(x, y)


@activity
def move_mouse_relative(x=None, y=None):
    """Moves the mouse an x- and y- distance relative to its current pixel position.
    """
    from pyautogui import moveRel

    return moveRel(x, y)


@activity
def drag_mouse_to(x=None, y=None, button="left"):
    """Drag the mouse from its current position to a entered x-y position, while holding a specified button.
    """
    from pyautogui import dragTo

    return dragTo(x, y, 0.2, button=button)


@activity
def click_image(filename=None):
    """Click on similar image on the screen

    This function searches the screen for a match with template image and clicks directly in the middle.
    Note that this only finds exact matches.

    :param filename: Path to the template image.
    """
    if not filename:
        return

    from pyautogui import locateCenterOnScreen, click

    x, y = locateCenterOnScreen(filename)

    return click(x, y)


@activity
def double_click_image(filename=None):
    """DOuble click on similar image on the screen

    This function searches the screen for a match with template image and doubleclicks directly in the middle.
    Note that this only finds exact matches.

    :param filename: Path to the template image.
    """
    if not filename:
        return

    from pyautogui import locateCenterOnScreen, click

    x, y = locateCenterOnScreen(filename)

    return click(x, y, 2)


@activity
def right_click_image(filename=None):
    """Right click on similar image on the screen

    This function searches the screen for a match with template image and right clicks directly in the middle.
    Note that this only finds exact matches.

    :param filename: Path to the template image.
    """
    if not filename:
        return

    from pyautogui import locateCenterOnScreen, rightClick

    x, y = locateCenterOnScreen(filename)

    return rightClick(x, y)

@activity
def locate_image_on_screen(filename=None):
    """Find similar image on the screen

    This function searches the screen for a match with template image and clicks directly in the middle.
    Note that this only finds exact matches.

    :param filename: Path to the template image.

    :return: Tuple with (x, y) coördinates
    """
    if not filename:
        return
    from pyautogui import locateCenterOnScreen, click

    x, y = locateCenterOnScreen(filename)

    return x, y


"""
Folder Operations
"""

@activity
def get_files_in_folder(path=None, extension=None):
    """List all files in a folder and subfolders

    Checks all folders and subfolders for files. This could take some time for large repositories. 

    :param path: Path of the folder to retreive files from. Default folder is the home directory.
    :param extension: Optional filter on certain extensions, for example 'pptx', 'exe,' xlsx', 'txt', .. Default value is no filter.

    :return: List of files with their full path
    """
    import os

    if not path:
            path = os.path.expanduser("~")

    paths = []
    for dirpath,_,filenames in os.walk(path):
        for f in filenames:
            full_path = os.path.abspath(os.path.join(dirpath, f))
            if extension:
                if not full_path.endswith(extension):
                    continue
            paths.append(full_path)
    
    return paths

@activity
def create_folder(path):
    """Creates new folder at the given path

    :param path: Full path of folder that will be created
    """
    import os

    if not os.path.exists(path):
        os.makedirs(path)


@activity
def rename_folder(path, new_name):
    """Rename a folder

    :param path: Full path of folder that will be renamed
    :param new_name: New name of the folder e.g. 'new_folder'.
    """
    import os

    if os.path.exists(path):
        base_path = path.split("\\")[:-1]
        new_path = "\\".join(base_path) + "\\" + new_name
        if not os.path.exists(new_path):
            os.rename(path, new_path)


@activity
def show_folder(path=None):
    """Open a folder with the default explorer.

    :param path: Full path of folder that will be opened. Default value is the home directory
    """
    import os

    if not path:
        path = os.path.expanduser("~")

    if os.path.isdir(path):
        os.startfile(path)


@activity
def move_folder(old_path, new_path):
    """Move a folder

    Moves a folder from one place to another.
    If the new location already contains a folder with the same name, a random 8 character uid is added to the name.

    :param old_path: Full path to the source location of the folder
    :param new_path: Full path to the destination location of the folder
    """
    from uuid import uuid4
    import os

    name = old_path.split("\\")[-1]
    new_path = new_location + "\\" + name
    if os.path.isdir(old_path):
        if not os.path.isdir(new_path):
            os.rename(old_path, new_path)
        elif os.path.isdir(new_path):
            new_path = new_path + "_" + str(uuid4())[:8]
            os.rename(old_path, new_path)


@activity
def remove_folder(path, allow_root=False, delete_read_only=True):
    """Remove a folder including all subfolders

    For the function to work optimal, all files and subfolders in the main targetfolder should be closed.

    :param path: Full path to the folder that will be deleted
    :param allow_root: Allow paths with an arbitrary length of 10 characters or shorter to be deleted. Default value is False.
    """
    import os
    import shutil

    if len(path) > 10 or allow_root:
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=delete_read_only)


@activity
def empty_folder(path, allow_root=False):
    """Remove all contents from a folder

    For the function to work optimal, all files and subfolders in the main targetfolder should be closed.

    :param path: Full path to the folder that will be emptied
    :param allow_root: Allow paths with an arbitrary length of 10 characters or shorter to be emptied. Default value is False.
    """
    import os

    if len(path) > 10 or allow_root:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))


@activity
def folder_exists(path):
    """Checks whether folder exists, 
 
    :param path: Full path to folder

    :return: Boolean
    """
    import os

    return os.path.isdir(path)


@activity
def copy_folder(old_path, new_path):
    """Copy a folder

    Copies a folder from one place to another.
    If the new location already contains a folder with the same name, a random 8 character uid is added to the name.

    :param old_path: Full path to the source location of the folder
    :param new_path: Full path to the destination location of the folder
    """
    from uuid import uuid4
    import os
    import shutil

    new_path = new_path + "\\" + old_path.split("\\")[-1]
    if os.path.isdir(old_path):
        if not os.path.isdir(new_path):
            shutil.copytree(old_path, new_path)
        elif os.path.isdir(new_path):
            new_path = new_path + "_" + str(uuid4())[:8]
        shutil.copytree(old_path, new_path)
    return


@activity
def zip_folder(path, new_path=None):
    """Zip a folder and it's contents


    :param path: Full path to the source location of the folder that will be zipped
    :param new_path: Full path to save the zipped folder. If no path is specified a folder with the original folder name plus 8 random characters

    """
    import zipfile
    import os
    import shutil
    from uuid import uuid4

    if not new_path:
        from uuid import uuid4
        new_path = path + "_" + str(uuid4())[:8]
    if os.path.isdir(path):
        shutil.make_archive(new_path, "zip", path)
    return


@activity
def unzip(path, new_path=False):
    """Unzips a file or folder 

    :param path: Full path to the source location of the file or folder that will be unzipped
    :param new_path: Full path to save unzipped contents. If no path is specified the unzipped contents will be stored in the same directory as the zipped file is located. 
    """
    import zipfile
    import os
    import shutil

    if os.path.exists(path):
        zipp = zipfile.ZipFile(path)
        if not new_path:
            base_path = "\\".join(path.split("\\")[:-1])
            zipp.extractall(base_path)
        elif os.path.isdir(new_path):
            zipp.extractall(new_path)
        zipp.close()
    return


"""
Delay
"""

@activity
def wait(seconds=1):
    """Wait function
    
    Not that this activity is blocking. This means that subsequent activities will not occur until the the specified waiting time has expired.
    
    :param seconds: Time in seconds to wait
    """
    from time import sleep

    sleep(seconds)


@activity
def wait_for_image(path=None, timeout=60):
    """Waits for an image to appear on the screen

    Note that this activity waits for an exact match of the template image to appear on the screen. 
    Small variations, such as color or resolution could result in a mismatch.

    :param path: Full or relative path to the template image.
    :param timeout: Maximum time in seconds to wait before continuing. Default value is 60 seconds.
    """

    from pyautogui import locateCenterOnScreen
    from time import sleep

    for _ in range(timeout):
        try:
            locateCenterOnScreen(path)
            break
        except TypeError:
            sleep(1)

@activity
def wait_folder_exists(path, timeout=60):
    """Wait until a folder exists.

    Not that this activity is blocking and will keep the system waiting.

    :param path: Full path to folder.
    :param timeout: Maximum time in seconds to wait before continuing. Default value is 60 seconds.
    """
    from time import sleep

    while not os.path.exists(path):
        sleep(1)
    return

    for _ in range(timeout):
        if os.path.exists(path):
            break
            sleep(1)


"""
Microsoft® Office Word
"""

class Word:
    def __init__(self, visible=True, file_path=None):
        """Start Word Application

        For this activity to work, Microsoft Office Word needs to be installed on the system.

        :parameter visible: Show Word in the foreground if True or hide if False, defaults to True.
        :parameter path: Enter a path to open Word with an existing Word file. If no path is specified a document will be initialized, this is the default value.
        """
        self.file_path = file_path

        self.app = self._launch()
        self.app.Visible = visible
        

    def _launch(self):
        """Utility function to create the Word application scope object

        :return: Application object (win32com.client)
        """
        try:
            import win32com.client

            app = win32com.client.gencache.EnsureDispatch("Word.Application")

        except:
            raise Exception(
                "Could not launch Word, do you have Microsoft Office installed on Windows?"
            )

        if self.file_path:
            app.Documents.Open(self.file_path)
        else:
            app.Documents.Add()

        return app

    @activity
    def append_text(self, text):
        """Append text at end of Word document

        :param text: Text to append to document
        """
        import win32com.client

        wc = win32com.client.constants
        self.app.Selection.EndKey(Unit=wc.wdStory)
        self.app.Selection.TypeText(text)
 
    @activity
    def replace_text(self, placeholder_text, replacement_text):
        """Replace all occurences of text in document

        Can be used for example to replace arbitrary placeholder value. 
        For example when using template slidedeck, using 'XXXX' as a placeholder.
        Take note that all strings are case sensitive.
        
        :parameter placeholder_text: Placeholder text value (string) in the document, this will be replaced, e.g. 'Company Name'
        :parameter replacement_text: Text (string) to replace the placeholder values with. It is recommended to make this unique to avoid wrongful replacement, e.g. 'XXXX_placeholder_XXX'
        """

        self.app.Selection.GoTo(0)
        self.app.Selection.Find.Text = placeholder_text
        self.app.Selection.Find.Replacement.Text = replacement_text
        self.app.Selection.Find.Execute(Replace=2, Forward=True)
        
    @activity
    def read_all_text(self, return_as_list=False):
        """Read all text from Word document

        :param return_as_list: Set this paramater to True to return text as a list of strings. Default value is False.
        """

        if return_as_list:
            return self.app.ActiveDocument.Content.Text.split('\r') 
        return self.app.ActiveDocument.Content.Text
    
    @activity
    def export_to_pdf(self, path=None):
        """Export Word document to PDF

        :parameter path: Output path where PDF file will be exported to. Default path is home directory with filename 'pdf_export.pdf'.
        """

        if not path:
            import os
            path = os.path.expanduser("~") + '/pdf_export.pdf'

        self.app.ActiveDocument.ExportAsFixedFormat(OutputFileName=path,
            ExportFormat=17,
            OpenAfterExport=False,
            OptimizeFor=0,
            CreateBookmarks=1,
            DocStructureTags=True
            )
    
    @activity
    def export_to_html(self, path=None):
        """Export Word document to HTML

        :parameter path: Output path where HTML file will be exported to. Default path is home directory with filename 'html_export.html'.
        """
        if not path:
            import os
            path = os.path.expanduser("~") + '/pdf_export.pdf'

        import win32com.client

        wc = win32com.client.constants
        word.app.ActiveDocument.WebOptions.RelyOnCSS = 1
        word.app.ActiveDocument.WebOptions.OptimizeForBrowser = 1
        word.app.ActiveDocument.WebOptions.BrowserLevel = 0 
        word.app.ActiveDocument.WebOptions.OrganizeInFolder = 0
        word.app.ActiveDocument.WebOptions.UseLongFileNames = 1
        word.app.ActiveDocument.WebOptions.RelyOnVML = 0
        word.app.ActiveDocument.WebOptions.AllowPNG = 1
        word.app.ActiveDocument.SaveAs(FileName= path, FileFormat= wc.wdFormatHTML)
        

    @activity
    def set_footers(self, text):
        """Set footers of Word document

        :param text: Text to put in the footer
        """
        for section in self.app.ActiveDocument.Sections:
            for footer in section.Footers:
                footer.Range.Text = text


    @activity
    def set_headers(self, text):
        """Set headers of Word document

        :param text: Text to put in the header
        """
        for section in self.app.ActiveDocument.Sections:
            for footer in section.Headers:
                footer.Range.Text = text


class WordFile: 
    def __init__(self, file_path=None):
        """Read and Write xlsx files. 

        These activities can read, write and edit Word (docx) files without the need of having Word installed. 
        Note that, in contrary to working with the :func: 'Word' activities, a file get saved directly after manipulation.

        :parameter file_path: Enter a path to open Word with an existing Word file. If no path is specified a 'document.docx' will be initialized in the home directory, this is the default value. If a document with the same name already exists the file will be overwritten.
        """  

        self.file_path = file_path

        self.app = self._launch()

    def _launch(self):

        from docx import Document
        import os

        if self.file_path:
            if not os.path.exists(self.file_path):
                document = Document(self.file_path)
        else:         
            path = os.path.expanduser("~") + '\document.docx'
            document = Document()
            document.save(path)
            self.file_path = path

    @activity
    def read_all_text(self, return_as_list=False):
        """Read all text from Word document

        :param return_as_list: Set this paramater to True to return text as a list of strings. Default value is False.
        """

        from docx import Document

        document = Document(self.file_path)
        text = []
        for paragraph in document.paragraphs:
            text.append(paragraph.text) 
    
        if return_as_list:
            return text
        return '\r'.join(map(str, text))

    @activity
    def append_text(self, text, auto_save=True):
        """Append text at end of Word document

        :param text: Text to append
        :param auto_save: Save document after performing activity. Default value is True
        """
        from docx import Document

        document = Document(self.file_path)
        document.add_paragraph(text)

        if auto_save:
            document.save(self.file_path)

    @activity
    def save(self):

        document.save(self.file_path)

    @activity
    def save_as(self, path):

        document.save(path)

    @activity
    def set_headers(self,text, auto_save=True):
        """Set headers of Word document

        :param text: Text to put in the header
        :param auto_save: Save document after performing activity. Default value is True
        """
        from docx import Document

        document = Document(self.file_path)
        document.add_heading(text)

        if auto_save:
            document.save(self.file_path)

    @activity
    def replace_text(self, placeholder_text, replacement_text, auto_save=True):
        """Replace all occurences of text in document

        Can be used for example to replace arbitrary placeholder value. 
        For example when using template slidedeck, using 'XXXX' as a placeholder.
        Take note that all strings are case sensitive.
        
        :parameter placeholder_text: Placeholder text value (string) in the document, this will be replaced, e.g. 'Company Name'
        :parameter replacement_text: Text (string) to replace the placeholder values with. It is recommended to make this unique to avoid wrongful replacement, e.g. 'XXXX_placeholder_XXX'
        :param auto_save: Save document after performing activity. Default value is True
        """
        from docx import Document

        document = Document(self.file_path)
        for paragraph in document.paragraphs:
            paragraph.text = paragraph.text.replace(placeholder_text, replacement_text)

        if auto_save:
            document.save(self.file_path)

"""
Microsoft® Office Outlook
"""
class Outlook:
    def __init__(self, account_name=None):
        self.app = self._launch()
        self.account_name = account_name

        """Start Outlook Application

        For this activity to work, Outlook needs to be installed on the system.
        """

    def _launch(self):
        """Utility function to create the Outlook application scope object

        :return: Application object (win32com.client)
        """
        try:
            import win32com.client

            app = win32com.client.gencache.EnsureDispatch("outlook.application")

        except:
            raise Exception(
                "Could not launch Outlook, do you have Microsoft Office installed on Windows?"
            )

        return app

    def send_mail(
        self, to_address, subject="", body="", html_body=None, attachment_paths=None
    ):
        """Send an e-mail with Outlook

        :param to_address: The e-mail address the e-mail should be sent to
        :param subject: The subject of the e-mail
        :param body: The text body contents of the e-mail
        :param html_body: The HTML body contents of the e-mail (optional)
        :param attachment_paths: List of file paths to attachments
        """
        # mapi = self.app.GetNamespace("MAPI")

        # Create a new e-mail
        mail = self.app.CreateItem(0)

        mail.To = to_address
        mail.Subject = subject
        mail.Body = body

        if html_body:
            mail.HTMLBody = html_body

        # Add attachments
        if attachment_paths:
            for attachment_path in attachment_paths:
                mail.Attachments.Add(attachment_path)

        # Send the e-mail
        mail.Send()

    def get_folders(self, limit=999):
        """Retrieve list of folders from Outlook

        :param limit: Maximum number of folders to retrieve
        """

        folders = []

        if self.account_name:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(self.account_name).Folders
        else:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(1).Folders
        for folder in found_folders:
            name = folder.Name
            folders.append(name)

        return folders

    def get_mails(self, folder_name="Inbox", fields=None):
        """Retrieve list of messages from Outlook
        
        :param folder_name: Name of the Outlook folder, can be found using :function:`get_folders`.
        :param limit: Number of messages to retrieve
        :param fields: Fields (properties) of e-mail messages to give, requires tupl Stadard is 'Subject', 'Body', 'SentOn' and 'SenderEmailAddress'.

        :return: List of dictionaries containing the e-mail messages with from, to, subject, body and html.
        """

        if not fields:
            fields = ("Subject", "Body", "SenderEmailAddress")

        messages = []

        if self.account_name:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(self.account_name).Folders
        else:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(1).Folders
        for folder in found_folders:
            name = folder.Name
            if name == folder_name:
                break
        else:
            raise Exception(
                "Could not find the folder with name '{}'.".format(folder_name)
            )

        # Loop over the items in the folder
        for item in folder.Items:
            message = {}

            for key in fields:
                try:
                    message[key] = getattr(item, key)
                except AttributeError:
                    pass

            messages.append(message)

        return messages

    def delete_mails(
        self,
        folder_name="Inbox",
        limit=0,
        subject_contains="",
        body_contains="",
        sender_contains="",
    ):
        """Delete e-mails from Outlook

        Deletes email messages in a certain folder. Can be specified by searching on subject, body or sender e-mail.

        :param folder_name: Name of the Outlook folder, can be found using :method:`get_folders`
        :param limit: Maximum number of e-mails to delete in one go
        :param subject_contains: Only delete e-mail if subject contains this
        :param body_contains: Only delete e-mail if body contains this
        :param sender_contains: Only delete e-mail if sender contains this
        
        """
        # Find the appropriate folder
        if self.account_name:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(self.account_name).Folders
        else:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(1).Folders
        for folder in found_folders:
            name = folder.Name
            if name == folder_name:
                break
        else:
            raise Exception(
                "Could not find the folder with name '{}'.".format(folder_name)
            )

        # Loop over the items in the folder
        for i, item in enumerate(folder.Items):

            if limit:
                if i > limit:
                    break

            if subject_contains in item.Subject:
                if body_contains in item.Body:
                    if sender_contains in item.SenderEmailAddress:
                        item.Delete()

    def move_mails(
        self,
        source_folder_name="Inbox",
        target_folder_name="Archive",
        limit=0,
        subject_contains="",
        body_contains="",
        sender_contains="",
    ):
        """Move e-mails from Outlook from one folder to another

        Deletes email messages in a certain folder. Can be specified by searching on subject, body or sender e-mail.

        :param source_folder_name: Name of the Outlook source folder from where e-mails will be moved, can be found using :method:`get_folders`
        :param target_folder_name: Name of the Outlook destination folder to where e-mails will be moved, can be found using :method:`get_folders`
        :param limit: Maximum number of e-mails to move in one go
        :param subject_contains: Only move e-mail if subject contains this
        :param body_contains: Only move e-mail if body contains this
        :param sender_contains: Only move e-mail if sender contains this
        """
        # Find the appropriate source folder
        if self.account_name:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(self.account_name).Folders
        else:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(1).Folders
        for source_folder in found_folders:
            name = source_folder.Name
            if name == source_folder_name:
                break
        else:
            raise Exception(
                "Could not find the folder with name '{}'.".format(source_folder_name)
            )

        # Find the appropriate target folder
        if self.account_name:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(self.account_name).Folders
        else:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(1).Folders
        for target_folder in found_folders:
            name = target_folder.Name
            if name == target_folder_name:
                break
        else:
            raise Exception(
                "Could not find the folder with name '{}'.".format(target_folder_name)
            )

        # Loop over the items in the folder
        for i, item in enumerate(source_folder.Items):

            if limit:
                if i > limit:
                    break

            if subject_contains in item.Subject:
                if body_contains in item.Body:
                    if sender_contains in item.SenderEmailAddress:
                        item.Move(target_folder)

    def save_attachments(self, folder_name="Inbox", target_folder_path=None):
        """Save all attachments from Outlook

        :param folder_name: Name of the Outlook folder, can be found using :function:`get_folders`.
        :param target_folder_path: Path where attachments will be saved. Default is the home directory.

        :return: List of paths to saved attachments.
        """
        import os

        paths = []

        # Set to user home if no path specified
        if not target_folder_path:
            target_folder_path = os.path.expanduser("~")

        # Find the appropriate folder
        if self.account_name:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(self.account_name).Folders
        else:
            found_folders = self.app.GetNamespace("MAPI").Folders.Item(1).Folders
        for folder in found_folders:
            name = folder.Name
            if name == folder_name:
                break
        else:
            raise Exception(
                "Could not find the folder with name '{}'.".format(folder_name)
            )
        # Loop over the items in the folder
        for item in folder.Items:
            for attachment in item.Attachments:
                path = os.path.join(target_folder_path, attachment.FileName)
                attachment.SaveAsFile(path)
                paths.append(path)

        return paths

    def get_contacts(self, fields=None):
        """Retrieve list of contacts from Outlook
        
        :param fields: Fields can be specified as a tuple with their exact names. Standard value is None returning "LastName", "FirstName" and "Email1Address".

        :return: List of dictionaries containing the contact details.
        """
        import win32com.client

        if not fields:
            fields = ("LastName", "FirstName", "Email1Address")

        contacts = []

        mapi = self.app.GetNamespace("MAPI")

        data = mapi.GetDefaultFolder(win32com.client.constants.olFolderContacts)

        for item in data.Items:
            if item.Class == win32com.client.constants.olContact:
                contact = {}
                for key in item._prop_map_get_:
                    if key in fields:
                        if isinstance(getattr(item, key), (int, str)):
                            contact[key] = getattr(item, key)
                contacts.append(contact)

        return contacts

    
    def add_contact(self, email, first_name="", last_name=""):
        """Add a contact in Outlook

        :param email: The e-mail address for the contact
        :param first_name: First name for the contact (optional)
        :param last_name: Last name for the contact (otpional)
        """

        # Create a new contact
        contact = self.app.CreateItem(2)

        contact.Email1Address = email

        if first_name:
            contact.FirstName = first_name

        if last_name:
            contact.LastName = last_name

        contact.Save()


    def quit(self):
        """Quit Outlook
        """
        self.app.Application.Quit()



"""
Microsoft® Office Excel
"""
        
class ExcelFile:
    def __init__(self, file_path=None):
        """Read and Write xlsx files. 

        This activity can read, write and edit Excel (xlsx) files without the need of having Excel installed. 
        Note that, in contrary to working with the :func: 'Excel' activities, a file get saved directly after manipulation.

        :parameter file_path: Enter a path to open Excel with an existing Excel file. If no path is specified a 'workbook.xlsx' will be initialized in the home directory, this is the default value. If a workbook with the same name already exists the file will be overwritten.
        """

        self.file_path = file_path
        self.sheet_name = None  

        self.app = self._launch()

    def _launch(self):

        import openpyxl
        import os
        
        if self.file_path:
            if not os.path.exists(self.file_path):
                #self.book(self.file_path)
                self.book = openpyxl.load_workbook(self.file_path)
        else:
            path = os.path.expanduser("~") + '\workbook.xlsx'
            self.book = openpyxl.load_workbook(path)
            self.file_path = path

    @activity
    def activate_worksheet(self, name):
        """Activates a worksheet

        Activate a worksheet. By default the first worksheet is activated.

        :param name: Name of the worksheet to activate.        
        """

        self.sheet_name= name

    @activity
    def save_as(self, path):
        """Save current Workbook to another location

        :param path: Path where workbook will be saved
        """

        self.book.save(path)

    @activity
    def write_cell(self, column, row, value, auto_save=True):
        """Write Excel cell

        :param column: Column number (integer) to write
        :param row: Row number (integer) to write
        :param value: Value to write to specific cell
        :param auto_save: Save document after performing activity. Default value is True
        """
        
        if self.sheet_name:
            sheet = book[self.sheet_name]
        else:
            sheet = book.active
        
        sheet.cell(row=row, column=column).value = value
        
        if auto_save:
            self.book.save(self.file_path)

    @activity
    def read_cell(self, column, row):
        """ Read Excel cell
        
        :param column: Column number (integer) to read
        :param row: Row number (integer) to read

        :return: Cell value
        """
        if self.sheet_name:
            sheet = self.book[self.sheet_name]
        else:
            sheet = self.book.active

        return sheet.cell(row=row, column=column).value

    @activity
    def add_worksheet(self, name, auto_save=True):
        """Add a new worksheet

        :param name: Name of the worksheet to add
        :param auto_save: Save document after performing activity. Default value is True
        """

        self.book.create_sheet(name)
        if auto_save:
            self.book.save(self.file_path)

    @activity
    def get_worksheet_names(self):
        """Get worksheet names
        """

        return self.book.sheetnames



class Excel:
    def __init__(self, visible=True, file_path=None):
        """Start Excel Application

        For this activity to work, Microsoft Office Excel needs to be installed on the system.
        
        :parameter visible: Show Excel in the foreground if True or hide if False, defaults to True.
        :parameter path: Enter a path to open Excel with an existing Excel file. If no path is specified a workbook will be initialized, this is the default value.
        """
        self.file_path = file_path

        self.app = self._launch()
        self.app.Visible = visible
        

    def _launch(self):
        """Utility function to create the Excel application scope object

        :return: Application object (win32com.client)
        """
        try:
            import win32com.client

            app = win32com.client.gencache.EnsureDispatch("Excel.Application")

        except:
            raise Exception(
                "Could not launch Excel, do you have Microsoft Office installed on Windows?")

        if self.file_path:
            app.Workbooks.Open(self.file_path)
        else:
            app.Workbooks.Add()

        self.workbook = app.ActiveWorkbook
    
        return app

    @activity
    def add_worksheet(self, name=None):
        """Add Excel worksheet
        Adds a worksheet to the current workbook

        :parameter workbook: Workbook object which is retrieved with either new_workbook or open_workbook
        :parmeter name: Give the sheet a name (optional)
        """
        worksheet = self.workbook.Worksheets.Add()
        if name:
            worksheet.Name = name


    @activity
    def activate_worksheet(self, name):
        """Activate worksheet in Excel
        
        :parameter name: Name of the worksheet to activate
        """
        for worksheet in self.workbook.Worksheets:
            if worksheet.Name == name:
                worksheet.Activate()
                
    @activity
    def save(self):
        """Save active Excel Workbook
        """
        self.workbook.Save()


    @activity
    def save_as(self, path):
        """Save current Excel Workbook to another location

        :param path: Path where workbook will be saved
        """
        self.app.DisplayAlerts = False
        self.workbook.SaveAs(path)
        self.app.DisplayAlerts = True
        
    @activity
    def write_cell(self, column, row, value):
        """Write Excel cell

        :param column: Column number (integer) to write
        :param row: Row number (integer) to write
        :param value: Value to write to specific cell
        """
        self.workbook.ActiveSheet.Cells(row, column).Value = value

    @activity
    def read_cell(self, column, row):
        """Read Excel cell

        :param column: Column number (integer) to read
        :param row: Row number (integer) to read

        :return: Cell value
        """
        return self.workbook.ActiveSheet.Cells(row, column).Value

    @activity
    def write_range(self, range_, value):
        """Write Excel range

        :param range_: Range to write to, e.g. "A1:D10"
        :param value: Value to write to range
        """
        self.workbook.ActiveSheet.Range(range_).Value = value

    @activity
    def read_range(self, range_):
        """Read Excel range

        :param range_: Range to read from, e.g. "A1:D10"

        :return value: Values in param range
        """
        return self.workbook.ActiveSheet.Range(range_).Value

    @activity
    def run_macro(self, name):
        """Run Excel macro

        :param name: Name of the macro to run. 
        """
        return self.app.Run(name)

    @activity
    def get_worksheet_names(self):
        """Get worksheet names from active workbook in Excel

        :return: List is worksheet names
        """
        names = []
        
        for worksheet in self.workbook.Worksheets:
            names.append(worksheet.Name)
        
        return names

    @activity
    def get_table(self, name):
        """Get table from active workbook in Excel

        :param: List of table names
        """
        data = []

        for worksheet in self.workbook.Worksheets:
            for list_object in worksheet.ListObjects:
                if list_object.Name == name:
                    for row in list_object.DataBodyRange.Value:
                        data_row = {}
                        for i, column in enumerate(list_object.HeaderRowRange.Value[0]):
                            data_row[column] = row[i]
                        data.append(data_row)
        
        return data

    @activity
    def activate_range(self, range_):
        """Activate range

        :param range_: Range to activate, e.g. "A1:D10"
        """
        self.workbook.ActiveSheet.Range(range_).Select()

    @activity
    def activate_first_empty_cell_down(self):
        """Activate first empty cell down in Excel
        """
        column = self.app.ActiveCell.Column
        row = self.app.ActiveCell.Row
        for cell in self.workbook.ActiveSheet.Columns(column).Cells:
            if not cell.Value and cell.Row > row:
                cell.Select()
                break

    @activity
    def activate_first_empty_cell_right(self):
        """Activate first empty cell down in Excel
        """
        column = self.app.ActiveCell.Column
        row = self.app.ActiveCell.Row
        for cell in self.workbook.ActiveSheet.Rows(row).Cells:
            if not cell.Value and cell.Column > column:
                cell.Select()
                break   

    @activity
    def activate_first_empty_cell_left(self):
        """Activate first empty cell left in Excel
        """
        column = self.app.ActiveCell.Column
        row = self.app.ActiveCell.Row

        for i in range(column):
            if column-i > 0:
                cell = self.workbook.ActiveSheet.Cells(row, column-i)
                if not cell.Value:
                    cell.Select()
                    break

    @activity
    def activate_first_empty_cell_up(self):
        """Activate first empty cell up in Excel
        """
        column = self.app.ActiveCell.Column
        row = self.app.ActiveCell.Row

        for i in range(row):
            if row-i > 0:
                cell = self.workbook.ActiveSheet.Cells(row-i, column)
                if not cell.Value:
                    cell.Select()
                    break

    @activity
    def write_cell_formula(self, column, row, formula):
        """Write Excel cell formula

        :param column: Column number (integer) to write formula
        :param row: Row number (integer) to write formula
        :param value: Formula to write to specific cell e.g. "=10*RAND()"
        """
        self.workbook.ActiveSheet.Cells(row, column).Formula = formula
    
    @activity
    def read_cell_formula(self, column, row, formula):
        """Read Excel cell formula

        :param column: Column number (integer) to read formula
        :param row: Row number (integer) to read formula

        :return: Cell value
        """
        return self.workbook.ActiveSheet.Cells(row, column).Formula


    @activity
    def insert_empty_row(self, row):
        """Insert emtpy row

        Existing data will shift down

        :param row: Row number (integer) where to insert empty row e.g 1
        """
        row_range = 'A' + str(row)
        self.workbook.ActiveSheet.Range(row_range).EntireRow.Insert()

    @activity
    def insert_empty_column(self, column):
        """Insert empty column

        Existing columns will shift to the right

        :param column: Column letter (string) where to insert empty column e.g. 'A'
        """
        column_range = str(column) + '1'
        self.workbook.ActiveSheet.Range(column_range).EntireColumn.Insert()

    @activity
    def delete_row(self, row):
        """Delete row in Excel

        Existing data will shift up

        :param row: Row number (integer) where to delete row e.g 1
        """
        row_range = 'A' + str(row)
        self.workbook.ActiveSheet.Range(row_range).EntireRow.Delete()

    @activity
    def delete_column(self, range_):
        """Delete column in Excel

        Existing columns will shift to the left

        :param column: Column letter (string) where to delete  column e.g. 'A'
        """
        column_range = str(column) + '1'
        self.workbook.ActiveSheet.Range(column_range).EntireColumn.Delete()
        
    @activity
    def export_to_pdf(self, path=None):
        """Export Excel workbook

        :parameter path: Output path where PDF file will be exported to. Default path is home directory with filename 'pdf_export.pdf'.
        """
        if not path:
            import os
            path = os.path.expanduser("~") + '/pdf_export.pdf'

        self.workbook.ActiveSheet.ExportAsFixedFormat(0, path, 0, True, True)

    @activity
    def insert_data_as_table(self, data, range_='A1', table_style="TableStyleMedium2"):
        """Insert list of dictionaries as a table in Excel

        :param data: List of dictionaries to write as table
        :param range_: Range or startingpoint for table e.g. 'A1'
        """
        row = self.workbook.ActiveSheet.Range(range_).Row
        column = self.workbook.ActiveSheet.Range(range_).Column

        column_names = list(data[0].keys())
        data_values = [[d[key] for key in data[0].keys()] for d in data]

        values = [column_names] + data_values
        for i in range(len(values)):
            for j in range(len(values[0])):
                self.workbook.ActiveSheet.Cells(row+i,column+j).Value = values[i][j]

        start_cell = self.workbook.ActiveSheet.Cells(row,column)
        end_cell = self.workbook.ActiveSheet.Cells(row+i,column+j)
        self.workbook.ActiveSheet.Range(start_cell, end_cell).Select()
        self.app.ActiveSheet.ListObjects.Add().TableStyle = table_style

    @activity
    def read_worksheet(self, name=None, headers=False):
        """Read data from worksheet to a list of lists

        :param name: Optional name of worksheet to read. If no name is specified will take active sheet
        :param headers: Boolean to treat first row as headers. Default value is False

        :retun: List of dictionaries with sheet data
        """
        if name:
            self.activate_worksheet(name)
        
        data = self.workbook.ActiveSheet.UsedRange.Value
        
        if isinstance(data, str):
            return data
        
        # Remove empty columns and rows
        data = [list(x) for x in data if any(x)]
        transposed = list(map(list, zip(*data)))
        transposed = [row for row in transposed if any(row)]
        data = list(map(list, zip(*transposed)))

        if headers:
            header_row = data[0]
            data = data[1:]
            data = [{column:row[i] for i, column in enumerate(header_row)} for row in data] 
        
        return data

    @activity
    def quit(self):
        """Close Excel

        This closes excel, make sure to use :func: 'save' or 'save_as' if you would like to save before quitting.
        """
        self.app.Application.Quit()


class PowerPoint:
    def __init__(self, visible=True, path=None, add_slide=True):
        """Start Excel Application

        For this activity to work, PowerPoint needs to be installed on the system.

        :parameter visible: Show PowerPoint in the foreground if True or hide if False, defaults to True.
        :parameter path: Enter a path to open an existing PowerPoint presentation. If no path is specified a new presentation will be initialized, this is the default value.
        :parameter add_slide: Add an initial empty slide when creating new PowerPointfile, this prevents errors since most manipulations require a non-empty presentation. Default value is True
        """
        self.app = self._launch(path)
        self.app.Visible = visible


    def _launch(self, path):
        """Utility function to create the Excel application scope object

        :return: Application object (win32com.client)
        """
        try:
            import win32com.client

            app = win32com.client.gencache.EnsureDispatch("PowerPoint.Application")

        except:
            raise Exception(
                "Could not launch PowerPoint, do you have Microsoft Office installed on Windows?")

        if path:
            return app.Presentations.Open(file_path)
        else:
            return app.Presentations.Add()

    @activity
    def save(self, path=None):
        """Save PowerPoint Slidedeck

        :parameter path: Save the PowerPoint presentation. Default value is the home directory and filename 'presentation.pptx'
        """
        if not path:
            path = os.path.expanduser("~") + '\presentation.pptx'

        return self.app.SaveAs(path)

    @activity
    def quit(self):
        """Close PowerPoint Application
        """
        return self.app.Application.Quit()


    @activity
    def add_slide(self, index=None, type='blank'):
        """Add PowerPoint Slides
        Adds slides to a presentation

        :parameter index: Index where the slide should be inserted. Default value is as final slide.
        :parmeter type: Type of the slide to be added. Supports following types: blank, chart, text, title and picture.
        """
        if type == 'blank':
            type_id = 12
        if type == 'chart':
            type_id = 8
        if type == 'text':
            type_id = 2
        if type == 'title':
            type_id = 1
        if type == 'picture':
            type_id = 36
        
        if not index:
            index = self.app.Slides.Count + 1 

        return self.app.Slides.Add(index,type_id)

    @activity
    def number_of_slides(self):
        """Return the number of slides
        """
        return self.app.Slides.Count

    @activity
    def add_text(self, text, index=None, font_size=48, font_name=None, bold=False, margin_bottom=100, margin_left=100, margin_right=100, margin_top=100):
        """Add text to a slide

        :parameter index: Slide index to add text. If none is specified, a new slide will be added as final slide
        :parmeter text: Text to be added
        :parameter font_size: Fontsize, default value is 48
        :parameter font_name: Fontname, if not specified will take default PowerPoint font
        :parameter bold: Toggle bold with True or False, default value is False
        :parameter margin_bottom: Margin from the bottom in pixels, default value is 100 pixels
        :parameter margin_left: Margin from the left in pixels, default value is 100 pixels
        :parameter margin_right: Margin from the right in pixels, default value is 100 pixels
        :parameter margin_top: Margin from the top in pixels, default value is 100 pixels
        """

        if not index:
            index = self.app.Slides.Count + 1 
            self.app.Slides.Add(index, 12)
        text_box = self.app.Slides(index).Shapes.AddTextbox(1,100, 100,200, 50).TextFrame.TextRange
        text_box.Text = text
        text_box.Font.Size = font_size
        if font_name:
            text_box.Font.Name = font_name
        text_box.Font.Bold = bold

    @activity
    def delete_slide(self,index=None):
        """Delete slide
        
        :parameter index: Slide index to be deleted. If none is specified, last slide will be deleted
        """
        if not index:
            index = self.app.Slides.Count 

        return self.app.Slides(index).Delete()

    @activity
    def replace_text(self, placeholder_text, replacement_text):
        """Replace all occurences of text in Powerpoint slides

        Can be used for example to replace arbitrary placeholder value in a PowerPoint. 
        For example when using a template slidedeck, using 'XXXX' as a placeholder.
        Take note that all strings are case sensitive.
        
        :parameter placeholder_text: Placeholder value (string) in the Powerpoint, this will be replaced, e.g. 'Company Name'
        :parameter replacement_text: Text (string) to replace the placeholder values with. It is recommended to make this unique in your PowerPoint to avoid wrongful replacement, e.g. 'XXXX_placeholder_XXX'
        """
        for slide in self.app.Slides:
            for shape in slide.Shapes:
                shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(placeholder,value)

    @activity
    def export_to_pdf(self, path=None):
        """Export PowerPoint presentation to PDF file

        :parameter path: Output path where PDF file will be exported to. Default path is home directory with filename 'pdf_export.pdf'.
        """

        if self.app.Slides.Count == 0:
            raise Exception('Please add a slide first bedore exporting the presentation.')

        if not path:
            import os
            path = os.path.expanduser("~") + '/pdf_export.pdf'
        
        return  self.app.ExportAsFixedFormat2(path, 2, PrintRange=None)

    @activity
    def export_slides_to_images(self, path=None, type='png'):
        """Export PowerPoint slides to seperate image files

        :parameter path: Output path where image files will be exported to. Default path is home directory.
        :parameter type: Output type of the images, supports 'png' and 'jpg' with 'png' as default value
        """

        if self.app.Slides.Count == 0:
            raise Exception('Please add a slide first bedore exporting the presentation.')

        if not path:
            path = os.path.expanduser("~")

        return self.app.Export(path, 'png')



"""
Microsoft Salesforce
"""

def sf_api_call(action, key, parameters = {}, method = 'get', data = {}):
    """Activity to make calls to Salesforce REST API.

    :params action: Action (the URL)
    :params key: Authorisation key 
    :params parameters: URL params
    :params method: Method (get, post or patch)
    :params data: Data for POST/PATCH.
    """
    headers = {
        'Content-type': 'application/json',
        'Accept-Encoding': 'gzip',
        'Authorization': 'Bearer ' + key
    }
    if method == 'get':
        r = requests.request(method, instance_url+action, headers=headers, params=parameters, timeout=30)
    elif method in ['post', 'patch']:
        r = requests.request(method, instance_url+action, headers=headers, json=data, params=parameters, timeout=10)
    else:
        raise ValueError('Method should be get or post or patch.')
    print('Debug: API %s call: %s' % (method, r.url) )
    if r.status_code < 300:
        if method=='patch':
            return None
        else:
            return r.json()
    else:
        raise Exception('API error when calling %s : %s' % (r.url, r.content))

"""
E-mail (SMTP)
"""


@activity
def send_mail_smtp(
    smtp_host, smtp_user, smtp_password, to_address, subject="", message="", port=587
):
    """This function lets you send emails with an e-mail address. 
    
    The first and second arguments require the mail address and password of your e-mail account. 
    The destination is the receiving mail address. The subject and message variables contain respectively 
    the mail subject and the text in the mail. The port variable is standard 587. 
    In most cases this argument can be ignored, but in some cases it needs to be changed to 465.
    """
    BODY = "\r\n".join(
        [
            "To: %s" % destination,
            "From: %s" % user,
            "Subject: %s" % subject,
            "",
            message,
        ]
    )
    smtpObj = smtplib.SMTP(host, port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(user, password)
    smtpObj.sendmail(user, destination, BODY)
    smtpObj.quit()


"""
Windows
"""


@activity
def set_user_password(username, password):
    """Sets the password for a Windows user.

    :parameter username: Username
    :parameter password: New password
    """
    from win32com import adsi

    user = adsi.ADsGetObject("WinNT://localhost/%s,user" % username)
    user.SetPassword(password)


@activity
def check_user_password(username, password):
    """Checks a password for a Windows user
    
    :parameter username: Username
    :parameter password: New password

    :return: True if the password is correct
    """
    from win32security import LogonUser
    from win32con import LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT

    try:
        LogonUser(
            username,
            None,
            password,
            LOGON32_LOGON_INTERACTIVE,
            LOGON32_PROVIDER_DEFAULT,
        )
    except:
        return False
    return True

@activity
def lock_windows():
    """Locks Windows requiring login to continue
    """
    import ctypes
    ctypes.windll.user32.LockWorkStation()

@activity
def is_logged_in():
    """Checks if the current user is logged in and not on the lockscreen. A lot of automations do not work properly when the desktop is locked.

    :return: True if the user is logged in
    """
    import subprocess

    output = subprocess.check_output("TASKLIST")

    if "LogonUI.exe" in str(output):
        return False
    else:
        return True


@activity
def desktop_locked():
    """Checks if the current user is locked out and on the lockscreen. A lot of automations do not work properly when the desktop is locked.

    :return: True when the lockscreen is active
    """
    return not is_logged_in()

@activity
def get_username():
    """Get current logged in user's username
    """
    import getpass
    return getpass.getuser()

class ActiveDirectory:
    """ Interface to Windows Active Directory through ADSI
    """

    def __init__(self, ldap_server=None, username=None, password=None):
        import pyad

        self.pyad = pyad
        
        if ldap_server:
            self.pyad.set_defaults(ldap_server=ldap_server)

        if username:
            self.pyad.set_defaults(username=username)

        if password:
            self.pyad.set_defaults(password=password)
    @activity
    def get_object_by_distinguished_name(self, distinguished_name):
        return self.pyad.from_dn(distinguished_name)

@activity
def set_to_clipboard(text):
    """Set any text to the Windows clipboard. 
    Credit to Cees Timmerman (https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python)

    :parameter text: Text to put in the clipboard
    """
    import win32clipboard

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()


@activity
def get_from_clipboard():
    """Get the text currently in the Windows clipboard
    Credit to Cees Timmerman (https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python)

    :return: Text currently in the clipboard
    """
    import win32clipboard

    win32clipboard.OpenClipboard()
    try:
        data = str(win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT))
        return data

    except Exception as e:
        raise e

    finally:
        win32clipboard.CloseClipboard()


@activity
def clear_clipboard():
    """Empty the clipboard
    """
    from ctypes import windll

    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    return


@activity
def run_vbs_script(script_path, parameters=[]):
    """Run a VBScript file

    :parameter script_path: Path to the .vbs-file
    :parameter parameters: Additional arguments to pass to the VBScript
    """
    import subprocess

    subprocess.call(["cscript.exe", script_path] + parameters)


@activity
def beep(frequency=1000, duration=250):
    """Make a beeping sound.

    :param frequency: Integer to specify frequency (Hz), default value is 1000 Hz
    :param duration: Integer to specify duration of beep in miliseconds (ms), default value is 250 ms.
    """
    import winsound

    winsound.Beep(frequency, duration)


@activity
def speak(text, speed=None):
    """Use the Text-To-Speech engine available on your system

    :param text: The text which should be said
    :param speed: Multiplication factor for the speed at which the text should be pronounced. 
    """
    import pyttsx3

    engine = pyttsx3.init()

    if speed:
        default_rate = engine.getProperty("rate")
        engine.setProperty("rate", speed * default_rate)

    engine.say(text)
    engine.runAndWait()



"""
Utilities
"""


@activity
def home_path():
    """Returns the current user's home path

    :return: Path to the current user's home folder
    """
    from os.path import expanduser

    return expanduser("~")


@activity
def desktop_path():
    """Returns the current user's desktop path
    :return: Path to the current user's desktop folder
    """
    import os.path

    return os.path.join(os.path.expanduser("~"), "Desktop")

@activity
def set_wallpaper(image_path):
    """Sets desktop wallpaper

    :parameter image_path: Path to the image. This image will be set as desktop wallpaper
    """
    import ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)

@activity
def download_file_from_url(url, target_path=''):
    """Download file from a URL

    :param url: Source URL to download file from
    :param target_path: Target path. If no path is given will download in working directory.
    """
    import requests
    import re
    import os

    r = requests.get(url, stream=True)

    if r.status_code == 200:
        if not target_path:
            fn = os.path.basename(url)
            target_path = os.path.join(os.getcwd(), fn)

        with open(target_path, 'wb') as f:
            f.write(r.content)

        return target_path

    else:
        raise Exception('Could not download file from {}'.format(url))

"""
Trello
"""

class TrelloInterface:
    pass

    @activity
    def add_card(
        self,
        title="My card",
        description="My description",
        board_name="My board",
        list_name="My list",
        api_key="",
        api_secret="",
        token="",
        token_secret="any",
    ):
        """Add card to a Trello board
        For this you need a Trello API key, secret and token. 
        Token secret can be any string, but should be altered for security purposes.
        """
        from trello import TrelloClient

        client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            token=token,
            token_secret=token_secret,
        )

        trello_boards = client.list_boards()
        for trello_board in trello_boards:
            if trello_board.name == board_name:
                target_board = trello_board
                break

        trello_lists = target_board.all_lists()
        for trello_list in trello_lists:
            if trello_list.name == list_name:
                target_list = trello_list
                break

        target_list.add_card(title, desc=description)


"""
System
"""


@activity
def rename_file(old_path, new_file_name):
    """Rename a file
    
    This activity will not rename the file if a file with the desired name already exists in the folder.

    :param old_path: Full path to the file that will be renamed
    :param new_file_name: Name of the new file
    """
    import os

    if os.path.isfile(old_path):
        base_path = old_path.split("\\")[:-1]
        new_path = "\\".join(base_path) + "\\" + new_file_name
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)


@activity
def move_file(old_path, new_location):
    """Move a file

    If the new location already contains a file with the same name, a random 8 character uid will be added 
    in front of the name before the file is moved.

    :param old_path: Full path to the file that will be renamed
    :param new_location: Path to the folder where file will be moved to
    """
    import uuid
    import os

    name = old_path.split("\\")[-1]
    new_path = new_location + "\\" + name
    if os.path.exists(old_path):
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
        elif os.path.exists(new_path):
            new_path = new_location + "\\" + "(" + str(uuid.uuid4())[:8] + ") " + name
            os.rename(old_path, new_path)
    return


@activity
def remove_file(path):
    """Remove a file

    :param path: Full path to the file that will be deleted.
    """

    import os
    if os.path.isfile(path):
        os.remove(path)
    return


@activity
def file_exists(path):
    """Check if file exists

    This function checks whether the file with the given path exists.

    :param path: Full path to the file to check.

    return: True or False (boolean)
    """
    import os
    return os.path.isfile(path)

@activity
def wait_file_exists(path, timeout=60):
    """Wait until a file exists.

    Not that this activity is blocking and will keep the system waiting.

    :param path: Full path to file.
    :param timeout: Maximum time in seconds to wait before continuing. Default value is 60 seconds.
    """
    from time import sleep

    while not os.path.exists(path):
        sleep(1)
    return

    for _ in range(timeout):
        if os.path.exists(path):
            break
            sleep(1)

@activity
def write_list_to_file(list_to_write, file_path):
    """Writes a list to a  text (.txt) file. 
    
    Every element of the entered list is written on a new line of the text file.
    
    :param list_to_write: List to write to .txt file
    :param path: Path to the text-file. If the specified path does not exist, the function will create a new .txt file. 
    """
    with open(file_path, "w") as filehandle:
        filehandle.writelines("%s\n" % place for place in list_to_write)
    return


@activity
def read_list_from_txt(file_path):
    """Read txt file
    
    This activity writes the content of a .txt file to a list and returns that list. 
    Every new line from the .txt file becomes a new element of the list. The activity will 
    not work if the entered path is not attached to a .txt file.

    :param path: Path to the .txt file

    :return: List with contents of specified .txt file
    """
    written_list = []
    with open(file_path, "r") as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            current_place = line[:-1]
            written_list.append(current_place)
    return written_list


@activity
def append_line(text, file_path):
    """Append a text line to a file and creates the file if it does not exist yet.

    :parameter text: The text line to write to the end of the file
    :parameter file_path: Path to the file to write to
    """
    import os

    if not os.path.isfile(file_path):
        with open(file_path, "a"):
            os.utime(file_path, None)

    with open(file_path, "a") as f:
        f.write("\n" + text)


@activity
def copy_file(old_path, new_path=None):
    """Copy a file

    Copies a file from one place to another.
    If the new location already contains a file with the same name, a random 8 character uid is added to the name.

    :param old_path: Full path to the source location of the folder
    :param new_path: Optional full path to the destination location of the folder. If not specified file will be copied to the same location with a random 8 character uid is added to the name.
    """
    from uuid import uuid4
    import os
    import shutil

    if not new_path:
        new_path = old_path

    if os.path.isfile(old_path):
        if not os.path.isfile(new_path):
            shutil.copy(old_path, new_path)
        elif os.path.isfile(new_path):
            filename, file_extension = os.path.splitext(old_path)
            new_path = filename + "_" + str(uuid4())[:8] + file_extension
        shutil.copy(old_path, new_path)
    return

@activity
def get_file_extension(path):
    """Get extension of a file
    
    :param path: Path to file to get extension from

    :return: String with extension, e.g. '.txt'
    """

    import os 
    filename, file_extension = os.path.splitext(old_path)

    return file_extension


@activity
def send_to_printer(file):
    """Send file to default printer to print

    This activity sends a file to the printer. Make sure to have a default printer set up.

    :parameter file: Path to the file to print, should be a printable file
    """
    import os
    os.startfile(file, 'print')

"""
Automagica Portal Reporting
"""


@activity
def insert_table_header(data):
    """Inserts the header of an Automagica Report.

    :param data: List of dictionaries that will be parsed as headers
    """
    data_keys = []

    for row in data:
        for key, _ in row.items():
            if key not in data_keys:
                data_keys.append(key)

    header = "|".join(data_keys)

    header_next = "|".join(["---" for key in data_keys])

    print("AUTOMAGICA_MARKDOWN_START: " + str(header) + " :AUTOMAGICA_MARKDOWN_END")
    print(
        "AUTOMAGICA_MARKDOWN_START: " + str(header_next) + " :AUTOMAGICA_MARKDOWN_END"
    )

    return data_keys


@activity
def insert_table_item(item, keys):
    """Inserts the header of an Automagica Report.

    :param item: Item to add
    :param keys: Keys to add
    """
    print(
        "AUTOMAGICA_MARKDOWN_START: "
        + "|".join([str(item.get(key, "")) for key in keys])
        + " :AUTOMAGICA_MARKDOWN_END"
    )


@activity
def insert_table(data):
    """Add data to portal reporting

    Function to report in the Automagica Portal. Can be used to generate reports, 
    logs and worklists. Only available to users with access to the Portal. 
    This outputs a list of flat dicts to a markdown table with headers to the console.

    :param data: List of dictionaries to add to portal
    """
    keys = insert_table_header(data)

    for item in data:
        insert_table_item(item, keys)


@activity
def insert_title(title="My title", level=1):
    """Function to insert a report title in the Automagica Portal.
    
    :param title: String to add as title
    """
    print("AUTOMAGICA_MARKDOWN_START: " + "#" * level + " :AUTOMAGICA_MARKDOWN_END")


"""
PDF
"""


@activity
def read_text_from_pdf(file_path):
    """Extracts the text from a PDF

    This activity reads text from a pdf file. Can only read PDF files that contain a text layer.
    
    :param file_path: Path to the PDF (either relative or absolute)
    :return: The text from the PDF
    """
    from PyPDF2 import PdfFileReader

    text = ""

    with open(file_path, 'rb') as f:
        reader = PdfFileReader(f)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            text += page.extractText()

    return text


@activity
def join_pdf_files(file_paths, output_path):
    """Merges multiple PDFs into a single file

    :param file_paths: List of paths to PDF files
    :param output_path: Full path where joined pdf files can be written
    """
    from PyPDF2 import PdfFileMerger, PdfFileReader

    merger = PdfFileMerger()
    for file_path in file_paths:
        with open(file_path, "rb") as f:
            merger.append(PdfFileReader(f))

    merger.write(output_path)


@activity
def extract_page_range_from_pdf(file_path, start_page, end_page, output_path):
    """Extracts a particular range of a PDF to a separate file

    :param file_path: Path to the PDF (either relative or absolute)
    :param start_page: Page number to start from, with 0 being the first page
    :param end_page: Page number to end with, with 0 being the first page
    """
    from PyPDF2 import PdfFileWriter, PdfFileReader

    with open(file_path, "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        for i in range(start_page, end_page):
            writer.addPage(reader.getPage(i))

        with open(output_path, "wb") as f:
            writer.write(f)


@activity
def extract_images_from_pdf(file_path):
    """Save a specific page from a PDF as an image

    Credits to user Sylvain on Stackoverflow (https://stackoverflow.com/a/34116472)

    :param file_path: Full path to store extracted images
    """
    from PyPDF2 import PdfFileReader
    from PIL import Image

    with open(file_path, "rb") as f:
        reader = PdfFileReader(f)
        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            objects = page["/Resources"]["/XObject"].getObject()

            for obj in objects:
                if objects[obj]["/Subtype"] == "/Image":
                    size = (objects[obj]["/Width"], objects[obj]["/Height"])
                    data = objects[obj].getData()

                    if objects[obj]["/ColorSpace"] == "/DeviceRGB":
                        mode = "RGB"
                    else:
                        mode = "P"

                    if objects[obj]["/Filter"] == "/FlateDecode":
                        img = Image.frombytes(mode, size, data)
                        img.save(obj[1:] + ".png")

                    elif objects[obj]["/Filter"] == "/JPXDecode":
                        img = open(obj[1:] + ".jp2", "wb")
                        img.write(data)
                        img.close()

@activity
def apply_watermark_to_pdf(
    file_path, watermark_path, output_path=''):
    """Watermark a PDF

    :param file_path: Filepath to the document that will be watermarked. Should be pdf file.
    :param watermark_path: Filepath to the watermark. Should be pdf file.
    """
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import os

    watermark = PdfFileReader(open(watermark_path, "rb"))

    input_file = PdfFileReader(open(file_path, "rb"))

    page_count = input_file.getNumPages()

    output_file = PdfFileWriter()

    for page_number in range(page_count):
       input_page = input_file.getPage(page_number)
       input_page.mergePage(watermark.getPage(0))
       output_file.addPage(input_page)

    if not output_path:
        output_path = file_path.replace('.pdf', '_watermarked.pdf')

    with open(output_path, "wb") as outputStream:
       output_file.write(outputStream)


"""
System monitoring
"""


@activity
def get_cpu_load(measure_time=1):
    """Get  average CPU load for all cores.

    param measure_time: Time (seconds) to measure load. Displayed load is an average over measured_time. Standard measure_time is 1 second.

    """
    import psutil

    cpu_measurements = []
    for _ in range(measure_time):
        cpu_measurements.append(psutil.cpu_percent(interval=1))
    return sum(cpu_measurements) / len(cpu_measurements)


@activity
def get_number_of_cpu(logical=True):
    """Get the number of CPU's in the current system. 

    :param logical: Determines if only logical units are added to the count, default value is True.
    """
    import psutil

    return psutil.cpu_count(logical=logical)


@activity
def get_cpu_frequency():
    """Get frequency at which CPU currently operates.
    
    Also shows minimum and maximum frequency.
    """
    import psutil

    return psutil.cpu_freq()


@activity
def get_cpu_stats():
    """Get CPU statistics
    
    Number of CTX switches, intterupts, soft-interrupts and systemcalls.
    """
    import psutil

    return psutil.cpu_stats()


@activity
def get_memory_stats(mem_type="swap"):
    """Get  memory statistics
    
    Total, used, free and percentage in use.
    :param mem_type: Choose mem_type = 'virtual' for virtual memory, and mem_type = 'swap' for swap memory (standard).
    """
    import psutil

    if mem_type == "virtual":
        return psutil.virtual_memory()
    else:
        return psutil.swap_memory()


@activity
def get_disk_stats():
    """Get disk statistics of main disk
    
    Total, used, free and percentage in use.
    """
    import psutil

    return psutil.disk_usage("/")


@activity
def get_disk_partitions():
    """Get disk partition info

    Returns tuple with info for every partition.
    """
    import psutil

    return psutil.disk_partitions()


@activity
def get_boot_time():
    """Get most recent boot time

    Returns time PC was booted in seconds after the epoch.
    """
    import psutil

    return psutil.boot_time()


@activity
def get_time_since_last_boot():
    """Get uptime since last boot

    Returns time since last boot in seconds.
    """
    import time
    import psutil

    return time.time() - psutil.boot_time()


"""
Image operations
"""


@activity
def show_image(path):
    """Open image in default viewer

    Displays an image specified by the path variable on the default imaging program.

    :param path: Full path to image
    """
    from PIL import Image

    im = Image.open(path)

    return im.show()


@activity
def rotate_image(path, angle=90):
    """Rotate an image

    :param angle: Degrees to rotate image. Note that angles other than 90, 180, 270, 360 can resize the picture. 
    """
    from PIL import Image

    im = Image.open(path)

    return im.rotate(angle, expand=True).save(path)


@activity
def resize_image(path, size):
    """Resize image

    Resizes the image specified by the path variable. The size is specifie by the second argument. This is a tuple with the
    width and height in pixels. E.g. ResizeImage("C:\\Users\\Pictures\\Automagica.jpg", (300, 400)) gives the image a width
    of 300 pixels and a height of 400 pixels.

    :param path: Path to the image
    :param size: Tuple with new size e.g. (300, 400)
    """
    from PIL import Image

    im = Image.open(path)

    return im.resize(size).save(path)


@activity
def get_image_width(path):
    """Get with of image

    :param path: Path to image
    """
    from PIL import Image

    im = Image.open(path)

    width, _ = im.size

    return width


@activity
def get_image_height(path):
    """Get height of image

    :param path: Path to image
    """
    from PIL import Image

    im = Image.open(path)

    _, height = im.size

    return height


@activity
def crop_image(path, box=None):
    """Crpo image
    Crops the image specified by path to a region determined by the box variable.

    :param path: Path to image
    :param box:  A tuple that defines the left, upper, right and lower pixel coördinate e.g.: (left, upper, right, lower)
    """
    im = Image.open(path)
    return im.crop(box).save(path)



@activity
def mirror_image_horizontally(path):
    """Mirror image
    Mirrors an image with a given path horizontally from left to right.

    :param path: Path to image
    """
    im = Image.open(path)
    return im.transpose(Image.FLIP_LEFT_RIGHT).save(path)


@activity
def mirror_image_vertically(path):
    """
    Mirrors an image with a given path vertically from top to bottom.

    :param path: Path to image
    """
    im = Image.open(path)
    return im.transpose(Image.FLIP_TOP_BOTTOM).save(path)


"""
Process
"""

@activity
def run(task):
    """Use Windows Run to boot a process

    Note this uses keyboard inputs which means this process can be disrupted by interfering inputs

    :param task: Name of the task to run e.g. 'mspaint.exe'
    """
    from pyautogui import hotkey, typewrite, press
    import time

    hotkey('winleft', 'r')
    time.sleep(0.5)

    import platform

    # Set keyboard layout for Windows platform
    if platform.system() == "Windows":
        from win32api import LoadKeyboardLayout
        LoadKeyboardLayout("00000409", 1)

    typewrite(task, interval=0.01)
    press('enter')

@activity
def is_process_running(name):
    """Check if process is running
    Checks if given process name (name) is currently running on the system.

    :param name: Name of process
    :return: Boolean
    """
    import psutil

    if name:
        for p in psutil.process_iter():
            if name in p.name():
                return True

    return False


@activity
def get_running_processes():
    """Get names of unique processes currently running on the system.

    :return: List of unique running processes
    """
    import psutil

    process_list = []

    for p in psutil.process_iter():
        process_list.append(p.name())

    return list(set(process_list))


@activity
def start_process(path):
    """Start a program or process

    :param path: Path to executable
    """
    from subprocess import Popen

    return Popen(path)


@activity
def kill_process(name=None):
    """Kill a process

    Kills a process forcefully

    :param name: Name of the process
    """
    import os
    return os.system("taskkill /f /im " + name + " >nul 2>&1")


""" 
Optical Character Recognition
"""


@activity
def extract_text_from_image(file_path):
    """Extract text from image
    
    Extracts any text from an image. Requires tesseract to be installed locally

    :param file_path: Path to image
    """
    import pytesseract
    from pytesseract import image_to_string
    import platform
    from PIL import Image

    if platform.system() == "Windows":
        pytesseract.pytesseract.tesseract_cmd = (
            "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract"
        )

    return image_to_string(Image.open(file_path))


"""
Office 365
"""


@activity
def send_email_with_outlook365(client_id, client_secret, to_email, subject='', body=''):
    """Send email directly with Office Outlook 365

    :param client_id: Client id for office 365 account
    :param client_secret: Client secret for office 365 account
    :param to_email: E-mail to send to
    :param subject: Optional subject
    :param body: Optional body of the email
    """
    from O365 import Account

    credentials = (client_id, client_secret)

    account = Account(credentials)
    m = account.new_message()
    m.to.add(to_email)
    m.subject = subject
    m.body = body
    m.send()


"""
SAP
"""


class SAPGUI:
    def __init__(self):
        pass

