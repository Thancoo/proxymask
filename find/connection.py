#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 15:11
# @File     : connection.py
# @IDE      : PyCharm


import asyncio
import sqlalchemy as sa

from aiomysql.sa import create_engine


metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255)))


async def go(loop):
    engine = await create_engine(user='root', db='test_pymysql',
                                 host='127.0.0.1', password='', loop=loop)
    async with engine.acquire() as conn:
        await conn.execute(tbl.insert().values(val='abc'))
        await conn.execute(tbl.insert().values(val='xyz'))

        async for row in conn.execute(tbl.select()):
            print(row.id, row.val)

    engine.close()
    await engine.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))
