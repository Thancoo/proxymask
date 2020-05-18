#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/18 18:43
# @File     : parse.py
# @IDE      : PyCharm


from tools import fmt
from tools import forge
from settings import system
from pgsql import replace

class MariaDBParser:

    def __init__(self):
        self.packet = bytes()
        self.data = self.packet.upper()
        self.index = int()
        self.code = int()

    def _exclude(self) -> bool:
        pass_keys = [i.encode().upper() for i in system.PGSQL_PASS_KEYS]
        if any(i in self.data for i in pass_keys):
            return True

    def _determine(self):
        select_index = self.data.find(b'SELECT')
        create_index = self.data.find(b'CREATE')
        if create_index != -1 and create_index < select_index:
            self.index = create_index
        self.index = select_index

    def dispatch(self, packet:bytes) -> bytes:
        self.packet = packet
        self._determine()
        if self._exclude():
            return self.packet

        if self.index == 5 and self.code == 0:
            _sql = fmt.default_sql(self.packet[self.index:].decode())
            sql = replace.replace(_sql)
            return self._construct(sql)




    def _construct(self,sql:str) -> bytes:
        return self.packet








