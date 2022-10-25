from common.find_element import findElement
class MetCategory():
    def __init__(self,driver):
      self.fe = findElement(driver)

    #选中一级分类
    def choose_category(self):
        self.fe.get_element("parent").click()

    #选中第二个子分类
    def choose_twocategory(self):
        self.fe.get_element("parent2").click()