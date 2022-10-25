from common.find_element import findElement
class UnitPage():
    def __init__(self,driver):
        self.fe = findElement(driver)

    #选中单位
    def choose_unit(self):
        self.fe.get_elements_by_node("unit-win","span_tagname")[0].click()