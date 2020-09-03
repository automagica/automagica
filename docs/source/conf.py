import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
project = "Automagica"
copyright = "2020, Oakwood Technologies BVBA"
author = "Oakwood Technologies BVBA"
version = ""
release = "3"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.githubpages", "recommonmark"]
templates_path = ["_templates"]
source_suffix = [".rst", ".md"]
master_doc = "index"
language = None
exclude_patterns = []
pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
    "https://fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic,900italic,900",
]
html_logo = "_static/logo.png"
html_theme_options = {
    "logo_only": True,
    "display_version": False,
}
htmlhelp_basename = "Automagicadoc"
latex_elements = {}
latex_documents = [
    (
        master_doc,
        "Automagica.tex",
        "Automagica Documentation",
        "Oakwood Technologies BVBA",
        "manual",
    ),
]
man_pages = [(master_doc, "automagica", "Automagica Documentation", [author], 1)]
texinfo_documents = [
    (
        master_doc,
        "Automagica",
        "Automagica Documentation",
        author,
        "Automagica",
        "One line description of project.",
        "Miscellaneous",
    ),
]

