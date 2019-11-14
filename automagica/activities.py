import os
import platform
import shutil
from PIL import Image
import uuid
import psutil
from time import sleep
import pyautogui
'''
Delay activities
'''


def Wait(seconds=None):
    '''
    Stall the execution of the preceding functions for a specified number of seconds.
    '''
    sleep(seconds)


'''
Keyboard/mouse activities
'''


def GetMouseCoordinates():
    '''
    Displays a message box with the absolute coordinates of the current position of the mouse.
    '''
    coord = pyautogui.position()
    coordstring = "( " + str(coord[0]) + " , " + str(coord[1]) + " )"
    return DisplayMessageBox(coordstring, "Mouse Position")


def ClickOnPosition(x=None, y=None):
    '''
    Clicks on a pixel position on the visible screen determined by x and y coördinates.
    '''
    return pyautogui.click(x, y)


def DoubleClickOnPosition(x=None, y=None):
    '''
    Double clicks on a pixel position on the visible screen determined by x and y coördinates.
    '''
    return pyautogui.doubleClick(x, y)


def RightClickOnPosition(x=None, y=None):
    '''
    Right clicks on a pixel position on the visible screen determined by x and y coördinates.
    '''
    return pyautogui.rightClick(x, y)


def MoveToPosition(x=None, y=None):
    '''
    Moves te pointer to a x-y position.
    '''
    return pyautogui.moveTo(x, y)


def MoveRelative(x=None, y=None):
    '''
    Moves the mouse an x- and y- distance relative to its current pixel position.
    '''
    return pyautogui.moveRel(x, y)


def DragToPosition(x=None, y=None, button="left"):
    '''
    Drag the mouse from its current position to a entered x-y position, while holding a specified button.
    '''
    return pyautogui.dragTo(x, y, 0.2, button=button)


def ClickOnImage(filename=None, double_click=False, right_click=False):
    from pyautogui import locateCenterOnScreen, rightClick, click

    x, y = locateCenterOnScreen(filename)
    clicks = 2 if double_click else 1
    if right_click:
        return rightClick(x, y)
    else:
        return click(x, y, clicks)

def WaitOnImage(filename=None, timeout=120):
    """
    Waits for an image to appear on the screen
    """
    from pyautogui import locateCenterOnScreen
    from time import sleep

    for _ in range(timeout):
        try:
            locateCenterOnScreen(filename)
            break
        except TypeError:
            sleep(1)

    


def PressKey(key=None):
    '''
    Press and release an entered key.
    '''
    if key:
        return pyautogui.press(key)


def PressHotkey(first_key, second_key, third_key=None):
    '''
    Press a combination of two or three keys simultaneously.
    '''
    if not third_key:
        return pyautogui.hotkey(first_key, second_key)
    if third_key:
        return pyautogui.hotkey(first_key, second_key, third_key)


def Type(text=None, interval_seconds=0.001):
    '''
    Type text in the current active field. The first argument represent the text and is entered as a string. 
    The second variable is the time between two keystrokes. Pay attention that you can only press single 
    character keys. Keys like ":", "F1",... can not be part of the text argument.
    '''
    from pyautogui import typewrite
    # Set keyboard layout for Windows platform
    if platform.system() == 'Windows':
        from win32api import LoadKeyboardLayout
        LoadKeyboardLayout('00000409', 1)
    return typewrite(text, interval=interval_seconds)


def CapsLock():
    '''
    Press the Caps Lock key.
    '''
    return pyautogui.press('capslock')


def NumLock():
    '''
    Press the Num Lock key.
    '''
    return pyautogui.press('numlock')


def Enter():
    '''
    Press the enter key.
    '''
    return pyautogui.press('enter')


def SpaceBar():
    '''
    Press the space bar key.
    '''
    return pyautogui.press('space')


def Backspace():
    '''
    Press the Backspace key.
    '''
    return pyautogui.press('backspace')


def Delete():
    '''
    Press the Delete key.
    '''
    return pyautogui.press('delete')


def Endkey():
    '''
    Press the End key.
    '''
    return pyautogui.press('end')


def Tab():
    '''
    Press the Tab key.
    '''
    return pyautogui.press('tab')


def CreateUniqueKey(length=32):
    '''
    universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems. This key can be 
    considered as unique for there to be a one in a billion chance of duplication, 103 trillion version 4 UUIDs must be generated.
    The general form is e.g. "123e4567-e89b-12d3-a456-426655440000". The argument specifies the length of the returned string.
    If it is omitted, the entire 128-bit UUID is returned as a string.
    '''
    return str(uuid.uuid4())[:length]


def TypeInRunWindow(text=None):
    '''
    Open the "Run" window and type the entered text.
    '''
    if text:
        PressHotkey("win", "r")
        Type(text, 0.08)
        Enter
    return


