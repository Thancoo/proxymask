#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 9:51 下午
# @Author   : vadon
# @File     : mysql.py
# @Software : PyCharm


import settings
from tools import fmt
from tools import forge


class BaseMysqlParser:
    def __init__(self, packet: bytes):
        self.packet = packet
        self.type = None

    def exclude(self) -> bool:
        passes = [i.encode().upper() for i in settings.MYSQL_PASS_KEYS]
        if any(i in self.packet.upper() for i in passes):
            return True

    def determine_type(self) -> (int, int):
        index = fmt.determine_index(self.packet)
        self.type = index
        # if self.type == 6 and self.
