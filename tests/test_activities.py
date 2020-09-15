"""Copyright 2020 Oakwood Technologies BVBA"""


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
    from automagica.activities import Chrome
    # Open Chrome
    chrome = Chrome(auto_update_chromedriver=True)

    # Browse to Google
    chrome.browse_to("https://google.com")

    # Save the page source
    source = chrome.page_source

    # Quit the browser
    chrome.quit()

    assert "Google" in source


def test_cryptography_activities():
    """
    Test scenario to test encrypting and decrypting activities
    """
    from automagica.activities import generate_random_key, encrypt_text_with_key, decrypt_text_with_key

    # Generate a random key
    key = generate_random_key()
    
    # Encrypt text with generated key
    encrypted_text = encrypt_text_with_key('Testing', key)

    # Decrypt text with same key
    decrypted_text = decrypt_text_with_key(encrypted_text, key)

    assert decrypted_text == 'Testing'

