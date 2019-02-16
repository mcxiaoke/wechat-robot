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
from wechat import MediaStore
from config import CONFIG, CONFIG2
from const import DEFAULT_TYPE
from utils import get_content_type, WECHAT_UNKNOWN_TEXT, WECHAT_NO_IMAGE_TEXT

logging.basicConfig(level=logging.DEBUG)


webot = WeRoBot()
webot.config.update(CONFIG)
westore = MediaStore('webot', CONFIG['APP_ID'], CONFIG['APP_SECRET'])

miubot = WeRoBot()
miubot.config.update(CONFIG2)
miustore = MediaStore('miubot', CONFIG2['APP_ID'], CONFIG2['APP_SECRET'])


def _reply_one_media(message, store, type_name=DEFAULT_TYPE):
    media_id = store.random_user_media_id(message.source, type_name)
    logging.info('_handle_text media_id=%s' % media_id)
    if media_id:
        return ImageReply(message=message, media_id=media_id)
    else:
        return WECHAT_NO_IMAGE_TEXT


def _handle_text(message, store):
    logging.info('_handle_text from=%s' % message.source)
    logging.info('_handle_text to=%s' % message.target)
    type_name, is_media = get_content_type(message.content)
    logging.info('_handle_text type=%s' % type_name)
    return _reply_one_media(message, store, type_name) if is_media else type_name


@webot.text
def we_handle_text(message):
    return _handle_text(message, westore)


@miubot.text
def miu_handle_text(message):
    return _handle_text(message, miustore)


@webot.image
def we_handle_image(message):
    return _reply_one_media(message, westore)


@miubot.image
def miu_handle_image(message):
    return _reply_one_media(message, miustore)


@webot.handler
def we_handle_all(message):
    return WECHAT_UNKNOWN_TEXT


@miubot.handler
def miu_handle_all(message):
    return WECHAT_UNKNOWN_TEXT
