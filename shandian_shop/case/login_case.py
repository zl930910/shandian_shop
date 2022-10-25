import sys
sys.path.append("/Users/zhangli/PycharmProjects/shandian_shop")
from page.loginPage import LoginPage
from selenium import webdriver
import unittest
import time
class LoginCase():
    #前置
    # def setUp(self):
    #     self.driver = webdriver.Chrome("/Users/zhangli/Documents/autoTest/browser/chromedriver")
    #     self.driver.get("https://b.shandian.net/")
    #     self.lp = LoginPage(self.driver)
    def __init__(self,driver):
        self.driver = driver
        self.lp = LoginPage(self.driver)


    #登录成功
    def login_succ(self):
        try:
            self.lp.input_userName("17740831868")
            self.lp.input_password("654321")
            self.lp.click_loginBtn()
            time.sleep(2)
            # self.assertEqual("张丽丽", self.lp.get_username())
            # 店铺选择
            self.lp.click_brandshop()
            self.lp.click_inShop()

            # self.lp.click_shopTab()
            # self.lp.click_shop()
        except:
            print("元素没有定位到或操作的内容有误！")




    # #后置
    # def tearDown(self):
    #     # pass
    #     #出现错误时，截图
    #    for method_name,error in self._outcome.errors:
    #        if error:
    #             case_name = self._testMethodName
    #             file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
    #             self.driver.save_screenshot(file_path)
    #    self.driver.close()


if __name__ == '__main__':
    # lc = LoginCase()
    # lc.test_login_succ()
    unittest.main()