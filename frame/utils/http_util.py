#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 21:13
# @Author  : wanhongfei@bytedance.com
# @Comment : json 序列化工具包
# @File    : json_util.py
# @Software: PyCharm

import json
import urllib
import urllib2


def post_json_resp(url, values, header={}, is_json_body=False):
    '''
    post json resp
    :param url:
    :param values:
    :param header:
    :param is_json_body:
    :return:
    '''
    data = None
    if is_json_body:
        header['Content-Type'] = 'application/json'
        data = json.dumps(values)
    else:
        data = urllib.urlencode(values)
        header['Content-Type'] = 'application/x-www-form-urlencoded'
    request = urllib2.Request(url, data, {})
    response = urllib2.urlopen(request)
    html = response.read()
    return json.loads(html)


def get_json_resp(url):
    '''
    get_resp_content
    '''
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    data = json.loads(html)
    return data
