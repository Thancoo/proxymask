#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/22 10:04
# @File     : factory_method.py
# @IDE      : PyCharm


class ShapeFactory:
    def get_shape(self):
        return self.shape_name


class Circle(ShapeFactory):
    def __init__(self):
        self.shape_name = 'Circle'

    def draw(self):
        print(self, 'Circle draw')


class Rectangle(ShapeFactory):
    def __int__(self):
        self.shape_name = 'Rectangle'

    def draw(self):
        print(self, 'Rectangle draw')


class ShapeInterfaceFactory:
    def create(self):
        raise NotImplementedError


class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()


class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()
