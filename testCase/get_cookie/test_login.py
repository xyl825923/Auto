# -*- coding: UTF-8 -*-
"""
@Project: jdy-auto-test
@Author : yuling xiao
@Date : 2022/11/7 10:14
@File : test_login.py
"""
import time

import allure
import pytest


from page_object.loginPage import LoginPage


@allure.epic("进销存UI自动化")
@allure.feature('登录')
class TestLogin():

    @pytest.mark.run(order=1)
    @allure.story("登录")
    def test_login(self, beginandend):
        self.driver, self.logger = beginandend
        lp = LoginPage(self.driver)
        lp.login_echop()

        # 断言
        # if '登录成功' in case_description:
        #     assert lp.get_except_result_access() in result
        #     self.logger.info(case_description)
        # elif '登录失败' in case_description:
        #     time.sleep(1)
        #     assert lp.get_except_result_fail() in result
        #     self.logger.info(case_description)
