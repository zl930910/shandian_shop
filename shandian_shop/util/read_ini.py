import configparser
class Readini():

    def __init__(self,node=None,filename=None):

        if filename == None:
            filename = "/Users/zhangli/PycharmProjects/shandian_shop/config/LocalElement.ini"
        if node == None:
            self.node = "loginElement"
        else:
            self.node = node
        self.cf = self.read_ini(filename)

    #读取配置文件中的内容
    def read_ini(self,filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf

    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

if __name__ == '__main__':
    read = Readini("wul")
    print(read.get_value("uss"))


