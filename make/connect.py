#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/4/9 17:22
# @File     : connect.py
# @IDE      : PyCharm


import psycopg2 as pg
import pymysql as my


class Cursor:
    def __init__(self, db_type: str, **options):
        self.type = db_type
        if 'host' in options:
            self.host = options['host']
        if 'port' in options:
            self.port = options['port']
        if 'username' in options:
            self.username = options['username']
        if 'password' in options:
            self.password = options['password']
        if 'database' in options:
            self.database = options['database']

    def connect(self):
        if self.type == 'pgsql':
            conn = pg.connect(
                database=self.database,
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn.cursor()

    # https://www.cnblogs.com/ryanzheng/p/9693511.html
    def execute(self, statement):

        pass

    def close(self):
        pass


if __name__ == '__main__':
    a = Connection('aa', )
