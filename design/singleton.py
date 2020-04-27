#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/22 10:24
# @File     : singleton.py
# @IDE      : PyCharm


import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


class MyContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(111)
        return self

    def do_self(self):
        print(self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(222)
        print(exc_type)
        print(exc_val)
        print(exc_tb)


if __name__ == '__main__':
    with MyContext('test') as m:
        m.do_self()
