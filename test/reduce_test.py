# -*- coding: utf-8 -*-
# @Time     : 2020/7/27 7:19 下午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : reduce_test.py
# @Project  : proxymask


from functools import reduce


def add(x, y):
    return x + y


res = reduce(add())


