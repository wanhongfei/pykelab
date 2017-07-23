#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 10:58
# @Author  : wanhongfei@bytedance.com
# @Comment : 
# @File    : db_test.py
# @Software: PyCharm
from test.models.user import User

if __name__ == '__main__':
    from frame.orm.sqlalchemy_orm_util import multi_db_init, open_session, commit_session

    ret = multi_db_init({
        "test": "mysql+mysqldb://root:19940921@localhost:3306/test",
        "test2": "mysql+mysqldb://root:19940921@localhost:3306/test2",
    })
    user = User()
    user.name = "haha"
    session = open_session(ret['test2'])
    session.add(user)
    commit_session(session)
