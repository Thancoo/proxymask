#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/24 18:33
# @File     : args_parser.py
# @IDE      : PyCharm


import configparser


def read_config(config_file_name):
    config = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation()
    )
    config.read(config_file_name)
    return config


if __name__ == '__main__':
    config_file = './conf.ini'
    conf = read_config(config_file)
    print(conf)
