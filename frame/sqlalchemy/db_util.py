#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 21:50
# @Author  : wanhongfei@bytedance.com
# @Comment :
# @File    : db_util.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类,所有model继承base
Base = declarative_base()


def get_db_sessionmaker(db_uri, **kvargs):
    '''
    简易数据库初始化方法
    :param db_uri:
    :return:
    '''
    # 初始化数据库连接:
    engine = create_engine(db_uri, **kvargs)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    return DBSession
