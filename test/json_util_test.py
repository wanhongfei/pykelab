#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 23:50
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : json_util_test.py
# @Software: PyCharm
from utils.json_util import obj_to_formatting_json

if __name__ == '__main__':
    '''
    test
    '''


    class A(object):
        def __init__(self):
            self.a = 1
            self.b = "2"
            self.c = []


    a = A()

    print obj_to_formatting_json(a)
