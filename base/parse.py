#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 10:47
# @File     : parse.py
# @IDE      : PyCharm

from typing import Optional

from tools import forge


class BaseParser:
    # Must be upper
    pass_keys = []

    def __init__(self):
        self.packet = bytes()
        self.sql = str()
        self.index = int()
        self.code = int()

    def exclude(self) -> bool:
        if any(bytes(i) in self.packet.upper() for i in self.pass_keys):
            return True

    def judge(self) -> None:
        self.index = forge.determine_index(self.packet)

    def get_sql(self, packet: bytes) -> Optional[str]:
        self.packet = packet
        return

    def get_packet(self) -> bytes:
        return self.packet
