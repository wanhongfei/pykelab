#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 21:47
# @Author  : wanhongfei@bytedance.com
# @Comment : 基本类型转换工具包
# @File    : bean_util.py
# @Software: PyCharm
import types

PUBLIC_PROTECTED_PRIVATE_LEVEL = 0
PUBLIC_PROTECTED_LEVEL = 1
PUBLIC_LEVEL = 2

PRIVATE_PREFIX = "__"
PROTECTED_PREFIX = "_"


def obj_to_dict(obj, level=PUBLIC_PROTECTED_PRIVATE_LEVEL):
    '''
    对象转字典
    :param obj:
    :param level：0=>public+protected+private 1=>public+protected 2=>public
    :return:
    '''
    class_name = obj.__class__.__name__
    private_prefix = "_" + class_name
    bean_dict = obj.__dict__
    res = {}
    for key in bean_dict:
        value = bean_dict.get(key)
        key = str(key).replace(private_prefix, "");
        if level == PUBLIC_LEVEL and key.startswith(PROTECTED_PREFIX):
            continue
        if level == PUBLIC_PROTECTED_LEVEL and key.startswith(PRIVATE_PREFIX):
            continue
        if value and is_custom_type(value):
            value = obj_to_dict(value)
        res[key] = value
    return res


def is_custom_type(obj):
    '''
    判断是否自定义类型
    :param obj:
    :return:
    '''
    return (type(obj) is types.InstanceType) \
           or not (is_dict(obj) or is_tuple(obj) or is_list(obj) or is_slice(obj) or
                   is_set(obj) or is_int(obj) or is_long(obj) or is_float(obj) or is_string(obj))


def is_dict(obj):
    '''
    判断是否是字典
    :param obj:
    :return:
    '''
    return isinstance(obj, dict)


def is_set(obj):
    '''
    判断是否是集合
    :param obj:
    :return:
    '''
    return isinstance(obj, set)


def is_tuple(obj):
    '''
    判断是否元组
    :param obj:
    :return:
    '''
    return isinstance(obj, tuple)


def is_list(obj):
    '''
    判断是否列表
    :param obj:
    :return:
    '''
    return isinstance(obj, list)


def is_slice(obj):
    '''
    判断是否列表
    :param obj:
    :return:
    '''
    return isinstance(obj, slice)


def is_int(obj):
    '''
    判断是否整形
    :param obj:
    :return:
    '''
    return isinstance(obj, int)


def is_long(obj):
    '''
    判断是否长整形
    :param obj:
    :return:
    '''
    return isinstance(obj, long)


def is_float(obj):
    '''
    判断是否浮点型
    :param obj:
    :return:
    '''
    return isinstance(obj, float)


def is_string(obj):
    '''
    判断是否字符串
    :param obj:
    :return:
    '''
    return isinstance(obj, str)


def get_attr(obj, field_name):
    '''
    反射获取属性值
    :param obj:
    :param field_name:
    :return:
    '''
    return getattr(obj, field_name)


def set_attr(obj, field_name, value):
    '''
    反射获取属性值
    :param obj:
    :param field_name:
    :return:
    '''
    set_attr(obj, field_name, value)


def has_attr(obj, field_name):
    '''
    检测是否有指定属性
    :param obj:
    :param field_name:
    :return:
    '''
    return has_attr(obj, field_name)
