#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/14 14:15
# @File     : redis_test.py
# @IDE      : PyCharm


from redis import StrictRedis

redis = StrictRedis(
    host='192.168.1.100',
    port=6379,
    db=0,
    password=''
)

redis.set('name', 'One')
print(redis.get('name'))
print(redis.keys())



