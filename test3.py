#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/17 8:22 下午
# @Author   : vadon
# @File     : test3.py
# @Software : PyCharm


from multiprocessing import Pool
import time


def func(name, number):
    print(name)
    print(number)
    time.sleep(2)
    print(time.ctime())


if __name__ == '__main__':
    lst = [
        ['aa', 111],
        ['bb', 222],
        ['cc', 333],
    ]
    p = Pool(5)
    start = time.time()

    for i in lst:
        p.apply_async(func, args=(*i,))
    p.close()
    p.join()
    print(time.time() - start)
