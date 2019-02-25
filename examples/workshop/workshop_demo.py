"""
Initialising Automagica
""""

from automagica import *

"""
Browser Automation - Opening
""""

from automagica import *
browser = ChromeBrowser()

"""
Browser Automation - Opening Google.com
""""

from automagica import *
browser = ChromeBrowser()
browser.get('https://google.com')

"""
Browser Automation - Opening Google.com and showing title
""""

from automagica import *
browser = ChromeBrowser()
browser.get('https://google.com')
title = browser.title
browser.close()
DisplayMessageBox(title)

"""
Browser Automation - Searching on Google with Xpath
"""

from automagica import *
browser = ChromeBrowser()
browser.get('https://google.com')
# Enter Search Text
browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('Oslo')
# Submit
browser.find_element_by_xpath('//*[@id="lst-ib"]').submit()

"""
Browser Automation - Searching on Google with ?q in URL
"""

from automagica import *
browser = ChromeBrowser()
browser.get('https://google.com/?q=oslo')

"""
Browser Automation - Searching on Bing with Xpath
"""

from automagica import *
browser = ChromeBrowser()
browser.get('https://bing.com')
# Enter Search Text
browser.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('Oslo')
# Submit
browser.find_element_by_xpath('//*[@id="sb_form_q"]').submit()

"""
Browser Automation - Searching on Bing with ?q in URL
"""

from automagica import *
browser = ChromeBrowser()
browser.get('https://bing.com/?q=oslo')

"""
Finding Google search results with Automagica
"""

from automagica import *
GetGoogleSearchLinks("oslo")

"""
Visit every Google Search Result for Oslo
"""

from automagica import *
browser = ChromeBrowser()
for link in GetGoogleSearchLinks("oslo"):
    browser.get(link)

"""
Save every Google Search Result for Oslo in a .txt
"""

from automagica import *
browser = ChromeBrowser()
links = GetGoogleSearchLinks("oslo")
WriteListToFile(links, file="results.txt")

"""
Browser Automation - Closing
""""
from automagica import *

browser = ChromeBrowser()
browser.get('https://bing.com')
title = browser.title
if not "Google" in title:
    browser.close()
    DisplayMessageBox(title, title="Oops!", type="warning")

"""
Simple Mouse Example 1
"""

from automagica import *
GetMouseCoordinates()

"""
Simple Mouse Example 2
"""

from automagica import *
x = 100
y = 100
DoubleClickOnPosition(x, y)

"""
Simple Mouse Example - Failsafe
"""

from automagica import *
import random

for i in range(0,10):
    random_X_position = random.randint(300,500)
    random_Y_position = random.randint(300,500)
    DragToPosition(random_X_position, random_Y_position)

"""
Copy File, in this case an xlsx
"""
from automagica import *
Copyfile("example.xlsx", "copy.xlsx")    

