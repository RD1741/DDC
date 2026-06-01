import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumDriver
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class scheduling(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    util = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    caseId = 'value'
    apply_bt = "//button[@type='button'][normalize-space()='Apply']"
    view_button = "//table[@class='table table-layout-fixed']//tbody//tr[1]//td[9]//ul//li//a"
    ssn = "//table[@class='table ng-star-inserted'][1]//tbody//tr[11]//td"
    reset_bt = "//button[normalize-space()='Reset']"
    sch_profile = "//div[@class='user--icon']"
    sch_logout = "//div[@class='user-drop-down active']//ul//li//a"
    acc = "//div[@role='listitem']"
    add_acc = "//div[@id='otherTile']//div[@class='table-row']"
    loader = "//*[@class='loader']"
    sign_in_title = "//div[@id='loginHeader']//div"
    case = "//div[@class='header']//h1//span"
    ver_m_f_name = "//table[@class='table ng-star-inserted'][1]//tbody//tr[4]//td"
    ver_m_l_name = "//table[@class='table ng-star-inserted'][1]//tbody//tr[6]//td"
    ver_c_f_name = "//table[@class='table ng-star-inserted'][2]//tbody//tr[4]//td"
    ver_c_l_name = "//table[@class='table ng-star-inserted'][2]//tbody//tr[6]//td"
    ver_af_f_name = "//table[@class='table ng-star-inserted'][3]//tbody//tr[4]//td"
    ver_af_l_name = "//table[@class='table ng-star-inserted'][3]//tbody//tr[6]//td"
    ver_m_sch_st = "//div[@class='case-table']//table//tbody//tr[1]//td[12]"
    ver_c_sch_st = "//div[@class='case-table']//table//tbody//tr[2]//td[12]"
    ver_af_sch_st = "//div[@class='case-table']//table//tbody//tr[3]//td[12]"
    expand = "//div[@class='expand-btn']"
    ddc_req_id = 'ddcRequestID'
    req_apply = "//button[@class='btn btn-primary btn-small']"
    req_view = "//div[@class='table-wrapper']//table//td[9]//a"
    linked_cases = "//ul[@class='icon-list']//li[2]"
    case_link = "//div//h1//span[@class='ng-star-inserted']"
    link_case1 = "//div[@class='dropdown-menu related-dropdown-menu show']//li[1]"
    link_case2 = "//div[@class='dropdown-menu related-dropdown-menu show']//li[2]"

    def click_reset_bt(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.reset_bt)
        self.ElementClick(self.reset_bt)

    def send_case_id(self, inp_c_id):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.caseId, locatorType="id")
        self.sendKeys(inp_c_id, self.caseId, locatorType="id")

    def click_on_applyBt(self):
        self.waitForElement(self.apply_bt)
        self.ElementClick(self.apply_bt)

    def click_view_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.view_button)
        self.ElementClick(self.view_button)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def verifyNoData(self, inp_c_id):
        self.click_reset_bt()
        self.send_case_id(inp_c_id)
        self.click_on_applyBt()
        self.click_view_button()
        time.sleep(2)
        self.webScroll(self.scroll_view_element(self.ssn, locatorType="xpath"))
        ver_no_data = self.isElementTextPresent(self.ssn, locatorType="xpath")
        return ver_no_data

    def click_profile(self):
        self.waitForElement(self.sch_profile, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.sch_profile, locatorType="xpath")

    def click_logout(self):
        self.waitForElement(self.sch_logout, locatorType="xpath")
        self.ElementClick(self.sch_logout, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_logout_acc(self):
        self.waitForElement(self.acc, locatorType="xpath")
        self.ElementClick(self.acc, locatorType="xpath")
        self.driver.delete_all_cookies()

    def SchLogout(self):
        self.click_profile()
        self.click_logout()
        self.click_logout_acc()
    def verifySchLogoutTest(self):
        self.waitForElement(self.sign_in_title, locatorType="xpath")
        logout_result = self.isElementPresent(self.sign_in_title, locatorType="xpath")
        self.log.info("Logout Successfully")
        return logout_result

    def verify_case(self, inp_c_id):
        self.click_reset_bt()
        self.send_case_id(inp_c_id)
        self.click_on_applyBt()
        self.click_view_button()
        c = self.isElementTextPresent(self.case, locatorType="xpath")
        case_id = self.util.strip_string(c)
        return case_id

    def find_case(self, inp_c_id):
        self.click_reset_bt()
        self.send_case_id(inp_c_id)
        self.click_on_applyBt()
        self.click_view_button()
    def verify_m_f_name(self):
        self.waitForElement(self.ver_m_f_name)
        self.webScroll(self.scroll_view_element(self.ver_m_f_name, "xpath"))
        m_f = self.isElementTextPresent(self.ver_m_f_name, locatorType="xpath")
        return m_f
    def verify_c_f_name(self):
        self.waitForElement(self.ver_c_f_name)
        self.webScroll(self.scroll_view_element(self.ver_c_f_name, "xpath"))
        c_f = self.isElementTextPresent(self.ver_c_f_name, locatorType="xpath")
        return c_f
    def verify_af_f_name(self):
        self.waitForElement(self.ver_af_f_name)
        self.webScroll(self.scroll_view_element(self.ver_af_f_name, "xpath"))
        af_f = self.isElementTextPresent(self.ver_af_f_name, locatorType="xpath")
        return af_f
    def verify_m_l_name(self):
        self.waitForElement(self.ver_m_l_name)
        self.webScroll(self.scroll_view_element(self.ver_m_f_name, "xpath"))
        m_l = self.isElementTextPresent(self.ver_m_l_name, locatorType="xpath")
        return m_l
    def verify_c_l_name(self):
        self.waitForElement(self.ver_c_l_name)
        self.webScroll(self.scroll_view_element(self.ver_c_l_name, "xpath"))
        c_l = self.isElementTextPresent(self.ver_c_l_name, locatorType="xpath")
        return c_l
    def verify_af_l_name(self):
        self.waitForElement(self.ver_af_l_name)
        self.webScroll(self.scroll_view_element(self.ver_af_l_name, "xpath"))
        af_l = self.isElementTextPresent(self.ver_af_l_name, locatorType="xpath")
        return af_l
    def verify_mother_status(self):
        self.waitForElement(self.ver_m_sch_st)
        self.webScroll(self.scroll_view_element(self.ver_m_sch_st, "xpath"))
        m_sch = self.isElementTextPresent(self.ver_m_sch_st, "xpath")
        return m_sch
    def verify_child_status(self):
        self.waitForElement(self.ver_c_sch_st)
        self.webScroll(self.scroll_view_element(self.ver_c_sch_st, "xpath"))
        c_sch = self.isElementTextPresent(self.ver_c_sch_st, "xpath")
        return c_sch
    def verify_af_status(self):
        self.waitForElement(self.ver_af_sch_st)
        self.webScroll(self.scroll_view_element(self.ver_af_sch_st, "xpath"))
        af_sch = self.isElementTextPresent(self.ver_af_sch_st, "xpath")
        return af_sch

    def click_expand(self):
        self.waitForElement(self.expand)
        self.ElementClick(self.expand)
    def send_ddc_req_id(self, inp_req):
        self.waitForElement(self.ddc_req_id, "id")
        self.webScroll(self.scroll_view_element(self.ddc_req_id, "id"))
        self.sendKeys(inp_req, self.ddc_req_id, "id")

    def click_req_apply(self):
        self.waitForElement(self.req_apply)
        self.webScroll(self.scroll_view_element(self.req_apply, "xpath"))
        self.ElementClick(self.req_apply)

    def click_req_view(self):
        self.waitForElementPresent(self.loader, "xpath")
        self.waitForElement(self.req_view)
        self.ElementClick(self.req_view)

    def find_case_id(self, inp_req):
        self.click_expand()
        self.send_ddc_req_id(inp_req)
        self.click_req_apply()
        self.click_req_view()

    def click_linked_cases(self):
        self.waitForElement(self.linked_cases)
        self.ElementClick(self.linked_cases)
    def verify_linked_cases(self):
        c = self.isElementTextPresent(self.case_link, locatorType="xpath")
        case_id = self.util.strip_string(c)
        self.click_linked_cases()
        l1 = self.isElementTextPresent(self.link_case1, locatorType="xpath")
        l2 = self.isElementTextPresent(self.link_case2, locatorType="xpath")
        LinkedCaseIds = [case_id, l1, l2]
        return LinkedCaseIds