'''
Monitoring
'''


def CPULoad(measure_time=1):
    '''
    Returns average CPU load for all cores.
    Measures once every second, adjust measure_time (seconds) to get a longer averaged measured time. Standard measure_time is 1 second.
    '''
    cpu_measurements = []
    for x in range(measure_time):
        cpu_measurements.append(psutil.cpu_percent(interval=1))
    return sum(cpu_measurements)/len(cpu_measurements)


def NumberOfCPU(logical=True):
    '''
    Returns the number of CPU's in the current system. 
    The parameter 'logical' determines if only logical units are added to the count, default value is True.
    '''
    return psutil.cpu_count(logical=logical)


def CPUFreq():
    '''
    Returns frequency at which CPU currently operates.
    Also shows minimum and maximum frequency.
    '''
    return psutil.cpu_freq()


def CPUStats():
    '''
    Returns CPU statistics: Number of CTX switches, intterupts, soft-interrupts and systemcalls.
    '''
    return psutil.cpu_stats()


def MemoryStats(mem_type='swap'):
    '''
    Returns memory statistics: total, used, free and percentage in use.
    Choose mem_type = 'virtual' for virtual memory, and mem_type = 'swap' for swap memory (standard).
    '''
    if mem_type == 'virtual':
        return psutil.virtual_memory()
    else:
        return psutil.swap_memory()


def DiskStats():
    '''
    Returns disk statistics of main disk: total, used, free and percentage in use.
    '''
    return psutil.disk_usage('/')


def DiskPartitions():
    '''
    Returns tuple with info for every partition.
    '''
    return psutil.disk_partitions()


def BootTime():
    '''
    Returns time PC was booted in seconds after the epoch.
    '''
    return psutil.boot_time()


def TimeSinceLastBoot():
    '''
    Returns time since last boot in seconds.
    '''
    import time
    return time.time() - psutil.boot_time()


'''
Windows activities
'''


def BeepSound(frequency=1000, duration=250):
    '''
    Makes a beeping sound.
    Choose frequency (Hz) and duration (ms), standard is 1000 Hz and 250 ms.
    '''
    import winsound
    winsound.Beep(frequency, duration)
    return


def UseFailsafe(switch=True):
    from pyautogui import FAILSAFE
    FAILSAFE = switch


def ClearClipboard():
    '''
    Removes everything from the clipboard.
    '''
    from ctypes import windll
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    return


'''
Process activities
'''


def ProcessRunning(name):
    '''
    Checks if given process name (name) is currently running on the system.
    Returns True or False.
    '''
    if name:
        for p in psutil.process_iter():
            if name in p.name():
                return True
    return False


def ListRunningProcesses():
    '''
    Returns a list with all names of unique processes currently running on the system.
    '''
    process_list = []
    for p in psutil.process_iter():
        process_list.append(p.name())
    return set(process_list)


def ChromeRunning():
    '''
    Returns True is Chrome is running.
    '''
    for p in psutil.process_iter():
        if "chrome.exe" in p.name():
            return True
    return False


def WordRunning():
    '''
    Returns True is Word is running.
    '''
    for p in psutil.process_iter():
        if "winword.exe" in p.name().lower():
            return True
    return False


def ExcelRunning():
    '''
    Returns True is Excel is running.
    '''
    for p in psutil.process_iter():
        if "excel.exe" in p.name():
            return True
    return False


def PowerpointRunning():
    '''
    Returns True is Powerpoint is running.
    '''
    for p in psutil.process_iter():
        if "powerpnt.exe" in p.name().lower:
            return True
    return False


def DropboxRunning():
    '''
    Returns True is Dropbox is running.
    '''
    for p in psutil.process_iter():
        if "dropbox.exe" in p.name().lower():
            return True
    return False


def FirefoxRunning():
    '''
    Returns True is Firefox is running.
    '''
    for p in psutil.process_iter():
        if "firefox.exe" in p.name().lower():
            return True
    return False


def TeamviewerRunning():
    '''
    Returns True is Teamviewer is running.
    '''
    for p in psutil.process_iter():
        if "teamviewer.exe" in p.name().lower():
            return True
    return False


def SkypeRunning():
    '''
    Returns True is Skype is running.
    '''
    for p in psutil.process_iter():
        if "skypehost.exe" in p.name().lower():
            return True
    return False


def EdgeRunning():
    '''
    Returns True is Microsoft Edge is running.
    '''
    for p in psutil.process_iter():
        if "microsoftedge.exe" in p.name().lower():
            return True
    return False


def OnedriveRunning():
    '''
    Returns True is Onedrive is running.
    '''
    for p in psutil.process_iter():
        if "onedrive.exe" in p.name().lower():
            return True
    return False


