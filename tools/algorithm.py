#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 8:46 下午
# @Author   : vadonical
# @Email    : vadonical@gmail.com
# @File     : algorithm.py
# @Software : PyCharm


import re
import random

HEADLINE_DISPLAY = True


# BYTES
def number2bytes(number: int, length: int, reverse=False) -> bytes:
    """
    Change a number to its hexadecimal native bytes
    :param number: the number
    :param length: the length of out, fixed-digit digits zeroing at high digits
    if necessary
    :param reverse: big or little end code
    :return: raw length bytes
    """
    lst = list()
    for i in range(0, length):
        lst.append(number >> (i * 8) & 0xff)
    if reverse:
        return bytes(lst)
    lst.reverse()
    return bytes(lst)


def bytes2number(byte: bytes):
    pass


def list2dict(l1: list, l2: list, reverse=False) -> dict:
    if l1 is None:
        l1 = list()
    if l2 is None:
        l2 = list()
    if not reverse:
        return dict(zip(l1, l2))
    return dict(zip(l2, l1))


def random_words(length=4, mode=0) -> str:
    """

    :param length:
    :param mode:
    :return:
    """
    if length <= 0:
        length = random.randint(1, 16)
    words = list()
    uppers = [i for i in range(65, 91)]
    lowers = [i for i in range(97, 123)]
    if mode == 0:
        lst = lowers
    elif mode == 1:
        lst = uppers
    else:
        lst = uppers + lowers
    for i in range(length):
        words.append(chr(random.choice(lst)))
    return str().join(words)


def split_string_by_length(string: str, length: int) -> list:
    """
    Split string by length
    :param string:
    :param length:
    :return:
    """
    regex = re.compile(r'.{%d}' % length, re.DOTALL)
    lst = re.findall(regex, string)
    lst.append(string[(len(lst) * length):])
    return lst


def headline(header: str, separator='-', length=80):
    """
    Dividing line of separating program running steps by string
    :param header: string you want to separate
    :param separator: separator symbols
    :param length: the length of the dividing line
    :return: None
    """
    if len(header) > length - 4:
        header = 'DEFAULT'
    if HEADLINE_DISPLAY:
        line_num = (length - len(header) - 2) // 2
        print(
            separator * line_num + chr(32) + header + chr(32) + separator * (
                    length - line_num - 2 - len(header)
            )
        )


def bytes2string(packet: bytes) -> str:
    return packet.decode(encoding='utf-8', errors='ignore')

if __name__ == '__main__':
    a = random_words()
    print(a)
