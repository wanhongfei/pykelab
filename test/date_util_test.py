#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 8:23
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : date_util_test.py
# @Software: PyCharm
from dateutil.rrule import DAILY, TU, MO

if __name__ == '__main__':
    print get_timestamp_by_rule(DAILY, dtstart='2017/07/10', until='2017/07/14', count=1, byweekday=(MO, TU))