def IllustratorRunning():
    '''
    Returns True is Illustrator is running.
    '''
    for p in psutil.process_iter():
        if "illustrator.exe" in p.name().lower():
            return True
    return False


def LaunchProcess(process_executable=None):
    from subprocess import Popen

    return Popen(process_executable)


def OpenProgramByName(name, main_drive="C:\\"):
    from subprocess import Popen

    if not name[-4:] == ".exe":
        name = name + ".exe"
    for root, dirs, files in os.walk(main_drive):
        for file in files:
            if file == name and file.endswith(".exe"):
                Popen(os.path.join(root, file))
                return


def KillProcess(process=None, name=None):
    if process:
        return process.kill()
    if name:
        return os.system("taskkill /f /im " + name + " >nul 2>&1")
    return


'''
Browser activities
'''


def ChromeBrowser(ignore_images=False, headless=False):
    '''

    Opens the Chrome Browser in a Selenium instance.

    Args:
        ignore_images (bool): do not load images
        headless (bool): run without a window

    Returns:
        webdriver: Selenium Webdriver

    Example:
        browser = ChromeBrowser(ignore_iamges=True)
        browser.get('https://automagica.io')

    '''
    if platform.system() == 'Linux':
        chromedriver_path = '\\bin\\webdriver\\linux64\\chromedriver'
    elif platform.system() == 'Windows':
        chromedriver_path = '\\bin\\win32\\chromedriver.exe'
    else:
        chromedriver_path = '\\bin\\mac64\\chromedriver.exe'

    from selenium.webdriver import Chrome, ChromeOptions

    chrome_options = ChromeOptions()

    if headless:
        chrome_options.add_argument("--headless")

    if ignore_images:
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

    return Chrome(os.path.abspath(__file__).replace('activities.py', '') + chromedriver_path, chrome_options=chrome_options)


def GetGoogleSearchLinks(search_text):
    '''
    Return a list with the links on the first page of google when searching for the entered text.
    This text needs to be entered as a string.
    '''
    import urllib
    import requests
    from bs4 import BeautifulSoup
    r = requests.get('https://www.google.com/search?&q=' +
                     urllib.parse.quote_plus(search_text))
    soup = BeautifulSoup(r.content, "html.parser")
    links = []
    for block in soup.findAll('h3', {'class': 'r'}):
        link = block.a.get('href').split("?q=")[1].split("&sa=U")[0]
        if 'https' in link:
            links.append(link)
    return links


''' 
OCR activities 
'''


def ExtractTextFromImage(filename=None):
    import pytesseract
    if platform.system() == 'Windows':
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
    from pytesseract import image_to_string
    return image_to_string(Image.open(filename))


'''
Excel activities
'''

from openpyxl import load_workbook, Workbook

# Renaming functions
OpenExcelWorkbook = load_workbook

# Renaming classes
NewExcelWorkbook = Workbook


def ExcelCreateWorkbook(path):
    '''
    Create a new .xlsx file and save it under a specified path. If the entered path already
    exists, the function does nothing.
    '''
    if not os.path.exists(path):
        Workbook().save(path)
    return


def ExcelOpenWorkbook(path):
    '''
    Open a .xlsx file with Microsoft Excel. Make sure you enter a valid path. This can be a path
    referencing an existing .xlsx file e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx". 
    This will open the existing file. You can also enter a comletely new path. In this case, the 
    function creates a new .xlsx file with that path and opens it with Excel.
    '''
    if os.path.exists(path):
        os.startfile(path)
    elif not os.path.exists(path):
        ExcelCreateWorkbook(path)
        os.startfile(path)
    return


def ExcelSaveExistingWorkbook(path, new_path=None):
    '''
    Save (as) an existing .xlsx file. The second variable is the new path the file needs to be saved
    at. You can ignore this variable if you just want to save the file and do not want to "save as".
    For the function to work properly, it is important that the file you want to save is not opened.
    '''
    workbook = load_workbook(path)
    if not new_path:
        workbook.save(path)
    elif not os.path.isfile(new_path):
        workbook.save(new_path)
    return


def ExcelCreateWorkSheet(path, sheet_name=None):
    '''
    Create a new worksheet with a specified name in an existing workbook specified by the path variable. If
    no sheet_name is entered, the new sheet is named "sheet1", "sheet2", "sheet3", ..., depending on the sheets
    that already exist.
    Make shure you enter a valid path referencing a .xlsx file e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
    For the function to work properly, it is important that the .xlsx file is closed during the execution.
    '''
    workbook = load_workbook(path)
    if sheet_name and sheet_name not in workbook.get_sheet_names():
        workbook.create_sheet(title=sheet_name)
    elif not sheet_name:
        workbook.create_sheet()
    workbook.save(path)
    return


