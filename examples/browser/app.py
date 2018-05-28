from automagica import *

""" 
Browses to Google, searches for our GitHub project, opens the first Google Search result link
"""

# Initiate browser
browser = ChromeBrowser()
# Surf to google.com
browser.get('https://google.com')
# Enter searchterm
browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('oakwoodai automagica')
# Click on search button
browser.find_element_by_xpath('//*[@id="lst-ib"]').submit()
# Select first hit
browser.find_elements_by_class_name('r')[0].click()
