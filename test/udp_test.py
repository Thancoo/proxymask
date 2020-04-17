#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/16 10:53
# @File     : udp_test.py
# @IDE      : PyCharm


from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'', ('localhost', 22221))
res = s.recvfrom(1024 * 8)
print(res)
