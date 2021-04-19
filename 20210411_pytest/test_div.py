"""
__author__ = 'wangct'
__time__ = '2021-04-11'
"""
import pytest
import yaml
import allure


# 读取yaml存放的数据
def getdata_div():
    with open("./datas/div1.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


# fixture for div
@pytest.fixture(params=getdata_div()["init_datas"],ids=getdata_div()["ids"])
def div_case(request):
    return request.param


# 计算器除法测试类
class TestCal:
    # 调用fixture
    @allure.story("相除")
    def test_div_num(self,init_class,div_case):
        try:
            assert div_case[2] == round(init_class.div(div_case[0], div_case[1]), 2)
        except ZeroDivisionError:
            print("除数为0")

