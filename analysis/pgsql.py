#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 14:28
# @File     : pgsql.py
# @IDE      : PyCharm


import settings
from tools import fmt
from tools import forge


class BasePgSQLParser:

    def __init__(self, packet: bytes):
        self.packet = packet
        self.type = None

    def exclude(self) -> bool:
        passes = [i.encode().upper() for i in settings.PGSQL_PASS_KEYS]
        if any(i in self.packet.upper() for i in passes):
            return True

    def determine_type(self) -> (int, int):
        index = fmt.determine_index(self.packet)
        self.type = index
        if self.type == 6 and self.packet[-1] == 4:
            return 6, -38
        return 0, -1

    def get_sql(self):
        """
        Get statement
        :return:
        """
        pre, pos = self.determine_type()
        stmt = self.packet[pre:pos]
        print('STMT:', stmt)
        return stmt

    def construct(self, sql: str) -> bytes:
        if not isinstance(sql, str):
            print('the statement must be str')
            return self.packet

        # cut off if there is a semicolon
        if sql[-1] == chr(59):
            sql = sql[:-1]
        default_sql = fmt.default_sql(sql)
        if self.type == 6:
            self.type = None
            return self.sub_construct_one(default_sql)
        pass

    def sub_construct_one(self, sql: str) -> bytes:
        """
        dbv
        :param sql:
        :return:
        """
        s_one = bytes([self.packet[0]])
        s_thr = bytes([self.packet[5]])
        s_pos = self.packet[-38:]

        l_two = forge.number2bytes(
            number=len(sql) + 8,
            length=4,
            reverse=False
        )
        r_sql = sql.encode()

        # error
        packet = s_one + l_two + s_thr + r_sql + s_pos
        return packet

    @property
    def database(self):
        return 'pgsql'
