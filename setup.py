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

        if platform.system() == "Linux" or platform.system() == "Darwin":
            import subprocess  # nosec
            import os
            import automagica

            automagica_path = automagica.__file__.replace(
                os.path.basename(os.path.realpath(__file__)), ""
            )

            # Make binaries executable
            binaries_path = os.path.join(automagica_path, "bin")
            subprocess.call(["chmod", "-R", "+x", binaries_path])

            # Make lab-folder writeable (required by Jupyter Notebook)
            lab_path = os.path.join(automagica_path, "lab")
            subprocess.call(["chmod", "-R", "777", lab_path])


# Use the readme in the main folder to
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Only show the first part of the Readme, up to the first title
long_description = long_description.split("##")[0]

setup(
    name="Automagica",
    version="3.1.1",
    description="Open Source RPA and UI automation",
    author="Oakwood Technologies BVBA",
    author_email="mail@oakwood.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://automagica.com/",
    project_urls={
        "Documentation": "https://automagica.readthedocs.io/",
        "Source Code": "https://github.com/automagica/automagica",
    },
    entry_points={"console_scripts": ["automagica=automagica.cli:cli"]},
    packages=["automagica"],
    install_requires=[
        "requests==2.24.0",  # Apache 2.0 License
        "selenium==3.141.0",  # Apache 2.0 License
        "openpyxl==3.0.4",  # MIT License
        "python-docx==0.8.10",  # MIT License
        "PyPDF2==1.26.0",  # BSD 3-Clause "New" or "Revised" License
        "mimesis==4.1.1",  # MIT License
        "psutil==5.6.6",  # BSD 3-Clause
        "keyring==21.0.0",  # MIT License
        "cryptography==3.0",  # Apache 2.0 License/BSD 3-Clause "New" or "Revised" License
        "pyad==0.6.0",  # Apache 2.0 License
        "Pillow==7.2.0",  # PIL License (permissive),
        "pysnmp==4.4.12",  # BSD 2-Clause "Simplified" License
        "pandas==1.1.0",  # BSD 3-Clause
        "mss==5.0.0",  # MIT License
        "mouse==0.7.1",  # MIT License
        "keyboard==0.13.5",  # MIT License
        "babel==2.7.0",  # BSD 3-Clause
        "click==7.0",  # BSD 3-Clause6
        "idna==2.5",  # BSD 3-Clause
        "pyglet==1.5.5",  # MIT License
        "jupyterlab==2.1.5",  # BSD License
    ],
    include_package_data=True,
    cmdclass={"install": InstallationWrapper},
)

