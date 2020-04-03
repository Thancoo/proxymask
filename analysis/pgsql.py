#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 14:28
# @File     : pgsql.py
# @IDE      : PyCharm


import settings
from tools import character


class BasePgSQLParser:

    def __init__(self, packet):
        self.packet = packet
        self.data = character.bytes2string(self.packet).upper()
        self.sql = str()
        self.status = None
        pass

    def exclude(self):
        if any(i in self.data for i in settings.PGSQL_PASS_KEYS):
            return True

        pass

    def get_sql(self):





        pass

    def construct(self, sql):
        self.sql = sql
        pass

    def sub_construct_one(self):
        pass

    @property
    def info(self):
        return 'pgsql'
