#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 14:35
# @File     : parse.py
# @IDE      : PyCharm


from typing import Optional

from tools import forge
from base import parse


class PgSQLParser(parse.BaseParser):
    # Must be upper
    pass_keys = ['PG_', 'INFORMATION_SCHEMA']

    def judge(self) -> None:
        pass

    def get_sql(self, packet: bytes) -> Optional[str]:
        self.exclude()
    def get_packet(self) -> bytes:
        pass


