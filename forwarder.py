#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/6 11:59
# @File     : forwarder.py
# @IDE      : PyCharm


import sys
import asyncio
import traceback
import multiprocessing

from settings import database
# from analysis import stream
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
        print('AAA')

        # stream_obj = stream.Stream(packet)
        # res = stream_obj.distribute()
        #
        # # 需要做修改，进行语句替换
        # print('DDD', res)
        # if isinstance(res, tuple):
        #     print('TUP')
        #     stmt, parser_obj = res
        #
        #     # rep_obj = simulation.ReplaceDemo(db=obj)
        #     # new_stmt = rep_obj.random(sql=stmt, length=1000)
        #
        #     new_stmt = '''SELECT "id", "course", "company" FROM "my_schema"."data_course" WHERE "id"<8207700'''
        #     data = parser_obj.construct(sql=new_stmt)
        #     print('REPR:', repr(data))
        #     print(data)
        #     packet = data

        return packet


def run(name: str, local: str, remote: str):
    print(f'{name}: {local} -> {remote}')
    loop = asyncio.get_event_loop()
    local_list = local.split(':')
    remote_list = local.split(':')
    coroutine = loop.create_server(
        lambda: ForwarderProtocol(
            remote_host=remote_list[0],
            remote_port=int(remote_list[-1])
        ),
        host=local_list[0],
        port=int(local_list[-1])
    )

    server = loop.run_until_complete(coroutine)
    try:
        loop.run_until_complete(server.wait_closed())
    except KeyboardInterrupt as ki:
        sys.stderr.flush()
        traceback.print_exc(ki)


if __name__ == '__main__':
    run(*database.services[0])
    # pool = multiprocessing.Pool()
    # for i in database.services:
    #     pool.apply_async(func=run, args=(i[0], i[1],i[2]))
    # pool.close()
    # pool.join()

