import os
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from base.base_page import BasePage

from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl

class HelpTickets(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    expandbtn = "//div[@class='expand-btn']"
    case_number = "(//input[@id='case'])[1]"
    ticket_no = "//*[@id='ticket']"
    ticket_column = "//tr//th[text()='Ticket # ']"
    loader = "//*[@class='loader']"
    ticketNo = "((//tbody//tr)[1]//td//div)[1]"
    loginBt = "//button[normalize-space()='Login']"
    USERNAME = 'i0116'
    NEXT = "idSIButton9"
    PASSWORD = 'i0118'
    CONTINUE_BUTTON = "idSIButton9"
    dashboard_text = "//div//h1[normalize-space()='Dashboard']"
    filter_bt = "//div[@class='expand-btn filter-applied']"
    dashboard = "//ul[@class='nav flex-column']//li[1]//a"
    apply_bt = "//button[@type='submit']"
    result_table = "//div[@class='scroll-section']//div//a"
    case_status = "dropdownMenuButton1"
    status_list = "//div[normalize-space()='Pending']"
    ok_bt = "//button[normalize-space()='Ok']"
    status_verification = "//button[@id='dropdownMenuButton1']"
    pick_one_profile = "//div[@class='table-row']"
    use_another_acc = "//div[@id='otherTileText']"
    profile = "//div[@class='user--name']"
    profile_icon = "//div[@class='user--icon']"
    logout = "//a[normalize-space()='Logout']"
    ticketNo_verify = "//tr//td[1]//div"

    ticketNo_inp = "//input[@id='ticket']"
    attachment = "//div[@class='attach-file']//div[1]//div"
    from_localstorage = "//div[@class='attach-file']//div[1]//ul//li[1]"
    from_caseDocument = "//a[normalize-space()='From Case Documents']"
    docSelect_checkBox = "//div[@class='d-flex']//input[@type='checkbox']"
    resolutionSelect = "//app-select-dropdown[@formcontrolname='status']//button"
    resolutionSelect_li = "//div[@class='form-wrap']//li"
    nextDeptToReviewBt = "//app-select-dropdown[@formcontrolname='nextToDepartmentReview']//button"
    nextDept_select = "//div[@class='form-wrap']//li"
    comment = "//textarea[@id='comments']"
    attachment_tab = "//ul[@role='tablist']//li[4]//a[text()='Attachment']"
    docCount_inTab = "//div[@class='fix-height']//div[@class='case__listing']//app-help-activities" \
                     "//div//div[1]//div[1]//div[@class='attach mt-2 mb-3 ng-star-inserted'][1]"
    submit_bt = "//span[normalize-space()='Submit']"
    send_bt = "//span[normalize-space()='Send']"
    closeMessage = "toastercloseBtn"
    clearBt = "//button[normalize-space()='Clear']"
    button_loader = ".btn-loader"
    doc_link = "//td//a[@class='doc-link']"
    attachment_bt = "//div[@class='case__listing']//ul//li[4]//a"

    def click_expand(self):
        self.waitForElement(self.expandbtn, locatorType="xpath")
        self.ElementClick(self.expandbtn, locatorType="xpath")

    def verifyHelp(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.ticket_column)
        Ticket_ver = self.isElementPresent(self.ticket_column)
        time.sleep(12)
        return Ticket_ver

    def getTicketNo(self):
        self.waitForElement(self.ticketNo, locatorType="xpath")
        TicketNo = self.isElementTextPresent(self.ticketNo, locatorType="xpath")
        return TicketNo

    def switchWindow(self):
        parent = self.driver.current_window_handle
        win_hand = self.driver.window_handles
        print(len(win_hand))
        child = None
        a = 0
        for wind in win_hand:
            a += 1
            if a == len(win_hand):
                child = wind
        # child = self.driver.window_handles[1]
        self.driver.switch_to.window(child)
        print("tab switched - to help tab")
        return parent

    def switch_back_parent(self, parent):
        self.driver.switch_to.window(parent)
        time.sleep(2)

    def inp_caseNumber(self, inp_s):
        self.waitForElement(self.case_number, locatorType="xpath")
        self.sendKeys(inp_s, self.case_number, locatorType="xpath")

    def inp_ticketNumber(self, inp_s):
        self.waitForElement(self.ticketNo_inp, locatorType="xpath")
        self.sendKeys(inp_s, self.ticketNo_inp, locatorType="xpath")

    def click_applyBt(self):
        self.waitForElement(self.apply_bt, locatorType="xpath")
        self.ElementClick(self.apply_bt, locatorType="xpath")

    def click_ClearBt(self):
        self.waitForElement(self.clearBt, locatorType="xpath")
        self.ElementClick(self.clearBt, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_result_table(self):
        self.waitForElement(self.result_table, locatorType="xpath")
        self.ElementClick(self.result_table, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_ok(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.ok_bt, locatorType="xpath", timeout=300)
        self.ElementClick(self.ok_bt, locatorType="xpath")
        self.waitForElementPresent(self.button_loader, locatorType="css_selector", timeout=100)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_on_status(self):
        self.waitForElement(self.case_status, "id")
        self.ElementClick(self.case_status, "id")

    def status_type(self):
        self.waitForElement(self.status_list)
        t_status_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.status_list)
        if t_status_list is not False:
            t_status_list[0].click()
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            self.log.info("input is False")

    def verify_status(self):
        self.waitForElement(self.status_verification, locatorType="xpath", timeout=300)
        self.webScroll(self.scroll_view_element(self.status_verification, locatorType="xpath"))
        self.waitForElement(self.status_verification, locatorType="xpath")
        # title_result = self.isElementTextPresent(self.status_verification, locatorType="xpath")
        element = self.isElementPresent(self.status_verification)
        element = element.text
        return element

    def click_dashboard(self):
        self.waitForElement(self.dashboard, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.dashboard, locatorType="xpath")

    def click_filterBt(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.filter_bt, locatorType="xpath")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.filter_bt, locatorType="xpath")

    def verify_ticket(self, inp_s):
        self.click_dashboard()
        self.click_expand()
        self.click_ClearBt()
        self.inp_caseNumber(inp_s)
        self.click_applyBt()
        self.click_filterBt()
        self.click_result_table()
        self.click_on_status()
        self.status_type()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        # self.click_ok()

    def click_on_profile(self):
        self.waitForElement(self.profile_icon)
        self.ElementClick(self.profile_icon)

    def click_on_logout(self):
        self.waitForElement(self.logout)
        self.ElementClick(self.logout)

    def profile_pick(self):
        self.waitForElement(self.pick_one_profile)
        self.ElementClick(self.pick_one_profile)

    def logout1(self):
        self.click_on_profile()
        self.click_on_logout()
        self.profile_pick()
        self.driver.delete_all_cookies()

    def click_login_link(self):
        self.waitForElement(self.loginBt)
        self.waitForElementPresent(self.loader, "xpath", "70")
        self.ElementClick(self.loginBt)

    def enter_email(self, email):
        self.waitForElement(self.USERNAME, locatorType="id")
        self.sendKeys(email, self.USERNAME, locatorType="id")

    def click_nextbutton(self):
        self.waitForElement(self.NEXT, locatorType="id")
        self.ElementClick(self.NEXT, locatorType="id")

    def enter_password(self, password):
        self.waitForElement(self.PASSWORD, locatorType="id")
        self.sendKeys(password, self.PASSWORD, locatorType="id")

    def click_continue_button(self):
        self.waitForElement(self.CONTINUE_BUTTON, locatorType="id")
        self.ElementClick(self.CONTINUE_BUTTON, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def verify_helpLogin(self):
        self.waitForElement(self.dashboard_text, locatorType="xpath")
        # title_result = self.isElementTextPresent(self.status_verification, locatorType="xpath")
        element = self.isElementPresent(self.dashboard_text)
        element = element.text
        return element

    def HelpLogin(self, email, password):
        # self.waitForElement(self.LOGIN_BUTTON, locatorType="xpath")
        self.driver.delete_all_cookies()
        status = self.isElementPresent(self.loginBt, locatorType="xpath")
        if status is not False:
            self.click_login_link()
        else:
            pass
        self.enter_email(email)
        self.click_nextbutton()
        self.enter_password(password)
        self.click_continue_button()

    def expectedTicketNo(self):
        Id = self.isElementTextPresent(self.ticketNo_verify, locatorType="xpath")
        # groupId = self.utiles.replaceTicketNo(Id)
        return Id

    def verify_ticket_number(self, inp_s):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        # self.click_dashboard()
        # self.click_expand()
        self.click_filterBt()
        self.click_ClearBt()
        self.inp_ticketNumber(inp_s)
        self.click_applyBt()
        self.click_filterBt()
        # self.click_result_table()

    def click_attach_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.attachment, locatorType="xpath"))
        self.waitForElement(self.attachment, locatorType="xpath")
        self.ElementClick(self.attachment, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def select_attach_caseDoc(self):
        self.waitForElement(self.from_caseDocument, locatorType="xpath")
        self.ElementClick(self.from_caseDocument, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def select_attach_loc(self):
        self.waitForElement(self.from_localstorage, locatorType="xpath")
        self.ElementClick(self.from_localstorage, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def select_checkBox(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.docSelect_checkBox, locatorType="xpath")
        self.ElementClick(self.docSelect_checkBox, locatorType="xpath")

    def click_resolutionBt(self):
        self.waitForElement(self.resolutionSelect, locatorType="xpath")
        self.ElementClick(self.resolutionSelect, locatorType="xpath")

    def select_resolution(self, inp_resolution):
        if inp_resolution is not None:
            search_add_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.resolutionSelect_li)
            resolution_sel = self.utiles.find_dropdown_select(search_add_list, inp_resolution)
            if resolution_sel is not False:
                resolution_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_deptToView(self, inp_dept):
        ele = self.getElement(self.nextDeptToReviewBt, "xpath")
        if ele.is_enabled():
            self.waitForElement(self.nextDeptToReviewBt, locatorType="xpath")
            self.ElementClick(self.nextDeptToReviewBt, locatorType="xpath")
            self.select_deptToView(inp_dept)
        else:
            pass

    def select_deptToView(self, inp_dept):
        if inp_dept is not None:
            search_add_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.nextDept_select)
            dept_sel = self.utiles.find_dropdown_select(search_add_list, inp_dept)
            if dept_sel is not False:
                dept_sel.click()
            else:
                 self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def send_comments(self, inp_comment):
        self.waitForElement(self.comment, "xpath")
        self.ElementClick(self.comment, "xpath")
        self.sendKeys(inp_comment, self.comment, locatorType="xpath")

    def click_attachmentTab(self):
        self.waitForElement(self.attachment_tab, locatorType="xpath")
        self.ElementClick(self.attachment_tab, locatorType="xpath")

    def getDocNo(self):
        self.webScroll(self.scroll_view_element(self.docCount_inTab, locatorType="xpath"))
        self.waitForElement(self.docCount_inTab, locatorType="xpath")
        countNo = self.isElementTextPresent(self.docCount_inTab, locatorType="xpath")
        split_count = self.utiles.docNo_strip(countNo)
        return split_count

    def click_submit(self):
        self.waitForElement(self.submit_bt, locatorType="xpath")
        self.ElementClick(self.submit_bt, locatorType="xpath")

    def click_send(self):
        sendBt_enable = self.waitForElement(self.send_bt, locatorType="xpath")
        if sendBt_enable.is_enabled():
            self.webScroll(self.scroll_view_element(self.send_bt, locatorType="xpath"))
            self.waitForElement(self.send_bt, locatorType="xpath")
            self.ElementClick(self.send_bt, locatorType="xpath")
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            self.log.info("button is not present")

    def closeToasterMsg(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.closeMessage, "id")
        self.ElementClick(self.closeMessage, "id")

    def attachDocToVerify(self, resolution, department, comment):
        self.click_attach_button()
        self.select_attach_caseDoc()
        self.select_checkBox()
        self.click_submit()
        self.click_resolutionBt()
        self.select_resolution(resolution)
        self.click_deptToView(department)
        self.send_comments(comment)
        self.click_send()
        self.click_ok()
        # self.closeToasterMsg()

    def click_attachmentBt(self):
        self.waitForElement(self.attachment_bt, locatorType="xpath")
        self.ElementClick(self.attachment_bt, locatorType="xpath")

    def docVerification(self):
        docLink = self.isElementPresent(self.doc_link, locatorType="xpath")
        return docLink







