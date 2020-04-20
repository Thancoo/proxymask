#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/20 13:54
# @File     : cong.py
# @IDE      : PyCharm


import toml

my_file = './config/my.toml'
a = toml.load(my_file)
print(type(a))
print(a)