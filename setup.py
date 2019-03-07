#!/usr/bin/env python
from distutils.core import setup

setup(name='Automagica',
      version='0.3.4',
      description='Bot for Automagica - Smart Robotic Process Automation',
      author='Oakwood Technologies',
      author_email='mail@oakwood.ai',
      url='https://oakwood.ai/',
      entry_points={
          'console_scripts': ['automagica=automagica.command_line:main'],
      },
      packages=['automagica'],
      package_data={'automagica': [
          'bin/win32/chromedriver.exe',
          'bin/mac64/chromedriver',
          'bin/linux64/chromedriver']},
      install_requires=[
          'socketIO-client==0.7.2',
          'PyAutoGUI==0.9.36',
          'opencv-python==3.4.2.17',
          'sty==1.0.0b2',
          'selenium==3.7.0',
          'pywinauto==0.6.5',
          'pytesseract==0.2.0',
          'openpyxl==2.4.8',
          'python-docx==0.8.6',
          'pywin32==223',
          'PyPDF2==1.26.0',
          'psutil==5.4.6',
          'beautifulsoup4==4.6.0',
          'py-trello==0.13.0'
      ],
      include_package_data=True
      )
