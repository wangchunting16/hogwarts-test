"""
__author__ = 'wangct'
__time__ = '2021-04-11'
"""
import pytest
from Calculator import Calculator

# 将计算器的实例化放到fixture，代替setup
@pytest.fixture(scope='class')
def init_class():
    calc = Calculator()
    yield calc


# 调整用例的顺序
def pytest_collection_modifyitems(session,config,items:list):
    items.reverse() #用例倒序执行
    # 支持用例名中文编码输出
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
