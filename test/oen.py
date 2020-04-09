#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/7 18:29
# @File     : oen.py
# @IDE      : PyCharm


import settings

data = b"P\x00\x00\x01[\x00SELECT nspname AS TABLE_SCHEM, NULL AS TABLE_CATALOG FROM pg_catalog.pg_namespace  WHERE nspname <> 'pg_toast' AND (nspname !~ '^pg_temp_'  OR nspname = (pg_catalog.current_schemas(true))[1]) AND (nspname !~ '^pg_toast_temp_'  OR nspname = replace((pg_catalog.current_schemas(true))[1], 'pg_temp_', 'pg_toast_temp_'))  ORDER BY TABLE_SCHEM\x00\x00\x00B\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00D\x00\x00\x00\x06P\x00E\x00\x00\x00\t\x00\x00\x00\x00\x00S\x00\x00\x00\x04"
lst = [i.encode().upper() for i in settings.PGSQL_PASS_KEYS]
print(lst)


if any(i in data.upper() for i in lst):
    print(True)
else:
    print(False)

print('ss'.encode() + 'hello'.encode())

data = b'hello'
data = data + bytes([66])
print(data)
print(data[:2])
print(bytes([data[0]]))

new_stmt = '''SELECT "id", "course", "company" FROM "my_schema"."data_course" WHERE "id"<8207700'''
print(new_stmt.encode())


