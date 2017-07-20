#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 20:55
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : string_util.py
# @Software: PyCharm

def is_blank(s):
    '''
    判断是否空字符串
    :param s:
    :return:
    '''
    return s == None or len(s) == 0


def is_not_blank(s):
    '''
    判断是否空字符串
    :param s:
    :return:
    '''
    return s == None or len(s) == 0


def join(collection, sp=","):
    '''
    集合转为字符串
    :param collection:
    :param sp:
    :return:
    '''
    res = ""
    for item in collection:
        res += str(item)
    return res


def equals(a, b):
    '''
    敏感字符串比较
    :param a:
    :param b:
    :return:
    '''
    return a == None and b == None or str(a).strip() == str(b).strip()


def equals_ignore_case(a, b):
    '''
    敏感字符串比较
    :param a:
    :param b:
    :return:
    '''
    return a == None and b == None or str(a).lower().strip() == str(b).lower().strip()


def is_digit(num):
    '''
    是否数字
    :param num:
    :return:
    '''
    return str(num).isdigit()


def format(pattern, *args):
    '''
    字符串格式化
    http://blog.csdn.net/handsomekang/article/details/9183303
    :param pattern:
    :param args:
    :return:
    '''
    return str(pattern).format(*args)
