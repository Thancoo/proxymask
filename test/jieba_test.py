#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/3 13:51
# @File     : jieba_test.py
# @IDE      : PyCharm


import jieba

s = '可使用 jieba.cut 和 jieba.cut_for_search 方法进行分词，两者所返回的结构都是一个可迭代的 generator，可使用 for 循环来获得分词后得到的每一个词语（unicode），或者直接使用 jieba.lcut 以及 jieba.lcut_for_search 直接返回 list'
lst = jieba.lcut(s, cut_all=False)
print(lst)
# print(' '.join(lst))


seg_list = jieba.cut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")
print("【搜索引擎模式】：" + "/ ".join(seg_list))
