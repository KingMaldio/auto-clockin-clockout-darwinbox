#!/bin/bash

# <path-to-env> example: /Users/yourname/Documents/auto-darwin/env/bin/activate (mac)
source <path-to-env>

# <path-to-auto-darwin> example: /Users/yourname/Documents/auto-darwin
pip install <path-to-auto-darwin>/requirements.txt
python <path-to-auto-darwin>/main.py
