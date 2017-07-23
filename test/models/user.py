#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 11:06
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : user.py
# @Software: PyCharm

# 定义User对象:
from sqlalchemy import Column, Integer, String

from frame.orm.sqlalchemy_orm_util import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(20))
    password = Column(String(20))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
