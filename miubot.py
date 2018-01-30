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

from config import WECHAT2_TOKEN, WECHAT2_AES_KEY, WECHAT2_APPID, WECHAT2_APPSECRET
from const import WECHAT_CAT_WORDS, WECHAT_ERROR_HTML
from utils import get_media_ids2, get_poem_lines2
import logging
logging.basicConfig(level=logging.DEBUG)

miubot = WeRoBot()
miubot.config['TOKEN'] = WECHAT2_TOKEN
miubot.config['ENCODING_AES_KEY'] = WECHAT2_AES_KEY
miubot.config["APP_ID"] = WECHAT2_APPID
miubot.config["APP_SECRET"] = WECHAT2_APPSECRET

media_ids = get_media_ids2()
poem_lines = get_poem_lines2()

@miubot.filter(re.compile(WECHAT_CAT_WORDS))
def handle_cat(message):
    logging.debug('handle_cat msg=%s' % message)
    if media_ids:
    	media_id = random.choice(media_ids)
        logging.debug('handle_cat media_id=%s' %media_id)
        return ImageReply(message, media_id=media_id)
    return "没找到猫图喵~~~"

@miubot.handler
def handle_all(message):
    if poem_lines:
        return random.choice(poem_lines)
    else:
        return "咕噜咕咕咕咕咕噜咕咕"

@miubot.error_page
def make_error_page(url):
    return WECHAT_ERROR_HTML
