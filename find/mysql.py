#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/14 16:15
# @File     : mysql.py
# @IDE      : PyCharm


import pymysql

conn = pymysql.connect(
    host='192.168.1.181',
    port=3306,
    user='root',
    password='123456',
    db='information_schema',
    charset='utf8'
)
print(conn)

cursor = conn.cursor()
print(cursor)

# sql = "select table_name from information_schema.tables where table_schema='csdb' and table_type='base table';"
# sql = "SELECT distinct TABLE_SCHEMA FROM TABLES"
# sql = "select table_name from information_schema.tables where table_schema='db_mask' and table_type='base table';"

# create database
sql = 'create database data;'

# create table





result = cursor.execute(sql)
print(result)


db_mask = cursor.fetchall()

print(type(db_mask))
print(len(db_mask))







