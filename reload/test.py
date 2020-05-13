#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/24 18:35
# @File     : test.py
# @IDE      : PyCharm


import time
import multiprocessing


def func(message: str):
    print(message)
    time.sleep(1)
    print('end')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    for i in range(10000):
        msg = 'hello, %d' % i
        pool.apply_async(func, (msg,))
    print('AAA')
    pool.close()
    pool.join()
    print('Dene')
