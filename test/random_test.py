#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 9:20
# @File     : random_test.py
# @IDE      : PyCharm


import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.seq = range(10)

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError, random.shuffle, (1,2,3))


if __name__ == '__main__':
    unittest.main()