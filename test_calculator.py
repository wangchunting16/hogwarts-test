"""
__author__ = 'wangct'
__time__ = '2021-04-10'
"""
import pytest

# 计算器类
class Calculator:
    # 相加
    def add(self,a,b):
        return  a + b

    # 相除
    def div(self,a,b):
        return  a / b

class TestCal:
    @pytest.mark.parametrize('a,b,result',[
        [0,0,0],
        [0.0,0.0,0.0],
        [0.1,-0.1,0.0]
    ])
    def test_add(self,a,b,result):
        calc = Calculator()
        assert  result == calc.add(a,b)


    @pytest.mark.parametrize('a,b,result',[
        [0,1,0],
        [0.0,0.1,0.0],
        [0.1,-0.1,-1]
    ])
    def test_div(self,a,b,result):
        calc = Calculator()
        assert  result == calc.div(a,b)