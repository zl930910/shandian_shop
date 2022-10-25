from common.find_element import findElement
class SupplierPage():
    def __init__(self,driver):
       self.fe = findElement(driver)

    def choose_supplier(self):
        self.fe.get_element("selectbtns").click()