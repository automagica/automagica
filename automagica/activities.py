import os
import platform

from PIL import Image

'''
Delay activities
'''
from time import sleep


def Wait(seconds=None):
    sleep(seconds)


'''
Keyboard/mouse activities
'''
# Renaming functions
from pyautogui import hotkey
PressHotkey = hotkey


def ClickOnPosition(x=None, y=None):
    from pyautogui import click

    return click(x, y)


def ClickOnImage(filename=None, double_click=False, right_click=False):
    from pyautogui import locateCenterOnScreen, rightClick, click

    x, y = locateCenterOnScreen(filename)
    clicks = 2 if double_click else 1
    if right_click:
        return rightClick(x, y)
    else:
        return click(x, y, clicks)


def Type(text=None, interval_seconds=0.001):
    from pyautogui import typewrite

    # Set keyboard layout for Windows platform
    if platform.system() == 'Windows':
        from win32api import LoadKeyboardLayout
        LoadKeyboardLayout('00000409', 1)
    return typewrite(text, interval=interval_seconds)


'''
Windows activities
'''


def UseFailsafe(switch=True):
    from pyautogui import FAILSAFE
    FAILSAFE = switch


'''
Process activities
'''


def LaunchProcess(process_executable=None):
    from subprocess import Popen

    return Popen(process_executable)


def KillProcess(process=None):
    return process.kill()


'''
Browser activities
'''


def ChromeBrowser():
    if platform.system() == 'Linux':
        chromedriver_path = '\\bin\\webdriver\\linux64\\chromedriver'
    elif platform.system() == 'Windows':
        chromedriver_path = '\\bin\\win32\\chromedriver.exe'
    else:
        chromedriver_path = '\\bin\\mac64\\chromedriver.exe'
    from selenium.webdriver import Chrome
    return Chrome(os.path.abspath(__file__).replace('activities.py', '') + chromedriver_path)


''' 
OCR activities 
'''


def ExtractTextFromImage(filename=None):
    if platform.system == 'Windows':
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


def ExcelReadCell(path, row, col, cell=None):
    """Read a Cell from an Excel file.
    Make sure you enter a valid path e.g. C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx...
    You can either enter a row and a cell e.g. row = 1, cell = 1 or define a cell name e.g. cell="A2"... 
    First row is defined row number 1 and first column is defined column number 1
    """
    from openpyxl import load_workbook, Workbook
    workbook = load_workbook(path)
    worksheet = workbook.active
    if cell:
        return worksheet[cell].value
    else:
        return worksheet[row-1][col-1].value


def ExcelWriteCell(path, sheet=None, row=1, col=1, cell=None, write_value='Value'):
    """Write a Cell to an Excel file.
    Make sure you enter a valid path e.g. C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx...
    You can either enter a row and a cell e.g. row = 1, cell = 1 or define a cell name e.g. cell="A2"... 
    First row is defined row number 1 and first column is defined column number 1...
    Value can be anything, standard is "Value"
    """
    from openpyxl import load_workbook, Workbook
    workbook = load_workbook(path)
    if sheet:
        worksheet = workbook[sheet]
    else:
        worksheet = workbook.active

    worksheet.cell(row=row, column=col, value=write_value)
    workbook.save(path)
    return


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
    if platform.system == 'Windows':
        from win32com import client
        word = client.DispatchEx('Word.Application')
        word_document = word.Documents.Open(word_filename)
        word_document.SaveAs(pdf_filename, FileFormat=17)
        word_document.Close()
    else:
        print('Not implemented for other platforms than Windows.')

'''
Message boxes
'''

def DisplayMessageBox(body, title="Message", type="info"):
    '''
    Shows an pop-up message with title and body. Three possible types, info, error and warning with the default value info.
    '''
    import tkinter
    from tkinter import messagebox

    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    
    if not body:
         messagebox.showwarning("Warning","No input for message box")
      
    if type == "error":
        messagebox.showwarning(title,body)
    if type == "warning":
        messagebox.showwarning(title,body)
    if type == "info":
        messagebox.showinfo(title,body)
    return

def RequestUserInput():
    '''
    Shows a pop-up message which askes for input which is captured and returned.
    '''
    from tkinter import Tk
    from tkinter.simpledialog import askstring

    root = Tk()
    root.withdraw() # hide main window

    text = askstring("Input", "Give input:")
    return text

def StartFile(path):
    from os import startfile
    os.startfile(path)
    return
