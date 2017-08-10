#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 21:13
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : string_util_test.py
# @Software: PyCharm
from frame.utils import string_util

if __name__ == '__main__':
    print string_util.format("{}+{}={}", 1, 2, 3)
    print string_util.cast("1", float)