def ExcelGetSheets(path):
    '''
    Return a list containing the sheet names of an Excel file. Make shure you enter a valid path 
    referencing a .xlsx file e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
    '''
    workbook = load_workbook(path)
    return workbook.get_sheet_names()


def ExcelReadCell(path, cell="A1", sheet=None):
    '''
    Read a cell from an Excel file and return its value.
    Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
    The cell you want to read needs to be defined by a cell name e.g. "A2". The third variable 
    is a string with the name of the sheet that needs to be read. If omitted, the 
    function reads the entered cell of the active sheet.
    '''
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook.get_sheet_by_name(sheet)
    else:
        worksheet = workbook.active

    return worksheet[cell].value


def ExcelReadRowCol(path, r=1, c=1, sheet=None):
    '''
    Read a Cell from an Excel file and return its value.
    Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
    The cell you want to read needs to be row and a column. E.g. r = 2 and c = 3 refers to cell C3. 
    The third variable needs to be a string with the name of the sheet that needs to be read. 
    If omitted, the function reads the entered cell of the active sheet. First row is defined 
    row number 1 and first column is defined column number 1.
    '''
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook.get_sheet_by_name(sheet)
    else:
        worksheet = workbook.active

    return worksheet.cell(row=r, column=c).value


def ExcelWriteRowCol(path, sheet=None, r=1, c=1, write_value='Value'):
    '''
    Write a value to a Cell to an Excel file.
    Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx"...
    The cell should be defined by a row and a column. E.g. row=4, column=8.
    First row is defined row number 1 and first column is defined column number 1...
    Value can be anything, standard is "Value".
    When executing the code, make sure .xlsx file you want to write is closed.
    '''
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook.get_sheet_by_name(sheet)
    else:
        worksheet = workbook.active
    worksheet.cell(row=r, column=c).value = write_value
    workbook.save(path)
    return


def ExcelWriteCell(path, sheet=None, cell="A1", write_value='Value'):
    '''
    Write a Cell to an Excel file.
    Make sure you enter a valid path e.g. "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx"...
    The cell should be defined by a cell name. E.g. "B6".
    Value can be anything, standard is "Value".
    When executing the code, make sure .xlsx file you want to write is closed.
    '''
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook.get_sheet_by_name(sheet)
    else:
        worksheet = workbook.active

    worksheet[cell] = write_value
    workbook.save(path)
    return


def ExcelPutRowInList(path, start_cell, end_cell, sheet=None):
    '''
    Put the elements of a specified row in a list. The .xlsx file and sheet that needs to be read are 
    specified by respectively the path- and sheet variable. If no sheet is specified, the sheet-variable 
    is set to the current active sheet. Also make shure to enter a valid path e.g. 
    "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
    The row is specified by strings referring to the first and final cell. E.g. start_cell = "B3"
    and end_cell = "E3" will put all the elements of the third row from cell "B3" to cell "E3" in 
    a list: ["B3", "C3", "D3", "E3"]. For the function to work, the two cells need to be of the same row and start_cell needs to be
    the cell at the left hand side.  
    '''
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook.get_sheet_by_name(sheet)
    else:
        worksheet = workbook.active

    values = []
    for rowobj in worksheet[start_cell:end_cell][0]:
        values.append(rowobj.value)

    return values


def ExcelPutColumnInList(path, start_cell, end_cell, sheet=None):
    '''
    Put the elements of a specified column in a list. The .xlsx file and sheet that needs to be read are 
    specified by respectively the path- and sheet variable. If no sheet is specified, the sheet-variable 
    is set to the current active sheet. Also make shure to enter a valid path e.g. 
    "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
    The column is specified by strings referring to the first and final cell. E.g. start_cell = "E3"
    and end_cell = "E6" will put all the elements of the fifth column from cell "E3" to cell "E6" in 
    a list: ["E3", "E4", "E5", "E6]. For the function to work, the two cells need to be of the same 
    column and start_cell needs to be the upper cell.  
    '''
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook.get_sheet_by_name(sheet)
    else:
        worksheet = workbook.active

    values = []
    for colobj in worksheet[start_cell:end_cell]:
        values.append(colobj[0].value)

    return values


def ExcelPutSelectionInMatrix(path, upper_left_cell, bottom_right_cell, sheet=None):
    '''
    Put the elements of a specified selection in a matrix. The .xlsx file and sheet that needs to be read are 
    specified by respectively the path- and sheet variable. If no sheet is specified, the sheet-variable 
    is set to the current active sheet. Also make shure to enter a valid path e.g. 
    "C:\\Users\\Bob\\Desktop\\RPA Examples\\data.xlsx".
    The selection is specified by strings referring to the upper left and bottom right cell. 
    E.g. upper_left_cell = "B2" and bottom_right_cell = "C3" will return a matrix with values: 
    [["B2", "C2"], ["B3", "C3"]]. If a cell is empty, its value is set to "None".
    '''
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook.get_sheet_by_name(sheet)
    else:
        worksheet = workbook.active

    matrix = []
    for rowobj in worksheet[upper_left_cell:bottom_right_cell]:
        next_row = []
        for cellobj in rowobj:
            next_row.append(cellobj.value)
        matrix.append(next_row)

    return matrix


