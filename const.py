# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re

SOURCE_ROOT = os.path.join('..', 'images')

MATCH_WORDS = {
    r'.*?(猫|喵|萌|咕|噜|毛|咪|鼠|Moew|mao|miao|miu|cat).*?': 'cats',
    r'.*?(狗|汪|犬|吠|dog|gou).*?': 'dogs',
    r'.*?(鸟|鸡|鸭|鹅|鹤|雁|bird).*?': 'birds',
    r'.*?(鱼|fish).*?': 'fish',
    r'.*?(牛|马|驴|niu|cow).*?': 'cow',
    r'.*?(花|flower).*?': 'flower',
    r'.*?(图|搞笑|表情|哦|哈|呵|嘻|哇|嘎|呱|咕|gu|gua|ha|hi|he|image|pic|img|gif|jpg).*?': 'emoji'
}

MATCH_TYPES = MATCH_WORDS.values()

DEFAULT_TYPE = 'cats'
