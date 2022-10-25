#coding=utf-8
from util.read_ini import Readini
from selenium import webdriver
class findElement():
    def __init__(self,driver):
        self.driver = driver
        self.read_ini = Readini()

    #获取单个元素
    def get_element(self,key,nodeKey=None):
        data = self.read_ini.get_value(key)
        by = data.split(":")[0]
        value = data.split(":")[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "cssSelector":
                return self.driver.find_element_by_css_selector(value)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
            elif by == "tagName":
                return self.driver.find_element_by_tag_name(value)
            elif by == "linkText":
                return self.driver.find_element_by_link_text(value)
        except:
            return None

    #获取多个元素
    def get_elements(self,key):
        data = self.read_ini.get_value(key)
        by = data.split(":")[0]
        value = data.split(":")[1]
        try:
            if by == "id":
                return self.driver.find_elements_by_id(value)
            elif by == "cssSelector":
                return self.driver.find_elements_by_css_selector(value)
            elif by == "xpath":
                return self.driver.find_elements_by_xpath(value)
            elif by == "tagName":
                return self.driver.find_elements_by_tag_name(value)
            elif by == "linkText":
                return self.driver.find_elements_by_link_text(value)
        except:
            return None


    #通过父级元素获取单个子元素
    def get_element_by_node(self,key,nodeKey):
        ele =  self.get_element(key)
        data = self.read_ini.get_value(nodeKey)
        by = data.split(":")[0]
        value = data.split(":")[1]
        # try:
        if by == "id":
            return ele.find_element_by_id(value)
        elif by == "cssSelector":
            return ele.find_element_by_css_selector(value)
        elif by == "xpath":
            return ele.find_element_by_xpath(value)
        elif by == "tagName":
            return ele.find_element_by_tag_name(value)
        elif by == "linkText":
            return ele.find_element_by_link_text(value)
        # except:
        #     return None

    # 通过父级元素获取多个子元素
    def get_elements_by_node(self, key, nodeKey):
        ele = self.get_element(key)
        data = self.read_ini.get_value(nodeKey)
        by = data.split(":")[0]
        value = data.split(":")[1]
        try:
            if by == "id":
                return ele.find_elements_by_id(value)
            elif by == "cssSelector":
                return ele.find_elements_by_css_selector(value)
            elif by == "xpath":
                return ele.find_elements_by_xpath(value)
            elif by == "tagName":
                return ele.find_elements_by_tag_name(value)
            elif by == "linkText":
                return ele.find_elements_by_link_text(value)
        except:
            return "元素没有定位到"


    #输入
    def sendKeys(self,element,value):
        if element!=None:
            element.send_keys(value)
        else:
            return "element没有找到"


if __name__ == '__main__':
   driver = webdriver.Chrome("/Users/zhangli/Documents/autoTest/browser/chromedriver")
   driver.get("https://b.shandian.net/")
   s =  findElement(driver)
   ss = s.get_element("btn")
   print(type(ss))
