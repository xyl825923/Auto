# -*- coding: UTF-8 -*-
"""
@Project: jdy-auto-test
@Author : yuling xiao
@Date : 2022/11/9 21:09
@File : loginPage.py
@Describe: 进入是登录页面
"""
import time

from selenium.webdriver.chrome.options import Options

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

    searchKey = (By.ID, 'searchKey')
    searchBtn = (By.ID, 'searchBtn')

    # 进入使用
    into = (By.XPATH, "//*[@id='service']/div[1]/div[4]/div[2]/a[4]/span")

    # 元素动作
    # @pytest.mark.parametrize()
    def get_cookie(self):
        # self.open_browser()
        self.get(self.url)
        self.send_keys(self.input_usernsme, self.username)
        self.send_keys(self.input_pwd, self.pwd)
        self.click(self.button)
        self.click(self.agree)
        self.send_keys(self.searchKey, '杭州自动化测试')
        self.click(self.searchBtn)
        self.click(self.into)
        # 等待3秒，待session和token都成功返回并存到浏览器中
        time.sleep(3)
        data = self.driver.get_cookies()
        print(data)
        cookie_data = [item["name"] + "=" + item["value"] for item in data]
        cookie = '; '.join(item for item in cookie_data)
        # 把cookie写入配置文件中
        read_conf.write_conf('headers', 'cookie', cookie)

    # 登录成功断言
    def get_except_result_access(self):
        self.element_Wait(LoginPage.comm_access)
        return self.get_value(LoginPage.comm_access)

    # 登录失败断言
    def get_except_result_fail(self):
        self.element_Wait(LoginPage.login_fail)
        return self.get_value(LoginPage.login_fail)
