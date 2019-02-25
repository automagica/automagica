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


# Wait for the page to load  (login screen specific)


# Login using username and password


# Go to Qlikcloud.com, directly select the right Sheet.


# Wait for page to load


# Go into Iframe


# Wait for the page to load


# Look for the Sheet with summary in it.


# Wait for the page to load


# Save screenshot
