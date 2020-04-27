#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/24 18:37
# @File     : args_reloader.py
# @IDE      : PyCharm


from reload import args_parser
a = locals()

print(a)
print(repr(a))
print(type(a))

for i in range(5):
    b = locals()
    exec('var{} = {}'.format(i, i))
    print('BBB', b)
    # print(locals()['var2'])
    # print(locals()['var2'])
    # print(locals()['var2'])
    # print(locals()['var2'])
    # print(locals()['var2'])

print(var0)
print(var1)
print(var2)
print(var3)
print(var4)




