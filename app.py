# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, abort
from werobot.contrib.flask import make_view
from bot import webot, miubot
from wework import wework_send, wework_receive

application = Flask(__name__)
application.add_url_rule(rule='/wechat',
                 endpoint='/wechat',
                 view_func=make_view(webot),
                 methods=['GET', 'POST'])

application.add_url_rule(rule='/miuchat',
                 endpoint='/miuchat',
                 view_func=make_view(miubot),
                 methods=['GET', 'POST'])

application.add_url_rule('/wework/api/u5bs0CnW.send',
                 view_func=wework_send,
                 methods=['GET', 'POST'])

application.add_url_rule('/wework/api/receive',
                 view_func=wework_receive,
                 methods=['GET', 'POST'])

@application.route('/')
def index():
    host = request.url_root
    return render_template('index.html', host=host)


if __name__ == '__main__':
    application.run('0.0.0.0', 8001, debug=True)
