# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import logging
import os
import shutil
import sys

# Suppress all warnings in Sphinx
# warnings.filterwarnings('ignore')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# add the abs path to the custom extension for collecting the contributor variables from the rst files
sys.path.insert(0, os.path.abspath('../dev_tools/ext'))
sys.path.insert(0, os.path.abspath("content"))

# Specify the master document
master_doc = "index"  # Path relative to the source directory

# -- Project information -----------------------------------------------------

project = 'nexusformat_wiki'
copyright = '2025, nexus'
author = 'nexus'
release = '1'

# -- General configuration ---------------------------------------------------
needs_sphinx = '2.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'contrib_ext',
    'myst_parser',
]

# Show `.. todo` directives in the output
# todo_include_todos = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain _templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'
html_title = ''
# Disable the generation of genindex.html
html_use_index = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_file_suffix = ".html"

# Add extra files
# html_extra_path = ['CNAME']

html_sidebars = {
    '**': [
        'localtoc.html',
        'sourcelink.html',
        'searchbox.html',
        'nexus.html',
    ],
}

myst_enable_extensions = ["linkify", "strikethrough"]
myst_linkify_fuzzy_links = False  # Turn off automatic anchor/bookmark treatment
myst_all_links_external = True
myst_url_schemes = ("http", "https", "mailto", "file")  # Allow file paths
suppress_warnings = [
    'myst.crossref.target_not_found',
    'myst.header',
    'myst.strikethrough',
]

def setup(app):
    print("Sphinx setup() function is being called")
    logging.getLogger('myst').setLevel(logging.CRITICAL)

    def copy_asset(source_dir, target_dir):
        if not os.path.exists(source_dir):
            print(f"WARNING: The directory {source_dir} does not exist.")
            return
        print(f"Copying {source_dir} to {target_dir}")
        shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)

    def do_copy():
        print("Sphinx do_copy() function is being called")
        copy_asset(os.path.join(app.srcdir, 'pdfs'), os.path.join(app.outdir, 'pdfs'))

    app.connect('build-finished', lambda app, exception: do_copy())
    app.add_css_file('details_summary_hide.css')


# The name of an image file (within the static path) to use as favicon of the
# content.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark_square.svg"

# Output file base name for HTML help builder.
htmlhelp_basename = 'NeXusWikidoc'


