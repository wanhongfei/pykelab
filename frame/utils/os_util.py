#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 11:55
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : os_util.py
# @Software: PyCharm
import os


def get_file_extension(filepath):
    '''
    获取文件扩展名
    :param filepath:
    :return:
    '''
    return os.path.splitext(filepath)[1]
