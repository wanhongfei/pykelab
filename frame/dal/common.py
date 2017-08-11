#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 11:13
# @Author  : wanhongfei@bytedance.com
# @Comment : dict与model互转
# @File    : upload.py
# @Software: PyCharm

from django.forms.models import model_to_dict

model_to_dict = model_to_dict


def dict_to_model(dict_kv, model_type):
    '''
    字典转model
    :param dict_kv:
    :param model_type:
    :return:
    '''
    id = dict_kv.get('id')
    obj = None
    if id:
        obj = model_type.objects.get(id=id)
    else:
        obj = model_type.objects.create()
    for k, v in dict_kv.items():
        if hasattr(obj, k):
            setattr(obj, k, v)
    return obj
