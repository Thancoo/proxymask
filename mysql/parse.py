#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/11 16:25
# @File     : parse.py
# @IDE      : PyCharm


from tools import fmt
from tools import forge
from mysql import replace
from settings import system


class MySQLParser:

    def __init__(self):
        self.packet = bytes()
        self.data = self.packet.upper()
        self.index = int()
        self.code = int()

    def _exclude(self) -> bool:
        pass_keys = [i.encode().upper() for i in system.MySQL_PASS_KEYS]
        if any(i in self.data for i in pass_keys):
            return True

    def _determine(self):
        """

        :return:
        """
        select_index = self.data.find(b'SELECT')
        create_index = self.data.find(b'CREATE')
        if create_index != -1 and create_index < select_index:
            self.index = create_index
        self.index = select_index

    def dispatch(self, packet: bytes) -> bytes:
        """

        :param packet:
        :return:
        """
        self.packet = packet
        self._determine()
        if self._exclude():
            return self.packet

        if self.index in [5, ] and self.code == 0:
            _sql = fmt.default_sql(self.packet[self.index:].decode())
            sql = replace.replace(_sql)
            return self._construct(sql)

    def _construct(self, sql: str) -> bytes:
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
