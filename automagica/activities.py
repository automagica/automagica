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
import pyautogui

# Renaming functions
PressHotkey = pyautogui.hotkey

def ClickOnPosition(x=None, y=None):
    return pyautogui.click(x, y)


def ClickOnImage(filename=None, double_click=False, right_click=False):
    x, y = pyautogui.locateCenterOnScreen(filename)
    clicks = 2 if double_click else 1
    if right_click:
        return pyautogui.rightClick(x, y)
    else:
        return pyautogui.click(x, y, clicks)

def Type(text=None, interval_seconds=None):
    return pyautogui.typewrite(text, interval=interval_seconds)


'''
Windows activities
'''
import pywinauto

def UseFailsafe(switch=True):
    pyautogui.FAILSAFE = switch


'''
Process activities
'''
import subprocess

def LaunchProcess(process_executable=None):
    return subprocess.Popen(process_executable)

def KillProcess(process=None):
    return process.kill()


'''
Browser activities
'''
from selenium.webdriver import Chrome

def ChromeBrowser():
    if platform.system() == 'Linux':
        chromedriver_path = '\\bin\\webdriver\\linux64\\chromedriver'
    elif platform.system() == 'Windows':
        chromedriver_path = '\\bin\\win32\\chromedriver.exe'
    else:
        chromedriver_path = '\\bin\\mac64\\chromedriver.exe'
    return Chrome(os.path.abspath(__file__).replace('activities.py','') + chromedriver_path)


''' 
OCR activities 
'''
import pytesseract

def ExtractTextFromImage(filename=None):
    if platform.system == 'Windows':
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
    return pytesseract.image_to_string(Image.open(filename))


'''
Excel activities
'''
import openpyxl

# Renaming functions
OpenExcelWorkbook = openpyxl.load_workbook

# Renaming classes
NewExcelWorkbook = openpyxl.Workbook


'''
Word activities
'''
import docx

def OpenWordDocument(filename=None):
    return docx.Document(filename)

def ReplaceText(document, text=None, replace_with=None):
        for paragraph in document.paragraphs:
            paragraph.text = paragraph.text.replace(text, replace_with)
        return document

def ConvertWordToPDF(word_filename=None, pdf_filename=None):
    if platform.system == 'Windows':
        from win32com import client
        word = client.DispatchEx('Word.Application')
        word_document = word.Documents.Open(word_filename)
        word_document.SaveAs(pdf_filename, FileFormat = 17)
        word_document.Close()
    else:
        print('Not implemented for other platforms than Windows.')