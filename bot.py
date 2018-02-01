# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re
import random
import codecs
import requests
import logging
from werobot import WeRoBot
from werobot.replies import TextReply, ImageReply, SuccessReply
from wechat import MediaStore, TYPE_CAT, TYPE_DOG, TYPE_POEM, TYPE_OTHER
from utils import get_content_type, get_poem_one, WECHAT_UNKNOWN_TEXT, WECHAT_NO_IMAGE_TEXT

logging.basicConfig(level=logging.DEBUG)

from config import CONFIG, CONFIG2

webot = WeRoBot()
webot.config.update(CONFIG)
westore = MediaStore('webot', CONFIG['APP_ID'], CONFIG['APP_SECRET'])

miubot = WeRoBot()
miubot.config.update(CONFIG2)
miustore = MediaStore('miubot', CONFIG2['APP_ID'], CONFIG2['APP_SECRET'])

def _handle_text(message, store):
    logging.info('_handle_text from=%s' % message.source)
    logging.info('_handle_text to=%s' % message.target)
    type_name, is_media = get_content_type(message.content)
    logging.info('_handle_text type=%s' % type_name)
    if is_media:
        media_id = store.random_user_media_id(message.source, type_name)
        logging.info('_handle_text media_id=%s' % media_id)
        if media_id:
            return ImageReply(message=message, media_id=media_id)
        else:
            return WECHAT_NO_IMAGE_TEXT
    elif type_name == TYPE_POEM:
            return get_poem_one(message.content)
    return WECHAT_UNKNOWN_TEXT

@webot.text
def we_handle_text(message):
    return _handle_text(message, westore)


@miubot.text
def miu_handle_text(message):
    return _handle_text(message, miustore)

@webot.handler
def we_handle_all(message):
    return WECHAT_UNKNOWN_TEXT

@miubot.handler
def miu_handle_all(message):
    return WECHAT_UNKNOWN_TEXT
