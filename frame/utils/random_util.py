#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 10:45
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : random_util.py
# @Software: PyCharm
import random

from frame.utils import string_util


def randint(left, right, gap=1):
    '''
    随机生成整型，[left,right)
    x = letf + y * gap
    :param left:
    :param right:
    :param gap:
    :return:
    '''
    return random.randrange(left, right, gap)


LOWWER_ALPHA_CH_ARRAY = "abcdefghijklnmopqrstuvwxyz"
DIGIT_CH_ARRAY = "1234567890"
DEFAULT_SAMPLE_CH_ARRAY = LOWWER_ALPHA_CH_ARRAY + LOWWER_ALPHA_CH_ARRAY.upper() + DIGIT_CH_ARRAY


def randsample(len=1, ch=DEFAULT_SAMPLE_CH_ARRAY, sep=""):
    '''
    随机生成指定长度指定字符集的字符串
    :param len:
    :param ch:
    :return:
    '''
    return string_util.join(random.sample(ch, len), sep)


def randchoice(items):
    '''
    随机返回一个元素
    :param array:
    :return:
    '''
    return random.choice(items)
