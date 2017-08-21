# coding=utf8
# ***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
# *************************************************************************/

#
# @file common.py
#
# @brief common.py
#
# @author wanhongfei@bytedance.com
# @date   2017-08-06
# @update 2017-08-06
#
#
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from frame.utils.json_util import json_to_obj
from frame.utils.collection_util import get_param


def get_req_param(request, param_name, default=None, type=str):
    '''
    get param value of request(get & post)
    '''
    value = get_param(request.REQUEST, param_name, default, type)
    if value:
        return value
    elif request.raw_post_data:
        data = json_to_obj(request.raw_post_data)
        if data.get(param_name):
            return type(data.get(param_name))
    else:
        return default


def get_session(request, key, default=None):
    '''
    get value from session by key
    :param request:
    :param key:
    :return:
    '''
    return get_param(request.session, key, default, None)


def set_session(request, key, value):
    '''
    set value into session
    :param request:
    :param key:
    :param value:
    :return:
    '''
    request.session[key] = value


def set_session(request, kv):
    '''
    set value into session
    :param request:
    :param key:
    :param value:
    :return:
    '''
    request.session.update(kv)


def set_session_expiry(request, value):
    '''
    ==> session默认在服务器端保存15天.

    1.如果value是个整数，session会在些秒数后失效。
    2.如果value是个datatime或timedelta，session就会在这个时间后失效。
    3.如果value是0, 用户关闭浏览器session就会失效。
    4.如果value是None, session会依赖全局session失效策略。
    :param value:
    :return:
    '''
    request.session.set_expiry(value)


def set_cookie(request, key, value):
    '''
    设置cookie
    :param request:
    :param key:
    :param value:
    :return:
    '''
    request.set_cookie(key, value)


def set_cookie(request, kv):
    '''
    设置cookie
    :param request:
    :param key:
    :param value:
    :return:
    '''
    for k, v in kv:
        request.set_cookie(k, v)


def get_cookie(request, key, default=None):
    '''
    获取cookie
    :param request:
    :param key:
    :return:
    '''
    return get_param(request.COOKIES, key, default, None)


def get_client_ip(request):
    '''
    获取客户端ip
    :param request:
    :return:
    '''
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']


def get_method(request):
    '''
    获取请求方法
    :param request:
    :return:
    '''
    return request.method


def get_url(request):
    '''
    获取请求url
    :param request:
    :return:
    '''
    return request.META['QUERY_STRING']


def get_user_agent(request):
    '''
    获取user——agent
    :param request:
    :return:
    '''
    return request.META['HTTP_USER_AGENT']


def post_json_data(request):
    '''
    将postbody中的原生字符串转为json
    :param request:
    :return:
    '''
    return json_to_obj(request.raw_post_data)


def get_path(request):
    '''
    请求路径/data/stream/xxx/yy
    :param request:
    :return:
    '''
    return request.path