'''
Word activities
'''


def OpenWordDocument(filename=None):
    from docx import Document
    return Document(filename)


def ReplaceText(document, text=None, replace_with=None):
    for paragraph in document.paragraphs:
        paragraph.text = paragraph.text.replace(text, replace_with)
    return document


def ConvertWordToPDF(word_filename=None, pdf_filename=None):
    if platform.system() == 'Windows':
        from win32com import client
        word = client.DispatchEx('Word.Application')
        word_document = word.Documents.Open(word_filename)
        word_document.SaveAs(pdf_filename, FileFormat=17)
        word_document.Close()
        word.Quit()
    else:
        print('Not implemented for other platforms than Windows.')


'''
PDF Activities
'''

import PyPDF2


def MergePDF(pdf1, pdf2, merged_path):
    '''
    The first two arguments are the PDF's that need to be merged, entered as a path. The pages from pdf2 
    will be added to pdf2. The merged PDF receives a new path specefied by the third argument.
    '''
    from PyPDF2 import PdfFileMerger

    pdfs = [str(pdf1), str(pdf2)]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(merged_path)
    return


def ExtractTextFromPDFPage(path, page=1):
    '''
    This function extracts all the text from a given page and returns it as a string. The pdf needs to be
    entered as a path. Pay attention that the entered page needs to be greater than 0.
    '''
    if os.path.isfile(path) and page > 0:
        pdfFile = open(path, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        if page <= pdfReader.numPages:
            pdfPage = pdfReader.getPage(page-1)
        else:
            pdfPage = pdfReader.getPage(pdfReader.numPages - 1)
        return pdfPage.extractText()


'''
Message boxes
'''


def DisplayMessageBox(body, title="Message", type="info"):
    '''
    Shows a pop-up message with title and body. Three possible types, info, error and warning with the default value info.
    '''
    import tkinter
    from tkinter import messagebox

    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    if not body:
        messagebox.showwarning("Warning", "No input for message box")

    if type == "error":
        messagebox.showwarning(title, body)
    if type == "warning":
        messagebox.showwarning(title, body)
    if type == "info":
        messagebox.showinfo(title, body)
    return


def RequestUserInput():
    '''
    Shows a pop-up message which asks for input which is captured and returned.
    '''
    from tkinter import Tk
    from tkinter.simpledialog import askstring

    root = Tk()
    root.withdraw()  # hide main window

    text = askstring("Input", "Give input:")
    return text


def StartFile(path):
    from os import startfile
    startfile(path)
    return


'''
File Operations
'''


def OpenFile(path):
    '''
    Entering "C:\\Users\\Downloads\\Automagica.docx" as pathname will open the .docx-file "Automagica.docx". 
    '''
    if os.path.isfile(path):
        os.startfile(path)
    return


def RenameFile(old_path, new_file_name):
    '''
    Entering "C:\\Users\\Documents\\Automagica.docx" as "old_path" and "Automagica123.docx" as new_file_name changes
    the name of the directory in C:\\Users\\Documents from Automagica to Automagica123. The function will not
    rename a file if a file with the desired name already exists in the folder.
    '''
    if os.path.isfile(old_path):
        base_path = old_path.split("\\")[:-1]
        new_path = "\\".join(base_path)+"\\" + new_file_name
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
    return


def MoveFile(old_path, new_location):
    '''
    Entering "C:\\Users\\Documents\\Automagica.docx" as old_path and "C:\\Users\\Downloads"
    as new_location moves the file Automagica.docx from directory "Documents" to directory "Downloads".
    If the new location already contains a file with the same name, a random 8 character uid will be added 
    in front of the name before the file is moved.
    '''
    import uuid
    name = old_path.split("\\")[-1]
    new_path = new_location + "\\" + name
    if os.path.exists(old_path):
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
        elif os.path.exists(new_path):
            new_path = new_location + "\\" + \
                "(" + str(uuid.uuid4())[:8] + ") " + name
            os.rename(old_path, new_path)
    return


def RemoveFile(path):
    '''
    Entering "C:\\Users\\Downloads\\Automagica.xlsx" will delete the file named "Automagica.xlsx" at the location specified by
    the given path.
    '''
    if os.path.isfile(path):
        os.remove(path)
    return


def FileExists(path):
    '''
    This function checks whether the file with the given path exists, e.g. by entering
    "C:\\Users\\Documents\\Automagica.docx", the function returns True if the file exists or False
    if it doesn't exist.
    '''
    return os.path.isfile(path)


def CopyFile(old_path, new_path):
    '''
    By entering "C:\\Users\\Documents\\Automagica.docx" as old_path and "C:\\Users\\Downloads" as new_location...
    the function copies the file "Automagica.docx" to the new location. If the new location already contains a file
    with the same name, the copy will replace this file.
    '''
    from shutil import copyfile
    copyfile(old_path, new_path)


def WaitForFile(path):
    '''
    Wait until a file with the entered path exists.
    '''
    from time import sleep
    while not os.path.exists(path):
        sleep(1)
    return


def WriteListToFile(list_to_write, file):
    '''
    Writes a list to a .txt file. Every element of the entered list is written on a new
    line of the text file. The .txt file is entered with a path. If the path does not exist
    yet, the function will create a new .txt file at the specified path and write it. If the 
    path does exist, the function writes the list in the existing file.
    '''
    with open(file, 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in list_to_write)
    return


def WriteFileToList(file):
    '''
    This function writes the content of a entered .txt file to a list and returns that list. 
    Every new line from the .txt file becomes a new element of the list. The function will 
    not work if the entered path is not attached to a .txt file.
    '''
    written_list = []
    with open(file, 'r') as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            current_place = line[:-1]
            written_list.append(current_place)
    return written_list


'''
Folder Operations
'''


def CreateFolder(path):
    '''
    Creates new folder at the given path
    '''
    if not os.path.exists(path):
        os.makedirs(path)
    return


def RenameFolder(old_path, new_folder_name):
    '''
    Entering "C:\\Users\\OldFolder as old_path" and "NewFolder" as new_folder_name changes
    the name of the directory in C:\\Users from "OldFolder" to "NewFolder".
    '''
    if os.path.exists(old_path):
        base_path = old_path.split("\\")[:-1]
        new_path = "\\".join(base_path)+"\\" + new_folder_name
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
    return


def OpenFolder(path):
    '''
    Entering "C:\\Users\\Downloads\\Automagica" will open the folder "Automagica" if the path exists.
    '''
    if os.path.isdir(path):
        os.startfile(path)
    return


def MoveFolder(old_path, new_location):
    '''
    Entering "C:\\Users\\Oldlocation\\Automagica" as old_path and "C:\\Users\\Newlocation"
    as new_location moves the folder "Automagica" from directory "Oldlocation" to directory "Newlocation".
    If the new location already contains a folder with the same name, a random 8 character uid is added to the name.
    '''
    import uuid
    name = old_path.split("\\")[-1]
    new_path = new_location + "\\" + name
    if os.path.isdir(old_path):
        if not os.path.isdir(new_path):
            os.rename(old_path, new_path)
        elif os.path.isdir(new_path):
            new_path = new_path + " (" + str(uuid.uuid4())[:8] + ")"
            os.rename(old_path, new_path)
    return


def RemoveFolder(path, allow_root=False, delete_read_only=True):
    '''
    Entering "C:\\Users\\Documents\\Automagica" removes the folder "Automagica" including all of its subdirectories and files.
    Standard, the safety variable allow_root is False. When False the function checks whether the path lenght has a minimum of 10 characters. 
    This is to prevent entering for example "\\" as a path resulting in deleting the root and all of its subdirectories.
    To turn off this safety check, explicitly set allow_root to True. For the function to work optimal, all files present in the
    directory must be closed.
    '''
    if len(path) > 10 or allow_root:
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=delete_read_only)
    return


