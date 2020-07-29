# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 5:32 下午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : magic_getattr.py
# @Project  : proxymask


class Ob:
    def __init__(self):
        self.c = 5


class Test:
    def __init__(self):
        self.a = 1

    def __setattr__(self, key, value):
        print('__setattr__')
        if key == 'a':
            object.__setattr__(self, key, value + 100)
        if key == 'b':
            object.__setattr__(self, key, value + 200)

    def __getattr__(self, item):
        n = Ob()
        print(f'can not find attr {item}')
        return n.__getattribute__(item)


if __name__ == '__main__':
    t = Test()
    t.a = 100
    t.one = 1
    t.two = 2
    print(t.a)
    print(t.c)
