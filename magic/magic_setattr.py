# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 5:25 下午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : magic_setattr.py
# @Project  : proxymask


class Test:
    def __setattr__(self, key, value):
        if key == 'one':
            object.__setattr__(self, key, value + 100)
        if key == 'two':
            object.__setattr__(self, key, value + 200)


if __name__ == '__main__':
    t = Test()
    t.one = 1
    t.two = 2
    print(vars(t))
