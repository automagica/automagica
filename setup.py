#!/usr/bin/env python
import sys
import setuptools
from distutils.core import setup

# Cross-platform dependencies
install_requires = [
    "requests==2.22.0",  # Apache 2.0 License
    "selenium==3.7.0",  # Apache 2.0 License
    "pywinauto==0.6.5",  # BSD 3-Clause "New" or "Revised" License
    "openpyxl==2.4.8",  # MIT License
    "python-docx==0.8.6",  # MIT License
    "PyPDF2==1.26.0",  # BSD 3-Clause "New" or "Revised" License
    "faker==2.0.3",  # MIT License
    "psutil==5.4.6",  # BSD 3-Clause "New" or "Revised" License (requires python3-devel on Ubuntu/Fedora)
    "PySimpleGUI==4.15.1",  # GNU Lesser General Public License v3.0
    "keyring==21.0.0",  # MIT License
    "cryptography==2.3.1",  # Apache 2.0 License/BSD 3-Clause "New" or "Revised" License
    "pyad==0.6.0",  # Apache 2.0 License
    "jupyterlab==1.2.4",  # BSD 3-Clause
    "py-trello==0.13.0",  # BSD 3-Clause "New" or "Revised" License
    "plyer==1.4.0",  # MIT License
    "Pillow==7.0.0",  # PIL License (permissive)
    "PyAutoGUI==0.9.48",  # BSD 3-Clause "New" license
]

# Windows-only dependencies
if sys.platform.startswith("win"):
    install_requires += ["pywin32==227"]  # BSD 3-Clause "New" or "Revised" License

package_data = {
    "automagica": [
        "bin/win32/chromedriver.exe",  # BSD 3-Clause "New" or "Revised" License
        "bin/mac64/chromedriver",  # BSD 3-Clause "New" or "Revised" License
        "bin/linux64/chromedriver",  # BSD 3-Clause "New" or "Revised" License
        "lab/.jupyter/custom/automagica-lab.png",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/custom.css",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/custom.js",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/favicon.png",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/logo.png",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/logo-white.png",  # Copyrighted by Oakwood Technologies BVBA
        "icon.ico",  # Copyrighted by Oakwood Technologies BVBA
    ]
}

setup(
    name="Automagica",
    version="2.0.9",
    description="Bot for Automagica",
    author="Oakwood Technologies BVBA",
    author_email="mail@oakwood.ai",
    url="https://automagica.com/",
    entry_points={"console_scripts": ["automagica=automagica.cli:main"]},
    packages=["automagica"],
    package_data=package_data,
    install_requires=install_requires,
    include_package_data=True,
)

# In case of Linux, make the chromedriver executable (superuser required)
import platform

if platform.system() == "Linux":
    import automagica

    library_path = automagica.__file__.replace("__init__.py", "")

    import os
    import stat

    chromedriver_path = os.path.join(library_path, "bin/linux64/chromedriver")
    st = os.stat(chromedriver_path)
    os.chmod(chromedriver_path, st.st_mode | stat.S_IEXEC)
