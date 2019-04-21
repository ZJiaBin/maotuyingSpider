# -*- coding: UTF-8 -*-
'''
Python 3.x
无忧代理IP Created on 2018年07月11日
描述：本段代码是Scrapy的代理中间件，用于设置代理IP
@author: www.data5u.com
'''
# 导入随机模块
import random
# 导入data5u文件中的IPPOOL
import getIp
# 导入官方文档对应的HttpProxyMiddleware

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class IPPOOlS(HttpProxyMiddleware):

    def __init__(self, ip=''):
        self.ip = ip
    def process_request(self, request, spider):
        thisip = getIp.getRandomIp()
        print("当前使用IP是：" + thisip)
        request.meta["proxy"] = "http://" + thisip

