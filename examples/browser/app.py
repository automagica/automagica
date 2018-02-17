from automagica import ChromeBrowser

""" 
Browses to Google, searches for our GitHub project, opens the first Google Search result link
"""

browser = ChromeBrowser()

browser.get('https://google.com')

browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('oakwoodai automagica')

browser.find_element_by_xpath('//*[@id="lst-ib"]').submit()

browser.find_elements_by_class_name('r')[0].click()