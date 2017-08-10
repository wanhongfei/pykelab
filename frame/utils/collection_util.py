#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 0:01
# @Author  : wanhongfei@bytedance.com
# @Comment : 集合工具类
# @File    : collection_util.py
# @Software: PyCharm

def get_param(obj, para_name, default=None, type=None):
    '''
    获取参数
    :param obj:
    :param para_name:
    :param default:
    :param type:
    :return:
    '''
    value = obj.get(para_name)
    if value:
        return value if not type else type(value)
    else:
        return default


def is_empty(items):
    '''
    判空
    :param items:
    :return:
    '''
    if items:
        # False,0,'',[],{},() 都视为False
        return False
    else:
        return True


def str_to_str_list(s, seperator=","):
    '''
    将字符串分割为字符串数组
    :param s:
    :param sep:
    :return:
    '''
    return list(str(s).split(seperator))


def str_to_int_list(s, seperator=","):
    '''
    将字符串分割为字符串数组
    :param s:
    :param sep:
    :return:
    '''
    slist = str_to_str_list(s, seperator)
    res = []
    for item in slist:
        res.append(int(item))
    return res


def beans_to_dict(list, fieldName):
    '''
    list相关属性和自身组成dict
    :param list:
    :param fieldName:
    :return:
    '''
    res = {}
    for item in list:
        key = getattr(item, fieldName)
        value = item
        res[key] = value
    return res


def make_list(*args):
    '''
    组装数组
    :param args:
    :return:
    '''
    return list(args)


def list_duplicate(src_list):
    '''
    数组去重
    :param src_list:
    :return:
    '''
    return list(set(src_list))


def combine_to_list(a, b):
    '''
    数组并集
    :param a:
    :param b:
    :return:
    '''
    return list(set(a).union(set(b)))


def different_to_list(a, b):
    '''
    数组求差集，存在与a而不存于b
    :param a:
    :param b:
    :return:
    '''
    return list(set(a).difference(set(b)))


def intersection_to_list(a, b):
    '''
    数组求交集
    :param a:
    :param b:
    :return:
    '''
    return list(set(a).intersection(set(b)))
