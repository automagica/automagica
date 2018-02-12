#!/usr/bin/env python

from distutils.core import setup

setup(name='Automagica',
      version='0.1',
      description='Robot for Automagica - Smart Robotic Process Automation',
      author='Koen van Eijk',
      author_email='koen@oakwood.ai',
      url='https://oakwood.ai/',
      entry_points = {
        'console_scripts': ['automagica=automagica.command_line:main'],
      },
      packages=['automagica'],
      install_requires=[
          'socketIO-client==0.7.2',
          'PyAutoGUI==0.9.36',
          'opencv-python==3.4.0.12',
          'sty==1.0.0b2'
      ],
)