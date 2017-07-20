#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 22:06
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : encrypt_util_test.py
# @Software: PyCharm
from utils import encrypt_util

if __name__ == '__main__':
    print encrypt_util.encode("hahah", "sha1")
