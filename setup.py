#!/usr/bin/env python
import sys
import setuptools
from distutils.core import setup

setup(name='Automagica',
      version='2.0.0',
      description='Robot for Automagica - Smart Robotic Process Automation',
      author='Oakwood Technologies BVBA',
      author_email='mail@oakwood.ai',
      url='https://automagica.com/',
      entry_points={
          'console_scripts': ['automagica=automagica.cli:main'],
      },
      packages=['automagica'],
      package_data={'automagica': [
          'bin/win32/chromedriver.exe',
          'bin/mac64/chromedriver',
          'bin/linux64/chromedriver']},
      install_requires=[
          'plyer==1.4.0',
          'python-socketio==4.3.0',
          'PyAutoGUI==0.9.36',
          'opencv-python==3.4.2.17',
          'selenium==3.7.0',
          'pytesseract==0.2.0',
          'openpyxl==2.4.8',
          'python-docx==0.8.6',
          'PyPDF2==1.26.0',
          'faker==2.0.3'
          'psutil==5.4.6',
          'keyring==13.0.0',
          'PySimpleGUI==4.4.1',
          'beautifulsoup4==4.6.0',
          'keyring==13.0.0',
          'websocket-client==0.56.0',
          'cryptography==2.3.1',
          'py-trello==0.13.0'] + (
              ['pywinauto==0.6.5', 'pywin32==225'] if sys.platform.startswith('win') else [
              ]
      ),
      include_package_data=True
      )
