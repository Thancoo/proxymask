#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 17:16
# @File     : mysql_c.py
# @IDE      : PyCharm


import pymysql


conn = pymysql.connect(
    host='192.168.1.180',
    # port=3306,
    user='root',
    password='123456',
    database='demo',
)

cur = conn.cursor()
sql = 'select * from data_course where id = 8207700'
cur.execute(sql)
res = cur.fetchall()
print(res)
print(dir(res))
print(res.count(1))
print(res.index(0))


#

