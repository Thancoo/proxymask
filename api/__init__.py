#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/3 16:04
# @File     : __init__.py.py
# @IDE      : PyCharm


from sanic import Sanic

app_admin = Sanic('admin')
app_login = Sanic('login')
