#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/14 14:56
# @File     : fb.py
# @IDE      : PyCharm


from redisdemo.demo import RedisHelper

obj = RedisHelper()
while True:
    msg = input('>>:')
    obj.public(msg)
