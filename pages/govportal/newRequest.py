import time
import os
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumDriver
from base.base_page import BasePage
from configurations.config_changes import ROOT_DIR
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class NewRequestPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    case_id = 'caseIds'
    search_button = "//div[@class='form__content']" \
                    "//button[@class='btn btn-primary btn-small'][normalize-space()='Search']"
    # search_button = "//div[@class='form__content']//button[normalize-space()='Search']"
    case = "//div[@class='case__content--block position-relative']//div//h1"
    user_acc = "//div[@class='down-click-btn-1 dropdown']//div[@class='user--details']"
    user_acc_search = 'search_input'
    acc_list = "//div[@class='dropdown-menu show']//ul//li//a"
    schedule = "//ul[@class='nav flex-column']//li[3]//a"
    case_files = "//ul[@class='nav flex-column']//li[1]//a"
    agencyno = 'agencyCaseNo'
    view_table = "//div[@class='table-responsive mt-0']//table[2]//tbody"
    view_action = "//table//tbody//tr[1]//td[7]//li[1]//a"
    schedule_status = "//div[@id='v-pills-home']//div[@class='status orange-circle-status']"
    add_request = "//button[normalize-space()='Add Request']"
    agency_case = 'agencyCase'
    auth_docket = 'Docket'
    comments = '//*[@id="panelsStayOpen-collapseTwo"]/form/div/div/div[3]/textarea'
    add = 'dropdownMenuMore'
    add_list = "//div[@class='dropdown-menu show ng-star-inserted']//ul//li"
    delete_party = "//div[@class='result ng-star-inserted']//*[normalize-space()='Delete Party']"
    add_doc = "//button[normalize-space()='Add']"
    tested_mother = "//*[@id='v-pills-tab']//button//span[text()='Mother']"
    tested_child = "//*[@id='v-pills-tab']//button//span[text()='Child']"
    tested_alle_father = "//*[@id='v-pills-tab']//button//span[text()='Alleged Father']"
    added_party = "//button[@id='v-pills-home-tab'][4]//span"
    label_mother = 'Mother'
    label_child = "Child"
    label_alleged_father = "Alleged Father"
    not_schedule = "inlineRadio1"
    to_schedule = 'inlineRadio2'
    retest = 'inlineRadio3'
    first_name = 'testPartyName'
    last_name = 'lastName'
    race = "//app-single-select[@class='ng-star-inserted']//div//button"
    search = "//input[@placeholder='Search']"
    race_search_list = "//*[@label='race']/div/div/ul/li"
    cal_click = "//*[@aria-label='Open calendar']//span[1]"
    month_year = "//button[@aria-label='Choose month and year']"
    calender = "//*[@class='mat-calendar-body']/tr/td"
    range_list = "//span[@class='mat-button-wrapper']/span"
    previous_cal = "//button[@aria-label='Previous 24 years']"
    next_cal = "//button[@class='mat-focus-indicator mat-calendar-next-button mat-icon-button " "mat-button-base']"
    ssn_digit = 'ssn'
    address = 'address1'
    country = "//app-single-select[@label='countryName']//div"
    country_search_list = "//*[@label='countryName']/div/div/ul/li"
    zip = 'pin'
    state = "//app-single-select[@label='regionName']//div"
    state_list = "//*[@label='regionName']/div/div/ul/li"
    city = "//app-city-select//div[@class='ngx-dropdown-container']//button"
    city_search = "//input[@placeholder='Type at least 3 characters']"
    incarcerated = 'Incarcerated'
    Facility = 'Facility'
    Inmate = 'Inmate'
    incarcerated_cal = "//div[@class='mat-form-field-suffix ng-tns-c68-3 ng-star-inserted']//button"
    contact_person = 'contactPerson'
    name = 'name'
    phone = 'Phone'
    deceased = 'Deceased'
    deceased_cal = "//*[@data-mat-calendar = 'mat-datepicker-11']//button"
    label_incarcerated = 'Incarcerated'
    label_contact_person = 'Add’l Contact Person'
    label_deceased = 'Deceased'
    sample_id = 'sampleID'
    sample_search = "//div[@class='col-md-4 search-input ng-star-inserted'][1]//div[1]"
    sample_fname = "//div[@class='col-md-3 ng-star-inserted'][1]//input"
    sample_lname = "//div[@class='col-md-3 ng-star-inserted'][2]//input"
    sample_ssn = "//div[@class='col-md-2 ng-star-inserted']//input[@id='ssn']"
    sample_cal = "//div[@class='col-md-2 ng-star-inserted']//button[@aria-label='Open calendar']//span[1]"
    tested_party_role = "//app-single-select[@label='role']//div"
    # party_list = "//ul[@class='available-items']//li"
    samp_res = "//tbody/tr[1]/td[1]/div[1]/input[1]"
    use_sam = "//button[normalize-space()='Use Selected Sample']"
    add_new = "//button[normalize-space()='Add New Party']"
    agency_case_no = 'agencyCaseNo'
    agency_search = "//div[@class='col-md-4 search-input ng-star-inserted'][2]//div[1]"
    agency_search_button = "//button[normalize-space()='Search']"
    radio1 = 'inlineRadiosample1'
    auth_doc = 'docket'
    fname = 'firstName'
    retest_checkbox = 'Address'
    submit = "//button[normalize-space()='Submit']"
    cancel_button = "//button[normalize-space()='Cancel']"
    success = 'success'
    cancel = 'cancel'
    login_button = "//button[@type='submit']"
    request = 'value1'
    copy = "//a[@class='mat-tooltip-trigger copy']"
    paste = "//a[@class='mat-tooltip-trigger paste disabled']"
    table = "//table[@class='table schedule-table']"
    profile = "//div[@class='user--icon']"
    profile_list = "//div[@class='user-drop-down active']//ul//li"
    user_mail = 'userName'
    loader = "//*[@class='loader']"
    use_select = "//button[normalize-space()='Use Selected Sample']"
    close = "//button[@aria-label='Close']"
    auth_search = "//div[@class='col-md-4 search-input ng-star-inserted'][3]//div"
    download_icon = "//tbody/tr[1]/td[7]/ul[1]/li[2]/a[1]"
    download = 'download'
    doc_icon = "//div[@class='main__content--header']//ul//li"
    back = "//div[@class='d-flex align-items-center']"
    browse = "//input[@type='file']"
    file_add = "//div[@class='drag ng-star-inserted']"
    docc_add = "//button[normalize-space()='Add']"
    add_bt = "//a[normalize-space()='Add']"
    document = "//app-single-select[@label='documentType']//button[@type='button']//span[2]"
    search_doc = "//input[@placeholder='Search']"
    doc_list = "//ul[@class='available-items']//li"
    close_icon = "//button[@aria-label='Close']"
    party_list = "//div[@class='ngx-dropdown-list-container dropdown-search ng-star-inserted']//ul//li//input"
    tested_party_bt = "//div[@class='ngx-dropdown-button']//span[@class='nsdicon-angle-down']"
    agency = 'value2'
    searchButton = "//button[normalize-space()='Search']"
    table_element = "//tbody/tr[1]/td[2]"
    clearButton = "//button[normalize-space()='Clear']"
    request_id = "//tbody//tr[1]//td[1]"
    c_id = "//div[@class='case__content--header d-flex justify-content-between align-content-center']//h1"
    acc_status = "//tbody//tr//div//div[1]"
    ver_ssn_ed = "//table[@class='table ng-star-inserted'][1]//tbody//tr[5]//td"
    gov_profile = "//div[@class='user--icon']"
    gov_logout = "//div[@class='user-drop-down active']//div//ul//li//a"
    acc = "//div[@role='listitem']"
    add_acc = "//div[@id='otherTile']//div[@class='table-row']"
    sign_in_title = "//div[@id='loginHeader']//div"
    acc_text = "//div[@class='user ng-star-inserted']//div[@class='user--name']"
    SEARCH_CLEAR = "//*[@class='form__content']/div/div/button[1]"
    scan_close = "//div[@class='dynamsoft-dialog-close']"
    no_of_docc = "//div[@class='back remove-icon justify-content-between']"
    no_data = "//div[@class='page__listing']//p"
    success_msgg = "//app-toaster//div[2]//h2"
    toaster_close = "//button[@data-bs-dismiss='toast']"
    m_name = "//table[@class='table ng-star-inserted'][1]//tr[1]//td[1]"
    c_name = "//table[@class='table ng-star-inserted'][2]//tr[1]//td[1]"
    af_name = "//table[@class='table ng-star-inserted'][3]//tr[1]//td[1]"
    agency_value = "//form[@name='scheduleFilterForm']//div[2]//input"
    ver_f_name = "//label[@for='firstName']//following-sibling::p"
    ver_l_name = "//label[@for='lastName']//following-sibling::p"
    ver_child = "//div[@id='v-pills-tab']//button[2]"
    ver_af = "//div[@id='v-pills-tab']//button[3]"

    view_table2 = "//div[@class='table-responsive mt-0']//table[3]//tbody"
    view_table3 = "//div[@class='table-responsive mt-0']//table[4]//tbody"


    def searchClear(self):
        self.waitForElement(self.SEARCH_CLEAR, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.SEARCH_CLEAR, "xpath")

    def send_CaseId(self, inp_case):
        self.waitForElement(self.case_id, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(inp_case, self.case_id, locatorType="id")

    def click_searchButton(self):
        self.waitForElement(self.search_button)
        self.ElementClick(self.search_button)


    def click_table(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.view_table)
        self.ElementClick(self.view_table)

    def actualcase(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ac = self.isElementTextPresent(self.case, locatorType="xpath")
        if ac is not False:
            act = self.utiles.StringSplit(ac)
        else:
            act = False
        return act

    def verifyCaseId(self, inp_case):
        self.send_CaseId(inp_case)
        self.click_searchButton()
        time.sleep(3)
        self.click_table()

    def click_user_acc(self):
        self.waitForElement(self.user_acc)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.user_acc)
        time.sleep(2)

    def send_user_search(self, inp_ac):
        self.waitForElement(self.user_acc_search, locatorType="id")
        self.sendKeys(inp_ac, self.user_acc_search, locatorType="id")
        time.sleep(2)

    def user_acc_selection(self, inp_user_acc):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.acc_list)
        user_acc_sel = self.utiles.find_dropdown_select(search_list, inp_user_acc)
        user_acc_sel.click()
        time.sleep(2)
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        # time.sleep(2)

    def AccountSelection(self, inp_ac, inp_user_acc):
        self.click_user_acc()
        self.send_user_search(inp_ac)
        self.user_acc_selection(inp_user_acc)

    def verifyAccount(self):
        self.waitForElement(self.acc_text)
        ac = self.isElementTextPresent(self.acc_text, locatorType="xpath")
        return ac

    def click_schedule(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.schedule)
        self.ElementClick(self.schedule)

    def click_add_request(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.add_request)
        self.ElementClick(self.add_request)

    def send_agency_case(self, agency_no):
        self.waitForElement(self.agency_case, locatorType="id")
        self.sendKeys(agency_no, self.agency_case, locatorType="id")

    def send_auth_docket(self, auth):
        self.waitForElement(self.auth_docket, locatorType="id")
        self.sendKeys(auth, self.auth_docket, locatorType="id")

    def send_comments(self, comment):
        # self.waitForElement(self.comments)
        self.sendKeys(comment, self.comments)

    def click_add(self):
        self.waitForElement(self.add, locatorType="id")
        self.ElementClick(self.add, locatorType="id")

    def add_tested_party_selection(self, inp_tested_party):
        tested_party__list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.add_list)
        tp = self.utiles.find_dropdown_select(tested_party__list, inp_tested_party)
        tp.click()

    def add_party(self, input_tested_party):
        self.scroll_up()
        self.click_add()
        self.add_tested_party_selection(input_tested_party)

    def click_mother(self):
        self.waitForElement(self.tested_mother)
        self.ElementClick(self.tested_mother)

    def click_child(self):
        self.waitForElement(self.tested_child)
        self.ElementClick(self.tested_child)

    def click_alleged_father(self):
        self.waitForElement(self.tested_alle_father)
        self.ElementClick(self.tested_alle_father)

    def sendf_name(self, input_first_name):
        self.waitForElement(self.first_name, locatorType="id")
        self.sendKeys(input_first_name, self.first_name, locatorType="id")

    def sendl_name(self, input_last_name):
        self.waitForElement(self.last_name, locatorType="id")
        self.sendKeys(input_last_name, self.last_name, locatorType="id")

    def click_race(self):
        self.waitForElement(self.race)
        self.ElementClick(self.race)

    def click_search(self):
        self.waitForElement(self.search)
        self.ElementClick(self.search)

    def race_selection(self, inp_race):
        if inp_race is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.race_search_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_race)
            race_sel.click()
        else:
            self.log.info("Input is None")

    def click_country(self):
        # self.waitForElement(self.country)
        self.ElementClick(self.country)

    def country_selection(self, inp_country):
        if inp_country is not None:
            self.click_country()
            self.click_search()
            search_country_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.country_search_list)
            country_sel = self.utiles.find_dropdown_select(search_country_list, inp_country)
            country_sel.click()
        else:
            self.log.info("Input country is None")

    def send_zip(self, zipcode):
        # self.waitForElement(self.zip, locatorType="id")
        self.sendKeys(zipcode, self.zip, locatorType="id")
        self.sendKeys(Keys.TAB, self.zip, locatorType="id")

    def click_state(self):
        self.waitForElement(self.state)
        self.ElementClick(self.state)

    def state_selection(self, inp_state):
        if inp_state is not None:
            self.click_state()
            self.click_search()
            search_state_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.state_list)
            state_sel = self.utiles.find_dropdown_select(search_state_list, inp_state)
            state_sel.click()
        else:
            self.log.info("Input state is None")

    def click_search_button(self):
        self.waitForElement(self.searchButton)
        self.ElementClick(self.searchButton)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def send_sample_id(self, inp_sample_id):
        # self.waitForElement(self.sample_id, locatorType="id")
        self.sendKeys(inp_sample_id, self.sample_id, locatorType="id")

    def send_agency_case_no(self, inp_agency_case_no):
        # self.waitForElement(self.agency_case_no, locatorType="id")
        self.sendKeys(inp_agency_case_no, self.agency_case_no, locatorType="id")

    def send_firstname(self, first_name):
        self.waitForElement(self.fname, locatorType="id")
        self.sendKeys(first_name, self.fname, locatorType="id")

    def send_auth_doc(self, input_auth):
        # self.waitForElement(self.auth_doc, locatorType="id")
        self.sendKeys(input_auth, self.auth_doc, locatorType="id")

    def click_not_schedule(self):
        # self.waitForElement(self.not_schedule, locatorType="id")
        # self.webScroll(self.scroll_view_element(self.not_schedule, locatorType="id"))
        self.waitForElement(self.not_schedule, locatorType="id")
        self.ElementClick(self.not_schedule, locatorType="id")
        self.scroll_Down()

    def click_scheduling(self):
        # self.waitForElement(self.to_schedule, locatorType="id")
        # self.webScroll(self.scroll_view_element(self.to_schedule, locatorType="id"))
        self.waitForElement(self.to_schedule, locatorType="id")
        self.ElementClick(self.to_schedule, locatorType="id")
        self.scroll_Down()

    def click_retest(self):
        self.waitForElement(self.retest, locatorType="id")
        self.webScroll(self.scroll_view_element(self.retest, locatorType="id"))
        self.waitForElement(self.retest, locatorType="id")
        self.ElementClick(self.retest, locatorType="id")
        self.scroll_Down()

    def click_retest_checkbox(self):
        self.waitForElement(self.retest_checkbox, locatorType="id")
        self.ElementClick(self.retest_checkbox, locatorType="id")

    def click_submit(self):
        # self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        self.waitForElement(self.submit)
        self.webScroll(self.scroll_view_element(self.submit, locatorType="xpath"))
        self.ElementClick(self.submit)

    def click_yes(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.success, locatorType="id")
        self.ElementClick(self.success, locatorType="id")
        # self.waitForElementPresent(self.loader, locatorType="xpath")

    def select_party(self, input_tested_party):
        if self.label_mother == input_tested_party:
            self.click_mother()
        elif self.label_child == input_tested_party:
            self.click_child()
        elif self.label_alleged_father == input_tested_party:
            self.click_alleged_father()
        else:
            self.add_party(input_tested_party)

    def select_race(self, input_tested_party, input_race):
        if input_race is not None:
            if self.label_mother == input_tested_party:
                self.click_race()
                self.click_search()
                self.race_selection(input_race)
            elif self.label_alleged_father == input_tested_party:
                self.click_race()
                self.click_search()
                self.race_selection(input_race)
            else:
                print(input_race)
        else:
            self.log.info("Input Race is not None")

    def scheduling_and_not_scheduling(self, input_tested_party, input_first_name="", input_last_name="",
                                      input_race=""):
        self.sendf_name(input_first_name)
        self.sendl_name(input_last_name)
        self.select_race(input_tested_party, input_race)

    def retest_details(self, input_tested_party, inp_sample_id, inp_agency_case_no, input_auth, first_name,
                       input_last_name, input_race):
        self.send_sample_id(inp_sample_id)
        self.send_agency_case_no(inp_agency_case_no)
        self.send_auth_doc(input_auth)
        self.send_firstname(first_name)
        self.sendl_name(input_last_name)
        self.select_race(input_tested_party, input_race)

    def Schedule_details(self, agency_no, auth, comment):
        self.send_agency_case(agency_no)
        self.send_auth_docket(auth)
        self.send_comments(comment)

    def TestedNotSchedule(self, input_tested_party, input_first_name, input_last_name, input_race):
        self.scroll_up()
        self.select_party(input_tested_party)
        self.click_not_schedule()
        self.scheduling_and_not_scheduling(input_tested_party, input_first_name, input_last_name, input_race)

    def TestedSchedule(self, input_tested_party, input_first_name, input_last_name, input_race):
        self.scroll_up()
        self.select_party(input_tested_party)
        self.click_scheduling()
        self.scheduling_and_not_scheduling(input_tested_party, input_first_name, input_last_name, input_race)

    def TestedRetest(self, input_tested_party, inp_sample_id, inp_agency_case_no, input_auth, first_name,
                     input_last_name, input_race):
        self.scroll_up()
        self.select_party(input_tested_party)
        self.click_retest()
        self.retest_details(input_tested_party, inp_sample_id, inp_agency_case_no, input_auth, first_name,
                            input_last_name, input_race)

    def Add_Party_Details(self, input_tested_party, input_first_name, input_last_name, input_race):
        self.click_not_schedule()
        self.scheduling_and_not_scheduling(input_tested_party, input_first_name, input_last_name, input_race)

    def send_agencyno(self, inp_agency):
        self.waitForElement(self.agency, locatorType="id")
        self.sendKeys(inp_agency, self.agency, locatorType="id")

    def verifySchedule(self):
        ver_add_req = self.isElementPresent(self.add_request, locatorType="xpath")
        self.log.info("Add request clicked")
        return ver_add_req

    def verifyAddRequest(self):
        ver_add_req = self.isElementPresent(self.tested_mother, locatorType="xpath")
        self.log.info("Add request clicked")
        return ver_add_req

    def verifyAddParty(self):
        ver_add_party = self.isElementPresent(self.added_party, locatorType="xpath")
        return ver_add_party

    def click_case_files(self):
        self.waitForElement(self.case_files)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.case_files)

    def verifyCaseFile(self):
        self.waitForElement(self.case_id, locatorType="id")
        ver_cs = self.isElementPresent(self.case_id, locatorType="id")
        return ver_cs

    def send_agency(self, inp_agency):
        self.waitForElement(self.agencyno, locatorType="id")
        self.sendKeys(inp_agency, self.agencyno, locatorType="id")

    def click_Button_search(self):
        self.waitForElement(self.search_button)
        self.ElementClick(self.search_button)

    def click_tableview(self):
        self.waitForElement(self.view_table)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.view_table)
        # self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_back(self):
        self.waitForElement(self.back)
        self.ElementClick(self.back)

    def verifyCase(self, inp_agency):
        self.click_case_files()
        self.send_agency(inp_agency)
        self.click_Button_search()
        self.click_tableview()
        id = self.isElementTextPresent(self.c_id, locatorType="xpath")
        e_c_id = self.utiles.StringSplit(id)
        return e_c_id

    def click_delete_party(self):
        self.waitForElement(self.delete_party)
        self.ElementClick(self.delete_party)

    def delete_tested_party(self):
        self.click_child()
        self.click_delete_party()
        self.click_alleged_father()
        self.click_delete_party()

    def verifyRequestId(self):
        self.click_schedule()
        r_id = self.isElementTextPresent(self.request_id, locatorType="xpath")
        time.sleep(2)
        return r_id

    def verifyAccStatus(self, inp_case):
        self.send_CaseId(inp_case)
        self.click_searchButton()
        time.sleep(2)
        status_text = self.isElementTextPresent(self.acc_status, locatorType="xpath")
        return status_text

    def verify_from_anc(self, inp_case):
        self.send_CaseId(inp_case)
        self.click_searchButton()
        self.click_tableview()
        ver_samp_dt = self.isElementTextPresent(self.ver_ssn_ed, locatorType="xpath")
        return ver_samp_dt

    def click_profile(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.gov_profile, locatorType="xpath")
        self.ElementClick(self.gov_profile, locatorType="xpath")

    def click_logout(self):
        self.waitForElement(self.gov_logout, locatorType="xpath")
        self.ElementClick(self.gov_logout, locatorType="xpath")

    def click_logout_acc(self):
        self.waitForElement(self.acc, locatorType="xpath")
        self.ElementClick(self.acc, locatorType="xpath")
        self.driver.delete_all_cookies()

    def GovLogout(self):
        self.click_profile()
        self.click_logout()
        self.click_logout_acc()

    def case_verified(self, inp_agencys):
        self.click_case_files()
        self.send_agency(inp_agencys)
        self.click_Button_search()
        self.click_tableview()

    def verify_created_caseID(self):
        self.waitForElement(self.c_id, locatorType="xpath")
        eid = self.isElementTextPresent(self.c_id, locatorType="xpath")
        e_c_id = self.utiles.StringSplit(eid)
        return e_c_id

    def verifyGovLogoutTest(self):
        self.waitForElement(self.sign_in_title, locatorType="xpath")
        logout_result = self.isElementPresent(self.sign_in_title, locatorType="xpath")
        self.log.info("Logout Successfully")
        return logout_result


    def click_docc_icon(self):
        self.scroll_up()
        self.waitForElement(self.doc_icon)
        self.ElementClick(self.doc_icon)

    def click_addDocc(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.docc_add)
        self.ElementClick(self.docc_add)

    def click_add_bt(self):
        self.waitForElement(self.add_bt)
        self.ElementClick(self.add_bt)

    def click_scan_close(self):
        self.waitForElement(self.scan_close)
        if self.scan_close is not False:
            self.ElementClick(self.scan_close)
        else:
            pass

    def click_document(self):
        self.waitForElement(self.document)
        self.ElementClick(self.document)

    def click_close_icon(self):
        self.waitForElement(self.close_icon)
        self.ElementClick(self.close_icon)

    def document_selection(self):
        self.waitForElement(self.doc_list)
        document_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.doc_list)
        if document_list is not False:
            document_list[0].click()
        else:
            self.log.info("input is False")

    def click_browse_files(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        uploadElement = self.getElement(self.browse, locatorType="xpath")
        path = "test_data/"
        browse_files = os.path.join(ROOT_DIR, path, "report.pdf")
        uploadElement.send_keys(browse_files)

    def click_tested_party(self):
        self.waitForElement(self.tested_party_bt)
        self.ElementClick(self.tested_party_bt)


    def tested_party_selection(self):
        self.waitForElement(self.party_list)
        t_party_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.party_list)
        if t_party_list is not False:
            t_party_list[0].click()
            t_party_list[1].click()
            t_party_list[2].click()
        else:
            self.log.error("party_sel is none")

    def click_upload(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.add_bt)
        button_enable = self.getElement(self.add_bt, locatorType="xpath")
        if button_enable.is_enabled():
            self.ElementClick(self.add_bt)
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            self.log.info("button is not present")

    def get_No_of_Docc(self):
        no_ofDocc = self.isElementTextPresent(self.no_of_docc, locatorType="xpath")
        return no_ofDocc

    def AddDocument(self):

        self.click_docc_icon()
        self.waitForElementPresent(self.loader, "xpath")
        self.click_addDocc()
        self.click_document()
        self.document_selection()
        self.click_browse_files()
        self.click_tested_party()
        self.tested_party_selection()
        self.waitForElementPresent(self.loader, "xpath")
        self.click_upload()
        time.sleep(3)

    def click_clear_button(self):
        self.waitForElement(self.clearButton)
        self.ElementClick(self.clearButton)

    def verifyCaseNotListed(self, inp_agency):
        self.click_clear_button()
        self.click_case_files()
        self.send_agency(inp_agency)
        time.sleep(2)
        self.click_Button_search()
        self.click_tableview()
        ver_list = self.isElementPresent(self.no_data, locatorType="xpath")
        return ver_list

    def toasterMessageClose(self):
        self.waitForElement(self.toaster_close)
        self.ElementClick(self.toaster_close)

    def verifytoaster_msg_success(self):
        self.waitForElement(self.success_msgg)
        self.waitForElementPresent(self.loader, "xpath")
        ele_pre = self.isElementTextPresent(self.success_msgg, locatorType="xpath")
        # time.sleep(2)
        self.toasterMessageClose()
        return ele_pre

    def verify_m_name(self):
        self.waitForElement(self.m_name)
        m = self.isElementTextPresent(self.m_name, locatorType="xpath")
        return m
    def verify_c_name(self):
        self.waitForElement(self.c_name)
        c = self.isElementTextPresent(self.c_name, locatorType="xpath")
        return c
    def verify_af_name(self):
        self.waitForElement(self.af_name)
        af = self.isElementTextPresent(self.af_name, locatorType="xpath")
        return af

    def click_view(self):
        self.waitForElement(self.view_action)
        self.ElementClick(self.view_action)

    def verify_first_name(self):
        self.waitForElement(self.ver_f_name)
        self.webScroll(self.scroll_view_element(self.ver_f_name, "xpath"))
        fname = self.isElementTextPresent(self.ver_f_name, locatorType="xpath")
        return fname
    def verify_last_name(self):
        self.waitForElement(self.ver_l_name)
        lname = self.isElementTextPresent(self.ver_l_name, locatorType="xpath")
        return lname
    def find_agency_case(self, inp_agency):
        self.send_agencyno(inp_agency)
        self.click_search_button()
        self.click_view()
    def verify_schedule_status(self):
        self.waitForElement(self.schedule_status)
        status = self.isElementTextPresent(self.schedule_status, locatorType="xpath")
        return status
    def click_verify_child(self):
        self.waitForElement(self.ver_child)
        self.ElementClick(self.ver_child)
    def click_verify_alleged_father(self):
        self.waitForElement(self.ver_af)
        self.ElementClick(self.ver_af)


    def verifyRequest(self):
        r_id = self.isElementTextPresent(self.request_id, locatorType="xpath")
        time.sleep(2)
        return r_id

    def click_tableview2(self):
        self.waitForElement(self.view_table2)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.view_table2)

    def click_tableview3(self):
        self.waitForElement(self.view_table3)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.view_table3)

    def verifyLinkedCase(self, inp_agency):
        self.click_case_files()
        self.send_agency(inp_agency)
        self.click_Button_search()
        self.click_tableview()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        id1 = self.isElementTextPresent(self.c_id, locatorType="xpath")
        e_c_id1 = self.utiles.StringSplit(id1)
        self.click_back()
        self.click_tableview2()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        id2 = self.isElementTextPresent(self.c_id, locatorType="xpath")
        e_c_id2 = self.utiles.StringSplit(id2)
        self.click_back()
        self.click_tableview3()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        id3 = self.isElementTextPresent(self.c_id, locatorType="xpath")
        e_c_id3 = self.utiles.StringSplit(id3)
        caseIds = [e_c_id1, e_c_id2, e_c_id3]
        caseIds.sort()
        return caseIds




