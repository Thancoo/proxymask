#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/7 10:36
# @File     : client.py
# @IDE      : PyCharm

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9090))

while True:
    msg = input('>>> ').strip()
    if not msg:
        continue
    s.send(msg.encode('UTF-8'))
    data = s.recv(1024)
    print(data)
