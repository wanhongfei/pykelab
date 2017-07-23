#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: wanhongfei
# Mail: wanhongfei@bytedance.com
# Created Time:  2016-07-16
#############################################


from setuptools import setup, find_packages

setup(
    name = "pykelab_vf",
    version = "0.0.1",
    keywords = ("pip", "django", "vf", "kelab"),
    description = "kelab-vf for python and django",
    long_description = "eds sdk for python",
    license = "MIT Licence",

    url = "",
    author = "wanhongfei",
    author_email = "wanhongfei@bytedance.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [
        'django',
        'sqlalchemy',
    ]
)
