# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project Information -----------------------------------------------------

project = 'How do i Sign into Comcast Email Account? Step-by-Step old Account Access Guide'
author = 'Mark Tawin'
copyright = '2025, Sign into Comcast Email Account'
release = '1.0.0'

# -- General Configuration ---------------------------------------------------

extensions = []

#This tells Sphinx where to find custom templates like layout.html
templates_path = ['_templates']

# Exclude build and OS files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML Output Options -----------------------------------------------------

# Choose your theme here (use 'furo', 'sphinx_rtd_theme', etc.)
html_theme = 'furo'

# Required for injecting meta tags using layout.html
html_context = {}

# Path to static assets (CSS, images if needed)
html_static_path = ['_static']
