#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 9:54 下午
# @Author   : vadon
# @File     : character.py
# @Software : PyCharm


def bytes2string(packet: bytes) -> str:
    return packet.decode(encoding='utf-8', errors='ignore')


if __name__ == '__main__':
    b = b'Hello, world\x90\xff'
    print(bytes2string(b))
    print(len(bytes2string(b)))
    string = "print('Hello, world')"
    exec(string)



