#!/bin/sh
rsync -av -e ssh --delete --exclude='.venv' --exclude='.git' --exclude='images' --exclude='data' --exclude='.pyc' --exclude='.vscode' --exclude='__pycache__' . ubuntu@tx.mcxiaoke.com:~/docker/wechat-robot
