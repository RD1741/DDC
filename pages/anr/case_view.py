import random
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.anr.plates import Plates
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl


class CaseView(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.pl = Plates(self.driver)

    success_msgg = "//app-toaster//div[@class='alert alert--success ng-star-inserted']"  # //app-toaster//div[2]//h2
    error_msg = "//app-toaster//div[@class='alert alert--error ng-star-inserted']"
    closeMessage = "toastercloseBtn"
    case_view = "navbarcaseView"
    assignedCase = "//ul[@class='ng-trigger ng-trigger-listAnimation']//li"
    loader = "//*[@class='loader']"
    search = "searchID"
    myCase = "mycase-tab"
    allCases = "home-tab"
    expandButton = "//div[@class='tab-arrow']"
    case = "//ul[@class='ng-trigger ng-trigger-listAnimation']//li"
    unAssignbtn = "casedetailsunassigncaseBtn"
    approvebutton = "(//button[contains(text(),'Approve')])[1]"
    exclusions_aprove = "casedetailsapproveBtn"
    interpretation_approve = "casedetailsinterpretationapproveBtn"
    active_loci_aprove = "caselistingapproveBtn"
    report_information_approve = "casereportapproveBtn"
    viewDraftReportbtn = "viewdraftreportBtn"
    SignBtn = "signcasereportBtn"
    draftReportClosebtn = "viewdraftreportcloseBtn"
    draftReportdalay = "//span[@role='View Draft Report']"
    draftReporttitle = "//h5[contains(text(),'Draft Report')]"
    urgentTick = "//input[@id='statusCheckboxClose']"
    SendClosingbtn = "sendtoclosingBtn"
    casestatus = "//div[contains(@class,'status')]"
    sampleNote = "//div[@class='toolTipForNote ng-star-inserted']//parent::a"
    comment = "caseviewcommentIcon"
    addedText = "//div[@class='post']//p"
    addedComment = "//div[@class='post active']//p"
    commentClose = "//button[@aria-label='Close']"
    sampleID = "//p[contains(text(),'Sample')]"
    anr_profile = "//div[@class='user--icon']"
    anr_logout = "//div[@class='user-logout']//ul//li//a"
    acc = "//div[@role='listitem']"
    LOGIN_BUTTON = "//button[normalize-space()='Login']"
    CASE_VIEW_MENU = "//span[normalize-space()='Case View']"
    SCROLL_LOADER = "//*[@class='scroll-loader']"
    NO_DATA_FOUND = "//h6[normalize-space()='No Data Found!']"
    documents = "caseviewdocumentsIcon"
    view_doc = "viewdocumentIcon0"
    view_image = "//table[@class='table notify-table']//tbody//tr[2]//td[6]//ul//li[2]"
    ver_doc = "//div[@class='ng-star-inserted']//h5"
    data_review = "//ul[@id='tabListing']//li[2]//a"
    more_info = "//div[text()='More Info']/span"

    proceedToPHD_bt = "//div[@class='btn-wrap ng-star-inserted']//button[1]//span"
    proceedToPHD_supervisor_bt = "//div[@class='btn-wrap ng-star-inserted']//button[2]//span"
    report_history_icon = "reporthistoryIcon"
    report_history_title = "//div[@class='cdk-drag-handle modal-header']//h5[normalize-space()='REPORT HISTORY']"
    select_report = "//app-select-dropdown[@label='label']//button[@type='button']"
    reportID_list = "//ul[@class='available-items']//li"
    apply_bt = "reporthistoryapplyIcon"
    print_pdf = "//div[@id='toolbarViewerRight']//pdf-print//button[@id='print']"
    close_icon = "reporthistoryBtn"
    warning_close = "confirmboxcloseBtn"
    ver_m_s_id = "//div[@class='case-table caselist-table']//table//tbody//tr[1]//td[1]"
    ver_c_s_id = "//div[@class='case-table caselist-table']//table//tbody//tr[2]//td[1]"
    ver_af_s_id = "//div[@class='case-table caselist-table']//table//tbody//tr[3]//td[1]"
    ver_m_f_name = "//div[@class='case-table caselist-table']//table//tbody//tr[1]//td[2]"
    ver_c_f_name = "//div[@class='case-table caselist-table']//table//tbody//tr[2]//td[2]"
    ver_af_f_name = "//div[@class='case-table caselist-table']//table//tbody//tr[3]//td[2]"
    ver_c_id = "//div[@class='test-id']"
    M_race_title = "//tbody//tr//td[4]"
    AF_race_title = "//tbody//tr[3]//td[4]"
    reportLang = "//button[@id='home-tab']"
    indicator = "//div[@class='table-case col-auto']//ul[2]//li[3]//div"
    NATA_SCC_exists = "(//caption[text()='Data review Listing']//parent::table/tbody/tr)/td[6]"
    indicator_status = "//div[@class='align-items-baseline indicator']"
    req_reviewStatus = "//ul[@class='ng-trigger ng-trigger-listAnimation']//li" \
                       " //div[2][normalize-space()='Requires Review (Supervisor Review)']"
    help_ticket = "navabarhelpTickets"
    help_icon = "//span[@id='helpIcon']//span"
    close_icon_hlp = "createticketcloseIcon"
    add_hlp_closeIcon = "//div[@class='modal-header align-items-center']//div[@aria-label='Close']"
    choose_helpRequest = "//app-select-dropdown[@id='issues']//span[@title='Select'][normalize-space()='Select']"
    choose_helpReq_input = "//div[@class='search-container ng-star-inserted']//input"
    help_req_list = "//ul[@class='available-items']//li"
    samples_require_hlp = "//div[@class='form-check ng-star-inserted']//input"
    help_submit_bt = "createticketsaveBtn"
    help_cancel_bt = "createticketcancelBtn"
    sampleId_M = "//div[@class='with-scorll-table']//div[@class='table-body']//tr[1]//td[1]"
    sampleId_C = "//div[@class='with-scorll-table']//div[@class='table-body']//tr[2]//td[1]"
    sampleId_Af = "//div[@class='with-scorll-table']//div[@class='table-body']//tr[3]//td[1]"
    sampleType_M = "//div[@class='with-scorll-table']//div[@class='table-body']//tr[1]//td[11]"
    sampleType_C = "//div[@class='with-scorll-table']//div[@class='table-body']//tr[2]//td[11]"
    sampleType_Af = "//div[@class='with-scorll-table']//div[@class='table-body']//tr[3]//td[11]"
    ver_m = "//div[@class='case-table caselist-table']//table//tbody//tr[1]//td[3]"
    ver_c = "//div[@class='case-table caselist-table']//table//tbody//tr[2]//td[3]"
    ver_af = "//div[@class='case-table caselist-table']//table//tbody//tr[3]//td[3]"
    ver_acc = "//div[@class='table-case col-auto']//ul[2]//li[2]"
    ver_indicator = "//div[@class='table-case col-auto']//ul[2]//li[3]//div"
    CASE_VIEW_M_Egram = "//tbody/tr[1]/td[7]/ul[1]/li[2]/a"
    CASE_VIEW_C_Egram = "//tbody/tr[2]/td[7]/ul[1]/li[2]/a"
    CASE_VIEW_AF_Egram = "//tbody/tr[3]/td[7]/ul[1]/li[2]/a"
    sample_id_list = "//*[@class='listing-section']/div[2]/div[2]/table/tr/td[1]"
    addType = "//button[@id='commentType']//span[2]"
    addReason = "//button[@id='commentReason']//span[2]"
    note = "//li[contains(text(),'Note')]"
    internal = "//li[contains(text(),'Internal')]"
    textarea = "//textarea[@formcontrolname='comment']"
    commentPost = "//button[normalize-space()='Post']"
    inforedicon = "//div[@class='reprint-popover ng-star-inserted']"
    updatemsgTitle = "//div[@class='tooltip-list-wrap']//h4"
    updatemsgBody = "//div[@class='tooltip-list-wrap']//div//div"
    collectionDate = "//div[@class='case-table']//table//tbody//tr//td[6]"
    proceedToPHDReview = "proceedtophdreviewBtn"
    inclusion = "flexRadioinclusiondefault"
    exclusion = "flexRadio2default"
    inclusionWithMutaion = "flexRadiomutationdefault"
    inconclusive = "flexRadioinconclusivedefault"
    alert_Confirmation_button = "confirmboxokBtn"
    alert_icon = "alertsIcon"
    acknowledgements = "//*[@id='collapseOne']/div/ul/li/div/button"
    alert_close_button = "alertscloseBtn"
    after_acknowledge_element = "//*[@id='collapseOne']/div/ul/li/div/div[2]"
    alert_pop_label = "alertsLabel"
    case_view_case_status = "//div[@id='review']/app-infinite-scroll/ul/li/div[2]/div[2]"
    case_view_alert_count = "//*[@id='alertsIcon']/div"
    reprocess_button_case_view = "casedetailsreprocessBtn"
    caseView_sampleID = "sampleId"
    caseview_plateRunID = "platerunId"
    caserview_reason_reprocess = "reasonforReprocess"
    caseview_battery = "batteryName"
    caseview_submit = "samplereprocesssubmitBtn"
    reprocess_method = "reprocess0"
    caseview_drop_down_list = "//*[@class='available-items']/li"
    sample_status_list_elements = "//*[@class='text-nowrap']"
    continue_bt = "confirmboxokBtn"
    cancel_bt = "confirmboxcancelBtn"
    dangerAlert = "//span//div[@class='badge rounded-pill bg-danger']"
    alertIcon = "alertsIcon"
    alertTable_list = "//div[@id='accordionExample']//div//h2[@id='headingOne']"
    acknowledgeBt = "alertsacknowledgeBtn0"
    # allAcknowledgeBt = "//div[@id='collapseOne']//ul//li//button"
    allAcknowledgeBt = "//div[@data-bs-parent = '#accordionExample' and contains(@class,'show')]" \
                       "//button[contains(@id,'alertsacknowledge')]"
    WarningText = "//div[@id='collapseOne']//div//ul//li//h3"
    alertWarningText = "//div[@id='accordionExample']//div[2]//div[@id='collapseOne']//ul//li//h3"
    cpiValue = "//div[@class='col cpi ng-star-inserted']//ul//li[2]"
    nodataFound = "//h6[normalize-space()='No Data found']"
    QCvalueresult = "//tbody//tr[@class='selected orange red ng-star-inserted']//td[2]//span"
    activelociText = "//h4[normalize-space()='Active Loci']"
    # dueDateView = "//div[@class='case-details']//ul[@class='list custom-list']//li[2]"
    dueDateView = "//ul[@class='ng-trigger ng-trigger-listAnimation']//div[2]//p[2]"
    no_case_selected = "//h2[@class='ng-star-inserted']"
    case_view_title = "//*[@class='main__content']/div[1]/div[1]/h1"
    acknowledge_button_loader = ".btn-loader"
    role1 = "//li//a[@id='trio-tab0']"
    role2 = "//li//a[@id='trio-tab1']"
    calculation_update = "editcalculationupdateBtn"
    PI_editIcon = "pieditIcon"

    def getTexts(self):
        self.waitForElement(self.inforedicon, locatorType="xpath")
        ele = self.getElement(self.inforedicon, locatorType="xpath")
        hover = ActionChains(self.driver).move_to_element(ele)
        hover.perform()
        self.waitForElement(self.updatemsgTitle)
        title = self.isElementTextPresent(self.updatemsgTitle, "xpath")
        self.waitForElement(self.updatemsgBody)
        body = self.isElementTextPresent(self.updatemsgBody, "xpath")
        print("title ", title, " body ", body)
        return title, body

    def clickMyCase(self):
        self.waitForElement(self.myCase, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.myCase, locatorType="id")

    def clickAllCases(self):
        self.waitForElement(self.allCases, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.allCases, locatorType="id")

    def click_case_file(self):
        self.waitForElement(self.case_view, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.case_view, locatorType="id")

    def send_search(self, inp_s):
        self.waitForElement(self.search, locatorType="id")
        self.waitForElementPresent(self.SCROLL_LOADER, locatorType="xpath")
        self.sendKeys(inp_s, self.search, locatorType="id")
        # time.sleep(1)
        self.driver.find_element(By.ID, self.search).send_keys(Keys.ENTER)
        time.sleep(3)
        # self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_expand(self):
        self.waitForElement(self.expandButton)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.expandButton)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def CaseSelect(self, caseid):
        print("Aler3")

        self.click_case_file()
        print("Aler4")

        self.send_search(caseid)
        print("Aler5")

        cv = CaseView(self.driver)
        cv.click_alert_confirmation_popup()
        self.click_expand()
        time.sleep(2)
        self.clickCase()
        time.sleep(2)
        cv.click_alert_confirmation_popup()
        print("Aler6")

        # self.click_expand()
        print("Aler7")

    def UnAssignElementCheck(self):
        self.waitForElement(self.unAssignbtn, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        unassignCase = self.isElementPresent(self.unAssignbtn, "id")
        return unassignCase

    def click_sampleNotes(self):
        self.waitForElement(self.sampleNote)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.sampleNote)

    def open_Comments(self):
        self.waitForElement(self.comment, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.comment, "id")

    def chkSampleID(self):
        self.waitForElement(self.sampleID)
        notesampleId = self.getElement(self.sampleID, "xpath").text
        return notesampleId

    def getText(self):
        self.waitForElement(self.addedText)
        caseStat = self.getElement(self.addedText, "xpath").text
        return caseStat

    def getComment(self):
        self.waitForElement(self.addedComment)
        comment = self.getElement(self.addedComment, "xpath").text
        return comment

    def closeComment(self):
        self.waitForElement(self.commentClose)
        self.ElementClick(self.commentClose)

    def commentChk(self):
        self.click_sampleNotes()
        caseViewSampID = self.chkSampleID()
        txt = self.getText()
        self.closeComment()
        return txt

    def ANCcommentChk(self):
        self.open_Comments()
        # self.scroll_Down()
        self.webScroll(self.scroll_view_element(self.addedComment))
        txt = self.getComment()
        # self.closeComment()
        return txt

    def ANRcommentadd(self, text):
        self.open_Comments()
        self.click_addType()
        self.select_Note()
        self.click_Reason()
        self.select_internal()
        self.addText(text)
        self.post_comm()

    def click_addType(self):
        self.waitForElement(self.addType)
        self.ElementClick(self.addType)

    def select_Note(self):
        self.waitForElement(self.note)
        time.sleep(1)
        self.ElementClick(self.note)
        time.sleep(3)

    def click_Reason(self):
        self.waitForElement(self.addReason)
        self.ElementClick(self.addReason)

    def select_internal(self):
        self.webScroll(self.scroll_view_element(self.internal))
        time.sleep(1)
        self.waitForElement(self.internal)
        time.sleep(1)
        self.ElementClick(self.internal)
        time.sleep(3)

    def addText(self, comment):
        self.waitForElement(self.textarea)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(comment, self.textarea)

    def post_comm(self):
        self.waitForElement(self.commentPost)
        self.ElementClick(self.commentPost)

    def clickApprove(self):
        self.waitForElement(self.approvebutton)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.approvebutton))
        self.ElementClick(self.approvebutton)

    def click_interpretationApprove(self):
        self.waitForElement(self.interpretation_approve, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.interpretation_approve, "id"))
        self.ElementClick(self.interpretation_approve, "id")
        approve_result = self.verifyToaster_success()
        self.utiles.assertionTrue(approve_result, "### Approve Button Click Failed")
        self.closeToasterMsg()

    def click_exclusionsApprove(self):
        self.waitForElement(self.exclusions_aprove, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.exclusions_aprove, "id"))
        self.ElementClick(self.exclusions_aprove, "id")
        approve_result = self.verifyToaster_success()
        self.utiles.assertionTrue(approve_result, "### Approve Button Click Failed")
        self.closeToasterMsg()

    def click_activeLociApprove(self):
        self.waitForElement(self.active_loci_aprove, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.active_loci_aprove, "id"))
        self.ElementClick(self.active_loci_aprove, "id")
        approve_result = self.verifyToaster_success()
        self.utiles.assertionTrue(approve_result, "### Approve Button Click Failed")
        self.closeToasterMsg()

    def click_reportInfoApprove(self):
        self.waitForElement(self.report_information_approve, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.report_information_approve, "id"))
        self.ElementClick(self.report_information_approve, "id")
        approve_result = self.verifyToaster_success()
        self.utiles.assertionTrue(approve_result, "### Approve Button Click Failed")
        self.closeToasterMsg()

    def verifyToaster_success(self):
        self.waitForElement(self.success_msgg, locatorType="xpath")
        success_msg = self.isElementPresent(self.success_msgg, locatorType="xpath")
        if success_msg is not False:
            return success_msg.text
        else:
            return False

    def closeToasterMsg(self):
        # self.waitForElementPresent(self.loader, "xpath")
        self.waitForElement(self.closeMessage, "id")
        self.ElementClick(self.closeMessage, "id")

    def closeErrMsg(self):
        ele = self.isElementPresent(self.closeMessage, "id")
        if ele is not False:
            self.ElementClick(self.closeMessage, "id")

    def CheckAllApprovals(self):
        # for x in range(1, 5):
        #     self.webScroll(self.scroll_view_element(self.approvebutton))
        #     self.clickApprove()
        #     approve_result = self.verifyToaster_success()
        #     self.utiles.assertionTrue(approve_result, "### Approve Button Click Failed")
        #     self.closeToasterMsg()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        time.sleep(5)
        self.click_exclusionsApprove()
        self.click_interpretationApprove()
        self.click_activeLociApprove()
        self.click_reportInfoApprove()

    def clickCase(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.case, "xpath")
        self.ElementClick(self.case)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def clickSign(self):
        self.waitForElement(self.SignBtn, "id")
        self.webScroll(self.scroll_view_element(self.SignBtn, "id"))
        self.ElementClick(self.SignBtn, "id")

    def report_lang_sel(self, inp_lang):
        rep_lang_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.reportLang)
        if inp_lang is not None:
            for lang_ele in rep_lang_list:
                if lang_ele.text == inp_lang:
                    lang_ele.click()
        else:
            self.log.info("Input is None")

    def ViewDraftReport(self):
        self.waitForElement(self.viewDraftReportbtn, "id")
        self.ElementClick(self.viewDraftReportbtn, "id")
        self.waitForElementPresent(self.draftReportdalay)
        self.waitForElement(self.draftReporttitle)
        draft_rep = self.isElementPresent(self.draftReporttitle, locatorType="xpath")
        self.log.info("Draft Report is Present")
        return draft_rep

    def closeDraftReport(self):
        self.waitForElement(self.draftReportClosebtn, "id")
        self.ElementClick(self.draftReportClosebtn, "id")

    def verifyDraftReport(self):
        self.waitForElement(self.draftReporttitle)
        draft_rep = self.isElementPresent(self.draftReporttitle, locatorType="xpath")
        self.log.info("Draft Report is Prsesnt")
        return draft_rep

    def markUrgent(self):
        self.waitForElement(self.urgentTick)
        self.webScroll(self.scroll_view_element(self.urgentTick))
        self.ElementClick(self.urgentTick)

    def SendtoClosing(self):
        self.waitForElement(self.SendClosingbtn, "id")
        self.ElementClick(self.SendClosingbtn, "id")

    # def clickAllCases(self):
    #     self.waitForElement(self.allCases)
    #     self.ElementClick(self.allCases)

    def getStatus(self):
        self.waitForElement(self.casestatus)
        caseStat = self.getElement(self.casestatus, "xpath").text
        return caseStat

    def caseStatuschk(self):
        self.click_expand()
        self.clickAllCases()
        Status = self.getStatus()
        return Status.strip()

    def verify_case_status_from_case_view(self):
        Status = self.getStatus()
        return Status.strip()

    def click_profile(self):
        self.waitForElement(self.anr_profile, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.anr_profile, locatorType="xpath")

    def click_logout(self):
        self.waitForElement(self.anr_logout, locatorType="xpath")
        self.ElementClick(self.anr_logout, locatorType="xpath")

    def click_logout_acc(self):
        element = self.waitForElement(self.acc, locatorType="xpath")
        if element is not None:
            self.click_the_element(element)
        else:
            print("Element is None")
        self.driver.delete_all_cookies()
        time.sleep(4)

        # self.waitForElement(self.acc, locatorType="xpath")
        # self.ElementClick(self.acc, locatorType="xpath")
        # self.driver.delete_all_cookies()
        # time.sleep(4)

    def AnrLogout(self):
        self.click_profile()
        self.click_logout()
        self.click_logout_acc()
        self.driver.delete_all_cookies()
        time.sleep(2)

    def verifyAnrLogoutTest(self):
        self.waitForElement(self.LOGIN_BUTTON, locatorType="xpath")
        logout_result = self.isElementPresent(self.LOGIN_BUTTON, locatorType="xpath")
        self.log.info("Logout Successfully")
        self.driver.delete_all_cookies()
        time.sleep(1)
        return logout_result

    def verify_case_view_page(self):
        self.waitForElement(self.case_view_title, "xpath")
        self.waitForElementPresent(self.SCROLL_LOADER, "xpath")
        result = self.getElement(self.case_view_title, "xpath").text.strip()
        return result

    def verify_caseView_search_result(self):
        # self.waitForElement(self.NO_DATA_FOUND, "xpath")
        self.waitForElementPresent(self.SCROLL_LOADER, "xpath")
        result = self.isElementPresent(self.NO_DATA_FOUND, "xpath")
        if result is False:
            return True
        else:
            return False

    def click_documents(self):
        self.waitForElement(self.documents, "id")
        self.ElementClick(self.documents, "id")

    def click_view_document(self):
        self.click_documents()
        self.waitForElement(self.view_doc, "id")
        self.ElementClick(self.view_doc, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_view_image(self):
        self.click_documents()
        self.waitForElement(self.view_image)
        self.ElementClick(self.view_image)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def verify_document(self):
        self.click_view_document()
        ver_document = self.isElementTextPresent(self.ver_doc, locatorType="xpath")
        return ver_document

    def verify_image(self):
        self.click_view_image()
        ver_document = self.isElementTextPresent(self.ver_doc, locatorType="xpath")
        return ver_document

    def closeifAlert(self):
        self.alertChk()

    def click_PHDreview_bt(self):
        self.waitForElement(self.proceedToPHD_bt)
        self.ElementClick(self.proceedToPHD_bt)

    def click_PHD_SupervisiorBt(self):
        self.waitForElement(self.proceedToPHD_supervisor_bt)
        self.ElementClick(self.proceedToPHD_supervisor_bt)

    def assignCase(self):
        self.webScroll(self.scroll_view_element(self.proceedToPHD_bt, locatorType="xpath"))
        self.click_PHDreview_bt()
        time.sleep(2)

    def click_reportHistory(self):
        self.waitForElement(self.report_history_icon, "id")
        self.ElementClick(self.report_history_icon, "id")

    # def click_selectReport(self):
    #     self.waitForElement(self.select_report)
    #     self.ElementClick(self.select_report)

    def choose_selectReportID(self):
        self.waitForElement(self.select_report)
        self.ElementClick(self.select_report)
        self.waitForElement(self.reportID_list)
        t_party_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.reportID_list)
        if t_party_list is not False:
            t_party_list[0].click()

    def click_applyBt(self):
        self.waitForElement(self.apply_bt, "id")
        self.ElementClick(self.apply_bt, "id")

    def click_closeIcon(self):
        self.waitForElement(self.close_icon, "id")
        self.ElementClick(self.close_icon, "id")

    def click_warningCloseIcon(self):
        self.waitForElement(self.warning_close, "id")
        self.ElementClick(self.warning_close, "id")

    def check_reportHistory_title(self):
        self.waitForElement(self.report_history_title, locatorType="xpath")
        preview = self.isElementTextPresent(self.report_history_title, locatorType="xpath")
        return preview

    def check_pdfPrint_option(self):
        self.waitForElement(self.print_pdf, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        preview = self.isElementPresent(self.print_pdf, locatorType="xpath")
        return preview

    def get_M_S_ID(self):
        self.waitForElement(self.ver_m_s_id)
        self.webScroll(self.scroll_view_element(self.ver_m_s_id, locatorType="xpath"))
        ver_s = self.isElementTextPresent(self.ver_m_s_id, locatorType="xpath")
        return ver_s

    def get_C_S_ID(self):
        self.waitForElement(self.ver_c_s_id)
        self.webScroll(self.scroll_view_element(self.ver_c_s_id, locatorType="xpath"))
        ver_s = self.isElementTextPresent(self.ver_c_s_id, locatorType="xpath")
        return ver_s

    def get_AF_S_ID(self):
        self.waitForElement(self.ver_af_s_id)
        self.webScroll(self.scroll_view_element(self.ver_af_s_id, locatorType="xpath"))
        ver_s = self.isElementTextPresent(self.ver_af_s_id, locatorType="xpath")
        return ver_s

    def get_M_Name(self):
        self.waitForElement(self.ver_m_f_name)
        self.webScroll(self.scroll_view_element(self.ver_m_f_name, locatorType="xpath"))
        ver_m = self.isElementTextPresent(self.ver_m_f_name, locatorType="xpath")
        return ver_m

    def get_C_Name(self):
        self.waitForElement(self.ver_c_f_name)
        self.webScroll(self.scroll_view_element(self.ver_c_f_name, locatorType="xpath"))
        ver_c = self.isElementTextPresent(self.ver_c_f_name, locatorType="xpath")
        return ver_c

    def get_AF_Name(self):
        self.waitForElement(self.ver_af_f_name)
        self.webScroll(self.scroll_view_element(self.ver_af_f_name, locatorType="xpath"))
        ver_af = self.isElementTextPresent(self.ver_af_f_name, locatorType="xpath")
        return ver_af

    def verify_case_id(self):
        c_id = self.isElementTextPresent(self.ver_c_id, locatorType="xpath")
        ver_c_id = self.utiles.SplitTestId(c_id)
        return ver_c_id

    def verify_MRace_title(self):
        self.waitForElement(self.M_race_title)
        ver_MTitle = self.isElementTextPresent(self.M_race_title, locatorType="xpath")
        return ver_MTitle

    def verify_AFRace_title(self):
        self.waitForElement(self.AF_race_title)
        ver_AfTitle = self.isElementTextPresent(self.AF_race_title, locatorType="xpath")
        return ver_AfTitle

    def click_dataReview(self):
        self.waitForElement(self.data_review, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.data_review, locatorType="xpath")

    def click_moreInfo(self):
        self.waitForElement(self.more_info, locatorType="xpath")
        self.ElementClick(self.more_info, locatorType="xpath")

    def NATA_SCC_presenceCheck(self):
        self.waitForElement(self.NATA_SCC_exists)
        ver_NATA = self.isElementTextPresent(self.NATA_SCC_exists, locatorType="xpath")
        return ver_NATA

    def check_NATA_SCC(self):
        self.click_dataReview()
        time.sleep(2)
        self.click_moreInfo()

    def verify_indicatorStatus(self):
        self.waitForElement(self.indicator_status)
        ver_status = self.isElementTextPresent(self.indicator_status, locatorType="xpath")
        return ver_status

    def verify_ReqReview_Status(self):
        self.waitForElement(self.req_reviewStatus)
        ver_status1 = self.isElementTextPresent(self.req_reviewStatus, locatorType="xpath")
        return ver_status1

    def click_help_icon(self):
        self.waitForElement(self.help_icon, "xpath")
        self.ElementClick(self.help_icon, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_helpRequest_role(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.choose_helpRequest, locatorType="xpath")
        self.ElementClick(self.choose_helpRequest, locatorType="xpath")

    def send_role_search(self, inp_r):
        self.waitForElement(self.choose_helpReq_input)
        self.sendKeys(inp_r, self.choose_helpReq_input)
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
        self.waitForElement(self.help_submit_bt, "id")
        self.ElementClick(self.help_submit_bt, "id")

    def click_help_cancel(self):
        self.waitForElement(self.help_cancel_bt, "id")
        self.ElementClick(self.help_cancel_bt, "id")

    def click_help_closeIcon(self):
        ele_pre = self.isElementPresent(self.add_hlp_closeIcon, locatorType="xpath")
        if ele_pre is not False:
            self.ElementClick(self.add_hlp_closeIcon)
        else:
            pass

    def click_help_ticket(self):
        self.waitForElement(self.help_ticket, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.help_ticket, locatorType="id")

    def help_close_icon(self):
        self.waitForElement(self.add_hlp_closeIcon, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.add_hlp_closeIcon, locatorType="xpath")

    def help_ticket_creation(self, inp_r, role):
        self.webScroll(self.scroll_view_element(self.help_icon, locatorType="id"))
        self.click_help_icon()
        self.click_helpRequest_role()
        self.send_role_search(inp_r)
        self.choose_helpRequest_role(role)
        self.choose_sampleRequiring_help()
        self.click_help_submit()
        self.closeErrMsg()
        self.help_close_icon()
        time.sleep(2)

    def verify_sampleId_M(self):
        self.waitForElement(self.sampleId_M)
        ver_sampleId1 = self.isElementTextPresent(self.sampleId_M, locatorType="xpath")
        return ver_sampleId1

    def verify_sampleId_C(self):
        self.waitForElement(self.sampleId_C)
        ver_sampleId2 = self.isElementTextPresent(self.sampleId_C, locatorType="xpath")
        return ver_sampleId2

    def verify_sampleId_Af(self):
        self.waitForElement(self.sampleId_Af)
        ver_sampleId3 = self.isElementTextPresent(self.sampleId_Af, locatorType="xpath")
        return ver_sampleId3

    def verify_sampleType_M(self):
        self.waitForElement(self.sampleType_M)
        ver_sampleTypeM = self.isElementTextPresent(self.sampleType_M, locatorType="xpath")
        return ver_sampleTypeM

    def verify_sampleType_C(self):
        self.waitForElement(self.sampleType_C)
        ver_sampleTypeC = self.isElementTextPresent(self.sampleType_C, locatorType="xpath")
        return ver_sampleTypeC

    def verify_sampleType_Af(self):
        self.waitForElement(self.sampleType_Af)
        ver_sampleTypeAf = self.isElementTextPresent(self.sampleType_Af, locatorType="xpath")
        return ver_sampleTypeAf

    def verify_case_role_m(self):
        cr_m = self.isElementTextPresent(self.ver_m, locatorType="xpath")
        return cr_m

    def verify_case_role_c(self):
        cr_c = self.isElementTextPresent(self.ver_c, locatorType="xpath")
        return cr_c

    def verify_case_role_af(self):
        cr_af = self.isElementTextPresent(self.ver_af, locatorType="xpath")
        return cr_af

    def verify_account(self):
        ac = self.isElementTextPresent(self.ver_acc, locatorType="xpath")
        a = self.utiles.splitAccount(ac)
        return a

    def verify_related_f_m_indicator(self):
        ind = self.isElementTextPresent(self.ver_indicator, locatorType="xpath")
        return ind

    def caseView_M_Egram(self):
        # time.sleep(2)
        self.waitForElement(self.CASE_VIEW_M_Egram, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.CASE_VIEW_M_Egram, "xpath")
        time.sleep(2)

    def caseView_C_Egram(self):
        # time.sleep(2)
        self.waitForElement(self.CASE_VIEW_C_Egram, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.CASE_VIEW_C_Egram, "xpath")
        # time.sleep(2)

    def caseView_AF_Egram(self):
        # time.sleep(2)
        self.waitForElement(self.CASE_VIEW_AF_Egram, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.CASE_VIEW_AF_Egram, "xpath")
        # time.sleep(2)

    def caseView_M_EgramVerification(self):
        self.caseView_M_Egram()
        sample_id = self.pl.GetEgramSampleID()
        return sample_id

    def caseView_C_EgramVerification(self):
        self.caseView_C_Egram()
        sample_id = self.pl.GetEgramSampleID()
        return sample_id

    def caseView_AF_EgramVerification(self):
        self.caseView_AF_Egram()
        sample_id = self.pl.GetEgramSampleID()
        return sample_id

    def getSample(self):
        Elements = self.driver.find_elements(By.XPATH, self.sample_id_list)
        samplelist = []
        for value in Elements:
            sample = value.text
            samplelist.append(sample)
        return samplelist

    def samples(self):
        # Elements = self.driver.find_elements(By.XPATH, self.sample_id_list)
        SampleIdList = self.getSample()
        TrioSampleList = []
        for x in SampleIdList:
            if "M-" in x:
                TrioSampleList.append(x)
            elif "C-" in x:
                TrioSampleList.append(x)
            elif "AF-" in x:
                TrioSampleList.append(x)
            else:
                print("Not matched")

        return TrioSampleList

    def getIndicator(self):
        self.waitForElement(self.indicator)
        indicatortxt = self.isElementTextPresent(self.indicator, locatorType="xpath")
        return indicatortxt

    def verify_info_red_icon(self):
        self.waitForElement(self.inforedicon, "xpath")
        self.waitForElementPresent(self.SCROLL_LOADER, "xpath")
        result = self.getElement(self.inforedicon, "xpath").text
        return result

    def getCollectionDate(self):
        colDate = self.elementPresenceCheck(ByType=By.XPATH, locator=self.collectionDate)
        Dates = []
        for date in colDate:
            addDate = self.utiles.deleteLeadingZeros(date.text)
            Dates.append(addDate)
        print(Dates)
        return Dates

    def proceedToPhdReview(self):
        self.waitForElementPresent(self.loader, "xpath")
        self.waitForElement(self.proceedToPHDReview, "id")
        # self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.proceedToPHDReview, "id")
        self.waitForElementPresent(self.acknowledge_button_loader, locatorType="css_selector", timeout=100)

    def isInclusion(self):
        self.waitForElement(self.inclusion, "id")
        self.waitForElementPresent(self.loader, "xpath")
        element = self.getElement(self.inclusion, "id")
        # if element is not None:
        if element.is_selected():
            status = True
        else:
            status = False
        print(status)
        return status
        # else:
        #     print("Element is not found")

    def isExclusion(self):
        self.waitForElement(self.exclusion, "id")
        self.waitForElementPresent(self.loader, "xpath")
        element = self.getElement(self.exclusion, "id")
        print("Exclusion", element.is_selected())
        # if element is not None:
        if element.is_selected():
            status = True
        else:
            status = False
        print("status is ", status)
        return status
        # else:
        #     print("Element is not found")

    def isInclusion_with_mutation(self):
        self.waitForElement(self.inclusionWithMutaion, "id")
        self.waitForElementPresent(self.loader, "xpath")
        element = self.getElement(self.inclusionWithMutaion, "id")
        # if element is not None:
        print("isInclusion_with_mutation", element.is_selected())
        if element.is_selected():
            status = True
        else:
            status = False
        print(status)
        return status
        # else:
        #     print("Element is not found")

    def isInconclusive(self):
        self.waitForElement(self.inconclusive, "id")
        self.waitForElementPresent(self.loader, "xpath")
        element = self.getElement(self.inconclusive, "id")
        # if element is not None:
        if element.is_selected():
            status = True
        else:
            status = False
        print(status)
        return status
        # else:
        #     print("Element is not found")

    def Interpretation(self, result):
        status = None
        print(result)
        if result == "Inclusion With Mutation":
            status = self.isInclusion_with_mutation()
        elif result == "Exclusion":
            status = self.isExclusion()
            print(status)
        elif result == "Inclusion":
            status = self.isInclusion()
            print(status)
        elif result == "Inconclusive":
            status = self.isInconclusive()
            print(status)
        else:
            print("No such interpretation")
        return status

    def click_alert_confirmation_popup(self):
        element = self.waitForElement(self.alert_Confirmation_button, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if element is not None:
            element.click()
        else:
            print("Element is none")
        # self.ElementClick(self.alert_Confirmation_button, locatorType="id")

    def presence_of_alert_confirmation_popup(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.alert_Confirmation_button, locatorType="id")
        element = self.getElement(self.alert_Confirmation_button, locatorType="id")
        if element != None:
            status = True
        else:
            status = False
        return status

    def click_case_view_alert_icon(self):
        element = self.waitForElement(self.alert_icon, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if element is not None:
            element.click()
        else:
            print("Element is None")

    def close_alert_popup(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.alert_close_button, locatorType="id")
        if element is not None:
            element.click()
        else:
            print("Case view alert pop up is not closed")

    def acknowledge_alerts(self):
        elements = self.waitForElements(locator=self.acknowledgements, locatorType="xpath")
        print("Wait for elements", elements)
        # ele = self.elementPresenceCheck(ByType="xpath", locator=self.acknowledgements)
        print("Presence of elements", elements)
        if elements is not None:
            for ackButton in elements:
                ackButton.click()
            after_elements = self.waitForElements(locator=self.after_acknowledge_element, locatorType="xpath")
            status = []
            for after_ack in after_elements:
                if "Acknowledged" == after_ack.text.strip():
                    print("Text is ", after_ack.text.strip())
                    status.append(True)
                else:
                    status.append(False)
            if False not in status:
                result = True
            else:
                result = False
        else:
            print("Element is None")
            result = False
        return result

    def label_of_alert_popup(self):
        result = True
        element = self.waitForElement(self.alert_pop_label, locatorType="id")
        if element is not None:
            print("label is ", element.text.split())
            texts = element.text.split()
            txt_value = None
            for text_vale in texts:
                if "Alerts" == text_vale:
                    txt_value = text_vale
                    break
                else:
                    print("Not matched")
            if "Alerts" == txt_value:
                result = True
            else:
                result = False
        else:
            print("Element is None")
        return result

    def get_case_view_case_status(self, case_status):
        element = self.waitForElement(locator=self.case_view_case_status, locatorType="xpath")
        print(element.text.strip())
        if element.text.strip() == case_status:
            status = True
        else:
            status = False
        return status

    def case_view_alert_number(self):
        element = self.waitForElement(self.case_view_alert_count, locatorType="xpath", timeout=5)
        if element is not None:
            count = int(element.text.strip())

        else:
            print("There is not alert present")
            count = 0
        return count

    def click_on_case_view_re_process_button(self):
        element = self.waitForElement(self.reprocess_button_case_view, locatorType="id")
        self.waitForElementPresent(self.loader, "xpath")
        if element is not None:
            element.click()
        else:
            print("Element is None")

    def select_sample_id_from_case_view(self, sampleID):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.caseView_sampleID, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(1)
            element_list = self.elementPresenceCheck(ByType="xpath", locator=self.caseview_drop_down_list)
            actual_element = self.utiles.get_dropdown_value_from_list(element_list, sampleID)
            if actual_element is not None and actual_element != False:
                actual_element.click()
                time.sleep(2)
            else:
                print("Element is not found from the list")
        else:
            print("Element is " + str(element))

    def select_plate_run_id(self, plateID):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.caseview_plateRunID, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(1)
            element_list = self.elementPresenceCheck(ByType="xpath", locator=self.caseview_drop_down_list)
            actual_element = self.utiles.find_dropdown_select(element_list, plateID)
            if actual_element is not None and actual_element != False:
                actual_element.click()
                time.sleep(2)
            else:
                print("Element is not found from the list")
        else:
            print("Element is " + str(element))

    def select_reason_for_reprocess(self, reason_for_reprocess):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.caserview_reason_reprocess, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(1)
            element_list = self.elementPresenceCheck(ByType="xpath", locator=self.caseview_drop_down_list)
            actual_element = self.utiles.find_dropdown_select(element_list, reason_for_reprocess)
            if actual_element is not None and actual_element != False:
                actual_element.click()
                time.sleep(2)
            else:
                print("Element is not found from the list")
        else:
            print("Element is " + str(element))

    def select_case_view_battery(self, battery):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.caseview_battery, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(1)
            element_list = self.elementPresenceCheck(ByType="xpath", locator=self.caseview_drop_down_list)
            actual_element = self.utiles.find_dropdown_select(element_list, battery)
            if actual_element is not None and actual_element != False:
                actual_element.click()
                time.sleep(2)
            else:
                print("Element is not found from the list")
        else:
            print("Element is " + str(element))

    def case_view_reprocess_method(self):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.reprocess_method, locatorType="id")
        if element is not None:
            element.click()
        else:
            print("Element is None")

    def case_view_submit(self):
        element = self.waitForElement(self.caseview_submit, locatorType="id")
        self.waitForElementPresent(self.loader, "xpath")
        if element is not None:
            element.click()
        else:
            print("Element is None")
        self.waitForElementPresent(self.loader, "xpath")

    def sample_reprocess_from_case_view(self, sampleList, plateID, reprocessReason="Failed Positive",
                                        battery="GlobalFiler"):
        dic = {}
        # time.sleep(2)
        for x in sampleList:
            self.click_on_case_view_re_process_button()
            self.select_sample_id_from_case_view(x)
            self.select_plate_run_id(plateID)
            self.select_reason_for_reprocess(reprocessReason)
            self.select_case_view_battery(battery)
            self.case_view_reprocess_method()
            self.case_view_submit()
            self.closeToasterMsg()
            atrID = self.pl.get_atr_sampleProcessingId()
            dic[x] = atrID
            # time.sleep(5)
        print(dic)
        return dic

    def sample_status_from_case_view(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        elements = self.elementPresenceCheck(ByType="xpath", locator=self.sample_status_list_elements)
        if elements != []:
            element_list = elements
        else:
            print("Element list is empty")
            element_list = False
        return element_list

    def verify_sample_status_from_case_view(self, input_text):
        status_list = []
        status = None
        elements = self.sample_status_from_case_view()
        if elements is not False:
            for x in elements:
                print("input text is ", input_text, "element text is ", x.text)
                if input_text == x.text.strip():
                    status_list.append(True)
                else:
                    status_list.append(False)
            print(status_list)
            for y in status_list:
                if y:
                    status = True
                else:
                    status = False
                    break
        else:
            print("Elements are Empty")
            status = False
        return status

    def click_case_view_warning(self):
        element = self.waitForElement(self.alert_Confirmation_button, locatorType="id", timeout=10)
        if element is not None:
            element.click()
        else:
            print("Element is None")

    search_no_record = "//*[@id='myTabContent']/app-all-case/div/app-infinite-scroll/div/h6"

    def no_record_found_after_search(self):
        element = self.waitForElement(self.search_no_record, locatorType="xpath", timeout=40)
        if element is not None:
            status = False
        else:
            print("Element is None")
            status = True
        return status

    def click_ContinueBt(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_pre = self.isElementPresent(self.continue_bt, locatorType="id")
        if ele_pre is not False:
            ele_pre.click()
            time.sleep(1)
        else:
            pass

    def click_CancelBt(self):
        ele_pre = self.isElementPresent(self.cancel_bt, locatorType="id")
        if ele_pre is not False:
            self.ElementClick(self.cancel_bt, "id")
            time.sleep(2)
        else:
            pass

    def DangeralertBadgePresence(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.dangerAlert)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        badge = self.isElementPresent(self.dangerAlert)
        return badge

    def click_alert_bt(self):
        self.waitForElement(self.alertIcon, "id")
        self.ElementClick(self.alertIcon, "id")

    def dangerAlertCheck(self):
        if self.DangeralertBadgePresence() is not False:
            self.click_alert_bt()
            time.sleep(2)
        else:
            self.log.info("No alert in this case")

    def acknowledgeAllSample(self):
        self.waitForElement(self.alertTable_list, "xpath")
        list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.alertTable_list)
        print(len(list))
        for self.acknowledgeBt in list:
            self.clickAcknowledgeBt()

    def clickAcknowledgeBt(self):
        ele = self.elementPresenceCheck(ByType=By.XPATH, locator=self.allAcknowledgeBt)
        for x in ele:
            self.webScroll(self.scroll_view_element(self.allAcknowledgeBt, locatorType="xpath"))
            x.click()
            self.waitForElementPresent(self.acknowledge_button_loader, locatorType="css_selector", timeout=100)

    def getWarningMessage(self):
        splitWarning = []
        self.waitForElement(self.alertWarningText)
        warning = self.elementPresenceCheck(ByType=By.XPATH, locator=self.alertWarningText)
        for item in warning:
            splitWarning.append(item.text)
        return splitWarning[0]

    def getBothWarningMessage(self):
        splitWarning = []
        self.waitForElement(self.WarningText)
        warning = self.elementPresenceCheck(ByType=By.XPATH, locator=self.WarningText)
        for item in warning:
            splitWarning.append(item.text)
            self.webScroll(self.scroll_view_element(self.WarningText))
        return splitWarning

    def verify_cpiValue(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        cpi = self.isElementTextPresent(self.cpiValue, locatorType="xpath")
        CPI = self.utiles.splitCPIvalue(cpi)
        return CPI

    def click_ok(self):
        self.waitForElement(self.continue_bt, "id")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.continue_bt, "id")

    def listAcknowledgement(self):
        self.waitForElement(self.allAcknowledgeBt, "xpath")
        button = self.elementPresenceCheck(ByType=By.XPATH, locator=self.allAcknowledgeBt)
        for ele in button:
            ele.click()
            self.waitForElementPresent(self.acknowledge_button_loader, locatorType="css_selector", timeout=100)

    def NoAlertCheck(self):
        ele = self.elementPresenceCheck(ByType=By.XPATH, locator=self.dangerAlert)
        if ele is False:
            self.click_alert_bt()
            print("No data Found : No alert present")
        else:
            self.log.info("Alert present")

    def QCvalueVerification(self):
        self.webScroll(self.scroll_view_element(self.activelociText))
        ele = self.elementPresenceCheck(ByType=By.XPATH, locator=self.QCvalueresult)
        # ele = self.isElementTextPresent(self.QCvalueresult, locatorType="xpath")
        eleList = []
        x = "-1.00"
        for x in ele:
            eleList.append(x.text)
        return eleList

    def verify_dueDate(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        date = self.isElementTextPresent(self.dueDateView, locatorType="xpath")
        due = self.utiles.splitdueDate(date)
        return due

    def verify_phd_review(self):
        element = self.waitForElement(self.no_case_selected, locatorType="xpath")
        if element is not None:
            if "No Case Selected" == element.text.strip():
                status = True
            else:
                status = False
        else:
            status = False
        return status

    def getAlertMessage(self):
        splitWarning = []
        self.waitForElement(self.WarningText)
        warning = self.elementPresenceCheck(ByType=By.XPATH, locator=self.WarningText)
        for item in warning:
            splitWarning.append(item.text)
        return splitWarning[0], splitWarning[1]

    def find_case_view_case_status(self):
        element = self.waitForElement(self.casestatus)
        if element is not None:
            status = element.text.strip()
        else:
            status = None
        return status

    def FindRace(self):
        row = "//div[@class='case-table caselist-table']//table//tbody//tr"
        rowList = self.driver.find_elements(By.XPATH, row)
        sampleRace = []
        for x in range(1, len(rowList) + 1):
            x = str(x)
            trs = "[" + x + "]"
            sampleId = self.getElement(row + trs + "/td[1]", "xpath").text
            if "S-" in sampleId:
                race = self.getElement(row + trs + "/td[4]", "xpath").text
                sampleRace.append(race)
        return sampleRace

    def getTextArea(self):
        text_area = "//div[@id='home']//textarea"
        contents = self.getElement(text_area, "xpath").get_attribute("value")
        return contents

    def extractText(self):
        text = "//div[@id='home']//textarea"
        self.webScroll(self.scroll_view_element(text))
        y = self.getElement(text, locatorType="xpath").get_attribute("value")
        print(y)

    def maternityTab_click(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.role1, "xpath")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.role1, "xpath")

    def paternityTab_click(self):
        self.waitForElement(self.role2, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.role2, "xpath")

    def identify_caseTestType(self):
        self.maternityTab_click()
        self.CheckAllApprovals()
        time.sleep(2)
        self.webScroll(self.scroll_view_element(self.role2))
        self.paternityTab_click()
        self.CheckAllApprovals()

    def click_PI_edit_icon(self):
        self.waitForElement(self.PI_editIcon, "id")
        self.ElementClick(self.PI_editIcon, "id")

    def randNum_generation(self):
        tablelist = "//div[@class='modal-body']//table[@class='table']//tr//td[2]//input"
        ChngS = self.elementPresenceCheck(ByType=By.XPATH, locator=tablelist)
        for ele in ChngS:
            self.webScroll(ele)
            # for ele in range(0, len(tablelist)):
            # p = int(random.random() / 100)
            p = float("{0:.2f}".format(random.uniform(1, 10)))
            print(p)
            ele.send_keys(str(p))

    def click_PIcalcUpdate(self):
        self.waitForElement(self.calculation_update, "id")
        self.webScroll(self.scroll_view_element(self.calculation_update, "id"))
        self.ElementClick(self.calculation_update, "id")
        self.waitForElementPresent(self.acknowledge_button_loader, locatorType="css_selector", timeout=100)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def RITableValueEdit(self, caseId):
        export_bt = "casedetailsapproveBtn"
        bt = self.isElementPresent(export_bt, "id")
        icon = self.isElementPresent(self.PI_editIcon, "id")
        if bt is False:
            if icon is not False:
                self.forIconFalseCondition(caseId)
            else:
                self.forTruePhDCondition(caseId)
        else:
            pass

    def forIconFalseCondition(self, caseId):
        self.webScroll(self.scroll_view_element(self.PI_editIcon, "id"))
        self.click_PI_edit_icon()
        self.randNum_generation()
        self.click_PIcalcUpdate()
        self.closeToasterMsg()
        time.sleep(2)
        self.webScroll(self.scroll_view_element(self.proceedToPHDReview, "id"))
        self.proceedToPhdReview()
        self.closeToasterMsg()
        self.send_search(caseId)
        self.click_expand()
        self.clickAllCases()
        self.clickCase()
        # self.closeToasterMsg()
        self.click_expand()
        # self.closeToasterMsg()
        time.sleep(2)

    def forTruePhDCondition(self, caseId):
        self.webScroll(self.scroll_view_element(self.proceedToPHDReview, "id"))
        self.proceedToPhdReview()
        self.send_search(caseId)
        self.click_expand()
        self.clickAllCases()
        self.clickCase()
        # self.closeToasterMsg()
        self.click_expand()

    def Approve_buttons(self):
        self.click_activeLociApprove()
        self.click_reportInfoApprove()

    def fetch_sample(self):
        li = []
        iconList = "//a[@mattooltip='EGRAM']"
        fetchID = "//div[@class='case-table caselist-table']//tbody//tr//td[1]"
        pdfIcon = self.elementPresenceCheck(ByType=By.XPATH, locator=iconList)
        print(len(pdfIcon))
        for row in range(0, len(pdfIcon)):
            ele = self.driver.find_elements(By.XPATH, iconList)[row]
            ele.click()
            time.sleep(2)
            self.pl.EgramVIewCLose()
            sample_id = fetchID
            ele1 = self.driver.find_elements(By.XPATH, sample_id)[row]
            if ele1.text is not None:
                sNo = ele1.text
                print(sNo)
                li.append(sNo)
        return li