def EmptyFolder(path, allow_root=False):
    '''
    Entering "C:\\Users\\Documents\\Automagica" removes all the files and folders saved in the "Automagica" folder but maintains the folder itself.
    Standard, the safety variable allow_root is False. When False the function checks whether the path lenght has a minimum of 10 characters. 
    This is to prevent entering for example "\\" as a path resulting in deleting the root and all of its subdirectories.
    To turn off this safety check, explicitly set allow_root to True. For the function to work optimal, all files present in the directory
    must be closed.
    '''
    if len(path) > 10 or allow_root:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
    return


def FolderExists(path):
    '''
    This function checks whether the folder with the given path exists, e.g. by entering...
    "C:\\Users\\Documents\\Automagica", the function returns True if the folder exists or False if 
    it doesn't exist.
    '''
    return os.path.isdir(path)


def CopyFolder(old_path, new_location):
    '''
    By entering "C:\\Users\\Documents\\Automagica" as old_path and "C:\\Users\\Downloads" as new_location...
    the function copies the folder "Automagica" together with all its contents to the new location. The folder name...
    remains unchanged, except when the folder already exists a 8 character random uid will be added to the name.
    '''
    import uuid
    new_path = new_location + "\\" + old_path.split("\\")[-1]
    if os.path.isdir(old_path):
        if not os.path.isdir(new_path):
            shutil.copytree(old_path, new_path)
        elif os.path.isdir(new_path):
            if os.path.isdir(new_path):
                new_path = new_path + " (" + str(uuid.uuid4())[:8] + ")"
            shutil.copytree(old_path, new_path)
    return


