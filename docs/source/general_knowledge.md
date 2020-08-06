# General knowledge

This section contains some general tips & tricks to help you building your first automation with Automagica.

## Variables

Most Automagica activities include parameters. Some are required and some are optional for more flexibility and advanced usage. The chapter 'Activities' contains a list of all the activities and their possible parameters. 

In general a parameter can be a word (string), a number (integer) or a path (raw string).

### String:

A string can be a word or a sentence, in Python a string starts and ends with apostrophes ('')

```
# Example of a string:
my_string = 'This can be everything'
``` 

### Number:

An integer is a number:

```
# Example of an integer:
my_integer = 7
``` 

### Path

A path specifies the directories in which a file, folder, executable,... is located. An example of such a pathname is: "C:\\Users\\Bob\\Desktop\\Automagica.pptx". A pathname needs to be a (raw) string when entered in a function, you can achieve this by adding an 'r' in front of your path. 
```
# Pathname:
C:\Users\Bob\Desktop\Automagica.pptx

# As a string:
r'C:\Users\\Bob\Desktop\Automagica.pptx'

# In a function:
open_file('C:\\Users\\Bob\\Desktop\\Automagica.pptx')
``` 

Alternatively you can double every backslash input. The next snippet of code illustrates how to use this method

```
# Pathname:
C:\Users\Bob\Desktop\Automagica.pptx

# As a string:
'C:\\Users\\Bob\\Desktop\\Automagica.pptx'

# In a function:
open_file('C:\\Users\\Bob\\Desktop\\Automagica.pptx')
``` 

In Windows Explorer, a path can be determined by pressing shift + right click on a file, folder,... A menu pops up, where you can select "copy as path" (see image). This copies te path as a string to the clipboard, e.g. "C:\Program Files (x86)\Dropbox\Client\Dropbox.exe". This path still needs an 'r' added in front or all its backslashes doubled for it to be in correct form for a function input: r"C:\Program Files (x86)\Dropbox\Client\Dropbox.exe" or "C:\\\Program Files (x86)\\\Dropbox\\\Client\\\Dropbox.exe".

![Imgur](https://i.imgur.com/9xI2mbk.png?2)


# Browser Automation

Out-of-the box Automagica uses Chrome as automated browser. Automating the browser requires you to find the elements to manipulate them.
The following sections will explain how to find, read and manipulate those web elements.

## Basic functions

To open a browser choose 'Open Chrome browser' from menu or type the command:
```
browser = Chrome()
```

The browser function will wait until the page has fully loaded (that is, the “onload” event has fired) before continuing in the Automagica script. It’s worth noting that if your page uses a lot of AJAX on load then the browser function may not know when it has completely loaded.

Browse to a website by clicking 'Browse to URL' in the menu or use the command:
```
browser.get('https://mywebsite.com/')
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


An optional check to see if you are on the correct website is to check the title. For example if you are surfing to https://www.google.com, you might want to check if "Google" is in the title to make sure the bot surfed to the correct page.
```
browser = Chrome()
browser.get('https://google.com/')
if not "Google" in browser.title:
    errorbox("Site is not correct")
```

## Navigating

To navigate and perform actions in the browser it is crucial to locate elements. Elements can be everything in the html files of a website like text, titles, buttons, text fields, tables, etc...

## Quick start

There are two methods to finding elements, *find_element* to find a single element and *find_elements* to find multiple.
Arguably the easiest way to find a certain element is by copying it's XPath.

To do this in Chrome right click on the element you want to find, in the example below this is the "Google Search" button on Google.com. Click *inspect element* and a side tab with the html code opens with the element you selected highlighted in blue.

![Imgur](https://i.imgur.com/A2xdvUP.png)

In the html code, right click the highlighted block and select *Copy* -> *Copy XPath*.

![Imgur](https://i.imgur.com/WRD46Xi.png)

You can now use the absolute XPath to manipulate the element. However this is a fast method for prototyping, we do not recommend using absolute paths in production environments. Slight changes in the html code would cause the absolute path to change and to likely cause errors. A more in-depth overview in the next section.

## Selecting elements

### Selection by name

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

### Selection by Id

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

## Selection by Xpath

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

## Browsing Example

The following example browses to Google, searches for Automagica, opens the first Google Search result link

```
# Open Chrome
browser = Chrome()

# Browse to Google
browser.get('https://google.com')

# Enter Search Text
browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys('automagica')

# Submit
browser.find_element_by_xpath('//*[@id="lst-ib"]').submit()

# Click the first link
browser.find_elements_by_class_name('r')[0].click()
```

