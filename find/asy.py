#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 15:59
# @File     : asy.py
# @IDE      : PyCharm


import asyncio
import time
import datetime


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main(p):
    print(p)
    print(f'started at {time.strftime("%X")}')
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f'finished at {time.strftime("%X")}')


async def main1():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f'started at {time.strftime("%X")}')
    await task1
    await task2
    print(f'finished at {time.strftime("%X")}')


async def nested(number):
    return number


# 协程
async def main2():
    a = await nested(45)
    print(a)


# 任务
async def main3():
    task = asyncio.create_task(nested(68))
    a = await task
    print(a)


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


print(asyncio.iscoroutinefunction(display_date))
