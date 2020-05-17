#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/14 15:49
# @File     : database.py
# @IDE      : PyCharm


redis_config = {
    'host': '192.168.1.100',
    'port': 6379,
    'password': '123456'
}


# 服务器转发端口
# database_name local_addr remote_addr
services = [
    ['mysql', '127.0.0.1:3306', '192.168.1.10:3306'],
    ['postgres', '127.0.0.1:5432', '192.168.1.10:5432'],
]



