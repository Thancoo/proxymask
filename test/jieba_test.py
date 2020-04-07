#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/3 13:51
# @File     : jieba_test.py
# @IDE      : PyCharm


from functools import wraps
import time
import jieba

# s = '可使用 jieba.cut 和 jieba.cut_for_search 方法进行分词，两者所返回的结构都是一个可迭代的 generator，可使用 for 循环来获得分词后得到的每一个词语（unicode），或者直接使用 jieba.lcut 以及 jieba.lcut_for_search 直接返回 list'
# lst = jieba.lcut(s, cut_all=False)
# print(lst)
# # print(' '.join(lst))
#
#
# seg_list = jieba.cut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")
# print("【搜索引擎模式】：" + "/ ".join(seg_list))


def time_this(func):
    """
    Decorator defines a method's boundaries and execution speed.
    :param func: inner func
    :return: the result of inner func
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('The execution time of', func.__name__, 'is',
              (end - start) * 1000, 'milliseconds')

        return result

    return wrapper


@time_this
def test(n):
    c = 0
    while c < n:
        tt = 'testHello,Java'
        b = tt.upper().encode()
        c += 1

@time_this
def test1(n):
    c = 0
    while c < n:
        tt = 'testHello,Java'
        b = tt.encode().upper()
        c += 1




# 1855 1835
# 1851 1835

if __name__ == '__main__':
    # test(10000000)
    test1(10000000)