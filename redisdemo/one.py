#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/14 15:18
# @File     : one.py
# @IDE      : PyCharm


from redis import StrictRedis, ConnectionPool


pool = ConnectionPool(host='192.168.1.100', port=6379)

redis = StrictRedis(connection_pool=pool)

redis.set('ooo', 111)
a = redis.get('ooo')
print(a == 111)
print(type(a))
b = str(a, encoding='utf-8')
print(repr(b))
print(type(b))

data = [
    {
        'uid': "1234",
        'score': 123,
        'bookname': '局外人',
        'authname': '加缪'

    },
    {
        'uid': "1235",
        'bookname': '我喜欢你，像风走了八千里',
        'authname': '末那大叔',
        'score': 44
    },
    {
        'uid': "1236",
        'bookname': '债务危机',
        'score': 188,
        'authname': '达里欧',
    },
    {
        'uid': "1237",
        'bookname': '全球科技通史',
        'authname': '吴军',
        'score': 99,
    },
    {
        'uid': "1224",
        'score': 12,
        'authname': '霍金',
        'bookname': '霍金沉思录'
    },
    {
        'uid': "1224",
        'bookname': '小丑',
        'authname': 'DG',
        'score': 44
    },
    {
        'uid': "1224",
        'bookname': '脱胎换骨',
        'authname': '克里斯',
        'score': 223
    },
    {
        'uid': "1224",
        'bookname': '间花荨影',
        'authname': '古戈力',
        'score': 11
    }
]
