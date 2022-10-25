from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests
from requests.sessions import session

import json

class Test_Selenium():
    def login(self):
        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.6/chromedriver")
        driver.get("https://b.shandian.net/")
        EC.title_contains("闪店商家")
        print(EC.title_contains("闪店商家"))
        driver.find_element_by_id("name").send_keys("13540258963")
        element = driver.find_element_by_id("pass")
        # EC.visibility_of_element_located(element)
        loctor = (By.ID, "pass")
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located(loctor))
        driver.find_element_by_id("pass").send_keys("123456")

        driver.find_element_by_css_selector(".btn").click()
        ss =  session()
        # print(ss.get("https://b.shandian.net/").json())

        driver.close()


if __name__ == '__main__':
    test = Test_Selenium()
    test.login()