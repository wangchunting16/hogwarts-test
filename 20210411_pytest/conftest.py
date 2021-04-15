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





# # fixture for div
# @pytest.fixture(params=,ids=)
# def div_case_1(request):
#     return  request.param

