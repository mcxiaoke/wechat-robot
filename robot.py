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

from config import WECHAT_TOKEN, WECHAT_AES_KEY, WECHAT_APPID, WECHAT_APPSECRET
from const import WECHAT_CAT_WORDS, WECHAT_ERROR_HTML
from utils import get_media_ids, get_poem_lines
import logging
logging.basicConfig(level=logging.INFO)

robot = WeRoBot()
robot.config['TOKEN'] = WECHAT_TOKEN
robot.config['ENCODING_AES_KEY'] = WECHAT_AES_KEY
robot.config["APP_ID"] = WECHAT_APPID
robot.config["APP_SECRET"] = WECHAT_APPSECRET

media_ids = get_media_ids()
poem_lines = get_poem_lines()

@robot.filter(re.compile(WECHAT_CAT_WORDS))
def handle_cat(message):
    if media_ids:
    	media_id = random.choice(media_ids)
        return ImageReply(message, media_id=media_id)
    return "没找到猫图喵~~~"

@robot.handler
def handle_all(message):
    if poem_lines:
        return random.choice(poem_lines)
    else:
        return "咕噜咕咕咕咕咕噜咕咕"

@robot.error_page
def make_error_page(url):
    return WECHAT_ERROR_HTML
