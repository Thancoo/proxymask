#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 14:09
# @File     : cocotest.py
# @IDE      : PyCharm


from cocoNLP.extractor import extractor

ex = extractor()

text = '急寻特朗普，男孩，于2018年11月27号11时在陕西省安康市汉滨区走失。丢失发型短发，...如有线索，请迅速与警方联系：18100065143，132-6156-2938，baizhantang@sina.com.cn 和yangyangfuture at gmail dot com'

# 抽取邮箱
emails = ex.extract_email(text)
print(emails)


