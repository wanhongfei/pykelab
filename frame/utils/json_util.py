#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 21:13
# @Author  : wanhongfei@bytedance.com
# @Comment : json 序列化工具包
# @File    : json_util.py
# @Software: PyCharm

import json
from datetime import date, datetime

import bean_util


class ComplexEncoder(json.JSONEncoder):
    '''
    处理datetime和date无法json序列化的问题
    '''

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def obj_to_json(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
                allow_nan=True, cls=None, indent=None, separators=None,
                encoding='utf-8', default=None, sort_keys=False):
    '''
    对象序列化为 json
    :param obj:
    :param skipkeys:
    :param ensure_ascii:
    :param check_circular:
    :param allow_nan:
    :param cls:
    :param indent:
    :param separators:
    :param encoding:
    :param default:
    :param sort_keys:
    :return:
    '''
    # 自定义类型无法进行json序列化，先转为dict
    obj = obj if not bean_util.is_custom_type(obj) else bean_util.obj_to_dict(obj)
    # set=>list
    obj = obj if not bean_util.is_set(obj) else list(obj)
    return json.dumps(obj, skipkeys, ensure_ascii,
                      check_circular, allow_nan, cls,
                      indent, separators, encoding,
                      default, sort_keys, cls=ComplexEncoder)


def obj_to_formatting_json(obj):
    '''
    对象序列化为格式化 json
    :param obj:
    :return:
    '''
    print bean_util.is_custom_type(obj)
    obj = obj if not bean_util.is_custom_type(obj) else bean_util.obj_to_dict(obj)
    print obj
    return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))


def json_to_obj(json, type=str):
    '''
    json 字符串转为对象
    :param json:
    :return:
    '''
    return type(json.load(json))
