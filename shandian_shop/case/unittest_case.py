import unittest
class Unit_Test(unittest.TestCase):
    #装饰器
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前")

    def test_01(self):
        print("这是第一条case")

    def test_02(self):
        print("这是第二条case")

    def test_03(self):
        print("这是第三条case")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后")

if __name__ == '__main__':
    # unittest.main()
    #容器的使用
    suite = unittest.TestSuite()
    suite.addTest(Unit_Test("test_01"))
    suite.addTest(Unit_Test("test_02"))
    unittest.TextTestRunner().run(suite)