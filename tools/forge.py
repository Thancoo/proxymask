#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 8:46 下午
# @Author   : vadonical
# @Email    : vadonical@gmail.com
# @File     : pgsql.py
# @Software : PyCharm


import re
import random
import datetime

HEADLINE_DISPLAY = True


def check_id_card_is_valid(chinese_id_number: str) -> bool:
    """
    check chinese id card is valid
    :param chinese_id_number:
    :return:
    """
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_dict = {
        0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '7', 8: '4',
        9: '3', 10: '2'
    }
    total = 0
    check_data = chinese_id_number[:17]
    check_bit = chinese_id_number[-1]
    for i, data in enumerate(check_data):
        total += int(data) * weight[i]
    result = check_dict.get(total % 11) == check_bit
    return result


def check_birthday(birthday: str) -> bool:
    """

    :param birthday:
    :return:
    """
    try:
        datetime.datetime.strptime(birthday, '%Y%m%d').date()
    except ValueError:
        return False
    else:
        return '19000101' <= birthday < datetime.date.today().strftime('%Y%m%d')


def is_leap_year(year: int) -> bool:
    """

    :param year:
    :return:
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


# determine index


def determine_index(packet: bytes) -> int:
    """

    :param packet:
    :return:
    """
    select_index = packet.upper().find(bytes('SELECT'))
    create_index = packet.upper().find(bytes('CREATE'))
    if create_index != -1 and create_index < select_index:
        return create_index
    return select_index


# BYTES
def number2bytes(number: int, length: int, reverse=False) -> bytes:
    """
    Change a number to its hexadecimal native bytes
    :param number: the number
    :param length: the length of out, fixed-digit digits zeroing at high digits
    if necessary
    :param reverse: big or little end code
    :return: raw length bytes
    """

    lst = list()
    for i in range(0, length):
        lst.append(number >> (i * 8) & 0xff)
    if reverse:
        return bytes(lst)
    lst.reverse()
    return bytes(lst)


def bytes2number(byte: bytes):
    pass


def list2dict(l1: list, l2: list, reverse=False) -> dict:
    if l1 is None:
        l1 = list()
    if l2 is None:
        l2 = list()
    if not reverse:
        return dict(zip(l1, l2))
    return dict(zip(l2, l1))


def random_words(length=4, mode=0) -> str:
    """

    :param length:
    :param mode:
    :return:
    """
    if length <= 0:
        length = random.randint(1, 16)
    words = list()
    uppers = [i for i in range(65, 91)]
    lowers = [i for i in range(97, 123)]
    if mode == 0:
        lst = lowers
    elif mode == 1:
        lst = uppers
    else:
        lst = uppers + lowers
    for i in range(length):
        words.append(chr(random.choice(lst)))
    return str().join(words)


def split_string_by_length(string: str, length: int) -> list:
    """
    Split string by length
    :param string:
    :param length:
    :return:
    """
    regex = re.compile(r'.{%d}' % length, re.DOTALL)
    lst = re.findall(regex, string)
    lst.append(string[(len(lst) * length):])
    return lst


def headline(header: str, separator='-', length=80):
    """
    Dividing line of separating program running steps by string
    :param header: string you want to separate
    :param separator: separator symbols
    :param length: the length of the dividing line
    :return: None
    """
    if len(header) > length - 4:
        header = 'DEFAULT'
    if HEADLINE_DISPLAY:
        line_num = (length - len(header) - 2) // 2
        print(
            separator * line_num + chr(32) + header + chr(32) + separator * (
                    length - line_num - 2 - len(header)
            )
        )


def bytes2string(packet: bytes) -> str:
    return packet.decode(encoding='utf-8', errors='ignore')


def weighted_average(weighted_list: list, value_list: list) -> float:
    """

    :param weighted_list:
    :param value_list:
    :return:
    """
    if len(weighted_list) != len(value_list):
        print('the weight list does not match the value list')
        return 0
    total = sum(weighted_list)
    rate = 0
    for i in range(len(value_list)):
        rate += value_list[i] * (weighted_list[i] / total)
    return rate


if __name__ == '__main__':
    count = [10, 10, 30, 20, 30]
    value = [100, 80, 60, 100, 100]
    # print(sum(count))
    a = weighted_average(count, value)
    print(a)
