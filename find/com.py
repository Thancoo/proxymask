#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 15:48
# @File     : com.py
# @IDE      : PyCharm


import time
from queue import Queue
from threading import Thread


def producer(out_q):
    n = 0
    while True:
        out_q.put(n)
        n += 1
        time.sleep(.5)
        print(n)


def consumer(in_q):
    while True:
        data = in_q.get()
        time.sleep(1)
        print(data)


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
