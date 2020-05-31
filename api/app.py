#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/31 2:12 下午
# @Author   : vadon
# @File     : app.py
# @Software : PyCharm

from sanic.response import json
from api import app_admin, app_login


@app_admin.route('/index')
async def index(request):
    print(request)
    return json({'msg': 'this is index'})


@app_login.route('/login')
async def login(request):
    print(request)
    return json({'msg': 'this is login'})
