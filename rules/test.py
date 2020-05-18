#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 16:55
# @File     : replace.py
# @IDE      : PyCharm


import pymysql
import re


# 通过正则匹配出个人敏感信息，如姓名、手机号码、地址、身份证号码、银行卡号
def check_secret(value):
    phone_pattern = '^((13[0-9])|(14[5,7,9])|(15[^4])|(18[0-9])|(17[0,1,3,5,6,7,8]))\\d{8}$'  # 匹配手机号码
    if re.match(phone_pattern, value):
        return 'secret_phone'  # 标记字段是否涉密，以及涉密类型(如姓名、手机号码、地址、身份证号码、银行卡号)
    else:
        return 'no_secret'


class DB(object):
    def __init__(self, ip, port, username, password, database):
        self.db = pymysql.connect(
            host=ip,
            port=port,
            user=username,
            password=password,
            database=database,
        )
        self.cursor = self.db.cursor()

    #  通过schemata获取所有数据库名称
    def get_database(self):
        self.cursor.execute(
            "SELECT schema_name from information_schema.schemata ")
        database_list = self.cursor.fetchall()
        result = []
        for line in database_list:
            if line[0] not in ['information_schema', 'mysql',
                               'performance_schema', 'test',
                               'scan_result']:  # 排除默认的数据库
                result.append(line[0])
        return result

    #  获取表名
    def get_table(self, database):
        self.cursor.execute(
            "select table_name from information_schema.tables where table_schema= '%s' " % database)
        table_list = self.cursor.fetchall()
        result = []
        for line in table_list:
            result.append(line[0])
        return result

    #  获取字段名
    def get_column(self, database, table):
        self.cursor.execute(
            "select column_name from information_schema.columns where table_schema='%s' and table_name='%s'" % (
                database, table))
        column_list = self.cursor.fetchall()
        result = []
        for line in column_list:
            result.append(line[0])
        return result

    #  获取字段内容
    def get_content(self, database, table, column):
        print(database, table, column)
        self.cursor.execute(
            "select %s from %s.%s LIMIT 0,1" % (column, database, table))
        content = self.cursor.fetchall()
        if content:
            return content[0][0]

    def __del__(self):

        self.db.close()


if __name__ == '__main__':
    db = DB(
        ip='192.168.1.180',
        port=3306,
        username='root',
        password='123456',
        database='demo'
    )
    databases = db.get_database()
    for database in databases:
        tables = db.get_table(database)
        for table in tables:
            columns = db.get_column(database, table)
            for column in columns:
                data = db.get_content(database, table, column)
                data = str(data)  # 转成字符串,否则正则报错
                print(database, table, column, data, check_secret(data))  # 输出结果
