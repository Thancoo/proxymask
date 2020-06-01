#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/5/31 1:26 下午
# @Author   : vadon
# @File     : two.py
# @Software : PyCharm


from sanic import Sanic
from sanic.response import json

app = Sanic('one')


@app.route('/')
async def test(request):
    print(request)
    dic = {'hello': 'world'}
    return json(dic)


@app.route('/test')
async def node(request):
    print(request)
    dic = {'one': 'aaa'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9090, debug=True)
