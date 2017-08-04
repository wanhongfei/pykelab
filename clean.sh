#!/bin/bash
#***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
#*************************************************************************/

#
#@file clean.sh
#
#@brief clean.sh
#
#@author wanhongfei@bytedance.com
#@date   2017-07-16
#@update 2017-07-16
#
#

find ./ -name "*.pyc" -print | xargs -n1 rm -rf
find ./ -name "*.swp" -print | xargs -n1 rm -rf

