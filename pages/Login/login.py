import time

from base.seleniumbase import SeleniumDriver
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl
from configurations.config_changes import *


class Login(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGIN_BUTTON = "homeloginBtn"
    USERNAME = 'i0116'
    NEXT = "idSIButton9"
    PASSWORD = 'i0118'
    CONTINUE_BUTTON = "idSIButton9"
    open_page = "//ul[@class='nav flex-column']//li[1]"
    anc_profile = "headeruserIcon"
    gov_profile = "//div[@class='user--icon']"
    add_acc = "//div[@id='otherTile']//div[@class='table-row']"
    loader = "//*[@class='loader']"
    ANCLOGINBUTTON = ""
    STAY_SIGHN_IN_BUTTON = "idSIButton9"
    login_loader = "//*[@id='loading']/div"
    logo = "homeddcLogo"
    pick_an_account = "//*[@class='table-row']"
    anr_login_spinner = "//*[@class='spinner-loading']"

    def click_login_link(self):
        self.waitForElementPresent(self.login_loader, "xpath", "70")
        self.waitForElement(self.LOGIN_BUTTON, "id")
        self.ElementClick(self.LOGIN_BUTTON, "id")

    def enter_email(self, email):
        self.waitForElement(self.USERNAME, locatorType="id", timeout=400)
        self.sendKeys(email, self.USERNAME, locatorType="id")

    def click_nextbutton(self):
        self.waitForElement(self.NEXT, locatorType="id", timeout=400)
        self.ElementClick(self.NEXT, locatorType="id")

    def enter_password(self, password):
        self.waitForElement(self.PASSWORD, locatorType="id", timeout=400)
        self.sendKeys(password, self.PASSWORD, locatorType="id")

    def click_continue_button(self):
        self.waitForElement(self.CONTINUE_BUTTON, locatorType="id")
        self.ElementClick(self.CONTINUE_BUTTON, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_stay_singnIn_button(self):
        self.waitForElement(self.STAY_SIGHN_IN_BUTTON, "id")
        self.ElementClick(self.STAY_SIGHN_IN_BUTTON, "id")

    def Login(self, email, password):
        self.driver.delete_all_cookies()
        time.sleep(2)
        print("Clear the cookies")
        self.waitForElementPresent(self.login_loader, locatorType="xpath")
        self.waitForElement(self.logo, locatorType="id", timeout=60)
        status = self.isElementPresent(self.logo, locatorType="id")
        print("Status is ", status)
        if status is not False:
            self.click_login_link()
            self.pick_account()
        else:
            pass
        self.enter_email(email)
        self.click_nextbutton()
        self.enter_password(password)
        self.click_continue_button()
        self.click_stay_singnIn_button()

    def verifyAncLoginTest(self):
        # self.waitForElement(self.anc_profile, locatorType="id")
        self.waitForElementPresent(self.login_loader, "xpath")
        self.waitForElement(self.anc_profile, locatorType="id")
        result = self.isElementTextPresent(self.anc_profile, locatorType="id")
        # self.log.info("Login successfully")
        return result

    def verifyGovLoginTest(self):
        self.waitForElement(self.gov_profile, locatorType="xpath")
        result = self.isElementPresent(self.gov_profile, locatorType="xpath")
        # self.log.info("Login successfully")
        return result

    def verifySchLoginTest(self):
        self.waitForElement(self.gov_profile, locatorType="xpath")
        result = self.isElementPresent(self.gov_profile, locatorType="xpath")
        # self.log.info("Login successfully")
        return result

    def pick_account(self):
        elements = self.waitForElements(self.pick_an_account, locatorType="xpath")

        if elements is not None and len(elements) > 1:
            for element in range(0, len(elements)):
                if element == len(elements) - 1:
                    elements[element].click()
                else:
                    print("Element count is matching")
        else:
            print("Element is None or There is not showing existing accounts")

