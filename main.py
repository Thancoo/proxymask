#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 10:19 下午
# @Author   : vadon
# @File     : main.py
# @Software : PyCharm


from sanic import Sanic, Blueprint
from sanic.response import json, text
from sanic.log import logger

app = Sanic(__name__)
blueprint = Blueprint('foo')


@app.route('/')
async def test(request):
    print(request)
    print(request.cookies)
    print(dir(request))
    print(request.ctx)
    logger.info(request.ctx)
    return json({'Hello', 'world'})


@app.route('/query')
async def query_string(request):
    print(request.endpoint)
    return json({
        'parsed': True,
        'args': request.args,
        'url': request.url,
        'query': request.query_string
    })


@blueprint.get('/bp')
async def bar(request):
    return text(request.endpoint)


@app.route('/cookie')
async def cookie_test(request):
    test_cookie = request.cookies.get('test')
    return text(f'Test cookie set to: {test_cookie}')


@app.route('/write_cookie')
async def write_cookie(request):
    response = text('There is a cookie up in this response')
    response.cookies['test'] = 'It worked'
    response.cookies['one'] = '1111'
    response.cookies['two'] = '2222'
    response.cookies['two']['two1'] = '2121'
    return response


if __name__ == '__main__':
    app.blueprint(blueprint)
    app.run(host='0.0.0.0', port=8000)
