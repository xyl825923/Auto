# -*- coding: UTF-8 -*-
"""
@Project: jdy-auto-test
@Author : yuling xiao
@Date : 2022/11/7 9:14
@File : conftest.py
"""

import pytest
from selenium import webdriver
from common.logger_util import LoggerUtil


@pytest.fixture(scope="session", autouse=True, name='beginandend')
def beginToend():
    lu = LoggerUtil()
    logger = lu.get_logger()
    logger.info("----------测试用例执行开始----------")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield (driver, logger)
    logger.info("----------测试用例执行结束----------\n")
    driver.quit()
    lu.remove_handler()


#
# # 控制台输出中午乱码的问题
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
