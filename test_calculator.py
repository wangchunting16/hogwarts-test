"""
__author__ = 'wangct'
__time__ = '2021-04-10'
"""

class TestCal:
    @pytest.mark.parametrize('a,b,result',[
        [0,0,0],
        [0.0,0.0,0.0],
        [0.1,-0.1,0.0]
    ])
    def test_add(self,a,b,result):
        calc = Calculator()
        assert  result == calc.add(a,b)

    # def test_div(self,a,b,result):
    #     calc = Calculator()
    #     assert  result - calc.div(a,b)