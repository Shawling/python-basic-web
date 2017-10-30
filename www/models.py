#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Models for user, blog, comment.
'''

__author__ = 'Shawling'

import time
import uuid

from orm import BooleanField, FloatField, Model, StringField, TextField, IntegerField


# 通过拼接时间戳与Python内置的uuid算法保证id的唯一性
def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class BaseModel(Model):
    __table__ = 'tablename'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    title = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(50)')
    content = TextField()
    picture = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)