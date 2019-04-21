# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test.py  
   Description :  
   Author :       JHao
   date：          2017/3/7
-------------------------------------------------
   Change Activity:
                   2017/3/7: 
-------------------------------------------------
"""
__author__ = 'JHao'

from Test import testConfig
from Api import ProxyApi
if __name__ == '__main__':
    # testConfig.testConfig()
    for i in range(100):
        print(ProxyApi.get())
