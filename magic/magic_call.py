# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 4:43 下午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : magic_call.py
# @Project  : proxymask


class Test:
    def __init__(self):
        self.a = 1

    def __call__(self, *args, **kwargs):
        res = str()
        for i in args:
            res += str(i)
        return f"the value is {res}"


if __name__ == '__main__':
    t = Test()
    print(t(100, 'string'))
