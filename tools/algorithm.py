#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 8:46 下午
# @Author   : vadonical
# @Email    : vadonical@gmail.com
# @File     : algorithm.py
# @Software : PyCharm


def number2bytes(number: int, length:int, reverse=False) -> bytes:
    """
    Change a number to its hexadecimal native bytes
    :param number: The number
    :param length: the length of out, fixed-digit digits zeroing at high digits
    if necessary
    :param reverse: Big or Little end code
    :return: Raw length bytes
    """
    lst = list()
    for i in range(0, length):
        lst.append(number >> (i * 8) & 0xff)
    if reverse:
        return bytes(lst)
    lst.reverse()
    return bytes(lst)



