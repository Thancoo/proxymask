# -*- coding: utf-8 -*-
# @Time     : 2020/7/27 9:51 上午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : default_method.py
# @Project  : proxymask


class Test:
    def __init__(self):
        self.a = 1

    def run(self):
        print(self.a, 'run')

    def default_method(self):
        print('default_method')
        print(self.a)

    def __getattr__(self, item):
        if item not in self.__dict__:
            item = self.default_method
        return item


if __name__ == '__main__':
    t = Test()
    t.java()
    t.run()
