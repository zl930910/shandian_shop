class BasePage():

    #输入
    def sendKeys(self, element, value):
        if element != None:
            element.send_keys(value)
        else:
            return "element没有找到"