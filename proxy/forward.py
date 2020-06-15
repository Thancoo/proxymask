#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/6/15 8:28 下午
# @Author   : vadon
# @File     : forward.py
# @Software : PyCharm


import sys
import asyncio


class ProxyProtocol(asyncio.Protocol):
    def __init__(self, peer: asyncio.transports.WriteTransport):
        self.peer = peer
        self.transport = None
        self.buffer = list()

    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.transport = transport
        if len(self.buffer) > 0:
            self.transport.writelines(self.buffer)


