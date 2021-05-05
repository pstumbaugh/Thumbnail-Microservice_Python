#!/usr/bin/env python
import pika
import sys
import os
import certifi
import urllib.request as urlrq
import ssl
from urllib.request import urlretrieve
from PIL import Image

url = os.environ.get(
    "CLOUDAMQP_URL", 'amqps://arjploml:xDkV7ZyHtHsuU0vgz5p6Zej8SCnKtst1@beaver.rmq.cloudamqp.com/arjploml')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.exchange_declare('test_exchange')

channel.queue_declare(queue='test_queue')

channel.queue_bind('test_queue', 'test_exchange', 'tests')

channel.basic_publish(
    body='Hello RabbitMQ!',
    exchange='test_exchange',
    routing_key='tests'
)
print(' Message Sent ')
channel.close()
connection.close()
