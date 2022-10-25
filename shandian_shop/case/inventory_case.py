from selenium import webdriver
from page.sidebarPage import SidebarPage
from page.inventoryPage import InventoryPage
import time
from case.login_case import LoginCase
from page.matcategoryPage import MetCategory
from page.brandPage import BrandPage
from page.unitPage import UnitPage
from page.SupplierPage import SupplierPage
import unittest
class InventoryCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/zhangli/Documents/autoTest/browser/chromedriver")
        self.driver.get("https://b.shandian.net/")
        # self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.lc = LoginCase(self.driver)#登录
        self.sp = SidebarPage(self.driver)#侧边栏
        self.ip = InventoryPage(self.driver)#物料
        self.mc = MetCategory(self.driver) #分类
        self.bp = BrandPage(self.driver) #品牌
        self.up =  UnitPage(self.driver)#单位
        self.spp = SupplierPage(self.driver)

    #添加物料
    # @unittest.skip("无条件跳过该测试")
    def test_Inventory(self):
        self.lc.login_succ() #登录系统
        self.sp.click_Openh1() #点击展开
        self.sp.click_openli()
        self.ip.click_materielTab()
        # beforeNum = int(self.ip.get_tablesNum()) #获取添加前的数据
        time.sleep(2)
        print(self.ip.get_tablesNum())
        self.ip.click_addmaterie()
        time.sleep(2)
        self.ip.input_materiename("西红柿")
        self.ip.input_materiecode("125452")
        self.ip.click_materietype()
        time.sleep(2)
        self.ip.click_choosematerie()
        #
        self.ip.click_icon()
        time.sleep(2)
        self.mc.choose_category()
        self.ip.click_PopupsureBtn()
        time.sleep(2)
        self.ip.click_addbrand()
        self.bp.choose_onebrand()
        self.ip.click_PopupsureBtn()
        #
        self.ip.input_shelflife("12")
        time.sleep(2)
        self.ip.click_addunit()
        self.up.choose_unit()
        self.ip.click_PopupsureBtn()
        time.sleep(2)
        self.ip.click_sureBtn()
        # self.assertEqual("1",int(self.ip.get_tablesNum())+1)

    #物料入库
    @unittest.skip("无条件跳过该测试")
    def test_Warehousing(self):
        self.lc.login_succ()  # 登录系统
        self.sp.click_Openh1()  # 点击展开
        self.sp.click_openli()
        self.ip.click_materielTab()
        time.sleep(2)
        self.ip.click_Warehousing()#点击入库按钮
        time.sleep(2)
        self.ip.click_link()
        time.sleep(2)
        self.ip.click_area()
        self.ip.click_btn()
        time.sleep(2)
        # #点击供应商
        self.ip.click_li()
        self.spp.choose_supplier()
        self.ip.click_btn()
        time.sleep(2)
        self.ip.input_price("12")
        self.ip.input_PurchaseNum("11")
        #
        self.ip.click_PurchaseBtn()
        self.assertEqual("入库成功",self.ip.get_tips())

    #物料盘库
    @unittest.skip("无条件跳过该测试")
    def test_checkinventory(self):
        self.lc.login_succ()  # 登录系统
        self.sp.click_Openh1()  # 点击展开
        self.sp.click_openli()
        self.ip.click_materielTab()
        time.sleep(2)
        self.ip.click_checkinventory()
        time.sleep(2)
        self.ip.input_checkinventoryNum("100")
        self.ip.click_sureBtn()
        time.sleep(2)
        self.ip.box__btns()
        time.sleep(2)
        self.assertEqual("盘库成功!",self.ip.get_message())

    #物料耗损
    @unittest.skip("无条件跳过该测试")
    def test_details_Wastage(self):
        self.lc.login_succ()  # 登录系统
        self.sp.click_Openh1()  # 点击展开
        self.sp.click_openli()
        self.ip.click_materielTab()
        self.ip.click_details()
        time.sleep(2)
        self.assertTrue("True",self.ip.get_Materialname())
        self.ip.click_Wastage()
        self.ip.input_PurchaseNum("100")
        # time.sleep(10)
        self.ip.click_PurchaseBtn()
        self.assertEqual("耗损成功", self.ip.get_Wastagemessage())

    #物料编辑
    # @unittest.skip("无条件跳过该测试")
    def test_editmateriel(self):
        self.lc.login_succ()  # 登录系统
        self.sp.click_Openh1()  # 点击展开
        self.sp.click_openli()
        self.ip.click_materielTab()
        self.ip.click_details()
        time.sleep(2)
        self.assertTrue("True", self.ip.get_Materialname())
        self.ip.click_editBtn()
        time.sleep(2)
        self.ip.input_editname("番茄")
        self.ip.input_editcode("123456")
        self.ip.click_materialtype()
        self.ip.chooseEdittype()
        self.ip.click_addclassify()
        self.mc.choose_twocategory()
        self.ip.click_btn()
        time.sleep(2)
        self.ip.click_editbrand()
        time.sleep(2)
        self.bp.choose_twobrand()
        self.ip.click_btn()
        time.sleep(2)
        self.ip.click_editsureBtn()
        self.assertEqual("修改物料成功!", self.ip.get_Wastagemessage())
    #
    #删除物料
    # @unittest.skip("无条件跳过该测试")
    def test_materieldelete(self):
        self.lc.login_succ()  # 登录系统
        self.sp.click_Openh1()  # 点击展开
        self.sp.click_openli()
        self.ip.click_materielTab()
        self.ip.click_details()
        time.sleep(2)
        self.assertTrue("True", self.ip.get_Materialname())
        self.ip.click_deleteBtn()
        time.sleep(2)
        self.ip.click_deleteSure()
        # self.assertEqual("修改物料成功!", self.ip.get_Wastagemessage())


    # 后置
    # def tearDown(self):
    #     pass
    #     # self.driver.close()

if __name__ == '__main__':
    unittest.main()