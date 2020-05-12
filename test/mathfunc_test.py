#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 9:28
# @File     : mathfunc_test.py
# @IDE      : PyCharm


import unittest
from test.mathfunc import *


class MathFuncTest(unittest.TestCase):

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(100, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, sub(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, mul(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, div(6, 3))
        self.assertEqual(2.5, div(5, 2))


if __name__ == '__main__':
    unittest.main()
