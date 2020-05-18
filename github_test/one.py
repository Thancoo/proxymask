#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/7 10:09
# @File     : parse.py
# @IDE      : PyCharm


import time
import random
import os
from multiprocessing import Pool


def work(n):
    time.sleep(1)
    return n ** 2


if __name__ == '__main__':
    p = Pool()
    results = list()
    for i in range(10):
        res = p.apply_async(func=work, args=(i,))
        results.append(res)
    p.close()
    p.join()
    print(results)
    nums = list()
    for res in results:
        # print(dir(res))
        nums.append(res.get())
        nums.append(res.ready())
        nums.append(res.successful())
        nums.append(res.wait())
    print(nums)
