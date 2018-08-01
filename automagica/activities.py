import os
import platform
import shutil
from PIL import Image
import uuid

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
import pyautogui


def GetMouseCoordinates():
    '''
    Displays a message box with the absolute coordinates of the current position of the mouse.
    '''
    coord = pyautogui.position()
    coordstring = "( " + str(coord[0]) + " , " + str(coord[1]) + " )"
    return DisplayMessageBox(coordstring,"Mouse Position")


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



def PressKey(key=None):
    '''
    Press and release an entered key.
    '''
    if key:
        return pyautogui.press(key)


def PressHotkey(first_key,second_key,third_key=None):
    '''
    Press a combination of two or three keys simultaneously.
    '''
    if not third_key:
        return pyautogui.hotkey(first_key,second_key)
    if third_key:
        return pyautogui.hotkey(first_key,second_key,third_key)


def Type(text=None, interval_seconds=0.001):
    from pyautogui import typewrite
    # Set keyboard layout for Windows platform
    if platform.system() == 'Windows':
        from win32api import LoadKeyboardLayout
        LoadKeyboardLayout('00000409', 1)
    return typewrite(text, interval=interval_seconds)


def CreateUniqueKey(length=32):
    '''
    universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems. This key can be 
    considered as unique for there to be a one in a billion chance of duplication, 103 trillion version 4 UUIDs must be generated.
    The general form is e.g. "123e4567-e89b-12d3-a456-426655440000". The argument specifies the length of the returned string.
    If it is omitted, the entire 128-bit UUID is returned as a string.
    '''
    return str(uuid.uuid4())[:length]


'''
Windows activities
'''


def UseFailsafe(switch=True):
    from pyautogui import FAILSAFE
    FAILSAFE = switch


def ClearClipboard():
    from ctypes import windll
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    return


'''
Process activities
'''


def LaunchProcess(process_executable=None):
    from subprocess import Popen

    return Popen(process_executable)


def OpenProgramByName(name, main_drive = "C:\\"):
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
    Make sure you enter a valid path e.g. "C:\\Users\Bob\\Desktop\\RPA Examples\\data.xlsx"...
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
PDF Activities
'''

def MergePDF(pdf1,pdf2,merged_path):
    '''
    The first two arguments are the PDF's that need to be merged. The pages from pdf2 
    will be added to pdf2. The merged PDF receives a new path specefied by the third argument.
    '''
    from PyPDF2 import PdfFileMerger

    pdfs = [str(pdf1), str(pdf2)]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(merged_path)
    return


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


def UnzipFolder(path,new_path=False):
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


