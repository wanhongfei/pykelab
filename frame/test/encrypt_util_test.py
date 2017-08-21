#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/20 22:06
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : encrypt_util_test.py
# @Software: PyCharm
from frame.utils.encrypt_util import AESEncoder

if __name__ == '__main__':
    aes = AESEncoder('1111111111111111')
    s= aes.encrypt("osao")
    b= aes.decrypt(s)
    print b
