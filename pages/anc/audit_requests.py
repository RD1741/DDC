import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class AuditRequests(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    audit_requests = "menubarauditRequest"
    title = "//h1[normalize-space()='Audit Requests']"
    Listingtitle = "//caption[text()=' Listing ']/..//div[@class='d-flex align-items-center']"
    case_no = 'value'
    apply = "auditrequestapplyBtn"
    reset = "auditrequestresetBtn"
    audit = "auditrequestIcon"
    auth_doc = 'authentication'
    agency_case = 'agencycaseno'
    scanBarcodeM = "auditcasescanbarcodeBtn"
    M_sample_id = "//div[@class='right-table']//table[1]//tbody//tr[1]//td//button"
    tables_count = "//div[@class='right-table']//table"
    M = "//div[@class='row verify-form-wrapper']//div[1]//input"
    C = "//div[@class='row verify-form-wrapper']//div[2]//input"
    AF = "//div[@class='row verify-form-wrapper']//div[3]//input"
    done = "auditsamplesverificationdoneBtn"
    M_firstname = "//div[@class='right-table']//table[1]//tbody//tr[5]//td//input"
    wrong_sign = "//td[@class='verify']//div[@class='value-mismatch']"
    first_entry = "//input[@value='1']"
    confirm = "//button[normalize-space()='Confirm Selection']"
    C_firstname = "//div[@class='right-table']//table[2]//tbody//tr[5]//td//input"
    AF_firstname = "//div[@class='right-table']//table[3]//tbody//tr[5]//td//input"
    M_lastname = "//div[@class='right-table']//table[1]//tbody//tr[7]//td//input"
    C_lastname = "//div[@class='right-table']//table[2]//tbody//tr[7]//td//input"
    AF_lastname = "//div[@class='right-table']//table[3]//tbody//tr[7]//td//input"
    dob_m = "//div[@class='right-table']//table[1]//tbody//tr[11]//td//button"
    dob_c = "//div[@class='right-table']//table[2]//tbody//tr[11]//td//button"
    dob_af = "//div[@class='right-table']//table[3]//tbody//tr[11]//td//button"
    race_m = "//div[@class='right-table']//table[1]//tbody//tr[13]//td//button"
    race_m_list = "//div[@class='right-table']//table[1]//tbody//tr[13]//td//app-single-select//ul//li//a"
    race_c = "//div[@class='right-table']//table[2]//tbody//tr[13]//td//button"
    race_c_list = "//div[@class='right-table']//table[2]//tbody//tr[13]//td//app-single-select//ul//li//a"
    race_af = "//div[@class='right-table']//table[3]//tbody//tr[13]//td//button"
    race_af_list = "//div[@class='right-table']//table[3]//tbody//tr[13]//td//app-single-select//ul//li//a"
    col_date_m = "//div[@class='right-table']//table[1]//tbody//tr[14]//td//button"
    col_date_c = "//div[@class='right-table']//table[2]//tbody//tr[14]//td//button"
    col_date_af = "//div[@class='right-table']//table[3]//tbody//tr[14]//td//button"
    validate_audit = "auditcasevalidateauditBtn"
    loader = "//*[@class='loader']"
    not_listed = "//p[contains(text(),'No Data Available')]"

    def click_audit_requests(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.audit_requests, "id")
        self.ElementClick(self.audit_requests, "id")
        time.sleep(2)

    def send_case_no(self, inp_case_no):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.case_no, locatorType="id")
        self.sendKeys(inp_case_no, self.case_no, locatorType="id")

    def click_apply_button(self):
        self.waitForElement(self.apply, "id")
        self.ElementClick(self.apply, "id")
        time.sleep(2)

    def click_reset_button(self):
        self.waitForElement(self.reset, "id")
        self.ElementClick(self.reset, "id")

    def click_audit(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.audit, "id")
        self.ElementClick(self.audit, "id")

    def send_auth_doc(self, inp_auth):
        self.waitForElement(self.auth_doc, locatorType="id")
        self.sendKeys(inp_auth, self.auth_doc, locatorType="id")

    def send_agency_case(self, inp_agency):
        self.waitForElement(self.agency_case, locatorType="id")
        self.sendKeys(inp_agency, self.agency_case, locatorType="id")

    def click_m_sample_id(self):
        self.waitForElement(self.M_sample_id)
        self.ElementClick(self.M_sample_id)

    def send_M(self, count, inp_m_fname, m_lastname, m_dob, m_race, m_cdt):
        self.send_Firstname(count, inp_m_fname)
        self.send_Lastname(count, m_lastname)
        self.click_dob(count, m_dob)
        self.click_race(count, m_race)
        self.click_col_date(count, m_cdt)

    def send_C(self, count, inp_c_fname, c_lastname, c_dob, c_race, c_cdt):
        self.send_Firstname(count, inp_c_fname)
        self.send_Lastname(count, c_lastname)
        self.click_dob(count, c_dob)
        self.click_race(count, c_race)
        self.click_col_date(count, c_cdt)

    def send_AF(self, count, inp_c_fname, af_lastname, af_dob, af_race, af_cdt):
        self.send_Firstname(count, inp_c_fname)
        self.send_Lastname(count, af_lastname)
        self.click_dob(count, af_dob)
        self.click_race(count, af_race)
        self.click_col_date(count, af_cdt)

    def click_done(self):
        self.waitForElement(self.done, "id")
        self.ElementClick(self.done, "id")
        time.sleep(2)

    def select_correct_entry(self):
        self.waitForElement(self.wrong_sign)
        self.ElementClick(self.wrong_sign)
        self.waitForElement(self.first_entry)
        self.ElementClick(self.first_entry)
        self.waitForElement(self.confirm)
        self.ElementClick(self.confirm)


    def send_m_firstname(self, inp_m_fname):
        self.waitForElement(self.M_firstname)
        self.webScroll(self.scroll_view_element(self.M_firstname, locatorType="xpath"))
        self.waitForElement(self.M_firstname)
        self.sendKeys(inp_m_fname, self.M_firstname)
        self.select_correct_entry()

    def send_mother_lastname(self, m_lastname):
        self.waitForElement(self.M_lastname)
        self.webScroll(self.scroll_view_element(self.M_lastname, locatorType="xpath"))
        self.waitForElement(self.M_lastname, locatorType="xpath")
        self.sendKeys(m_lastname, self.M_lastname, locatorType="xpath")
        self.select_correct_entry()

    def click_m_dob(self, m_dob):
        if m_dob is not False:
            self.waitForElement(self.dob_m)
            self.webScroll(self.scroll_view_element(self.dob_m, locatorType="xpath"))
            self.waitForElement(self.dob_m)
            self.select_date_from_calender(m_dob, self.dob_m, locatorType="xpath")
            self.select_correct_entry()
        else:
            pass

    def click_m_race(self, inp_race_m):
        if inp_race_m is not False:
            self.waitForElement(self.race_m)
            self.webScroll(self.scroll_view_element(self.race_m, locatorType="xpath"))
            self.waitForElement(self.race_m)
            self.ElementClick(self.race_m)
            self.race_m_sel(inp_race_m)
            # self.select_correct_entry()
        else:
            pass

    def race_m_sel(self, count, inp_race_m):
        race_list = "//div[@class='right-table']//table[" + str(count +1) + "]" \
                    "//tbody//tr[13]//td//app-single-select//ul//li//a"
        if inp_race_m is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=race_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_race_m)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def click_m_col_date(self, m_cdt):
        if m_cdt is not False:
            self.waitForElement(self.col_date_m)
            self.webScroll(self.scroll_view_element(self.col_date_m, locatorType="xpath"))
            self.waitForElement(self.col_date_m)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(m_cdt, self.col_date_m, locatorType="xpath")
            self.select_correct_entry()
        else:
            pass

    def send_c_firstname(self, inp_c_fname):
        if inp_c_fname is not False:
            self.waitForElement(self.C_firstname)
            self.webScroll(self.scroll_view_element(self.C_firstname, locatorType="xpath"))
            self.waitForElement(self.C_firstname)
            self.sendKeys(inp_c_fname, self.C_firstname)
            self.select_correct_entry()
        else:
            pass

    def send_child_lastname(self, c_lastname):
        self.waitForElement(self.C_lastname)
        self.webScroll(self.scroll_view_element(self.C_lastname, locatorType="xpath"))
        self.waitForElement(self.C_lastname, locatorType="xpath")
        self.sendKeys(c_lastname, self.C_lastname, locatorType="xpath")
        self.select_correct_entry()

    def click_c_dob(self, c_dob):
        if c_dob is not False:
            self.waitForElement(self.dob_c)
            self.webScroll(self.scroll_view_element(self.dob_c, locatorType="xpath"))
            self.waitForElement(self.dob_c)
            self.select_date_from_calender(c_dob, self.dob_c, locatorType="xpath")
            self.select_correct_entry()
        else:
            pass

    def click_c_race(self, inp_race_c):
        if inp_race_c is not None:
            self.waitForElement(self.race_c)
            self.webScroll(self.scroll_view_element(self.race_c, locatorType="xpath"))
            self.waitForElement(self.race_c)
            self.ElementClick(self.race_c)
            self.race_m_sel(inp_race_c)
            self.select_correct_entry()
        else:
            pass

    def race_c_sel(self, inp_race_c):
        if inp_race_c is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.race_c_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_race_c)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def click_c_col_date(self, c_cdt):
        if c_cdt is not False:
            self.waitForElement(self.col_date_c)
            self.webScroll(self.scroll_view_element(self.col_date_c, locatorType="xpath"))
            self.waitForElement(self.col_date_c)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(c_cdt, self.col_date_c, locatorType="xpath")
            self.select_correct_entry()
        else:
            pass

    def send_af_firstname(self, inp_af_fname):
        if inp_af_fname is not False:
            self.waitForElement(self.AF_firstname)
            self.webScroll(self.scroll_view_element(self.AF_firstname, locatorType="xpath"))
            self.waitForElement(self.AF_firstname)
            self.sendKeys(inp_af_fname, self.AF_firstname)
            self.select_correct_entry()
        else:
            pass

    def send_Af_lastname(self, af_lastname):
        if af_lastname is not False:
            self.waitForElement(self.AF_lastname)
            self.webScroll(self.scroll_view_element(self.AF_lastname, locatorType="xpath"))
            self.waitForElement(self.AF_lastname, locatorType="xpath")
            self.sendKeys(af_lastname, self.AF_lastname, locatorType="xpath")
            self.select_correct_entry()
        else:
            pass

    def click_af_dob(self, af_dob):
        if af_dob is not False:
            self.waitForElement(self.dob_af)
            self.webScroll(self.scroll_view_element(self.dob_af, locatorType="xpath"))
            self.waitForElement(self.dob_af)
            self.select_date_from_calender(af_dob, self.dob_af, locatorType="xpath")
            # self.select_correct_entry()
        else:
            pass

    def click_af_race(self, inp_race_af):
        if inp_race_af is not False:
            self.waitForElement(self.race_af)
            self.webScroll(self.scroll_view_element(self.race_af, locatorType="xpath"))
            self.waitForElement(self.race_af)
            self.ElementClick(self.race_af)
            self.race_af_sel(inp_race_af)
            self.select_correct_entry()
        else:
            pass

    def race_af_sel(self, inp_race_af):
        if inp_race_af is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.race_af_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_race_af)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def click_af_col_date(self, af_cdt):
        self.waitForElement(self.col_date_af)
        self.webScroll(self.scroll_view_element(self.col_date_af, locatorType="xpath"))
        self.waitForElement(self.col_date_af)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.select_date_from_calender(af_cdt, self.col_date_af, locatorType="xpath")
        self.select_correct_entry()

    def click_validate_audit(self):
        self.waitForElement(self.validate_audit, "id")
        self.ElementClick(self.validate_audit, "id")

    def send_case(self, inp_case_no):
        self.click_reset_button()
        self.send_case_no(inp_case_no)
        self.click_apply_button()
        self.click_audit()

    def getTable_count(self):
        count = self.elementPresenceCheck(ByType="xpath", locator=self.tables_count)
        x = len(count)
        print(len(count))
        return x

    def click_scanBarcodeM(self):
        self.waitForElement(self.scanBarcodeM, "id")
        self.ElementClick(self.scanBarcodeM, "id")

    def verify_audit_requests(self):
        self.waitForElement(self.audit_requests, "id")
        ver_ar = self.isElementTextPresent(self.audit_requests, locatorType="id")
        return ver_ar

    def verifyCaseNotListed(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ver_list = self.isElementPresent(self.not_listed, locatorType="xpath")
        return ver_list

    def verify_testedParty_title(self):
        self.waitForElement(self.Listingtitle, locatorType="xpath")
        actual_title = self.elementPresenceCheck(ByType="xpath", locator=self.Listingtitle)
        texts = []
        for matched_element in actual_title:
            text = matched_element.text
            texts.append(text)
            print(text)
        return texts

    def send_Firstname(self, count, inp_fname):
        firstname = f"//div[@class='right-table']//table[{str(count + 1)}]//tbody//tr[5]//td//input"
        if inp_fname is not None:
            self.waitForElement(firstname)
            self.webScroll(self.scroll_view_element(firstname, locatorType="xpath"))
            self.waitForElement(firstname)
            self.sendKeys(inp_fname, firstname)
            self.select_correct_entry()
        else:
            print("Fist name is None")

    def send_Lastname(self, count, inp_lname):
        lastname = f"//div[@class='right-table']//table[{str(count + 1)}]//tbody//tr[7]//td//input"
        if inp_lname is not None:
            self.waitForElement(lastname)
            self.webScroll(self.scroll_view_element(lastname, locatorType="xpath"))
            self.waitForElement(lastname)
            self.sendKeys(inp_lname, lastname)
            self.select_correct_entry()
        else:
            print("Fist name is None")

    def click_dob(self, count, dob):
        commonDOB = f"//div[@class='right-table']//table[{str(count + 1)}]//tbody//tr[11]//td//button"
        print(dob)
        if dob is not False:
            self.waitForElement(commonDOB)
            self.webScroll(self.scroll_view_element(commonDOB, locatorType="xpath"))
            self.waitForElement(commonDOB)
            self.select_date_from_calender(dob, commonDOB, locatorType="xpath")
            self.select_correct_entry()
        else:
            pass

    def click_race(self, count, inp_race):
        race = f"//div[@class='right-table']//table[{str(count + 1)}]//tbody//tr[13]//td//button"
        if inp_race is not None:
            self.waitForElement(race)
            self.webScroll(self.scroll_view_element(race, locatorType="xpath"))
            self.waitForElement(race)
            self.ElementClick(race)
            self.race_m_sel(count, inp_race)
            # self.select_correct_entry()
        else:
            pass

    def click_col_date(self, count, c_dt):
        col_date = f"//div[@class='right-table']//table[{str(count + 1)}]//tbody//tr[14]//td//button"
        if c_dt is not False:
            self.waitForElement(col_date)
            self.webScroll(self.scroll_view_element(col_date, locatorType="xpath"))
            self.waitForElement(col_date)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(c_dt, col_date, locatorType="xpath")
            self.select_correct_entry()
        else:
            pass

    def AuditsampleIds(self, count, inp_s_id):
        sampleID = f"//div[@class='row verify-form-wrapper']//div[{str(count + 1)}]//input"
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(sampleID, locatorType="xpath")
        self.sendKeys(inp_s_id[count], sampleID, locatorType="xpath")
        self.driver.find_element(By.XPATH, sampleID).send_keys(Keys.ENTER)
        time.sleep(1)

    def send_allSampleID(self, inp_s_id):
        for c in range(0, len(inp_s_id)):
            self.AuditsampleIds(c, inp_s_id)

    def send_allSampleIDforAudit(self, inp_auth, inp_agency, inp_s, inp_m_fname, m_lastname, m_dob, m_race, m_cdt,
                                 inp_c_fname, c_lastname, c_dob, c_race, c_cdt, inp_af_fname, af_lastname, af_dob,
                                 af_race, af_cdt):
        self.send_auth_doc(inp_auth)
        self.send_agency_case(inp_agency)
        self.webScroll(self.scroll_view_element(self.scanBarcodeM, locatorType="id"))
        self.click_scanBarcodeM()
        time.sleep(2)
        self.send_allSampleID(inp_s)
        self.click_done()
        time.sleep(2)
        self.send_sampleDetails(inp_m_fname, m_lastname, m_dob, m_race, m_cdt, inp_c_fname, c_lastname, c_dob, c_race,
                                c_cdt, inp_af_fname, af_lastname, af_dob, af_race, af_cdt)

    def send_sampleDetails(self, inp_m_fname, m_lastname, m_dob, m_race, m_cdt, inp_c_fname, c_lastname, c_dob, c_race,
                           c_cdt, inp_af_fname, af_lastname, af_dob, af_race, af_cdt):

        title_list = self.verify_testedParty_title()
        if self.getTable_count() != 0:
            for k in range(0, self.getTable_count()):
                self.func(k, title_list[k], inp_m_fname, m_lastname, m_dob, m_race, m_cdt, inp_c_fname,
                          c_lastname, c_dob, c_race, c_cdt, inp_af_fname, af_lastname, af_dob, af_race, af_cdt)
        else:
            self.log.info("no data available")

    def func(self, count, identifier, inp_m_fname, m_lastname, m_dob, m_race, m_cdt, inp_c_fname, c_lastname,
             c_dob, c_race, c_cdt, inp_af_fname, af_lastname, af_dob, af_race, af_cdt):
        if identifier == "M" or identifier == "AM":
            self.send_M(count, inp_m_fname, m_lastname, m_dob, m_race, m_cdt)
        elif identifier == "C":
            self.send_C(count, inp_c_fname, c_lastname, c_dob, c_race, c_cdt)
        elif identifier == "AF" or identifier == "FE":
            self.send_AF(count, inp_af_fname, af_lastname, af_dob, af_race, af_cdt)

