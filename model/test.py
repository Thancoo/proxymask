#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/9 18:17
# @File     : replace.py
# @IDE      : PyCharm

import pymysql

conn = pymysql.connect(
    host='192.168.1.100',
    port=3306,
    user='root',
    password='123456',
    db='test',
    charset='utf8'
)

cursor = conn.cursor()
print(cursor)
# sql = 'select * from zx_table;'
# rows = cursor.execute(sql)
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())


sql1 = """select TABLE_NAME from information_schema.columns where table_schema='mysql';"""
rows = cursor.execute(sql1)
res = cursor.fetchall()
lst = list()
for i in res:
    if i[0] not in lst:
        lst.append(i[0])

sql2 = """select * from mysql.%s""" % 'user'

rows2 = cursor.execute(sql2)
res = cursor.fetchall()

print(res)

# sql2 = "select table_name from information_schema.tables where table_schema='csdb' and table_type='base table';"
#
# rows2 = cursor.execute(sql2)
# print(cursor.fetchall())









