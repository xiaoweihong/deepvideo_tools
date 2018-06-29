#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 下午2:20
# @Author : xiaowei
# @Site : 
# @File : test-producer.py
# @Software: PyCharm
from kafka import *
import time


producer=KafkaProducer(bootstrap_servers='192.168.2.33:9092')


def log(str):
    t = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
    print("[%s]%s" % (t, str))

count=0
while True:
    producer.send('xiaowei','晓威-{}'.format(count).encode('utf-8'))
    count+=1
    producer.flush()

producer.close()
