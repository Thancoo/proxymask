#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/14 10:16
# @File     : test.py
# @IDE      : PyCharm


s = tuple

s.mro()
print(s.mro())

mysql_dict = {
    'data': {
        'user': {
            'id_number': {
                'id_number': 100,
                'ip_ad': 80
            }
        }
    }
}

from rules import regex


def check_data(columns: list, data: tuple) -> dict:
    results = construct_columns(columns)
    for item in data:
        for i in item:
            i = str(i).strip()
            if len(i) == 11:
                res = regex.varify_mobile_phone(i)
                if res:
                    index = item.index(i)
                    if results[columns[index]].get('mobile_phone'):
                        results[columns[index]]['mobile_phone'] += 1
                    else:
                        results[columns[index]]['mobile_phone'] = 1
            if len(i) == 18:
                res = regex.varify_id_card(i)
                if res:
                    index = item.index(i)
                    if results[columns[index]].get('id_card'):
                        results[columns[index]]['id_card'] += 1
                    else:
                        results[columns[index]]['id_card'] = 1
            if '@' in i and len(i) > 8:
                res = regex.varify_email(i)
                if res:
                    index = item.index(i)
                    if results[columns[index]].get('email'):
                        results[columns[index]]['email'] += 1
                    else:
                        results[columns[index]]['email'] = 1

    return results


def construct_columns(columns: list) -> dict:
    res = dict()
    for i in columns:
        res[i] = dict()
    return res


if __name__ == '__main__':
    l = ['id', 'name', 'age', 'id_number', 'email', 'ip', 'mobile_phone']
    t = ((
             1, 'one', 18, '112233199512141415', '111linux@gmail.com',
             '192.168.1.108',
             '18818185959'), (
             2, 'two', 19, '1215161199911101683', 'node@qq.com', '195.36.23.1',
             '13825254545'))
    aa = check_data(l, t)
    print(aa)
    construct_columns(l)
