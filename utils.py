# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re
import random
import codecs

WECHAT_CAT_WORDS = r'.*?(猫|喵|萌|咕|噜|Moew|mao|miao|miu|cat).*?'
WECHAT_DOG_WORDS = r'.*?(狗|汪|犬|吠|dog|gou).*?'
WECHAT_POEM_WORDS = r'.*?(古代|文学|作品|诗|词|曲|赋|律|调|唐|宋|poem|poetry).*?'
WECHAT_ERROR_HTML = '<html><head></head><body><h1>喵喵喵，这里不是给麻瓜能来的，快走开</h1></body</html>'

POETRY_OF_TANG = os.path.join('data', 'poetry_of_tang.txt')
POETRY_OF_SONG = os.path.join('data', 'poetry_of_song.txt')

with codecs.open(POETRY_OF_TANG, 'r', 'utf8') as f:
    content = f.read()
    lines = content.split('\n\n')
    TANG_LINES = list(filter(bool, lines))

from wechat import TYPE_CAT, TYPE_DOG, TYPE_POEM, TYPE_OTHER

def get_poem_one(text):
    if TANG_LINES:
        return random.choice(TANG_LINES)
    else:
        return '还没准备好诗词，啊哈哈!'

def get_content_type(text):
    # return type,is_media
    if re.search(WECHAT_CAT_WORDS, text, re.I):
        return TYPE_CAT, True
    elif re.search(WECHAT_DOG_WORDS, text, re.I):
        return TYPE_DOG, True
    elif re.search(WECHAT_POEM_WORDS, text, re.I):
        return TYPE_POEM, False
    else:
        return TYPE_OTHER, False

if __name__ == '__main__':
    print(random.choice(TANG_LINES))
