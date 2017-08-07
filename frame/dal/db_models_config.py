# coding=utf8
# ***************************************************************************
#
# Copyright (c) 2017 ByteDance.com, Inc. All Rights Reserved
#
# *************************************************************************/

#
# @file db_models_config.py
#
# @brief db_models_config.py
#
# @author wanhongfei@bytedance.com
# @date   2017-08-06
# @update 2017-08-06
#
#
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models

type_name_to_models_type = {
    "int": models.IntegerField,
    "bigint": models.BigIntegerField,
    "varchar": models.IntegerField,
    "char": models.CharField,
    "datetime": models.DateTimeField,
    "date": models.DateField,
    "decimal": models.DecimalField,
    "float": models.FloatField,
    "boolean": models.BooleanField,
}


def get_models_field(type_name, length, not_null=False, decimal=0, default=None, primary_key=False,
                     auto_now=False, auto_now_add=False):
    '''
    get django orm models fields type
    '''
    type_name = type_name.lower()
    if type_name_to_models_type.get(type_name):
        field_type = type_name_to_models_type[type_name]
        if type_name in ("decimal"):
            return field_type(max_length=length, decimal_places=decimal, null=not_null, default=default)
        if type_name in ("date", "datetime"):
            return field_type(max_length=length, null=not_null, default=default, auto_now=auto_now,
                              auto_now_add=auto_now_add)
        return field_type(max_length=length, default=default, null=not_null)
    else:
        raise Exception('please use models.xxx new the fields of orm models')
