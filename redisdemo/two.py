#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/14 15:47
# @File     : two.py
# @IDE      : PyCharm


import cache

a = cache.get_redis()


print(a.hmget('nnn', 'one'))

a.hset('nnn', 'thr', "{'000': 222}")

print(a.hkeys('nnn'))
print(a.hgetall('nnn'))
print(a.hlen('nnn'))
print(a.hvals('nnn'))
print(a.hexists('nnn', 'ooo'))

print(a.hdel('nnn', 'one'))

print(a.hkeys('nnn'))










