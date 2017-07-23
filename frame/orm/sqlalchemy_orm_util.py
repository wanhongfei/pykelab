#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 21:50
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : sqlalchemy.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类,所有model继承base
Base = declarative_base()


def single_db_init(db_uri):
    '''
    简易数据库初始化方法
    :param db_uri:
    :return:
    '''
    # 初始化数据库连接:
    engine = create_engine(db_uri)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    return DBSession


def multi_db_init(kv_db_uri={}):
    '''
    多数据库初始化方法
    :param db_uri:
    :return:
    '''
    ret = {}
    for key in kv_db_uri:
        engine = create_engine(kv_db_uri.get(key))
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        ret[key] = Session
        Base.metadata.create_all(engine)
    return ret


def open_session(Session=None):
    '''
    开启会话
    :param Session:
    :return:
    '''
    return Session()


def commit_session(session=None):
    '''
    提交会话
    :param Session:
    :return:
    '''
    session.commit()
    session.close()


def rollback_session(session=None):
    '''
    回滚会话
    :param Session:
    :return:
    '''
    session.rollback()
    session.close()
