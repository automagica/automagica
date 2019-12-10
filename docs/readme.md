# Automagica documentation building

Guid to build documentation from activities.py file automatically?


## Installation



```python
pip install sphinx
# Optional for theme
sudo pip install sphinx_rtd_theme
```
Make a doc folder and run:
```python
sphinx-quickstart
```

This should create conf.py and make.bat files. Doctree should look like:

├───automagica
├───docs
    ├───build
    │   ├───doctrees
    │   └───html
    │       ├───_sources
    │       └───_static
    └───source
        ├───_static
        └───_templates

Where the automagica folder holds the automagica.py file with docstrings

## Building

First step is to create .rst files. Go to docs folder and run:

```python
sphinx-apidoc -o ./source ../automagica -f
```

Next edit the config file (conf.py) to include the activities.py by adding:
```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../automagica'))
```
Final step is to build the html by running make.bat in the doc folder:
```python
make html
```

Final tree should look like:

├───automagica
│       activities.py
│
└───docs
    │   make.bat
    │   Makefile
    │   readme.md
    │
    ├───build
    │   ├───doctrees
    │   │       activities.doctree
    │   │       environment.pickle
    │   │       index.doctree
    │   │       modules.doctree
    │   │
    │   └───html
    │       │   .buildinfo
    │       │   .nojekyll
    │       │   activities.html
    │       │   genindex.html
    │       │   index.html
    │       │   modules.html
    │       │   objects.inv
    │       │   py-modindex.html
    │       │   search.html
    │       │   searchindex.js
    │       │
    │       ├───_sources
    │       │       activities.rst.txt
    │       │       index.rst.txt
    │       │       modules.rst.txt
    │       │
    │       └───_static
    │               ajax-loader.gif
    │               alabaster.css
    │               basic.css
    │               comment-bright.png
    │               comment-close.png
    │               comment.png
    │               custom.css
    │               doctools.js
    │               documentation_options.js
    │               down-pressed.png
    │               down.png
    │               file.png
    │               jquery-3.2.1.js
    │               jquery.js
    │               minus.png
    │               plus.png
    │               pygments.css
    │               searchtools.js
    │               underscore-1.3.1.js
    │               underscore.js
    │               up-pressed.png
    │               up.png
    │               websupport.js
    │
    └───source
        │   activities.rst
        │   conf.py
        │   index.rst
        │   modules.rst
        │
        ├───_static
        └───_templates

# Rebuilding

Rebuilding can be done with following commands in doc folder:

```python
sphinx-apidoc -o ./source ../automagica -f
make clean
make html
```