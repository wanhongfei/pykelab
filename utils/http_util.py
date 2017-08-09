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


def post_resp_content(url, values, header={}, is_json_body=False):
    data = None
    if is_json_body:
        header['Content-Type'] = 'application/json'
        data = json.dumps(values)
    else:
        data = urllib.urlencode(values)
    request = urllib2.Request(url, data, {})
    response = urllib2.urlopen(request)
    html = response.read()
    data = json.loads(html)
    return data


def get_resp_content(url):
    '''
    get_resp_content
    '''
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    data = json.loads(html)
    return data
