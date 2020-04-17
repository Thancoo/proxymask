#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/16 10:48
# @File     : udp.py
# @IDE      : PyCharm


from socketserver import BaseRequestHandler, UDPServer
import time


class TimeHandler(BaseRequestHandler):
    def handle(self) -> None:
        print("Got connection from", self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == '__main__':
    serv = UDPServer(('', 22222), TimeHandler)
    serv.serve_forever()
