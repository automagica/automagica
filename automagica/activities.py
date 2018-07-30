import os
import platform
import shutil
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


def OpenProgramByName(name, main_drive = "C:\\"):

    import os
    from subprocess import Popen

    if not name[-4:] == ".exe":
        name = name + ".exe"
    for root, dirs, files in os.walk(main_drive):
        for file in files:
            if file == name and file.endswith(".exe"):
                Popen(os.path.join(root, file))
				return


def KillProcess(process=None, name=None):
    import os
    if process:
        return process.kill()
    if name:
        return os.system("taskkill /f /im " + name + " >nul 2>&1")
    return


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
    Shows a pop-up message with title and body. Three possible types, info, error and warning with the default value info.
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
    Shows a pop-up message which asks for input which is captured and returned.
    '''
    from tkinter import Tk
    from tkinter.simpledialog import askstring

    root = Tk()
    root.withdraw() # hide main window

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
    if os.path.exists(path):
        os.startfile(path)
    return


def RenameFile(old_path,new_file_name):
    '''
    Entering "C:\\Users\\Documents\\Automagica.docx" as "old_path" and "Automagica123.docx" as new_file_name changes
    the name of the directory in C:\\Users\\Documents from Automagica to Automagica123. The function will not
    rename a file if a file with the desired name already exists in the folder.
    '''
    if os.path.isfile(old_path):
        base_path = old_path.split("\\")[:-1]
        new_path = "\\".join(base_path)+"\\" + new_file_name
        if not os.path.exists(new_path):
            os.rename(old_path,new_path)
    return


def MoveFile(old_path,new_location):
    '''
    Entering "C:\\Users\\Documents\\Automagica.docx" as old_path and "C:\\Users\\Downloads"
    as new_location moves the file Automagica.docx from directory "Documents" to directory "Downloads".
    If the new location already contains a file with the same name, a random 8 character uid will be added 
    in front of the name before the file is moved.
    '''
    import uuid
    name=old_path.split("\\")[-1]
    new_path=new_location + "\\" + name
    if os.path.exists(old_path):
        if not os.path.exists(new_path):
            os.rename(old_path,new_path)
        elif os.path.exists(new_path):
            new_path = new_location + "\\" + "(" + str(uuid.uuid4())[:8] + ") " + name
            os.rename(old_path,new_path)
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


def CopyFile(old_path,new_location):
    '''
    By entering "C:\\Users\\Documents\\Automagica.docx" as old_path and "C:\\Users\\Downloads" as new_location...
    the function copies the file "Automagica.docx" to the new location. If the new location already contains a file
    with the same name, the copy will replace this file.
    '''
    if os.path.isfile(old_path):
        if os.path.isdir(new_location):
            shutil.copy(old_path,new_location)


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
            os.rename(old_path,new_path)
    return


def OpenFolder(path):
    '''
    Entering "C:\\Users\\Downloads\\Automagica" will open the folder "Automagica" if the path exists.
    '''
    if os.path.exists(path):
        os.startfile(path)
    return


def MoveFolder(old_path, new_location):
    '''
    Entering "C:\\Users\\Oldlocation\\Automagica" as old_path and "C:\\Users\\Newlocation"
    as new_location moves the folder "Automagica" from directory "Oldlocation" to directory "Newlocation".
    If the new location already contains a folder with the same name, a random 8 character uid is added to the name.
    '''
    import uuid
    name=old_path.split("\\")[-1]
    new_path=new_location + "\\" + name
    if os.path.isdir(old_path):
        if not os.path.isdir(new_path):
            os.rename(old_path,new_path)
        elif os.path.isdir(new_path):
            new_path = new_path + " (" + str(uuid.uuid4())[:8] + ")"
            os.rename(old_path,new_path)
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


def EmptyFolder(path, allow_root = False):
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


def CopyFolder(old_path,new_location):
    '''
    By entering "C:\\Users\\Documents\\Automagica" as old_path and "C:\\Users\\Downloads" as new_location...
    the function copies the folder "Automagica" together with all its contents to the new location. The folder name...
    remains unchanged, except when the folder already exists a 8 character random uid will be added to the name.
    '''
    import uuid
    new_path=new_location + "\\" + old_path.split("\\")[-1]
    if os.path.isdir(old_path):
        if not os.path.isdir(new_path):
            shutil.copytree(old_path,new_path)
        elif os.path.isdir(new_path):
            if os.path.isdir(new_path):
                new_path = new_path + " (" + str(uuid.uuid4())[:8] + ")"
            shutil.copytree(old_path,new_path)
    return


def ZipFolder(dir_path,new_path):
    '''
    Creates a zipped directory of a directory specified by the first argument. The newly zipped directory 
    receives a path specified by the second argument.
    '''
    if os.path.isdir(dir_path):
        shutil.make_archive(new_path,'zip',dir_path)
    return


'''
Windows Applications
'''
import subprocess

def OpenCalculator():
    """
    Open Calculator.
    """
    subprocess.Popen("calc.exe")
    return


def OpenPaint():
    """
    Open MS Paint.
    """
    subprocess.Popen("mspaint.exe")
    return


def OpenNotepad():
    """
    Open Notepad
    """
    subprocess.Popen("notepad.exe")
    return


def OpenSnippingTool():
    """
    Open Snipping Tool.
    """
    subprocess.Popen("SnippingTool.exe")
    return


def OpenControlPanel():
    """
    Open Windows Control Panel.
    """
    subprocess.Popen("control.exe")
    return


def OpenCleanManager():
    """
    Open Clean Manager.
    """
    subprocess.Popen("cleanmgr.exe")
    return


def OpenDialer():
    """
    Open Windows Dialer.
    """
    subprocess.Popen("dialer.exe")
    return


def OpenVolumeMixer():
    """
    Open Windows Volume Mixer.
    """
    subprocess.Popen("SndVol.exe")
    return


def OpenXPSViewer():
    """
    Open Windows XPS Viewer.
    """
    subprocess.Popen("xpsrchvw")
    return    

