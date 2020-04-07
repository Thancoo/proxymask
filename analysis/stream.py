#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 14:02
# @File     : stream.py
# @IDE      : PyCharm


import settings

from analysis import pgsql
from analysis import mysql


class Stream:

    def __init__(self, packet: bytes) -> None:
        self.packet = packet


    def distribute(self) -> (tuple, str):
        if len(self.packet) < settings.LIMIT_LENGTH:
            return
        if self.is_select_statement():
            # pgsql
            if self.get_database == 'pgsql':
                obj = pgsql.BasePgSQLParser(packet=self.packet)
                if obj.exclude():
                    return self.packet
                statement = obj.get_sql()
                print('CCC:', statement, obj)
                return statement, obj

            # mysql
            elif self.get_database == 'mysql':
                pass

    def is_select_statement(self):
        keys = ['SELECT', 'FROM']
        b_keys = [i.encode('utf-8') for i in keys]
        if all(i in self.packet for i in b_keys):
            return True

    @property
    def get_database(self):
        if self.packet:
            return 'pgsql'


if __name__ == '__main__':
    select = ['SELECT', 'FROM']
    b_select = [i.encode('utf-8') for i in ['SELECT', 'FROM']]
    print(b_select)
