import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumDriver
from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class scheduleRreqVerification(BasePage):
    log = cl.customLogger(logging.DEBUG)
    util = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    noShow_report = "//aside[@class='sidebar']//ul//li[5]//a"
    schedule_request = "//ul[@class='nav flex-column']//li[1]//a//span"
    caseId = "//div//input[@id='value']"
    cal_click = "(//button[@aria-label='Open calendar'])[5]"
    to_schedule_click = "(//span[@class='nsdicon-angle-down'])[6]"
    search_field = "//*[@class='search-wrap ng-star-inserted']/input"
    apply_bt = "//button[@type='button'][normalize-space()='Apply']"
    reset_bt = "//button[@type='button'][normalize-space()='Reset']"
    caseID_ele = "//tbody//tr//td[1]"
    corporate_opt = "//ul[@class='nav nav-tabs']//li[3]"
    loader = "//*[@class='loader']"
    actual_mfname = "(//tr[@class='ng-star-inserted'])[1]//td[1]"
    actual_cfname = "(//tr[@class='ng-star-inserted'])[2]//td[1]"
    case_detail_act_gov = "//tbody/tr[1]//td[9]//ul//li//a"
    case_detail_act_corp = "//tbody/tr[1]//td[7]//ul//li//a"
    testedParty_cb_m = "//tbody/tr[1]//td[1]//div/input"
    testedParty_cb_c = "//tbody/tr[2]//td[1]//div/input"
    testedParty_cb_af = "//tbody/tr[3]//td[1]//div/input"
    schedule_action_m = "//tbody/tr[1]//td[13]//ul//li[1]"
    schedule_action_c = "//tbody/tr[2]//td[13]//ul//li[1]"
    schedule_action_af = "//tbody/tr[3]//td[13]//ul//li[1]"
    schedule_pending_actM = "//tbody/tr[1]//td[13]//ul//li[2]"
    schedule_pending_actC = "//tbody/tr[2]//td[13]//ul//li[2]"
    schedule_pending_actAf = "//tbody/tr[3]//td[13]//ul//li[2]"
    additional_scheduling_m = "//tbody/tr[1]//td[13]//ul//li[3]"
    additional_scheduling_c = "//tbody/tr[2]//td[13]//ul//li[3]"
    additional_scheduling_af = "//tbody/tr[3]//td[13]//ul//li[3]"
    cancel_action_m = "//tbody/tr[1]//td[13]//ul//li[4]"
    cancel_action_c = "//tbody/tr[2]//td[13]//ul//li[4]"
    cancel_action_af = "//tbody/tr[3]//td[13]//ul//li[4]"
    firstCase_cal_bt = "(//button[@aria-label='Open calendar'])[1]"
    secondCase_cal_bt = "(//button[@aria-label='Open calendar'])[2]"
    thirdCase_cal_bt = "(//button[@aria-label='Open calendar'])[3]"
    fourthCase_cal_bt = "(//button[@aria-label='Open calendar'])[4]"
    collection_time1_bt = "(//input[@placeholder='9.30 AM'])[1]"
    collection_time2_bt = "(//input[@placeholder='9.30 AM'])[2]"
    collection_time3_bt = "(//input[@placeholder='9.30 AM'])[3]"
    hour_input1 = "(//input[@placeholder='00'])[1]"
    hour_input2 = "(//input[@placeholder='00'])[2]"
    hour_input3 = "(//input[@placeholder='00'])[3]"
    open_appointment_bt1 = "(//input[@type='checkbox'])[1]"
    open_appointment_bt2 = "(//input[@type='checkbox'])[2]"
    details_bt = "//div[@class='button-section']//a[normalize-space()='Details']"
    confirm_bt = "//div[@class='button-section']//*[normalize-space()='Confirm']"
    schedule_selected_bt = "//button[normalize-space()='Schedule Selected']"
    back_to_schedulingList = "//a[normalize-space()='Back to Scheduling List']"
    sample_details = "//div[@class='tab-section']/ul/li[1]"
    recollect_history = "//div[@class='tab-section']/ul/li[2]"
    schedule_history = "//div[@class='tab-section']/ul/li[3]"
    plusBt_recollect_history = "//h2[@id='m5']//button"
    plusBt_schedule_history = "(//h2[@id='m5'])[1]//button"
    no_show_action_m = "//tbody/tr[1]/td[13]//ul[1]/li[1]//a"
    no_show_action_c = "//tbody/tr[2]/td[13]//ul[1]/li[1]"
    cancel_action_after_sch_m = "//tbody/tr[1]/td[13]//ul[1]/li[2]"
    cancel_action_after_sch_c = "//tbody/tr[2]/td[13]//ul[1]/li[2]"
    recollect_action_m = "//tbody/tr[1]/td[13]//ul[1]/li[3]"
    recollect_action_c = "//tbody/tr[2]/td[13]//ul[1]/li[3]"
    collect_noShow_fee_NO = "//div[2]//input[@id='emboss2'][1]"
    collect_noShow_fee_Yes = "//div[1]//input[@id='emboss1'][1]"
    cancel_bt = "//button[@type='button'][normalize-space()='Cancel']"
    submit_bt = "//button[@type='button'][normalize-space()='Submit']"
    yes_bt = "//div[@class='confirm-buttons']//button[1]"
    no_bt = "//div[@class='confirm-buttons']//button[2]"
    mark_as_complete_m = "//tbody/tr[1]/td[13]//ul[1]/li[1]"
    mark_as_complete_c = "//tbody/tr[2]/td[13]//ul[1]/li[1]"
    regenerate_act_m = "//tbody/tr[1]/td[13]//ul[1]/li[2]"
    regenerate_act_c = "//tbody/tr[2]/td[13]//ul[1]/li[2]"
    success_msgg = "//app-toaster//div[2]//h2"
    error_msgg = "//app-toaster//div[2]//h2"
    title_m = "//div[normalize-space()='M']"
    title_af = "//div[normalize-space()='AF']"
    case_details_id = "//div[@class='case__content--block position-relative page__content']/div[1]//h1//span"
    no_data_available = "//div[@class='no-data__container ng-star-inserted']//p"
    collector_management_bt = "//ul[@class='nav flex-column']//li[2]//a"
    expand_bt = "//div[@class='expand-btn']"
    collector_id = "//input[@id='collectorID']"
    apply_bt_adv = "//div[@class='btn-wrap float-end btn-between-space ng-star-inserted']" \
                   "//button[@class='btn btn-primary'][normalize-space()='Apply']"
    actual_coll_id = "//tr[@class='ng-star-inserted']//td[2]"
    act_caseId = "//div[@class='sub-heading ng-star-inserted']"
    view_action = "//tr//td[6]//ul//li[1]"
    edit_action = "//tr//td[6]//ul//li[2]"
    view_icon_corp = "//tr[1]//td[7]//ul[@class='actions']//li[1]//a"

    help_icon = "//li[@class='mat-tooltip-trigger help']"
    help_active = "//ul[@class='icon-list']//li[@class='mat-tooltip-trigger help active closed']"
    help_icon_active = "//li[@class='mat-tooltip-trigger help active']"
    close_icon_hlp = "//div[@class='modal-header align-items-center']//button[@aria-label='Close']"
    add_hlp_closeIcon = "//div[@class='modal-header align-items-center']//div[@aria-label='Close']"
    choose_help_request = "//button[@class='ngx-dropdown-button']//span"
    choose_hlp_req_input = "//div[@class='search-wrap ng-star-inserted']//input"
    help_req_list = "//ul[@class='available-items']//li"
    samples_require_hlp = "//div[@class='form-check ng-star-inserted']//input"
    help_submit_bt = "//button[normalize-space()='Submit']"
    help_cancel_bt = "//button[normalize-space()='Cancel']"
    help_add_icon = "//div[@class='add-help-icon']"
    gov_tab = "//div[@class='page__listing']//ul[@role='tablist']//li[1]//a[1]"
    DTC_tab = "//div[@class='page__listing']//ul[@role='tablist']//li[2]//a[1]"
    corporate_tab = "//div[@class='page__listing']//ul[@role='tablist']//li[3]//a[1]"
    media_tab = "//div[@class='page__listing']//ul[@role='tablist']//li[4]//a[1]"
    doc_icon = "//ul[@class='icon-list']//li[3]"
    schedule_comment = "//div[normalize-space()='tested']"
    collection_site_bt = "//ul[@class='nav flex-column']//li[3]//a"
    collection_site_id_input = "//div[@id='facility-details']/div[@class='accordion-body']/div[1]//div[3]//input"
    filter_apply_bt = "//button[@class='btn btn-primary btn-small'][normalize-space()='Apply']"
    exp_collection_id = "//div[@id='facility-details']//div[@class='row']//div[5]//p"
    status_change = "(//span[@class='nsdicon-angle-down'])[5]"
    status_change_list = "//ul[@class='available-items']//li"
    help_status_ver = "//div[@class='dropdown']//span"

    doc_close_icon = "documentcloseBtn"

    def input_caseId(self, caseId):
        self.waitForElement(self.caseId)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(caseId, self.caseId)

    def input_date(self, schedule_req_cal):
        self.waitForElement(self.cal_click, locatorType="xpath")
        self.select_date_from_calender(schedule_req_cal, self.cal_click, locatorType="xpath")

    def click_on_applyBt(self):
        self.waitForElement(self.apply_bt)
        self.ElementClick(self.apply_bt)

    def click_on_viewIcon(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.view_icon_corp)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.view_icon_corp)

    def click_on_noShow_report(self):
        self.waitForElement(self.noShow_report)
        self.ElementClick(self.noShow_report)

    def click_on_corporate(self):
        self.waitForElement(self.corporate_opt)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.corporate_opt)

    def click_on_resetBt(self):
        self.waitForElement(self.reset_bt)
        self.ElementClick(self.reset_bt)

    def Actual_CaseId(self):
        actual = self.isElementTextPresent(self.caseID_ele, locatorType="xpath")
        actual_id = self.utiles.strip_string(actual)
        return actual_id

    def noData_available_check(self):
        noData = self.isElementPresent(self.no_data_available, locatorType="xpath")
        return noData

    def verifyCaseID(self, caseid):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_on_corporate()
        self.input_caseId(caseid)
        self.click_on_applyBt()
        if self.noData_available_check() is False:
            return True
        else:
            return False

    def status_change_ToNotschedule(self):
        self.waitForElement(self.status_change)
        self.ElementClick(self.status_change)

    def status_list_select(self, inp_status):
        if inp_status is not None:
            search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.status_change_list)
            status_sel = self.utiles.find_dropdown_select(search_list, inp_status)
            if status_sel is not False:
                status_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def verifyCaseId_gov(self, caseid):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.input_caseId(caseid)
        # self.status_change_ToNotschedule()
        # self.status_list_select(status)
        self.click_on_applyBt()

    def Actual_mFname(self):
        actaul_mF = self.isElementTextPresent(self.actual_mfname, locatorType="xpath")
        actual_mfname = self.utiles.strip_string(actaul_mF)
        return actual_mfname

    def Actual_cFname(self):
        actaul_cF = self.isElementTextPresent(self.actual_cfname, locatorType="xpath")
        actual_cfname = self.utiles.strip_string(actaul_cF)
        return actual_cfname

    def click_on_caseDetails_action(self):
        self.waitForElement(self.case_detail_act_gov)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.case_detail_act_gov)
        # self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_on_checkbox_m(self):
        self.waitForElement(self.testedParty_cb_m)
        self.ElementClick(self.testedParty_cb_m)

    def click_on_checkbox_c(self):
        self.waitForElement(self.testedParty_cb_c)
        self.ElementClick(self.testedParty_cb_c)

    def click_on_checkbox_af(self):
        self.waitForElement(self.testedParty_cb_af)
        self.ElementClick(self.testedParty_cb_af)

    def click_on_schedule_sel_bt(self):
        self.waitForElement(self.schedule_selected_bt)
        self.ElementClick(self.schedule_selected_bt)
        # self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_open_appointment(self):
        self.waitForElement(self.open_appointment_bt1)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.open_appointment_bt1)

    def click_on_details_Bt(self):
        self.waitForElement(self.details_bt)
        self.ElementClick(self.details_bt)

    def click_on_confirm_bt(self):
        self.waitForElement(self.confirm_bt)
        self.ElementClick(self.confirm_bt)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_on_back_to_scheduleList(self):
        self.waitForElement(self.back_to_schedulingList)
        self.ElementClick(self.back_to_schedulingList)

    def click_on_sample_details(self):
        self.waitForElement(self.sample_details)
        self.ElementClick(self.sample_details)

    def click_on_recollect_history(self):
        self.waitForElement(self.recollect_history)
        self.ElementClick(self.recollect_history)

    def click_on_recollect_plusBt(self):
        self.waitForElement(self.plusBt_recollect_history)
        self.ElementClick(self.plusBt_recollect_history)

    def click_on_scheduled_history(self):
        self.waitForElement(self.schedule_history)
        self.ElementClick(self.schedule_history)

    def click_on_scheduled_plusBt(self):
        self.waitForElement(self.plusBt_schedule_history)
        self.ElementClick(self.plusBt_schedule_history)

    def click_on_noShow_m(self):
        self.waitForElement(self.no_show_action_m)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.no_show_action_m)
        self.select_yes()
        self.click_submit()

    def click_on_noShow_c(self):
        self.waitForElement(self.no_show_action_c)
        self.ElementClick(self.no_show_action_c)

    def click_on_cancel_icon_Msch(self):
        self.waitForElement(self.cancel_action_after_sch_m)
        self.ElementClick(self.cancel_action_after_sch_m)

    def click_on_cancel_icon_Csch(self):
        self.waitForElement(self.cancel_action_after_sch_c)
        self.ElementClick(self.cancel_action_after_sch_c)

    def click_recollect_actionM(self):
        self.waitForElement(self.recollect_action_m)
        self.ElementClick(self.recollect_action_m)

    def click_recollect_actionC(self):
        self.waitForElement(self.recollect_action_c)
        self.ElementClick(self.recollect_action_c)

    def select_yes(self):
        self.waitForElement(self.collect_noShow_fee_Yes)
        self.ElementClick(self.collect_noShow_fee_Yes)

    def select_no(self):
        self.waitForElement(self.collect_noShow_fee_NO)
        self.ElementClick(self.collect_noShow_fee_NO)

    def click_cancel(self):
        self.waitForElement(self.cancel_bt)
        self.ElementClick(self.cancel_bt)

    def click_submit(self):
        self.waitForElement(self.submit_bt)
        self.ElementClick(self.submit_bt)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_yes(self):
        self.waitForElement(self.yes_bt)
        self.ElementClick(self.yes_bt)

    def click_no(self):
        self.waitForElement(self.no_bt)
        self.ElementClick(self.no_bt)

    def click_markAsComplete_m(self):
        self.waitForElement(self.mark_as_complete_m)
        self.ElementClick(self.mark_as_complete_m)
        self.select_yes()
        self.click_submit()

    def click_markAsComplete_c(self):
        self.waitForElement(self.mark_as_complete_c)
        self.ElementClick(self.mark_as_complete_c)
        self.select_yes()
        self.click_submit()

    def click_regenerate_m(self):
        self.waitForElement(self.regenerate_act_m)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.regenerate_act_m)
        self.select_yes()
        self.click_submit()

    def schedule_a_case(self, caseid):
        self.verifyCaseID(caseid)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_on_viewIcon()
        self.click_on_checkbox_m()
        self.click_on_checkbox_c()
        self.click_on_schedule_sel_bt()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.details_bt, locatorType="xpath"))
        self.click_open_appointment()
        self.click_on_confirm_bt()

    def schedule_a_case_gov(self, caseid):
        self.verifyCaseId_gov(caseid)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_on_caseDetails_action()
        self.click_on_checkbox_m()
        self.click_on_checkbox_c()
        self.click_on_schedule_sel_bt()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.details_bt, locatorType="xpath"))
        self.click_open_appointment()
        self.click_on_confirm_bt()

    def verifyToaster_success(self):
        success_msg = self.isElementPresent(self.success_msgg, locatorType="xpath").text
        return success_msg

    def verify_NoShow_report(self, caseid):
        self.click_on_noShow_report()
        self.input_caseId(caseid)
        time.sleep(2)
        self.click_on_applyBt()

    def get_case_id(self):
        self.webScroll(self.scroll_view_element(self.case_details_id, locatorType="xpath"))
        time.sleep(2)
        generated = self.isElementTextPresent(self.case_details_id, locatorType="xpath")
        generated_id = self.utiles.strip_string(generated)
        return generated_id

    def sample_rcvd_status_check(self, caseid):
        self.verifyCaseId_gov(caseid)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_on_caseDetails_action()

    def click_coll_management(self):
        self.waitForElement(self.collector_management_bt)
        self.ElementClick(self.collector_management_bt)

    def click_expand_bt(self):
        self.waitForElement(self.expand_bt)
        self.ElementClick(self.expand_bt)

    def inp_collector_id(self, coll_id):
        self.waitForElement(self.collector_id)
        self.sendKeys(coll_id, self.collector_id)

    def click_apply_bt(self):
        self.waitForElement(self.apply_bt_adv)
        self.ElementClick(self.apply_bt_adv)

    def click_view_action(self):
        self.waitForElement(self.view_action)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.view_action)

    def click_editAction(self):
        self.waitForElement(self.edit_action)
        self.ElementClick(self.edit_action)

    def actual_collector_id(self):
        self.waitForElement(self.actual_coll_id, locatorType="xpath")
        act_coll_id = self.isElementPresent(self.actual_coll_id, locatorType="xpath").text
        return act_coll_id

    def search_case_id(self, coll_id):
        self.click_coll_management()
        self.click_expand_bt()
        time.sleep(1)
        self.inp_collector_id(coll_id)
        time.sleep(1)
        self.click_apply_bt()
        if self.noData_available_check() is False:
            return True
        else:
            return False

    def coll_act_caseID(self):
        self.waitForElement(self.act_caseId, locatorType="xpath")
        actual_case_id = self.isElementTextPresent(self.act_caseId, locatorType="xpath")
        # actual_cID = self.utiles.stripText(actaul_case_id)
        return actual_case_id

    def click_on_gov(self):
        self.waitForElement(self.gov_tab)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.gov_tab)

    def click_on_DTC(self):
        self.waitForElement(self.DTC_tab)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.DTC_tab)

    def click_on_corporate_tab(self):
        self.waitForElement(self.corporate_tab)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.corporate_tab)

    def click_on_media(self):
        self.waitForElement(self.media_tab)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.media_tab)

    def click_on_scheduleReq_bt(self):
        self.waitForElement(self.schedule_request)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.schedule_request)

    def click_help_icon(self):
        self.waitForElement(self.help_icon)
        self.ElementClick(self.help_icon)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_help_icon_active(self):
        self.waitForElement(self.help_icon_active)
        self.ElementClick(self.help_icon_active)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_helpRequest_role(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.choose_help_request, locatorType="xpath")
        self.ElementClick(self.choose_help_request, locatorType="xpath")

    def send_role_search(self, inp_r):
        self.waitForElement(self.choose_hlp_req_input)
        self.sendKeys(inp_r, self.choose_hlp_req_input)
        time.sleep(1)

    def choose_helpRequest_role(self, inp_role):
        if inp_role is not None:
            search_role_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.help_req_list)
            role_sel = self.utiles.find_dropdown_select(search_role_list, inp_role)
            if role_sel is not False:
                role_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def choose_sampleRequiring_help(self):
        self.waitForElement(self.samples_require_hlp)
        self.ElementClick(self.samples_require_hlp)

    def click_help_submit(self):
        self.waitForElement(self.help_submit_bt)
        self.ElementClick(self.help_submit_bt)

    def click_help_cancel(self):
        self.waitForElement(self.help_cancel_bt)
        self.ElementClick(self.help_cancel_bt)

    def click_help_addIcon(self):
        self.waitForElement(self.help_add_icon)
        self.ElementClick(self.help_add_icon)

    def click_help_closeIcon(self):
        ele_pre = self.isElementPresent(self.add_hlp_closeIcon, locatorType="xpath")
        if ele_pre is not False:
            self.ElementClick(self.add_hlp_closeIcon)
        else:
            pass

    def additional_ticket(self,  inp_r, role):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        add_req = self.isElementPresent(self.help_add_icon, locatorType="xpath")
        if add_req is not False:
            self.click_help_addIcon()
        else:
            pass
        self.click_helpRequest_role()
        self.send_role_search(inp_r)
        self.choose_helpRequest_role(role)
        self.choose_sampleRequiring_help()
        self.click_help_submit()
        time.sleep(2)

    def channel_input(self, inp_ch):
        if inp_ch == "Government":
            self.click_on_gov()
        elif inp_ch == "DTC":
            self.click_on_DTC()
        elif inp_ch == "Corporate":
            self.click_on_corporate_tab()
        elif inp_ch == "Media":
            self.click_on_media()
        else:
            self.log.info("no tab found")

    def help_request(self, inp_ch, caseid):
        self.click_on_scheduleReq_bt()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.channel_input(inp_ch)
        self.input_caseId(caseid)
        self.click_on_applyBt()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_on_caseDetails_action()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        active_icon = self.isElementPresent(self.help_icon_active, locatorType="xpath")
        if active_icon is not False:
            self.click_help_icon_active()
        else:
            self.click_help_icon()

    def click_doc_icon(self):
        self.waitForElement(self.doc_icon)
        self.ElementClick(self.doc_icon)

    def document_verify(self, inp_ch, caseid):
        self.click_on_scheduleReq_bt()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_on_resetBt()
        self.channel_input(inp_ch)
        self.input_caseId(caseid)
        self.click_on_applyBt()
        self.click_on_caseDetails_action()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_doc_icon()

    def verify_comment(self):
        self.waitForElement(self.schedule_comment, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.schedule_comment, locatorType="xpath"))
        comment = self.isElementPresent(self.schedule_comment, locatorType="xpath").text
        return comment

    def check_comment_againstCase(self, inp_ch, caseid, status):
        self.click_on_scheduleReq_bt()
        self.channel_input(inp_ch)
        self.input_caseId(caseid)
        # self.status_change_ToNotschedule()
        # self.status_list_select(status)
        self.click_on_applyBt()
        self.click_on_caseDetails_action()
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_collection_site(self):
        self.waitForElement(self.collection_site_bt)
        self.ElementClick(self.collection_site_bt)

    def input_collection_id(self, collectionId):
        self.waitForElement(self.collection_site_id_input)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(collectionId, self.collection_site_id_input)

    def click_on_filter_applyBt(self):
        self.waitForElement(self.filter_apply_bt)
        self.ElementClick(self.filter_apply_bt)

    def Actual_CollecionID(self):
        actual_id = self.isElementTextPresent(self.exp_collection_id, locatorType="xpath")
        # actual_id = self.utiles.strip_string(actual)
        return actual_id

    def search_in_collection_site(self, collectionID):
        self.click_collection_site()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_expand_bt()
        self.input_collection_id(collectionID)
        self.click_on_filter_applyBt()
        self.click_view_action()
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def help_active_icon_click(self):
        self.waitForElement(self.help_active)
        self.ElementClick(self.help_active)

    def help_status_verification(self):
        self.waitForElement(self.help_status_ver, locatorType="xpath")
        element = self.isElementPresent(self.help_status_ver)
        element = element.text
        return element

    def help_ticket_status(self, caseid):
        self.click_on_scheduleReq_bt()
        self.input_caseId(caseid)
        self.click_on_applyBt()
        self.click_on_caseDetails_action()
        self.help_active_icon_click()

    def click_docClose_Icon(self):
        self.waitForElement(self.doc_close_icon, "id")
        self.ElementClick(self.doc_close_icon, "id")
