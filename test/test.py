#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/15 14:24
# @File     : test.py
# @IDE      : PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        node = head
        c = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + c
            c = s // 10
            node.next = ListNode(s % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node = node.next
        if c != 0:
            node.next = ListNode(1)
        return head.next
