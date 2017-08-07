# coding=utf8
# ***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
# *************************************************************************/

#
# @file __init__.py
#
# @brief __init__.py
#
# @author wanhongfei@bytedance.com
# @date   2017-08-04
# @update 2017-08-04
#
#
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_PATH)
