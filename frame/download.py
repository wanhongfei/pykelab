#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 11:01
# @Author  : wanhongfei@bytedance.com
# @Comment : 下载文件
# @File    : download.py
# @Software: PyCharm

from django.http import StreamingHttpResponse

from utils.os_util import get_file_extension

DEFAULT_CONTENT_TYPE = "text/plain"
EXT_TO_CONTENT_TYPE = {
    "txt": "text/plain",
    # picture
    "gif": "image/gif",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "jpg": "image/jpeg",
    # office
    "doc": "application/msword",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "xls": "application/vnd.ms-excel",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "ppt": "application/vnd.ms-powerpoint",
    "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    # pdf
    "pdf": "application/pdf",
    # compress
    "zip": "application/zip",
    # music and vidio
    "avi": "video/avi",
    "mp4": "video/mpeg4",
}


def get_download_stream_response(download_filepath, dialog_download_filename, buff_size=512):
    '''
    利用缓冲下载大文件+解决乱码问题
    :param download_filepath:
    :param dialog_download_filename:
    :param buff_size:
    :return:
    '''
    ext = get_file_extension(dialog_download_filename).lower()
    content_type = EXT_TO_CONTENT_TYPE.get(ext, DEFAULT_CONTENT_TYPE)

    def file_iterator(file_name, chunk_size):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(download_filepath, buff_size))
    response['Content-Type'] = content_type
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(dialog_download_filename)
    return response
