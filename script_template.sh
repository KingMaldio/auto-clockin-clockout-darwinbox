#!/bin/bash

# <path-to-env> example: /Users/yourname/Documents/auto-darwin/env/bin/activate (mac)
source <path-to-env>

pip install selenium
pip install webdriver_manager

# <path-to-auto-darwin> example: /Users/yourname/Documents/auto-darwin/main.py
python <path-to-auto-darwin>
