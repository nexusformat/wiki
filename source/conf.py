# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import sys, os, datetime
import shutil
import warnings

# Suppress all warnings in Sphinx
# warnings.filterwarnings('ignore')
suppress_warnings = ["misc"]
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# add the abs path to the custom extension for collecting the contributor
# variables from the rst files
# -- Project information -----------------------------------------------------

project = "nexus wiki"
copyright = "2025, nexus"
author = "nexus"
release = "1"

# -- General configuration ---------------------------------------------------

# https://github.com/nexusformat/definitions/issues/659#issuecomment-577438319
needs_sphinx = "2.3"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_toolbox.collapse",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
    "sphinx.ext.autodoc",
]

# Show `.. todo` directives in the output
# todo_include_todos = True
source_encoding = "utf-8-sig"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinxdoc"
html_use_index = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add extra files
# html_extra_path = ['CNAME']

html_sidebars = {
    "**": [
        "localtoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html",
        "google_search.html",
        "nexus.html",
    ],
}


def setup(app):
    print("Sphinx setup() function is being called")

    def copy_asset(source_dir, target_dir):
        if not os.path.exists(source_dir):
            print(f"WARNING: The directory {source_dir} does not exist.")
            return
        print(f"Copying {source_dir} to {target_dir}")
        shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)

    def do_copy():
        print("Sphinx do_copy() function is being called")
        copy_asset(
            os.path.join(app.srcdir, "extra_files"),
            os.path.join(app.outdir, "extra_files"),
        )
        copy_asset(os.path.join(app.srcdir, "pdfs"), os.path.join(app.outdir, "pdfs"))

    app.connect("build-finished", lambda app, exception: do_copy())
    app.add_css_file("details_summary_hide.css")


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "../common/NeXus_Logo_dark_square.svg"
html_favicon = "https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark_square.svg"

# Output file base name for HTML help builder.
htmlhelp_basename = "NeXusWikidoc"

