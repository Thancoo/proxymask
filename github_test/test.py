#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/7 9:56
# @File     : test.py
# @IDE      : PyCharm


from multiprocessing import Pool

import requests
import json
import os


def get_page(url):
    print('Process %s get %s' % (os.getpid(), url))
    response = requests.get(url)
    if response.status_code == 200:
        return {'url': url, 'text': response.text}


def parse_page(res):
    print('Process %s parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('./db.txt', 'a') as  f:
        f.write(parse_res)


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    p = Pool()
    res_list = list()
    for url in urls:
        res = p.apply_async(get_page, args=(url,), callback=parse_page)
        res_list.append(res)
    p.close()
    p.join()
    print([res.get() for res in res_list])
