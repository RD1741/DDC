import time
from base.seleniumbase import SeleniumDriver
from pages.Login.login import Login
from utilities.common_function import CommonUtil
from configurations.config_changes import *


class AncLoginPage(Login, SeleniumDriver):
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGIN_BUTTON = "//button[@type='button']"
    MS_USERNAME = "//input[@id='i0116']"
    MS_NEXT1 = "idSIButton9"
    MS_PASSWORD = "//input[@id='i0118']"
    CONTINUE_BUTTON = "idSIButton9"
    invalid_user = "//div[normalize-space()='Please enter an email id']"
    invalid_password = "//div[normalize-space()='Please enter password']"
    caseID = "//*[@class='lable-view']/label//following-sibling::text()"
    case_filebt = "//a[@class='nav-link case']"
    review_reqBT = "//span[normalize-space()='Review Requests']"
    caseID_input = "//input[@id='caseNo']"
    clear_bt = "//button[normalize-space()='Clear']"
    search_bt = "//button[normalize-space()='Search']"
    apply_bt = "//button[normalize-space()='Apply']"
    table_click = "//div[@class='lable-view']"
    profile = "//div[@class='user--name']"
    profile_icon = "//div[@class='user--icon d-none d-xl-block']"
    logout = "//a[normalize-space()='Logout']"
    sch_profile_icon = "//div[@class='user--icon']"
    pick_an_acc = "//div[@class='table-row']"
    sign_in_title = "//div[@id='loginHeader']//div"
    anr_login_spinner = "//*[@class='spinner-loading']"

    STAY_SIGHN_IN_BUTTON = "idSIButton9"

    def click_login_link(self):
        self.waitForElement(self.LOGIN_BUTTON, locatorType="xpath")
        self.ElementClick(self.LOGIN_BUTTON, locatorType="xpath")

    def enter_email(self, email):
        self.waitForElement(self.MS_USERNAME, locatorType="xpath")
        self.sendKeys(email, self.MS_USERNAME, locatorType="xpath")

    def click_next_button(self):
        self.waitForElement(self.MS_NEXT1, locatorType="id")
        self.ElementClick(self.MS_NEXT1, locatorType="id")

    def enter_password(self, password):
        self.waitForElement(self.MS_PASSWORD, locatorType="xpath")
        self.sendKeys(password, self.MS_PASSWORD, locatorType="xpath")

    def click_continue_button(self):
        self.waitForElement(self.CONTINUE_BUTTON, locatorType="id")
        self.ElementClick(self.CONTINUE_BUTTON, locatorType="id")

    def verifyLoginTest(self):
        self.waitForElement(self.profile, locatorType="xpath")
        result = self.isElementPresent(self.profile, locatorType="xpath")
        self.log.info("Logged-in successfully")
        return result

    def verifyLogoutTest(self):
        logout_result = self.isElementPresent(self.LOGIN_BUTTON, locatorType="xpath")
        self.log.info("Logout Successfully")
        return logout_result

    def verify_Invalid_username(self):
        invalid_result = self.isElementPresent(self.invalid_user, locatorType="xpath")
        self.log.info("Please enter an email id ")
        return invalid_result

    def verify_Invalid_password(self):
        invalid_res = self.isElementPresent(self.invalid_password, locatorType="xpath")
        self.log.info("Please enter password")
        return invalid_res

    def actual_caseID(self):
        case_ID = self.getElement(self.caseID, locatorType="xpath")
        return case_ID

    def click_on_case_FileBT(self):
        self.waitForElement(self.case_filebt, locatorType="xpath")
        self.ElementClick(self.case_filebt, locatorType="xpath")

    def input_caseID(self, inp):
        self.waitForElement(self.caseID_input, locatorType="xpath")
        self.sendKeys(inp, self.caseID_input, locatorType="xpath")

    def click_on_SearchBt(self):
        self.waitForElement(self.search_bt, locatorType="xpath")
        self.ElementClick(self.search_bt, locatorType="xpath")

    def click_on_ClearBt(self):
        self.waitForElement(self.clear_bt, locatorType="xpath")
        self.ElementClick(self.clear_bt, locatorType="xpath")

    def click_on_applyBt(self):
        self.waitForElement(self.apply_bt, locatorType="xpath")
        self.ElementClick(self.apply_bt, locatorType="xpath")

    def click_on_table(self):
        self.waitForElement(self.table_click, locatorType="xpath")
        self.ElementClick(self.table_click, locatorType="xpath")

    def click_on_profile(self):
        self.waitForElement(self.profile_icon)
        self.ElementClick(self.profile_icon)

    def click_on_schProfile(self):
        self.waitForElement(self.sch_profile_icon)
        self.ElementClick(self.sch_profile_icon)

    def click_on_pick_account(self):
        self.waitForElement(self.pick_an_acc)
        self.ElementClick(self.pick_an_acc)

    def click_on_logout(self):
        self.waitForElement(self.logout)
        self.ElementClick(self.logout)

    def click_stay_singnIn_button(self):
        self.waitForElement(self.STAY_SIGHN_IN_BUTTON, "id")
        self.ElementClick(self.STAY_SIGHN_IN_BUTTON, "id")

    def login1(self, email, password):
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.waitForElementPresent(self.anr_login_spinner, locatorType="xpath")
        status = self.isElementPresent(self.LOGIN_BUTTON, locatorType="xpath")
        # ano_acc = self.isElementPresent(self.use_another_acc, locatorType="xpath")
        if status is not False:
            self.click_login_link()
            self.pick_account()

        # if ano_acc is not False:
        #     self.another_acc_sel()
        #     time.sleep(1)
        self.enter_email(email)
        self.click_next_button()
        self.enter_password(password)
        self.click_continue_button()
        self.click_stay_singnIn_button()

    pick_one_profile = "//div[@class='table-row']"
    use_another_acc = "//div[@id='otherTileText']"

    def profile_pick(self):
        self.waitForElement(self.pick_one_profile)
        self.ElementClick(self.pick_one_profile)

    def another_acc_sel(self):
        self.waitForElement(self.use_another_acc)
        self.ElementClick(self.use_another_acc)

    def login_schedule(self, new_email, new_password):
        # self.another_acc_sel()
        self.enter_email(new_email)
        self.click_next_button()
        self.enter_password(new_password)
        self.click_continue_button()

    def logout1(self):
        self.click_on_profile()
        self.click_on_logout()
        self.profile_pick()
        # self.driver.delete_all_cookies()
        # time.sleep(3)

    def sch_logout(self):
        self.click_on_schProfile()
        self.click_on_logout()
        # self.driver.delete_all_cookies()
        # time.sleep(3)
        # self.click_on_pick_account()
        # self.driver.delete_all_cookies()

    def verifySchLogout(self):
        logout_result = self.isElementPresent(self.sign_in_title, locatorType="xpath")
        self.log.info("Logout Successfully")
        return logout_result
