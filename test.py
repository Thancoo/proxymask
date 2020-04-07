#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/26 8:52 下午
# @Author   : vadon
# @File     : test.py
# @Software : PyCharm


from settings import PGSQL_PASS_KEYS
from tools import character
from analysis.stream import Stream
from blues import test
from blues import one
from api import one as aa
from analysis import gg






b = b'\0xffhello, world'
a = character.bytes2string(b)

print(test.Test)
print(one.Test)
print(aa.One)
print(gg.GoodGame)
print(Stream)

