IPPOOL = [ ]

# -*- coding: UTF-8 -*-
'''
Python 3.x
无忧代理IP Created on 2018年07月11日
描述：本段代码定时从无忧代理API接口获取代理IP，存入IP池中
@author: www.data5u.com
'''
import requests;
import time;
import threading;


# 获取代理IP的线程类
class GetIpThread(threading.Thread):
    def __init__(self,apiUrl, fetchSecond):
        super(GetIpThread, self).__init__();
        self.fetchSecond=fetchSecond;
        self.apiUrl=apiUrl;
    def run(self):
        while True:
            # 获取IP列表
            res = requests.get(self.apiUrl).content.decode()
            print(res)
            # 按照\n分割获取到的IP
            global IPPOOL
            IPPOOL = [res.split('\n')[0]];
            # print(data5u.IPPOOL)
            # 休眠
            time.sleep(self.fetchSecond);

if __name__ == '__main__':
    # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
    order = "598c89eed90af9ca23a0e17a33362ac8";
    # 获取IP的API接口
    apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order;
    # 获取IP时间间隔，建议为5秒
    fetchSecond = 5;
    # 开始自动获取IP
    GetIpThread(apiUrl, fetchSecond).start();