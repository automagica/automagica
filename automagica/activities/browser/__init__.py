def start_chrome(ignore_images=False, headless=False):
    """Opens the Chrome Browser with the Selenium webdriver.
    Args:
        ignore_images (bool): do not load images
        headless (bool): run without a window

    Returns:
        webdriver: Selenium Webdriver

    Example:
        browser = ChromeBrowser(ignore_iamges=True)
        browser.get('https://automagica.io')

    """
    import platform
    import os
    from selenium.webdriver import Chrome, ChromeOptions

    # Check what OS we are on
    if platform.system() == "Linux":
        chromedriver_path = "\\bin\\webdriver\\linux64\\chromedriver"
    elif platform.system() == "Windows":
        chromedriver_path = "\\bin\\win32\\chromedriver.exe"
    else:
        chromedriver_path = "\\bin\\mac64\\chromedriver.exe"

    chrome_options = ChromeOptions()

    if headless:
        chrome_options.add_argument("--headless")

    if ignore_images:
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

    return Chrome(
        os.path.abspath('') + chromedriver_path,
        chrome_options=chrome_options,
    )

