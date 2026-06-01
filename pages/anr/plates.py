import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl
from configurations.config_changes import *
from utilities.data_base_connection import MysqlConnection
import re


class Plates(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SCROLL_LOADER = "//*[@class='scroll-loader']"
    message = "//app-toaster//div[2]//h2"
    success_msgg = "//app-toaster//div[@class='alert alert--success ng-star-inserted']"
    error_msg = "//app-toaster//div[@class='alert alert--error ng-star-inserted']"
    closeMessage = "toastercloseBtn"
    search = "searchID"
    dataReviewTab = "data-review-tab"
    plateDetailsTab = "plate-details-tab"
    moreInfobtn = "//div[text()='More Info']/span"
    plate = "(//ul[@class='ng-trigger ng-trigger-listAnimation']//li)[1]"
    assignbutton = "assigntomeBtn"
    unassignbutton = "unassignBtn"
    loader = "//*[@class='loader']"
    importResultbutton = "importBtn"
    expandbutton = "plateviewplatelistviewIcon"
    plateQCPassed = "plateqcpassedBtn"
    GBFLadder = "(//div[@class='form-check'])[1]//input"
    NaOHNegativeControl = "(//div[@class='form-check'])[3]//input"
    PositiveControl = "(//div[@class='form-check'])[2]//input"
    QCPassedSubmit = "plateqcpassedsubmitBtn"
    importResultsbutton = "importBtn"
    datareviewImportResultButton = "datareviewimportresultsBtn"
    importButton = "importresultimportBtn"
    importComment = "//textarea[@placeholder='Leave a comment']"
    chooseFile = "//input[@title='Choose files']"
    browseFile = "(//div[@class='file-upload']//span)[2]"
    browseFilet = "//div[@class='show-file']//div[2]//span"
    browsefile1 = "//div[@class='browes']//span"
    browsFile = "//div[@class='file-upload']//div[2]//span[normalize-space()='Browse File']"
    SuccessMessage = "//h2[normalize-space()='Success']"
    PlateStatusMessage = "//p[normalize-space()='Plate Status Updated Successfully']"
    ImportSuccessMsg = ""
    PICalcproceed = "//button//span[contains(text(),'Proceed to PI Calc')]"
    sampleNotes = "//tbody/tr[1]/td[1]/ul[1]/li[2]/a[1]"
    addedNote = "//div[@class='toolTipForNote ng-star-inserted']//parent::a"
    addNotes = "//span[@class='nsdicon-angle-down']"
    addedText = "//div[@class='post']//p"
    others = "//li[contains(text(),'Others')]"
    textarea = "//textarea[@formcontrolname='leaveComment']"
    commentSubmit = "//span[normalize-space()='Submit']"
    VBReportSubmit = "//span[normalize-space()='Submit']"
    submitLoader = "//span[@class='btn-loader ng-star-inserted']"
    commentClose = "notespopupcloseBtn"
    VBReportClose = "//button[@aria-label='Close']"
    sampleID = "//p[contains(text(),'Sample')]"
    fileUploadPath = "//input[@title='Choose files']"
    # fileUploadPath = "//div[@class='browes']"
    EMPTY_PLATE_LISTING = "//h2[normalize-space()='No Plate Selected']"
    ver_m_s_id = "//div[@class='table-body']//table//tr[1]//td[1]"
    ver_c_s_id = "//div[@class='table-body']//table//tr[2]//td[1]"
    ver_af_s_id = "//div[@class='table-body']//table//tr[3]//td[1]"
    ver_c_id = "casenumber7"
    TestPanel1 = "(//caption[text()='Data review Listing']//parent::table/tbody/tr)[1]/td[7] "
    TestPanel2 = "(//caption[text()='Data review Listing']//parent::table/tbody/tr)[2]/td[7] "
    TestPanel3 = "(//caption[text()='Data review Listing']//parent::table/tbody/tr)[3]/td[7] "
    labNotes = "//div[@class='content']//table//tr[3]//td[2]//span"
    caseType = "//div[@class='table-body']//table//tr[1]//td[3]"
    audit_status = "//div[@class='table-body']//table//tr[1]//td[normalize-space()='YES']"
    caseDef = "//div[@class='table-body']//table//tr[1]//td[10]"
    samp_type_1 = "//div[@class='table-body']//table//tr[1]//td[13]"
    samp_type_2 = "//div[@class='table-body']//table//tr[2]//td[13]"
    samp_type_3 = "//div[@class='table-body']//table//tr[3]//td[13]"
    COPY_FSA_FILES = "//span[@class='mat-mdc-tooltip-trigger copy-fsa']"
    SELECT_EGRAM_TAB = "//*[@id='importtabListing']/li[2]"
    AF_EGRAM_SELECTION = "//tbody/tr[1]/td[1]/ul[1]/li[5]/a[1]"
    C_EGRAM_SELECTION = "//tbody/tr[2]/td[1]/ul[1]/li[5]/a[1]"
    M_EGRAM_SELECTION = "//tbody/tr[3]/td[1]/ul[1]/li[5]/a[1]"
    EGRAM_VIEW_CLOSE = "//button[@aria-label='Close']"
    GET_EGRAM_SAMPLE_ID = "//div[@class='modal-header']/h5"
    GET_COPYING_TEXT = "//span[@data-bs-target='#copyFSA']/span[2]"
    RUN_ID_ELEMENET_BEFORE_CLICK_ON_FSA = "//td[normalize-space()='RUN ID:']"
    run_id = "//*[@id='plate-details']/div[1]/div/table/tr/td[1]/span"
    run_on_date = "//*[@id='plate-details']/div[1]/div/table/tr/td[3]/span"
    folder_path = "//*[@id='plate-details']/div[1]/div/table/tr/td[4]/span"
    INNER_LOADER_FSA_FILE = "//span[@class='inner-loader']"
    sample_id_list = "//*[@class='listing-section']/div[2]/div[2]/table/tr/td[1]"
    SampleId = "(//caption[text()='my-plates table body']//parent::table)/tr[@class='ng-star-inserted']/td[1]"
    # WellNo = "(//caption[text()='my-plates table body']//parent::table)/tr[@class='ng-star-inserted']/td[6]"
    WellNo = "//*[@class='listing-section']//table//tr//td[10]"
    ViabilityChk = "//a[@mattooltip='Viability Check']"
    previewVBReport = "//span[text()=' Preview Viability Report']"
    Helpbtn_datareview = "//tr[1]//li//a[@id='datareviewhelpcaseIcon']"
    Helpbtn_plates = "(//a[@mattooltip='Help'])[7]"
    HelpbtnCV = "//span[@mattooltip='Help']/span"
    SampleReqHelp = "//input[@formcontrolname='testPartyItem']"
    chooseHelpReq = "//*[@id='issues']/div/button"
    helpRequests = "//ul[@class='available-items']/li"
    helpRequestsEle = "//ul[@class='available-items']//li[1]"
    HelpSubmit = "//button[@type='submit']"
    helpClose = "//div[@aria-label='Close']"
    helpCaseNo = "//p[contains(text(),'Case# :')]"
    helpTicketNo = "(//button[contains(text(),'Ticket')])[1]"
    plateTab = "//ul[@class='nav flex-column']//li[1]//a"
    # plateId = "//*[@id='plate-details']/div[2]/div[2]/div[1]/div[2]/table/tr[1]/td[7]"
    plateId = "//*[@class='listing-section']//table//tr//td[8]"
    add_help_tick = "//div[@class='buttons']//div[contains(@class,'add-help-icon')]"
    row = "//*[@class='listing-section']/div[2]/div[1]/div[2]/table/tr"
    groupId = "//td[2][@id='groupNumber0']"
    sampleTable_Actionlist = "(//tbody/tr//td[1]//ul)"
    ticket_status = "//span[@id='dropdownMenuButton1']"
    all_plates = "home-tab"
    plate_qc_failed_button = "plateqcfailedBtn"
    reason_for_reprocess = "//app-select-dropdown[@label='reason']//span[@class='nsdicon-angle-down']"
    drop_down_lists = "//*[@class='available-items']/li"
    battery_element = "//app-select-dropdown[@label='batteryName']//span[@class='nsdicon-angle-down']"
    type_of_reporcess = "//app-select-dropdown[@label='typeName']//span[@class='nsdicon-angle-down']"
    plate_qc_failed_submit = "plateqcfailedsubmitBtn"

    plate_details_help = "//*[@class='action']/li[6]/a"
    help_label = "helpLabel"
    help_close_button = "listticketscloseIcon"
    choose_help = "issues"
    drop_down_options = "search-text"
    drop_down_list = "//*[@class='ngx-dropdown-container']/div/ul[2]/li"
    select_tested_party = "tsParty0"
    help_submit = "createticketsaveBtn"
    help_tickets = "//*[@id='ticket.ticketId']"
    help_icon = "//span[@id='helpIcon']//span"
    import_button_loader = "//*[@role='Import']"
    proceed_to_pi_button_loader = ".btn-loader"
    acknowledge_button_loader = ".btn-loader"

    caseType_list = "//*[@class='listing-section']/div[2]/div[2]/table/tr/td[5]"
    dataReviewEditIcon = "datarevieweditIcon"
    AlertBadge = "//div[@class='badge rounded-pill bg-danger ng-star-inserted']"
    AlertIcon = "//div[@class='btn-wrap']//span[3]//span"
    plusIcon_inAlert = "//h2[@id='headingOne']//button"
    alertWarningText = "//div[@id='collapseOne']//div//ul//li[1]//h3"
    orangeColor = "//table[@id='datareviewmainTable']//tbody//tr[1]//td[2]//span"
    BlueColor = "//table[@id='datareviewmainTable']//tbody//tr[2]//td[4]//span"
    redColor = "//table[@id='datareviewmainTable']//tbody//tr[2]//td[1]//span"
    GreenColor = "//table[@id='datareviewdetailTable']//tbody//tr[2]//td[2]"
    alertClose = "alertscloseBtn"
    acknowledgeBt = "alertsacknowledgeBtn0"
    confirmBt = "confirmboxokBtn"
    alertTable_list = "//div[@id='accordionExample']//div//h2[@id='headingOne']"
    nodataFound = "//h6[normalize-space()='No Data found']"
    allAcknowledgeBt = "//div[@data-bs-parent = '#accordionExample' and contains(@class,'show')]" \
                       "//button[contains(@id,'alertsacknowledge')]"
    dueDateIcon = "//span[@mattooltip='Due Date']"
    testIDbutton = "//button[@id='caseNumber']//span[normalize-space()='Select']"
    testID_select = "//div[@class='ngx-dropdown-container']//ul//li"
    changeDateCalendar = "//div[normalize-space()='Change Due Date']//button"
    delaySubmit = "delayduedatesubmitBtn"
    delayField = "//table[@id='myplatemainTable']//tr//td[7]"
    dueDateCol = "//table[@id='samplelistingTable']//tr//td[7]"

    sample_ids_from_datareview = "//*[@id ='datareviewdetailTable']/tbody/tr/td/div/div"
    plate_details_sample_rows = "//*[@id='myplatemainTable']/tr"
    get_plate_details_samples = "//*[@id='myplatemainTable']/tr/td[1]"
    edit_gene_marker_table_icon = "(//*[@id='datarevieweditIcon'])"
    first_colum_of_first_row = "//*[@id='datareviewmainTable']/tbody/tr[1]/td[1]/input"
    get_first_column_element_text = "//*[@id='datareviewmainTable']/tbody/tr[1]/td[1]/span"
    data_review_save_icon = "datareviewsavecaseIcon"
    sample_reprocess_button = "datareviewreprocesssamplecaseIcon"
    reprocess_method_first_option = "reprocess0"
    reason_for_reproces = "reasonforReprocess"
    batteryName = "batteryName"
    samplereprocesssubmitBtn = "samplereprocesssubmitBtn"
    presence_of_plate_alerts = "//*[@class='alert-loader-wrap']/span/div"
    redraw_sample_icons = "//*[@id='redrawsampleIcon']"
    reason_redraw = "//*[@label='redrawReason']/div/button"
    choose_help_re = "//*[@label='issueTitle']/div/button"
    redraw_submit = "sampleredrawsubmitBtn"
    redraw_iterm_list = "//*[@class='available-items']/li"
    anr_login_spinner = "//*[@class='spinner-loading']"

    searchBar = "//div[@class='search-container ng-star-inserted']//input"


    def getPlateId(self):
        self.waitForElement(self.plateId)
        PlateIDNo = self.isElementTextPresent(self.plateId, "xpath")
        return PlateIDNo

    def gethelpCaseNo(self):
        self.waitForElement(self.helpCaseNo)
        CaseNo = self.isElementTextPresent(self.helpCaseNo, "xpath")
        return CaseNo

    def getTicketNo(self):
        self.waitForElement(self.helpTicketNo)
        Ticket = self.isElementTextPresent(self.helpTicketNo, "xpath")
        TicketNo = self.utiles.SplitTicketNo(Ticket)
        return TicketNo

    def clickHelp_datareview(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.Helpbtn_datareview)
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.Helpbtn_datareview)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def clickHelp_plates(self):
        # self.waitForElement(self.Helpbtn_plates)
        # self.webScroll(self.Helpbtn_plates)
        # self.ElementClick(self.Helpbtn_plates)
        # self.waitForElementPresent(self.loader, locatorType="xpath")

        enableCheck = self.elementPresenceCheck(ByType=By.XPATH, locator=self.sampleTable_Actionlist)
        for row in range(len(enableCheck)):
            ele = self.driver.find_elements(By.XPATH, self.sampleTable_Actionlist + "//li[1]/a")[row]
            self.webScroll(ele)
            note_ele = self.sampleTable_Actionlist + "//li[6]/a"
            hlp = self.isElementPresent(note_ele)
            ele1 = self.driver.find_elements(By.XPATH, note_ele)[row]
            if hlp.is_enabled():
                ele1.click()
                break

    def clickHelpCV(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.HelpbtnCV)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.HelpbtnCV)

    def clickHelpReqSample(self):
        self.waitForElement(self.SampleReqHelp)
        self.ElementClick(self.SampleReqHelp)
        # t_party_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.SampleReqHelp)
        # for ele in t_party_list:
        #     if ele is not False:
        #         ele.click()
        #     else:
        #         self.log.error("party_sel is none")

    def clickHelpSubmit(self):
        self.waitForElement(self.HelpSubmit)
        self.ElementClick(self.HelpSubmit)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def clickHelpReq(self):
        self.waitForElement(self.chooseHelpReq)
        self.ElementClick(self.chooseHelpReq)

    def clickaddHelpReq(self):
        self.waitForElement(self.add_help_tick)
        self.ElementClick(self.add_help_tick)

    def closeHelpRequest(self):
        self.waitForElement(self.helpClose)
        self.ElementClick(self.helpClose)

    def ANRhelp(self, request):
        help_req = self.isElementPresent(self.chooseHelpReq, locatorType="xpath")
        if help_req is False:
            self.clickaddHelpReq()
            self.clickHelpReq()
            self.help_req_sel(request)
            self.clickHelpReqSample()
            self.clickHelpSubmit()
            help_sub = self.verifyToaster_success()
            self.utiles.hard_assertion(help_sub, "Success", "### Submitting Help Request Failed")
            # self.closeToasterMsg()
        else:
            self.clickHelpReq()
            self.help_req_sel(request)
            self.clickHelpReqSample()
            self.clickHelpSubmit()
            help_sub = self.verifyToaster_success()
            self.utiles.hard_assertion(help_sub, "Success", "### Submitting Help Request Failed")
            # self.closeToasterMsg()

    def help_req_sel(self, inp_help_req):
        if inp_help_req is not None:
            self.waitForElement(self.searchBar)
            self.sendKeys(inp_help_req, self.searchBar, "xpath")
            time.sleep(1)
            self.waitForElement(self.helpRequestsEle, "xpath")
            self.ElementClick(self.helpRequestsEle, "xpath")
        else:
            self.log.info("input is none")

    def ViabilityChks(self):
        self.waitForElement(self.ViabilityChk)
        VBchk = self.elementPresenceCheck("xpath", self.ViabilityChk)
        for vbicon in VBchk:
            vbicon.click()
            self.waitForElement(self.VBReportSubmit)
            self.ElementClick(self.VBReportSubmit)
            vbSubmit = self.verifyToaster_success()
            self.utiles.assertionTrue(vbSubmit, "Viability check submit Failed")
            self.closeToasterMsg()

    def verifyToaster_success(self):
        self.waitForElement(self.message)
        element_present = self.isElementPresent(self.message, locatorType="xpath")

        if element_present is not False:
            success_msg = element_present.text
            return success_msg
        else:
            # self.utiles.assertionTrue(element_present, "element not present")
            return element_present

        # self.utiles.assertionTrue(element_present, "element not present")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        # success_msg = self.getElement(self.message, locatorType="xpath").text

    # def closeToasterMsg(self):
    #     self.waitForElement(self.closeMessage, "id")
    #     self.waitForElementPresent(self.loader, locatorType="xpath")
    #     self.ElementClick(self.closeMessage, "id")

    def closeToasterMsg(self):
        self.waitForElement(self.closeMessage, locatorType="id")
        self.ElementClick(self.closeMessage, locatorType="id")

    def send_search(self, inp_s):
        self.waitForElementPresent(self.anr_login_spinner, locatorType="xpath")
        self.waitForElementPresent(self.SCROLL_LOADER, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.search, "id", timeout=100)
        # self.ElementClick(self.search, "id")
        self.sendKeys(inp_s, self.search, "id")
        time.sleep(2)
        # self.sendKeys(Keys.ENTER, self.search, "id")
        self.driver.find_element(By.ID, self.search).send_keys(Keys.ENTER)
        time.sleep(2)

    def click_plate_tab(self):
        self.waitForElement(self.plateTab, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.plateTab, locatorType="xpath")

    def click_plate(self):
        self.waitForElement(self.plate)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.plate)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_dataReview(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.dataReviewTab, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.dataReviewTab, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def clickplateDetails(self):
        self.waitForElement(self.plateDetailsTab, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.plateDetailsTab, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_MoreInfo(self):
        self.waitForElement(self.moreInfobtn)
        self.ElementClick(self.moreInfobtn)

    def moreInfobtnCheck(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.moreInfobtn)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        moreInfo = self.isElementPresent(self.moreInfobtn)
        return moreInfo

    def getTestPaneltxt(self):
        self.waitForElement(self.TestPanel1)
        TP1 = self.getElement(self.TestPanel1, "xpath").text
        self.waitForElement(self.TestPanel2)
        TP2 = self.getElement(self.TestPanel2, "xpath").text
        self.waitForElement(self.TestPanel3)
        TP3 = self.getElement(self.TestPanel3, "xpath").text
        TestPanel = [TP1, TP2, TP3]
        return TestPanel

    def BatteryCheck(self):
        self.click_dataReview()
        self.click_MoreInfo()
        TPtxt = self.getTestPaneltxt()
        return TPtxt

    def click_assign(self):
        self.waitForElement(self.assignbutton, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        # self.waitForElementPresent(self.RUN_ID_ELEMENET_BEFORE_CLICK_ON_FSA, locatorType="xpath")
        self.ElementClick(self.assignbutton, "id")
        # self.waitForElementPresent(self.loader, locatorType="xpath")

    def UnAssignElementCheck(self):
        # self.waitForElement(self.unassignbutton, "id")
        time.sleep(3)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        unassignPlate = self.isElementPresent(self.unassignbutton, "id")
        return unassignPlate

    def PlateQCelementcheck(self):
        self.waitForElement(self.plateQCPassed, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        plateQCPass = self.isElementPresent(self.plateQCPassed, "id")
        return plateQCPass

    def click_expand(self):
        self.waitForElement(self.expandbutton, "id")
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.expandbutton, "id")

    def commentChk(self):
        self.click_sampleNotes()
        # caseViewSampID = self.chkSampleID()
        txt = self.getText()
        self.closeComment()
        return txt

    def getText(self):
        self.waitForElement(self.addedText)
        caseStat = self.getElement(self.addedText, "xpath").text
        return caseStat

    def click_sampleNotes(self):
        enableCheck = self.elementPresenceCheck(ByType=By.XPATH, locator=self.sampleTable_Actionlist)
        for row in range(len(enableCheck)):
            ele = self.driver.find_elements(By.XPATH, self.sampleTable_Actionlist + "//li[1]/a")[row]
            self.webScroll(ele)
            note_ele = self.sampleTable_Actionlist + "//li[2]/a"
            ele1 = self.driver.find_elements(By.XPATH, note_ele)[row]
            if "disabled" not in ele.get_attribute("class"):
                ele1.click()
                break

    def click_addedNotes(self):
        self.waitForElement(self.addedNote)
        self.ElementClick(self.addedNote)

    def click_addNotes(self):
        self.waitForElement(self.addNotes)
        self.ElementClick(self.addNotes)

    def select_Others(self):
        self.scroll_view_element(self.others)
        time.sleep(1)
        self.isElementVisible(self.others)
        time.sleep(1)
        self.waitForElement(self.others)
        time.sleep(1)
        self.ElementClick(self.others)
        time.sleep(3)

    def addText(self, comment):
        self.waitForElement(self.textarea)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(comment, self.textarea)

    def submit_comm(self):
        self.waitForElement(self.commentSubmit)
        self.ElementClick(self.commentSubmit)
        self.waitForElementPresent(self.submitLoader, locatorType="xpath")

    def chkSampleID(self):
        self.waitForElement(self.sampleID)
        notesampleId = self.getElement(self.sampleID, "xpath").text
        return notesampleId

    def closeComment(self):
        self.waitForElement(self.commentClose, locatorType="id")
        self.waitForElementPresent(self.loader)
        self.MoveandClick(self.commentClose, locatorType="id")
        # self.ElementClick(self.commentClose)

    def commentAdd(self, txt):
        self.click_sampleNotes()
        self.click_addNotes()
        self.select_Others()
        self.addText(txt)
        self.submit_comm()
        # plateSampId = self.chkSampleID()
        # self.closeComment()
        # return plateSampId

    def click_plateQCPassed(self):
        self.waitForElement(self.plateQCPassed, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.plateQCPassed, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def selectGBFLadder(self):
        self.waitForElement(self.GBFLadder)
        self.ElementClick(self.GBFLadder)

    def submitQCPassed(self):
        self.waitForElement(self.QCPassedSubmit, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.QCPassedSubmit, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def PlateQCPass(self):
        self.click_plateQCPassed()
        # self.selectGBFLadder()
        self.submitQCPassed()
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def clickImportResults(self):
        self.waitForElement(self.importResultsbutton, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.importResultsbutton, "id")

    def dataReviewclickImportResults(self):
        self.waitForElement(self.datareviewImportResultButton, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.datareviewImportResultButton, "id")

    def clickBrowseFiles(self):
        self.waitForElement(self.browsFile)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.MoveandClick(self.browsFile)
        # self.ElementClick(self.browsFile)
        # self.ElementClickJS(self.browsFile)
        time.sleep(2)
        # element = self.getElement(self.chooseFile, "xpath")
        # element.click()

    def sendComments(self, comment):
        self.waitForElement(self.importComment)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(comment, self.importComment)

    def clickImport(self):
        self.waitForElement(self.importButton, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.importButton, "id")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElementPresent(self.import_button_loader, locatorType="xpath")

    def ImportResults(self, path):
        self.clickImportResults()
        self.clickBrowseFiles()
        self.utiles.fileupload(path)
        self.sendComments("test")
        self.clickImport()

    def ImportResultsnew(self, path):
        self.clickImportResults()
        self.waitFile(path)
        self.sendComments("test")
        self.clickImport()

    def waitFile(self, path):
        # self.waitForElement(self.fileUploadPath)
        time.sleep(4)
        # self.sendKeys("D:\\Projects\\DDC-project\\ddc-regression-main\\test_data\\csv_file\\trio-TS.csv",
        #               self.fileUploadPath)
        self.sendKeysForFileUpload(path, self.fileUploadPath)
        # time.sleep(5)

    def ProceedtoPICalc(self):
        self.waitForElement(self.PICalcproceed, timeout=100)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.PICalcproceed)
        self.waitForElementPresent(self.proceed_to_pi_button_loader, locatorType="css_selector", timeout=100)

    def verify_presence_of_case_id(self):
        self.waitForElementPresent(self.loader, "xpath")
        self.waitForElementPresent(self.SCROLL_LOADER, "xpath")
        status = self.isElementPresent(self.EMPTY_PLATE_LISTING, "xpath")
        if status == False:
            return True
        else:
            return False

    def get_S_ID(self):
        self.waitForElement(self.ver_m_s_id)
        ver_m_s = self.isElementTextPresent(self.ver_m_s_id, locatorType="xpath")
        self.waitForElement(self.ver_c_s_id)
        ver_c_s = self.isElementTextPresent(self.ver_c_s_id, locatorType="xpath")
        self.waitForElement(self.ver_af_s_id)
        ver_af_s = self.isElementTextPresent(self.ver_af_s_id, locatorType="xpath")
        sample_id = [ver_m_s, ver_c_s, ver_af_s]
        return sample_id

    def verify_case_id(self):
        self.webScroll(self.scroll_view_element(self.ver_c_id, locatorType="id"))
        c_id = self.isElementTextPresent(self.ver_c_id, locatorType="id")
        return c_id

    def getSampleId(self):
        self.waitForElement(self.SampleId)
        SampleId = self.elementPresenceCheck("xpath", self.SampleId)
        SampIDList = []
        for items in SampleId:
            self.webScroll(items)
            time.sleep(1)
            SampIDList.append(items.text)
        return SampIDList

    def getWellNo(self):
        self.waitForElement(self.WellNo)
        welNo = self.elementPresenceCheck("xpath", self.WellNo)
        WellNoList = []
        for items in welNo:
            self.webScroll(items)
            time.sleep(1)
            WellNoList.append(items.text)
        return WellNoList

    def getJsonDetails(self, data):
        jsonDetails = {}
        samples = data['racks'][0]['samples']
        sampleLength = len(samples)
        for x in range(sampleLength):
            jsonDetails[data['racks'][0]['samples'][x]['wellNo']] = data['racks'][0]['samples'][x]['sampleId']
        return jsonDetails

    def getPlateControls(self, data):
        PlConList = []
        samples = data['racks'][0]['samples']
        sampleLength = len(samples)
        for x in range(sampleLength):
            PlConList.append(data['racks'][0]['samples'][x]['sampleId'].upper())
        return PlConList

    def getSample(self):
        Elements = self.driver.find_elements(By.XPATH, self.sample_id_list)
        samplelist = []
        for value in Elements:
            sample = value.text
            samplelist.append(sample)
        while ("" in samplelist):
            samplelist.remove("")
        return samplelist

    def samples(self):
        # Elements = self.driver.find_elements(By.XPATH, self.sample_id_list)
        SampleIdList = self.getSample()
        TrioSampleList = []
        TrioPlateControls = []
        SampleList = []
        for x in SampleIdList:
            SampleList.append(x)
            if "S-" in x:
                TrioSampleList.append(x)
            # elif "C-" in x:
            #     TrioSampleList.append(x)
            # elif "AF-" in x:
            #     TrioSampleList.append(x)
            else:
                TrioPlateControls.append(x)
                print("Not matched")
        return TrioSampleList, SampleList

    def verify_lab_notes(self):
        self.waitForElement(self.labNotes)
        ln = self.isElementTextPresent(self.labNotes, locatorType="xpath")
        return ln

    def verify_audit_status(self):
        aud_st = self.isElementTextPresent(self.audit_status, locatorType="xpath")
        return bool(aud_st)

    def verify_case_def(self):
        cd = self.isElementTextPresent(self.caseDef, locatorType="xpath")
        return cd

    def verify_sample_type(self):
        self.waitForElement(self.samp_type_1)
        self.webScroll(self.scroll_view_element(self.samp_type_1, locatorType="xpath"))
        s1 = self.isElementTextPresent(self.samp_type_1, locatorType="xpath")

        self.waitForElement(self.samp_type_2)
        self.webScroll(self.scroll_view_element(self.samp_type_2, locatorType="xpath"))
        s2 = self.isElementTextPresent(self.samp_type_2, locatorType="xpath")

        self.waitForElement(self.samp_type_3)
        self.webScroll(self.scroll_view_element(self.samp_type_3, locatorType="xpath"))
        s3 = self.isElementTextPresent(self.samp_type_3, locatorType="xpath")
        sample = [s1, s2, s3]
        return sample

    def sortedDict(self, myDict):
        myKeys = list(myDict.keys())
        myKeys.sort()
        sorted_dict = {i: myDict[i] for i in myKeys}
        return sorted_dict

    def click_on_copy_fsa_files(self):
        self.waitForElement(self.COPY_FSA_FILES, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        self.waitForElementPresent(self.INNER_LOADER_FSA_FILE, "xpath")
        self.ElementClick(self.COPY_FSA_FILES, "xpath")
        # time.sleep(5)

    def select_Egram_tab(self):
        self.waitForElement(self.SELECT_EGRAM_TAB, "xpath")
        self.ElementClick(self.SELECT_EGRAM_TAB, "xpath")

    def import_Egram_files(self, path):
        self.dataReviewclickImportResults()
        self.select_Egram_tab()
        self.waitFile(path)
        self.clickImport()
        # time.sleep(2)

    def AFEgramSelection(self):
        time.sleep(2)
        self.waitForElement(self.AF_EGRAM_SELECTION, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        time.sleep(2)
        self.ElementClick(self.AF_EGRAM_SELECTION, "xpath")

    def CEgramSelection(self):
        self.waitForElement(self.C_EGRAM_SELECTION, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        time.sleep(2)
        self.ElementClick(self.C_EGRAM_SELECTION, "xpath")

    def MEgramSelection(self):
        self.waitForElement(self.M_EGRAM_SELECTION, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        time.sleep(2)
        self.ElementClick(self.M_EGRAM_SELECTION, "xpath")

    def EgramVIewCLose(self):
        self.waitForElement(self.EGRAM_VIEW_CLOSE, "xpath")
        self.ElementClick(self.EGRAM_VIEW_CLOSE, "xpath")
        # time.sleep(2)

    def GetEgramSampleID(self):
        self.waitForElementPresent(self.loader, "xpath")
        self.waitForElement(self.GET_EGRAM_SAMPLE_ID, 'xpath')
        self.waitForElementPresent(self.loader, "xpath")
        elementText = self.isElementTextPresent(self.GET_EGRAM_SAMPLE_ID, 'xpath')
        if elementText is not False:
            elemetList = elementText.split("-")
            if LOCAL:
                sampleId = elemetList[1] + "-" + elemetList[2]
            else:
                sampleId = elemetList[1] + "-" + elemetList[2] + "-" + elemetList[3]
            sampleId = sampleId.strip()
        else:
            sampleId = False
        return sampleId

    def EgramAFSampleIDVerification(self):
        self.AFEgramSelection()
        time.sleep(2)
        sample_id = self.GetEgramSampleID()
        return sample_id

    def EgramCSampleIDVerification(self):
        self.CEgramSelection()
        sample_id = self.GetEgramSampleID()
        return sample_id

    def EgramMSampleIDVerification(self):
        self.MEgramSelection()
        sample_id = self.GetEgramSampleID()
        return sample_id

    def getRunID(self):
        self.waitForElement(self.run_id, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        runiD = self.isElementTextPresent(self.run_id, "xpath")
        runiD = runiD.split("-")
        return runiD[0].strip()

    def getRunDate(self):
        self.waitForElement(self.run_on_date, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        date = self.isElementTextPresent(self.run_on_date, "xpath")
        date = date.split(" ")
        return date[2].strip()

    def getEgramFolderNameFromPath(self):
        self.waitForElement(self.folder_path, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        folderPath = self.isElementTextPresent(self.folder_path, "xpath")
        if folderPath is not False:
            foldName = folderPath.split("/")
            foldName = foldName[7].strip()
        else:
            foldName = False
        return foldName

    def getFsaFolderNameFromPath(self):
        self.waitForElement(self.folder_path, "xpath")
        self.waitForElementPresent(self.loader, "xpath")
        folderPath = self.isElementTextPresent(self.folder_path, "xpath")
        return folderPath

    def getsamples(self):
        sample_type = self.verify_sample_type()
        print(sample_type)
        sample_id = self.samples()
        print(sample_id)
        samples = {sample_id[0]: sample_type[0], sample_id[1]: sample_type[1], sample_id[2]: sample_type[2]}
        return samples

    def getPlateDetails(self):
        plateDetails = {}
        SmplId = self.getSampleId()
        Wellno = self.getWellNo()
        for x in range(len(Wellno)):
            plateDetails[Wellno[x]] = SmplId[x]
        return plateDetails

    def getJsonWellNo(self, data):
        WellNoList = []
        samples = data['racks'][0]['samples']
        sampleLength = len(samples)
        for x in range(sampleLength):
            WellNoList.append(data['racks'][0]['samples'][x]['wellNo'])
        return WellNoList

    def getAnalysisPlateId(self, data):
        analysisPlateId = data['racks'][0]['analysisPlateId']
        return analysisPlateId

    def tables(self):
        rowList = self.driver.find_elements(By.XPATH, self.row)
        sampleIDs = []
        sampleTypes = []
        CaseType = []
        SampDict = {}
        for x in range(1, len(rowList) + 1):
            x = str(x)
            trs = "[" + x + "]"
            sampleId = self.getElement(self.row + trs + "/td[1]", "xpath").text

            # if "S-" in sampleId or "C-" in sampleId or "AF-" in sampleId:
            if "S-" in sampleId:
                sampleType = self.getElement(self.row + trs + "/td[10]", "xpath").text
                caseType = self.getElement(self.row + trs + "/td[5]", "xpath").text
                sampleIDs.append(sampleId)
                sampleTypes.append(sampleType)
                CaseType.append(caseType)
                SampDict[sampleId] = sampleType
        return SampDict

    def CheckRace(self):
        rowList = self.driver.find_elements(By.XPATH, self.row)
        sampleIDs = []
        sampleTypes = []
        CaseType = []
        SampDict = {}
        for x in range(1, len(rowList) + 1):
            x = str(x)
            trs = "[" + x + "]"
            sampleId = self.getElement(self.row + trs + "/td[1]", "xpath").text

            # if "S-" in sampleId or "C-" in sampleId or "AF-" in sampleId:
            if "S-" in sampleId:
                sampleType = self.getElement(self.row + trs + "/td[10]", "xpath").text
                caseType = self.getElement(self.row + trs + "/td[5]", "xpath").text
                sampleIDs.append(sampleId)
                sampleTypes.append(sampleType)
                CaseType.append(caseType)
                SampDict[sampleId] = sampleType
        return SampDict

    def getSampleIdAndRole(self):
        row = "//div[@class='case-table caselist-table']//table//tbody//tr"
        rowList = self.driver.find_elements(By.XPATH, row)
        sampleIDs = []
        case_roles = []
        SampDict = {}
        for x in range(1, len(rowList) + 1):
            x = str(x)
            trs = "[" + x + "]"
            sampleId = self.getElement(row + trs + "/td[1]", "xpath").text

            if "S-" in sampleId:
                case_role = self.getElement(row + trs + "/td[3]", "xpath").text
                sampleIDs.append(sampleId)
                case_roles.append(case_role)
                SampDict[sampleId] = case_role
        return SampDict
    def verify_groupId(self):
        Id = self.isElementTextPresent(self.groupId, locatorType="xpath")
        return Id

    def egram_fileVerification(self, actualSampleId, sample1=None, sample2=None, sample3=None):
        sampleLists = [sample1, sample2, sample3]
        status = None
        for sample in sampleLists:
            if actualSampleId == sample:
                status = True
                break
            else:
                status = False
        return status

    def gethelpTicketStatus(self):
        self.waitForElement(self.ticket_status, "xpath")
        CaseNo = self.isElementTextPresent(self.ticket_status, "xpath")
        return CaseNo

    def click_help_from_plate_details(self):
        elements = self.waitForElements(self.plate_details_help, locatorType="xpath")
        for help_elements in elements:
            if help_elements.is_enabled():
                help_elements.click()
                break
            else:
                print("Element is not enabled")

    def verify_help_popup(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.help_label, locatorType="id")
        label = element.text
        if "Help" == label:
            status = True
        else:
            status = False
        return status

    def close_help_popup(self):
        element = self.waitForElement(self.help_close_button, locatorType="id")
        element.click()

    def choose_help_reqst(self):
        element = self.waitForElement(self.choose_help, locatorType="id")
        element.click()

    def select_the_help_ticket_option(self, input_text):
        element = self.waitForElement(self.drop_down_options, locatorType="name")
        element.send_keys(input_text)
        time.sleep(1)
        element_list = self.elementPresenceCheck(ByType="xpath", locator=self.drop_down_list)
        actual_element = self.utiles.find_dropdown_select(element_list, input_text)
        if actual_element is not None and actual_element != False:
            actual_element.click()
            time.sleep(2)
        else:
            print("Element is not found from the list")

    def select_tested_party_checkBox(self):
        element = self.waitForElement(self.select_tested_party, locatorType="id")
        element.click()

    def help_req_submit(self):
        element = self.waitForElement(self.help_submit, locatorType="id")
        element.click()

    def select_the_help_request(self):
        self.click_help_from_plate_details()
        status = self.verify_help_popup()
        return status

    def create_help_ticket(self, input_text):
        self.choose_help_reqst()
        self.select_the_help_ticket_option(input_text)
        self.select_tested_party_checkBox()
        self.help_req_submit()

    def verify_help_tickets_at_plates(self):
        elements = self.waitForElements(self.help_tickets, locatorType="xpath")
        tickets = []
        if elements is not None:
            status = True
            for x in elements:
                tickets.append(x.text)
        else:
            status = False
        print(tickets)
        return status, tickets

    def help_ticket_added_or_not(self):
        status, tickets = self.verify_help_tickets_at_plates()
        return status, tickets

    def click_help_icon(self):

        element = self.waitForElement(self.help_icon, locatorType="xpath")
        # if element is not None:
        element.click()
        # else:
        #     print("Element is not found")

    def verify_help_ticket_in_case_view(self):
        time.sleep(2)
        self.click_help_icon()
        time.sleep(2)
        status, tickets = self.verify_help_tickets_at_plates()
        return status, tickets

    def click_on_plate_qc_failed_button(self):
        element = self.waitForElement(self.plate_qc_failed_button, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(2)
        else:
            print("Element is ", element)

    def reason_for_re_process(self, input_text):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.reason_for_reprocess, locatorType="xpath")
        if element is not None:
            element.click()
            # time.sleep(1)
        else:
            print("Element is ", element)
        dropDownList = self.elementPresenceCheck(ByType="xpath", locator=self.drop_down_lists)
        actual_element = self.utiles.find_dropdown_select(dropDownList, input_text)
        if actual_element is not None and actual_element != False:
            actual_element.click()
            # time.sleep(1)
        else:
            print("Element is not found from the list")

    def select_battery(self, input_text):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.battery_element, locatorType="xpath")
        if element is not None:
            element.click()
            # time.sleep(2)
        else:
            print("Element is ", element)
        dropDownList = self.elementPresenceCheck(ByType="xpath", locator=self.drop_down_lists)
        actual_element = self.utiles.find_dropdown_select(dropDownList, input_text)
        if actual_element is not None and actual_element != False:
            actual_element.click()
            time.sleep(2)
        else:
            print("Element is not found from the list")

    def type_of_reprocess(self, input_text):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.type_of_reporcess, locatorType="xpath")
        if element is not None:
            element.click()
        else:
            print("Element is ", element)
        dropDownList = self.elementPresenceCheck(ByType="xpath", locator=self.drop_down_lists)
        actual_element = self.utiles.find_dropdown_select(dropDownList, input_text)
        if actual_element is not None and actual_element != False:
            actual_element.click()
            time.sleep(2)
        else:
            print("Element is not found from the list")

    def click_plate_qc_failed_submit(self):
        element = self.waitForElement(self.plate_qc_failed_submit, locatorType="id")
        if element is not None:
            element.click()
        else:
            print("Element is ", element)

    def plate_qc_failed(self, Reason_for_Re_process, Battery, Type_of_Re_process):
        self.click_on_plate_qc_failed_button()
        self.reason_for_re_process(Reason_for_Re_process)
        self.select_battery(Battery)
        self.type_of_reprocess(Type_of_Re_process)
        self.click_plate_qc_failed_submit()

    def click_on_all_plates(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.all_plates, "id")
        element.click()

    alert_notification = "alert-loader-wrap"
    alert_click = "//*[@class='alert-loader-wrap']/span"
    alert_samples = "//*[@id='headingOne']/button"
    ack_button_list = "//*[@id='collapseOne']/div/ul/li/div/button"
    alert_close_button = "alertscloseBtn"
    alert_confirmation_button = "confirmboxokBtn"
    no_plate_selected = "//h2[@class='ng-star-inserted']"
    ack_count = "//*[@id='headingOne']/button/span"
    ack_button_loader = "//*[@class='btn-loader ng-tns-c84-3 ng-star-inserted']"

    def is_alert_notification(self):
        element = self.waitForElement(self.alert_notification, locatorType="id")
        if element is not None:
            status = True
        else:
            status = False
        return status

    def click_alerts_from_plate(self):
        time.sleep(4)
        element = self.waitForElement(self.alert_click, locatorType="xpath")
        self.waitForElementPresent(self.loader, "xpath")
        if element is not None:
            element.click()
        else:
            print("Element is None")
        # self.ElementClick(self.alert_click, "xpath")

    def click_acknowledge(self, count):
        elements = self.elementPresenceCheck(ByType="xpath", locator=self.ack_button_list)
        print(len(elements))
        print(elements)
        if len(elements) != 0:
            for element in range(0, count):
                time.sleep(1)
                print(element)
                self.waitForElementPresent(self.ack_button_loader, "xpath")
                elements[element].click()
        else:
            print("Element list is empty")

    def click_alert_close(self):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.alert_close_button, locatorType="id")
        element.click()

    def is_plate_alerts(self):
        element = self.waitForvisibilityOfElement(self.presence_of_plate_alerts, locatorType="xpath", timeout=40)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        # element = self.waitForvisibilityOfElement(self.presence_of_plate_alerts, locatorType="xpath", timeout=10)
        if element is not None:
            result = True
        else:
            result = False
        return result

    def click_alert_samples(self):
        # status = self.is_alert_notification()
        # if status != False:
        # time.sleep(2)
        ack_status = True
        if self.is_plate_alerts():
            self.click_alerts_from_plate()
            elements = self.elementPresenceCheck(ByType="xpath", locator=self.alert_samples)
            if len(elements) != 0:
                number = self.acknowledge_count()
                sum_of_Alerts = sum(number)
                print(sum_of_Alerts)
                print(number)
                for element in range(0, len(elements)):
                    elements[element].click()
                    print(number[element])
                    time.sleep(2)
                    self.click_acknowledge(number[element])
                print("alerts", sum_of_Alerts, "ackned count", self.plate_ack_count())
                if sum_of_Alerts == self.plate_ack_count():
                    ack_status = True
                else:
                    ack_status = False
                self.click_alert_close()
            else:
                print("Element list is empty")
                self.click_alert_close()
            # self.alert_confirmation()
            # time.sleep(2)
        else:
            print("There is no plate alerts found")
        return ack_status

    def acknowledge_count(self):
        emp_list = []
        acknowledge_element_count = self.elementPresenceCheck(ByType="xpath", locator=self.ack_count)
        for x in acknowledge_element_count:
            count = x.text
            number = self.utiles.multiple_character_replace(count, "(", ")")
            number = int(number)
            emp_list.append(number)
        return emp_list

    def alert_confirmation(self):
        self.waitForElementPresent(self.loader, "xpath")
        time.sleep(1)
        element = self.waitForElement(self.alert_confirmation_button, locatorType="id")
        if element is not None:
            self.ElementClick(self.alert_confirmation_button, locatorType="id")
            time.sleep(1)
            status = self.click_alert_samples()
        else:
            print("There is no alerts found")
            status = True
        return status

    def verify_plate_qc_failure(self):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.no_plate_selected, locatorType="xpath", timeout=100)
        if element is not None:
            text = element.text
            if "No Plate Selected" == text.strip():
                status = True
            else:
                status = False
        else:
            status = False
        return status

    def click_on_redraw_sample_icon(self, reason_for_redraw="Additional Testing Required",
                                    choose_help_req="Sharing Bio M (RET6)"):
        status = None
        elements = self.elementPresenceCheck(ByType="xpath", locator=self.redraw_sample_icons)
        if elements is not []:
            for element in elements:
                if "disabled" not in element.get_attribute("class"):
                    element.click()
                    self.reason_for_redraw(reason_for_redraw)
                    self.choose_help_req(choose_help_req)
                    self.redraw_submit_button()
                    time.sleep(2)
                    if "disabled" in element.get_attribute("class"):
                        status = True
                    else:
                        status = False
                    break

        else:
            print("Redraw list is empty")
        return status

    def reason_for_redraw(self, input_text):
        element = self.waitForElement(self.reason_redraw, locatorType="xpath")
        element.click()
        time.sleep(4)
        dropDownList = self.elementPresenceCheck(ByType="xpath", locator=self.redraw_iterm_list)
        actual_element = self.utiles.find_dropdown_select(dropDownList, input_text)
        actual_element.click()

    def choose_help_req(self, input_text):
        element = self.waitForElement(self.choose_help_re, locatorType="xpath")
        element.click()
        time.sleep(4)
        dropDownList = self.elementPresenceCheck(ByType="xpath", locator=self.redraw_iterm_list)
        actual_element = self.utiles.find_dropdown_select(dropDownList, input_text)
        actual_element.click()

    def redraw_submit_button(self):
        element = self.waitForElement(self.redraw_submit, locatorType="id")
        element.click()

    reprocess_text = "(//div[@class='status'])[2]"

    def re_process_status(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.reprocess_text, locatorType="xpath")
        return element.text.strip()

    acknowledged_count = "//*[@id='accordionExample']/div/div/div/ul/li/div/div[2]"

    def plate_ack_count(self):
        time.sleep(2)
        element = self.elementPresenceCheck(ByType="xpath", locator=self.acknowledged_count)
        element_count = int(len(element))
        return element_count

    def sample_battery(self, input_text):
        element = self.waitForElement(locator=self.batteryName, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(2)
            element_list = self.elementPresenceCheck(ByType="xpath", locator=self.drop_down_list)
            actual_element = self.utiles.find_dropdown_select(element_list, input_text)
            if actual_element is not None and actual_element != False:
                actual_element.click()
                time.sleep(2)
            else:
                print("Element is not found from the list")
        else:
            print("Element list is empty")

    def reason_for_reprocess_method(self, input_text):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(locator=self.reprocess_method_first_option, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(1)
            click_reason_reprocess_button = self.waitForElement(locator=self.reason_for_reproces, locatorType="id")
            if click_reason_reprocess_button is not None:
                click_reason_reprocess_button.click()
                time.sleep(2)
            else:
                print("Element is not present")

            element_list = self.elementPresenceCheck(ByType="xpath", locator=self.drop_down_list)
            actual_element = self.utiles.find_dropdown_select(element_list, input_text)
            if actual_element is not None and actual_element != False:
                actual_element.click()
                time.sleep(2)
            else:
                print("Element is not found from the list")
        else:
            print("Element is " + str(element))

    def reason_for_reprocess_drop_down(self, input_text):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(locator=self.reason_for_reproces, locatorType="id")
        if element is not None:
            element.click()
            time.sleep(1)
            element_list = self.elementPresenceCheck(ByType="xpath", locator=self.drop_down_list)
            actual_element = self.utiles.find_dropdown_select(element_list, input_text)
            if actual_element is not None and actual_element != False:
                actual_element.click()
                time.sleep(2)
            else:
                print("Element is not found from the list")

        else:
            print("Element is " + str(element))

    def sample_reprocess_submit_button(self):
        element = self.waitForElement(locator=self.samplereprocesssubmitBtn, locatorType="id")
        element.click()
        time.sleep(2)

    def sample_reprocess(self, text_1, text_2):
        reProcess_button_status = []
        status = None
        self.waitForElementPresent(self.loader, "xpath")
        elements = self.elementPresenceCheck(ByType="id", locator=self.sample_reprocess_button)
        sampleID_atrID = {}
        if elements != []:
            for x in elements:
                attribute_status = self.sample_reprocess_button_is_enabled(x)
                if attribute_status:
                    x.click()
                    sampleID = self.get_re_process_sample_id()
                    if sampleID is not None:
                        sampleID = re.sub("\(.*?\)", "()", sampleID)
                        sampleID = sampleID.replace("Sample ID - ", "").replace("()", "").strip()
                        self.reason_for_reprocess_method(text_1)
                        self.sample_battery(text_2)
                        self.sample_reprocess_submit_button()
                        time.sleep(1)
                        attribute_status = self.sample_reprocess_button_is_enabled(x)
                        print("attribute status", attribute_status)
                        reProcess_button_status.append(attribute_status)
                        atrSampleProcessingID = self.get_atr_sampleProcessingId()
                        sampleID_atrID[sampleID] = atrSampleProcessingID

                    else:
                        print("SampleId is None")

                else:
                    print("Element is not enabled")
            for stat in reProcess_button_status:
                if stat == False:
                    print("Reprocess element is disabled")
                    status = True
                else:
                    print("Reprocess element is not disabled")
                    status = False
                    break

        else:
            print("Element list is empty")
        return sampleID_atrID, status

    reprocess_sampleID_element = "(//*[@class='d-flex']/p)[2]"

    def get_re_process_sample_id(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(self.reprocess_sampleID_element, locatorType="xpath")
        if element is not None:
            element = element.text
        else:
            print("Element is None")
        return element

    def get_atr_sampleProcessingId(self):
        connect = MysqlConnection(dev_ddc_host, dev_ddc_db, dev_db_username, dev_db_password)
        ID = connect.mysql_connect(
            "SELECT atrSampleProcessId FROM 00devanr789.SampleReProcessRequest order by sampleReprocessId desc limit 1")
        return ID

    plate_menu = "navbarPlates"

    def click_on_plate_menu(self):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.plate_menu, locatorType="id")
        if element is not None:
            element.click()
        else:
            print("Element is None")

    def sample_reprocess_button_is_enabled(self, element):
        attribute_text = element.get_attribute("class")
        attribute_status = self.utiles.is_button_enabled(attribute_text)
        return attribute_status

    plate_details_tab = "//a[@id='plate-details-tab']"

    def click_plate_details_tab(self):
        self.waitForElementPresent(self.loader, "xpath")
        element = self.waitForElement(self.plate_details_tab, "xpath")
        if element is not None:
            element.click()
        else:
            print("Element is None")

    def edit_gene_marker_table(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")

        element = self.waitForElement(self.edit_gene_marker_table_icon, locatorType="xpath")
        if element is not None:
            element.click()
        else:
            print("Element is None")

    def get_first_column_element_value(self, count):
        get_first_column_element_text = f"//*[@id='datareviewmainTable']/tbody/tr[{count}]/td[1]/span"
        element_text = None
        self.waitForElementPresent(self.loader, locatorType="xpath")
        element = self.waitForElement(get_first_column_element_text, locatorType="xpath")
        if element is not None:
            element_text = element.text.strip()
        else:
            print("Element is None")
        return element_text

    def update_the_first_column_value(self, counter, input_text):
        row_value_change = f"//*[@id='datareviewmainTable']/tbody/tr[{counter}]/td[1]/input"
        element = self.waitForElement(row_value_change, locatorType="xpath")
        if element is not None:
            if input_text is not None:
                if input_text == "X":

                    element.clear()
                    time.sleep(1)
                    element.send_keys("Y")
                else:
                    element.clear()
                    time.sleep(1)
                    element.send_keys("X")
            else:
                print("Element text is None")
        else:
            print("Element is None")

    def data_review_save(self):
        element = self.waitForElement(self.data_review_save_icon, locatorType="id")
        if element is not None:
            element.click()
            self.waitForElementPresent(self.data_review_save_icon, locatorType="id")
        else:
            print("data review save button is None")

    def update_data_review_column_value(self, sample):
        # value_text = self.get_first_column_element_value()
        # self.edit_gene_marker_table()
        # self.update_the_first_column_value(value_text)
        self.edit_sample_id_from_data_review(sample)
        self.data_review_save()

    def verify_case_type(self):
        rowList = self.driver.find_elements(By.XPATH, self.row)
        CaseType = []
        for x in range(1, len(rowList) + 1):
            x = str(x)
            trs = "[" + x + "]"
            sampleId = self.getElement(self.row + trs + "/td[1]", "xpath").text

            if "S-" in sampleId:
                caseType = self.getElement(self.row + trs + "/td[5]", "xpath").text
                CaseType.append(caseType)
        return CaseType[0]

    def click_dataReviewEditBt(self):
        self.waitForElement(self.dataReviewEditIcon, locatorType="id")
        button_enable = self.getElement(self.dataReviewEditIcon, locatorType="id")
        if button_enable.is_enabled():
            # self.waitForElement(self.upload)
            self.ElementClick(self.dataReviewEditIcon, "id")
            time.sleep(2)
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            self.log.info("button is not present")

    def alertBadgePresenceVerify(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.AlertBadge)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        badge = self.isElementPresent(self.AlertBadge)
        return badge

    def alert_button(self):
        self.waitForElement(self.AlertIcon, "xpath")
        self.ElementClick(self.AlertIcon, "xpath")

    def alertCheck(self):
        if self.alertBadgePresenceVerify() is not False:
            self.alert_button()
            time.sleep(2)
        else:
            self.log.info("No alert in this case")

    def alert_PlusButton(self):
        self.waitForElement(self.plusIcon_inAlert, "xpath")
        self.ElementClick(self.plusIcon_inAlert, "xpath")
        time.sleep(1)

    def getWarningText(self):
        self.waitForElement(self.alertWarningText)
        warning = self.isElementTextPresent(self.alertWarningText, "xpath")
        splittedwarning = self.utiles.SplitWarning(warning)
        return splittedwarning

    def colorPresence(self):
        color = self.driver.find_elements(By.XPATH, self.orangeColor).value_of_css_property('background-color')
        list = []
        # orange = Color.from_string(
        #     self.driver.find_elements(By.XPATH, self.orangeColor).value_of_css_property('background-color'))
        for x in color:
            if Color.from_string(x.value_of_css_property('background-color')) != x.rgba(0, 0, 0, 0):
                list.append(x.value_of_css_property('background-color'))
                break
            return list

    def alert_CloseButton(self):
        self.waitForElement(self.alertClose, "id")
        self.ElementClick(self.alertClose, "id")

    # def clickAcknowledgeBt(self):
    #     self.waitForElement(self.acknowledgeBt, "id")
    #     self.ElementClick(self.acknowledgeBt, "id")

    def clickAcknowledgeBt(self):
        ele = self.elementPresenceCheck(ByType=By.XPATH, locator=self.allAcknowledgeBt)
        for x in ele:
            self.webScroll(self.scroll_view_element(self.allAcknowledgeBt, locatorType="xpath"))
            x.click()
            self.waitForElementPresent(self.acknowledge_button_loader, locatorType="css_selector", timeout=100)

    def click_ConfirmBt(self):
        self.waitForElement(self.confirmBt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if self.confirmBt is not False:
            self.ElementClick(self.confirmBt, "id")
        else:
            pass

    def RedColorPresence(self):
        # orange = Color.from_string(self.driver.find_element(By.XPATH, self.orangeColor).value_of_css_property('color'))
        red = Color.from_string(
            self.driver.find_element(By.XPATH, self.redColor).value_of_css_property('background-color'))
        print(red)
        return red

    def BlueColorPresence(self):
        # orange = Color.from_string(self.driver.find_element(By.XPATH, self.orangeColor).value_of_css_property('color'))
        blue = Color.from_string(
            self.driver.find_element(By.XPATH, self.BlueColor).value_of_css_property('background-color'))
        print(blue)
        return blue

    def colorPresence1(self):
        color = "//table[@id='datareviewmainTable']//tbody//td[4]"
        x = []
        a = self.elementPresenceCheck(ByType=By.XPATH, locator=color)
        for b in a:
            ColorPresent = Color.from_string(b.value_of_css_property('background-color'))
            x.append(ColorPresent)
        return x

    def GreenColorPresence(self):
        # orange = Color.from_string(self.driver.find_element(By.XPATH, self.orangeColor).value_of_css_property('color'))
        green = Color.from_string(
            self.driver.find_element(By.XPATH, self.GreenColor).value_of_css_property('background-color'))
        print(green)
        return green

    def acknowledgeAllSample(self):
        # list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.alertTable_list)
        list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.plusIcon_inAlert)
        for ele in list:
            ele.click()
            self.clickAcknowledgeBt()

    def noDataFound(self):
        # self.waitForElement(self.NO_DATA_FOUND, "xpath")
        self.waitForElementPresent(self.SCROLL_LOADER, "xpath")
        result = self.isElementPresent(self.nodataFound, "xpath")
        if result is False:
            return False
        else:
            print("No data found")
            return True

    def clickDueDate_Icon(self):
        self.waitForElement(self.dueDateIcon, "xpath")
        self.ElementClick(self.dueDateIcon, "xpath")

    def click_testID_button(self):
        self.waitForElement(self.testIDbutton, "xpath")
        self.ElementClick(self.testIDbutton, "xpath")

    def testID_selection(self):
        self.waitForElement(self.testID_select)
        t_party_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.testID_select)
        for ele in t_party_list:
            if ele is not False:
                ele.click()
            else:
                self.log.error("no tested party present")

    def choose_delayDate(self, date):
        ele = self.changeDateCalendar
        if date is not None:
            self.waitForElement(ele, locatorType="xpath")
            self.webScroll(self.scroll_view_element(ele, locatorType="xpath"))
            self.waitForElement(ele, locatorType="xpath")
            self.select_date_from_calender(date, ele, locatorType="xpath")
        else:
            pass

    def click_delaySubmit(self):
        self.waitForElement(self.delaySubmit, "id")
        self.ElementClick(self.delaySubmit, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def change_delayDate(self, date):
        self.clickDueDate_Icon()
        self.click_testID_button()
        self.testID_selection()
        self.choose_delayDate(date)
        time.sleep(1)
        self.click_delaySubmit()

    def delayDate_verification(self):
        list = []
        enableCheck = self.elementPresenceCheck(ByType=By.XPATH, locator=self.sampleTable_Actionlist)
        for row in range(len(enableCheck)):
            ele = self.driver.find_elements(By.XPATH, self.sampleTable_Actionlist + "//li[1]/a")[row]
            self.webScroll(ele)
            ele1 = self.driver.find_elements(By.XPATH, self.delayField)[row]
            if "-" not in ele1.text:
                list.append(ele1.text)
                break
        return list

    def getdueDate(self):
        self.waitForElement(self.delayField, "xpath")
        due = self.isElementTextPresent(self.delayField, "xpath")
        return due

    # plate_details_sample_rows = "//*[@id='myplatemainTable']/tr/td[2]"

    def get_mother_sample_id_from_plate_details_table(self):
        sample_id = None
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_list = self.elementPresenceCheck(ByType="xpath", locator=self.plate_details_sample_rows)
        if ele_list != []:
            for row_element in range(1, len(ele_list) + 1):
                print(row_element)
                row_element = str(row_element)
                tested_party_element = f"//*[@id='myplatemainTable']/tr[{row_element}]/td[2]"
                tested_patry = self.waitForElement(tested_party_element)
                tested_patry_text = tested_patry.text.strip()
                if "Mother" == tested_patry_text:
                    sample_id_element = f"//*[@id='myplatemainTable']/tr[{row_element}]/td[1]"
                    sample_element = self.waitForElement(sample_id_element)
                    if sample_element is not None:
                        sample_id = sample_element.text.strip()
                        break
                    else:
                        print("Sample id is None")
                else:
                    print("Tested party is not matching")
        else:
            print("Element list is empty ")
        return sample_id

    def edit_sample_id_from_data_review(self, sample_id):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_list = self.elementPresenceCheck(ByType="xpath", locator=self.sample_ids_from_datareview)
        if ele_list != []:
            i = 0
            for element in ele_list:
                i += 1
                if sample_id == element.text.strip():
                    edit_element = f"(// *[@ id='datarevieweditIcon'])[{i}]"
                    element = self.waitForElement(edit_element, locatorType="xpath")
                    if element is not None:
                        value_text = self.get_first_column_element_value(i)
                        element.click()
                        self.update_the_first_column_value(i, value_text)

                    else:
                        print("Element is None")
                else:

                    print("Sample id" + str(sample_id), element.text)
        else:
            print("Element list is empty")

    def click_ok_alert_confirmation(self):
        self.waitForElementPresent(self.loader, "xpath")
        time.sleep(1)
        element = self.waitForElement(self.alert_confirmation_button, locatorType="id")
        if element is not None:
            self.ElementClick(self.alert_confirmation_button, locatorType="id")
            time.sleep(1)
        else:
            print("Alert confirmation pop is not open")

    status_plate_details = "(//*[@class='status'])[1]"

    def verify_unacknowlodge(self):
        element = self.waitForElement(self.status_plate_details, locatorType="xpath", timeout=100)
        return element.text.strip()
    def fetch_sample(self):
        li = []
        iconList = "//table[@id='datareviewactionsTable']//tbody//td//ul"
        fetchID = "//table[@id='datareviewdetailTable']//tbody//td//div//div"
        pdfIcon = self.elementPresenceCheck(ByType=By.XPATH, locator=iconList)
        print(len(pdfIcon))
        for row in range(0, len(pdfIcon)):
            ele = self.driver.find_elements(By.XPATH, iconList + "//li[5]/a")[row]
            ele.click()
            time.sleep(2)
            self.EgramVIewCLose()
            sample_id = fetchID
            ele1 = self.driver.find_elements(By.XPATH, sample_id)[row]
            if ele1.text is not None:
                sNo = ele1.text
                print(sNo)
                li.append(sNo)
        return li