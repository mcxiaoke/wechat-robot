# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals
import os
import logging

from flask import Flask, request, abort, render_template
from werobot.contrib.flask import  make_view
from robot import robot
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import (
    InvalidSignatureException,
    InvalidAppIdException,
)

# set token or get from environments
# TOKEN = os.getenv('WECHAT_TOKEN', '123456')
# AES_KEY = os.getenv('WECHAT_AES_KEY', '')
# APPID = os.getenv('WECHAT_APPID', '')

from config import WECHAT_TOKEN as TOKEN
from config import WECHAT_AES_KEY as AES_KEY
from config import WECHAT_APPID as APPID

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.add_url_rule(rule='/wechat',
                 endpoint='/',
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])

@app.route('/')
def index():
    host = request.url_root
    return render_template('index.html', host=host)


#@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    encrypt_type = request.args.get('encrypt_type', 'raw')
    msg_signature = request.args.get('msg_signature', '')
    logging.warning(signature)
    logging.warning(timestamp)
    logging.warning(nonce)
    logging.warning(encrypt_type)
    logging.warning(msg_signature)
    logging.warning(request.args.get('echostr', ''))
    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException as e:
        logging.error(e)
        abort(403)
    if request.method == 'GET':
        echo_str = request.args.get('echostr', '')
        return echo_str

    # POST request
    if encrypt_type == 'raw':
        # plaintext mode
        msg = parse_message(request.data)
        if msg.type == 'text':
            reply = create_reply(msg.content, msg)
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        return reply.render()
    else:
        # encryption mode
        from wechatpy.crypto import WeChatCrypto

        crypto = WeChatCrypto(TOKEN, AES_KEY, APPID)
        try:
            msg = crypto.decrypt_message(
                request.data,
                msg_signature,
                timestamp,
                nonce
            )
        except (InvalidSignatureException, InvalidAppIdException):
            abort(403)
        else:
            msg = parse_message(msg)
            if msg.type == 'text':
                reply = create_reply(msg.content, msg)
            else:
                reply = create_reply('Sorry, can not handle this for now', msg)
            return crypto.encrypt_message(reply.render(), nonce, timestamp)


if __name__ == '__main__':
    app.run('127.0.0.1', 8000, debug=True)
