#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/22 9:50
# @File     : simple_factory.py
# @IDE      : PyCharm


class Shape:
    def draw(self):
        print(self, 'shape draw')


class Circle(Shape):
    def draw(self):
        print(self, 'circle draw')


class Rectangle(Shape):
    def draw(self):
        print(self, 'rectangle draw')


class ShapeFactory:
    def create(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        return None


if __name__ == '__main__':
    fac = ShapeFactory()
    obj = fac.create('Circle')
    obj.draw()
