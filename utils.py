# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re
import random
import codecs
from itertools import izip

from wechat import TYPE_CAT, TYPE_DOG, TYPE_POEM, TYPE_OTHER, TYPE_TEXT, TYPE_IMAGE, TYPE_UNKNOWN

WORDS_FILE = 'words.txt'

WECHAT_CAT_WORDS = r'.*?(猫|喵|萌|咕|噜|毛|咪|Moew|mao|miao|miu|cat).*?'
WECHAT_DOG_WORDS = r'.*?(狗|汪|犬|吠|dog|gou).*?'
WECHAT_OTHER_WORDS = r'.*?(图|搞笑|表情|哦|哈|ha|hi|he|image|pic|img|gif|jpg).*?'
WECHAT_POEM_WORDS = r'.*?(古代|文学|作品|诗|词|曲|赋|律|调|唐|宋|poem|poetry).*?'
WECHAT_ERROR_HTML = '<html><head></head><body><h1>喵喵喵，这里不是麻瓜能来的，快走开</h1></body</html>'
WECHAT_UNKNOWN_TEXT = '发猫或狗有惊喜哦，喵喵喵~~~'
WECHAT_NO_IMAGE_TEXT = '图片找不到了，机器人出问题了'
WECHAT_NO_POEM_TEXT = '还没准备好诗词，啊哈哈!'

POETRY_OF_TANG = os.path.join('data', 'poetry_of_tang.txt')
POETRY_OF_SONG = os.path.join('data', 'poetry_of_song.txt')

with codecs.open(POETRY_OF_TANG, 'r', 'utf8') as f:
    content = f.read()
    lines = content.split('\n\n')
    TANG_LINES = list(filter(bool, lines))

with codecs.open(POETRY_OF_SONG, 'r', 'utf8') as f:
    content = f.read()
    lines = content.split('\n\n')
    SONG_LINES = list(filter(bool, lines))

POEM_LINES = TANG_LINES + SONG_LINES


def get_poem_one(text):
    if POEM_LINES:
        return random.choice(POEM_LINES)
    else:
        return WECHAT_NO_POEM_TEXT


def check_words(text):
    try:
        with codecs.open(WORDS_FILE, 'r', 'utf8') as f:
            words = f.readlines()
            words = [w.strip() for w in words]
            words = dict(izip(*([iter(words)]*2)))
            for word, response in words.iteritems():
                if re.search(word, text, re.I):
                    return response, False
    except Exception:
        pass


def get_content_type(text):
    words_response = check_words(text)
    if words_response:
        return words_response
    # return type,is_media
    if re.search(WECHAT_CAT_WORDS, text, re.I):
        return TYPE_CAT, True
    elif re.search(WECHAT_DOG_WORDS, text, re.I):
        return TYPE_DOG, True
    elif re.search(WECHAT_OTHER_WORDS, text, re.I):
        return TYPE_OTHER, True
    elif re.search(WECHAT_POEM_WORDS, text, re.I):
        return get_poem_one(text), False
    else:
        return WECHAT_UNKNOWN_TEXT, False


if __name__ == '__main__':
    print(random.choice(POEM_LINES))
