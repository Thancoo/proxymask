#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/11 16:25
# @File     : common.py
# @IDE      : PyCharm


import pymysql
import asyncio

from settings import system
from rules import regex


class MySQLFind:
    def __init__(self, host, port, user, password):
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
        """

        :param is_system:
        :return:
        """
        sql = 'show databases'
        databases = list()
        res = self.cursor.execute(sql)
        if res:
            for i in self.cursor.fetchall():
                if is_system:
                    databases.append(i[0])
                else:
                    if i[0] not in system.mysql_system_database:
                        databases.append(i[0])
        return databases

    def find_table(self, database):
        datebase_list = list()
        sql = f"select table_name from information_schema.tables where table_schema='{database}' and table_type='base table';"
        print(sql)
        # 查询库下面的所有表
        res = self.cursor.execute(sql)
        if res:
            for i in self.cursor.fetchall():
                datebase_list.append((database, i[0]))
        print(datebase_list)

        pass

    def find_data(self, database, table, limit=2):
        sensitive_data = dict()
        fields = list()
        # 查询单个表中的字段名
        sql = f"SELECT COLUMN_NAME  FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '{database}' AND TABLE_NAME = '{table}'"
        self.cursor.execute(sql)
        for i in self.cursor.fetchall():
            fields.append(i[0])
        print(fields)
        sql = f"select * from {database}.{table} limit {limit}"
        print(sql)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        result = self.check_data(fields, data)
        print(result)

    # mysql_schema table:'zx', fileds:node, type:1, query:10, sure:5
    # 数据库 模式名（库名） 数据表 字段名 字段类型 查询条数 确定数
    def check_data(self, columns: list, data: tuple) -> dict:
        results = self.construct_columns(columns)  # type: dict
        for item in data:
            for i in item:
                i = str(i).strip()
                if len(i) == 11:
                    res = regex.varify_mobile_phone(i)
                    if res:
                        index = item.index(i)
                        if results[columns[index]].get('mobile_phone'):
                            results[columns[index]]['mobile_phone'] += 1
                        else:
                            results[columns[index]]['mobile_phone'] = 1
                if len(i) == 18:
                    res = regex.varify_id_card(i)
                    if res:
                        index = item.index(i)
                        if results[columns[index]].get('id_card'):
                            results[columns[index]]['id_card'] += 1
                        else:
                            results[columns[index]]['id_card'] = 1
                if '@' in i and len(i) > 8:
                    res = regex.varify_email(i)
                    if res:
                        index = item.index(i)
                        if results[columns[index]].get('email'):
                            results[columns[index]]['email'] += 1
                        else:
                            results[columns[index]]['email'] = 1

        return results

    @staticmethod
    def construct_columns(columns: list) -> dict:
        res = dict()
        for i in columns:
            res[i] = dict()
        return res

    # 查询单表
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    a = MySQLFind('192.168.1.100', 3306, 'root', '123456', )
    b = a.find_database()

    c = a.find_data('data', 'user')
    print(c)
