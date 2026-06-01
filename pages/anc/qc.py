import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl
from configurations.config_changes import *


class QC(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    qc = "menubarQC"
    qc_samp_id = 'mother'
    qc_c_s_id = "//div[@class='right-table']//table[2]//tbody//tr[1]//td//input"
    qc_af_s_id = "//div[@class='right-table']//table[3]//tbody//tr[1]//td//input"
    # success_msgg = "//app-toaster//div[2]//h2"
    ver_m_s_id = "//table[@class='table ng-star-inserted'][1]//tbody//tr[2]//td"
    ver_c_s_id = "//table[@class='table ng-star-inserted'][2]//tbody//tr[2]//td"
    ver_af_s_id = "//table[@class='table ng-star-inserted'][3]//tbody//tr[2]//td"
    pass_button = "samplecheckpassBtn"
    fail_button = "samplecheckfailBtn"
    submit = "samplechecksubmitBtn"
    clear = "samplecheckclearBtn"
    loader = "//*[@class='loader']"
    table2 = "//div[@class='right-table']//table[2]"
    table3 = "//div[@class='right-table']//table[3]"

    caseDetail_confirmBt = "casedetailslistconfirmBtn"
    R_arrowBt = "//*[@id='caseModal']/div/div/div[1]/div[1]/div[1]/div/div[2]"
    L_arrowBt = "//*[@id='caseModal']/div/div/div[1]/div[1]/div[1]/div/div[1]"
    caseID_verify = "//div[@class='d-flex align-items-center']//h5"

    success_msgg = "//app-toaster//div[@class='alert alert--success ng-star-inserted']"
    error_msg = "//app-toaster//div[@class='alert alert--error ng-star-inserted']"
    closeMessage = "toastercloseBtn"

    backToListing_bt = "samplecheckbacktolistingBtn"
    inp_caseId = "caseNo"
    apply_bt = "qclistingapplyBtn"
    reset_bt = "qclistingresetBtn"
    qualityCheck_action = "//tbody//tr//td[8]//ul//li[1]//a"
    title_verify = "//div/../ancestor::table//tr//th//div/div[1]//text()"
    comment = "//textarea[@placeholder='Enter comments']"
    inp_scanKitBarCode = "//input[@placeholder='Scan Kit Barcode']"
    barCode1_verify = "//div[@class='kit-content-wrap']//div[1]"
    barCode2_verify = "//div[@class='kit-content-wrap']//div[2]"
    Continue = "//div[@class='confirm-buttons']//button[normalize-space()='Skip & continue']"


    def verifySampleWithSuccessMessage(self):
        self.waitForElement(self.success_msgg, timeout=20)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_pre = self.isElementTextPresent(self.success_msgg, locatorType="xpath")
        if ele_pre == "Success":
            ele_pre = True
        else:
            ele_pre = False
        return ele_pre

    def closeToasterMsg(self):
        self.waitForElement(self.closeMessage, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.closeMessage, "id")

    def click_qc(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.qc, "id")
        self.ElementClick(self.qc, "id")

    def send_allSampleIDforQC(self, inp_s_id, testID):
        for c in range(0, len(inp_s_id)):
            table = "//div[@class='right-table']//table[" + str(c) + "]"
            self.waitForElementPresent(self.loader,  "xpath")
            self.QCsampleIds(c, inp_s_id, testID)

    def QCsampleIds(self, count, inp_s_id, testID):
        enterQC = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[1]//td//input"
        # tableNo = "//div[@class='right-table']//table[" + str(count + 1) + "]"
        sampleTable_verify = "//div[@class='right-table']/table[" + str(count + 1) + "]/tbody/tr/td/div"
        print(inp_s_id)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(enterQC, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(inp_s_id[count], enterQC, locatorType="xpath")
        self.driver.find_element(By.XPATH, enterQC).send_keys(Keys.ENTER)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.checkForMultipleCaseID(testID)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        table_view = self.isElementPresent(sampleTable_verify, locatorType="xpath")
        if table_view.get_property('disabled'):
            self.utiles.assertionTrue(table_view, "Failed to pass sampleID")
        else:
            self.log.info("Sample id pass failed")
        # pass_button_visibile = self.getElement(self.pass_button, locatorType="id")
        # if pass_button_visibile.is_enabled():
        #     pass
        # else:
        #     self.log.info("Sample id pass failed")

    def send_sam_id(self, identifier, inp_s_id, testID):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.qc_samp_id, locatorType="id")
        self.sendKeys(inp_s_id, self.qc_samp_id, locatorType="id")
        self.driver.find_element(By.ID, self.qc_samp_id).send_keys(Keys.ENTER)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.checkForMultipleCaseID(testID)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        table2_view = self.isElementPresent(self.table2, locatorType="xpath")
        self.utiles.assertionTrue(table2_view, "Failed to pass sampleID")

    def send_c_sam_id(self, inp_c_s_id):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.qc_c_s_id, locatorType="xpath")
        self.sendKeys(inp_c_s_id, self.qc_c_s_id, locatorType="xpath")
        self.driver.find_element(By.XPATH, self.qc_c_s_id).send_keys(Keys.ENTER)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        table3_view = self.isElementPresent(self.table3, locatorType="xpath")
        self.utiles.assertionTrue(table3_view, "Failed to pass sampleID")
        pass_button_visibile = self.getElement(self.pass_button, locatorType="id")
        if pass_button_visibile.is_enabled():
            pass
        else:
            self.log.info("Sample id pass failed")

    def send_af_sam_id(self, inp_af_s_id):
        if inp_af_s_id is not False:
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.waitForElement(self.qc_af_s_id, locatorType="xpath")
            self.sendKeys(inp_af_s_id, self.qc_af_s_id)
            self.driver.find_element(By.XPATH, self.qc_af_s_id).send_keys(Keys.ENTER)
            self.closeToasterMsg()
            pass_button_visibile = self.getElement(self.pass_button, locatorType="id")
            if pass_button_visibile.is_enabled():
                pass
            else:
                self.log.info("Sample id pass failed")
        else:
            pass

    def click_pass_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        pass_button_visibile = self.getElement(self.pass_button, locatorType="id")
        if pass_button_visibile.is_enabled():
            self.waitForElement(self.pass_button, "id")
            self.ElementClick(self.pass_button, "id")
            self.waitForElementPresent(self.loader, "xpath")
        else:
            self.log.info("pass button disabled")

    def click_submit_button(self):
        self.webScroll(self.scroll_view_element(self.submit, locatorType="id"))
        self.waitForElement(self.submit, "id")
        self.ElementClick(self.submit, "id")
        self.waitForElementPresent(self.loader, "xpath")

    def verifyQc(self):
        self.waitForElement(self.qc_samp_id, locatorType="id")
        ver_qc = self.getElement(self.qc_samp_id, locatorType="id").text
        return ver_qc

    def click_confirmDeatils(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if DEV or TEST:
            caseBt = self.waitForElement(self.caseDetail_confirmBt, "id", timeout=400)
            if caseBt is not False:
                self.ElementClick(self.caseDetail_confirmBt, "id")
            else:
                pass
        else:
            pass

    def expectedCaseID(self):
        Id = self.isElementTextPresent(self.caseID_verify, locatorType="xpath")
        groupId = self.utiles.SplitTestConfirmID(Id)
        return groupId

    def click_Rarrow(self):
        status = False
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.R_arrowBt, "xpath")
        if element is not None:
            attribute_text = element.get_attribute("class")
            if "disabled" not in attribute_text:
                status = True
                element.click()
            else:
                status = False
                print("Element is disabled")
        else:
            print("Element is None")
        return status

    def click_Larrow(self):
        self.waitForElementPresent(self.loader)
        self.waitForElement(self.L_arrowBt)
        self.ElementClick(self.L_arrowBt)

    def checkForMultipleCaseID(self, TestID):
        arrowBt = self.isElementPresent(self.R_arrowBt, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        x = True
        if arrowBt is not False:
            while x:
                status = self.click_Rarrow()
                print("test id is ", TestID, "expected id is ", self.expectedCaseID())
                if TestID == self.expectedCaseID():
                    print(TestID)
                    print(self.expectedCaseID())
                    x = False
                    self.click_confirmBt()
                else:
                    x = status
        else:
            pass

    def click_confirmBt(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.caseDetail_confirmBt, "id")
        self.ElementClick(self.caseDetail_confirmBt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_backToListingBtn(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.backToListing_bt, "id")
        self.ElementClick(self.backToListing_bt, "id")

    def click_resetBT(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.reset_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.reset_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_applyBT(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.apply_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.apply_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_QCactionBtn(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.qualityCheck_action, "xpath")
        self.ElementClick(self.qualityCheck_action, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def input_caseId(self, caseId):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if caseId is not None:
            self.waitForElement(self.inp_caseId, "id")
            self.sendKeys(caseId, self.inp_caseId, "id")
        else:
            pass

    def QCpass_process(self, caseNo):
        self.click_backToListingBtn()
        self.input_caseId(caseNo)
        self.click_applyBT()
        self.click_QCactionBtn()

    def verify_testedParty_title(self):
        actual_title = self.elementPresenceCheck(ByType="xpath", locator=self.title_verify)
        texts = []
        for matched_element in actual_title:
            text = matched_element.text
            texts.append(text)
            print(text)
        return texts

    def click_fail_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        fail_button_visibile = self.getElement(self.fail_button, locatorType="id")
        if fail_button_visibile.is_enabled():
            self.waitForElement(self.fail_button, "id")
            self.ElementClick(self.fail_button, "id")
        else:
            self.log.info("fail button disabled")

    def input_comment(self, comment):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if comment is not None:
            self.waitForElement(self.comment, "xpath")
            self.sendKeys(comment, self.comment, "xpath")
        else:
            pass

    def send_KitbarCode(self, inp_barcode):
        if inp_barcode is not False:
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.waitForElement(self.inp_scanKitBarCode, locatorType="xpath")
            self.sendKeys(inp_barcode, self.inp_scanKitBarCode)
            self.driver.find_element(By.XPATH, self.inp_scanKitBarCode).send_keys(Keys.ENTER)
        else:
            self.log.info("no kitbarcode")

    def BarCode1_Verification(self):
        self.waitForElement(self.barCode1_verify, locatorType="xpath")
        barcode = self.isElementTextPresent(self.barCode1_verify, locatorType="xpath")
        return barcode

    def BarCode2_Verification(self):
        self.waitForElement(self.barCode2_verify, locatorType="xpath")
        barcode = self.isElementTextPresent(self.barCode2_verify, locatorType="xpath")
        return barcode

    def click_yes(self):
        self.waitForElement(self.Continue, "xpath")
        self.ElementClick(self.Continue, "xpath")

    def skipBt_Verification(self):
        self.waitForElement(self.Continue, locatorType="xpath")
        bt = self.isElementPresent(self.Continue, locatorType="xpath")
        return bt

    def submitBtEnablecheck(self):
        self.webScroll(self.scroll_view_element(self.clear, locatorType="id"))
        self.waitForElement(self.submit, locatorType="id")
        button_enable = self.getElement(self.submit, locatorType="id")
        if button_enable.is_enabled():
            pass
        else:
            self.log.info("button is not enabled due to invalid kit barcode")

