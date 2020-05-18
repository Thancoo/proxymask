#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/18 9:26
# @File     : interceptor.py
# @IDE      : PyCharm


import sys
import asyncio
import traceback
from typing import Optional
from settings import database


class ConnectionProtocol(asyncio.Protocol):
    def __init__(self, peer: asyncio.transports.WriteTransport) -> None:
        self.peer = peer
        self.transport = None
        self.buffer = list()

    def connection_made(
            self, transport: asyncio.transports.WriteTransport
    ) -> None:
        self.transport = transport
        if len(self.buffer) > 0:
            self.transport.writelines(self.buffer)
            self.buffer = list()

    def data_received(self, data: bytes) -> None:
        self.peer.write(data)

    def connection_lost(self, exc: Optional[Exception]) -> None:
        self.peer.close()


class ForwarderProtocol(asyncio.Protocol):
    def __init__(self, remote_host: str, remote_port: int) -> None:
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.transport = None
        self.connection_protocol = None

    def connection_made(
            self, transport: asyncio.transports.WriteTransport
    ) -> None:
        self.transport = transport
        conn_loop = asyncio.get_event_loop()
        self.connection_protocol = ConnectionProtocol(self.transport)
        asyncio.ensure_future(
            conn_loop.create_connection(
                lambda: self.connection_protocol,
                self.remote_host,
                self.remote_port
            ),
            loop=conn_loop
        )

    def data_received(self, data: bytes) -> None:
        print('\nReceived(raw):\n', data)
        print('LenData:\n', len(data))
        new_data = self.fix_packet(data)

        if self.connection_protocol.transport is None:
            self.connection_protocol.buffer.append(new_data)
        else:
            self.connection_protocol.transport.write(new_data)

    def connection_lost(self, exc: Optional[Exception]) -> None:
        self.connection_protocol.transport.close()

    @staticmethod
    def fix_packet(packet: bytes) -> bytes:
        print('AAA')
        return packet


def main(loop):
    tasks = list()
    for i in database.SERVERS:
        print(i[1])
        print(i[2])
        print(i[3])
        print(i[4])
        oracle_coroutine = loop.create_server(
            lambda: ForwarderProtocol(
                remote_host=i[3],
                remote_port=i[4]
            ),
            host=i[1],
            port=i[2]
        )
        print(f'{i[0]}: {i[1]}:{i[2]} -> {i[3]}:{i[-1]}')
        tasks.append(oracle_coroutine)
    return tasks

    # ------------------------


def main2(loop):
    tasks = list()
    oracle_coroutine = loop.create_server(
        lambda: ForwarderProtocol(
            remote_host='192.168.1.116',
            remote_port=1521
        ),
        host='127.0.0.1',
        port=1520
    )
    tasks.append(oracle_coroutine)

    pgsql_coroutine = loop.create_server(
        lambda: ForwarderProtocol(
            remote_host='192.168.1.102',
            remote_port=5432
        ),
        host='127.0.0.1',
        port=5431
    )
    tasks.append(pgsql_coroutine)

    mysql_coroutine = loop.create_server(
        lambda: ForwarderProtocol(
            remote_host='192.168.1.102',
            remote_port=3306
        ),
        host='127.0.0.1',
        port=3305
    )

    tasks.append(mysql_coroutine)

    return tasks
    # ------------------

    # # print(f'Server on {server1.sockets[0].getsockname()}')
    # print(f'Server on {server2.sockets[0].getsockname()}')
    # # print(f'Server on {server3.sockets[0].getsockname()}')
    # try:
    #     # loop.run_until_complete(server1.wait_closed())
    #     loop.run_until_complete(server2.wait_closed())
    #     # loop.run_until_complete(server3.wait_closed())
    # except KeyboardInterrupt as ki:
    #     sys.stderr.flush()
    #     traceback.print_exc(ki)


def run2(loop, cors):
    croutines = asyncio.gather(*cors)
    servers = loop.run_until_complete(croutines)
    for i in servers:
        loop.run_until_complete(i.wait_closed())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    ss = main(loop)
    print('ssss', ss)
    run2(loop, ss)
