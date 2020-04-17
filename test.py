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

from queue import Queue, LifoQueue, PriorityQueue

q = Queue(maxsize=5)
lq = LifoQueue(maxsize=6)
pq = PriorityQueue(maxsize=5)

for i in range(5):
    q.put(i)
    lq.put(i)
    pq.put(i)


from phone import Phone

p = Phone()
a = p.find(18518920100)
print(a)


import ngender



from  pypinyin import Style, pinyin

a = pinyin('调情，拼音结果不会标明哪个韵母是轻声，轻声的韵母没有声调或数字标识')
print(a)

s = str()
for i in a:
    s += i[0] + ' '
print(s)

from make import one

h = one.MySQLHelper(host='192.168.1.181', user='root', password='123456', database='db_mask')
h.connect()


















