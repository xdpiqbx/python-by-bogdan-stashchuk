# import pygame

# pip --version
# pip3 --version
# pip 23.1.2 from .....\venv\lib\site-packages\pip (python 3.10)

# https://pypi.org

# Example
# pip install pygame
# pip uninstall pygame

# $ pip list
# Package    Version
# ---------- -------
# pip        23.1.2
# pygame     2.5.0
# setuptools 65.5.1
# wheel      0.38.4

# pygame.init()
# pygame 2.5.0 (SDL 2.28.0, Python 3.10.10)
# Hello from the pygame community. https://www.pygame.org/contribute.html

# ============================================================================ PIPEnv

#  -------------------------------!!!!! Install global
# https://pypi.org/project/pipenv/
# pip install pipenv
#  -------------------------------!!!!!

# After global installation:
# .../max> pip list
# Package          Version
# ---------------- ---------
# certifi          2023.5.7
# distlib          0.3.6
# et-xmlfile       1.1.0
# filelock         3.12.2
# pip              23.1.2
# pipenv           2023.7.11
# platformdirs     3.8.1
# setuptools       68.0.0
# virtualenv       20.23.1
# virtualenv-clone 0.5.7


# In Project folder:
#   1. Create folder .venv
#   2. pipenv install requests INSTEAD # pip install requests
# NOTE: you can "pip install requests" but it will not be in the Pipfile
#   3. To remove pack -> pipenv uninstall requests

# In PyCharm always choose environment Pipenv !!!

# pipenv install # will install all dependencies from Pipfile

# Activate pipenv
# $ pipenv shell
# Shell for D:\Python\python-by-bogdan-stashchuk\.venv already activated.
# New shell not activated to avoid nested environments.

# ==============================================
# pipenv graph - All deps in current pipenv
# pipenv update - update all pacs
# pipenv update requests - update only requests


# ============================================== Simple using requests module
# import requests
#
# r = requests.get('https://www.python.org')
# print(r)
# print(r.status_code)
# print(r.text)
