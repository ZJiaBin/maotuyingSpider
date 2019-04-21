# -*- coding: UTF-8 -*-
'''
Python 3.x
无忧代理IP Created on 2018年07月11日
描述：本段代码是Scrapy的下载中间件，用于模拟UserAgent
@author: www.data5u.com
'''
# 导入随机模块
import random
# 导入settings文件中的UAPOOL
from settings import UAPOOL
# 导入官方文档对应的HttpProxyMiddleware
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    # 初始化 注意一定要user_agent，不然容易报错
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    # 请求处理
    def process_request(self, request, spider):
        # 先随机选择一个用户代理
        thisua = random.choice(UAPOOL)
        print("当前使用User-Agent是："+thisua)
        request.headers.setdefault('User-Agent',thisua)
