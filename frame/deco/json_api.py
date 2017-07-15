#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 12:13
# @Author  : wanhongfei@bytedance.com
# @Comment : 将函数返回对象转为json
# @File    : api.py
# @Software: PyCharm
from django.http import HttpResponse

from utils import json_util


def json_api(func):
    '''
    使用于view的函数中，会将返回的结果转为json返回前端
    :param func:
    :return:
    '''

    def wrapper(request, *args, **kwargs):
        ret = func(request, *args, **kwargs)
        return HttpResponse(json_util.obj_to_json(ret))

    return wrapper
