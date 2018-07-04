#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/4 下午2:35
# @Author : xiaowei
# @Site : 
# @File : test-consumer.py
# @Software: PyCharm
import sys,os
BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from kafka import *
import time
import protobuf_test.genericobj_pb2 as genericobj
import protobuf_test.common_pb2 as commonobj
import protobuf_test.deepdata_pb2 as deepdata
import json
def log(str):
    t = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
    print("[%s]%s" % (t, str))

def getObject(depdata_obj,object):
    bindata=depdata_obj.BinData
    object.ParseFromString(bindata)
    return object

#consumer=KafkaConsumer('index-vehicle',bootstrap_servers=['192.168.6.27:9092'])
consumer=KafkaConsumer('index-vehicle',bootstrap_servers=['39.106.146.155:9092'])

depdata_obj=deepdata.GenericObj()
genericobj=genericobj.NonMotorVehicleObj()
VehicleObj=commonobj.VehicleObj()
srcMetadata=commonobj.SrcMetadata()
pedestrianObj=commonobj.PedestrianObj()

for msg in consumer:
    result="{}:{}:{} key={} value={}".format(msg.topic,msg.partition,msg.offset,msg.key,msg)
    result=msg.value
    depdata_obj.ParseFromString(result)

    if depdata_obj.ObjType==1:
        print(getObject(depdata_obj,VehicleObj))
    #elif depdata_obj.ObjType==2:
    #    print(depdata_obj)
    #elif depdata_obj.ObjType==3:
    #    print(depdata_obj)
    #elif depdata_obj.ObjType==4:
    #    print(depdata_obj)
   #     #log(depdata_obj.FmtType)
   #     temp=depdata_obj.BinData
   #     VehicleObj.ParseFromString(temp)
   #     str=VehicleObj
   #     log(str)
   #     #log(VehicleObj.Metadata.RepoInfo)
   #     #log(srcMetadata.ParseFromString(VehicleObj.Metadata.RepoInfo))
   #     #log(depdata_obj.ListFields())
   #     #log(dir(depdata_obj))

