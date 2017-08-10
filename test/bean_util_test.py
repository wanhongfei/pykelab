#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 23:49
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : bean_util_test.py
# @Software: PyCharm
from frame.utils import is_custom_type, obj_to_dict, PUBLIC_PROTECTED_LEVEL

if __name__ == '__main__':
    '''
    test
    '''


    class A(object):
        def __init__(self):
            self.a = 1
            self.b = "2"
            self.c = []
            self._d = "dasd"
            self.__e = B()


    class B:
        def __init__(self):
            self.sa = "sda"


    a = A()
    print is_custom_type(a)
    print is_custom_type(B())
    print obj_to_dict(a, PUBLIC_PROTECTED_LEVEL)
