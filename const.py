# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re

WECHAT_CAT_WORDS = r'.*?(猫|喵|萌|图|GIF|gif|Moew|mao|miao|miu|cat).*?'
WECHAT_ERROR_HTML = '<html><head></head><body><h1>喵喵喵，这里不是给麻瓜能来的，快走开</h1></body</html>'