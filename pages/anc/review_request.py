from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl
from configurations.config_changes import *


class ReviewRequest(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    review_requet = "menubarreviewRequest"
    review_reset = "reviewlistingresetBtn"
    review_applyBt = "reviewlistingapplyBtn"
    loader = "//*[@class='loader']"
    inp_caseID = "//input[@id='value']"
    reviewAction = "//tbody//tr[1]//td[10]//ul//li[1]//a"

    def click_reviewRequest(self):
        self.waitForElement(self.review_requet, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.review_requet, locatorType="id")

    def click_reviewReset_bt(self):
        self.waitForElement(self.review_reset, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.review_reset, locatorType="id")

    def click_reviewApply_bt(self):
        self.waitForElement(self.review_applyBt, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.review_applyBt, locatorType="id")

    def input_caseID(self, caseID):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if caseID is not None:
            self.waitForElement(self.inp_caseID, "xpath")
            self.sendKeys(caseID, self.inp_caseID, "xpath")
        else:
            pass

    def review_ActionList(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.reviewAction)
        self.ElementClick(self.reviewAction)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def reviewRequestProcess(self, caseID):
        self.click_reviewRequest()
        self.click_reviewReset_bt()
        self.input_caseID(caseID)
        self.click_reviewApply_bt()
        self.review_ActionList()



