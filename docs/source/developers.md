# Developers/contributors
This document contains information and serves as a reference for the Automagica core development team. It contains
## Build installers
### Windows One-Click Installer
From Windows 10 (VM), change current working directory to `/installers/windows` and run `build`. After the build process finishes, an executable can be found in the `/installers/windows/build/nsis` directory.

## Release on Python Package Index (PyPI)
Release on PyPi by running following commands from the main repository directory and providing PyPi credentials:
```bash
pip install twine
rmdir /S /Q dist # Windows
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Internationalization
### Extracting localization strings with PyBabel
```
pybabel extract -o locale/base.pot automagica
pybabel update -i messages.pot -d locale
```
After modification:
```
pybabel compile -d locale
```

### Create a new language .pot-file
For example for `pt_BR` (Portuguese Brazil)
```
pybabel init -l pt_BR -i locale/base.pot -d locale
```
