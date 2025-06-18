# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = ' How do I Sign into Comcast Email Account? Step-by-Step Old Account Access Guide'
copyright = '2025, Access and manage your Comcast Account'
author = 'Mark Tawin'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
