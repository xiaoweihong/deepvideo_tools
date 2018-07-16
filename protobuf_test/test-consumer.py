#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 下午6:14
# @Author : xiaowei
# @Site : 
# @File : test.py
# @Software: PyCharm
from kafka import KafkaConsumer
from kafka.structs import TopicPartition

consumer=KafkaConsumer('index-vehicle',bootstrap_servers=[':9078'],auto_offset_reset='earliest')
count=0
for msg in consumer:
    count+=1
    print(count)
    print(msg.value)
#import time
#consumer.subscribe(topics=('index-vehicle'))
#while True:
#    msg = consumer.poll(timeout_ms=5)   #从kafka获取消息
#    print(msg)
#    time.sleep(1)
if __name__=="__main__":
    pass