import time

from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumDriver
from utilities.common_function import CommonUtil


class SchedulePage(SeleniumDriver):
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    schedule = "//ul[@class='nav flex-column']//li[3]"
    request = "value1"
    agency_case = "value2"
    auth_docket = "value3"
    status = "//div[@class='ngx-dropdown-container']//button"
    search = "//input[@placeholder='Search']"
    search_list = "//ul[@class='available-items']//li"
    search_button = "//button[normalize-space()='Search']"
    clear_button = "//button[normalize-space()='Clear']"
    loader = "//*[@class='loader']"
    view = "//tbody/tr[1]/td[7]/ul[1]/li[1]/a[1]"

    def click_schedule(self):
        self.ElementClick(self.schedule)
        self.waitForElementPresent(self.loader)
    def send_request(self, inp_req):
        # self.waitForElement(self.request, locatorType="id")
        self.sendKeys(inp_req, self.request, locatorType="id")

    def send_agencyCase(self, inp_agency):
        # self.waitForElement(self.agency_case, locatorType="id")
        self.sendKeys(inp_agency, self.agency_case, locatorType="id")

    def send_authDocket(self, inp_auth):
        # self.waitForElement(self.auth_docket, locatorType="id")
        self.sendKeys(inp_auth, self.auth_docket, locatorType="id")

    def click_status(self):
        # self.waitForElement(self.status)
        self.ElementClick(self.status)

    def click_search(self):
        # self.waitForElement(self.search)
        self.ElementClick(self.search)

    def status_selection(self, input_status):
        self.waitForElement(self.search_list)
        search_status_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.search_list)
        status_sel = self.utiles.find_dropdown_select(search_status_list, input_status)
        status_sel.click()

    def click_search_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.search_button)

    def click_clear_button(self):
        # self.waitForElement(self.clear_button)
        self.ElementClick(self.clear_button)

    def click_view(self):
        self.ElementClick(self.view)

    def req_search(self, inp_req):
        self.send_request(inp_req)
        self.click_search_button()
        self.click_clear_button()

    def agency_search(self, inp_agency):
        self.send_agencyCase(inp_agency)
        self.click_search_button()
        self.click_clear_button()

    def auth_search(self, inp_auth):
        self.send_authDocket(inp_auth)
        self.click_search_button()
        self.click_clear_button()

    def status_search(self, inp_status):
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_clear_button()

    def req_agency(self, inp_req, inp_agency):
        self.send_request(inp_req)
        self.send_agencyCase(inp_agency)
        self.click_search_button()
        self.click_clear_button()

    def req_auth(self, inp_req, inp_auth):
        self.send_request(inp_req)
        self.send_authDocket(inp_auth)
        self.click_search_button()
        self.click_clear_button()

    def req_status(self, inp_req, inp_status):
        self.send_request(inp_req)
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_clear_button()

    def req_agency_auth(self, inp_req, inp_agency, inp_auth):
        self.send_request(inp_req)
        self.send_agencyCase(inp_agency)
        self.send_authDocket(inp_auth)
        self.click_search_button()
        self.click_clear_button()

    def req_agency_auth_status(self, inp_req, inp_agency, inp_auth, inp_status):
        self.send_request(inp_req)
        self.send_agencyCase(inp_agency)
        self.send_authDocket(inp_auth)
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_view()
        self.click_clear_button()

    def agency_auth(self, inp_agency, inp_auth):
        self.send_agencyCase(inp_agency)
        self.send_authDocket(inp_auth)
        self.click_search_button()
        self.click_clear_button()

    def agency_status(self, inp_agency, inp_status):
        self.send_agencyCase(inp_agency)
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_clear_button()

    def agency_req_status(self, inp_agency, inp_req, inp_status):
        self.send_agencyCase(inp_agency)
        self.send_request(inp_req)
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_clear_button()

    def agency_auth_status(self, inp_agency, inp_auth, inp_status):
        self.send_agencyCase(inp_agency)
        self.send_authDocket(inp_auth)
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_clear_button()

    def auth_status(self, inp_auth, inp_status):
        self.send_authDocket(inp_auth)
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_clear_button()

    def auth_req_status(self, inp_auth, inp_req, inp_status):
        self.send_authDocket(inp_auth)
        self.send_request(inp_req)
        self.click_status()
        self.click_search()
        self.status_selection(inp_status)
        self.click_search_button()
        self.click_clear_button()

    def verifyClickSchedule(self):
        ver_re = self.isElementPresent(self.request, locatorType="id")
        # self.log.info("Schedule clicked")
        return ver_re
