import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.common_function import CommonUtil
import logging
import utilities.custom_logger as cl
from configurations.config_changes import *


class CaseFiles(BasePage):
    log = cl.customLogger(logging.DEBUG)
    utiles = CommonUtil()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    caseID = "//h1[normalize-space()]"
    LOGIN_BUTTON = "//button[@type='button']"
    case_file = "menubarcaseFiles"
    help_ticket = "//li//a[contains(@class,'help')]"
    case_id = 'caseNo'
    new_case = "searchlistingnewcaseBtn"
    new_case_label = "//h1[normalize-space()='New Case']"
    channel = "//app-single-select[@uid='channelId']//button[@type='button']"
    channel_list = "//app-single-select[@uid='channelId']//div//ul//li//a//div"
    state = "//app-single-select[@uid='stateId']//div//button"
    state_list = "//ul[@role='list']//li//a//div"
    search = "(//input[@placeholder='Search'])[1]"
    account = "//app-single-select[@id='Account']//div//button"
    acc_list = "//*[@label='agencyName']/div/div/ul/li//a//div"
    auth_doc = 'authentication'
    agency_case = 'agencycaseno'
    test_type = "//div//app-single-select[@uid='testTypeId']//div//button//span[1]"
    test_type_list = "//*[@label='testType']//div//div//ul//li//a//div"
    test_type_label = "//div[@class='status'][normalize-space()='Paternity']"
    reconstruct_section = "//div//app-single-select[@uid='section']//div//button//span[1]"
    reconstruct_list = "//*[@label='section']//div//div//ul//li//a//div"
    case_definition = "//div//app-single-select[@uid='subCategoryId']//div//button"
    case_def_list = "//*[@label='subCategory']//div//div//ul//li//a//div"
    case_def_label = "//div[contains(text(),'Paternity Trio')]"
    add_testing = "//app-single-select[@label='additionalTest']//div//button"
    add_test_list = "//*[@label='additionalTest']//div//div//ul//li//a//div"
    type = "//app-single-select[@id='Type']//div//button"
    type_list = "//*[@label='type']//div//div//ul//li//a//div"
    turn_around = "//button[@id='id']"
    edit_turn_around = "//button[@id='Turnaround']"
    turnaround_list = "//*[@label='tatDisplay']//div//div//ul//li//a//div"
    billing_type = 'Private'
    court_order = 'courtOrder'
    language = "//div[@class='ngx-dropdown-button']"
    drop_check_list = "//ul[@class='available-items']//li//a//div"
    affidavit_type = "//app-single-select[@uid='key']//button[@type='button']"
    loader = "//*[@class='loader']"
    barcode = "newcasekitbarcode"
    country = "//app-single-select[@uid='countryId']//button[@type='button']"
    country_list = "//app-single-select[@uid='countryId']//div//ul//li//div"
    ref1 = "Reference1"
    ref2 = "Reference2"
    dins = "DNIS"
    # customer = 'Account'
    customer = 'customer'
    c_phone = "accountphone"
    c_email = "accountemail"
    c_relation = "Accountrel"
    rel_list = "//*[@label='relationType']//div//div//ul//li//a//div"
    M_sample_id = 'sampleNo0'
    C_sample_id = 'sampleNo1'
    AF_sample_id = 'sampleNo2'
    sample_id = "sampleNo"
    M_sdt_click = "//div[@class='right-table']//table[1]//tbody//tr[2]//td//button"
    C_sdt_click = "//div[@class='right-table']//table[2]//tbody//tr[2]//td//button"
    AF_sdt_click = "//div[@class='right-table']//table[3]//tbody//tr[2]//td//button"
    M_ddt_click = "//div[@class='right-table']//table[1]//tbody//tr[3]//td//button"
    C_ddt_click = "//div[@class='right-table']//table[2]//tbody//tr[3]//td//button"
    AF_ddt_click = "//div[@class='right-table']//table[3]//tbody//tr[3]//td//button"
    month_year = "//button[@aria-label='Choose month and year']"
    previous_cal = "//button[@aria-label='Previous 24 years']"
    range_list = "//span[@class='mat-button-wrapper']/span"
    Indicators = "//div[@mattooltip='Indicators']"
    SurrIVF = "//li[text()=' Surrogacy/ IVF']//input"
    SurrIVFtxt = "//li[text()=' Surrogacy/ IVF']"
    next_cal = "//button[@class='mat-focus-indicator mat-calendar-next-button mat-icon-button " "mat-button-base']"
    cal_list = "//*[@class='mat-calendar-body']/tr/td"
    M_sample_type = "sampleType0"
    C_sample_type = "sampleType1"
    AF_sample_type = "sampleType2"
    sampleType = "sampleType"
    M_sample_type_sel = "(//div[@class='right-table']//table[1]//tbody//tr[4]//button)[2]"
    C_sample_type_sel = "(//div[@class='right-table']//table[2]//tbody//tr[4]//button)[2]"
    AF_sample_type_sel = "(//div[@class='right-table']//table[3]//tbody//tr[4]//button)[2]"
    sample_type_list = "//ul[@role='list']//li//a//div"
    M_sel_samptype = "(//app-single-select[@uid='sampleSubTypeId']//button[@type='button'])[1]"
    C_sel_samptype = "(//app-single-select[@uid='sampleSubTypeId']//button[@type='button'])[2]"
    AF_sel_samptype = "(//app-single-select[@uid='sampleSubTypeId']//button[@type='button'])[3]"
    M_firstname = "firstName0"
    C_firstname = "firstName1"
    AF_firstname = "firstName2"
    firstname = "firstName"
    lastname = "lastName"
    M_lastname = "lastName0"
    C_lastname = "lastName1"
    AF_lastname = "lastName2"
    M_AKA = "aka0"
    C_AKA = "aka1"
    AF_AKA = "aka2"
    M_deceased = "deceased0"
    C_deceased = "deceased1"
    AF_deceased = "deceased2"
    lang_list = "//ul[@class='available-items']//li//div//label"
    lang_sel = "//ul[@class='available-items']//li//div//input"
    dropdown_list = "//ul[@class='available-items d-block']//li//a//div"
    M_gender = "gender0"
    C_gender = "gender1"
    AF_gender = "gender2"
    dob_m = "//div[@class='right-table']//table[1]//tbody//tr[11]//td//button"
    retail_dob_m = "//div[@class='right-table']//table[1]//tbody//tr[10]//td//button"
    dob_c = "//div[@class='right-table']//table[2]//tbody//tr[11]//td//button"
    retail_dob_c = "//div[@class='right-table']//table[2]//tbody//tr[10]//td//button"
    dob_af = "//div[@class='right-table']//table[3]//tbody//tr[11]//td//button"
    retail_dob_af = "//div[@class='right-table']//table[3]//tbody//tr[10]//td//button"
    ssn_m = "ssn0"
    ssn_c = "ssn1"
    ssn_af = "ssn2"
    race_m = "race0"
    common_race = "race"
    retail_race_m = "//div[@class='right-table']//table[1]//tbody//tr[11]//td//button"
    race_m_list = "//div[@class='right-table']//table[1]//tbody//tr[13]//td//app-single-select//ul//li//a"
    retail_race_m_list = "//div[@class='right-table']//table[1]//tbody//tr[11]//td//app-single-select//ul//li//a"
    race_c = "race1"
    race_c_list = "//div[@class='right-table']//table[2]//tbody//tr[13]//td//app-single-select//ul//li//a"
    race_af = "race2"
    retail_race_af = "//div[@class='right-table']//table[3]//tbody//tr[11]//td//button"
    race_af_list = "//div[@class='right-table']//table[3]//tbody//tr[13]//td//app-single-select//ul//li//a"
    retail_race_af_list = "//div[@class='right-table']//table[3]//tbody//tr[11]//td//app-single-select//ul//li//a"
    col_date_m = "//div[@class='right-table']//table[1]//tbody//tr[14]//td//button"
    retail_col_dt_m = "//div[@class='right-table']//table[1]//tbody//tr[12]//td//button"
    col_date_c = "//div[@class='right-table']//table[2]//tbody//tr[14]//td//button"
    retail_col_dt_c = "//div[@class='right-table']//table[2]//tbody//tr[12]//td//button"
    retail_col_dt_af = "//div[@class='right-table']//table[3]//tbody//tr[12]//td//button"
    col_date_af = "//div[@class='right-table']//table[3]//tbody//tr[14]//td//button"
    col_site_bt_m = "collectionSite0"
    col_site_bt_c = "collectionSite1"
    col_date_bt_af = "collectionSite2"
    col_site_bt_edit_m = "//div[@class='right-table']//table[1]//*[@label='siteName']//div//button"
    col_site_bt_edit_c = "//div[@class='right-table']//table[2]//*[@label='siteName']//div//button"
    m_tracking = 'tracking0'
    retail_tracking_m = "//div[@class='right-table']//table[1]//tbody//tr[14]//td//input"
    c_tracking = 'tracking1'
    retail_tracking_c = "//div[@class='right-table']//table[2]//tbody//tr[14]//td//input"
    af_tracking = 'tracking2'
    retail_tracking_af = "//div[@class='right-table']//table[3]//tbody//tr[14]//td//input"
    tracking = "tracking"
    invoice_date_m = "//div[@class='right-table']//table[1]//tbody//tr[23]//td//button"
    invoice_date_c = "//div[@class='right-table']//table[2]//tbody//tr[23]//td//button"
    invoice_date_af = "//div[@class='right-table']//table[3]//tbody//tr[23]//td//button"
    save = "newcaseSaveBtn"
    edit_bt = "casedetailseditIcon"
    accession = "newcaseAccessionBtn"
    test_samples = "newcaseSamplesBtn"
    cancel = "newcaseCancelBtn"
    create = "//button[normalize-space()='Create']"
    add_new = "//button[normalize-space()='Add New']"
    created = "//span[@class='btn btn-outline-primary btn-edit']"
    case = "//div[@class='header']//div//h1"
    doc = "casesidetabdocsIcon"
    add = "documentuploadaddBtn"
    scan_close = "//div[@class='dynamsoft-dialog-close']"
    document = "//div[@class='ngx-dropdown-container']//div[@class='input-block']"
    doc_list = "//div[@class='ngx-dropdown-list-container dropdown-search ng-star-inserted']//ul//li//div"
    tested_party = "//div[@class='row g-4 ng-star-inserted']//div[2]//app-multi-selector"
    party_list = "//div[@class='ngx-dropdown-list-container dropdown-search ng-star-inserted']//ul//li//input"
    comment = "enterComments"
    browse = "//input[@type='file']"
    upload = "documentuploadBtn"
    add_new_doc = "uploadaddnewIcon"
    add_new_collsite_bt = "collectionsiteselectoraddnewBtn"
    add_new_collectorName_bt = "colloctornameselectoraddnewBtn"
    close = "documentuploadexpandBtn"
    file = "//table[@class='table doc-table']//tbody//td[1]//span"
    c_id = "//button//div[@class='d-flex align-items-center']//span"
    case_search = "searchinputssearchBtn"
    clear = "searchinputsclearBtn"
    status = "//div[@class='details']//div[2]"
    table_view = "//div[@class='case-table-scroll']//div[@class='listing-box position-relative']"
    yes = "alertsuccess"
    skip = "kitbarcodeconfirmationskipBtn"
    start_yes = "casedetailsyesBtn"
    submission = "searchlistingsubmissionBtn"
    start_button = "casedetailsstartIcon"
    case_status = "//div[@class='dropdown']//button"
    anc_r_id = 'requestid'
    search_button = "searchinputssearchBtn"
    submission_search = 'irregularfiltersearchBtn'
    anc_profile = "//div[@class='user--icon d-none d-xl-block']"
    anc_logout = "headerlogoutIcon"
    acc = "//div[@role='listitem']"
    plus_button = "//table[@class='table table-layout-fixed']//tbody//ul//li[1]//a"
    req_id_tab = 'request1-tab0'
    drag_ele = "//div[@class='table-responsive sample-table report-table ng-star-inserted']//table//tbody//tr[1]"
    drag_ele2 = "//div[@class='table-responsive sample-table report-table ng-star-inserted']//table//tbody//tr[2]"
    move_ele = "//div[@class='right-table']//table[1]//tbody"
    sub_close = "//button[@aria-label='Close']"
    submission_col = "//ul[@class='menu-list']//li[1]//a"
    M_lnameEdited = "//*[@class='right-table']//table[1]/tbody[1]/tr[8]/td[1]/input"
    C_lnameEdited = "//*[@class='right-table']//table[2]/tbody[1]/tr[8]/td[1]/input"
    AF_lnameEdited = "//*[@class='right-table']//table[3]/tbody[1]/tr[8]/td[1]/input"
    M_mnameEdited = "//*[@class='right-table']//table[1]/tbody[1]/tr[7]/td[1]/input"
    C_mnameEdited = "//*[@class='right-table']//table[2]/tbody[1]/tr[7]/td[1]/input"
    AF_mnameEdited = "//*[@class='right-table']//table[3]/tbody[1]/tr[7]/td[1]/input"
    m_ssn_ed = "//*[@class='right-table']//table[1]/tbody[1]/tr[13]//td//input"
    ver_samp_ed = "//div[@class='right-table right-table-view']//table[1]//tbody//tr[13]//td"
    comp_req = 'CompletedRequests'
    hammer = "//tbody/tr[1]/td[1]/ul[1]/li[1]/a[1]"
    flag_checkbox = 'emergency'
    acknowledge = "//button[normalize-space()='Acknowledge']"
    rf_req = "//table[@class='table']//tbody//tr[1]//td[1]"
    green_flag = "//table[@class='table']//tbody//tr[1]//td[1]//div[@class='ribbon-top-left green ng-star-inserted']"
    qc = "menubarQC"
    qc_samp_id = 'mother'
    qc_c_s_id = "//div[@class='right-table']//table[2]//tbody//tr[1]//td//input"
    qc_af_s_id = "//div[@class='right-table']//table[3]//tbody//tr[1]//td//input"
    ver_m_s_id = "//table[@class='table ng-star-inserted'][1]//tbody//tr[2]//td"
    ver_c_s_id = "//table[@class='table ng-star-inserted'][2]//tbody//tr[2]//td"
    ver_af_s_id = "//table[@class='table ng-star-inserted'][3]//tbody//tr[2]//td"
    ver_m_col_dt = "//table[@class='table ng-star-inserted'][1]//tbody//tr[15]//td"
    ver_c_col_dt = "//table[@class='table ng-star-inserted'][2]//tbody//tr[15]//td"
    ver_af_col_dt = "//table[@class='table ng-star-inserted'][3]//tbody//tr[15]//td"
    ver_m_f_name = "//table[@class='table ng-star-inserted'][1]//tbody//tr[6]//td"
    ver_c_f_name = "//table[@class='table ng-star-inserted'][2]//tbody//tr[6]//td"
    ver_af_f_name = "//table[@class='table ng-star-inserted'][3]//tbody//tr[6]//td"
    pass_button = "samplecheckpassBtn"
    submit = "//button[normalize-space()='Submit']"
    delivery_pref = "//li[@id='casesidetabdeliveryIcon']//a"
    deli_pref_edit = "//button[normalize-space()='Edit']"
    delivery_pref_add = "//button[@id='caseseliverypreferenceaddBtn']"
    deli_pref_list = "//div[@aria-labelledby='caseseliverypreferenceaddBtn']//ul//li//a"
    copy = 'nocopies'
    delivery_mode = "//input[@id='del5']"
    standard_mail = "//input[@id='del1']"
    doc_req = 'doc1'
    address = "//input[@id='Address1']"
    cus_country = "//div[5]//app-single-select[@id='country']//div[1]//button[1]"
    c_list = "//ul[@id='displayList_']//li//div"
    zip = "//input[@id='Zip']"
    phone = '//input[@id="phone"]'
    cus_state = "//div[@class='col-md-6 mb-3'][7]//app-single-select[1]//button"
    city = 'City'
    deli_pref_save = "deliverypreferenceformsaveBtn"
    deli_pref_close = "casedeliverypreferencebacktocaseBtn"
    doc_upload_close = "documentuploadcloseBtn"
    doc_expandButton = "documentuploadexpandBtn"
    M_fnameEdited = "//*[@class='right-table']//table[1]/tbody[1]/tr[6]/td[1]/input"
    C_fnameEdited = "//*[@class='right-table']//table[2]/tbody[1]/tr[6]/td[1]/input"
    sample_rcvd_mEdited = "//div[@class='right-table']//table[1]//tbody//tr[3]//td//button"
    sample_rcvd_cEdited = "//div[@class='right-table']//table[2]//tbody//tr[3]//td//button"
    discard_date_mEdited = "//div[@class='right-table']//table[1]//tbody//tr[4]//td//button"
    discard_date_cEdited = "//div[@class='right-table']//table[2]//tbody//tr[4]//td//button"
    dob_mEdited = "//div[@class='right-table']//table[1]//tbody//tr[12]//td//button"
    dob_cEdited = "//div[@class='right-table']//table[2]//tbody//tr[12]//td//button"
    collection_date_mEdited = "//div[@class='right-table']//table[1]//tbody//tr[15]//td//button"
    collection_date_cEdited = "//div[@class='right-table']//table[2]//tbody//tr[15]//td//button"
    tracking_mEdited = "//*[@class='right-table']/table[1]/tbody[1]/tr[21]//td//input"
    tracking_cEdited = "//*[@class='right-table']/table[2]/tbody[1]/tr[21]//td//input"
    invoice_date_mEdited = "//div[@class='right-table']//table[1]//tbody//tr[24]//td//button"
    invoice_date_cEdited = "//div[@class='right-table']//table[2]//tbody//tr[24]//td//button"
    expected_mfname = "(//tr)[32]//td"
    expected_cfname = "(//tr)[57]//td"
    app_tooster_error = "//app-toaster//div[@class='alert alert--error ng-star-inserted']"
    app_tooster_success = "//app-toaster//div[@class='alert alert--success ng-star-inserted']"
    success_msgg = "//app-toaster//div[2]//h2"
    error_msgg = "//app-toaster//div[2]//h2"
    title_m = "//div[normalize-space()='M']"
    title_c = "//div[normalize-space()='C']"
    title_af = "//div[normalize-space()='AF']"
    details_table = "//div[@class='details']//div[1]"
    more_option_m = "dropdownMenuMore0"
    more_option_c = "//th[@class='child']//span[@id='dropdownMenuMoredet']"
    more_option_af = "dropdownMenuMore2"
    remove_sample = "//a[normalize-space()='Remove sample']"
    request_schedule = "casedetailsrequestscheduleIcon"
    confirmation_cb1 = "(//input[@type='checkbox'])[3]"
    confirmation_cb2 = "(//input[@type='checkbox'])[4]"
    confirmation_cb3 = "(//input[@type='checkbox'])[5]"
    confirm_bt = "schedulingrequestconfirmBtn"
    exp_caseId = "//div[@class='d-flex align-items-center']//span[@class='caseid']"
    testedParty_addbt = "//div[@class='d-flex justify-content-end']//button"
    testedParty_addList = "//div[@class='dropdown-menu add-dropdown-menu show']//ul//li"
    previous_bt = "//div[@class='prev']"
    next_bt = "//div[@class='next']"
    sampleId_title = "//td[normalize-space()='Sample ID']"
    sampleRcvd_title = "//td[normalize-space()='Sample Received']"
    caseFile_title = "//div//h1[text()='Case Files']"
    expand_bt = "//div[@class='expand-btn']"
    quick_search_tab = "quicksearch-tab"
    advance_search_tab = "advancedsearch-tab"
    case_id_inp = "caseNo"
    sample_rcvd_m = "(//span[@class='mat-button-wrapper'])[1]"
    update_bt = "caseeditupdateIcon"
    collection_date_m = "//div[@class='right-table']//table[1]//tbody//tr[15]//td//button"
    collection_date_c = "//div[@class='right-table']//table[2]//tbody//tr[15]//td//button"
    collection_date_af = "//div[@class='right-table']//table[3]//tbody//tr[15]//td//button"
    collector_name_m = "//div[@class='right-table']//table[1]//tbody//tr[16]//td//button"
    collector_name_c = "//div[@class='right-table']//table[2]//tbody//tr[16]//td//button"
    collector_name_adv_Msch = "//div[@class='right-table']//table[1]//tbody//tr[16]//td//div//div//" \
                              "a[normalize-space()='Advanced Search']"
    collector_name_adv_Csch = "//div[@class='right-table']//table[2]//tbody//tr[16]//td//div//div//" \
                              "a[normalize-space()='Advanced Search']"
    coll_fname = "//input[@id='Collector Name']"
    coll_lname = "//form[@class='ng-pristine ng-invalid ng-touched']//div[@class='row']//div[2]//input"
    exp_coll_id = "(//tr)[43]//td"
    closed_case_status = "//div[@class='details']//div[@class='content']//div[@class='status--btn']"
    view_report = "//div[@class='case__content--block position-relative case__content--scrolldet']//div[" \
                  "@class='header']//ul//li[1] "
    report_preview = "//h5[normalize-space()='Report Preview']"
    pdf_icon = "//div[@class='pdf']"
    close_icon = "//div[@class='modal-content']//div[@class='case-wrap']//button"
    help_icon = "casedetailshelpIcon"
    help_icon_active = "casedetailshelpIcon"
    close_icon_hlp = "//div[@class='modal-header align-items-center']//button[@aria-label='Close']"
    add_hlp_closeIcon = "//div[@class='modal-header align-items-center']//div[@aria-label='Close']"
    choose_help_request = "//button[@class='ngx-dropdown-button']//span"
    choose_hlp_req_input = "//div[@class='search-wrap ng-star-inserted']//input"
    help_req_list = "//ul[@role='list']//li"
    samples_require_hlp = "//div[@class='form-check ng-star-inserted']//input"
    help_submit_bt = "createticketsubmitBtn"
    help_cancel_bt = "createticketcancelBtn"
    help_add_icon = "listticketsaddhelpIcon"
    dob_close = "//div[@class='modal-content']//button[@aria-label='Close']"
    drag_m = "//div[@class='table-responsive sample-table report-table ng-star-inserted']//table//tbody//tr[1]"
    drag_c = "//div[@class='table-responsive sample-table report-table ng-star-inserted']//table//tbody//tr[3]"
    drag_af = "//div[@class='table-responsive sample-table report-table ng-star-inserted']//table//tbody//tr[2]"
    close_msg = "//button[@class='btn-close ng-star-inserted']"
    drag = "//div[@class='table-responsive sample-table report-table ng-star-inserted']//table//tbody//tr"
    tp_role = "//div[@class='table-responsive sample-table report-table ng-star-inserted']//table//tbody//th"
    closeMessage = "//button[@class='btn-close ng-star-inserted']"
    amend_bt = "finalreportviewamendBtn"
    resend_bt = "//button[normalize-space()='Re Send']"
    amend_editBt = "sampledetailseditBtn"
    middle_name_amend = "//div[@class='right-table']//table[1]//tr[2]//td//div//input"
    amend_update_Bt = "sampledetailsupdateBtn"
    commentClk = "//li[@mattooltip='Comments']"
    typeDrop = "(//app-single-select)[1]/div/button/span[2]"
    Noteselect = "(//li[@role])[4]"
    ReviewSelect = "(//li[@role])[3]"
    reasonDrop = "(//app-single-select)[2]/div/button/span[2]"
    textarea = "//textarea[@placeholder='Leave a comment']"
    Post = "//button[text()='Post']"
    submitLoader = "//*[@id='commentsModal']//app-content-loader/div/div[@class='loader']"
    addedComment = "//div[@class='post']/p"
    commentClose = "//div[@class='modal-content']//button[@aria-label='Close']"
    progress_wrp = "//div[@class='progress-wrap']"
    uploadLoader = "//*[@id='docsModal']/div/app-content-loader/div/div"
    toaster_close = "//button[@data-bs-dismiss='toast']"
    case_type = "//div[@class='row g-3 view-section']//div[10]//p"
    audit_flag = "//div[@class='ribbon-top ng-star-inserted']//span[text()='Audited']"
    caseDef = "//div[@class='row g-3 view-section']//div[11]//p"
    m_sample_rcvd = "//div[@class='right-table right-table-view']//table[1]//tbody//tr[3]//td"
    c_sample_rcvd = "//div[@class='right-table right-table-view']//table[2]//tbody//tr[3]//td"
    af_sample_rcvd = "//div[@class='right-table right-table-view']//table[3]//tbody//tr[3]//td"
    case_role_m = "//div[@class='right-table right-table-view']//table[1]//tbody//tr[4]//td"
    case_role_c = "//div[@class='right-table right-table-view']//table[2]//tbody//tr[4]//td"
    case_role_af = "//div[@class='right-table right-table-view']//table[3]//tbody//tr[4]//td"
    ver_account = "//div[@class='col-md-3 ng-star-inserted'][2]//p"
    ver_m_e_lastname = "//*[@class='right-table right-table-view']//table[1]//tbody[1]//tr[8]//td"
    ver_c_e_lastname = "//*[@class='right-table right-table-view']//table[2]//tbody[1]//tr[8]//td"
    ver_af_e_lastname = "//*[@class='right-table right-table-view']//table[3]//tbody[1]//tr[8]//td"
    indicator_c = "//th[@class='child']//div[@class='mat-tooltip-trigger indicator']"
    related_f_m = "//div[@class='left ng-star-inserted']//ul//li[11]"
    related_f_m_button = "//div[@class='left ng-star-inserted']//ul//li[11]//div//input"
    resend = "//ul[@class='icon-list']//li[2]//span"
    resend_req = "//button[normalize-space()='Re-send Request']"
    ver_col_dt_m = "//div[@class='right-table right-table-view']//table[1]//tbody//tr[15]//td"
    ver_col_dt_c = "//div[@class='right-table right-table-view']//table[2]//tbody//tr[15]//td"
    ver_col_dt_af = "//div[@class='right-table right-table-view']//table[3]//tbody//tr[15]//td"
    ver_s_type_m = "//table[@class='table ng-star-inserted'][1]//tbody//tr[5]//td"
    ver_s_type_c = "//table[@class='table ng-star-inserted'][2]//tbody//tr[5]//td"
    ver_s_type_af = "//table[@class='table ng-star-inserted'][3]//tbody//tr[5]//td"
    case_stat = "//button[@aria-label='Status']"
    alert_cancel = "alertcancel"
    KitBarcode_dropdown = "dropdownMenukitbarcode"
    addExtraKitBarCode = "newcasekitbarcodescan"
    pageViewCaseStatus = "//button[@id='casedetailscasestatusBtn']"
    status_filter_button = "casedetailscasestatusBtn"
    request_type = "//app-single-select[@label='id']//button[@type='button']//span[2]"
    request_type_list = "//div[@class='ngx-dropdown-list-container dropdown-search ng-star-inserted']//ul//li"
    NATA_immigration = "//app-single-select[@label='immigrationSubTypeName']//button[@type='button']"
    NATA_immigration_list = "//ul[@role='list']//li"
    county_involved = "//div[@class='row']//app-single-select[@uid='countryId']//button"
    NATA_affidavit_comments = "//textarea[@id='natacomments']"
    restricted_access = "//div[@class='restrict-box ng-star-inserted']//p"
    toogle_button = "//div[@class='menu-right']//div[@class='header'][2]//div[2]"
    select_referral_status = "//button[normalize-space()='Select Referral Status']"
    referral_status_list = "//div[@class='dropdown ng-star-inserted']//ul//li"
    help_status_icon = "casedetailshelpIcon"
    modified_status = "//div[@id='help-request']//div//span[@type='button']"
    ver_Msample_type = "//div[@class='right-table right-table-view']//table[1]//tbody//tr[5]//td"
    ver_Csample_type = "//div[@class='right-table right-table-view']//table[2]//tbody//tr[5]//td"
    ver_Afsample_type = "//div[@class='right-table right-table-view']//table[3]//tbody//tr[5]//td"
    ny_verification = "//div[@class='ny-watermark ng-star-inserted']"
    report_presence = "//a[@class='doc-link']"
    docc_view = "//ul[@class='menu-list']//li[7]"
    adv_search_coll_siteM = "//div[@class='right-table']//table[1]//tbody//tr[18]//td//div//div//" \
                            "a[normalize-space()='Advanced Search']"
    adv_search_coll_siteC = "//div[@class='right-table']//table[2]//tbody//tr[18]//td//div//div//" \
                            "a[normalize-space()='Advanced Search']"
    adv_search_coll_siteAF = "//div[@class='right-table']//table[3]//tbody//tr[18]//td//div//div//" \
                             "a[normalize-space()='Advanced Search']"
    collection_site_field = "//div[@class='row']//div[normalize-space()='Collection site']//input"
    zip_field = "//div[@class='row']//div[normalize-space()='Zip']//input"
    comments_field = "//div[@class='row']//div[normalize-space()='Comments']//textarea"
    exp_collection_siteID = "(//tr)[45]//td"
    exp_groupID = "//span[@class='ribbon2']//span"
    sampleIDAlredayExist = "//p[normalize-space()='Sample ID already exists in another Case.']"
    groupID = "//div[@class='header']//h1"
    getCaseID = "//*[@class='ribbon2']/span"
    doc_count = "//app-help-activities//div[2]//div[2]//div[@class='attach ng-star-inserted']"
    commonName_close = "testedparysearchcloseBtn"
    caseDetailIndicator = "casedetailsindicatorIcon"
    NY_enable = "//li[normalize-space()='NY']//div//input[@id='flexSwitchCheckChecked']"
    tables_count = "//div[@class='right-table']//table"
    title = "//caption[text()=' Listing ']/..//div[@class='d-flex align-items-center']"
    standardMail_text = "//span[normalize-space()='Standard Mail']"
    deliveryMode_text = "//ul[@class='delivery-box']//li//p//span"
    setUp_bt = "flexSwitchCheckChecked"
    onlineSetUp_email = "//input[@id='email']"
    onlineSetUp_password = "//input[@id='password']"
    securityQuestion_bt = "//button[@id='securityQuestion']"
    securityQuestion_li = "//app-online-setup-settings[@class='ng-star-inserted']//li[1]"
    securityAnswer = "//input[@id='securityAnswer']"
    onlineSetUp_confirm = "onlinesetupconfirmBtn"
    onlineSetup_verify = "//p[normalize-space()='Yes']"
    review_flag = "//app-case-details[@class='ng-star-inserted']//div[@class='case__content']" \
                  "//div[@class='ribbon ribbon-top-right review ng-star-inserted']//span"
    changeReviewStatus_checkbox = "//input[@id='changerequestStatus']"
    changeUpdate_bt = "caseeditconfirmBtn"
    changeCaseStatus_checkbox = "//input[@id='changecaseStatus']"
    changeStatus_bt = "//button[@id='changestatusTo']"
    changeStatus_li = "//app-single-select[@id='changestatusTo']//div[@class='ngx-dropdown-container']//ul//li"
    newCase_status = "//button[@id='casedetailscasestatusBtn']"
    deliveryByEmail = "//input[@id='mediumEmail']"
    deliveryByFax = "//input[@id='mediumFax']"
    testedPartyInfo_CloseBt = "//div[@class='modal-content']//button[@aria-label='Close']"
    copyFrom_child = "//tbody//tr[2]//td[2]//mat-select[@role='combobox']"
    copyFrom_af = "//tbody//tr[3]//td[2]//mat-select[@role='combobox']"
    tpName_c = "//tbody//tr[2]//td[3]"
    tpName_af = "//tbody//tr[3]//td[3]"
    childTitle = "//td[contains(text(),'Child')]"
    AFTitle = "//td[contains(text(),'Alleged Father')]"
    copyFrom_childlist = "//div[@role='listbox']//mat-option//span[contains(text(),'Child')]"
    copyFrom_AFlist = "//div[@role='listbox']//mat-option//span[contains(text(),'Alleged Father')]"
    newRole_list = "//tbody/tr[1][@class='ng-star-inserted']//td"
    allbarcode = "//div[1][@class='row g-3 view-section']//div[2]//p"
    valid_sampleID_already_existing_sample_id = "//*[@id='bodyModal']/app-root/app-toaster/div/div[2]/p"
    deliveryPrefEditBt = "//button[@id='deliverypreferenceformeditBtn']"
    onlineSetUp_disable_checkbox = "//input[@id='onlinePortal']"

    def toasterMessageClose(self):
        self.waitForElement(self.toaster_close)
        self.ElementClick(self.toaster_close)

    def caseIDForVerification(self):
        self.waitForElement(self.getCaseID, "xpath")
        caseID = self.isElementTextPresent(self.getCaseID, "xpath")
        print(caseID)
        return self.utiles.SplitgroupId(caseID)

    def commentAdd(self, comment):
        self.click_Comment()
        self.viewType()
        self.selectType()
        self.viewReason()
        self.selectReason()
        self.addText(comment)
        self.post_comm()
        addedcomm = self.getText()
        self.closeComment()
        return addedcomm

    def commentchk(self):
        self.click_Comment()
        self.webScroll(self.scroll_view_element(self.addedComment))
        txt = self.getText()
        # self.closeComment()
        return txt

    def click_Comment(self):
        self.waitForElement(self.commentClk)
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.commentClk)

    def viewType(self):
        self.waitForElement(self.typeDrop)
        self.ElementClick(self.typeDrop)

    def viewReason(self):
        self.waitForElement(self.reasonDrop)
        self.ElementClick(self.reasonDrop)

    def selectType(self):
        self.waitForElement(self.Noteselect)
        self.ElementClick(self.Noteselect)

    def selectReason(self):
        self.waitForElement(self.ReviewSelect)
        self.ElementClick(self.ReviewSelect)

    def addText(self, comment):
        self.waitForElement(self.textarea)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(comment, self.textarea)

    def post_comm(self):
        self.waitForElement(self.Post)
        self.ElementClick(self.Post)
        self.waitForElementPresent(self.submitLoader, locatorType="xpath")

    def getText(self):
        self.waitForElement(self.addedComment)
        addedCom = self.isElementTextPresent(self.addedComment, "xpath")
        return addedCom

    def closeComment(self):
        self.waitForElement(self.commentClose)
        self.waitForElementPresent(self.loader)
        # self.MoveandClick(self.commentClose, "xpath")
        self.ElementClick(self.commentClose)

    def click_help_tickets(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.help_ticket, locatorType="xpath")
        self.ElementClick(self.help_ticket, locatorType="xpath")

    def click_case_file(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.case_file, locatorType="id")
        self.ElementClick(self.case_file, locatorType="id")

    def verifyCaseFile(self):
        self.waitForElement(self.case_id, locatorType="id")
        result = self.isElementPresent(self.case_id, locatorType="id")
        return result

    def click_new_case(self):
        self.waitForElement(self.new_case, locatorType="id", timeout=100)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.new_case, locatorType="id")

    def verifyNewCase(self):
        self.waitForElement(self.channel, locatorType="xpath")
        result = self.isElementPresent(self.channel, locatorType="xpath")
        return result

    def click_channel(self):
        self.waitForElement(self.channel, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.channel, locatorType="xpath")
        time.sleep(1)

    def channel_selection(self, inp_channel, inp_s, inp_state, inp_acc, inp_auth, inp_agency, inp_barcode, inp_country,
                          inp_ref1, inp_ref2, inp_dins, inp_customer, inp_phone, inp_email, inp_c_relation):
        if inp_channel is not None:
            search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.channel_list)
            channel_sel = self.utiles.find_dropdown_select(search_list, inp_channel)
            if channel_sel is not False:
                channel_sel.click()
                self.waitForElementPresent(self.loader, locatorType="xpath")
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")
        if inp_channel == 'Government' or inp_channel == 'Media':
            self.channel_and_media(inp_s, inp_state, inp_acc, inp_auth, inp_agency)
        elif inp_channel == 'Corporate':
            self.corporate(inp_country, inp_acc, inp_ref1, inp_ref2)
        elif inp_channel == 'Retail':
            self.retail(inp_barcode, inp_dins, inp_customer, inp_phone, inp_email, inp_c_relation, inp_ref1, inp_ref2)

    def click_state(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.state, locatorType="xpath")
        self.ElementClick(self.state, locatorType="xpath")
        time.sleep(2)

    def send_search(self, inp_s):
        self.waitForElement(self.search)
        self.sendKeys(inp_s, self.search)
        time.sleep(3)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def state_selection(self, inp_state, inp_acc):
        if inp_state is not None:
            search_state_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.state_list)
            state_sel = self.utiles.find_dropdown_select(search_state_list, inp_state)
            if state_sel is not False:
                state_sel.click()
                self.waitForElementPresent(self.loader, locatorType="xpath")
                self.click_account()
                self.click_search()
                self.account_selection(inp_acc)
            else:
                self.log.info("input is False")

        else:
            self.log.info("Input is None")

    def click_account(self):
        self.waitForElement(self.account, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.account, locatorType="xpath")
        time.sleep(2)

    def account_selection(self, inp_acc):
        if inp_acc is not None:
            search_acc_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.acc_list)
            acc_sel = self.utiles.find_dropdown_select(search_acc_list, inp_acc)
            if acc_sel is not False:
                acc_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def send_auth_doc(self, inp_auth):
        if inp_auth is not None:
            self.waitForElement(self.auth_doc, locatorType="id")
            self.sendKeys(inp_auth, self.auth_doc, locatorType="id")
        else:
            pass

    def send_agency_case(self, inp_agency):
        if inp_agency is not None:
            self.waitForElement(self.agency_case, locatorType="id")
            self.sendKeys(inp_agency, self.agency_case, locatorType="id")
        else:
            pass

    def click_test_type(self):
        self.waitForElement(self.test_type, locatorType="xpath")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.test_type, locatorType="xpath")
        time.sleep(2)

    def test_type_selection(self, inp_test_type):
        if inp_test_type is not None:
            search_test_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.test_type_list)
            test_type_sel = self.utiles.find_dropdown_select(search_test_list, inp_test_type)
            if test_type_sel is not False:
                test_type_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_reconstruct_section(self):
        self.waitForElement(self.reconstruct_section, "xpath")
        self.ElementClick(self.reconstruct_section, locatorType="xpath")
        time.sleep(2)

    def reconstruct_selection(self, recon_section):
        if recon_section is not None:
            search_test_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.reconstruct_list)
            section_sel = self.utiles.find_dropdown_select(search_test_list, recon_section)
            if section_sel is not False:
                section_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_case_definition(self):
        self.waitForElement(self.case_definition)
        self.ElementClick(self.case_definition)
        time.sleep(2)

    def case_selection(self, inp_case_def):
        if inp_case_def is not None:
            search_case_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.case_def_list)
            case_sel = self.utiles.find_dropdown_select(search_case_list, inp_case_def)
            if case_sel is not False:
                case_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_add_testing(self):
        self.waitForElement(self.add_testing)
        self.ElementClick(self.add_testing)

    def add_testing_selection(self, inp_add_test):
        if inp_add_test is not None:
            search_add_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.add_test_list)
            add_test_sel = self.utiles.find_dropdown_select(search_add_list, inp_add_test)
            if add_test_sel is not False:
                add_test_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_type(self, inp_channel, inp_type):
        if inp_channel == 'Corporate' or inp_channel == 'DTC':
            self.waitForElement(self.type)
            self.webScroll(self.scroll_view_element(self.type, locatorType="xpath"))
            self.waitForElement(self.type)
            self.ElementClick(self.type)
            time.sleep(1)
            self.type_selection(inp_type)
        else:
            pass

    def type_selection(self, inp_type):
        if inp_type is not None:
            self.waitForElement(self.type_list)
            search_type_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.type_list)
            print(inp_type)
            type_sel = self.utiles.find_dropdown_select(search_type_list, inp_type)
            if type_sel is not False:
                type_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_turnaround(self):
        self.waitForElement(self.turn_around, "xpath")
        self.webScroll(self.scroll_view_element(self.turn_around, "xpath"))
        self.ElementClick(self.turn_around, "xpath")
        time.sleep(2)

    def click_edit_turn_around(self):
        self.waitForElement(self.edit_turn_around)
        self.webScroll(self.scroll_view_element(self.edit_turn_around, locatorType="xpath"))
        self.ElementClick(self.edit_turn_around)

    def turnaround_selection(self, inp_turnaround):
        if inp_turnaround is not None:
            search_turn_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.turnaround_list)
            turnaround_sel = self.utiles.find_dropdown_select(search_turn_list, inp_turnaround)
            if turnaround_sel is not False:
                turnaround_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_billing_type(self):
        self.waitForElement(self.billing_type, locatorType="id")
        self.ElementClick(self.billing_type, locatorType="id")

    def click_court_order(self):
        self.waitForElement(self.court_order, locatorType="id")
        self.ElementClick(self.court_order, locatorType="id")

    def click_language(self):
        self.waitForElement(self.language)
        self.ElementClick(self.language)

    def language_selection(self, inp_lang):
        if inp_lang is not None:
            search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.lang_list)
            sel_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.lang_sel)
            for lang in inp_lang:
                lang_sel = self.utiles.find_lang_select(search_list, sel_list, lang)
                lang_sel.click()
        else:
            self.log.info("Input is None")

    def click_affidavit_type(self):
        self.waitForElement(self.affidavit_type)
        self.ElementClick(self.affidavit_type)

    def affidavit_selection(self, inp_aff):
        if inp_aff is not None:
            search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.dropdown_list)
            aff_sel = self.utiles.find_dropdown_select(search_list, inp_aff)
            aff_sel.click()
        else:
            self.log.info("Input is None")

    def send_kit_barcode(self, inp_barcode):
        if inp_barcode is not None:
            self.waitForElement(self.barcode, "id")
            self.sendKeys(inp_barcode, self.barcode, "id")
            self.driver.find_element(By.ID, self.barcode).send_keys(Keys.ENTER)
        else:
            pass

    def send_ref1(self, inp_ref1):
        if inp_ref1 is not None:
            self.waitForElement(self.ref1, "id")
            self.sendKeys(inp_ref1, self.ref1, "id")
        else:
            pass

    def send_ref2(self, inp_ref2):
        if inp_ref2 is not None:
            self.waitForElement(self.ref2, "id")
            self.sendKeys(inp_ref2, self.ref2, "id")
        else:
            pass

    def click_country(self):
        self.webScroll(self.scroll_view_element(self.country, locatorType="xpath"))
        self.waitForElement(self.country)
        self.ElementClick(self.country)
        time.sleep(1)

    def click_search(self):
        self.waitForElement(self.search)
        self.ElementClick(self.search)

    def country_selection(self, inp_country, inp_acc):
        if inp_country is not None:
            search_country_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.country_list)
            country_sel = self.utiles.find_dropdown_select(search_country_list, inp_country)
            if country_sel is not False:
                country_sel.click()
            else:
                self.log.info("input is False")
            self.click_account()
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.click_search()
            self.account_selection(inp_acc)

    def send_dins(self, inp_dins):
        if inp_dins is not None:
            self.waitForElement(self.dins, "id")
            self.sendKeys(inp_dins, self.dins, "id")
        else:
            pass

    def send_customer(self, inp_customer):
        if inp_customer is not None:
            self.webScroll(self.scroll_view_element(self.customer, locatorType="id"))
            self.waitForElement(self.customer, locatorType="id")
            self.sendKeys(inp_customer, self.customer, locatorType="id")
        else:
            pass

    def send_cust_phone(self, inp_phone):
        if inp_phone is not None:
            self.waitForElement(self.c_phone, "id")
            self.sendKeys(inp_phone, self.c_phone, "id")
        else:
            pass

    def send_cust_email(self, inp_email):
        if inp_email is not None:
            self.waitForElement(self.c_email, "id")
            self.sendKeys(inp_email, self.c_email, "id")
        else:
            pass

    def click_cust_relation(self):
        self.waitForElement(self.c_relation, "id")
        self.webScroll(self.scroll_view_element(self.c_relation, locatorType="id"))
        self.waitForElement(self.c_relation, "id")
        self.ElementClick(self.c_relation, "id")

    def relation_selection(self, inp_c_relation):
        if inp_c_relation is not None:
            search_rel_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.rel_list)
            rel_sel = self.utiles.find_dropdown_select(search_rel_list, inp_c_relation)
            if rel_sel is not False:
                rel_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def channel_and_media(self, inp_s, inp_state, inp_acc, inp_auth, inp_agency):
        self.click_state()
        self.send_search(inp_s)
        self.state_selection(inp_state, inp_acc)
        self.send_auth_doc(inp_auth)
        self.send_agency_case(inp_agency)
        self.click_billing_type()
        self.click_court_order()

    def corporate(self, inp_country, inp_acc, inp_ref1, inp_ref2):
        time.sleep(2)
        self.click_country()
        self.click_search()
        time.sleep(2)
        self.country_selection(inp_country, inp_acc)
        self.send_ref1(inp_ref1)
        self.send_ref2(inp_ref2)

    def retail(self, inp_barcode, inp_dins, inp_customer, inp_phone, inp_email, inp_c_relation, inp_ref1, inp_ref2):
        self.send_kit_barcode(inp_barcode)
        self.send_dins(inp_dins)
        self.send_customer(inp_customer)
        self.send_cust_phone(inp_phone)
        self.send_cust_email(inp_email)
        # self.click_cust_relation()
        # self.relation_selection(inp_c_relation)
        self.send_ref1(inp_ref1)
        self.send_ref2(inp_ref2)

    def click_edit(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.edit_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.edit_bt, "id")
        self.click_alert_cancel_bt()

    def channel_sel(self, inp_ch):
        if inp_ch is not None:
            search_c_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.channel_list)
            c_sel = self.utiles.find_dropdown_select(search_c_list, inp_ch)
            if c_sel is not False:
                c_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_skip(self):
        self.waitForElement(self.skip, "id")
        self.ElementClick(self.skip, "id")

    def click_yes(self):
        button = self.isElementPresent(self.yes, "id")
        if button is not False:
            # self.waitForElement(self.yes, "id")
            self.ElementClick(self.yes, "id")
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            pass
        # time.sleep(1)

    def common(self, inp_test_type, recon_section, inp_case_def, inp_add_test, inp_channel, inp_type,
               online_setup, inp_turnaround):
        time.sleep(1)
        self.click_test_type()
        self.test_type_selection(inp_test_type)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if inp_test_type == "Reconstruct":
            self.click_reconstruct_section()
            self.reconstruct_selection(recon_section)
        else:
            pass
        self.click_case_definition()
        time.sleep(1)
        self.case_selection(inp_case_def)
        print("### Case definitions is :", inp_case_def)
        self.click_add_testing()
        self.add_testing_selection(inp_add_test)
        self.click_type(inp_channel, inp_type)
        self.type_selection(inp_type)
        time.sleep(2)
        if online_setup and inp_channel != "Government":
            self.MakeonlineSetup()
        else:
            print("Input channel is ", inp_channel)
        self.click_turnaround()
        self.turnaround_selection(inp_turnaround)

    def click_save(self):
        self.waitForElement(self.save, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.save, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        # time.sleep(2)

    def click_cancel(self):
        self.waitForElement(self.cancel, "id")
        self.ElementClick(self.cancel, "id")

    def getSample_id(self):
        s = self.utiles.unique_sample_ids()
        # return "M-" + s[0], "C-" + s[1], "AF-" + s[2]
        return "S-" + s[0], "S-" + s[1], "S-" + s[2], "S-" + s[3]

    def send_M_sample_id(self, count, m_id):
        sampleID = self.sample_id + str(count)
        if m_id is None:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.getSample_id()[0], sampleID, "id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            actual = self.verifytoaster_msg_success()
            self.utiles.hard_assertion("Success", actual, "sample id of mother is not entered")
        else:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.utiles.strip_WhiteSpace(m_id), sampleID, locatorType="id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            # actual = self.verifytoaster_msg_success()
            actual = self.verify_sample_is_valid()
            self.utiles.assertionTrue(actual, "Error occurs while entering the  Mother sample id " + m_id)

    def send_C_sample_id(self, count, c_id):
        sampleID = self.sample_id + str(count)
        if c_id is None:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.getSample_id()[1], sampleID, "id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            actual = self.verifytoaster_msg_success()
            self.utiles.hard_assertion("Success", actual, "sample id of mother is not entered")
        else:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.utiles.strip_WhiteSpace(c_id), sampleID, locatorType="id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            actual = self.verify_sample_is_valid()
            self.utiles.assertionTrue(actual, "Error occurs while entering the Child sample id " + c_id)

    def send_AF_sample_id(self, count, af_id):
        sampleID = self.sample_id + str(count)
        if af_id is None:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.getSample_id()[2], sampleID, "id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            actual = self.verifytoaster_msg_success()
            self.utiles.hard_assertion("Success", actual, "sample id of mother is not entered")
        else:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.utiles.strip_WhiteSpace(af_id), sampleID, locatorType="id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            actual = self.verify_sample_is_valid()
            self.utiles.assertionTrue(actual, "Error occurs while entering the AF sample id" + af_id)

    def send_FE_sample_id(self, count, af_id):
        sampleID = self.sample_id + str(count)
        if af_id is None:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.getSample_id()[3], sampleID, "id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            actual = self.verifytoaster_msg_success()
            self.utiles.hard_assertion("Success", actual, "sample id of mother is not entered")
        else:
            self.waitForElement(sampleID, "id")
            self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
            self.waitForElement(sampleID, "id")
            self.sendKeys(self.utiles.strip_WhiteSpace(af_id), sampleID, locatorType="id")
            self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
            actual = self.verify_sample_is_valid()
            self.utiles.assertionTrue(actual, "Error occurs while entering the AF sample id" + af_id)

    def click_M_sample_dt(self, count, m_sample_dt):
        ele = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[2]//td//button"
        if m_sample_dt is not None:
            self.waitForElement(ele, locatorType="xpath")
            self.webScroll(self.scroll_view_element(ele, locatorType="xpath"))
            self.waitForElement(ele, locatorType="xpath")
            self.select_date_from_calender(m_sample_dt, ele, locatorType="xpath")
        else:
            pass

    def click_C_sample_dt(self, count, c_sample_dt):
        ele = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[2]//td//button"
        if c_sample_dt is not None:
            self.waitForElement(ele, locatorType="xpath")
            self.webScroll(self.scroll_view_element(ele, locatorType="xpath"))
            self.waitForElement(ele, locatorType="xpath")
            self.select_date_from_calender(c_sample_dt, ele, locatorType="xpath")
        else:
            pass

    def click_AF_sample_dt(self, count, af_sample_dt):
        ele = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[2]//td//button"
        if af_sample_dt is not None:
            self.waitForElement(ele, locatorType="xpath")
            self.webScroll(self.scroll_view_element(ele, locatorType="xpath"))
            self.waitForElement(ele, locatorType="xpath")
            self.select_date_from_calender(af_sample_dt, ele, locatorType="xpath")
        else:
            pass

    def send_mother_firstname(self, count, m_firstname):
        FName = self.firstname + str(count)
        if m_firstname is not None:
            self.waitForElement(FName, "id")
            self.webScroll(self.scroll_view_element(FName, locatorType="id"))
            self.waitForElement(FName, locatorType="id")
            self.sendKeys(m_firstname, FName, locatorType="id")
            self.commonTab_close()
        else:
            pass

    def send_child_firstname(self, count, c_firstname):
        CName = self.firstname + str(count)
        if c_firstname is not None:
            self.waitForElement(CName, "id")
            self.webScroll(self.scroll_view_element(CName, locatorType="id"))
            self.waitForElement(CName, locatorType="id")
            self.sendKeys(c_firstname, CName, locatorType="id")
            self.commonTab_close()
        else:
            pass

    def send_Af_firstname(self, count, af_firstname):
        FName = self.firstname + str(count)
        if af_firstname is not None:
            self.waitForElement(FName, "id")
            self.webScroll(self.scroll_view_element(FName, locatorType="id"))
            self.waitForElement(FName, locatorType="id")
            self.sendKeys(af_firstname, FName, locatorType="id")
            self.commonTab_close()
        else:
            pass

    def send_mother_lastname(self, count, m_lastname):
        lastname = self.lastname + str(count)
        if m_lastname is not None:
            self.waitForElement(lastname, "id")
            self.webScroll(self.scroll_view_element(lastname, locatorType="id"))
            self.waitForElement(lastname, locatorType="id")
            self.sendKeys(m_lastname, lastname, locatorType="id")
            self.commonTab_close()
        else:
            pass

    def send_child_lastname(self, count, c_lastname):
        lastname = self.lastname + str(count)
        if c_lastname is not None:
            self.waitForElement(lastname, "id")
            self.webScroll(self.scroll_view_element(lastname, locatorType="id"))
            self.waitForElement(lastname, locatorType="id")
            self.sendKeys(c_lastname, lastname, locatorType="id")
            self.commonTab_close()
        else:
            pass

    def send_Af_lastname(self, count, af_lastname):
        lastname = self.lastname + str(count)
        if af_lastname is not None:
            self.waitForElement(lastname, "id")
            self.webScroll(self.scroll_view_element(lastname, locatorType="id"))
            self.waitForElement(lastname, locatorType="id")
            self.sendKeys(af_lastname, lastname, locatorType="id")
            self.commonTab_close()
        else:
            pass

    def click_m_dob(self, count, m_dob):
        dob = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[11]//td//button"
        if m_dob is not None:
            self.waitForElement(dob)
            self.webScroll(self.scroll_view_element(dob, locatorType="xpath"))
            self.waitForElement(self.dob_m)
            self.select_date_from_calender(m_dob, dob, locatorType="xpath")
            self.commonTab_close()
        else:
            pass

    def click_c_dob(self, count, c_dob):
        dob = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[11]//td//button"
        if c_dob is not None:
            self.waitForElement(dob)
            self.webScroll(self.scroll_view_element(dob, locatorType="xpath"))
            self.waitForElement(self.dob_m)
            self.select_date_from_calender(c_dob, dob, locatorType="xpath")
            self.commonTab_close()
        else:
            pass

    def click_af_dob(self, count, af_dob):
        dob = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[11]//td//button"
        if af_dob is not None:
            self.waitForElement(dob)
            self.webScroll(self.scroll_view_element(dob, locatorType="xpath"))
            self.waitForElement(self.dob_m)
            self.select_date_from_calender(af_dob, dob, locatorType="xpath")
            self.commonTab_close()
        else:
            pass

    def race_m_sel(self, count, inp_race_m):
        race_list = "//div[@class='right-table']//table[" + str(
            count + 1) + "]//tbody//tr[13]//td//app-single-select//ul//li//a"
        if inp_race_m is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=race_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_race_m)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def Samptype_m_sel(self, inp_samp_m):
        if inp_samp_m is not None:
            search_sampTP_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.sample_type_list)
            samp_sel = self.utiles.find_dropdown_select(search_sampTP_list, inp_samp_m)
            if samp_sel is not False:
                samp_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def Samptype_c_sel(self, inp_samp_c):
        if inp_samp_c is not None:
            search_sampTP_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.sample_type_list)
            samp_sel = self.utiles.find_dropdown_select(search_sampTP_list, inp_samp_c)
            if samp_sel is not False:
                samp_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def Samptype_af_sel(self, inp_samp_af):
        if inp_samp_af is not None:
            search_sampTP_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.sample_type_list)
            samp_sel = self.utiles.find_dropdown_select(search_sampTP_list, inp_samp_af)
            if samp_sel is not False:
                samp_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def click_m_race(self, count, inp_race_m):
        if inp_race_m is not None:
            race = self.common_race + str(count)
            self.waitForElement(race, "id")
            self.webScroll(self.scroll_view_element(race, locatorType="id"))
            self.waitForElement(race, "id")
            self.ElementClick(race, "id")
            self.race_m_sel(count, inp_race_m)
        else:
            self.log.info("input is none")

    def click_m_samp_type(self, inp_samp_m):
        self.waitForElement(self.M_sample_type, "id")
        self.webScroll(self.scroll_view_element(self.M_sample_type, locatorType="id"))
        self.waitForElement(self.M_sample_type, "id")
        self.ElementClick(self.M_sample_type, "id")
        self.Samptype_m_sel(inp_samp_m)

    def click_af_samp_type(self, inp_samp_af):
        self.waitForElement(self.AF_sample_type, "id")
        self.webScroll(self.scroll_view_element(self.AF_sample_type, locatorType="id"))
        self.waitForElement(self.AF_sample_type, "id")
        self.ElementClick(self.AF_sample_type, "id")
        self.Samptype_m_sel(inp_samp_af)

    def click_c_samp_type(self, inp_samp_c):
        self.waitForElement(self.C_sample_type, "id")
        self.webScroll(self.scroll_view_element(self.C_sample_type, locatorType="id"))
        self.waitForElement(self.C_sample_type, "id")
        self.ElementClick(self.C_sample_type, "id")
        self.Samptype_m_sel(inp_samp_c)

    def samp_type_sel_M(self, count, inp_samp_m):
        # sampletype = self.sampleType + str(count)
        sample_type_sel = "(//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[4]//button)[2]"
        self.waitForElement(sample_type_sel)
        self.webScroll(self.scroll_view_element(sample_type_sel, locatorType="xpath"))
        self.waitForElement(sample_type_sel)
        self.ElementClick(sample_type_sel)
        self.Samptype_m_sel(inp_samp_m)

    def samp_type_sel_Af(self, count, inp_samp_af):
        sample_type_sel = "(//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[4]//button)[2]"
        self.waitForElement(sample_type_sel)
        self.webScroll(self.scroll_view_element(sample_type_sel, locatorType="xpath"))
        self.waitForElement(sample_type_sel)
        self.ElementClick(sample_type_sel)
        self.Samptype_m_sel(inp_samp_af)

    def samp_type_sel_C(self, count, inp_samp_c):
        sample_type_sel = "(//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[4]//button)[2]"
        self.waitForElement(sample_type_sel)
        self.webScroll(self.scroll_view_element(sample_type_sel, locatorType="xpath"))
        self.waitForElement(sample_type_sel)
        self.ElementClick(sample_type_sel)
        self.Samptype_m_sel(inp_samp_c)

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

    def click_c_race(self, count, inp_race_c):
        race = self.common_race + str(count)
        if inp_race_c is not None:
            self.waitForElement(race, "id")
            self.webScroll(self.scroll_view_element(race, locatorType="id"))
            self.waitForElement(race, "id")
            self.ElementClick(race, "id")
            self.race_c_sel(inp_race_c)
        else:
            pass

    def race_af_sel(self, count, inp_race_af):
        raceList = "//div[@class='right-table']//table[" + \
                   str(count + 1) + "]//tbody//tr[13]//td//app-single-select//ul//li//a"
        if inp_race_af is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=raceList)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_race_af)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def click_af_race(self, count, inp_race_af):
        race = self.common_race + str(count)
        if inp_race_af is not None:
            self.waitForElement(race, "id")
            self.webScroll(self.scroll_view_element(race, locatorType="id"))
            self.waitForElement(race, "id")
            self.ElementClick(race, "id")
            self.race_af_sel(count, inp_race_af)
        else:
            pass

    def retail_race_m_sel(self, count, inp_ret_race_m):
        retail_race_list = "//div[@class='right-table']//table[" + str(
            count + 1) + "]//tbody//tr[11]//td//app-single-select//ul//li//a"
        if inp_ret_race_m is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=retail_race_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_ret_race_m)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def click_retail_m_race(self, count, inp_ret_race_m):
        race = self.common_race + str(count)
        if inp_ret_race_m is not False:
            self.waitForElement(race, "id")
            self.webScroll(self.scroll_view_element(race, locatorType="id"))
            self.waitForElement(race, "id")
            self.ElementClick(race, "id")
            self.retail_race_m_sel(count, inp_ret_race_m)
        else:
            self.log.info("input is none")

    def retail_race_af_sel(self, count, inp_ret_race_af):
        retail_race_list = "//div[@class='right-table']//table[" + str(
            count + 1) + "]//tbody//tr[11]//td//app-single-select//ul//li//a"
        if inp_ret_race_af is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=retail_race_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_ret_race_af)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def click_retail_af_race(self, count, inp_ret_race_af):
        race = self.common_race + str(count)
        races = self.getElement(race, "id")
        if races.is_enabled() is not None:
            if inp_ret_race_af is not False:
                self.waitForElement(race, "id")
                self.webScroll(self.scroll_view_element(race, locatorType="id"))
                self.waitForElement(race, "id")
                self.ElementClick(race, "id")
                self.retail_race_m_sel(count, inp_ret_race_af)
            else:
                self.log.info("input is none")
        else:
            print("element disabled")
            pass

    def click_retail_m_dob(self, count, retail_m_dob):
        retail_dob = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[10]//td//button"
        if retail_m_dob is not None:
            self.waitForElement(retail_dob)
            self.webScroll(self.scroll_view_element(retail_dob, locatorType="xpath"))
            self.waitForElement(retail_dob)
            self.select_date_from_calender(retail_m_dob, retail_dob, locatorType="xpath")
        else:
            pass

    def click_retail_c_dob(self, count, retail_c_dob):
        retail_dob = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[10]//td//button"
        if retail_c_dob is not None:
            self.waitForElement(retail_dob)
            self.webScroll(self.scroll_view_element(retail_dob, locatorType="xpath"))
            self.waitForElement(retail_dob)
            self.select_date_from_calender(retail_c_dob, retail_dob, locatorType="xpath")
        else:
            pass

    def click_retail_af_dob(self, count, retail_af_dob):
        retail_dob = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[10]//td//button"
        if retail_af_dob is not None:
            self.waitForElement(retail_dob)
            self.webScroll(self.scroll_view_element(retail_dob, locatorType="xpath"))
            self.waitForElement(retail_dob)
            self.select_date_from_calender(retail_af_dob, retail_dob, locatorType="xpath")
        else:
            pass

    def click_m_col_date(self, count, m_cdt):
        col_date = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[14]//td//button"
        if m_cdt is not None:
            self.waitForElement(col_date)
            self.webScroll(self.scroll_view_element(col_date, locatorType="xpath"))
            self.waitForElement(col_date)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(m_cdt, col_date, locatorType="xpath")
        else:
            pass

    def click_c_col_date(self, count, c_cdt):
        col_date = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[14]//td//button"
        if c_cdt is not None:
            self.waitForElement(col_date)
            self.webScroll(self.scroll_view_element(col_date, locatorType="xpath"))
            self.waitForElement(col_date)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(c_cdt, col_date, locatorType="xpath")
        else:
            pass

    def click_af_col_date(self, count, af_cdt):
        col_date = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[14]//td//button"
        if af_cdt is not None:
            self.waitForElement(col_date)
            self.webScroll(self.scroll_view_element(col_date, locatorType="xpath"))
            self.waitForElement(col_date)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(af_cdt, col_date, locatorType="xpath")
        else:
            pass

    def click_retail_m_col_date(self, count, retail_m_cdt):
        retail_m = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[12]//td//button"
        if retail_m_cdt is not None:
            self.waitForElement(retail_m)
            self.webScroll(self.scroll_view_element(retail_m, locatorType="xpath"))
            self.waitForElement(retail_m)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(retail_m_cdt, retail_m, locatorType="xpath")
        else:
            pass

    def click_retail_c_col_date(self, count, retail_c_cdt):
        retail_c = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[12]//td//button"
        if retail_c_cdt is not None:
            self.waitForElement(retail_c)
            self.webScroll(self.scroll_view_element(retail_c, locatorType="xpath"))
            self.waitForElement(retail_c)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(retail_c_cdt, retail_c, locatorType="xpath")
        else:
            pass

    def click_retail_af_col_date(self, count, retail_af_cdt):
        retail_af = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[12]//td//button"
        if retail_af_cdt is not None:
            self.waitForElement(retail_af)
            self.webScroll(self.scroll_view_element(retail_af, locatorType="xpath"))
            self.waitForElement(retail_af)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(retail_af_cdt, retail_af, locatorType="xpath")
        else:
            pass

    def send_m_tracking(self, count, inp_m_tracking):
        tracking_id = self.tracking + str(count)
        if inp_m_tracking is not None:
            self.waitForElement(tracking_id, "id")
            self.webScroll(self.scroll_view_element(tracking_id, locatorType="id"))
            self.waitForElement(tracking_id, "id")
            self.sendKeys(inp_m_tracking, tracking_id, "id")
            self.driver.find_element(By.ID, tracking_id).send_keys(Keys.ENTER)
        else:
            pass

    def send_c_tracking(self, count, inp_c_tracking):
        tracking_id = self.tracking + str(count)
        if inp_c_tracking is not None:
            self.waitForElement(tracking_id, "id")
            self.webScroll(self.scroll_view_element(tracking_id, locatorType="id"))
            self.waitForElement(tracking_id, "id")
            self.sendKeys(inp_c_tracking, tracking_id, "id")
            self.driver.find_element(By.ID, tracking_id).send_keys(Keys.ENTER)
        else:
            pass

    def send_af_tracking(self, count, inp_af_tracking):
        tracking_id = self.tracking + str(count)
        if inp_af_tracking is not None:
            self.waitForElement(tracking_id, "id")
            self.webScroll(self.scroll_view_element(tracking_id, locatorType="id"))
            self.waitForElement(tracking_id, "id")
            self.sendKeys(inp_af_tracking, tracking_id, "id")
            self.driver.find_element(By.ID, tracking_id).send_keys(Keys.ENTER)
        else:
            pass

    def send_retail_m_tracking(self, count, retail_m_tracking):
        retail_tra_m = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[12]//td//input"
        if retail_m_tracking is not None:
            self.waitForElement(retail_tra_m)
            self.webScroll(self.scroll_view_element(retail_tra_m, locatorType="xpath"))
            self.waitForElement(retail_tra_m)
            self.sendKeys(retail_m_tracking, retail_tra_m)
            self.driver.find_element(By.XPATH, retail_tra_m).send_keys(Keys.ENTER)
        else:
            pass

    def send_retail_c_tracking(self, count, retail_c_tracking):
        retail_tra_c = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[12]//td//input"
        if retail_c_tracking is not None:
            self.waitForElement(retail_tra_c)
            self.webScroll(self.scroll_view_element(retail_tra_c, locatorType="xpath"))
            self.waitForElement(retail_tra_c)
            self.sendKeys(retail_c_tracking, retail_tra_c)
            self.driver.find_element(By.XPATH, retail_tra_c).send_keys(Keys.ENTER)
        else:
            pass

    def send_retail_af_tracking(self, count, retail_af_tracking):
        retail_tra_af = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[12]//td//input"
        if retail_af_tracking is not None:
            self.waitForElement(retail_tra_af)
            self.webScroll(self.scroll_view_element(retail_tra_af, locatorType="xpath"))
            self.waitForElement(retail_tra_af)
            self.sendKeys(retail_af_tracking, retail_tra_af)
            self.driver.find_element(By.XPATH, retail_tra_af).send_keys(Keys.ENTER)
        else:
            pass

    def enter_m(self, count, inp_channel, m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt,
                retail_m_tracking):
        if inp_channel == 'Government' or inp_channel == 'Corporate' or inp_channel == 'Media':
            self.click_m_dob(count, m_dob)
            self.click_m_race(count, m_race)
            self.click_m_col_date(count, m_cdt)
            self.send_m_tracking(count, inp_m_tracking)
        elif inp_channel == 'Retail':
            self.click_retail_m_dob(count, retail_m_dob)
            self.click_retail_m_race(count, m_ret_race)
            # self.click_retail_m_col_date(count, retail_m_cdt)
            self.send_retail_m_tracking(count, retail_m_tracking)

    def enter_c(self, count, inp_channel, c_dob, c_race, c_cdt, inp_c_tracking, retail_c_dob, retail_c_cdt,
                retail_c_tracking):
        if inp_channel == 'Government' or inp_channel == 'Corporate' or inp_channel == 'Media':
            self.click_c_dob(count, c_dob)
            self.click_c_race(count, c_race)
            self.click_c_col_date(count, c_cdt)
            self.send_c_tracking(count, inp_c_tracking)
        elif inp_channel == 'Retail':
            self.click_retail_c_dob(count, retail_c_dob)
            # self.click_retail_c_col_date(count, retail_c_cdt)
            self.send_retail_c_tracking(count, retail_c_tracking)

    def enter_af(self, count, inp_channel, af_dob, af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob,
                 retail_af_cdt,
                 retail_af_tracking):
        if inp_channel == 'Government' or inp_channel == 'Corporate' or inp_channel == 'Media':
            self.click_af_dob(count, af_dob)
            self.click_af_race(count, af_race)
            self.click_af_col_date(count, af_cdt)
            self.send_af_tracking(count, inp_af_tracking)
        elif inp_channel == 'Retail':
            self.click_retail_af_dob(count, retail_af_dob)
            self.click_retail_af_race(count, af_ret_race)
            # self.click_retail_af_col_date(count, retail_af_cdt)
            self.send_retail_af_tracking(count, retail_af_tracking)

    def verifytoaster_msg_success(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.success_msgg)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_pre = self.isElementTextPresent(self.success_msgg, locatorType="xpath")
        # time.sleep(2)
        toaster_presence = self.isElementPresent(self.toaster_close, locatorType="xpath")
        if toaster_presence is not False:
            self.toasterMessageClose()
        else:
            pass
        return ele_pre

    def Report_Lang_Add(self, Langs):
        self.click_language()
        self.language_selection(Langs)
        self.click_language()

    def verifyCaseCreated(self):
        result = self.isElementPresent(self.created, locatorType="xpath")
        return result

    def expectedId(self):
        Id = self.isElementTextPresent(self.case, locatorType="xpath")
        caseId = self.utiles.strip_string(Id)
        return caseId

    def click_doc(self):
        self.waitForElement(self.doc, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.doc, "id")

    def Re_click_doc(self):
        self.waitForElement(self.doc, "id")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.doc, "id")

    def verify_doc_click(self):
        self.waitForElement(self.add, "id")
        ele = self.isElementPresent(self.add, "id")
        return ele

    def click_add(self):
        self.waitForElement(self.add, "id")
        self.ElementClick(self.add, "id")

    def click_scan_close(self):
        self.waitForElement(self.scan_close)
        if self.scan_close is not False:
            self.ElementClick(self.scan_close)
        else:
            pass

    def click_document(self):
        self.waitForElement(self.document)
        self.ElementClick(self.document)

    def document_selection(self):
        self.waitForElement(self.doc_list)
        document_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.doc_list)
        if document_list is not False:
            document_list[0].click()
        else:
            self.log.info("input is False")

    def click_tested_party(self):
        self.waitForElement(self.tested_party)
        self.ElementClick(self.tested_party)

    def tested_party_selection(self):
        self.waitForElement(self.party_list)
        t_party_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.party_list)
        for ele in t_party_list:
            if ele is not False:
                ele.click()
            else:
                self.log.error("party_sel is none")

    def tested_party_selection_for_MandC(self):
        self.waitForElement(self.party_list)
        t_party_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.party_list)
        if t_party_list is not False:
            t_party_list[0].click()
            t_party_list[1].click()
        else:
            self.log.error("party_sel is none")

    def send_comments(self, inp_comment):
        self.waitForElement(self.comment, "id")
        self.ElementClick(self.comment, "id")
        self.sendKeys(inp_comment, self.comment, locatorType="id")

    def click_browse_files(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        uploadElement = self.getElement(self.browse, locatorType="xpath")
        path = "test_data/"
        browse_files = os.path.join(ROOT_DIR, path, "report.pdf")
        uploadElement.send_keys(browse_files)
        # time.sleep(20)

    def click_upload(self):
        self.waitForElement(self.upload, locatorType="id")
        button_enable = self.getElement(self.upload, locatorType="id")
        if button_enable.is_enabled():
            # self.waitForElement(self.upload)
            self.ElementClick(self.upload, "id")
            time.sleep(2)
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            self.log.info("button is not present")

    def click_add_new_doc(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.add_new_doc, "id")
        self.ElementClick(self.add_new_doc, "id")

    def click_addNew_collectorName(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.add_new_collectorName_bt, "id")
        self.ElementClick(self.add_new_collectorName_bt, "id")

    def click_add_new_collName(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.add_new_collsite_bt, "id")
        self.ElementClick(self.add_new_collsite_bt, "id")

    # def image_doc_selection(self):
    #     self.waitForElement(self.doc_list)s
    #     document_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.doc_list)
    #     if document_list is not False:
    #         document_list[3].click()
    #     else:
    #         self.log.info("input is False")

    # def click_browse_files_for_img(self):
    #     self.waitForElementPresent(self.loader, locatorType="xpath")
    #     uploadElement = self.getElement(self.browse, locatorType="xpath")
    #     path = "test_data/"
    #     browse_files = os.path.join(ROOT_DIR, path, "Capture.PNG")
    #     uploadElement.send_keys(browse_files)
    #     time.sleep(20)

    # def AddImage(self, inp_comment):
    #     self.click_document()
    #     self.image_doc_selection()
    #     self.click_tested_party()
    #     self.tested_party_selection()
    #     self.send_comments(inp_comment)
    #     self.click_browse_files_for_img()

    def click_close(self):
        self.waitForElement(self.close, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.close, "id")
        # time.sleep(2)
        # self.toasterMessageClose()

    def AddDocument(self, inp_comment):
        self.click_doc()
        verify = self.verify_doc_click()
        self.utiles.assertionTrue(verify, "failed to perform the click action - doc ")
        self.click_add()
        self.click_scan_close()
        self.click_document()
        self.document_selection()
        self.click_browse_files()
        self.click_tested_party()
        self.tested_party_selection()
        self.send_comments(inp_comment)
        self.click_upload()

    def click_add_new(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        time.sleep(10)
        self.waitForElement(self.add_new_doc)
        self.ElementClick(self.add_new_doc)

    def image_doc_selection(self, channel=None):
        self.waitForElement(self.doc_list)
        document_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.doc_list)
        if document_list is not False:
            if channel == "Government":
                document_list[0].click()
            else:
                document_list[3].click()
        else:
            self.log.info("input is False")

    def click_browse_files_for_img(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        uploadElement = self.getElement(self.browse, locatorType="xpath")
        path = "test_data/"
        browse_files = os.path.join(ROOT_DIR, path, "Capture.PNG")
        uploadElement.send_keys(browse_files)
        time.sleep(3)

    def AddImage(self, inp_comment):
        # self.click_add_new()
        self.click_add_new_doc()
        self.click_document()
        self.image_doc_selection()
        self.click_browse_files_for_img()
        self.click_tested_party()
        self.tested_party_selection()
        self.send_comments(inp_comment)
        self.click_upload()

    def click_accession(self):
        self.waitForElement(self.accession, "id")
        self.webScroll(self.scroll_view_element(self.accession, "id"))
        self.ElementClick(self.accession, "id")
        # time.sleep(10)

    def click_test_samples(self):
        self.waitForElement(self.test_samples, "id")
        self.ElementClick(self.test_samples, "id")
        # time.sleep(10)

    def verifyFileUpload(self):
        file_data = self.isElementPresent(self.file, locatorType="xpath")
        return file_data

    def getCaseId(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.c_id, locatorType="xpath", timeout=400)
        e_id = self.isElementTextPresent(self.c_id, locatorType="xpath")
        print(e_id)
        e_c_id = self.utiles.strip_string(e_id)
        time.sleep(3)
        print(e_c_id)
        return e_c_id

    def send_case_id(self, inp_c_id):
        self.waitForElement(self.case_id, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.sendKeys(inp_c_id, self.case_id, locatorType="id")

    def click_case_search(self):
        self.waitForElement(self.case_search, "id")
        self.ElementClick(self.case_search, "id")

    def verifyCaseStatus(self, inp_c_id):
        # self.waitForElementPresent(self.loader, "xpath")
        self.click_case_file()
        self.click_clear_button()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        group = self.caseIDForVerification()
        self.click_table_view()
        self.waitForElementPresent(self.loader, "xpath")
        status_text = self.isElementTextPresent(self.case_status, locatorType="xpath")
        return status_text, group

    def verifyCaseStat(self):
        status_text = self.isElementTextPresent(self.case_stat, locatorType="xpath")
        return status_text

    def click_table_view(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.table_view)
        self.ElementClick(self.table_view)

    def click_start(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.start_button, "id")
        self.ElementClick(self.start_button, "id")
        time.sleep(2)

    def click_start_yes(self):
        self.waitForElement(self.start_yes, "id")
        self.ElementClick(self.start_yes, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        time.sleep(3)

    def verify_case_from_gov_portal(self, inp_c_id):
        self.click_case_file()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()
        self.click_start()
        self.click_start_yes()
        time.sleep(2)
        status_result = self.isElementTextPresent(self.case_status, locatorType="xpath")
        return status_result

    def click_submissions(self):
        self.waitForElement(self.submission, "id")
        self.ElementClick(self.submission, "id")

    def verifySubmissions(self):
        self.waitForElement(self.anc_r_id, locatorType="id")
        result = self.isElementPresent(self.anc_r_id, locatorType="id")
        return result

    def send_req_id(self, inp_r_id):
        self.waitForElement(self.anc_r_id, locatorType="id")
        self.sendKeys(inp_r_id, self.anc_r_id, locatorType="id")

    def click_complete_req(self):
        self.waitForElement(self.comp_req, locatorType="id")
        self.webScroll(self.scroll_view_element(self.comp_req, locatorType="id"))
        self.ElementClick(self.comp_req, locatorType="id")

    def click_search_button(self):
        self.waitForElement(self.search_button, "id")
        self.webScroll(self.scroll_view_element(self.search_button, locatorType="xpath"))
        self.ElementClick(self.search_button, "id")

    def click_submission_search(self):
        self.waitForElement(self.submission_search, "id")
        self.webScroll(self.scroll_view_element(self.submission_search, locatorType="id"))
        self.ElementClick(self.submission_search, "id")

    def click_clear_button(self):
        self.waitForElement(self.clear, "id")
        self.webScroll(self.scroll_view_element(self.clear, locatorType="id"))
        self.ElementClick(self.clear, "id")

    def click_plus_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.plus_button)
        self.ElementClick(self.plus_button)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def VerifyRequestId(self, inp_r_id):
        self.send_req_id(inp_r_id)
        self.click_complete_req()
        self.click_submission_search()
        time.sleep(2)
        self.click_plus_button()
        ver_req = self.isElementTextPresent(self.req_id_tab, locatorType="id")
        time.sleep(2)
        return ver_req

    def click_sub_close(self):
        self.waitForElement(self.sub_close)
        self.ElementClick(self.sub_close)
        time.sleep(2)

    def click_submission_col(self):
        self.waitForElement(self.submission_col)
        self.ElementClick(self.submission_col)

    def save_first_case(self, inp_turnaround):
        self.webScroll(self.scroll_view_element(self.M_sample_id, locatorType="id"))
        self.waitForElement(self.drag_ele)
        s = self.getElement(self.drag_ele, locatorType="xpath")
        self.waitForElement(self.M_firstname, "id")
        d = self.getElement(self.M_firstname, locatorType="id")
        self.driver.execute_script(self.utiles.open_script(), s, d)
        self.click_turnaround()
        self.turnaround_selection(inp_turnaround)
        self.click_save()
        time.sleep(2)
        ver_status = self.isElementTextPresent(self.case_status, locatorType="xpath")
        return ver_status

    def save_second_case(self, inp_turnaround):
        self.click_case_file()
        self.click_submissions()
        self.click_plus_button()
        self.webScroll(self.scroll_view_element(self.M_sample_id, locatorType="id"))
        self.waitForElement(self.drag_ele2)
        s = self.getElement(self.drag_ele2, locatorType="xpath")
        self.waitForElement(self.M_firstname, "id")
        d = self.getElement(self.M_firstname, locatorType="id")
        self.driver.execute_script(self.utiles.open_script(), s, d)
        self.click_turnaround()
        self.turnaround_selection(inp_turnaround)
        self.click_save()
        time.sleep(2)
        ver_status = self.isElementTextPresent(self.case_status, locatorType="xpath")
        print(ver_status)
        return ver_status

    def click_edit_button(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.edit_bt, "id")
        self.ElementClick(self.edit_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def get_gov_case(self, inp_c_id):
        self.click_case_file()
        self.click_clear_button()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()
        self.click_start()
        self.click_start_yes()

    def click_m__edit_last_name(self, m_e_last_name):
        if m_e_last_name is not None:
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.waitForElement(self.M_lnameEdited)
            self.webScroll(self.scroll_view_element(self.M_lnameEdited, locatorType="xpath"))
            self.waitForElement(self.M_lnameEdited)
            self.sendKeys(m_e_last_name, self.M_lnameEdited, locatorType="xpath")
        else:
            pass

    def click_m_edit_ssn(self, m_e_ssn):
        if m_e_ssn is not None:
            self.waitForElement(self.m_ssn_ed)
            self.webScroll(self.scroll_view_element(self.m_ssn_ed, locatorType="xpath"))
            self.waitForElement(self.m_ssn_ed)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.sendKeys(m_e_ssn, self.m_ssn_ed, locatorType="xpath")
        else:
            pass

    def click_c__edit_last_name(self, c_e_last_name):
        if c_e_last_name is not None:
            self.waitForElement(self.C_lnameEdited)
            self.webScroll(self.scroll_view_element(self.C_lnameEdited, locatorType="xpath"))
            self.waitForElement(self.C_lnameEdited)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.sendKeys(c_e_last_name, self.C_lnameEdited, locatorType="xpath")
        else:
            pass

    def edit_case(self, inp_turn_around, m_e_last_name, m_e_ssn, c_e_last_name, af_e_last_name):
        self.click_edit_button()
        time.sleep(2)
        self.click_edit_turn_around()
        self.turnaround_selection(inp_turn_around)
        self.click_m__edit_last_name(m_e_last_name)
        self.click_m_edit_ssn(m_e_ssn)
        self.click_c__edit_last_name(c_e_last_name)
        self.click_af__edit_last_name(af_e_last_name)

    def getSSN(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.ver_samp_ed)
        self.webScroll(self.scroll_view_element(self.ver_samp_ed, locatorType="xpath"))
        ver_s = self.isElementTextPresent(self.ver_samp_ed, locatorType="xpath")
        return ver_s

    def verify_red_flag_id(self):
        ver_rf = self.isElementTextPresent(self.rf_req, locatorType="xpath")
        return ver_rf

    def click_hammer_icon(self):
        self.waitForElement(self.hammer)
        self.ElementClick(self.hammer, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_checkbox(self):
        self.waitForElement(self.flag_checkbox, locatorType="id")
        self.ElementClick(self.flag_checkbox, locatorType="id")

    def click_acknowledge(self):
        self.waitForElement(self.acknowledge)
        self.ElementClick(self.acknowledge)

    def verifyAcknowledge(self):
        self.waitForElement(self.green_flag, locatorType="xpath")
        result = self.isElementPresent(self.green_flag, locatorType="xpath")
        return result

    def acknowledge_red_flag(self, inp_r_id):
        self.send_req_id(inp_r_id)
        self.click_search_button()
        self.click_hammer_icon()
        time.sleep(2)
        self.click_checkbox()
        self.click_acknowledge()

    def click_confirm(self):
        self.waitForElement(self.confirm_bt, "id")
        self.ElementClick(self.confirm_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        # self.webScroll(self.scroll_view_element(self.exp_caseId, locatorType="xpath"))

    def click_on_m_invoice_date(self, inv_m):
        self.waitForElement(self.invoice_date_m, locatorType="xpath")
        self.select_date_from_calender(inv_m, self.invoice_date_m, locatorType="xpath")

    def click_on_c_invoice_date(self, inv_c):
        self.waitForElement(self.invoice_date_c, locatorType="xpath")
        self.select_date_from_calender(inv_c, self.invoice_date_c, locatorType="xpath")

    def click_on_af_invoice_date(self, inv_af):
        self.waitForElement(self.invoice_date_af, locatorType="xpath")
        self.select_date_from_calender(inv_af, self.invoice_date_af, locatorType="xpath")

    def click_m_sample_rcvd_Edited(self, rcvd_mEdited):
        self.waitForElement(self.sample_rcvd_mEdited, locatorType="xpath")
        self.select_date_from_calender(rcvd_mEdited, self.sample_rcvd_mEdited, locatorType="xpath")

    def click_c_sample_rcvd_Edited(self, rcvd_cEdited):
        self.waitForElement(self.sample_rcvd_cEdited, locatorType="xpath")
        self.select_date_from_calender(rcvd_cEdited, self.sample_rcvd_cEdited, locatorType="xpath")

    def click_m_discard_date_Edited(self, dcd_mEdited):
        self.waitForElement(self.discard_date_mEdited, locatorType="xpath")
        self.select_date_from_calender(dcd_mEdited, self.discard_date_mEdited, locatorType="xpath")

    def click_on_c_discard_date_Edited(self, dcd_cEdited):
        self.waitForElement(self.discard_date_cEdited, locatorType="xpath")
        self.select_date_from_calender(dcd_cEdited, self.discard_date_cEdited, locatorType="xpath")

    def input_mfname_edited(self, Mfname):
        self.waitForElement(self.M_fnameEdited, locatorType="xpath")
        self.sendKeys(Mfname, self.M_fnameEdited, locatorType="xpath")

    def input_mlname_edited(self, Mlname):
        self.waitForElement(self.M_lnameEdited, locatorType="xpath")
        self.sendKeys(Mlname, self.M_lnameEdited, locatorType="xpath")

    def input_cfname_edited(self, cfirstname):
        self.waitForElement(self.C_fnameEdited, locatorType="xpath")
        self.sendKeys(cfirstname, self.C_fnameEdited, locatorType="xpath")

    def input_clname_edited(self, clastname):
        self.waitForElement(self.C_lnameEdited, locatorType="xpath")
        self.sendKeys(clastname, self.C_lnameEdited, locatorType="xpath")

    def click_m_DOB_edited(self, dob_mEdited):
        self.waitForElement(self.dob_mEdited, locatorType="xpath")
        self.select_date_from_calender(dob_mEdited, self.dob_mEdited, locatorType="xpath")

    def click_c_DOB_edited(self, dob_cEdited):
        self.waitForElement(self.dob_cEdited, locatorType="xpath")
        self.select_date_from_calender(dob_cEdited, self.dob_cEdited, locatorType="xpath")

    def click_m_collection_date_edited(self, coll_mEdited):
        self.waitForElement(self.collection_date_mEdited, locatorType="xpath")
        self.select_date_from_calender(coll_mEdited, self.collection_date_mEdited, locatorType="xpath")

    def click_c_collection_date_edited(self, coll_cEdited):
        self.waitForElement(self.collection_date_cEdited, locatorType="xpath")
        self.select_date_from_calender(coll_cEdited, self.collection_date_cEdited, locatorType="xpath")

    def input_m_trackingID_edited(self, trackId1_edited):
        self.waitForElement(self.tracking_mEdited, locatorType="xpath")
        self.sendKeys(trackId1_edited, self.tracking_mEdited, locatorType="xpath")
        self.driver.find_element(By.XPATH, self.tracking_mEdited).send_keys(Keys.ENTER)

    def input_c_trackingID_edited(self, trackId2_edited):
        self.waitForElement(self.tracking_cEdited, locatorType="xpath")
        self.sendKeys(trackId2_edited, self.tracking_cEdited, locatorType="xpath")
        self.driver.find_element(By.XPATH, self.tracking_cEdited).send_keys(Keys.ENTER)

    def click_m_invoice_date_edited(self, inv_mEdited):
        self.waitForElement(self.invoice_date_mEdited, locatorType="xpath")
        self.select_date_from_calender(inv_mEdited, self.invoice_date_mEdited, locatorType="xpath")

    def click_c_invoice_date_edited(self, inv_cEdit):
        self.waitForElement(self.invoice_date_cEdited, locatorType="xpath")
        self.select_date_from_calender(inv_cEdit, self.invoice_date_cEdited, locatorType="xpath")

    def select_testedParty(self, testedParty):
        if testedParty is not None:
            party_list = self.elementPresenceCheck(locator=self.testedParty_addList, ByType=By.XPATH)
            testedParty_sel = self.utiles.find_dropdown_select(party_list, testedParty)
            if testedParty_sel is not False:
                testedParty_sel.click()
            else:
                self.log.info("invalid input")
        else:
            self.log.info("Input is None")

    def add_tested_party(self, party):
        self.select_testedParty(party)

    def click_on_channel(self):
        self.waitForElement(self.channel, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.channel, locatorType="xpath")
        time.sleep(1)

    def click_update(self):
        self.waitForElement(self.update_bt, "id")
        self.ElementClick(self.update_bt, "id")
        time.sleep(4)
        # self.waitForElementPresent(self.loader, locatorType="xpath")

    def Get_mFname(self):
        self.waitForElement(self.expected_mfname, locatorType="xpath")
        generated = self.isElementTextPresent(self.expected_mfname, locatorType="xpath")
        generated_mFname = self.utiles.strip_string(generated)
        return generated_mFname

    def Get_cFname(self):
        self.waitForElement(self.expected_cfname, locatorType="xpath")
        generated = self.isElementTextPresent(self.expected_cfname, locatorType="xpath")
        generated_cFname = self.utiles.strip_string(generated)
        return generated_cFname

    def select_reqSchedule(self):
        self.waitForElement(self.request_schedule, "id")
        self.ElementClick(self.request_schedule, "id")

    def confirmation_selection(self):
        self.ElementClick(self.confirmation_cb1)
        self.ElementClick(self.confirmation_cb2)
        self.ElementClick(self.confirmation_cb3)

    def edited_confirmation(self):
        self.ElementClick(self.confirmation_cb1)
        self.ElementClick(self.confirmation_cb2)

    def more_option_fn(self):
        self.webScroll(self.scroll_view_element(self.more_option_c, locatorType="xpath"))
        self.click_on_moreOption()
        self.select_reqSchedule()
        self.edited_confirmation()

    def click_on_moreOption(self):
        self.waitForElement(self.more_option_c, "xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.more_option_c, "xpath")

    def verify_testedParty_title_m(self):
        self.waitForElement(self.title_m, locatorType="xpath")
        actual_title_m = self.isElementTextPresent(self.title_m, locatorType="xpath")
        return actual_title_m

    def verify_testedParty_title_af(self):
        self.waitForElement(self.title_af, locatorType="xpath")
        actual_title_af = self.isElementTextPresent(self.title_af, locatorType="xpath")
        return actual_title_af

    def click_quickSearch(self):
        self.waitForElement(self.quick_search_tab, "id")
        self.ElementClick(self.quick_search_tab, "id")

    def inp_caseID_QS(self, caseId):
        self.waitForElement(self.case_id_inp, locatorType="id")
        self.sendKeys(caseId, self.case_id_inp, locatorType="id")

    def click_Search_QS(self):
        self.waitForElement(self.case_search, "id")
        self.ElementClick(self.case_search, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_on_table(self):
        self.waitForElement(self.details_table)
        self.ElementClick(self.details_table)

    def apply_sample_rcvd_date(self, caseID):
        # self.click_case_file()
        self.click_quickSearch()
        self.inp_caseID_QS(caseID)
        self.click_Search_QS()

    def table_details(self, rcvd_mEdited, inp_turnaround):
        self.click_on_table()
        self.click_start()
        self.click_start_yes()
        self.click_edit()
        self.click_edit_turn_around()
        self.turnaround_selection(inp_turnaround)
        self.webScroll(self.scroll_view_element(self.sample_rcvd_mEdited, locatorType="xpath"))
        self.click_m_sample_rcvd_Edited(rcvd_mEdited)
        self.click_update()

    def verifyCaseTitle(self):
        title_res = self.isElementPresent(self.case_file, locatorType="id")
        self.log.info("case file title verified")
        return title_res

    def GetcaseId(self):
        self.webScroll(self.scroll_view_element(self.exp_caseId, locatorType="xpath"))
        generated = self.isElementTextPresent(self.exp_caseId, locatorType="xpath")
        generated_caseID = self.utiles.strip_string(generated)
        return generated_caseID

    def click_on_addBt(self):
        self.waitForElement(self.testedParty_addbt)
        self.ElementClick(self.testedParty_addbt)

    def click_M_collector_name(self):
        self.waitForElement(self.collector_name_m)
        self.ElementClick(self.collector_name_m)

    def click_C_collector_name(self):
        self.waitForElement(self.collector_name_c)
        self.ElementClick(self.collector_name_c)

    def click_M_coll_advSrc(self):
        self.waitForElement(self.collector_name_adv_Msch)
        self.ElementClick(self.collector_name_adv_Msch)

    def click_C_coll_advSrc(self):
        self.waitForElement(self.collector_name_adv_Csch)
        self.ElementClick(self.collector_name_adv_Csch)

    def click_Create(self):
        self.waitForElement(self.create)
        self.ElementClick(self.create)

    def input_coll_fname(self, inp_coll_fname):
        self.waitForElement(self.coll_fname, locatorType="xpath")
        self.sendKeys(inp_coll_fname, self.coll_fname, locatorType="xpath")

    def input_coll_lname(self, inp_coll_lname):
        self.waitForElement(self.coll_lname, locatorType="xpath")
        self.sendKeys(inp_coll_lname, self.coll_lname, locatorType="xpath")

    def channel_selection_corp(self, channel, inp_s, inp_state, inp_auth, inp_agency, inp_barcode,
                               inp_country, inp_acc, inp_ref1, inp_ref2, inp_dins, inp_customer, inp_phone, inp_email,
                               inp_c_relation):
        inp_channel = channel.strip()
        if inp_channel is not None:
            search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.channel_list)
            channel_sel = self.utiles.find_dropdown_select(search_list, inp_channel)
            if channel_sel is not False:
                channel_sel.click()
                time.sleep(5)
            else:
                self.log.info("No elements found")
        else:
            self.log.info("Input is None")

        if inp_channel == 'Government' or inp_channel == 'Media':
            self.channel_and_media(inp_s, inp_state, inp_acc, inp_auth, inp_agency)
        elif inp_channel == 'Corporate':
            self.corporate(inp_country, inp_acc, inp_ref1, inp_ref2)
        elif inp_channel == 'Retail':
            self.retail(inp_barcode, inp_dins, inp_customer, inp_phone, inp_email, inp_c_relation, inp_ref1, inp_ref2)
        else:
            print("no matching channel")

    def create_collector_name(self, fname, lname):
        self.scroll_view_element(self.collector_name_m, locatorType="xpath")
        self.click_M_collector_name()
        self.click_M_coll_advSrc()
        self.click_addNew_collectorName()
        self.input_coll_fname(fname)
        # self.input_coll_lname(lname)
        self.click_Create()
        time.sleep(7)

    def expected_coll_id(self):
        self.waitForElement(self.exp_coll_id, locatorType="xpath")
        expected_coll_id = self.isElementTextPresent(self.exp_coll_id, locatorType="xpath")
        return expected_coll_id

    def create_red_flag_case(self):
        self.click_plus_button()
        self.webScroll(self.scroll_view_element(self.M_firstname, locatorType="id"))
        source1 = self.getElement(self.drag_m, locatorType="xpath")
        target1 = self.getElement(self.M_firstname, locatorType="id")
        self.driver.execute_script(self.utiles.open_script(), source1, target1)
        self.click_submission_col()
        source2 = self.getElement(self.drag_c, locatorType="xpath")
        target2 = self.getElement(self.C_firstname, locatorType="id")
        self.driver.execute_script(self.utiles.open_script(), source2, target2)
        self.click_submission_col()
        source3 = self.getElement(self.drag_af, locatorType="xpath")
        target3 = self.getElement(self.AF_firstname, locatorType="id")
        self.driver.execute_script(self.utiles.open_script(), source3, target3)
        self.click_turnaround()
        self.turnaround_selection("0 W Day(s)")
        self.click_save()
        time.sleep(2)

    def verify_case_id(self, inp_c_id):
        self.click_case_file()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()
        cs = self.isElementTextPresent(self.c_id, locatorType="xpath")
        ver_cs = self.utiles.strip_string(cs)
        return ver_cs

    def getCaseType(self):
        self.waitForElement(self.case_type, locatorType="xpath")
        casetype = self.isElementTextPresent(self.case_type, locatorType="xpath")
        return casetype.upper()

    def getAccount(self):
        self.waitForElement(self.ver_account, locatorType="xpath")
        acc = self.isElementTextPresent(self.ver_account, locatorType="xpath")
        return acc

    def getCaseDef(self):
        self.waitForElement(self.caseDef, locatorType="xpath")
        case_def = self.isElementTextPresent(self.caseDef, locatorType="xpath")
        return case_def

    def get_sample_rcvd(self):
        m_s_id = self.isElementTextPresent(self.m_sample_rcvd, locatorType="xpath")
        c_s_id = self.isElementTextPresent(self.c_sample_rcvd, locatorType="xpath")
        af_s_id = self.isElementTextPresent(self.af_sample_rcvd, locatorType="xpath")
        s_id = [m_s_id, c_s_id, af_s_id]
        return s_id

    def getSampleId1(self, count):
        ver_s_id = "//table[@class='table ng-star-inserted'][" + str(count + 1) + "]//tbody//tr[2]//td"
        self.waitForElement(ver_s_id, locatorType="xpath", timeout=400)
        self.webScroll(self.scroll_view_element(ver_s_id, locatorType="xpath"))
        ver_s = self.isElementTextPresent(ver_s_id, locatorType="xpath")
        return ver_s

    def getM_colDate(self):
        self.waitForElement(self.ver_m_col_dt)
        self.webScroll(self.scroll_view_element(self.ver_m_col_dt, locatorType="xpath"))
        ver_cd = self.isElementTextPresent(self.ver_m_col_dt, locatorType="xpath")
        return ver_cd

    def getC_colDate(self):
        self.waitForElement(self.ver_c_col_dt)
        self.webScroll(self.scroll_view_element(self.ver_c_col_dt, locatorType="xpath"))
        ver_cd = self.isElementTextPresent(self.ver_c_col_dt, locatorType="xpath")
        return ver_cd

    def getAF_colDate(self):
        self.waitForElement(self.ver_af_col_dt)
        self.webScroll(self.scroll_view_element(self.ver_af_col_dt, locatorType="xpath"))
        ver_cd = self.isElementTextPresent(self.ver_af_col_dt, locatorType="xpath")
        return ver_cd

    def click_delivery_pref(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.delivery_pref)
        self.ElementClick(self.delivery_pref)

    def edit(self):
        self.waitForElement(self.deli_pref_edit)
        self.ElementClick(self.deli_pref_edit)

    def click_deli_pref_add(self):
        self.waitForElement(self.delivery_pref_add, locatorType="xpath")
        self.ElementClick(self.delivery_pref_add, locatorType="xpath")

    def sel_delivery_pref(self, inp_add):
        if inp_add is not None:
            ele = "//a[text()='" + inp_add + "']"
            print(ele)
            self.waitForElement(ele)
            self.ElementClick(ele)
        # if inp_add is not None:
        #     search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.deli_pref_list)
        #     for x in search_list:
        #         print(x.text)
        #         if x.text == str(inp_add):
        #             x.click()
        #         else:
        #             print("no element")

    def send_no_of_copies(self, inp_copy):
        self.waitForElement(self.copy, locatorType="id")
        self.sendKeys(inp_copy, self.copy, locatorType="id")

    def click_delivery_mode(self):
        self.waitForElement(self.delivery_mode, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.delivery_mode, locatorType="xpath"))
        self.ElementClick(self.delivery_mode, locatorType="xpath")

    def click_standardMail_mode(self):
        self.waitForElement(self.standard_mail, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.standard_mail, locatorType="xpath"))
        self.ElementClick(self.standard_mail, locatorType="xpath")

    def click_doc_required(self):
        self.waitForElement(self.doc_req, locatorType="id")
        self.ElementClick(self.doc_req, locatorType="id")

    def send_address(self, inp_address):
        self.waitForElement(self.address, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.address, locatorType="xpath"))
        self.sendKeys(inp_address, self.address, locatorType="xpath")

    def click_deli_pref_country(self):
        self.waitForElement(self.cus_country)
        self.webScroll(self.scroll_view_element(self.cus_country, locatorType="xpath"))
        self.ElementClick(self.cus_country)

    def deli_pref_country_selection(self, inp_cus_country):
        if inp_cus_country is not None:
            search_c_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.c_list)
            c_sel = self.utiles.find_dropdown_select(search_c_list, inp_cus_country)
            if c_sel is not False:
                c_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def send_zip(self, inp_zip):
        self.waitForElement(self.zip, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.zip, locatorType="xpath"))
        self.sendKeys(inp_zip, self.zip, locatorType="xpath")
        self.driver.find_element(By.XPATH, self.zip).send_keys(Keys.ENTER)
        time.sleep(2)

    def send_phone(self, input_phone):
        self.waitForElement(self.phone, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.phone, locatorType="xpath"))
        self.sendKeys(input_phone, self.phone, locatorType="xpath")

    def click_deli_pref_save(self):
        self.waitForElement(self.deli_pref_save, "id")
        self.webScroll(self.scroll_view_element(self.deli_pref_save, locatorType="id"))
        self.ElementClick(self.deli_pref_save, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_deli_pref_close(self):
        self.waitForElement(self.deli_pref_close, "id")
        self.ElementClick(self.deli_pref_close, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_upload_close_icon(self):
        self.waitForElement(self.doc_upload_close, "id")
        self.ElementClick(self.doc_upload_close, "id")

    def click_doc_expandButton(self):
        self.waitForElement(self.doc_expandButton, "id")
        self.ElementClick(self.doc_expandButton, "id")

    def delivery_preference(self, inp_add, inp_copy, inp_mode, inp_address, inp_cus_country, inp_zip, input_phone):
        self.click_delivery_pref()
        self.click_deli_pref_add()
        self.sel_delivery_pref(inp_add)
        self.send_no_of_copies(inp_copy)
        # self.click_standardMail_mode()
        self.choose_deliveryMode(inp_mode)
        # self.click_doc_required()
        self.send_address(inp_address)
        self.click_deli_pref_country()
        self.deli_pref_country_selection(inp_cus_country)
        self.send_zip(inp_zip)
        self.send_phone(input_phone)
        self.click_deli_pref_save()
        self.click_deli_pref_close()

    def click_profile(self):
        self.waitForElement(self.anc_profile, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.anc_profile, locatorType="xpath")

    def click_logout(self):
        self.waitForElement(self.anc_logout, locatorType="id")
        self.ElementClick(self.anc_logout, locatorType="id")

    def click_logout_acc(self):
        self.waitForElement(self.acc, locatorType="xpath")
        self.ElementClick(self.acc, locatorType="xpath")

    def AncLogout(self):
        self.click_profile()
        self.click_logout()
        self.click_logout_acc()
        self.driver.delete_all_cookies()
        # time.sleep(3)

    def verifyAncLogoutTest(self):
        self.waitForElement(self.LOGIN_BUTTON, locatorType="xpath")
        logout_result = self.isElementPresent(self.LOGIN_BUTTON, locatorType="xpath")
        self.log.info("Logout Successfully")
        return logout_result

    def status_check(self):
        self.waitForElement(self.closed_case_status, locatorType="xpath")
        closed_status = self.isElementTextPresent(self.closed_case_status, locatorType="xpath")
        # ver_cs = self.utiles.strip_string(closed_status)
        return closed_status

    def check_reportPreview_title(self):
        self.waitForElement(self.report_preview, locatorType="xpath")
        preview = self.isElementTextPresent(self.report_preview, locatorType="xpath")
        # ver_rp = self.utiles.strip_string(preview)
        return preview

    def click_view_report(self):
        self.waitForElement(self.view_report)
        view_rep = self.isElementPresent(self.view_report, locatorType="xpath")
        time.sleep(3)
        if view_rep is not False:
            self.ElementClick(self.view_report)
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            self.log.error("element not present")
            # raise Exception('view report button not present')

    def view_pdf_icon(self):
        self.waitForElement(self.pdf_icon)
        self.isElementPresent(self.pdf_icon, locatorType="xpath")

    def click_close_icon(self):
        self.waitForElement(self.close_icon)
        self.ElementClick(self.close_icon)
        time.sleep(2)

    def verify_closed_status(self, caseId):
        self.click_case_file()
        time.sleep(3)
        self.click_clear_button()
        self.send_case_id(caseId)
        self.click_case_search()

    def click_help_icon(self):
        self.waitForElement(self.help_icon, "id")
        self.ElementClick(self.help_icon, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_help_icon_active(self):
        self.waitForElement(self.help_icon_active, "id")
        self.ElementClick(self.help_icon_active, "id")
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
        self.waitForElement(self.help_submit_bt, "id")
        self.ElementClick(self.help_submit_bt, "id")

    def click_help_cancel(self):
        self.waitForElement(self.help_cancel_bt, "id")
        self.ElementClick(self.help_cancel_bt, "id")

    def click_help_addIcon(self):
        self.waitForElement(self.help_add_icon, "id")
        self.ElementClick(self.help_add_icon, "id")

    def click_help_closeIcon(self):
        ele_pre = self.isElementPresent(self.add_hlp_closeIcon, locatorType="xpath")
        if ele_pre is not False:
            self.ElementClick(self.add_hlp_closeIcon)
        else:
            pass

    def additional_ticket(self, inp_r, role):
        add_req = self.isElementPresent(self.help_add_icon, locatorType="id")
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

    def help_request(self):
        self.click_table_view()
        # self.click_start()
        # self.click_start_yes()
        active_icon = self.isElementPresent(self.help_icon_active, locatorType="id")
        if active_icon is not False:
            self.click_help_icon_active()
        else:
            self.click_help_icon()

    def closeToasterMsg(self):
        self.waitForElement(self.closeMessage)
        self.ElementClick(self.closeMessage)

    def click_amend_bt(self):
        self.waitForElement(self.amend_bt, "id")
        self.ElementClick(self.amend_bt, "id")

    def click_resend_bt(self):
        self.waitForElement(self.resend_bt)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.resend_bt)

    def click_editBt_amend(self):
        self.waitForElement(self.amend_editBt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.amend_editBt, "id")

    def send_middleName_m(self, inp_middle_name):
        self.waitForElement(self.middle_name_amend, locatorType="xpath")
        self.sendKeys(inp_middle_name, self.middle_name_amend, locatorType="xpath")

    def click_amend_UpdateBt(self):
        self.waitForElement(self.amend_update_Bt, "id")
        self.ElementClick(self.amend_update_Bt, "id")

    def awaiting_statusCheck(self):
        report_status = self.isElementTextPresent(self.case_status, locatorType="xpath")
        return report_status

    def amend_reportEdit(self, inp_middleName):
        self.click_amend_bt()
        self.click_editBt_amend()
        self.send_middleName_m(inp_middleName)
        self.click_amend_UpdateBt()
        self.waitForElementPresent(self.loader, locatorType="xpath")
        time.sleep(3)

    def SurrogacyIVFclk(self):
        self.waitForElement(self.SurrIVF)
        indicatortxt = self.isElementTextPresent(self.SurrIVFtxt, "xpath")
        self.ElementClick(self.SurrIVF)
        return indicatortxt

    def click_request_Type(self):
        self.waitForElement(self.request_type)
        self.ElementClick(self.request_type)
        time.sleep(2)

    def requestType_selection(self, inp_reqType):
        if inp_reqType is not None:
            search_request_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.request_type_list)
            reqType_sel = self.utiles.find_dropdown_select(search_request_list, inp_reqType)
            if reqType_sel is not False:
                reqType_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_NATA_immigration(self):
        self.waitForElement(self.NATA_immigration)
        self.ElementClick(self.NATA_immigration)
        time.sleep(2)

    def nataImmigration_selection(self, inp_immigrationType):
        if inp_immigrationType is not None:
            search_NATA_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.NATA_immigration_list)
            NATA_type_sel = self.utiles.find_dropdown_select(search_NATA_list, inp_immigrationType)
            if NATA_type_sel is not False:
                NATA_type_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_country_involved(self):
        self.waitForElement(self.county_involved)
        self.ElementClick(self.county_involved)
        time.sleep(1)

    def country_involved_selection(self, inp_country):
        if inp_country is not None:
            search_country_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.country_list)
            country_sel = self.utiles.find_dropdown_select(search_country_list, inp_country)
            if country_sel is not False:
                country_sel.click()
            else:
                self.log.info("input is False")

    def add_NATA_Affidavit_comment(self, comment):
        self.waitForElement(self.NATA_affidavit_comments)
        self.sendKeys(comment, self.NATA_affidavit_comments)

    def chain_NATA_selection(self, inp_reqType, inp_immigrationType, inp_country):
        self.click_request_Type()
        self.requestType_selection(inp_reqType)
        self.click_NATA_immigration()
        self.nataImmigration_selection(inp_immigrationType)
        self.click_country_involved()
        self.click_search()
        time.sleep(2)
        self.country_involved_selection(inp_country)
        self.add_NATA_Affidavit_comment("test purpose")

    def nata_Verification_Corp(self, inp_channel, inp_s, inp_state, inp_auth, inp_agency,
                               inp_barcode, inp_country, inp_acc, inp_ref1, inp_ref2, inp_dins, inp_customer, inp_phone,
                               inp_email, inp_c_relation, inp_test_type, recon_section, inp_case_def, inp_add_test,
                               inp_type, online_setup, inp_turnaround, inp_reqType,
                               inp_immigrationType, country_involved, M_sample_id, m_sample_dt,
                               m_firstname, m_lastname, m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob,
                               retail_m_cdt, retail_m_tracking, C_sample_id, c_sample_dt, c_firstname, c_lastname,
                               c_dob, c_race, c_cdt, inp_c_tracking, retail_c_dob, retail_c_cdt, retail_c_tracking,
                               AF_sample_id, af_sample_dt, af_firstname, af_lastname, af_dob, af_race, af_ret_race,
                               af_cdt, inp_af_tracking, retail_af_dob, retail_af_cdt, retail_af_tracking,
                               fe_sample_id, fe_sample_dt, fe_firstname, fe_lastname, fe_dob, fe_race, fe_ret_race,
                               fe_cdt, inp_fe_tracking, retail_fe_dob, retail_fe_cdt, retail_fe_tracking):
        self.click_on_channel()
        self.channel_selection_corp(inp_channel, inp_s, inp_state, inp_auth, inp_agency, inp_barcode,
                                    inp_country, inp_acc, inp_ref1, inp_ref2, inp_dins, inp_customer, inp_phone,
                                    inp_email, inp_c_relation)
        self.common(inp_test_type, recon_section, inp_case_def, inp_add_test, inp_channel, inp_type,
                    online_setup, inp_turnaround)
        self.chain_NATA_selection(inp_reqType, inp_immigrationType, country_involved)
        title_list = self.verify_testedParty_title()
        if self.getTable_count() != 0:
            for k in range(0, self.getTable_count()):
                self.func(k, title_list[k], M_sample_id, m_sample_dt, m_firstname, m_lastname, inp_channel, m_dob,
                          m_race,
                          m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt, retail_m_tracking, C_sample_id,
                          c_sample_dt, c_firstname, c_lastname, c_dob, c_race, c_cdt, inp_c_tracking, retail_c_dob,
                          retail_c_cdt, retail_c_tracking, AF_sample_id, af_sample_dt, af_firstname, af_lastname,
                          af_dob,
                          af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob, retail_af_cdt,
                          retail_af_tracking,
                          fe_sample_id, fe_sample_dt, fe_firstname, fe_lastname, fe_dob, fe_race, fe_ret_race, fe_cdt,
                          inp_fe_tracking, retail_fe_dob, retail_fe_cdt, retail_fe_tracking)
        else:
            self.log.info("no data available")

    def verifyRestricted_Case(self):
        self.webScroll(self.scroll_view_element(self.restricted_access, locatorType="xpath"))
        self.waitForElement(self.restricted_access, locatorType="xpath")
        title_result = self.isElementTextPresent(self.restricted_access, locatorType="xpath")
        return title_result

    def click_RestrictedToggle(self):
        self.waitForElement(self.toogle_button)
        self.ElementClick(self.toogle_button)

    def click_referral_status(self):
        self.webScroll(self.scroll_view_element(self.select_referral_status, locatorType="xpath"))
        self.waitForElement(self.select_referral_status)
        self.ElementClick(self.select_referral_status)

    def choose_referral_status(self, referral_type):
        if referral_type is not None:
            search_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.referral_status_list)
            referral_sel = self.utiles.find_dropdown_select(search_list, referral_type)
            if referral_sel is not False:
                referral_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def click_help_status(self):
        self.waitForElement(self.help_status_icon, "id")
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.help_status_icon, "id")

    def getModified_status(self):
        self.waitForElement(self.modified_status)
        element = self.isElementPresent(self.modified_status)
        element = element.text
        return element

    def verify_helpTicket_status(self, inp_c_id):
        time.sleep(2)
        self.click_case_file()
        self.click_clear_button()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()
        self.click_help_status()

    def get_MSampleType_status(self):
        self.waitForElement(self.ver_Msample_type)
        self.webScroll(self.scroll_view_element(self.ver_Msample_type, locatorType="xpath"))
        ver_Mstatus = self.isElementTextPresent(self.ver_Msample_type, locatorType="xpath")
        return ver_Mstatus

    def get_CSampleType_status(self):
        self.waitForElement(self.ver_Csample_type)
        ver_Cstatus = self.isElementTextPresent(self.ver_Csample_type, locatorType="xpath")
        return ver_Cstatus

    def get_AfSampleType_status(self):
        self.waitForElement(self.ver_Afsample_type)
        ver_Afstatus = self.isElementTextPresent(self.ver_Afsample_type, locatorType="xpath")
        return ver_Afstatus

    def verify_audit_flag(self, inp_c_id):
        self.click_case_file()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()
        ver_af = self.isElementTextPresent(self.audit_flag, locatorType="xpath")
        return bool(ver_af)

    def get_anr_case(self, inp_c_id):
        self.click_case_file()
        self.click_clear_button()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()

    def edit_anr_case(self, m_e_lastname, c_e_lastname, af_e_lastname):
        self.click_edit_button()
        self.click_m__edit_last_name(m_e_lastname)
        self.click_c__edit_last_name(c_e_lastname)
        # self.click_af__edit_last_name(af_e_lastname)

    def edit_anr_case_midl(self, *middle_name):
        self.click_edit_button()
        self.editMiddleName(*middle_name)

    def getEditedMName(self):
        self.waitForElement(self.ver_m_f_name)
        self.webScroll(self.scroll_view_element(self.ver_m_f_name, locatorType="xpath"))
        ver_mf = self.isElementTextPresent(self.ver_m_f_name, locatorType="xpath")
        self.waitForElement(self.ver_m_e_lastname)
        self.webScroll(self.scroll_view_element(self.ver_m_e_lastname, locatorType="xpath"))
        ver_ml = self.isElementTextPresent(self.ver_m_e_lastname, locatorType="xpath")
        return ver_mf + " " + ver_ml

    def getEditedCName(self):
        self.waitForElement(self.ver_c_f_name)
        self.webScroll(self.scroll_view_element(self.ver_c_f_name, locatorType="xpath"))
        ver_cf = self.isElementTextPresent(self.ver_c_f_name, locatorType="xpath")
        self.waitForElement(self.ver_c_e_lastname)
        self.webScroll(self.scroll_view_element(self.ver_c_e_lastname, locatorType="xpath"))
        ver_cl = self.isElementTextPresent(self.ver_c_e_lastname, locatorType="xpath")
        return ver_cf + " " + ver_cl

    def getEditedAFName(self):
        self.waitForElement(self.ver_af_f_name)
        self.webScroll(self.scroll_view_element(self.ver_af_f_name, locatorType="xpath"))
        ver_af_f = self.isElementTextPresent(self.ver_af_f_name, locatorType="xpath")
        self.waitForElement(self.ver_af_e_lastname)
        self.webScroll(self.scroll_view_element(self.ver_af_e_lastname, locatorType="xpath"))
        ver_af_l = self.isElementTextPresent(self.ver_af_e_lastname, locatorType="xpath")
        return ver_af_f + " " + ver_af_l

    def click_c_indicators(self):
        self.waitForElement(self.indicator_c)
        self.webScroll(self.scroll_view_element(self.indicator_c, locatorType="xpath"))
        self.ElementClick(self.indicator_c)

    def click_Related_Father_Mother(self):
        ele = self.getElement(self.related_f_m_button, locatorType="xpath")
        self.driver.execute_script("arguments[0].click();", ele)

    def click_indicator(self):
        self.click_edit_button()
        self.click_c_indicators()

    def select_indicator(self):
        self.click_Related_Father_Mother()
        self.click_c_indicators()
        self.click_update()
        self.click_skip()
        self.click_yes()

    def get_related_f_m_indicator(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.related_f_m)
        self.webScroll(self.scroll_view_element(self.related_f_m, "xpath"))
        ver_ind = self.isElementTextPresent(self.related_f_m, locatorType="xpath")
        print(ver_ind)
        return ver_ind

    def click_resend(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.resend)
        self.ElementClick(self.resend)

    def click_resend_request(self):
        self.waitForElement(self.resend_req)
        self.ElementClick(self.resend_req)
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def resend_request(self):
        self.click_resend()
        self.click_resend_request()

    def verify_status(self):
        st = self.isElementTextPresent(self.case_status, locatorType="xpath")
        return st

    def getCollDtM(self):
        col_m = self.isElementTextPresent(self.ver_col_dt_m, locatorType="xpath")
        return col_m

    def getCollDtC(self):
        col_c = self.isElementTextPresent(self.ver_col_dt_c, locatorType="xpath")
        return col_c

    def getCollDtAF(self):
        col_af = self.isElementTextPresent(self.ver_col_dt_af, locatorType="xpath")
        return col_af

    def getSample_type(self, k):
        sampleType = "//table[@class='table ng-star-inserted'][" + str(k + 1) + "]//tbody//tr[5]//td"
        self.waitForElement(sampleType, locatorType="xpath", timeout=400)
        self.webScroll(self.scroll_view_element(sampleType, locatorType="xpath"))
        ver_s = self.isElementTextPresent(sampleType, locatorType="xpath")
        return ver_s

    def getAllSampType(self):
        temp = []
        for k in range(0, self.getModifiedTable_count()):
            all = self.checkSampType(k)
            temp.append(all)
        return temp

    def getAllCaseRole(self):
        temp = []
        for k in range(0, self.getModifiedTable_count()):
            all_role = self.checkCaseRole(k)
            temp.append(all_role)
        return temp

    def checkCaseRole(self, k):
        title_list = self.verify_testedParty_title()
        role = ""
        if title_list[k] == "M":
            role = self.getCase_Role(k)
        elif title_list[k] == "C":
            role = self.getCase_Role(k)
        elif title_list[k] == "AF":
            role = self.getCase_Role(k)
        elif title_list[k] == "FE":
            role = self.getCase_Role(k)
        elif title_list[k] == "AM":
            role = self.getCase_Role(k)
        return role

    def getCase_Role(self, k):
        case_role = "//table[@class='table ng-star-inserted'][" + str(k + 1) + "]//tbody//tr[4]//td"
        self.waitForElement(case_role, locatorType="xpath", timeout=400)
        self.webScroll(self.scroll_view_element(case_role, locatorType="xpath"))
        ver_s = self.isElementTextPresent(case_role, locatorType="xpath")
        return ver_s

    def getAllRace(self):
        temp = []
        for k in range(0, self.getModifiedTable_count()):
            all_role = self.checkRace(k)
            temp.append(all_role)
        return temp

    def checkRace(self, k):
        title_list = self.verify_testedParty_title()
        race = ""
        if title_list[k] == "M":
            race = self.getRace(k)
        elif title_list[k] == "C":
            race = self.getRace(k)
        elif title_list[k] == "AF":
            race = self.getRace(k)
        elif title_list[k] == "FE":
            race = self.getRace(k)
        elif title_list[k] == "AM":
            race = self.getRace(k)
        return race

    def getRace(self, k):
        race = "//table[@class='table ng-star-inserted'][" + str(k + 1) + "]//tbody//tr[12]//td"
        self.waitForElement(race, locatorType="xpath", timeout=400)
        self.webScroll(self.scroll_view_element(race, locatorType="xpath"))
        ver_s = self.isElementTextPresent(race, locatorType="xpath")
        return ver_s

    def ListToDict(self, list_key, list_value):
        res = {}
        for key in list_key:
            for value in list_value:
                res[key] = value
                list_value.remove(value)
                break
        return res

    def checkSampType(self, k):
        title_list = self.verify_testedParty_title()
        sample = ""
        sam = ""
        if title_list[k] == "M":
            sam = self.getSample_type(k)
            # sample = self.getSampleId1(k)
        elif title_list[k] == "C":
            sam = self.getSample_type(k)
            # sample = self.getSampleId1(k)
        elif title_list[k] == "AF":
            sam = self.getSample_type(k)
            # sample = self.getSampleId1(k)
        elif title_list[k] == "FE":
            sam = self.getSample_type(k)
            # sample = self.getSampleId1(k)
        elif title_list[k] == "AM":
            sam = self.getSample_type(k)
            # sample = self.getSampleId1(k)

        return sam

    def clickIndicators(self):
        self.waitForElement(self.Indicators)
        self.ElementClick(self.Indicators)

    def AddSampleImageForNonChaninCases(self, inp_comment, channel=None):
        self.click_doc()
        verify = self.verify_doc_click()
        self.utiles.assertionTrue(verify, "failed to perform the click action - doc ")
        self.click_add()
        self.click_scan_close()
        self.click_document()
        self.click_browse_files_for_img()
        self.image_doc_selection(channel)
        self.click_tested_party()
        self.tested_party_selection()
        self.send_comments(inp_comment)
        self.click_upload()

    def AddSampleImageForNonChanMandC(self, inp_comment):
        self.click_doc()
        verify = self.verify_doc_click()
        self.utiles.assertionTrue(verify, "failed to perform the click action - doc ")
        self.click_add()
        self.click_scan_close()
        self.click_document()
        self.click_browse_files_for_img()
        self.image_doc_selection()
        self.click_tested_party()
        self.tested_party_selection_for_MandC()
        self.send_comments(inp_comment)
        self.click_upload()

    def verify_Case(self, inp_c_id):
        self.click_case_file()
        self.click_clear_button()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()
        self.waitForElement(self.c_id)
        c_text = self.isElementTextPresent(self.c_id, locatorType="xpath")
        case_text = self.utiles.strip_string(c_text)
        return case_text

    def verify_m_name(self):
        self.waitForElement(self.ver_m_f_name)
        self.webScroll(self.scroll_view_element(self.ver_m_f_name, locatorType="xpath"))
        f_name = self.isElementTextPresent(self.ver_m_f_name, locatorType="xpath")
        self.waitForElement(self.ver_m_e_lastname)
        l_name = self.isElementTextPresent(self.ver_m_e_lastname, locatorType="xpath")
        return f_name + " " + l_name

    def verify_NY(self):
        self.waitForElement(self.ny_verification, locatorType="xpath")
        result = self.isElementPresent(self.ny_verification, locatorType="xpath")
        return result

    def verify_reportadded(self):
        self.waitForElement(self.report_presence, locatorType="xpath")
        result = self.isElementPresent(self.report_presence, locatorType="xpath")
        return result

    def click_docc_view(self):
        self.waitForElement(self.docc_view)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.docc_view)

    def view_doc_from_Portal(self, inp_c_id):
        self.click_case_file()
        self.send_case_id(inp_c_id)
        self.click_case_search()
        self.click_table_view()
        self.click_docc_view()

    def click_adv_M(self):
        self.waitForElement(self.adv_search_coll_siteM)
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.adv_search_coll_siteM)

    def click_adv_C(self):
        self.waitForElement(self.adv_search_coll_siteC)
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.adv_search_coll_siteC)

    def click_adv_AF(self):
        self.waitForElement(self.adv_search_coll_siteAF)
        self.waitForElementPresent(self.loader, "xpath")
        self.ElementClick(self.adv_search_coll_siteAF)

    def add_coll_site_m(self):
        if self.col_site_bt_m is not None:
            self.waitForElement(self.col_site_bt_m, "id")
            self.webScroll(self.scroll_view_element(self.col_site_bt_m, locatorType="id"))
            self.ElementClick(self.col_site_bt_m, "id")
            time.sleep(2)
        else:
            pass

    def add_coll_site_m_edit(self):
        self.waitForElement(self.col_site_bt_edit_m)
        self.webScroll(self.scroll_view_element(self.col_site_bt_edit_m, locatorType="xpath"))
        self.ElementClick(self.col_site_bt_edit_m)

    def send_collection_site(self, collection_site):
        self.waitForElement(self.collection_site_field)
        self.sendKeys(collection_site, self.collection_site_field, locatorType="xpath")

    def send_zip_code(self, zip_code):
        self.waitForElement(self.zip_field)
        self.sendKeys(zip_code, self.zip_field, locatorType="xpath")

    def send_coll_comments(self, comments):
        self.waitForElement(self.comments_field)
        self.sendKeys(comments, self.comments_field, locatorType="xpath")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def expected_collection_SiteId(self):
        self.waitForElement(self.exp_collection_siteID, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.exp_collection_siteID, locatorType="xpath"))
        expected_coll_Siteid = self.isElementTextPresent(self.exp_collection_siteID, locatorType="xpath")
        return expected_coll_Siteid

    def add_new_coll_site_M(self, collection_site, zip, comments):
        self.add_coll_site_m_edit()
        self.click_adv_M()
        self.click_add_new_collName()
        self.send_collection_site(collection_site)
        self.send_zip_code(zip)
        time.sleep(2)
        self.send_coll_comments(comments)
        self.click_Create()
        actual = self.verifytoaster_msg_success()
        self.utiles.hard_assertion("Success", actual, "collection site not added ")
        # self.toasterMessageClose()

    def verify_c_name(self):
        self.waitForElement(self.ver_c_f_name)
        self.webScroll(self.scroll_view_element(self.ver_c_f_name, locatorType="xpath"))
        f_name = self.isElementTextPresent(self.ver_c_f_name, locatorType="xpath")
        self.waitForElement(self.ver_c_e_lastname)
        l_name = self.isElementTextPresent(self.ver_c_e_lastname, locatorType="xpath")
        return f_name + " " + l_name

    def verify_af_name(self):
        self.waitForElement(self.ver_af_f_name)
        self.webScroll(self.scroll_view_element(self.ver_af_f_name, locatorType="xpath"))
        f_name = self.isElementTextPresent(self.ver_af_f_name, locatorType="xpath")
        self.waitForElement(self.ver_af_e_lastname)
        l_name = self.isElementTextPresent(self.ver_af_e_lastname, locatorType="xpath")
        return f_name + " " + l_name

    def click_alert_cancel_bt(self):
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        ele = self.isElementPresent(self.alert_cancel, locatorType="id")
        if ele is not False:
            # self.waitForElement(self.alert_cancel, locatorType="id")
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.ElementClick(self.alert_cancel, locatorType="id")
        else:
            pass

    def expectedGroupId(self):
        Id = self.isElementTextPresent(self.exp_groupID, locatorType="xpath")
        print(Id)
        groupId = self.utiles.SplitgroupId(Id)
        return groupId

    def send_M_sampleId_dev(self, count, m_id):
        sampleID = self.sample_id + str(count)
        self.waitForElement(sampleID, "id")
        self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
        self.waitForElement(sampleID, "id")
        self.sendKeys(self.utiles.strip_WhiteSpace(m_id), sampleID, locatorType="id")
        self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
        # actual = self.verifytoaster_msg_success()
        actual = self.verify_sample_is_valid()
        self.utiles.assertionTrue(actual, "Error occurs while entering the  Mother sample id " + m_id)

    def send_C_sampleId_dev(self, count, c_id):
        sampleID = self.sample_id + str(count)
        self.waitForElement(sampleID, "id")
        self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
        self.waitForElement(sampleID, "id")
        self.sendKeys(self.utiles.strip_WhiteSpace(c_id), sampleID, locatorType="id")
        self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
        actual = self.verify_sample_is_valid()
        self.utiles.assertionTrue(actual, "Error occurs while entering the Child sample id " + c_id)

    def send_AF_sampleId_dev(self, count, af_id):
        sampleID = self.sample_id + str(count)
        self.waitForElement(sampleID, "id")
        self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
        self.waitForElement(sampleID, "id")
        self.sendKeys(self.utiles.strip_WhiteSpace(af_id), sampleID, locatorType="id")
        self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
        actual = self.verify_sample_is_valid()
        self.utiles.assertionTrue(actual, "Error occurs while entering the AF sample id" + af_id)

    def create_case_dev(self, inp_channel, inp_s, inp_state, inp_acc, inp_auth, inp_agency, inp_barcode, inp_country,
                        inp_ref1, inp_ref2, inp_dins, inp_customer, inp_phone, inp_email, inp_c_relation, inp_test_type,
                        inp_case_def, inp_add_test, Semail, Spassword, Sans, inp_type, inp_turnaround, M_sample_id,
                        m_sample_dt, m_firstname, m_lastname, m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking,
                        retail_m_dob, retail_m_cdt, retail_m_tracking, C_sample_id, c_sample_dt, c_firstname,
                        c_lastname, c_dob, c_race, c_cdt, inp_c_tracking, retail_c_dob,
                        retail_c_cdt, retail_c_tracking, af_sample_id, af_sample_dt, af_firstname, af_lastname, af_dob,
                        af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob, retail_af_cdt, retail_af_tracking,
                        fe_sample_id, fe_sample_dt, fe_firstname, fe_lastname, fe_dob, fe_race, fe_ret_race, fe_cdt,
                        inp_fe_tracking, retail_fe_dob, retail_fe_cdt, retail_fe_tracking, enable_oneline_setup=True,
                        recon_section=None):

        self.click_channel()
        self.channel_selection(inp_channel, inp_s, inp_state, inp_acc, inp_auth, inp_agency, inp_barcode, inp_country,
                               inp_ref1, inp_ref2, inp_dins, inp_customer, inp_phone, inp_email, inp_c_relation)
        self.common(inp_test_type, recon_section, inp_case_def, inp_add_test, inp_channel, inp_type,
                    enable_oneline_setup, inp_turnaround)
        # if inp_channel == "Retail":
        #     self.Report_Lang_Add(["French", "Spanish"])

        title_list = self.verify_testedParty_title()
        if self.getTable_count() != 0:
            for k in range(0, self.getTable_count()):
                self.func(k, title_list[k], M_sample_id, m_sample_dt, m_firstname, m_lastname, inp_channel, m_dob,
                          m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt, retail_m_tracking,
                          C_sample_id, c_sample_dt, c_firstname, c_lastname, c_dob, c_race, c_cdt, inp_c_tracking,
                          retail_c_dob, retail_c_cdt, retail_c_tracking, af_sample_id, af_sample_dt, af_firstname,
                          af_lastname, af_dob, af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob,
                          retail_af_cdt, retail_af_tracking, fe_sample_id, fe_sample_dt, fe_firstname, fe_lastname,
                          fe_dob, fe_race, fe_ret_race, fe_cdt, inp_fe_tracking, retail_fe_dob, retail_fe_cdt,
                          retail_fe_tracking)

        else:
            self.log.info("no data available")

    def func(self, count, identifier, M_sample_id, m_sample_dt, m_firstname, m_lastname, inp_channel, m_dob, m_race,
             m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt, retail_m_tracking, C_sample_id,
             c_sample_dt, c_firstname, c_lastname, c_dob, c_race, c_cdt, inp_c_tracking, retail_c_dob,
             retail_c_cdt, retail_c_tracking, af_sample_id, af_sample_dt, af_firstname, af_lastname, af_dob,
             af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob, retail_af_cdt, retail_af_tracking,
             fe_sample_id, fe_sample_dt, fe_firstname, fe_lastname, fe_dob,
             fe_race, fe_ret_race, fe_cdt, inp_fe_tracking, retail_fe_dob, retail_fe_cdt,
             retail_fe_tracking):
        if identifier == "M" or identifier == "AM" or identifier == "AMA" or identifier == "AS" or identifier == "AMGM"\
                or identifier == "HS" or identifier == "FS" or identifier == "D" or identifier == "Mt1":
            self.enter_Mother_details_dev(count, M_sample_id, m_sample_dt, m_firstname, m_lastname, inp_channel,
                                          m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt,
                                          retail_m_tracking)
        elif identifier == "C":
            self.enter_Child_details_dev(count, C_sample_id, c_sample_dt, c_firstname, c_lastname,
                                         inp_channel, c_dob, c_race, c_cdt, inp_c_tracking, retail_c_dob, retail_c_cdt,
                                         retail_c_tracking)
        elif identifier == "AF" or identifier == "AT" or identifier == "APA" or identifier == "AKS" or \
                identifier == "APGM" or identifier == "AMGF" or identifier == "PKHS" or identifier == "PKFS"\
                or identifier == "MKHS" or identifier == "APU" or identifier == "AMU"  or identifier == "R" \
                or identifier == "Mt2":
            self.enter_AF_details_dev(count, af_sample_id, af_sample_dt, af_firstname, af_lastname, inp_channel, af_dob,
                                      af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob, retail_af_cdt,
                                      retail_af_tracking)
        elif identifier == "FE" or identifier == "APGF" or identifier == "MPKHS" or identifier == "MPKS" or \
                identifier == "PKFS":
            self.enter_FE_details_dev(count, fe_sample_id, fe_sample_dt, fe_firstname, fe_lastname, inp_channel, fe_dob,
                                      fe_race, fe_ret_race, fe_cdt, inp_fe_tracking, retail_fe_dob, retail_fe_cdt,
                                      retail_fe_tracking)

    def getAllSampleID(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        temp = []
        for k in range(0, self.getModifiedTable_count()):
            all = self.samplefunction(k)
            temp.append(all)
        next = "casedetailsnextIcon"
        nextIcon = self.getElement(next, "id")
        if nextIcon.is_enabled() is not False:
            self.ElementClick(next, "id")
            for k in range(0, self.getModifiedTable_count()):
                all_id = self.samplefunction(k)
                temp.append(all_id)
                temp = list(dict.fromkeys(temp))
        print("temp", temp)
        return temp

    def samplefunction(self, k):
        title_list = self.verify_testedParty_title()
        sample = ""
        if title_list[k] == "M" or title_list[k] == "AS" or title_list[k] == "AM" or \
                title_list[k] == "AMA" or title_list[k] == "AMGM" or title_list[k] == "HS" or title_list[k] == "FS"\
                or title_list[k] == "D" or title_list[k] == "Mt1":
            sample = self.getSampleId1(k)
        elif title_list[k] == "C":
            sample = self.getSampleId1(k)
        elif title_list[k] == "AF" or title_list[k] == "AT" or title_list[k] == "APA" or title_list[k] == "AKS" or \
                title_list[k] == "APGM" or title_list[k] == "AMGF" or title_list[k] == "PKHS" or title_list[k] == "PKFS"\
                or title_list[k] == "MKHS" or title_list[k] == "APU" or title_list[k] == "AMU" or title_list[k] == "R" \
                or title_list[k] == "Mt2":
            sample = self.getSampleId1(k)
        elif title_list[k] == "FE" or title_list[k] == "APGF" or title_list[k] == "MPKHS" or title_list[k] == "MPKS":
            sample = self.getSampleId1(k)
        return sample

    def enter_Mother_details_dev(self, count, M_sample_id, m_sample_dt, m_firstname, m_lastname, inp_channel,
                                 m_dob, m_race,
                                 m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt, retail_m_tracking):
        if DEV or TEST:
            self.send_M_sampleId_dev(count, M_sample_id)
        else:
            self.send_M_sample_id(count, M_sample_id)
        self.click_M_sample_dt(count, m_sample_dt)
        self.send_mother_firstname(count, m_firstname)
        self.send_mother_lastname(count, m_lastname)
        self.enter_m(count, inp_channel, m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt,
                     retail_m_tracking)

    def enter_Child_details_dev(self, count, C_sample_id, c_sample_dt, c_firstname, c_lastname, inp_channel, c_dob,
                                c_race, c_cdt, inp_c_tracking, retail_c_dob, retail_c_cdt, retail_c_tracking):
        if DEV or TEST:
            self.send_C_sampleId_dev(count, C_sample_id)
        else:
            self.send_C_sample_id(count, C_sample_id)
        self.click_C_sample_dt(count, c_sample_dt)
        self.send_child_firstname(count, c_firstname)
        self.send_child_lastname(count, c_lastname)
        self.enter_c(count, inp_channel, c_dob, c_race, c_cdt, inp_c_tracking, retail_c_dob, retail_c_cdt,
                     retail_c_tracking)

    def enter_AF_details_dev(self, count, af_sample_id, af_sample_dt, af_firstname, af_lastname, inp_channel, af_dob,
                             af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob, retail_af_cdt,
                             retail_af_tracking):
        if DEV or TEST:
            self.send_AF_sampleId_dev(count, af_sample_id)
        else:
            self.send_AF_sample_id(count, af_sample_id)
        self.click_AF_sample_dt(count, af_sample_dt)
        self.send_Af_firstname(count, af_firstname)
        self.send_Af_lastname(count, af_lastname)
        self.enter_af(count, inp_channel, af_dob, af_race, af_ret_race, af_cdt, inp_af_tracking, retail_af_dob,
                      retail_af_cdt,
                      retail_af_tracking)

    def caseCreation_verification(self):
        self.waitForElement(self.c_id, locatorType="xpath", timeout="400")
        c_id_verify = self.isElementTextPresent(self.c_id, locatorType="xpath")
        return c_id_verify

    def skipBt_verification(self):
        self.waitForElement(self.skip, locatorType="id")
        skip_verify = self.isElementPresent(self.skip, locatorType="id")
        return skip_verify

    def verifyAccession(self):
        self.waitForElement(self.skip, "id", timeout=10)
        status = self.isElementVisible(self.skip, "id")
        return status

    def verifyCaseCreation(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.c_id, locatorType="xpath")
        e_id = self.isElementTextPresent(self.c_id, locatorType="xpath")
        print(e_id)
        if e_id != None or e_id != False:
            result = True
        else:
            result = False
        return result

    def verifySampleWithSuccessMessage(self):
        # self.waitForElement(self.success_msgg, timeout=20)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        # ele_pre = self.isElementTextPresent(self.success_msgg, locatorType="xpath")
        ele_pre = self.isElementTextPresent(self.valid_sampleID_already_existing_sample_id, locatorType="xpath")
        if ele_pre is not False:
            if ele_pre == "Success" or "Sample ID already exists in another Case.":
                ele_pre = True
            else:
                ele_pre = False

        else:
            ele_pre = False
            print("Sample id success message is not displayed")
        return ele_pre

    def verifySampleWithAlreadyExistMessages(self):
        self.waitForElement(self.sampleIDAlredayExist)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_pre = self.isElementTextPresent(self.sampleIDAlredayExist, locatorType="xpath")
        if ele_pre == "Sample ID already exists in another Case.":
            ele_pre = True
        else:
            ele_pre = False
        return ele_pre

    def verify_sample_is_valid(self):
        result1 = self.verifySampleWithSuccessMessage()
        # result2 = self.verifySampleWithAlreadyExistMessages()
        # if result1 is True or result2 is False:
        if result1 is True:
            status = True
        # elif result1 is False or result2 is True:
        #     status = True
        else:
            status = False
        return status

    def groupId_verification(self):
        Id = self.isElementTextPresent(self.groupID, locatorType="xpath")
        print(Id)
        new_ID = self.utiles.replaceGroupID(Id)
        return new_ID.strip()

    def documentCount(self):
        self.waitForElement(self.doc_count, locatorType="xpath")
        countNo = self.isElementTextPresent(self.doc_count, locatorType="xpath")
        # split_count = self.utiles.docNo_strip(countNo)
        return countNo

    def commonTab_close(self):
        ele_present = self.isElementPresent(self.commonName_close, locatorType="id")
        if ele_present is not False:
            self.ElementClick(self.commonName_close, locatorType="id")
        else:
            pass

    def click_caseDetailIndictor_bt(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if self.caseDetailIndicator is not False:
            self.waitForElement(self.caseDetailIndicator, locatorType="id")
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.ElementClick(self.caseDetailIndicator, locatorType="id")
            self.waitForElementPresent(self.loader, locatorType="xpath")
        else:
            pass

    def enable_NY(self):
        if self.NY_enable is not False:
            self.waitForElement(self.NY_enable, locatorType="xpath")
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.ElementClick(self.NY_enable, locatorType="xpath")
            self.waitForElementPresent(self.loader, locatorType="xpath")
            # self.verifytoaster_msg_success()
            self.ElementClick(self.caseDetailIndicator, locatorType="id")
        else:
            pass

    def NY_indicatorOn_verify(self):
        self.click_caseDetailIndictor_bt()
        self.enable_NY()
        time.sleep(2)

    def getTable_count(self):
        count = self.elementPresenceCheck(ByType="xpath", locator=self.tables_count)
        x = len(count)
        print(len(count))
        return x

    def getModifiedTable_count(self):
        modified = "//div[@class='right-table right-table-view']//table"
        count = self.elementPresenceCheck(ByType="xpath", locator=modified)
        x = len(count)
        # if nextIcon is not False:
        #     x = x + 1
        return x

    # def verify_testedParty_title(self):
    #     next = "casedetailsnextIcon"
    #     nextIcon = self.isElementPresent(next, "id")
    #     self.waitForElement(self.title, locatorType="xpath")
    #     actual_title = self.elementPresenceCheck(ByType="xpath", locator=self.title)
    #     texts = []
    #     for matched_element in actual_title:
    #         text = matched_element.text
    #         texts.append(text)
    #     if nextIcon is not False:
    #         self.ElementClick(next, "id")
    #         title = self.elementPresenceCheck(By.XPATH, locator=self.title)
    #         for ele in title:
    #             text_value = ele.text
    #             texts.append(text_value)
    #     texts = list(set(texts))
    #     # print("title", texts)
    #     return texts

    def verify_testedParty_title(self):
        self.waitForElement(self.title, locatorType="xpath")
        actual_title = self.elementPresenceCheck(ByType="xpath", locator=self.title)
        texts = []
        for matched_element in actual_title:
            text = matched_element.text
            texts.append(text)
            print(text)
        return texts

    def enter_FE_details_dev(self, count, fe_sample_id, fe_sample_dt, fe_firstname, fe_lastname, inp_channel, fe_dob,
                             fe_race, fe_ret_race, fe_cdt, inp_fe_tracking, retail_fe_dob, retail_fe_cdt,
                             retail_fe_tracking):
        if DEV or TEST:
            self.send_FE_sampleId_dev(count, fe_sample_id)
        else:
            self.send_FE_sample_id(count, fe_sample_id)
        self.click_FE_sample_dt(count, fe_sample_dt)
        self.send_FE_firstname(count, fe_firstname)
        self.send_FE_lastname(count, fe_lastname)
        self.enter_fe(count, inp_channel, fe_dob, fe_race, fe_ret_race, fe_cdt, inp_fe_tracking, retail_fe_dob,
                      retail_fe_cdt,
                      retail_fe_tracking)

    def enter_fe(self, count, inp_channel, fe_dob, fe_race, fe_ret_race, fe_cdt, inp_fe_tracking, retail_fe_dob,
                 retail_fe_cdt,
                 retail_fe_tracking):
        if inp_channel == 'Government' or inp_channel == 'Corporate' or inp_channel == 'Media':
            self.click_af_dob(count, fe_dob)
            self.click_af_race(count, fe_race)
            self.click_af_col_date(count, fe_cdt)
            self.send_af_tracking(count, inp_fe_tracking)
        elif inp_channel == 'Retail':
            # self.click_retail_af_dob(count, retail_fe_dob)
            self.click_retail_af_race(count, fe_ret_race)
            # self.click_retail_af_col_date(count, retail_fe_cdt)
            self.send_retail_af_tracking(count, retail_fe_tracking)

    # def send_FE_sample_id(self, count):
    #     sampleID = self.sample_id + str(count)
    #     self.waitForElement(sampleID, "id")
    #     self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
    #     self.waitForElement(sampleID, "id")
    #     self.sendKeys(self.getSample_id()[2], sampleID, "id")
    #     self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
    #     actual = self.verifytoaster_msg_success()
    #     self.utiles.hard_assertion("Success", actual, "sample id of mother is not entered")

    def send_FE_sampleId_dev(self, count, fe_id):
        sampleID = self.sample_id + str(count)
        self.waitForElement(sampleID, "id")
        self.webScroll(self.scroll_view_element(sampleID, locatorType="id"))
        self.waitForElement(sampleID, "id")
        self.sendKeys(self.utiles.strip_WhiteSpace(fe_id), sampleID, locatorType="id")
        self.driver.find_element(By.ID, sampleID).send_keys(Keys.ENTER)
        actual = self.verify_sample_is_valid()
        self.utiles.assertionTrue(actual, "Error occurs while entering the AF sample id" + fe_id)

    def click_FE_sample_dt(self, count, af_sample_dt):
        ele = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[2]//td//button"
        if af_sample_dt is not None:
            self.waitForElement(ele, locatorType="xpath")
            self.webScroll(self.scroll_view_element(ele, locatorType="xpath"))
            self.waitForElement(ele, locatorType="xpath")
            self.select_date_from_calender(af_sample_dt, ele, locatorType="xpath")
        else:
            pass

    def send_FE_firstname(self, count, af_firstname):
        FName = self.firstname + str(count)
        fname = self.getElement(FName, "id")
        if fname.is_enabled():
            if af_firstname is not None:
                self.waitForElement(FName, "id")
                self.webScroll(self.scroll_view_element(FName, locatorType="id"))
                self.waitForElement(FName, locatorType="id")
                self.sendKeys(af_firstname, FName, locatorType="id")
                self.commonTab_close()
            else:
                pass
        else:
            pass

    def send_FE_lastname(self, count, af_lastname):
        lastname = self.lastname + str(count)
        lname = self.getElement(lastname, "id")
        if lname.is_enabled():
            if af_lastname is not None:
                self.waitForElement(lastname, "id")
                self.webScroll(self.scroll_view_element(lastname, locatorType="id"))
                self.waitForElement(lastname, locatorType="id")
                self.sendKeys(af_lastname, lastname, locatorType="id")
                self.commonTab_close()
            else:
                pass
        else:
            pass

    def getdeliveryModeText(self):
        self.waitForElement(self.deliveryMode_text, "xpath")
        deliveryMethod = self.isElementTextPresent(self.deliveryMode_text, "xpath")
        return deliveryMethod

    def changeMLoverTrio(self, new_case_def):
        time.sleep(1)
        self.click_edit()
        self.click_case_definition()
        time.sleep(1)
        self.case_selection(new_case_def)

    def click_OnlineSetUpToggle(self):
        self.waitForElement(self.setUp_bt, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.setUp_bt, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def click_securityQuestion_bt(self):
        self.waitForElement(self.securityQuestion_bt, locatorType="xpath")
        self.ElementClick(self.securityQuestion_bt, locatorType="xpath")

    def select_securityQuestion(self):
        self.waitForElement(self.securityQuestion_li, locatorType="xpath")
        self.ElementClick(self.securityQuestion_li, locatorType="xpath")

    def click_onlinesetupConfirm(self):
        self.waitForElement(self.onlineSetUp_confirm, locatorType="id")
        self.ElementClick(self.onlineSetUp_confirm, locatorType="id")
        self.waitForElementPresent(self.loader, locatorType="xpath")

    def send_securityEmail(self, inp_email):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        if inp_email is not None:
            self.waitForElement(self.onlineSetUp_email, locatorType="xpath")
            self.sendKeys(inp_email, self.onlineSetUp_email, locatorType="xpath")
        else:
            pass

    def send_securityPassword(self, inp_password):
        if inp_password is not None:
            self.waitForElement(self.onlineSetUp_password, locatorType="xpath")
            self.sendKeys(inp_password, self.onlineSetUp_password, locatorType="xpath")
        else:
            pass

    def send_securityAnswer(self, inp_ans):
        if inp_ans is not None:
            self.waitForElement(self.securityAnswer, locatorType="xpath")
            self.sendKeys(inp_ans, self.securityAnswer, locatorType="xpath")
        else:
            pass

    def onlineSetupVerification(self):
        self.waitForElementPresent(self.loader, "xpath")
        self.waitForElement(self.onlineSetup_verify, "xpath")
        setupOnline = self.isElementTextPresent(self.onlineSetup_verify, "xpath")
        return setupOnline.strip()

    def MakeonlineSetup(self, Semail="demo@feathersoft.com", Spassword="123456", Sans="answer"):
        if DEV or TEST:
            self.click_OnlineSetUpToggle()
            time.sleep(1)
            self.send_securityEmail(Semail)
            self.send_securityPassword(Spassword)
            self.click_securityQuestion_bt()
            self.select_securityQuestion()
            self.send_securityAnswer(Sans)
            self.click_onlinesetupConfirm()
        else:
            pass
            print("Online setup cannot be enabled in local")

    def reviewflagTextPresence(self):
        self.waitForElement(self.review_flag, "xpath")
        review = self.isElementTextPresent(self.review_flag, "xpath")
        return review

    def click_changeReqReviewStatus_chckBox(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.changeReviewStatus_checkbox, "xpath")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.changeReviewStatus_checkbox, "xpath")

    def click_caseStatusChange_chckbox(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.changeCaseStatus_checkbox, "xpath")
        # self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.changeCaseStatus_checkbox, "xpath")

    def click_changeUpdate_bt(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.changeUpdate_bt, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.ElementClick(self.changeUpdate_bt, "id")

    def click_changeStatus(self):
        self.waitForElement(self.changeStatus_bt, locatorType="xpath")
        self.ElementClick(self.changeStatus_bt, locatorType="xpath")

    def statusType_selection(self, inp_status_type):
        if inp_status_type is not None:
            search_test_list = self.elementPresenceCheck(ByType=By.XPATH, locator=self.changeStatus_li)
            test_type_sel = self.utiles.find_dropdown_select(search_test_list, inp_status_type)
            if test_type_sel is not False:
                test_type_sel.click()
            else:
                self.log.info("input is False")
        else:
            self.log.info("Input is None")

    def change_reviewStatus(self, statusType):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_update()
        self.click_skip()
        if LOCAL:
            self.click_yes()
        self.click_changeReqReviewStatus_chckBox()
        self.click_caseStatusChange_chckbox()
        self.click_changeStatus()
        time.sleep(2)
        self.statusType_selection(statusType)
        self.click_changeUpdate_bt()

    def QCRenewStatusVerify(self):
        self.waitForElement(self.newCase_status, "id")
        self.waitForElementPresent(self.loader, locatorType="xpath")
        status_text = self.isElementTextPresent(self.newCase_status, locatorType="id")
        print(status_text)
        return status_text

    def click_deliveryBy_email(self):
        self.waitForElement(self.deliveryByEmail, locatorType="xpath")
        self.ElementClick(self.deliveryByEmail, locatorType="xpath")

    def click_deliveryBy_fax(self):
        self.waitForElement(self.deliveryByFax, locatorType="xpath")
        self.ElementClick(self.deliveryByFax, locatorType="xpath")

    def choose_deliveryMode(self, inp_mode):
        if inp_mode == "Courier - Next Day Delivery":
            self.click_delivery_mode()
        elif inp_mode == "Standard Mail":
            self.click_standardMail_mode()
        elif inp_mode == "Email":
            self.click_deliveryBy_email()
        elif inp_mode == "Fax":
            self.click_deliveryBy_fax()

    def click_testedPartyinfoClose(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        ele_present = self.isElementPresent(self.testedPartyInfo_CloseBt, locatorType="xpath")
        if ele_present is not False:
            self.ElementClick(self.testedPartyInfo_CloseBt, locatorType="xpath")
        else:
            pass

    def ML_over_Trio(self, M_sample_id, m_sample_dt, m_firstname, m_lastname, m_dob,
                     m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt, retail_m_tracking):
        self.webScroll(self.scroll_view_element(self.title, locatorType="xpath"))
        title_list = self.verify_testedParty_title()
        self.EditedPartyDetails(title_list[0], M_sample_id, m_sample_dt, m_firstname, m_lastname,
                                m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob,
                                retail_m_cdt, retail_m_tracking)

    def EditedPartyDetails(self, identifier, M_sample_id, m_sample_dt, m_firstname, m_lastname,
                           m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt,
                           retail_m_tracking):
        if identifier == "M" or identifier == "AM":
            self.enter_Mother_details_edited(M_sample_id, m_sample_dt, m_firstname, m_lastname,
                                             m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob,
                                             retail_m_cdt, retail_m_tracking)

    def send_sample_id_edited(self):
        sampleID = "//div[@class='right-table']//table[1]//tbody//tr[2]//td//input"
        self.waitForElement(sampleID, "xpath")
        self.webScroll(self.scroll_view_element(sampleID, locatorType="xpath"))
        self.waitForElement(sampleID, "xpath")
        self.sendKeys(self.getSample_id()[0], sampleID, "xpath")
        self.driver.find_element(By.XPATH, sampleID).send_keys(Keys.ENTER)
        actual = self.verifytoaster_msg_success()
        self.utiles.hard_assertion("Success", actual, "sample id of mother is not entered")

    def send_sampleId_dev_edited(self, m_id):
        sampleID = "//div[@class='right-table ng-star-inserted']//table[1]//tbody//tr[2]//td//input"
        self.waitForElement(sampleID, "xpath")
        self.webScroll(self.scroll_view_element(sampleID, locatorType="xpath"))
        self.waitForElement(sampleID, "xpath")
        self.sendKeys(self.utiles.strip_WhiteSpace(m_id), sampleID, locatorType="xpath")
        self.driver.find_element(By.XPATH, sampleID).send_keys(Keys.ENTER)
        # actual = self.verifytoaster_msg_success()
        actual = self.verify_sample_is_valid()
        self.utiles.assertionTrue(actual, "Error occurs while entering the  Mother sample id " + m_id)

    def click_sample_dt_edited(self, c_sample_dt):
        # sampleRcvd = "sampleReceivedOndatePicker"
        sampleRcvd = "//tbody//mat-datepicker-toggle[@id='sampleReceivedOndatePicker0']//button"
        # ele = sampleRcvd + str(count)
        # ele = "//div[@class='right-table']//table[" + str(count + 1) + "]//tbody//tr[3]//td//button"
        if c_sample_dt is not None:
            print(c_sample_dt)
            self.waitForElement(sampleRcvd, locatorType="xpath")
            # self.webScroll(self.scroll_view_element(sampleRcvd, locatorType="xpath"))
            self.waitForElement(sampleRcvd, locatorType="xpath")
            self.select_date_from_calender(c_sample_dt, sampleRcvd, locatorType="xpath")
        else:
            pass

    def send_firstname_edited(self, af_firstname):
        Fname = "//*[@class='right-table ng-star-inserted']//table[1]/tbody[1]/tr[6]/td[1]/input"
        FName = self.getElement(Fname, "xpath")
        if FName.is_enabled():
            if af_firstname is not None:
                self.waitForElement(Fname, "xpath")
                self.webScroll(self.scroll_view_element(Fname, locatorType="xpath"))
                self.waitForElement(Fname, locatorType="xpath")
                self.sendKeys(af_firstname, Fname, locatorType="xpath")
                self.commonTab_close()
            else:
                pass
        else:
            pass

    def send_lastname_edited(self, af_lastname):
        Slastname = "//*[@class='right-table ng-star-inserted']//table[1]/tbody[1]/tr[8]/td[1]/input"
        lname = self.getElement(Slastname, "xpath")
        if lname.is_enabled():
            if af_lastname is not None:
                self.waitForElement(Slastname, "xpath")
                self.webScroll(self.scroll_view_element(Slastname, locatorType="xpath"))
                self.waitForElement(Slastname, locatorType="xpath")
                self.sendKeys(af_lastname, Slastname, locatorType="xpath")
                self.commonTab_close()
            else:
                pass
        else:
            pass

    def click_col_date_edited(self, count, af_cdt):
        colbt = "collectionDatedatePicker"
        col_date = colbt + str(count)
        if af_cdt is not None:
            self.waitForElement(col_date, "id")
            self.webScroll(self.scroll_view_element(col_date, locatorType="id"))
            self.waitForElement(col_date, "id")
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(af_cdt, col_date, locatorType="id")
        else:
            pass

    def click_dob_edited(self, count, m_dob):
        dobtBt = "dobdatePicker"
        dob = dobtBt + str(count)
        if m_dob is not None:
            self.waitForElement(dob, "id")
            self.webScroll(self.scroll_view_element(dob, locatorType="id"))
            self.waitForElement(dob, "id")
            self.select_date_from_calender(m_dob, dob, locatorType="id")
            self.commonTab_close()
        else:
            pass

    def click_retail_dob_edited(self, retail_m_dob):
        retail_dob = "//div[@class='right-table ng-star-inserted']//table[1]//tbody//tr[11]//td//button"
        if retail_m_dob is not None:
            self.waitForElement(retail_dob)
            self.webScroll(self.scroll_view_element(retail_dob, locatorType="xpath"))
            self.waitForElement(retail_dob)
            self.select_date_from_calender(retail_m_dob, retail_dob, locatorType="xpath")
        else:
            pass

    def click_retail_col_date_edited(self, retail_m_cdt):
        retail_m = "//div[@class='right-table ng-star-inserted']//table[1]//tbody//tr[13]//td//button"
        if retail_m_cdt is not None:
            self.waitForElement(retail_m)
            self.webScroll(self.scroll_view_element(retail_m, locatorType="xpath"))
            self.waitForElement(retail_m)
            self.waitForElementPresent(self.loader, locatorType="xpath")
            self.select_date_from_calender(retail_m_cdt, retail_m, locatorType="xpath")
        else:
            pass

    def click_retail_race_edited(self, inp_ret_race_m):
        race = "//td[1]//app-single-select[@uid='raceId']//div//button"
        # race = self.common_race + str(count)
        if inp_ret_race_m is not False:
            self.waitForElement(race, "xpath")
            self.webScroll(self.scroll_view_element(race, locatorType="xpath"))
            self.waitForElement(race, "xpath")
            self.ElementClick(race, "xpath")
            self.retail_raceEdited(inp_ret_race_m)
        else:
            self.log.info("input is none")

    def enter_Mother_details_edited(self, M_sample_id, m_sample_dt, m_firstname, m_lastname,
                                    m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob, retail_m_cdt,
                                    retail_m_tracking):
        if DEV or TEST:
            self.send_sampleId_dev_edited(M_sample_id)
        else:
            self.send_sample_id_edited()
        time.sleep(2)
        self.click_sample_dt_edited(m_sample_dt)
        self.send_firstname_edited(m_firstname)
        self.send_lastname_edited(m_lastname)
        time.sleep(2)
        self.enter_mEdited(m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob,
                           retail_m_cdt, retail_m_tracking)

    def enter_mEdited(self, m_dob, m_race, m_ret_race, m_cdt, inp_m_tracking, retail_m_dob,
                      retail_m_cdt, retail_m_tracking):
        # if inp_channel == 'Government' or inp_channel == 'Corporate' or inp_channel == 'Media':
        #     self.click_dob_edited(count, m_dob)
        #     self.click_m_race(count, m_race)
        #     self.click_col_date_edited(count, m_cdt)
        #     self.send_m_tracking(count, inp_m_tracking)
        # elif inp_channel == 'Retail':
        self.click_retail_dob_edited(retail_m_dob)
        self.click_retail_race_edited(m_ret_race)
        # self.click_retail_col_date_edited(retail_m_cdt)
        self.send_retail_tracking_edited(retail_m_tracking)

    def retail_race(self, inp_ret_race):
        retail_race_list = "//div[@class='right-table']//table[1]//tbody//tr[12]//td//app-single-select//ul//li//a"
        if inp_ret_race is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=retail_race_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_ret_race)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def retail_raceEdited(self, inp_ret_race):
        retail_race_list = "//div[@class='right-table ng-star-inserted']//table[1]//tbody//tr[12]//td//app-single-select//ul//li//a"
        if inp_ret_race is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=retail_race_list)
            race_sel = self.utiles.find_dropdown_select(search_race_list, inp_ret_race)
            if race_sel is not False:
                race_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def send_retail_tracking_edited(self, retail_m_tracking):
        retail_tra_m = "//div[@class='right-table ng-star-inserted']//table[1]//tbody//tr[13]//td//input"
        if retail_m_tracking is not None:
            self.waitForElement(retail_tra_m)
            self.webScroll(self.scroll_view_element(retail_tra_m, locatorType="xpath"))
            self.waitForElement(retail_tra_m)
            self.sendKeys(retail_m_tracking, retail_tra_m)
            self.driver.find_element(By.XPATH, retail_tra_m).send_keys(Keys.ENTER)
        else:
            pass

    def clickTestedParty_C(self):
        self.waitForElement(self.copyFrom_child)
        self.ElementClick(self.copyFrom_child)

    def clickTestedParty_AF(self):
        self.waitForElement(self.copyFrom_af)
        self.ElementClick(self.copyFrom_af)

    def chooseTestedParty_AF(self):
        time.sleep(3)
        self.waitForElement(self.copyFrom_AFlist)
        self.ElementClick(self.copyFrom_AFlist)

    def chooseTestedParty_C(self):
        self.waitForElement(self.copyFrom_childlist)
        self.ElementClick(self.copyFrom_childlist)

    def TP_inpName_c(self):
        self.waitForElement(self.tpName_c, "xpath")
        inp_name = self.isElementTextPresent(self.tpName_c, "xpath")
        print(inp_name)

    def TP_inpName_af(self):
        self.waitForElement(self.tpName_af, "xpath")
        inp_name = self.isElementTextPresent(self.tpName_af, "xpath")
        print(inp_name)

    def testedparty_copyInfo(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.webScroll(self.scroll_view_element(self.edit_bt, locatorType="id"))
        self.click_edit()
        self.click_case_definition()
        time.sleep(1)
        self.case_selection("Paternity Trio")
        time.sleep(1)

    def childNameInTable(self):
        child = "//div[@class='right-table right-table-view']//table[1]//tbody//tr[6]//td"
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(child, locatorType="xpath", timeout=400)
        c_name = self.isElementTextPresent(child, locatorType="xpath")
        print(c_name)

    def AFNameInTable(self):
        AF = "//div[@class='right-table right-table-view']//table[2]//tbody//tr[6]//td"
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(AF, locatorType="xpath", timeout=400)
        af_name = self.isElementTextPresent(AF, locatorType="xpath")
        print(af_name)

    def click_confirmTestedParty(self):
        confirm = "//div//button[normalize-space()='Confirm']"
        self.waitForElement(confirm)
        self.ElementClick(confirm)

    def getKitBarCode(self):
        s = self.utiles.unique_kitbarcode()
        return "K-" + s[0], "K-" + s[1]

    def click_kitBarDropDown(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.waitForElement(self.KitBarcode_dropdown, "id")
        self.ElementClick(self.KitBarcode_dropdown, "id")

    def send_kitbarcodeForRetail(self):
        self.waitForElement(self.barcode, "id")
        self.webScroll(self.scroll_view_element(self.barcode, locatorType="id"))
        self.waitForElement(self.barcode, "id")
        x = self.utiles.strip_WhiteSpace(self.getKitBarCode()[0])
        self.sendKeys(x, self.barcode, "id")
        self.driver.find_element(By.ID, self.barcode).send_keys(Keys.ENTER)
        self.waitForElementPresent(self.loader, locatorType="xpath")
        self.click_kitBarDropDown()
        self.waitForElement(self.addExtraKitBarCode, "id")
        y = self.utiles.strip_WhiteSpace(self.getKitBarCode()[1])
        self.sendKeys(y, self.addExtraKitBarCode, "id")
        self.driver.find_element(By.ID, self.addExtraKitBarCode).send_keys(Keys.ENTER)
        self.click_kitBarDropDown()
        time.sleep(2)

    def getAllKitBarCode(self):
        self.waitForElement(self.allbarcode, locatorType="xpath")
        barcode = self.isElementTextPresent(self.allbarcode, locatorType="xpath")
        return barcode

    def YesBt_verification(self):
        self.waitForElement(self.yes, locatorType="id")
        yes_verify = self.isElementPresent(self.yes, locatorType="id")
        return yes_verify

    def click_gender(self, count):
        gender = "//div[@class='right-table ng-star-inserted']//table[" + str(count + 1) + "]//tbody//tr[10]"
        if gender is not False:
            self.waitForElement(gender, "xpath")
            self.webScroll(self.scroll_view_element(gender, locatorType="xpath"))
            self.waitForElement(gender, "xpath")
            self.ElementClick(gender, "xpath")
            self.gender_sel(count, "Select")
        else:
            self.log.info("input is none")

    def gender_sel(self, count, gender_sel):
        gender_list = "//div[@class='right-table ng-star-inserted']//table[" + str(
            count + 1) + "]//tbody//tr[10]//td//app-single-select//ul//li//a"
        if gender_sel is not None:
            search_race_list = self.elementPresenceCheck(ByType=By.XPATH, locator=gender_list)
            g_sel = self.utiles.find_dropdown_select(search_race_list, gender_sel)
            if g_sel is not False:
                g_sel.click()
            else:
                self.log.info("input is none")
        else:
            self.log.info("input is none")

    def deslect_gender(self):
        sample_detailBt = "caseeditsampledetailsBtn"
        self.webScroll(self.scroll_view_element(sample_detailBt, locatorType="id"))
        title_list = self.verify_testedParty_title()
        if self.getEditedTable_count() != 0:
            for k in range(0, self.getEditedTable_count()):
                self.gFunc(k, title_list[k])

    def gFunc(self, count, identifier):
        if identifier == "M" or identifier == "AM" or identifier == "AF" or identifier == "AT":
            self.click_gender(count)

    def getEditedTable_count(self):
        modified = "//div[@class='right-table ng-star-inserted']//table"
        count = self.elementPresenceCheck(ByType="xpath", locator=modified)
        x = len(count)
        print(len(count))
        return x

    def StatusCheckinPage(self):
        self.waitForElement(self.closed_case_status, locatorType="xpath")
        status = self.isElementTextPresent(self.closed_case_status, locatorType="xpath")
        # ver_cs = self.utiles.strip_string(closed_status)
        return status

    def verify_accessioning(self):
        self.waitForElementPresent(self.loader, locatorType="xpath")
        status = False
        element = self.waitForElement(self.status_filter_button, locatorType="id")
        if element is not None:
            ele_text = element.text.strip()
            if ele_text == "Accessioning Complete":
                status = True
            else:
                status = False
        else:
            print("Element is None")
        return status

    def click_deliveryPrefEdit(self):
        self.waitForElement(self.deliveryPrefEditBt, "xpath")
        self.ElementClick(self.deliveryPrefEditBt, "xpath")

    def disable_checkBox(self):
        self.waitForElement(self.onlineSetUp_disable_checkbox, "xpath")
        self.ElementClick(self.onlineSetUp_disable_checkbox, "xpath")

    def onlineSetUp_disableOption(self):
        # self.click_deliveryPrefEdit()
        self.disable_checkBox()
        self.click_deli_pref_save()

    def editMiddleName(self, *mid_name):
        for i, name in enumerate(mid_name):
            self.getMiddleName(i, name)

    def getMiddleName(self, k, mid):
        mid_name = "//div[@class='right-table ng-star-inserted']//table[" + str(k + 1) + \
                   "]//tbody//tr[7]//td//input"
        self.waitForElement(mid_name, "xpath", timeout=100)
        print(mid)
        self.webScroll(self.scroll_view_element(mid_name, "xpath"))
        self.sendKeys(mid, mid_name, "xpath")

    def verifyEditedMiddleName(self):
        temp = []
        mid = ""
        title_list = self.verify_testedParty_title()
        for k in range(0, self.getModifiedTable_count()):
            if title_list[k] == "M" or "AM":
                mid = self.verifyMiddleName(k)
            elif title_list[k] == "C":
                mid = self.verifyMiddleName(k)
            elif title_list[k] == "AF" or "FE":
                mid = self.verifyMiddleName(k)
            temp.append(mid)
        return temp

    def verifyMiddleName(self, k):
        mid_name = "//table[@class='table ng-star-inserted'][" + str(k + 1) + "]//tbody//tr[7]//td"
        self.waitForElement(mid_name, "xpath")
        self.webScroll(self.scroll_view_element(mid_name, "xpath"))
        mid = self.isElementTextPresent(mid_name, "xpath")
        return mid
