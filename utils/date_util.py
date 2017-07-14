#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 8:20
# @Author  : wanhongfei@bytedance.com
# @Comment : 日期工具类
# @File    : date_util.py
# @Software: PyCharm

import time

from dateutil import parser

DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_timestamp():
    '''
    获取时间戳
    :return:
    '''
    return long(time.time())


def string_to_timestamp(str):
    '''
    将字符串转为时间戳:
    2013-08-02
    20130802
    2013/08/03
    :param str:
    :return:
    '''
    cur_datetime = parser.parse(str)
    cur_timestamp = datetime_to_timestamp(cur_datetime)
    return long(cur_timestamp)


def timestamp_to_string(timestamp, pattern=DEFAULT_TIME_FORMAT):
    '''
    将时间戳转为字符串
    2013-08-02
    20130802
    2013/08/03
    :param str:
    :return:
    '''
    struct_time = timestamp_to_struct_time(timestamp)
    return time.strftime(pattern, struct_time)


def timestamp_to_struct_time(timestamp):
    '''
    将时间戳转为tuple
    time.struct_time(tm_year=2013, tm_mon=12, tm_mday=13, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=347, tm_isdst=0)
    :param timestamp:
    :return:
    '''
    return time.localtime(timestamp)


def struct_time_to_timestamp(time_tuple):
    '''
    将tuple转为时间戳
    :param time_tuple:
    :return:
    '''
    return long(time.mktime(time_tuple))


def datetime_to_timestamp(date_time):
    '''
    datetime 转为时间戳
    :param date_time:
    :return:
    '''
    return time.mktime(date_time.timetuple())
