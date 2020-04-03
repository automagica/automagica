#!/usr/bin/env python
import sys
from distutils.core import setup

import setuptools
from setuptools.command.install import install


class InstallationWrapper(install):
    def run(self):
        """
        Custom installation wrapper to do pre-installation 
        and post-installation (i.e. to change permissions 
        on chromedriver binaries on Linux)
        """

        # Pre-install

        # Install
        install.run(self)

        # Post-install

        import platform

        if platform.system() == "Linux":
            import subprocess
            import os
            import automagica

            automagica_path = automagica.__file__.replace("__init__.py", "")

            # Make binaries executable
            binaries_path = os.path.join(automagica_path, "bin")
            subprocess.call(["chmod", "-R", "+x", binaries_path])

            # Make lab-folder writeable (required by Jupyter Notebook)
            lab_path = os.path.join(automagica_path, "lab")
            subprocess.call(["chmod", "-R", "777", lab_path])


# Cross-platform dependencies
install_requires = [
    "requests==2.22.0",  # Apache 2.0 License
    "selenium==3.7.0",  # Apache 2.0 License
    "pywinauto==0.6.5",  # BSD 3-Clause "New" or "Revised" License
    "openpyxl==2.4.8",  # MIT License
    "python-docx==0.8.6",  # MIT License
    "PyPDF2==1.26.0",  # BSD 3-Clause "New" or "Revised" License
    "faker==2.0.3",  # MIT License
    # BSD 3-Clause "New" or "Revised" License (requires python3-devel on Ubuntu/Fedora)
    "psutil==5.6.6",
    "PySimpleGUI==4.15.1",  # GNU Lesser General Public License v3.0
    "keyring==21.0.0",  # MIT License
    "cryptography==2.3.1",  # Apache 2.0 License/BSD 3-Clause "New" or "Revised" License
    "pyad==0.6.0",  # Apache 2.0 License
    "jupyterlab==1.2.4",  # BSD 3-Clause
    "py-trello==0.13.0",  # BSD 3-Clause "New" or "Revised" License
    "plyer==1.4.0",  # MIT License
    "Pillow==7.0.0",  # PIL License (permissive),
    "pyperclip==1.7.0",  # BSD License (BSD)
    "PyAutoGUI==0.9.48",  # BSD 3-Clause "New" license
    "pysnmp==4.4.12",  # BSD 2-Clause "Simplified" License
    "pandas==1.0.0",  # BSD 3-Clause
    "mss==5.0.0",  # MIT License
]


package_data = {
    "automagica": [
        "bin/win32/chromedriver.exe",  # BSD 3-Clause "New" or "Revised" License
        "bin/mac64/chromedriver",  # BSD 3-Clause "New" or "Revised" License
        "bin/linux64/chromedriver",  # BSD 3-Clause "New" or "Revised" License
        # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/automagica-lab.png",
        "lab/.jupyter/custom/custom.css",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/custom.js",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/favicon.png",  # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/logo.png",  # Copyrighted by Oakwood Technologies BVBA
        # Copyrighted by Oakwood Technologies BVBA
        "lab/.jupyter/custom/logo-white.png",
        "icon.ico",  # Copyrighted by Oakwood Technologies BVBA
        "icons/automagica.ico", # Copyrighted by Oakwood Technologies BVBA
        "icons/click_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/double_click_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/is_visible_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/middle_click_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/move_to_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/read_text_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/right_click_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/type_into_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/wait_appear_button.png", # Copyrighted by Oakwood Technologies BVBA
        "icons/wait_vanish_button.png", # Copyrighted by Oakwood Technologies BVBA        
    ]
}

setup(
    name="Automagica",
    version="2.1.12",
    description="Bot for Automagica",
    author="Oakwood Technologies BVBA",
    author_email="mail@oakwood.ai",
    url="https://automagica.com/",
    entry_points={"console_scripts": ["automagica=automagica.cli:main"]},
    packages=["automagica"],
    package_data=package_data,
    install_requires=install_requires,
    include_package_data=True,
    cmdclass={"install": InstallationWrapper},
)
