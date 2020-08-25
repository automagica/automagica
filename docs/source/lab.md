# Automagica Lab

## Introduction
The Automagica Lab allows you to build software bots from an interactive development environment (IDE) based on Jupyter Notebooks. Those familiar with Jupyter Notebooks and Python will feel right at home with the Automagica Lab. 

## Getting started
After installing Automagica, you can launch the Automagica Lab with the following command:
```bash
automagica lab new
```
If you'd like to edit an existing Automagica Lab file (ending with `.ipynb`), run the following command:
```bash
automagica lab edit examples/automagica_lab_example.ipynb
```

!RECORDING Automagica Lab

## Tips when starting out Automagica in an interactive development environment (IDE)

Instead using Automagica Lab, you can use your own editor or Notebook environment.
Most activities come with a short example of how to use them under the [activities-section in this documentation](activities.rst).

_Note: after installing Python and Automagica start your scripts by importing Automagica to get access to all functionalities._

```
from automagica import *
```

### Variables

Most Automagica activities make us of parameters. Some are required and some are optional for more flexibility and advanced usage. The chapter 'Activities' contains a list of all the activities and their possible parameters. 

In general a parameter can be a word (string), a number (integer) or a path.

#### String:

A string can be a word or a sentence, in Python a string start and end with apostrophes ('')

```
# Example of a string:
my_string = 'This can be everything'
``` 

#### Number:

An integer is a number:

```
# Example of an integer:
my_integer = 7
``` 

#### Path

A path specifies the directories in which a file, folder, executable,... is located. An example of such a pathname is: "C:/Users/Bob/Desktop/Automagica.pptx".
```
# In a function:
open_file('C:/Users/Bob/Desktop/Automagica.pptx')
``` 

Alternatively you can double every backslash input. The next snippet of code illustrates how to use this method

```
# Pathname:
C:/Users/Bob/Desktop/Automagica.pptx

# As a string:
'C:/Users/Bob/Desktop/Automagica.pptx'

# In a function:
open_file('C:/Users/Bob/Desktop/Automagica.pptx')
``` 

