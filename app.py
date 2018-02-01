# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals
import os
import logging

from flask import Flask, request, abort, render_template
from werobot.contrib.flask import make_view
from bot import webot, miubot

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.add_url_rule(rule='/wechat',
                 endpoint='/wechat',
                 view_func=make_view(webot),
                 methods=['GET', 'POST'])

app.add_url_rule(rule='/miuchat',
                 endpoint='/miuchat',
                 view_func=make_view(miubot),
                 methods=['GET', 'POST'])

@app.route('/')
def index():
    host = request.url_root
    return render_template('index.html', host=host)

if __name__ == '__main__':
    app.run('127.0.0.1', 8000, debug=True)
