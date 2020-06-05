#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 14:02
# @File     : stream.py
# @IDE      : PyCharm

import settings

from analysis import pgsql
from settings import system
from pgsql.parse import PgSQLParser
from oracle.parse import OracleParser
from mysql.parse import MySQLParser
from mariadb.parse import MariaDBParser

ORACLE_ID = 1
MYSQL_ID = 2
PGSQL_ID = 3
MARIADB_ID = 4
SQLLITE = 5
DB2_ID = 6
SQLSERVER_ID = 7


class Stream:
    def __init__(self):
        self.packet = bytes()
        self.data = self.packet.upper()

    def distribute(self, packet: bytes) -> bytes:
        self.packet = packet
        # too short packet
        if len(self.packet) < system.LIMIT_LENGTH:
            return self.packet

        if self._is_query():
            obj = self._determine_database()
            new_packet = obj().dispatch(self.packet)
            return new_packet
        return self.packet

    def _is_query(self):
        keys = ['SELECT', 'FROM']
        bytes_keys = [i.encode() for i in keys]
        if all(i in self.packet for i in bytes_keys):
            return True

    def _determine_database(self):

        if self._is_oracle():
            if self.packet == chr(1):
                return None
            return OracleParser

        elif self._is_pgsql():
            return PgSQLParser

        elif self._is_mysql():
            if self.packet is None:
                return
            return MySQLParser

        elif self._is_mariadb():
            return MariaDBParser()

    def _is_oracle(self) -> bool:
        return True

    def _is_pgsql(self) -> bool:
        return True

    def _is_mysql(self) -> bool:
        return True

    def _is_mariadb(self) -> bool:
        return True


if __name__ == '__main__':
    select = ['SELECT', 'FROM']
    b_select = [i.encode() for i in ['SELECT', 'FROM']]
    print(b_select)
