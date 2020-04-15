#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/15 17:44
# @File     : aa.py
# @IDE      : PyCharm


import string
import math


def is_odd(n):
    return n % 2 == 1


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


def check_soldiers(n):
    return n % 3 == 2 and n % 5 == 3 and n % 7 == 2


temp = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
tt = filter(is_sqr, range(1, 101))
ss = filter(check_soldiers, range(1000, 1500))
print(list(ss))

print(temp)
print(list(temp))
