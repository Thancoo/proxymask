#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 8:51 下午
# @Author   : vadon
# @File     : simulation.py
# @Software : PyCharm


import random
import re
import settings


class ReplaceDemo:
    def __init__(self, db_type):
        self.db_type = db_type
        self.sql = str()

    def random(self, sql, length=0):
        ret = random.choice(settings.oracle['statements'])
        return

    def format_length(self, sql, length):
        if length < len(self.sql) + 4:
            return


        pass


if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    print(random.choices(lst, k=2))
