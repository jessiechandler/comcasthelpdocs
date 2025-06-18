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

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML Output Options -----------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']

# Enable custom templates (like layout.html for meta tags)
html_context = {}

# -- Options for HTML Meta Tags (via layout.html) ----------------------------

# No need to define meta here; they're injected in _templates/layout.html
