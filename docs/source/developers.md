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

# Want to join the development team?

## Developers
You can contribute in the following ways:
- Pull requests with code and/or documentation
- Feature requests, bug squatting, feel free to [create an issue](https://github.com/automagica/automagica/issues)!
- If you're interested in joining our team, [send us an e-mail](mailto:koen@automagica.com).
 

## Not a developer?
No problem! You can contribute in the following ways:
- __Star our repository__ by clicking the star icon at the top right of this page. This allows us to get more exposure within the GitHub community. The more people we can get involved the better!
- Miss a particular feature? [Create an 'issue'](https://github.com/automagica/automagica/issues)
- Something not working? [Create an issue](https://github.com/automagica/automagica/issues)
- Don't have a GitHub account? Feel free to send us an e-mail at [koen@automagica.com](mailto:koen@automagica.com) or [thomas@automagica.com](mailto:thomas@automagica.com).
