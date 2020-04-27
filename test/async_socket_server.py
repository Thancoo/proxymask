#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/22 9:13
# @File     : async_socket_server.py
# @IDE      : PyCharm

import socketserver
from typing import Any


class AsyncSocketServer(socketserver.BaseRequestHandler):
    def __init__(self, request: Any, client_address: Any,
                 server: socketserver.BaseServer):

        super().__init__(request, client_address, server)
        self.data = bytes()

    def handle(self) -> None:
        try:
            while True:
                self.data = self.request.recv(1024)
                print(f'{self.client_address} send: {self.data}')
                if not self.data:
                    print('connection lost')
                    break
                self.request.sendall(self.data.upper())
        except Exception as e:
            print(e)
            print(self.client_address, 'closed')
        finally:
            self.request.close()

    def setup(self) -> None:
        print('setup')

    def finish(self) -> None:
        print('finish')


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(
        ('localhost', 9999),
        AsyncSocketServer
    )
    s.serve_forever()
