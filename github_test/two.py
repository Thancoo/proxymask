#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/7 10:19
# @File     : two.py
# @IDE      : PyCharm


from threading import Thread
from multiprocessing import Process
import os


def work(i):
    print('Hello~~~', i, os.getpid())


if __name__ == '__main__':
    t = Thread(target=work, args=(100,))
    t.start()
    print('Main Thread', os.getpid())
    """
    Hello~~~ 100
    Main Thread
    """

    t = Process(target=work, args=(100,))
    t.start()
    print('Main Process', os.getpid())
    # """Main Process
    # Hello~~~ 100
    # """
