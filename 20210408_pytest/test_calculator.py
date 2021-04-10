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

# 计算器测试类
class TestCal:
    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【计算结束】")

    #测试加法的有效用例
    @pytest.mark.parametrize('a,b,result',[
        [0, 99, 99],     # 整数相加
        [0.0,0.1,0.1],   # 浮点数相加
        [10,-30,-20],    # 正整数和负整数相加
        [-0.1,0.5,0.4],  # 正小数和负小数相加
        [1,1.1,2.1],     # 整数和浮点数相加
        [4294967294,1,4294967295], # int的边界值
        [-9223372036854775808,9223372036854775807,-1], # bigint的边界值
        ['1','2','12'],  # 两个字符串相加
        [[1,2],[2,3],[1,2,2,3]],   # 数字列表相加
        [['abc', '123'], ['def', '456'], ['abc','123', 'def','456']]  # 字符列表相加
    ])
    def test_add_valid(self,a,b,result):
        calc = Calculator()
        assert  result == calc.add(a,b)

    # 测试除法的有效用例
    @pytest.mark.parametrize('a,b,result',[
        [0,1,0],         # 整数相除
        [0.0,0.1,0.0],   # 浮点数相除
        [0.2,-0.1,-2],   # 正负数相除
        [10, 0.1, 100],  # 整数和浮点数相除
        [10, 3, 3.3333333333333333],     # 除不尽的整数被除数，16位小数
        [1.0, 3.0, 0.3333333333333333],  # 除不尽的浮点数被除数，16位小数
        [2.0, 3.0, 0.6666666666666666],  # 除不尽的浮点数被除数，16位小数，截位取数
        [4294967295, 1, 4294967295],     # int的边界值
        [-9223372036854775807, 9223372036854775807, -1] # bigint的边界值
    ])
    def test_div_valid(self,a,b,result):
        calc = Calculator()
        assert  result == calc.div(a,b)



