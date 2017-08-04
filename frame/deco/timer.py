#coding=utf8
#***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
#*************************************************************************/

#
#@file timer.py
#
#@brief timer.py
#
#@author wanhongfei@bytedance.com
#@date   2017-08-04
#@update 2017-08-04
#
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time

def default_callback(func_name,warn_threshold,*argv,**kvargv):
    '''
    默认回调函数
    '''
    pass

def timer(callback=default_callback,warn_threshold=1):
    '''
    运行计时
    '''
    def decorator(func=None):
        '''
        被装饰函数
        '''
        def wrapper(*argv,**kvargv):
            '''
            被装饰函数的参数
            '''
            start_time = time.time()
            data = func(*argv,**kvargv)
            end_time = time.time()
            # 超过设定值进行回调,可记录慢sql 
            if callback and end_time - start_time > warn_threshold:
                callback(func.__name__,warn_threshold,*argv,**kvargv)
            return data
        return wrapper
    return decorator

@timer()
def test(a,b):
    time.sleep(1)
    return a+b

print test(1,2)
