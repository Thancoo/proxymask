#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/7 10:32
# @File     : server.py
# @IDE      : PyCharm


import multiprocessing
import threading
import socket


def action(c):
    while True:
        data = c.recv(1024)
        print(data)
        c.send(data.upper())


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9090))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        p = threading.Thread(target=action, args=(conn,))
        p.start()
