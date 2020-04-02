#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 16:47
# @File     : regex.py
# @IDE      : PyCharm


#
URL1 = r'^[a-zA-z]+://[^\s]*'
URL2 = r'^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$'
phone_regex = '^((13[0-9])|(14[5,7,9])|(15[^4])|(18[0-9])|(17[0,1,3,5,6,7,8]))\\d{8}$'
