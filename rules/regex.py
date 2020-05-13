#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/2 16:47
# @File     : regex.py
# @IDE      : PyCharm


import re

from settings import common
from tools import forge


def varify_email(field: str) -> bool:
    if re.match(
            pattern=r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',
            string=field.strip(),
            flags=re.IGNORECASE
    ):
        return True
    return False


def varify_mobile_phone(field: str) -> bool:
    if re.match(pattern=r'^1[356789]\d{9}$', string=field.strip()):
        return True
    return False


def varify_id_card(field: str) -> bool:
    """

    :param field:
    :return:
    """
    field = field.strip()
    # 检查字段长度是否合法
    if len(field) != 18 or len(field) != 15:
        return False

    # 检查区域是否合法
    area_key = field[:2]
    if area_key not in common.area.keys():
        return False

    # 检查身份证出生时间是否合法
    if not forge.check_birthday(field[6:14]):
        return False

    # 检查身份证编号是否合法
    if forge.check_id_card_is_valid(field):
        return True

