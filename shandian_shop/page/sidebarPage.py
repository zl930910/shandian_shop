from common.find_element import findElement

class SidebarPage():
    def __init__(self,driver):
        self.fe = findElement(driver)

    #点击展开按钮
    def click_Openh1(self):
        self.fe.get_element_by_node("mianNav","openh1").click()
        print(type(self.fe.get_element_by_node("mianNav","openh1")))

    #点击进销存系统
    def click_openli(self):
        self.fe.get_elements_by_node("mianNav","openli")[6].click()

