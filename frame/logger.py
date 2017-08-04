#coding=utf8
#***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
#*************************************************************************/

#
#@file logging.py
#
#@brief logging.py
#
#@author wanhongfei@bytedance.com
#@date   2017-08-04
#@update 2017-08-04
#
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging
from logging.handlers import TimedRotatingFileHandler

default_log_file_name = 'app.log'
default_log_level = logging.INFO
default_enable_console = True
default_log_format = '[%(levelname)s][%(asctime)s]:文件名%(filename)s-第%(lineno)d行-[错误信息%(message)s]'
default_date_format = '%Y-%m-%d %H:%M:%S'

# error 文件输出默认配置
wfHandler = TimedRotatingFileHandler(default_log_file_name+".wf", when="midnight")
formatter = logging.Formatter(default_log_format)
wfHandler.setFormatter(formatter)
wfHandler.setLevel(logging.ERROR)
logging.getLogger('').addHandler(wfHandler)

# info 信息输出默认配置
logHandler = TimedRotatingFileHandler(default_log_file_name, when="midnight")
formatter = logging.Formatter(default_log_format)
logHandler.setFormatter(formatter)
logHandler.setLevel(default_log_level)
logging.getLogger('').addHandler(logHandler)

# 控制台输出
console = logging.StreamHandler()  
console.setLevel(default_log_level)
formatter = logging.Formatter(default_log_format)  
console.setFormatter(formatter)
# 检查是否需要控制台输出
if default_enable_console:
    logging.getLogger('').addHandler(console)

def get_logger(logger_name):
    '''
    获取logger
    '''
    return logging.getLogger(logger_name)

log = get_logger(__name__)
log.debug('aaaa')
log.error('bbbb')
log.info('sdaa')
log.warn('dada')
    

