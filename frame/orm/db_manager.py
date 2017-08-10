#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 17:02
# @Author  : wanhongfei@bytedance.com
# @Comment :
# @File    : db_manager.py
# @Software: PyCharm
import threading
from contextlib import contextmanager

from frame.orm.db_util import get_db_sessionmaker, Base
from frame.utils import is_empty
from frame.utils import randchoice

Base = Base


class DBManager(object):
    # 单例模式
    singleton = None
    mutex = threading.Lock()

    def __init__(self):
        '''
        构造函数：多db_uri
        :param kw_sessions:
        '''
        self.__conf = {}
        self.__session_dict = {}

    def db_uri(self, name, db_uri, **kwargs):
        '''
        获取dburi
        :param name:
        :param db_uri:
        :return:
        '''
        self.__conf[name] = db_uri
        self.__session_dict[name] = get_db_sessionmaker(db_uri, **kwargs)
        return self

    @staticmethod
    def get_instance():
        '''
        单例模式
        :return:
        '''
        if DBManager.singleton == None:
            DBManager.mutex.acquire()
            if DBManager.singleton == None:
                DBManager.singleton = DBManager()
            DBManager.mutex.release()
        return DBManager.singleton

    def __get_session_maker(self, name=None):
        '''
        获取指定的sessionmaker
        :param name:
        :return:
        '''
        if is_empty(self.__session_dict) or is_empty(self.__conf):
            raise Exception("__session_dict is null,please add dburi to dbmanager")
        if name == None:
            name = randchoice(self.__session_dict.keys())
        return self.__session_dict[name]

    @contextmanager
    def session_ctx(self, name=None):
        '''
        构造session上下文，api
        :param name:
        :return:
        '''
        DBSession = self.__get_session_maker(name)
        session = DBSession()
        try:
            # 实现session.xxx().yyy().zzz()
            yield session
            session.commit()
        except Exception, ex:
            session.rollback()
        finally:
            session.close()
