# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from config import MQTT_SERVER, MQTT_PORT, MQTT_USER, MQTT_PASS
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('mqtt')


def sendMessage(topic, payload):
    try:
        publish.single(topic, payload, hostname=MQTT_SERVER,
                       port=MQTT_PORT, client_id="wechat_robot_%d" % int(datetime.now().timestamp()), auth={
                           'username': MQTT_USER, 'password': MQTT_PASS
                       })
        logger.info(
            'sendMessage ok: topic:[%s], payload:[%s]' % (topic, payload))
        return True
    except Exception as e:
        logger.warning(
            'sendMessage failed: topic:[%s], payload:[%s], error:%s' % (topic, payload, e))
        return False


def sendCommand(command):
    return sendMessage('device/cmd', command)


def forwardSMS(phoneNo, text):
    return sendMessage('sms/receive', '%s (%s)', text, phoneNo)


if __name__ == "__main__":
    sendMessage('test/hello', 'hello world from paho publish ts:%d' %
                int(datetime.now().timestamp()))
    sendCommand('/help')
