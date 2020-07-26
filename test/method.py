# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 4:35 下午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : method.py
# @Project  : proxymask


class A:
    explanation = "this is my programs"

    def normal_method(self, name):
        print(self.explanation, name)

    @classmethod
    def class_method(cls, explanation):
        print(cls.explanation, explanation)

    @staticmethod
    def static_method(explanation):
        print(explanation)


if __name__ == '__main__':
    a = A()
    a.explanation = 'test'
    a.normal_method('one')
    A.class_method('nodejs')
    a.class_method('python')



