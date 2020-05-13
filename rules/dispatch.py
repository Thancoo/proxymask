#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/7 18:45
# @File     : dispatch.py
# @IDE      : PyCharm


# import re

# IP mail IDCard


# class BaseField:
#     def __init__(self):
#         self.percent = 0
#         self.key = str()
#         self.field = str()
#         self.number = int()
#
#     def judge(self, key: str, field: str, number: int) -> int:
#         self.key = key
#         self.field = field
#         if len(field) == 0:
#             return 0
#
#     def determine_key(self):
#         pass
#
#     def determine_length(self):
#         pass
#
#     def determine_char(self):
#         pass
#
#     def determine_sequence(self):
#         pass
#
#     def determine_others(self):
#         pass
#
#
# class Email(BaseField):
#     count = [10, 10, 30, 20, 30]
#
#     def judge(self, key: str, field: str, number: int) -> List[bool]:
#         self.field = field.strip()
#         self.key = key.strip()
#         self.number = number
#
#         if len(key) == 0 or len(field) == 0:
#             return [False, False, False, False, False]
#         return [
#             self.determine_key(),
#             self.determine_length(),
#             self.determine_char(),
#             self.determine_sequence(),
#             self.determine_others(),
#         ]
#
#     def determine_key(self) -> bool:
#         for i in find.emails_keys:
#             if i in self.key:
#                 return True
#         return False
#
#     def determine_length(self) -> bool:
#         if 8 <= len(self.field) <= 40:
#             return True
#         return False
#
#     def determine_char(self) -> bool:
#         if '@' in self.field and '.COM' in self.field[-4:].upper():
#             return True
#         return False
#
#     def determine_sequence(self) -> bool:
#         return False
#
#     def determine_others(self) -> bool:
#
#         return False
