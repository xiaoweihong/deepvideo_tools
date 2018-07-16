#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/27 下午2:12
# @Author : xiaowei
# @Site : 
# @File : task.py
# @Software: PyCharm

import requests
import random
import json
import socket
import argparse
import sys


taskIds = []

__version__ = 'v1.0.0'

hostname=socket.getfqdn(socket.gethostname())
ip=socket.gethostbyname(hostname)

parser=argparse.ArgumentParser(description="this is a simple deepvideo api tool")

parser.add_argument("-f","--file",help="file inside rtsp",default="uri.txt")
parser.add_argument("-ip","--ip",help="kafka ip",default=ip)
parser.add_argument("-p","--port",help="thor port",default=19876)
parser.add_argument("-c","--command",help="api command[lr{list repo},ar{add repo},dr{delete repo},ls{list source},as{add source},ds{delete source},lt{list task},art{add random task},at{add task}c,dt{delete task}onsumer] ",default="lt")
parser.add_argument('-v', '--version', action='version', version='%(prog)s '+__version__)


ip=parser.parse_args().ip
file=parser.parse_args().file
port=parser.parse_args().port
command=parser.parse_args().command

def importer(stream_file="uri.txt"):
    '''
    从文件里获取流地址
    :return: 流地址列表
    '''
    stream_list = []
    with open(stream_file, "r") as f:
        for line in f.readlines():
            stream_list.append(line.strip())
        return stream_list


def list_repo():
    '''
    显示系统里的repo信息并打印
    '''
    url = "http://{}:{}/api/biz/repos?all=true".format(ip, port)
    response = requests.get(url).content
    result = json.loads(response)["Data"]
    print("repo info bellow:")
    for repo in result:
        print(repo["RepoId"], repo["Name"])
    return result[len(result) - 1]["RepoId"]


def add_repo():
    '''
    添加repo
    :return:
    '''
    url = "http://{}:{}/api/biz/addrepo".format(ip, port)
    for i in range(0, len(importer())):
        source = {"Name": "test" + str(i)}
        jsource = json.dumps(source)
        resp = requests.post(url, data=jsource)
        print(resp.status_code)
        print(resp.content)


def delete_repo():
    '''
    删除repo
    :return:
    '''
    for i in range(3, list_repo() + 1):
        url = "http://{}:{}/api/biz/delrepo?id={}".format(ip, port, str(i))
        resp = requests.delete(url)
        print(resp.status_code)
        print(resp.content)

def list_source():
    '''
    显示当前系统的资源
    :return: 返回资源的id
    '''
    source_id = []
    url = "http://{}:{}/api/source".format(ip, port)
    response = json.loads(requests.get(url).content)["Data"]
    for source in response:
        source_id.append(source["id"])
        print(source["id"], source["uri"])
    return source_id


def add_source():
    '''
    添加资源
    :return:
    '''
    url = "http://{}:{}/api/source".format(ip, port)
    urllist = importer()
    for i in range(3, list_repo() + 1):
        for row in urllist:
            sname = str(i)
            source = {"type": 3, "repoId": i, "sensorname": sname, "comment": "1", "uri": row}
            jsource = json.dumps(source)
            resp = requests.post(url, data=jsource)
            print(resp.content)
            i = i + 1
            break


def delete_source():
    '''
    删除资源
    :return:
    '''
    for i in list_source():
        url = "http://{}:{}/api/source?id={}".format(ip, port, i)
        resp = requests.delete(url)
        if resp.status_code == 200:
            print("资源{}-->删除成功".format(i))


def list_task():
    task_id = []
    url = "http://{}:{}/api/task".format(ip, port)
    try:
        response = requests.get(url,timeout=4).content
        task_lists = json.loads(response)["Data"]
        print("*" * 80)
        if len(task_lists) != 0:
            for task in task_lists:
                task_id.append(task["taskId"])
            #print("ID-->", task["taskId"],"source_address-->", task["source"]["uri"],"*", task["renderUri"])
                print("ID", task["taskId"],task["source"]["uri"],"*", task["renderUri"])
            print("*" * 80)
            print("任务数(total)--->", len(task_lists))
            print("*" * 80)
            return task_id
        else:
            print("task list is empty...")
    except requests.exceptions.ConnectTimeout:
        print("网络不正常")
    except requests.exceptions.Timeout:
        print("请求超时")
    except Exception as e:
        print(e)
def add_task_single():
    '''
    随机添加一个任务
    :return:
    '''
    sourceid = random.choice(list_source())
    url = "http://{}:{}/api/task".format(ip, port)
    source = {"name": "任务1", "typeId": 3, "sourceId": sourceid, "detectTypeIds": [2011, 2012, 2013, 2014, 2015],
              "relativePolygonRoi": [{"path": []}],
              "UserConfigMap": {"Threshold/Hotspots/Proportion": "1", "Sys/VehicleSnapshot": "-1"}, "speed": 1}
    jsource = json.dumps(source)
    resp = requests.post(url, data=jsource)
    if resp.status_code == 200:
        print("任务{}-->添加成功".format(sourceid))
        list_task()


def add_task():
    '''
    批量添加任务
    :return:
    '''
    url = "http://{}:{}/api/task".format(ip, port)
    for i in list_source():
        source = {"name": "任务1", "typeId": 3, "sourceId": i, "detectTypeIds": [2011, 2012, 2013, 2014, 2015],
                  "relativePolygonRoi": [{"path": []}],
                  "UserConfigMap": {"Threshold/Hotspots/Proportion": "1", "Sys/VehicleSnapshot": "-1"}, "speed": 1}
        jsource = json.dumps(source)
        resp = requests.post(url, data=jsource)
        if resp.status_code == 200:
            print("任务{}-->添加成功".format(i))

        print(resp.status_code)


def del_task_single():
    '''
    随机删除一个任务
    :return:
    '''
    taskId=random.choice(list_task())
    url = "http://%s:%s/api/task?id=%d" % (ip, port, taskId)
    resp = requests.delete(url)
    if resp.status_code == 200:
       print("任务{}-->删除成功".format(taskId))


def del_task():
    '''
    删除任务
    :return:
    '''
    for i in list_task():
        url = "http://%s:%s/api/task?id=%d" % (ip, port, i)
        resp = requests.delete(url)
        if resp.status_code == 200:
            print("任务{}-->删除成功".format(i))


def usage():
    print ("Usage: \n",\
          "-h,--help (show help on all flags [tip: all flags can have two dashes])\n",\
          "--ip (matrix ip,defult:local ip)\n",\
          "--port (thor port,defult:19876)\n",\
          "-f --file (file inside rtsp)\n",\
          "-c --command (default lt)\n")


if len(sys.argv)==1:
    usage()
    sys.exit(1)

if command == "lr":
    list_repo()
elif command == "ar":
    add_repo()
elif command == "dr":
    delete_repo()
elif command == "ls":
    list_source()
elif command == "as":
    add_source()
elif command == "ds":
    delete_source()
elif command == "lt":
    list_task()
elif command == "ats":
    add_task_single()
elif command == "at":
    add_task()
elif command == "dt":
    del_task()
elif command == "dts":
    del_task_single()
else:
    print(">>>>>>>>>>>命令参数不正确<<<<<<<<<<<<<<")



    # print(importer())
    # list_repo()
    # add_repo()
    # delete_repo()
    #list_task()
     #add_source()
    #list_source()
    #delete_source()
    # delete_source()
     #add_task_single()
     #add_task()

    #del_task()
     #list_task()


