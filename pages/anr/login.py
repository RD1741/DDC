import json
import time
from pathlib import Path

from base.seleniumbase import SeleniumDriver
from pages.Login.login import Login
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl
from configurations.config_changes import LOCAL, DEV, TEST


class AnrLogin(Login, SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGIN_BUTTON = "//button[normalize-space()='Login']"
    USERNAME = 'i0116'
    NEXT = "idSIButton9"
    PASSWORD = 'i0118'
    CONTINUE_BUTTON = "idSIButton9"
    open_page = "//ul[@class='nav flex-column']//li[1]"
    anr_profile = "//div[@class='user--icon']"
    anr_logout = "//div[@class='user-logout']//ul//li//a"
    acc = "//div[@role='listitem']"
    add_acc = "//div[@id='otherTile']//div[@class='table-row']"
    loader = "//*[@class='loader']"
    STAY_SIGHN_IN_BUTTON = "idSIButton9"
    anr_login_spinner = "//*[@class='spinner-loading']"

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
        self.waitForElement(self.anr_profile)
        self.waitForElementPresent(self.loader)
        self.ElementClick(self.anr_profile)
        self.waitForElement(self.anr_profile, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.anr_profile, locatorType="xpath")

    def click_logout(self):
        self.waitForElement(self.anr_profile, locatorType="xpath")
        self.ElementClick(self.anr_profile, locatorType="xpath")

    def click_logout_acc(self):
        self.waitForElement(self.acc, locatorType="xpath")
        self.ElementClick(self.acc, locatorType="xpath")

    def clickStaySignInButton(self):
        self.waitForElement(self.STAY_SIGHN_IN_BUTTON, "id")
        self.ElementClick(self.STAY_SIGHN_IN_BUTTON, "id")

    def AncLogin(self, email, password):
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.click_login_link()
        self.pick_account()
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.enter_email(email)
        self.click_nextbutton()
        self.enter_password(password)
        self.click_continue_button()
        self.clickStaySignInButton()

    def AncLogout(self):
        self.click_profile()
        self.click_logout()
        self.click_logout_acc()
        self.click_add_acc()
        time.sleep(2)

    def verifyLoginTest(self):
        self.waitForElement(self.anr_profile, locatorType="xpath")
        result = self.isElementPresent(self.anr_profile, locatorType="xpath")
        # self.log.info("Login successfully")
        return result

    def verifyLogoutTest(self):
        self.waitForElement(self.LOGIN_BUTTON, locatorType="xpath")
        logout_result = self.isElementPresent(self.LOGIN_BUTTON, locatorType="xpath")
        self.log.info("Logout Successfully")
        return logout_result
