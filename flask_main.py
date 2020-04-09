#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/4/8 11:08
# @File     : flask_main.py
# @IDE      : PyCharm

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world'


if __name__ == '__main__':
    app.run()
