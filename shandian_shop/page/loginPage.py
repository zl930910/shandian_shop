#coding=utf-8
from common.find_element import findElement
class LoginPage():
    def __init__(self,driver):
      self.fe = findElement(driver)
    
    #获取用户名元素
    def input_userName(self,value):
        self.fe.get_element("userName").send_keys(value)

    #获取密码
    def input_password(self,value):
        self.fe.get_element("password").send_keys(value)


    #获取登录按钮
    def click_loginBtn(self):
        self.fe.get_element("btn").click()


    #点击无品牌店铺
    def click_shopTab(self):
        self.fe.get_elements("mulu")[1].click()


    #点击要选中的店铺
    def click_shop(self):
        self.fe.get_element("shop").click()

    #获取登录后的用户名
    def get_username(self):
        self.fe.get_element("user-tit").text()

    #进入加盟店
    def click_brandshop(self):
        self.fe.get_element("shopListBox").click()

    #点击进入门店
    def click_inShop(self):
        self.fe.get_element("inshop").click()
