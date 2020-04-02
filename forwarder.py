#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/6 11:59
# @File     : forwarder.py
# @IDE      : PyCharm


import sys
import asyncio
import traceback
from parser import stream
from typing import Optional
from replace import simulation


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
        obj = stream.Stream(packet)
        res = obj.distribute()

        # 需要做修改，进行语句替换
        if isinstance(obj, tuple):
            stmt, obj = res
            new_obj = simulation.ReplaceDemo(db=obj)
            new_stmt = new_obj.random(sql=stmt, length=1000)
            return obj.construct(sql=new_stmt)

        return packet


def main() -> None:
    loop = asyncio.get_event_loop()
    oracle_coroutine = loop.create_server(
        lambda: ForwarderProtocol(
            remote_host='192.168.1.116',
            remote_port=1521
        ),
        host='127.0.0.1',
        port=1522
    )

    pgsql_coroutine = loop.create_server(
        lambda: ForwarderProtocol(
            remote_host='192.168.1.182',
            remote_port=5555
        ),
        host='127.0.0.1',
        port=5555
    )

    mysql_coroutine = loop.create_server(
        lambda: ForwarderProtocol(
            remote_host='192.168.1.180',
            remote_port=3306
        ),
        host='127.0.0.1',
        port=3306
    )
    server1 = loop.run_until_complete(oracle_coroutine)
    server2 = loop.run_until_complete(pgsql_coroutine)
    server3 = loop.run_until_complete(mysql_coroutine)

    print(f'Server on {server1.sockets[0].getsockname()}')
    print(f'Server on {server2.sockets[0].getsockname()}')
    print(f'Server on {server3.sockets[0].getsockname()}')
    try:
        loop.run_until_complete(server1.wait_closed())
        loop.run_until_complete(server2.wait_closed())
        loop.run_until_complete(server3.wait_closed())
    except KeyboardInterrupt as ki:
        sys.stderr.flush()
        traceback.print_exc(ki)


if __name__ == '__main__':
    main()
