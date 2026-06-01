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
    loginBt = "//button[normalize-space()='Login']"
    USERNAME = 'i0116'
    NEXT = "idSIButton9"
    PASSWORD = 'i0118'
    CONTINUE_BUTTON = "idSIButton9"
    dashboard_text = "//div//h1[normalize-space()='Dashboard']"
    expandbtn = "//div[@class='expand-btn']"
    filter_bt = "//div[@class='expand-btn filter-applied']"
    case_number = "(//input[@id='case'])[1]"
    ticket_no = "//*[@id='ticket']"
    ticket_column = "//tr//th[text()='Ticket # ']"
    loader = "//*[@class='loader']"
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

    def click_expand(self):
        self.waitForElement(self.expandbtn, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.expandbtn, locatorType="xpath")

    def click_filterBt(self):
        self.waitForElement(self.filter_bt, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.filter_bt, locatorType="xpath")

    def switch_back_parent(self, parent):
        self.driver.switch_to.window(parent)

    def verifyHelp(self):
        self.waitForElement(self.ticket_column)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        Ticket_ver = self.isElementPresent(self.ticket_column)
        return Ticket_ver

    def click_dashboard(self):
        self.waitForElement(self.dashboard, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.dashboard, locatorType="xpath")

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
        return parent

    def inp_caseNumber(self, inp_s):
        self.waitForElement(self.case_number, locatorType="xpath")
        self.sendKeys(inp_s, self.case_number, locatorType="xpath")

    def click_applyBt(self):
        self.waitForElement(self.apply_bt, locatorType="xpath")
        self.ElementClick(self.apply_bt, locatorType="xpath")

    def click_result_table(self):
        self.waitForElement(self.result_table, locatorType="xpath")
        self.ElementClick(self.result_table, locatorType="xpath")

    def click_ok(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.ok_bt, locatorType="xpath")
        self.ElementClick(self.ok_bt, locatorType="xpath")

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
        self.waitForElement(self.status_verification, locatorType="xpath")
        # title_result = self.isElementTextPresent(self.status_verification, locatorType="xpath")
        element = self.isElementPresent(self.status_verification)
        element = element.text
        return element

    def verify_ticket(self, inp_s):
        self.click_dashboard()
        self.click_expand()
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