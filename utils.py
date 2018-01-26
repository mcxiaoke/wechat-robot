# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import re
import random
import codecs

def get_media_ids():
    with open('media_ids.txt') as f:
        return f.read().splitlines()

def get_poem_lines():
    with codecs.open('poems.txt', 'r', 'utf8') as f:
        return f.read().splitlines()