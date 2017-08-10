#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 0:05
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : collection_util_test.py
# @Software: PyCharm
from frame.utils import different_to_list

if __name__ == '__main__':
    # class A(object):
    #     def __init__(self,id,name):
    #         self.id = id
    #         self.name = name
    #
    #     def __str__(self):
    #         return str(self.name)
    #
    # bean_dict = beans_to_dict([A(1,"sa"),A(2,3)],"id")
    # for key in bean_dict:
    #     print key,bean_dict[key]
    print different_to_list(list([1, 2, 3, 45]), list([2, 4, 5, 6]))
