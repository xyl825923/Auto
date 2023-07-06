# -*- coding: UTF-8 -*-
"""
@Project: Auto_API
@Author : yuling xiao
@Date : 2023/6/15 13:18
@File : read_conf.py
@Describe:
    读取配置文件内容的读取
"""
import configparser
import pathlib

# 配置文件的路径
file = pathlib.Path(__file__).parents[0].resolve() / 'conf.ini'


# 读取配置项
def read_conf(section, option):
    conf = configparser.ConfigParser()
    conf.read(file)
    values = conf.get(section, option)
    return values


def write_conf(section, option, value=None):
    conf = configparser.ConfigParser()
    conf.read(file)
    conf.set(section, option, value)
    with open(file, 'w') as f:
        conf.write(f)

