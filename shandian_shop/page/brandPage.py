from common.find_element import findElement
class BrandPage():
    def __init__(self,driver):
        self.fe = findElement(driver)

    #选中品牌(第一个)
    def choose_onebrand(self):
        self.fe.get_elements_by_node("brand-win","span_tagname")[0].click()

    # 选中品牌(第二个)
    def choose_twobrand(self):
        self.fe.get_elements_by_node("brand-win", "span_tagname")[1].click()