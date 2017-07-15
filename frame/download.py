#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 11:01
# @Author  : wanhongfei@bytedance.com
# @Comment : 下载文件
# @File    : download.py
# @Software: PyCharm
from django.http import StreamingHttpResponse


def get_download_stream_response(download_filepath, dialog_download_filename, buff_size=512):
    '''
    利用缓冲下载大文件+解决乱码问题
    :param download_filepath:
    :param dialog_download_filename:
    :param buff_size:
    :return:
    '''

    def file_iterator(file_name, chunk_size):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(download_filepath, buff_size))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(dialog_download_filename)
    return response
