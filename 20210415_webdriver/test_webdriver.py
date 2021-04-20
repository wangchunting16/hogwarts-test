"""
__author__ = 'wangct'
__time__ = '2021-04-15'
"""
import  selenium
from selenium import  webdriver

# def test_selenium():
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com/")

class TestDriver:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("霍格沃茨测试学院")
        self.driver.find_element_by_id("su").click()
        ele = self.driver.find_element_by_link_text("霍格沃茨测试学院")
        assert ele



