"""
__author__ = 'wangct'
__time__ = '2021-04-11'
"""
import pytest
import yaml



# 读取yaml存放的数据
def getdata_add1():
    with open("datas/add1.yaml") as f:
        datas = yaml.safe_load(f)
    return datas

def getdata_add2():
    with open("datas/add2.yaml") as f:
        datas = yaml.safe_load(f)
    return datas

# fixture for add
@pytest.fixture(params=getdata_add1()["init_datas"],ids=getdata_add1()["ids"])
def add_case1(request):
    return request.param

@pytest.fixture(params=getdata_add2()["init_datas"],ids=getdata_add2()["ids"])
def add_case2(request):
    return request.param


# 计算器加法测试类
class TestCal:
    # 调用fixture
    def test_add_num(self,init_class,add_case1):
        # self.calc = Calculator()
        assert  add_case1[2] == round(init_class.add(add_case1[0],add_case1[1]),2)
    def test_add_string(self,init_class,add_case2):
        # self.calc = Calculator()
        assert  add_case2[2] == init_class.add(add_case2[0],add_case2[1])