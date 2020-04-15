#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/15 14:35
# @File     : 003.py
# @IDE      : PyCharm

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution:
    def length_of_longest_string(self, s: str) -> int:
        index = -1
        dic = dict()
        max_length = 0
        for i, c in enumerate(s):
            if c in dic and dic[c] > index:
                index = dic[c]
                dic[c] = i
            else:
                dic[c] = i
                max_length = max(i - index, max_length)
        return max_length


if __name__ == '__main__':
    s = Solution().length_of_longest_string('aabbccdd')
    print(s)
