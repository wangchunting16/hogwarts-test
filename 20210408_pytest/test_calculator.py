"""
__author__ = 'wangct'
__time__ = '2021-04-10'
"""
#encoding:utf8
import pytest
from Calculator import Calculator

# 计算器测试类
class TestCal:
    def setup(self):
        self.calc = Calculator()
        print("【开始计算】")

    def teardown(self):
        print("【计算结束】")

    #测试加法的有效用例
    @pytest.mark.parametrize('a,b,result',[
        [0, 99, 99],     # 零数相加
        [123, 789, 912], # 整数相加
        [0.02,0.1,0.12],   # 浮点数相加
        [0.1, 0.2, 0.3],  # 无理浮点数相加
        [10,-30,-20],    # 正整数和负整数相加
        [-0.1,0.5,0.4],  # 正小数和负小数相加
        [1,1.1,2.1],     # 整数和浮点数相加
        [4294967294,1,4294967295], # int的边界值
        [-9223372036854775808,9223372036854775807,-1] # bigint的边界值
    ],ids = ['zero','int','float1','float2','minus','minus_float','int_float','int_max',
           'bigint_max'])
    def test_add_num(self,a,b,result):
        assert  result == round(self.calc.add(a,b),2)

    @pytest.mark.parametrize('a,b,result',[
        ['1','2','12'],  # 两个字符串相加
        [[1,2],[2,3],[1,2,2,3]],   # 数字列表相加
        [['abc', '123'], ['def', '456'], ['abc','123', 'def','456']]  # 字符列表相加
    ],ids=['string','num_list','string_list'])
    def test_add_order_type(self,a,b,result):
        assert  result == self.calc.add(a,b)

    # 测试除法的有效用例
    @pytest.mark.parametrize('a,b,result',[
        [1,0,False],         # 被除数为0
        [0,1,0],             # 零除
        [180, 3, 60],        # 整数相除
        [192.0,0.2,960.0],   # 浮点数相除
        [0.2,-0.1,-2],       # 正负数相除
        [-2.2, -2, 1.1],     # 负数相除
        [10, 0.1, 100],      # 整数和浮点数相除
        [10, 3, 3.33],     # 除不尽的整数被除数，保留2位小数
        [2.0, 3.0, 0.67],  # 除不尽的浮点数被除数，保留2位小数
        [4294967295, 1, 4294967295],     # int的边界值
        [-9223372036854775807, 9223372036854775807, -1] # bigint的边界值
    ],ids = ['zero1','zero2','int','float','minus','minus_float','int_float','irrational_int',
           'irrational_float','int_max','bigint_max'])
    def test_div(self,a,b,result):
        try:
            assert  result == round(self.calc.div(a,b),2)
        except ZeroDivisionError:
            print("除数为0")




