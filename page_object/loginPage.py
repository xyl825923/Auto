# -*- coding: UTF-8 -*-
"""
@Project: jdy-auto-test
@Author : yuling xiao
@Date : 2022/11/9 21:09
@File : loginPage.py
@Describe: 进入是登录页面
"""
import time

import pytest
from selenium.webdriver.common.by import By

from common.pages_util import BasePage
from configs.config_util import get_yaml_config
from configs import read_conf


class LoginPage(BasePage):
    # 页面元素定位
    input_usernsme = (By.XPATH, '//*[@id="login_username"]')
    input_pwd = (By.XPATH, '//*[@id="login_pwd"]')
    button = (By.ID, 'login_btn')
    # 同意
    agree = (By.XPATH, '//*[@id="agree-protocol"]')

    comm_access = '金蝶统一账号/精斗云登录'
    url = get_yaml_config('url', 'ui_test_url')
    username = get_yaml_config('default_login', 'username')
    pwd = get_yaml_config('default_login', 'password')

    # 元素动作
    # @pytest.mark.parametrize()
    def login_echop(self):
        # self.open_browser()
        self.get(self.url)
        self.send_keys(self.input_usernsme, self.username)
        self.send_keys(self.input_pwd, self.pwd)
        self.click(self.button)
        self.click(self.agree)

        # 等待3秒，待session和token都成功返回并存到浏览器中
        time.sleep(3)
        data = self.driver.get_cookies()
        print(data)
        cookie_data = [item["name"] + "=" + item["value"] for item in data]
        cookie = ';'.join(item for item in cookie_data)

        #
        # cookie_string = cookie.split(';')
        # cookie_datas = list(cookie_string.split('='))
        # cookie_datas = cookie_data[10].split('=')
        # cookie_dict = {}
        # for i in range(0, len(cookie_datas)-1):
        #     cookie_dict[cookie_datas[i]] = cookie_datas[i + 1]
        # print(cookie_dict)
        read_conf.write_conf('headers', 'yssession',  cookie.split(";")[10])

    # 登录成功断言
    def get_except_result_access(self):
        self.element_Wait(LoginPage.comm_access)
        return self.get_value(LoginPage.comm_access)

    # 登录失败断言
    def get_except_result_fail(self):
        self.element_Wait(LoginPage.login_fail)
        return self.get_value(LoginPage.login_fail)
