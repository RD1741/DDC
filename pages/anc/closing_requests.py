import time
from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class ClosingRequests(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    closing_requests = "//ul[@class='nav flex-column']//li[5]//a"
    caseNo = 'caseId'
    search = "closingsearchinputssearchBtn"
    closing_wizard = "closingWizardIcon"
    closing_wizards = "//table[@class='table table-layout-fixed']//tbody//tr//td//ul//li[2]//a"
    confirm = "deliverypreferenceconfirmBtn"
    reprint = "deliverypreferencereprintBtn"
    next1 = "newdeliverypreferencenextBtn"
    next2 = "finalreportnextBtn"
    send = "reviewsendreportBtn"
    back_to_listing = "//button[@type='button'][normalize-space()='Back To Listing']"
    edit = "//span[normalize-space()='Edit']"
    loader = "//*[@class='loader']"
    status = "//tbody//div[1]"
    middle_name = "//div[@class='right-table']//table[1]//tr[2]//td//div//input"
    update_Bt = "//div[@class='right']//span[2]"
    clear_bt = "closingsearchinputssearchclearBtn"
    not_listed = "//p[contains(text(),'No Data Available')]"
    success_msgg = "//app-toaster//div[2]//h2"
    toaster_close = "//button[@data-bs-dismiss='toast']"
    manual_closing_popup_text = "//*[@class='modal-body']/div/div/h2"
    closing_request_popup_loader = ".loader"

    def click_closing_requests(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.closing_requests)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.closing_requests)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        time.sleep(2)

    def click_edit(self):
        self.waitForElement(self.edit)
        self.ElementClick(self.edit)

    def verifyClosingRequests(self):
        self.waitForElement(self.caseNo, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ver_cr = self.isElementPresent(self.caseNo, locatorType="id")
        return ver_cr

    def send_case_no(self, inp_case_no):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.caseNo, locatorType="id")
        self.sendKeys(inp_case_no, self.caseNo, locatorType="id")

    def click_search_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.search, "id")
        self.ElementClick(self.search, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        time.sleep(2)

    def find_case(self, inp_case_no):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_clear_bt()
        self.send_case_no(inp_case_no)
        self.click_search_button()
        time.sleep(2)

    def verifyStatus(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ver_st = self.isElementTextPresent(self.status, locatorType="xpath")
        return ver_st

    def click_closing_wizard(self):
        self.waitForElement(self.closing_wizard, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        # self.waitForElement(self.closing_wizard, "id")
        self.ElementClick(self.closing_wizard, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def verifyClosingWizard(self):
        self.waitForElement(self.confirm, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ver_cw = self.isElementPresent(self.confirm, locatorType="id")
        return ver_cw

    def click_confirm_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.confirm, "id")
        self.ElementClick(self.confirm, "id")
        time.sleep(2)

    def click_reprint_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.reprint, "id")
        self.ElementClick(self.reprint, "id")
        time.sleep(2)

    def click_first_next_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.next1, "id")
        self.ElementClick(self.next1, "id")
        time.sleep(2)

    def click_second_next_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.next2, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.next2, "id")
        time.sleep(2)

    def click_send_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.send, "id")
        self.ElementClick(self.send, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_back_to_listing(self):
        # time.sleep(3)
        self.waitForElementPresent(self.closing_request_popup_loader, locatorType="css_selector")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.back_to_listing)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.back_to_listing)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def SendReport(self):
        self.click_confirm_button()
        self.click_first_next_button()
        # self.verifytoaster_msg_success()
        self.click_second_next_button()
        self.click_send_button()
        verification_status = self.verify_manual_closing()
        if verification_status:
            self.click_back_to_listing()
        else:
            print("Verification status is", verification_status)
        return verification_status

    def send_middleName_m(self, inp_middle_name):
        self.waitForElement(self.middle_name, locatorType="xpath")
        self.sendKeys(inp_middle_name, self.middle_name, locatorType="xpath")

    def click_UpdateBt(self):
        self.waitForElement(self.update_Bt)
        self.ElementClick(self.update_Bt)

    def amend_reportEdit(self, inp_middleName):
        self.click_reprint_button()
        self.click_edit()
        self.send_middleName_m(inp_middleName)
        self.click_UpdateBt()
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_clear_bt(self):
        self.waitForElement(self.clear_bt, "id")
        self.ElementClick(self.clear_bt, "id")

    def verifyCaseNotListed(self):
        ver_list = self.isElementPresent(self.not_listed, locatorType="xpath")
        return ver_list

    def verifytoaster_msg_success(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.success_msgg)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_pre = self.isElementTextPresent(self.success_msgg, locatorType="xpath")
        # time.sleep(2)
        toaster_presence = self.isElementPresent(self.toaster_close, locatorType="xpath")
        if toaster_presence is not False:
            self.toasterMessageClose()
        else:
            pass
        return ele_pre

    def toasterMessageClose(self):
        self.waitForElement(self.toaster_close)
        self.ElementClick(self.toaster_close)

    def verify_manual_closing(self):
        self.waitForElementPresent(self.closing_request_popup_loader, locatorType="css_selector")
        element = self.waitForElement(self.manual_closing_popup_text, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if element.text.strip() == "Successfully completed. Sent to Net suite":
            status = True
        else:
            status = False
        return status
