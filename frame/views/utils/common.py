#coding=utf8
#***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
#*************************************************************************/

#
#@file common.py
#
#@brief common.py
#
#@author wanhongfei@bytedance.com
#@date   2017-08-06
#@update 2017-08-06
#
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_param(request,param_name,default=None):
    '''
    get param value of request(get & post)
    '''
    if request.REQUEST.get('param_name'):
        return str(request.REQUEST.get('param_name'))
    else:
        return default
    
