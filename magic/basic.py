#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/22 11:00
# @File     : basic.py
# @IDE      : PyCharm

class Test:
    def __init__(self, data):
        print(111)
        self.data = data

    def __new__(cls, *args, **kwargs):
        print(222)
        print(args)
        print(kwargs)
        return cls

    def __del__(self):
        print(333)

    def run(self):
        print(self.data)


if __name__ == '__main__':
    t = Test('aaa')
    t.run()
