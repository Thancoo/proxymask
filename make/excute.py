#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/13 11:16
# @File     : excute.py
# @IDE      : PyCharm


import pymysql
import traceback


try:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456'
    )
    cur = conn.cursor()
    create_database = '''CREATE DATABASE IF NOT EXISTS py3_tstgr DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'''
    cur.execute(create_database)
    cur.close()
    print('YES')
except pymysql.Error as e:
    traceback.print_exc(e.args[0], e.args[1])
