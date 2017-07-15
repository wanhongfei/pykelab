#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 10:52
# @Author  : wanhongfei@bytedance.com
# @Comment : 方便外部项目引入
# @File    : __init__.py
# @Software: PyCharm


# 配置方法,添加__init__.py文件，增加以下语句进行初始化
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import sys

PROJECT_PATH = "D:\\workspace\\pykelab_vf"


def import_module(project_path, module_name):
    module_path = os.path.join(project_path, module_name)
    print module_path
    sys.path.insert(0, os.path.dirname(module_path))
    try:
        return __import__(module_name)
    finally:
        sys.path.remove(os.path.dirname(module_path))


utils = import_module(PROJECT_PATH, "utils")
frame = import_module(PROJECT_PATH, "frame")
print utils, frame

'''
# 使用demo
'''
from pykelab_vf.utils import json_util
print json_util.obj_to_formatting_json({1:2,3:"da"})
'''