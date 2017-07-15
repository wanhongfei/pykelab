#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 11:13
# @Author  : wanhongfei@bytedance.com
# @Comment : 上传文件
# @File    : upload.py
# @Software: PyCharm
import os

from django.http import HttpRequest


def upload_file_to_local(request, vars=[], upload_dir="tmp"):
    '''
    将上传文件放至本地
    上传文件外部函数要带注解：@csrf_exempt
    :param raw_request:
    :return:
    '''
    if isinstance(request, HttpRequest) and request.method == "POST":
        res = {}
        for var in vars:
            print var
            my_file = request.FILES.get(var, None)  # 获取上传的文件，如果没有文件，则默认为None
            if not my_file:
                raise Exception("no file to be upload")
            else:
                print my_file
            if not os.path.isdir(upload_dir):
                os.makedirs(upload_dir)
            filepath = os.path.join(upload_dir, my_file.name)
            res[var] = filepath
            destination = open(filepath, 'wb+')  # 打开特定的文件进行二进制的写操作
            try:
                for chunk in my_file.chunks():  # 分块写入文件
                    destination.write(chunk)
                return res
            except Exception, ex:
                raise Exception("write file failed", ex)
            finally:
                destination.flush()
                destination.close()
    else:
        raise Exception("request error")
