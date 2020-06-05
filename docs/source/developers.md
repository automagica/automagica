# Developers/contributors
## Release Automagica
1. Release on PyPi by running following commands from the main repository folder and providing PyPi credentials:
```bash
pip install twine
rmdir /S /Q dist # Windows
python setup.py sdist bdist_wheel
twine upload dist/*
```


## Internationalization
### Extracting localization strings with PyBabel
```
pybabel extract . -o locale/base.pot
```
### Create a new language .pot-file
For example for `pt_BR` (Portuguese Brazil)
```
pybabel init -l pt_BR -i locale/base.pot -d locale
```
