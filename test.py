#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/26 8:52 下午
# @Author   : vadon
# @File     : test.py
# @Software : PyCharm


def func():
    a = '123'
    b = 123
    return a, b


if __name__ == '__main__':
    b = func()
    print(isinstance(b, set))
    print(isinstance(b, tuple))
