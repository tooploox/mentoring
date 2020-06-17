#!/bin/bash

PYTHONPATH=. python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip