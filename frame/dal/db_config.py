#coding=utf8
#***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
#*************************************************************************/

#
#@file db.py
#
#@brief db.py
#
#@author wanhongfei@bytedance.com
#@date   2017-08-06
#@update 2017-08-06
#
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DBConfig(object):
    
    def __init__(self,dbname,user,pwd,name='default',host='127.0.0.1',port=3306):
        '''
        constructer func
        '''
        self.config = {}
        self.config[name] = {
            'ENGINE': 'django_mysqlpool.backends.mysqlpool',
            'NAME': dbname,
            'USER': user,
            'PASSWORD': pwd,
            'HOST': host,
            'PORT': port,
            'OPTIONS': { 'autocommit': True }, 
        }
    
    def add_config(self,db_config):
        '''
        add db_config
        '''
        self.config.update(db_config.config)
        return self
   
    def django_orm_db_config(self):
        '''
        get config of django orm config
        '''
        return self.config


db1 = DBConfig(dbname='haha',user='root',pwd='haha')
db2 = DBConfig(name='db2',dbname='haha',user='root',pwd='haha')
db3 = DBConfig(name='db3',dbname='haha',user='root',pwd='haha')
print db1.add_config(db2).add_config(db3).django_orm_db_config()