def ZipFolder(dir_path, new_path):
    '''
    Creates a zipped directory of a directory specified by the first argument. The newly zipped directory 
    receives a path specified by the second argument.
    '''
    if os.path.isdir(dir_path):
        shutil.make_archive(new_path, 'zip', dir_path)
    return


def UnzipFolder(path, new_path=False):
    '''
    Unzips a folder specified by the first variable. The unzipped folder will be stored in a directory specified by
    new_path. If this second variable is omitted, the unzipped folder will be stored in the same directory as the 
    zipped folder is located. 
    '''
    import zipfile
    if os.path.exists(path):
        zipp = zipfile.ZipFile(path)
        if not new_path:
            base_path = "\\".join(path.split("\\")[:-1])
            zipp.extractall(base_path)
        elif os.path.isdir(new_path):
            zipp.extractall(new_path)
        zipp.close()
    return


def WaitForFolder(path):
    '''
    Wait until a folder with the entered path exists.
    '''
    from time import sleep
    while not os.path.exists(path):
        sleep(1)
    return


'''
Image Operations
'''

import sys
from PIL import Image
import PIL


def OpenImage(path):
    '''
    Displays an image specified by the path variable on the default imaging program.
    '''
    im = Image.open(path)
    return im.show()


def RotateImage(path, angle):
    '''
    Entering "C:\\Users\\Pictures\\Automagica.jpg" as path and an a angle of 90 rotates the picture specified by the first
    argument over 90 degrees. Pay attention, because angles other than 90, 180, 270, 360 can resize the picture. 
    '''
    im = Image.open(path)
    return im.rotate(angle, expand=True).save(path)


def ResizeImage(path, size):
    '''
    Resizes the image specified by the path variable. The size is specifie by the second argument. This is a tuple with the
    width and height in pixels. E.g. ResizeImage("C:\\Users\\Pictures\\Automagica.jpg", (300, 400)) gives the image a width
    of 300 pixels and a height of 400 pixels.
    '''
    im = Image.open(path)
    return im.resize(size).save(path)


def ImageSize(path):
    '''
    Returns the size in pixels of an image specified by a path. The size is returned in a message box
    of the form: "(height, width)"
    '''

    im = Image.open(path)
    return DisplayMessageBox(str(im.size))


def CropImage(path, box=None):
    '''
    Crops the image specified by path to a region determined by the box variable. This variable is a 4 tuple who defines the
    left, upper, right and lower pixel coördinate e.g.: (left, upper, right, lower).
    '''
    im = Image.open(path)
    return im.crop(box).save(path)


def ImageFormat(path):
    '''
    Returns the format of an image specified by the input path. E.g. entering "C:\\Users\\Pictures\\Automagica.jpg"
    returns a message box saying JPEG.
    '''
    im = Image.open(path)
    return DisplayMessageBox(im.format)


def MirrorImageHorizontally(path):
    '''
    Mirrors an image with a given path from left to right.
    '''
    im = Image.open(path)
    return im.transpose(Image.FLIP_LEFT_RIGHT).save(path)


def MirrorImageVertically(path):
    '''
    Mirrors an image with a given path from top to bottom.
    '''
    im = Image.open(path)
    return im.transpose(Image.FLIP_TOP_BOTTOM).save(path)


'''
Email Operations
'''

import smtplib


