# -*- coding: UTF-8 -*-
"""
@Project: Auto_API
@Author : yuling xiao
@Date : 2023/6/15 13:07
@File : keys.py
@Describe:
    关键字驱动类下接口自动化测试的逻辑代码或底层
        关键字驱动类就是代码的二次封装，通过调用关键字方法来实现对应的操作行为
        一般会封装接口常用的请求内容
            1. 请求方法
            2. 请求的相关内容
                请求的url:http://ip:port/path
                请求的nody
                请求的header
        什么环境的接口测试，调用什么环境的ip：port
"""

import requests

# 定义一个接口关键字驱动类
from configs.read_conf import read_conf


class ApiKeys:
    def do_get(self, path, headers=None, params=None, **kwargs):
        # url的拼接
        url = self.set_url(path)
        # 请求头设置
        headers = self.set_headers(headers)
        # 发送请求
        response = requests.get(url=url, headers=headers, params=params, **kwargs)
        # 返回响应
        return response

    def do_post(self, path, headers=None, data=None, json=None, **kwargs):
        # url的拼接
        url = self.set_url(path)
        # 请求头设置
        headers = self.set_headers(headers)
        # 发送请求
        if json == 1:
            response = requests.post(url=url, headers=headers, json=data, **kwargs)
        else:
            response = requests.post(url=url, headers=headers, data=data, **kwargs)
        # 返回响应
        return response

    # url拼接
    def set_url(self, path=None):
        url = read_conf('envs', 'hzOnline')
        if path:
            url = url + path
        return url

    # 设置请求头
    def set_headers(self, headers=None):
        # 设置通用的请求头信息用字典进行保存
        base_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36 ",
            "Content-Type": "application/json",
            "charset": "utf-8",
            "cache-control": "no-cache"
        }
        print(headers)
        if headers:
            headers_list = headers.split('=')
            size = 2
            headers_lists = [headers_list[i * size:(i + 1) * size] for i in range(len(headers_list) - 1)]

            # headers_dict = {}
            # for i in range(len(headers_list) - 1):
            #     headers_dict[headers_list[i]] = headers_dict[headers_list[i + 1]]
            base_headers.update( zip(headers_lists[0], headers_lists[1]))
        if read_conf('headers', 'ysSession'):
            ysSession = read_conf('headers', 'ysSession')
            base_headers['ysSession'] = ysSession
        return headers