In Windows Explorer, a path can be determined by pressing shift + right click on a file, folder,... A menu pops up, where you can select "copy as path" (see image). 
This copies te path as a string to the clipboard, e.g. "C:\Program Files (x86)\Dropbox\Client\Dropbox.exe". Note that pasting this directly in your code will cause a SyntaxError, to avoid this you can either use forward slashes, add an 'r' added in front of the path the backslashes (to make a raw string) or double the backslashes (escaping) for it to be in correct form for a function input: 
```
r"C:\Program Files (x86)\Dropbox\Client\Dropbox.exe"

"C:/Users/Bob/Desktop/Automagica.pptx"

C:\\Users\\Bob\\Desktop\\Automagica.pptx
```
![Imgur](https://i.imgur.com/9xI2mbk.png?2)


## Browser Automation Example

Out-of-the box Automagica uses Chrome as automated browser. Automating the browser requires you to find the elements to manipulate them.
You could use Automagica to directly automate browser tasks within your Python scripts directly addressing the HTML elements. Another, more intuitive way would be to use Automagica Flow and Automagica Wand, which does not require knowledge of the inner HTML structure of the webpage.


The following sections will explain how to find, read and manipulate those web elements.

### Basic functions

To open a browser choose 'Open Chrome browser' from menu or type the command:
```
browser = Chrome()
```

The browser function will wait until the page has fully loaded (that is, the “onload” event has fired) before continuing in the Automagica script. It’s worth noting that if your page uses a lot of AJAX on load then the browser function may not know when it has completely loaded.

Browse to a website by clicking 'Browse to URL' in the menu or use the command:
```
browser.browse_to('https://mywebsite.com/')
```

Closing the browser can be done by:
```
browser.close()
```

To move backward and forward in your browser’s history:
```
browser.forward()
browser.back()
```

To click on an element:
```
element.click()
```

To enter text into a text field:
```
element.send_keys("some text")
```

To clear an element:
```
element.clear()
```

### Navigating

To navigate and perform actions in the browser it is crucial to locate elements. Elements can be everything in the html files of a website like text, titles, buttons, text fields, tables, etc...

### Quick start

There are two methods to finding elements, *find_element* to find a single element and *find_elements* to find multiple.
Arguably the easiest way to find a certain element is by copying it's XPath.

To do this in Chrome right click on the element you want to find, in the example below this is the "Google Search" button on Google.com. Click *inspect element* and a side tab with the html code opens with the element you selected highlighted in blue.

![Imgur](https://i.imgur.com/A2xdvUP.png)

In the html code, right click the highlighted block and select *Copy* -> *Copy XPath*.

![Imgur](https://i.imgur.com/WRD46Xi.png)

You can now use the absolute XPath to manipulate the element. However this is a fast method for prototyping, we do not recommend using absolute paths in production environments. Slight changes in the html code would cause the absolute path to change and to likely cause errors. A more in-depth overview in the next section.

### Selecting elements

#### Selection by name

Use this when you know name attribute of an element. With this strategy, the first element with the name attribute value matching the location will be returned. If no element has a matching name attribute, a NoSuchElementException will be raised.

For instance, consider these elements on a webpage:

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>

&nbsp;

The corresponding html code would be:

    <html>
     <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="loginbutton" type="submit" value="Login" />
      <input name="clearbutton" type="button" value="Clear" />
      </form>
     </body>
    <html>

The username and password field can be found by:

```
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
```

To fill in the fields:

```
username.send_keys("Automagica_User1")
password.send_keys("thisismypassword123")
```

To find and click on the login button:

```
login = browser.find_element_by_name('loginbutton')
login.click()
```

**Side note**

In case of double naming, finding by name always finds the first element. Imagine the following html code:

    <html>
     <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
      </form>
     </body>
    <html>

The following command will find the first element with the name "continue" and thus selecting the Login button:

```
continue = browser.find_element_by_name('continue')
```

#### Selection by Id

You can select elements by Id when this is known. This is a robust method, yet generally nog every element had a known id tag. Consider the html code below:

    <html>
     <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="continue" type="submit" value="Login" />
      </form>
     </body>
    <html>

In this case the form has an id "loginForm". Hence the form can be selected with the Id by:

```
loginform = browser.find_element_by_id('loginForm')
```

### Selection by Xpath

XPath (XML Path Language) is a query language for selecting nodes from an XML document. Since HTML can be an implementation of XML (referred to as XHTML), this language can be used to find and manipulate target elements in web applications.

The advantage of using XPath is the possibility to reach every element within an HTML structure. See [Quick start](#quick-start) for a visual introduction on how to find and use an element with XPath.
The disadvantage of using a full XPath is that it is not very robust. Even the slightest changes in a HTML page would cause absolute XPaths to change, which in result will likely cause your robot unable to find the correct elements. Note that this is different from using an element name or id, as elements will still be able to be found with changes in the HTML page as long as the name or id remains the same.

Therefore, when working with Xpath the robustness can be increased by finding a nearby element with an id or name attribute (ideally a parent element), so you can locate your target element based on the relationship.

Consider the following structure on a HTML page:

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>

&nbsp;

With the following source code:

    <html>
     <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="loginbutton" type="submit" value="Login" />
      <input name="clearbutton" type="button" value="Clear" />
      </form>
     </body>
    <html>


**Selecting the username:**

1. Absolute path (note that this would break if the HTML was changed only slightly)
2. Point to the first element in the form
3. First input element with attribute named ‘name’ and the value username
```
username = browser.find_element_by_xpath("//form[input/@name='username']")
username = browser.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = browser.find_element_by_xpath("//input[@name='username']")
```

**The "clear" button can be located by:**

1. Fourth input element of the form element with attribute named id and value loginForm
2. Input with attribute named name and the value continue and attribute named type and the value button
```
clear_button = browser.find_element_by_xpath("//form[@id='loginForm']/input[4]")
clear_button = browser.find_element_by_xpath("//input[@name='continue'][@type='button']")
```

**The form can be selected by:**

1. Absolute path (note that this would break if the HTML was changed only slightly):
2. First form element in the HTML
3. The form element with attribute named id and the value loginForm
```
login_form = browser.find_element_by_xpath("/html/body/form[1]")
login_form = browser.find_element_by_xpath("//form[1]")
login_form = browser.find_element_by_xpath("//form[@id='loginForm']")
```

### Browsing Example

The following example browses to Google, searches for Automagica, opens the first Google Search result link

```
# Open Chrome
browser = Chrome()

# Browse to Google
browser.browse_to('https://google.com')

# Enter Search Text
browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('automagica')

# Submit
browser.find_element_by_xpath('//*[@id="lst-ib"]').submit()

# Click the first link
browser.find_elements_by_class_name('r')[0].click()
```

A similar example with Automagica Flow [can be seen in this short YouTube video](https://img.youtube.com/vi/MVBvqlPn518/0.jpg)