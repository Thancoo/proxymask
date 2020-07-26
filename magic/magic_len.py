# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 5:04 下午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : magic_len.py
# @Project  : proxymask


class Test:
    def __init__(self):
        self.a = [1, 2, 3, 4, 5]

    def __len__(self):
        print('__len__')
        # TypeError: 'str' object cannot be interpreted as an integer
        # return str(len(self.a) + 100)
        return len(self.a) + 100


if __name__ == '__main__':
    b = Test()
    res = len(b)
    print(res)
