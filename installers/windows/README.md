# Automagica Windows One-click Installer (NSIS)

## Description
This allows you to create a Windows-installer for Automagica, wrapping a Python distribution and environment ready for running Automagica.

## Usage
1. Add folders `lib` and `pynsist_pkgs` with required files.
1. Deploy new version of `automagica` library to PyPi.
1. Change working directory to this 's directory
2. Run `build.bat`
3. The setup file is created in in `build/nsis`.

### Other licenses
Below a list of external dependencies utilized, but not embedded, in this project:

Name|Version|License Type
---|---|---
NSIS|N/A|zlib License
pynsist|2.4|MIT License
Python|3.7|Python Software Foundation License
conda|N/A|BSD 3-Clause License
wheel|0.34.2|MIT License
pip|9.0.1|MIT License