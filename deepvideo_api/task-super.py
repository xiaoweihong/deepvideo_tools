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



class task_run():

    def __init__(self):
        self.taskIds = []
        self.__version__ = 'v1.0.0'
        self.hostname=socket.getfqdn(socket.gethostname())
        self.ip=socket.gethostbyname(self.hostname)


    def arge_parse(self):
        '''
        从命令行获取参数
        :return:
        '''
        parser=argparse.ArgumentParser(description="this is a simple deepvideo api tool")
        parser.add_argument("-f","--file",help="file inside rtsp",default="uri.txt")
        parser.add_argument("-ip","--ip",help="kafka ip",default=self.ip)
        parser.add_argument("-p","--port",help="thor port",default=19876)
        parser.add_argument("-c","--command",help="api command[lr{list repo},ar{add repo},dr{delete repo},ls{list source},as{add source},ds{delete source},lt{list task},art{add random task},at{add task}c,dt{delete task}onsumer] ",default="lt")
        parser.add_argument('-v', '--version', action='version', version='%(prog)s '+self.__version__)

        return parser.parse_args()


    def importer(self,stream_file="uri.txt"):
        '''
        从文件里获取流地址
        :return: 流地址列表
        '''
        stream_list = []
        with open(stream_file, "r") as f:
            for line in f.readlines():
                stream_list.append(line.strip())
            return stream_list


    def list_repo(self,ip,port):
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


    def add_repo(self,ip,port):
        '''
        添加repo
        :return:
        '''
        url = "http://{}:{}/api/biz/addrepo".format(ip, port)
        for i in range(0, len(self.importer())):
            source = {"Name": "test" + str(i)}
            jsource = json.dumps(source)
            resp = requests.post(url, data=jsource)
            print(resp.status_code)
            print(resp.content)


    def delete_repo(self,ip,port):
        '''
        删除repo
        :return:
        '''
        for i in range(3, self.list_repo() + 1):
            url = "http://{}:{}/api/biz/delrepo?id={}".format(ip, port, str(i))
            resp = requests.delete(url)
            print(resp.status_code)
            print(resp.content)

    def list_source(self,ip,port):
        '''
        显示当前系统的资源
        :return: 返回资源的id
        '''
        source_id = []
        url = "http://{}:{}/api/source".format(ip, port)
        response = json.loads(requests.get(url).content)["Data"]
        print("资源列表如下:")
        print("*" * 80)
        for source in response:
            source_id.append(source["id"])
            print(source["id"], source["uri"])
        print("*" * 80)
        return source_id


    def add_source(self,ip,port):
        '''
        添加资源
        :return:
        '''
        url = "http://{}:{}/api/source".format(ip, port)
        urllist = self.importer()
        for i in range(3, self.list_repo(ip,port) + 1):
            for row in urllist:
                sname = str(i)
                source = {"type": 3, "repoId": i, "sensorname": sname, "comment": "1", "uri": row}
                jsource = json.dumps(source)
                resp = requests.post(url, data=jsource)
                print(resp.content)
                i = i + 1
                break


    def delete_source(self,ip,port):
        '''
        删除资源
        :return:
        '''
        for i in self.list_source(ip,port):
            url = "http://{}:{}/api/source?id={}".format(ip, port, i)
            resp = requests.delete(url)
            if resp.status_code == 200:
                print("资源{}-->删除成功".format(i))


    def list_task(self,ip,port):
        '''
        显示任务列表
        :param ip: 服务器ip
        :param port: 服务器端口
        :return: 返回任务列表id
        '''
        task_id = []
        url = "http://{}:{}/api/task".format(ip, port)
        try:
            response = requests.get(url,timeout=4).content
            task_lists = json.loads(response)["Data"]
            print("*" * 80)
            if len(task_lists) != 0:
                for task in task_lists:
                    task_id.append(task["taskId"])
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


    def add_task_single(self,ip,port):
        '''
        随机添加一个任务
        :return:
        '''
        sourceid = random.choice(self.list_source(ip,port))
        url = "http://{}:{}/api/task".format(ip, port)
        source = {"name": "任务1", "typeId": 3, "sourceId": sourceid, "detectTypeIds": [2011, 2012, 2013, 2014, 2015],
                  "relativePolygonRoi": [{"path": []}],
                  "UserConfigMap": {"Threshold/Hotspots/Proportion": "1", "Sys/VehicleSnapshot": "-1"}, "speed": 1}
        jsource = json.dumps(source)
        resp = requests.post(url, data=jsource)
        if resp.status_code == 200:
            print("任务{}-->添加成功".format(sourceid))
            self.list_task(ip,port)


    def add_task(self,ip,port):
        '''
        批量添加任务
        :return:
        '''
        url = "http://{}:{}/api/task".format(ip, port)
        for i in self.list_source(ip,port):
            source = {"name": "任务1", "typeId": 3, "sourceId": i, "detectTypeIds": [2011, 2012, 2013, 2014, 2015],
                      "relativePolygonRoi": [{"path": []}],
                      "UserConfigMap": {"Threshold/Hotspots/Proportion": "1", "Sys/VehicleSnapshot": "-1"}, "speed": 1}
            jsource = json.dumps(source)
            resp = requests.post(url, data=jsource)
            if resp.status_code == 200:
                print("任务{}-->添加成功".format(i))

            print(resp.status_code)


    def del_task_single(self,ip,port):
        '''
        随机删除一个任务
        :return:
        '''
        taskId=random.choice(self.list_task())
        url = "http://%s:%s/api/task?id=%d" % (ip, port, taskId)
        resp = requests.delete(url)
        if resp.status_code == 200:
           print("任务{}-->删除成功".format(taskId))


    def del_task(self,ip,port):
        '''
        删除任务
        :return:
        '''
        task_list=self.list_task(ip,port)
        if task_list:
            for i in self.list_task(ip,port):
                url = "http://%s:%s/api/task?id=%d" % (ip, port, i)
                resp = requests.delete(url)
                if resp.status_code == 200:
                    print("任务{}-->删除成功".format(i))



    def usage(self):
        '''
        使用说明
        :return:
        '''
        ip=self.arge_parse().ip
        file=self.arge_parse().file
        port=self.arge_parse().port

        if hasattr(self,self.arge_parse().command):
            func=getattr(self,self.arge_parse().command)
            func(ip,port)
        else:
            print("Usage: \n", \
                  "-h,--help (show help on all flags [tip: all flags can have two dashes])\n", \
                  "--ip (matrix ip,defult:local ip)\n", \
                  "--port (thor port,defult:19876)\n", \
                  "-f --file has(file inside rtsp)\n", \
                  "-c --command\n"
                  "\t list_repo\n"
                  "\t add_repo\n"
                  "\t delete_repo\n"
                  "\t list_source\n"
                  "\t add_source\n"
                  "\t delete_source\n"
                  "\t add_task\n"
                  "\t add_task_single\n"
                  "\t del_task_single\n"
                  "\t del_task"
                  )


if __name__ == '__main__':
    t=task_run()
    t.usage()
