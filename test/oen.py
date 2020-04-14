#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/7 18:29
# @File     : oen.py
# @IDE      : PyCharm


import settings

a = '\x00E\x00R\x00P\x00\x1fu\xa7ND\x8d\x99e(u7b\x93^'
# a = '\x00 E\x00 R\x00 P\x00  \x1fu \xa7N D\x8d  \x99e  (u  7b  \x93^'
print(a.encode('utf-8'))
print(a)
print(len(a))
# print(a.encode('utf-8'))
# print(a.encode('gbk'))

c = u'生产资料用户库'
print(c.encode())
print(ord('u'))




