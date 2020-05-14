#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Time     : 2020/5/14 15:58
# @File     : __init__.py
# @IDE      : PyCharm


import redis

from settings import dbs


def get_redis() -> redis.Redis:
    pool = redis.ConnectionPool(
        host=dbs.redis_config['host'],
        port=dbs.redis_config['port'],
        password=dbs.redis_config['password'],
    )
    conn = redis.Redis(connection_pool=pool)
    return conn