def SendMail(host, user, password, destination, subject="", message="", port=587):
    '''
    This function lets you send emails with an e-mail address. The first and second arguments require the
    mail address and password of your e-mail account. The destination is the receiving mail address. The subject
    and message variables contain respectively the mail subject and the text in the mail. The port variable is standard
    587. In most cases this argument can be ignored, but in some cases it needs to be changed to 465.
    '''
    BODY = '\r\n'.join(['To: %s' % destination, 'From: %s' %
                        user, 'Subject: %s' % subject, '', message])
    smtpObj = smtplib.SMTP(host, port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(user, password)
    smtpObj.sendmail(user, destination, BODY)
    smtpObj.quit()
    return


def SendMailWithHotmail(user, password, destination, subject="", message="", port=587):
    '''
    This function lets you send emails with a hotmail address. The first and second arguments require the
    mail address and password of your hotmail account. The destination is the receiving mail address. The subject
    and message variables contain respectively the mail subject and the text in the mail. The port variable is standard
    587. In most cases this argument can be ignored, but in some cases it needs to be changed to 465.
    '''
    SendMail('smtp-mail.outlook.com', user, password,
             destination, subject, message, port)
    return


def SendMailWithGmail(user, password, destination, subject="", message="", port=587):
    '''
    This function lets you send emails with a gmail address. The first and second arguments require the
    mail address and password of your gmail account. The destination is the receiving mail address. The subject
    and message variables contain respectively the mail subject and the text in the mail. The port variable is standard
    587. In most cases this argument can be ignored, but in some cases it needs to be changed to 465. Google has a 
    safety feature that blocks lessecure apps. For this function to work properly, this needs to be turned off, which
    can be done at the following link: https://myaccount.google.com/lesssecureapps. 
    '''
    SendMail('smtp.gmail.com', user, password,
             destination, subject, message, port)
    return


def SendMailWithYahoo(user, password, destination, subject="", message="", port=587):
    '''
    This function lets you send emails with a Yahoo address. The first and second arguments require the
    mail address and password of your Yahoo account. The destination is the receiving mail address. The subject
    and message variables contain respectively the mail subject and the text in the mail. The port variable is standard
    587. In most cases this argument can be ignored, but in some cases it needs to be changed to 465.
    '''
    SendMail('smtp.mail.yahoo.com', user, password,
             destination, subject, message, port)
    return


'''
Windows Applications
'''

import subprocess


def OpenCalculator():
    '''
    Open Calculator.
    '''
    subprocess.Popen("calc.exe")
    return


def OpenPaint():
    '''
    Open MS Paint.
    '''
    subprocess.Popen("mspaint.exe")
    return


def OpenNotepad():
    '''
    Open Notepad
    '''
    subprocess.Popen("notepad.exe")
    return


def OpenSnippingTool():
    '''
    Open Snipping Tool.
    '''
    subprocess.Popen("SnippingTool.exe")
    return


def OpenControlPanel():
    '''
    Open Windows Control Panel.
    '''
    subprocess.Popen("control.exe")
    return


def OpenCleanManager():
    '''
    Open Clean Manager.
    '''
    subprocess.Popen("cleanmgr.exe")
    return


def OpenDialer():
    '''
    Open Windows Dialer.
    '''
    subprocess.Popen("dialer.exe")
    return


def OpenVolumeMixer():
    '''
    Open Windows Volume Mixer.
    '''
    subprocess.Popen("SndVol.exe")
    return


def OpenXPSViewer():
    '''
    Open Windows XPS Viewer.
    '''
    subprocess.Popen("xpsrchvw")
    return


'''
Portal (premium) activities
'''

def InsertReportTableHeader(data):
    """
    Inserts the header of an Automagica Report.
    """
    data_keys = []

    for row in data:
        for key, _ in row.items():
            if key not in data_keys:
                data_keys.append(key)

    header = '|'.join(data_keys)

    header_next = '|'.join(['---' for key in data_keys])
    
    print('AUTOMAGICA_MARKDOWN_START: ' + str(header) + ' :AUTOMAGICA_MARKDOWN_END')
    print('AUTOMAGICA_MARKDOWN_START: ' + str(header_next) + ' :AUTOMAGICA_MARKDOWN_END')

    return data_keys


def InsertReportTableItem(item, keys):
    """
    Inserts the header of an Automagica Report.
    """
    print('AUTOMAGICA_MARKDOWN_START: ' + '|'.join([str(item.get(key, '')) for key in keys]) + ' :AUTOMAGICA_MARKDOWN_END')

 
def InsertReportTable(data):
    '''
    Function to report in the Automagica Portal. Can be used to generate reports, 
    logs and worklists. Only available to users with access to the Portal. 
    This outputs a list of flat dicts to a markdown table with headers to the console.
    '''
    keys = InsertReportTableHeader(data)

    for item in data:
        InsertReportTableItem(item, keys)


def InsertReportTitle(title='My title', level=1):
    '''
    Function to insert a report title in the Automagica Portal.
    This outputs a string as a title to the console.
    '''
    print('AUTOMAGICA_MARKDOWN_START: ' + '#' * level + ' :AUTOMAGICA_MARKDOWN_END')


'''
Trello activities
'''


def MakeTrelloCard(title='My card',
                   description='My description',
                   board_name='My board',
                   list_name='My list',
                   api_key='',
                   api_secret='',
                   token='',
                   token_secret='any'):
    """
    For this you need a Trello API key, secret and token. 
    Token secret can be any string, but should be altered for security purposes.
    """
    from trello import TrelloClient

    client = TrelloClient(
        api_key=api_key,
        api_secret=api_secret,
        token=token,
        token_secret=token_secret
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
