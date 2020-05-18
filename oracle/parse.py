#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/4/3 16:02
# @File     : parse.py
# @IDE      : PyCharm


from tools import fmt
from tools import forge
from settings import system
from oracle import replace


class OracleParser:

    def __init__(self):
        self.packet = bytes()
        self.data = self.packet.upper()
        self.index = int()
        self.code = int()

    def _exclude(self) -> bool:
        pass_keys = [i.encode('utf-8') for i in system.ORACLE_PASS_KEYS]
        if any(i in self.data for i in pass_keys):
            return True

    def _determine(self):
        select_index = self.data.find(b'SELECT')
        create_index = self.data.find(b'CREATE')
        if create_index != -1 and create_index < select_index:
            self.index = create_index
        self.index = select_index

    def dispatch(self, packet: bytes) -> bytes:
        self.packet = packet
        self._determine()
        if self._exclude():
            return self.packet
        if self.index in [93, 94, 97, 98] and self.code == 0:
            s_pos = self.packet[-52:]
            return self.packet
        return self.packet
