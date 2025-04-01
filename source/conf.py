# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import sys, os, datetime
import shutil
import warnings
import logging

# Suppress all warnings in Sphinx
# warnings.filterwarnings('ignore')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# add the abs path to the custom extension for collecting the contributor variables from the rst files
#sys.path.insert(0, os.path.abspath('../../../dev_tools/ext'))
sys.path.insert(0, os.path.abspath('../dev_tools/ext'))
sys.path.insert(0, os.path.abspath("content"))

# Specify the master document
master_doc = "content/index"  # Path relative to the source directory

# -- Project information -----------------------------------------------------

project = 'nexusformat_wiki'      
copyright = '2025, nexus'
author = 'nexus'                  
release = '1'                     


# # The full version, including alpha/beta/rc tags
# version = u'unknown NXDL version'
# release = u'unknown NXDL release'
# nxdl_version = open('../../NXDL_VERSION').read().strip()
# if nxdl_version is not None:
#     version = nxdl_version.split('.')[0]
#     release = nxdl_version
# 
# 
# -- General configuration ---------------------------------------------------

# https://github.com/nexusformat/definitions/issues/659#issuecomment-577438319
needs_sphinx = '2.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_toolbox.collapse',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx_tabs.tabs',
    'contrib_ext',
    'myst_parser',
]

# Show `.. todo` directives in the output
# todo_include_todos = True
  
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinxdoc'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['common']
# html_extra_path = ['md']
html_file_suffix = ".html"

# Add extra files
#html_extra_path = ['CNAME']

html_sidebars = {
    '**': [
        'localtoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
        'google_search.html',
        'nexus.html',
    ],
}

myst_enable_extensions = ["linkify"]
myst_linkify_fuzzy_links = False  # Turn off automatic anchor/bookmark treatment
myst_all_links_external = True
myst_url_schemes = ("http", "https", "mailto", "file")  # Allow file paths
suppress_warnings = [
    'myst.crossref.target_not_found',
    'myst.header',
]
# html_extra_path = ['pdfs']

def setup(app):
    print("Sphinx setup() function is being called")
    logging.getLogger('myst').setLevel(logging.CRITICAL)

    def fix_hrefs(app, exception):

        # Path to the output HTML files
        html_output_dir = os.path.join(app.outdir, 'content')
        print(f"fix_hrefs() function is being called, html_output_dir={html_output_dir}")
        # Traverse the directory and process each HTML file
        for root, dirs, files in os.walk(html_output_dir):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # print(f"\treading [{file_path}]")
                        content = f.read()

                # Replace href="#something.html" with href="something.html"
                updated_content = content.replace('href="#', 'href="')

                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    # print(f"\twriting [{file_path}]")
                    f.write(updated_content)

    def copy_asset(source_dir, target_dir):
        if not os.path.exists(source_dir):
            print(f"WARNING: The directory {source_dir} does not exist.")
            return
        print(f"Copying {source_dir} to {target_dir}")
        shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)

    def do_copy():
        print("Sphinx do_copy() function is being called")
        copy_asset(os.path.join(app.srcdir, 'extra_files'), os.path.join(app.outdir, 'extra_files'))
        copy_asset(os.path.join(app.srcdir, 'pdfs'), os.path.join(app.outdir, 'pdfs'))

    def copy_extra_files(app, exception):
        print("Sphinx copy_extra_files() function is being called")
        if exception:
            return

    app.connect('build-finished', lambda app, exception: do_copy())
    # app.connect('build-finished', fix_hrefs)
    app.add_css_file('details_summary_hide.css')
    # Sapp.connect('build-finished', copy_extra_files)
    
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark_square.svg"
    
# Output file base name for HTML help builder.
htmlhelp_basename = 'NeXusWikidoc'
    

