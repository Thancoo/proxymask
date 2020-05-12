#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/11 16:25
# @File     : parse.py
# @IDE      : PyCharm

from tools import forge
from mysql import replace


class MySQLParser:
    # Must be upper
    pass_keys = [
        'INFORMATION_SCHEMA',
    ]

    def __init__(self):
        self.packet = bytes()

    def dispatch(self, packet: bytes) -> bytes:
        """

        :param packet:
        :return:
        """
        self.packet = packet
        if any(bytes(i) in self.packet.upper() for i in self.pass_keys):
            return self.packet
        index, code = self._determine()
        if index in [5, ] and code == 0:
            r_sql = self.packet[5:]
            sql = str(r_sql)
            replace_sql = replace.test(sql)
            return self._constructor_one(replace_sql)

    def _determine(self) -> (int, int):
        """

        :return:
        """
        index = forge.determine_index(self.packet)
        return index, 0

    def _constructor_one(self, sql: str) -> bytes:
        """
        dbv, plsql, navicat, jetbrains
        :param sql:
        :return:
        """
        s_two = bytes(self.packet[4])
        r_sql = bytes(sql)
        l_one = forge.number2bytes(number=len(sql) + 1, length=4, reverse=True)
        packet = l_one + s_two + r_sql
        return packet
