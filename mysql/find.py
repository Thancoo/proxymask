#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/11 16:25
# @File     : find.py
# @IDE      : PyCharm


import pymysql
import asyncio

from settings import system


class MySQLFind:
    def __init__(self, host, port, user, password, database):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            # database=database,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def find_database(self, is_system=False):
        sql = 'show databases'
        databases = list()
        res = self.cursor.execute(sql)
        if res:
            for i in self.cursor.fetchall():
                if is_system:
                    databases.append(i[0])
                else:
                    if i[0] not in system.MYSQL_SYSTEM_DATABASE:
                        databases.append(i[0])
        return databases

    def find_table(self):
        pass

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    a = MySQLFind('192.168.1.181', 3306, 'root', '123456', 'db_mask')
    b = a.find_database()
    print(b)


