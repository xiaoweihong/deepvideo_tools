#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/13 下午3:04
# @Author : xiaowei
# @Site : 
# @File : kafka_tools.py
# @Software: PyCharm

import argparse
import socket
from kafka import KafkaConsumer


__version__ = 'v1.0.0'

hostname=socket.getfqdn(socket.gethostname())
ip=socket.gethostbyname(hostname)

parser=argparse.ArgumentParser(description="this is a simple kafka tool")

parser.add_argument("-t","--topic",help="topic name",default="index-vehicle")
parser.add_argument("-c","--command",help="kafka command[list,consumer] ",default="list")
parser.add_argument("-ip","--ip",help="kafka ip",default=ip)
parser.add_argument("-p","--port",help="kafka port",default=9092)
parser.add_argument('-v', '--version', action='version', version='%(prog)s '+__version__)

topic=parser.parse_args().topic
command=parser.parse_args().command
ip=parser.parse_args().ip
port=parser.parse_args().port
consumer=None
try:
    consumer=KafkaConsumer(topic,request_timeout_ms=3500,bootstrap_servers=["{}:{}".format(ip,port)])
except Exception as e :
    print(">>>>>>>>>>>please check kafka config ip>>>>>>>>>>>>>")
    exit(400)


def list_topic():
    topic_list=consumer.topics()

    return topic_list


def consumer_topic():
    if consumer is not None:
        for message in consumer:
            print(message)
    else:
        print("consumer")


if command=="list":
    print(list_topic())
elif command=="consumer":
    consumer_topic()
else:
    print(list_topic())

