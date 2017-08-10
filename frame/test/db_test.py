#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 10:58
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : db_test.py
# @Software: PyCharm
from frame.sqlalchemy.db_manager import DBManager
from frame.test.models.user import User

DBManager.get_instance() \
    .db_uri("test", "mysql+mysqldb://root:19940921@localhost:3306/test",
            pool_size=15) \
    .db_uri("test2", "mysql+mysqldb://root:19940921@localhost:3306/test2",
            pool_size=15)

if __name__ == '__main__':
    with DBManager.get_instance().session_ctx(name="test2") as session:
        print session.query(User.name).all()
