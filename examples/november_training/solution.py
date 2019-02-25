from automagica import *

def click_qlik_sheet(name):
    sheets = browser.find_elements_by_class_name('thumb-hover')
    for i, app in enumerate(browser.find_elements_by_id('item-title')):
        if name.lower() in app.text.lower():
            sheets[i].click()
    return

def wait_for_qlik_login_screen():
    for i in range(10):
        try:
            browser.find_element_by_xpath('//*[@id="MemberLoginForm_LoginForm_Username"]')
            return
        except:
            Wait(1)
    return

def get_iframe():
    return browser.find_elements_by_tag_name('iframe')[0].get_attribute('src')

# Initialise browser and to go qlikid.qlik.com.
browser = ChromeBrowser()
browser.get('https://qlikid.qlik.com/signin')

# Wait for the page to load  (login screen specific)
wait_for_qlik_login_screen()

# Login using username and password
username_field = browser.find_element_by_xpath('//*[@id="MemberLoginForm_LoginForm_Username"]')
username_field.send_keys('USERNAME')

password_field = browser.find_element_by_xpath('//*[@id="MemberLoginForm_LoginForm_Password"]')
password_field.send_keys('PASSWORD')

login_button = browser.find_element_by_xpath('/html/body/section/div/div[2]/input[1]')
login_button.click()

# Go to Qlikcloud.com, directly select the right Sheet.
browser.get('https://eu.qlikcloud.com/view/5981e189428a420001e16cab')

# Wait for page to load
Wait(5)

# Go into Iframe
browser.get(get_iframe())

# Wait for the page to load
Wait(5)

# Look for the Sheet with summary in it.
click_qlik_sheet('summary')

# Wait for the page to load
Wait(5)

# Save screenshot
browser.save_screenshot('result.png')
print('Saved Screenshot!')