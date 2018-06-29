#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 下午6:14
# @Author : xiaowei
# @Site : 
# @File : test.py
# @Software: PyCharm
from kafka import KafkaConsumer
from kafka.structs import TopicPartition

consumer=KafkaConsumer('index-vehicle',bootstrap_servers=['192.168.6.27:9092'])

print(consumer.partitions_for_topic('index-vehicle'))
#print(consumer.beginning_offsets(consumer.assignment()))
print(consumer.topics())
