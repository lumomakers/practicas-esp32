# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Prácticas con ESP32'
html_logo = "_static/general/logo_web.png"
copyright = '2026, Paco Avis'
author = 'Paco Avis'
release = 'S'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = []
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Hoja de estilos personalizada
html_css_files = ['css/custom.css',]


# Ocultar el enlace "Ver código fuente de la página"
html_show_sourcelink = False

#html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
