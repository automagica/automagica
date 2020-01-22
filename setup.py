#!/usr/bin/env python
import sys
import setuptools
from distutils.core import setup

setup(
    name="Automagica",
    version="2.0.8",
    description="Bot for Automagica",
    author="Oakwood Technologies BVBA",
    author_email="mail@oakwood.ai",
    url="https://automagica.com/",
    entry_points={"console_scripts": ["automagica=automagica.cli:main"]},
    packages=["automagica"],
    package_data={
        "automagica": [
            "bin/win32/chromedriver.exe",
            "bin/mac64/chromedriver",
            "bin/linux64/chromedriver",
            "lab/.jupyter/custom/automagica-lab.png",
            "lab/.jupyter/custom/custom.css",
            "lab/.jupyter/custom/custom.js",
            "lab/.jupyter/custom/favicon.png",
            "lab/.jupyter/custom/logo.png",
            "lab/.jupyter/custom/logo-white.png",
            "icon.ico",
        ]
    },
    install_requires=["requests==2.22.0", "selenium==3.7.0"]
    + (
        [
            "pywinauto==0.6.5",  # BSD 3-Clause "New" or "Revised" License
            "pywin32==227",  # BSD 3-Clause "New" or "Revised" License
            "openpyxl==2.4.8",  # MIT License
            "python-docx==0.8.6",  # MIT License
            "PyPDF2==1.26.0",  # BSD 3-Clause "New" or "Revised" License
            "faker==2.0.3",  # MIT License
            "psutil==5.4.6",  # BSD 3-Clause "New" or "Revised" License
            "PySimpleGUI==4.15.1",  # GNU Lesser General Public License v3.0
            "keyring==21.0.0",  # MIT License
            "cryptography==2.3.1",  # Apache 2.0 License/BSD 3-Clause "New" or "Revised" License
            "pyad==0.6.0",  # Apache 2.0 License
            "jupyterlab==1.2.4",  # BSD 3-Clause
            "py-trello==0.13.0",  # BSD 3-Clause "New" or "Revised" License
            "plyer==1.4.0",  # MIT License
            "Pillow==7.0.0",  # PIL License (permissive)
            "PyAutoGUI==0.9.36",  # BSD 3-Clause "New" license
        ]
        if sys.platform.startswith("win")
        else []
    ),
    include_package_data=True,
)
