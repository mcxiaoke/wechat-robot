#!/bin/sh
rsync -av -e ssh --exclude='__pycache__/' --exclude='images/' --exclude='.venv/' . root@tx.mcxiaoke.com:/opt/docker/wechat-robot
