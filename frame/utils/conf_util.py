#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 11:09
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : conf_util.py
# @Software: PyCharm
import ConfigParser


def conf(filepath, sec=None):
    '''
    读取配置文件
    :param file:
    :return:
    '''
    cf = ConfigParser.SafeConfigParser()
    cf.read(filepath)
    ret = {}
    if sec == None:
        for sec in cf.sections():
            tmp = {}
            for item in cf.items(sec):
                tmp[item[0]] = item[1]
            ret.update({sec: tmp})
    else:
        for item in cf.items(sec):
            ret[item[0]] = item[1]
    return ret
