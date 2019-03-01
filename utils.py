# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re
import random
import codecs
import logging
from itertools import izip

from const import SOURCE_ROOT, IMAGE_WORDS

logging.basicConfig(level=logging.DEBUG)

WORDS_FILE = 'words.txt'
POEM_LINES = []
JOKE_LINES = []
RE_POEM_WORDS = r'.*?(古代|文学|作品|诗|词|曲|赋|律|调|唐|宋|poem|poetry).*?'
WECHAT_ERROR_HTML = '<html><head></head><body><h1>喵喵喵，这里不是麻瓜能来的，快走开~~~</h1></body</html>'
WECHAT_UNKNOWN_TEXT = '发猫或狗有惊喜哦，喵喵喵~~~'
WECHAT_NO_IMAGE_TEXT = '图片找不到了，机器人出问题了'
WECHAT_NO_POEM_TEXT = '还没准备好诗词，啊哈哈!'

POETRY_OF_TANG = os.path.join('data', 'poetry_of_tang.txt')
POETRY_OF_SONG = os.path.join('data', 'poetry_of_song.txt')
JOKES_FILE = os.path.join('data', 'jokes.txt')

try:
    with codecs.open(POETRY_OF_TANG, 'r', 'utf8') as f:
        content = f.read()
        lines = content.split('\n\n')
        TANG_LINES = list(filter(bool, lines))

    with codecs.open(POETRY_OF_SONG, 'r', 'utf8') as f:
        content = f.read()
        lines = content.split('\n\n')
        SONG_LINES = list(filter(bool, lines))
    POEM_LINES = TANG_LINES + SONG_LINES
except:
    logging.info('init poem lines failed')

try:
    with codecs.open(JOKES_FILE, 'r', 'utf8') as f:
        content = f.read()
        lines = content.split('\n\n')
        JOKE_LINES = list(filter(bool, lines))
except:
    logging.info('init joke lines failed')


def get_poem_one(text):
    if POEM_LINES:
        return random.choice(POEM_LINES)
    else:
        return WECHAT_NO_POEM_TEXT

def get_joke_one(text):
    if JOKE_LINES:
        return random.choice(JOKE_LINES)
    else:
        return WECHAT_UNKNOWN_TEXT

def check_words(text):
    # 从文件中找匹配的回复文本
    try:
        with codecs.open(WORDS_FILE, 'r', 'utf8') as f:
            words = f.readlines()
            words = [w.strip() for w in words]
            words = dict(izip(*([iter(words)]*2)))
            for word, response in words.iteritems():
                if re.search(word, text, re.I):
                    return response
    except Exception:
        logging.info('check words failed')


def get_content_type(text):
    if text == '/list':
        return '\n'.join(IMAGE_WORDS.keys()), False
    words_response = check_words(text)
    # return matched text
    if words_response:
        return words_response, False
    for m_words, m_type in IMAGE_WORDS.items():
        if re.search(m_words, text, re.I):
            return m_type, True
    if re.search(RE_POEM_WORDS, text, re.I):
        return get_poem_one(text), False
    else:
        return get_joke_one(text), False


if __name__ == '__main__':
    print(random.choice(POEM_LINES))
