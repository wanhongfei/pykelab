# coding=utf8
# ***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
# *************************************************************************/

#
# @file timer.py
#
# @brief timer.py
#
# @author wanhongfei@bytedance.com
# @date   2017-08-04
# @update 2017-08-04
#
#
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def cros_domain(allow_host="*", allow_method="GET,POST,PUT,DELETE,OPTION", allow_headers="*", max_age=1000):
    '''
    跨域
    '''

    def decorator(func=None):
        '''
        被装饰函数
        '''

        def wrapper(*argv, **kvargv):
            '''
            被装饰函数的参数
            '''
            response = func(*argv, **kvargv)
            response["Access-Control-Allow-Origin"] = allow_host
            response["Access-Control-Allow-Methods"] = allow_method
            response["Access-Control-Max-Age"] = max_age
            response["Access-Control-Allow-Headers"] = allow_headers
            return response
        return wrapper
    return decorator