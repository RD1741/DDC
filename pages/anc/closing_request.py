import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class ClosingRequest(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    closing_request = "//ul[@class='nav flex-column']//li[5]//a"
    due_date = "(//span[@class='mat-button-wrapper'])[1]"
    search_bt = "//div[@class='btn-wrap']//button[2]"
    clear_bt = "closingsearchinputssearchclearBtn"
    case_number = "(//input[@id='caseId'])[1]"
    chain_bt = "(//div[@class='form-check-wrap'])[1]//div[1]//input"
    nonChain_bt = "(//div[@class='form-check-wrap'])[1]//div[2]//input"
    original_required_yes = "(//div[@class='form-check-wrap'])[2]//div[1]//input"
    original_required_no = "(//div[@class='form-check-wrap'])[2]//div[2]//input"
    delivery_mode = "(//div[@class='ngx-dropdown-container'])[1]//button"
    delivery_mode_li = "//*[@label='deliveryMode']//div//div//ul//li//a//div"
    channel_sel = "(//div[@class='ngx-dropdown-container'])[2]//button"
    channel_li = "//*[@label='channelName']//div//div//ul//li//a//div"
    state = "(//div[@class='ngx-dropdown-container'])[3]//button"
    state_li = "//*[@label='stateName']//div//div//ul//li//a//div"
    search = "//input[@placeholder='Search']"
    account = "//div[@class='single-select-top']//app-single-select[@id='account']//button[@type='button']"
    account_li = "//app-single-select[@uid='agencyId']//div//ul//li//div"
    case_status = "(//div[@class='ngx-dropdown-container'])[5]//button"
    case_status_li = "//app-single-select[@uid='caseStatusId']//div//ul//li//div"
    test_report = "//ul[@id='myTab']//li[1]"
    viability_report = "//ul[@id='myTab']//li[2]"
    view_report_action = "//div[@class='right-table']//tbody//tr[1]//td//ul//li[1]"
    view_reports = "//div[@class='right-table']//tbody//td//ul//li[1]"
    closing_wizard_action = "//div[@class='right-table']//tbody//tr[1]//td//ul//li[2]"
    closing_wizards = "//div[@class='right-table']//ul//li[2]"
    history_action = "//div[@class='right-table']//tbody//tr[1]//td//ul//li[3]"
    closeIcon = "//button[@aria-label='Close']"
    send_bt = "//button[normalize-space()='Send']"
    confirm = "//button[normalize-space()='Confirm']"
    back_to_listing = "//button[normalize-space()='Back To Listing']"
    testedParty_M_cb = "//button[normalize-space()='Tested Party - M']//div//input"
    closing_wizard_history = "//div[@class='case-wrap']//ul//li//div[1]"
    closing_wizard_comments = "//div[@class='case-wrap']//ul//li//div[2]"
    closing_wizard_help = "//div[@class='case-wrap']//ul//li//div[3]"
    loader = "//*[@class='loader']"
    caseNo = 'caseId'

    def click_closingRequest(self):
        self.waitForElement(self.closing_request, locatorType="xpath")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.closing_request, locatorType="xpath")

    def verifyClosingRequests(self):
        ver_cr = self.isElementPresent(self.case_number, locatorType="xpath")
        return ver_cr

    def click_search_bt(self):
        self.waitForElement(self.search_bt)
        self.ElementClick(self.search_bt)

    def click_clear_bt(self):
        self.waitForElement(self.clear_bt, "id")
        self.ElementClick(self.clear_bt, "id")

    def find_case(self, inp_case_no):
        self.send_case_no(inp_case_no)
        self.click_search_button()
        time.sleep(2)

    def send_case_no(self, inp_case_no):
        self.waitForElement(self.caseNo, locatorType="id")
        self.sendKeys(inp_case_no, self.caseNo, locatorType="id")

    def click_search_button(self):
        self.waitForElement(self.search)
        self.ElementClick(self.search)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        time.sleep(2)


    def click_testReport(self):
        self.waitForElement(self.test_report)
        self.ElementClick(self.test_report)

    def click_viability_Report(self):
        self.waitForElement(self.viability_report)
        self.ElementClick(self.viability_report)

    def click_viewReport(self):
        self.waitForElement(self.view_report_action)
        self.ElementClick(self.view_report_action)

    def click_closingWizard(self):
        self.waitForElement(self.closing_wizard_action)
        self.ElementClick(self.closing_wizard_action)

    def closing_wizard_actions(self):
        self.click_viability_Report()
        clo_wizs = self.elementPresenceCheck(ByType=By.XPATH, locator=self.closing_wizards)
        for clo_wiz in clo_wizs:
            clo_wiz.click()
            self.click_confirm_button()
            self.click_send()

    def click_history(self):
        self.waitForElement(self.history_action)
        self.ElementClick(self.history_action)

    def click_close(self):
        self.waitForElement(self.closeIcon)
        self.ElementClick(self.closeIcon)

    def click_confirm_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.confirm)
        self.ElementClick(self.confirm)
        time.sleep(2)
    def click_send(self):
        self.waitForElement(self.send_bt)
        self.ElementClick(self.send_bt)

    def click_backToListing(self):
        self.waitForElement(self.back_to_listing)
        self.ElementClick(self.back_to_listing)

    def click_due_date(self, inp_start_date, inp_end_date):
        if inp_start_date and inp_end_date is not None:
            self.waitForElement(self.due_date)
            self.select_date_from_calender(inp_start_date, self.due_date, locatorType="xpath")
            self.select_date_from_calender(inp_end_date, self.due_date, locatorType="xpath")
        else:
            pass

    def send_caseNum(self, inp_caseNum):
        self.waitForElement(self.case_number)
        self.sendKeys(inp_caseNum, self.case_number)
        time.sleep(2)

    def find_case(self, inp_case_no):
        self.send_caseNum(inp_case_no)
        self.click_search_bt()
        time.sleep(2)

    def click_caseType(self, input_type):
        if input_type == "Chain":
            self.waitForElement(self.chain_bt, locatorType="xpath")
            self.ElementClick(self.chain_bt, locatorType="xpath")
        elif input_type == "Non Chain (Hard Copy)":
            self.waitForElement(self.nonChain_bt, locatorType="xpath")
            self.ElementClick(self.nonChain_bt, locatorType="xpath")
        else:
            pass

    def click_delivery_Mode(self):
        self.waitForElement(self.delivery_mode)
        self.ElementClick(self.delivery_mode)

    def deliveryMode_selection(self, inp_del_mode):
        if inp_del_mode is not None:
            search_delivery_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.delivery_mode_li)
            del_mode_sel = self.utiles.find_dropdown_select(search_delivery_list, inp_del_mode)
            if del_mode_sel is not False:
                del_mode_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_channel(self):
        self.waitForElement(self.channel_sel)
        self.ElementClick(self.channel_sel)

    def channel_selection(self, inp_channel):
        if inp_channel is not None:
            channel_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.channel_li)
            channel_sel = self.utiles.find_dropdown_select(channel_list, inp_channel)
            if channel_sel is not False:
                channel_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_state(self):
        self.waitForElement(self.state, locatorType="xpath")
        self.ElementClick(self.state, locatorType="xpath")
        time.sleep(2)

    def send_search(self, inp_s):
        self.waitForElement(self.search)
        self.sendKeys(inp_s, self.search)
        time.sleep(2)

    def state_selection(self, inp_state):
        if inp_state is not None:
            search_state_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.state_li)
            state_sel = self.utiles.find_dropdown_select(search_state_list, inp_state)
            if state_sel is not False:
                state_sel.click()
            else:
                self.log.info("input is False")

        else:
            self.log.info("Input is None")

    def click_account(self):
        self.waitForElement(self.account, locatorType="xpath")
        self.ElementClick(self.account, locatorType="xpath")

    def account_selection(self, inp_acc):
        if inp_acc is not None:
            search_acc_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.account_li)
            acc_sel = self.utiles.find_dropdown_select(search_acc_list, inp_acc)
            if acc_sel is not False:
                acc_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_caseStatus(self):
        self.waitForElement(self.case_status)
        self.ElementClick(self.case_status)

    def caseStatus_selection(self, inp_status):
        if inp_status is not None:
            status_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.case_status_li)
            status_sel = self.utiles.find_dropdown_select(status_list, inp_status)
            if status_sel is not False:
                status_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def close_request(self, case_num):
        self.click_closingRequest()
        self.send_caseNum(case_num)
        self.click_search_bt()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_testReport()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_viability_Report()
        self.waitForElementPresent(self.loader, locatorType="xpath")
