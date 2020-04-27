#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/22 10:17
# @File     : prototype.py
# @IDE      : PyCharm


import copy


class ProtoType:
    def __init__(self):
        self._objects = dict()

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj


if __name__ == '__main__':
    class A:
        pass


    a = A()
    proto = ProtoType()
    proto.register_object('a', a)
    b = proto.clone('a', a=1, b=1, c=3)
    print(a)
    print(b)
    print(b.__dict__)
