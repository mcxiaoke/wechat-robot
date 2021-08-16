#!/bin/bash
source ~/docker/venv/bin/activate
pip install -r requirements.txt
export HOST_REDIS=1
python app.py