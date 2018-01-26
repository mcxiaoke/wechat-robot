# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re
import random
import codecs
import requests
from werobot import WeRoBot
from werobot.replies import TextReply, ImageReply, SuccessReply

from config import WECHAT_TOKEN as TOKEN
from config import WECHAT_AES_KEY as AES_KEY
from config import WECHAT_APPID as APPID
from config import WECHAT_APPSECRET as APPSECRET

import logging

logging.basicConfig(level=logging.INFO)

robot = WeRoBot(token=TOKEN)
robot.config["APP_ID"] = APPID
robot.config["APP_SECRET"] = APPSECRET
robot.config['ENCODING_AES_KEY'] = AES_KEY

with open('media_ids.txt') as f:
    media_ids = f.read().splitlines()

with codecs.open('poems.txt', 'r', 'utf8') as f:
    poem_lines = f.read().splitlines()

@robot.filter(re.compile(r".*?(猫|喵|萌|图|GIF|gif|Moew|mao|miao|miu|cat).*?"))
def cat(message):
    if media_ids:
    	media_id = random.choice(media_ids)
        return ImageReply(message, media_id=media_id)
    return "没找到猫图喵~~~"

@robot.handler
def process(message):
    if poem_lines:
        return random.choice(poem_lines)
    else:
        return "咕噜咕咕咕咕咕噜咕咕"

@robot.error_page
def make_error_page(url):
    return "<h1>喵喵喵，这里不是给麻瓜能来的，快走开</h1>"
