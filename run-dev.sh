#!/bin/bash
source ./.venv/bin/activate
pip install -r requirements.txt
export HOST_REDIS=1
# systemctl start redis-server
python app.py