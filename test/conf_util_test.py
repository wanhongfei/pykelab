#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 11:14
# @Author  : wanhongfei@bytedance.com
# @Comment :
# @File    : conf_util_test.py
# @Software: PyCharm
import os

from frame.utils import conf_util

if __name__ == '__main__':
    print conf_util.conf(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.conf"), "dev")
