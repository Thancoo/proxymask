#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/13 11:17
# @File     : person.py
# @IDE      : PyCharm


class BasePerson:
    def __init__(self, *args, **kwargs):
        self.args = args
        if 'name' in kwargs:
            self.name = kwargs['name']

        pass

    def name(self):
        pass

    def phone(self):
        pass

    def mobile_phone(self):
        pass

    def gender(self, mode=0):
        if mode:
            return 111


        pass

