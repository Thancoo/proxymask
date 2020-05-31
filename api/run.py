#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/31 2:20 下午
# @Author   : vadon
# @File     : run.py
# @Software : PyCharm


import asyncio
from api import app_admin
from api import app_login


def run(app, port):
    app.run(port=port)


if __name__ == '__main__':
    gather()
