#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/10 17:25
# @File     : one.py
# @IDE      : PyCharm


import pymysql
import traceback


class MySQLHelper:
    def __init__(self, host: str, user: str, password: str, database: str,
                 port=3306, charset='utf-8'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )
        self.cur = self.conn.cursor()

    def fetch_one(self, sql, params=None):
        data_one = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                data_one = self.cur.fetchone()
        except Exception as e:
            traceback.print_exc(e)
        finally:
            self.close()
        return data_one

    def fetch_all(self, sql, params=None):
        data_all = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                data_all = self.cur.fetchall()
        except Exception as e:
            traceback.print_exc(e)
        finally:
            self.close()
        return data_all

    def __item(self, sql, params=None):
        count = 0
        try:
            count = self.cur.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            traceback.print_exc(e)
        finally:
            self.close()
        return count

    def update(self, sql, params=None):
        return self.__item(sql, params)

    def insert(self, sql, params=None):
        return self.__item(sql, params)

    def delete(self, sql, params=None):
        return self.__item(sql, params)

    def close(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()


if __name__ == '__main__':
    h = MySQLHelper(host='192.168.1.181', user='root', password='123456', database='db_mask')
    h.connect()
    data = h.fetch_all('select * from appuser')
    print(data)
