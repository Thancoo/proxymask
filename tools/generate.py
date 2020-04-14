#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/9 18:41
# @File     : generate.py
# @IDE      : PyCharm


import random
import datetime

NOW = datetime.datetime.now()

print(NOW)
print(type(NOW.year))
"""
mod
    0 random
    1 *
"""

print(random.randint(1, 2))


def int2string(number: int, length: int) -> str:
    s = str(number)
    if len(s) < length:
        return chr(48) * (length - len(s)) + s
    return s


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def birth(age: int, scope: int, mode=0) -> str:
    rand_scope = random.randint(-scope, scope)
    y = NOW.year - age + rand_scope
    m = random.randint(1, 12)
    if m in [1, 3, 5, 7, 8, 10, 12]:
        d = random.randint(1, 31)
    elif m == 2 and is_leap_year(y):
        d = random.randint(1, 29)
    elif m == 2 and not is_leap_year(y):
        d = random.randint(1, 28)
    else:
        d = random.randint(1, 30)
    return int2string(y, 4) + int2string(m, 2) + int2string(d, 2)


def id_card(year: int, scope: int, mode=0) -> str:
    b = birth(year, scope, mode)
    print(b)
    return '123'


if __name__ == '__main__':
    for i in range(10):
        print(id_card(25,2))


