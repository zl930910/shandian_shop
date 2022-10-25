from common.find_element import findElement
class InventoryPage():

    def __init__(self,driver):
        self.fe = findElement(driver)

    #点击物料tab
    def click_materielTab(self):
        self.fe.get_elements_by_node("el-radio-group","labelTagName")[1].click()

    #点击商品tab
    def click_goodsTab(self):
        self.fe.get_elements_by_node("el-radio-group","labelTagName")[0].click()

    #点击新增物料按钮
    def click_addmaterie(self):
        self.fe.get_element("addmaterieBtn").click()

    #输入物料名称
    def input_materiename(self,value):
        self.fe.get_elements("input_inner")[0].click()
        self.fe.get_elements("input_inner")[0].send_keys(value)

    # 输入物料名称
    def input_materiecode(self, value):
        self.fe.get_elements("input_inner")[1].send_keys(value)

    # 点击物料类型
    def click_materietype(self):
        self.fe.get_elements("input_inner")[2].click()

    # 选择物料类型(成品)
    def click_choosematerie(self):
        self.fe.get_element("el-scrollbar").click()

    #点击添加物料分类
    def click_icon(self):
        self.fe.get_elements("icon-div")[0].click()

    #点击添加品牌
    def click_addbrand(self):
        self.fe.get_elements("icon-div")[1].click()

    #输入保质期
    def input_shelflife(self,value):
        self.fe.get_elements("input_inner")[3].send_keys(value)

    #点击物料单位
    def click_addunit(self):
        self.fe.get_elements("icon-div")[2].click()

    # 弹出框确定按钮
    def click_PopupsureBtn(self):
        self.fe.get_element("sureBtn").click()

    #点击确定按钮
    def click_sureBtn(self):
        self.fe.get_element("el-button--primary").click()

    #获取表格数据数量
    def get_tablesNum(self):
       return self.fe.get_element("tableNum").text

    #点击入库
    def click_Warehousing(self):
        self.fe.get_element("Warehousing").click()

    #选中仓库区域
    def click_area(self):
        self.fe.get_elements_by_node("area","span_tagname")[0].click()

    #点击跳出弹出框(选择仓库)
    def click_link(self):
        self.fe.get_elements("tableListInp")[0].click()

    # 点击跳出弹出框(选择供应商)
    def click_li(self):
        self.fe.get_elements("tableListInp")[1].click()

    #输入进价
    def input_price(self,value):
        self.fe.get_element("Purchaseprice").send_keys(value)

    #输入入库数量
    def input_PurchaseNum(self,value):
        self.fe.get_elements_by_node("weightNum","input_tagName")[0].send_keys(value)

    #点击弹出框确定按钮
    def click_btn(self):
        self.fe.get_element("win-ok").click()

    #点击确认入库按钮
    def click_PurchaseBtn(self):
        self.fe.get_element("orangebtn").click()

    #操作成功后的提示
    def get_tips(self):
       return self.fe.get_element("tips").text

    #点击盘库
    def click_checkinventory(self):
        self.fe.get_element("checkinventory").click()

    #输入盘库数量
    def input_checkinventoryNum(self,value):
        self.fe.get_elements("input_inner")[4].send_keys(value)

    #盘库确认
    def box__btns(self):
        self.fe.get_elements_by_node("el-message-box__btns","button_tagName")[1].click()

    #盘库成功后的提示
    def get_message(self):
       return self.fe.get_elements_by_node("message","p_tagName")[0].text

    #点击查看详情按钮
    def click_details(self):
        self.fe.get_element("details").click()

    #获取物料名称
    def get_Materialname(self):
        self.fe.get_element("Materialname").is_displayed()

    #点击耗损按钮
    def click_Wastage(self):
        self.fe.get_element("Wastage").click()

    #耗损成功提示
    def get_Wastagemessage(self):
       return self.fe.get_element("Wastagemessage").text

    #点击编辑按钮
    def click_editBtn(self):
        self.fe.get_element("warningBtn").click()

    #输入物料名称（编辑）
    def input_editname(self,value):
        self.fe.get_elements("materieledit")[0].clear()
        self.fe.get_elements("materieledit")[0].send_keys(value)

    #输入物料编码
    def input_editcode(self,value):
        self.fe.get_elements("materieledit")[1].clear()
        self.fe.get_elements("materieledit")[1].send_keys(value)

    #点击物料类型
    def click_materialtype(self):
        self.fe.get_elements("input_inner")[0].click()

    #选择物料类型
    def chooseEdittype(self):
        self.fe.get_element("chooseType").click()

    #点击添加分类（编辑）
    def click_addclassify(self):
        self.fe.get_elements("img-div")[0].click()

    #点击添加品牌（编辑）
    def click_editbrand(self):
        self.fe.get_elements("img-div")[1].click()

    #输入保质期
    def input_qualitydata(self,value):
        self.fe.get_element("datainput").send_keys(value)


    #点击确定按钮
    def click_editsureBtn(self):
        self.fe.get_element("yellowBtn").click()

    #点击删除按钮
    def click_deleteBtn(self):
        self.fe.get_element("infoBtn").click()

    #点击确定删除按钮
    def click_deleteSure(self):
        self.fe.get_element("blueBtn").click()
