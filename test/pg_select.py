#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 14:26
# @File     : pg_select.py
# @IDE      : PyCharm



#
data = b"P\x00\x00\x02V\x00SELECT c.oid, a.attnum, a.attname, c.relname, n.nspname, a.attnotnull OR (t.typtype = 'd' AND t.typnotnull), a.attidentity != '' OR pg_catalog.pg_get_expr(d.adbin, d.adrelid) LIKE '%nextval(%' FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON (c.relnamespace = n.oid) JOIN pg_catalog.pg_attribute a ON (c.oid = a.attrelid) JOIN pg_catalog.pg_type t ON (a.atttypid = t.oid) LEFT JOIN pg_catalog.pg_attrdef d ON (d.adrelid = a.attrelid AND d.adnum = a.attnum) JOIN (SELECT 13159 AS oid , 2 AS attnum UNION ALL SELECT 13159, 3) vals ON (c.oid = vals.oid AND a.attnum = vals.attnum) \x00\x00\x00B\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00D\x00\x00\x00\x06P\x00E\x00\x00\x00\t\x00\x00\x00\x00\x00S\x00\x00\x00\x04"
print(data.find(b'SELECT'))
print(data[-38:])
print(data[6:-38].strip())
print(type(str(data[6:-38].strip())))
print((str(data[6:-38].strip())))
print(data[0] == 80)
print(data[:2])