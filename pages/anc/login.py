import time

from base.seleniumbase import SeleniumDriver
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class AncLogin(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGIN_BUTTON = "//button[@type='button']"
    USERNAME = 'i0116'
    NEXT = "idSIButton9"
    PASSWORD = 'i0118'
    CONTINUE_BUTTON = "idSIButton9"
    anc_profile = "//div[@class='user--icon d-none d-xl-block']"
    anc_logout = "//div[@class='user-logout']//ul//li//a"
    acc = "//div[@role='listitem']"
    add_acc = "//div[@id='otherTile']//div[@class='table-row']"
    loader = "//*[@class='loader']"

    def click_login_link(self):
        self.waitForElement(self.LOGIN_BUTTON)
        self.ElementClick(self.LOGIN_BUTTON)

    def click_add_acc(self):
        self.waitForElement(self.add_acc)
        self.ElementClick(self.add_acc)

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

    def click_profile(self):
        self.waitForElement(self.anc_profile)
        self.waitForElementPresent(self.loader)
        self.ElementClick(self.anc_profile)
        self.waitForElement(self.anc_profile, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.anc_profile, locatorType="xpath")

    def click_logout(self):
        self.waitForElement(self.anc_logout, locatorType="xpath")
        self.ElementClick(self.anc_logout, locatorType="xpath")

    def click_logout_acc(self):
        self.waitForElement(self.acc, locatorType="xpath")
        self.ElementClick(self.acc, locatorType="xpath")

    def AncLogin(self, email, password):
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.click_login_link()
        self.enter_email(email)
        self.click_nextbutton()
        self.enter_password(password)
        self.click_continue_button()

    def AncLogout(self):
        self.click_profile()
        self.click_logout()
        self.click_logout_acc()
        self.click_add_acc()
        time.sleep(2)

    def verifyLoginTest(self):
        self.waitForElement(self.anc_profile, locatorType="xpath")
        result = self.isElementPresent(self.anc_profile, locatorType="xpath")
        # self.log.info("Login successfully")
        return result

    def verifyLogoutTest(self):
        self.waitForElement(self.LOGIN_BUTTON, locatorType="xpath")
        logout_result = self.isElementPresent(self.LOGIN_BUTTON, locatorType="xpath")
        self.log.info("Logout Successfully")
        return logout_result
