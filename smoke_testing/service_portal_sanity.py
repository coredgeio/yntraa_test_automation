import logging
import pytest
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from pages.resources.networking.ip_address_page import *
from test_helper.testdata.compute_testdata import ComputeTextData
from test_helper.testdata.sanity_testdata import SanityTextData
from pages.sanity_service_provider import *
import asyncio
from selenium.webdriver.common.keys import Keys
import pyautogui

@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "shubh@yopmail.com",
        #"username": "atul159@yopmail.com",
        "password": "India@143"
    }

"""Verify the header on CCP home page - "Enabling Possibilities. Empowering Ideas." """
@pytest.mark.testrail(65436)
def test_Verify_the_header_on_Yntraa_home_page(page):
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()
    yntraa_page_heading = page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])
    page_heading = yntraa_page_heading.inner_text()
    print(page_heading)
    assert page_heading == SanityTextData.yntraa_header, "User could not be navigated to yntraa page header!!"
    logging.info("User successfully navigated to yntraa homepage  screen!")

"""Verify the description on CCP home page """
@pytest.mark.testrail(65494)
def test_verify_description_on_yntraa_home_page(page):
    expect(page.get_by_test_id(locators['YNTRAA_DISCRIPTION_PAGE'])).to_be_visible()
    yntraa_discription_element = page.get_by_test_id(locators['YNTRAA_DISCRIPTION_PAGE'])
    yntraa_description_value = yntraa_discription_element.inner_text()
    assert yntraa_description_value == SanityTextData.yntraa_discription, f"The yntraa page description value - {yntraa_description_value}, is different than expected!"
    logging.info("Description on yntraa page screen is correct!")

"""Verify the UI for logged in screen for -Logo, Project, DDoS, Search Bar, Create button, Region, Wallet Balance, My Organisation, User Profile Section, Storage, Networking, Security, Automation, My Edge Site, CaaS, Managed Database, Support, etc."""
@pytest.mark.testrail(65592)
def test_verify_the_UI_for_logged_yntaa_screen(page):
    expected_elements = [
        'YNTRAA_HEADER_PAGE', 'YNTRAA_LOGO', 'YNTRAA_PROJECT', 'YNTRAA_SEARCH_BAR',
        'YNTRAA_REGION', 'YNTRAA_WALLET_BALANCE', 'YNTRAA_ORGNIZATION', 'YNTRAA_USERPROFILE',
        'STORAGE_TAB', 'NETWORKING_TAB', 'SECURITY_TAB', 'AUTOMATION_TAB', 'EDGE_SIDE_TAB',
        'CAAS_TAB', 'MANAGED_DATABASE_TAB', 'SUPPORT_TAB'
    ]  # 'YNTRAA_CREATE_BTN',

    for element_id in expected_elements:
        element = page.get_by_test_id(locators[element_id])
        assert element.is_visible(), f"{element_id} is not visible on the page"

"""Verify logged in screen for Information Cards - Create Compute Instance, Deploy your Applications, Create Managed Database, Explore Yntraa Platform"""
@pytest.mark.testrail(65437)
def test_logged_in_screen_for_Information_Cards(page):
    expect(page.get_by_test_id(locators['COMPUTE_OPERATION'])).to_be_visible()
    compute_operation_element = page.get_by_test_id(locators['COMPUTE_OPERATION'])
    compute_operation_text = compute_operation_element.inner_text()
    assert compute_operation_text == "Create Compute Instance"
    expect(page.get_by_test_id(locators['DEPLOY_OPERATION'])).to_be_visible()
    deploy_operation_element = page.get_by_test_id(locators['DEPLOY_OPERATION'])
    deploy_operation_text = deploy_operation_element.inner_text()
    assert deploy_operation_text == "Deploy your Applications"
    expect(page.get_by_test_id(locators['DATABASE_OPERATION'])).to_be_visible()
    database_operation_element = page.get_by_test_id(locators['DATABASE_OPERATION'])
    database_operation_text = database_operation_element.inner_text()
    assert database_operation_text == "Create Managed Database"
    expect(page.get_by_test_id(locators['PLATFORM_OPERATION'])).to_be_visible()
    platform_operation_element = page.get_by_test_id(locators['PLATFORM_OPERATION'])
    platform_operation_text = platform_operation_element.inner_text()
    assert platform_operation_text == "Explore Yntraa Platform"

"""Verify logged in screen for Quick Links -Create Project, Upgrade Quota Request, Create Key Pair, Create Virtual Machine, Create Kubernetes Cluster, Create Autoscaling Group, Create Namespace, Create Volume, Create Bucket, Create File System, Create"""
@pytest.mark.testrail(65593)
def test_verify_logged_screen_for_quick_links(page):
    expect(page.get_by_test_id(locators['QUICK_LINK'])).to_be_visible()
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["YNTRAA_QUICK_LINK"]}"]')
    expected_text = "Create Project, Upgrade Quota Request, Create Key Pair, Create Virtual Machine, Create Kubernetes Cluster, Create Autoscaling Group, Create Namespace, Create Volume, Create Bucket, Create File System, Create Container, Create Network, Create Security Group, Create Load Balancer, Create Firewall Rule, Create VPNaaS, Upload SSL Certificate, Create Stack, Create Database Cluster, Raise Ticket"
    actual_texts = []
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        print(element_text)
        actual_texts.append(element_text)
    actual_text = ", ".join(actual_texts)
    assert expected_text == actual_text, f"Expected text: '{expected_text}', Actual text: '{actual_text}'"

"""Verify logged in screen for Learn More - Product Overviews, Quick Start Guide, How Tos, API Documentation"""
@pytest.mark.testrail(65438)
def test_verify_Logged_screen_for_learn_more(page):
    expect(page.get_by_test_id(locators['LEARN_MORE_TAB'])).to_be_visible()
    learn_more_value = page.get_by_test_id(locators['LEARN_MORE_TAB'])
    text = learn_more_value.inner_text()
    assert text == "Learn More"
    expected_text = "Product Overviews,Quick Start Guide,How Tos,API Documentation"
    expected_values = expected_text.split(",")
    for value in expected_values:
        locator = f"//h6[contains(text(), '{value.strip()}')]"
        element_exists = page.query_selector(locator) is not None
        assert element_exists, f"Expected value '{value.strip()}' not found in Learn More field text"

"""Verify the Global search bar functionality """
@pytest.mark.testrail(65439)
def test_Verify_the_Global_search_bar_functionality(page):
    expect(page.get_by_test_id(locators['YNTRAA_SEARCH_BAR'])).to_be_visible()
    input_box_locator = page.locator(locators['GLOBAL_BAR_SERACH_FIELD'])
    expect(input_box_locator).to_be_visible()
    input_box_text = input_box_locator.inner_text()
    assert input_box_text == "", "Input box text is not empty"
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['GLOBAL_BAR_SEARCH'], "Tejas Compute")
    page.get_by_test_id("btn-search-tejas-compute").click()
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

"""Create button - Create Resources popup - Verify the Projects option """
@pytest.mark.testrail(65440)
def test_verify_create_button(page):
    page.get_by_test_id("btn-global-create").is_visible()
    page.locator(locators['BTN_CREATEA']).click()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    print(create_resource_heading)
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['PROJECT_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    print(Project_option_text)
    assert Project_option_text == "Projects"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()

@pytest.mark.testrail(65441)
def test_verify_create_button_Quota_service(page):
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    print(create_resource_heading)
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['QUOTA_SERVICE_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    print(Project_option_text)
    assert Project_option_text == "Quota Service"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()

@pytest.mark.testrail(65442)
def test_verify_create_button_Compute(page):
    page.get_by_test_id("btn-global-create").is_visible()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['COMPUTE_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Compute"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()


@pytest.mark.testrail(65443)
def test_verify_create_button_Storage(page):
    page.get_by_test_id("btn-global-create").is_visible()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['STORAGE_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Storage"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()


@pytest.mark.testrail(65444)
def test_verify_create_button_Networking(page):
    page.get_by_test_id("btn-global-create").is_visible()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['NETWORKING_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Networking"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()

@pytest.mark.testrail(65445)
def test_verify_create_button_Securitoption(page):
    page.get_by_test_id("btn-global-create").is_visible()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['SECURITY_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Security"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()

@pytest.mark.testrail(65446)
def test_verify_create_button_Automation_option(page):
    page.get_by_test_id("btn-global-create").is_visible()

    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['AUTOMATION_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Automation"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()

@pytest.mark.testrail(65447)
def test_verify_create_button_Managed_Database_option(page):
    page.get_by_test_id("btn-global-create").is_visible()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['MANAGEDATABSE_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Managed Database"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()


@pytest.mark.testrail(65448)
def test_verify_create_button_Support_service(page):
    page.get_by_test_id("btn-global-create").is_visible()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['SUPPORT_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Support"
    expect(page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE'])).to_be_visible()
    # page.get_by_test_id(locators['CREATE_BTN_UNDER_CREATE_RESOURCE']).click()
    # page.wait_for_timeout(10000)

@pytest.mark.testrail(65449)
def test_verify_create_button_Verify_the_Search_Bar(page):
    #page.locator(locators['BTN_CREATEA']).click()
    page.locator(locators['SEARCH_FIELD_CREATE']).is_visible()
    input_box_locator = page.locator(locators['CREATEREASOURE_SEARCH'])
    expect(input_box_locator).to_be_visible()
    input_box_text = input_box_locator.inner_text()
    assert input_box_text == "", "Input box text is not empty"
    clear_and_fill_field(page, locators['SEARCH_FIELD_CREATE'], "Tejas Compute")
    page.locator(locators['SEARCH_VALUE']).is_visible()
    page.wait_for_timeout(1000)
    clear_and_fill_field(page, locators['SEARCH_FIELD_CREATE'], "")
    page.wait_for_timeout(1000)


@pytest.mark.testrail(65450)
def test_verify_create_button_Support_service(page):
    page.get_by_test_id("btn-global-create").is_visible()
    expect(page.get_by_test_id(locators['CREATE_RESOURCES'])).to_be_visible()
    create_resource_heading = page.get_by_test_id(locators['CREATE_RESOURCES']).inner_text()
    assert create_resource_heading == "Create Resources"
    ProjectOption = page.get_by_test_id(locators['SUPPORT_OPTION'])
    Project_option_text = ProjectOption.inner_text()
    assert Project_option_text == "Support"
    Project_option_text = ProjectOption.click()
    expect(page.get_by_test_id(locators['BTN_CREATE_TICKET'])).to_be_visible()
    page.get_by_test_id(locators['BTN_CREATE_TICKET']).click()
    expect(page.get_by_test_id(locators['HEADING_SUPPORT'])).to_be_visible()
    page.wait_for_timeout(10000)

    expect(page.locator(locators['TICKET_CATEGORY'])).to_be_visible()
    page.locator(locators['TICKET_CATEGORY']).click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="category-select-option"]')
    count = len(Dropdown_elements)
    other_option_found = False
    for index, element in enumerate(Dropdown_elements, start=1):
        element_text = element.inner_text()
        if "Other" in element_text:
            other_option_found = True
            element.click()
            print("Clicked on Other")
            break
    page.wait_for_timeout(TIMEOUT)

    page.locator(locators['TICKET_SUBCATEGORY']).click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="sub-category-select-option"]')
    count = len(Dropdown_elements)
    for index, element in enumerate(Dropdown_elements, start=1):
        element_text = element.inner_text()
        if "Other" in element_text:
            element.click()
            print("Clicked on Other")
            break
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['TICKET_SUBJECT'], "Unable to create VM")
    clear_and_fill_field(page, locators['TICKET_MESSAGE'], "Unable to create VM")

    expect(page.get_by_test_id(locators['TICKET_ATTCHED'])).to_be_visible()
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    page.get_by_test_id(locators['CONFIRMATION_TEXT']).click()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Ticket raised successfully."

@pytest.mark.testrail(65451)
def test_Verify_the_Region_dropdown(page):
    expect(page.get_by_test_id(locators['YNTRAA_REGION'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_REGION']).click()
    region_text = page.locator(locators['REGION_VALUE'])
    expect(region_text).to_be_visible()
    region_name =  region_text.inner_text()
    print(region_name)
    assert region_name != "", "Region_name is not empty"
    region_text.click()
    page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(65452)
def test_Verify_the_Wallet_Balance_dropdown(page):
    expect(page.get_by_test_id(locators['YNTRAA_WALLET_BALANCE'])).to_be_visible()
    wallet_balance_element = page.locator(locators['WALLET_AMOUNT'])
    expect(wallet_balance_element).to_be_visible()
    wallet_balance_text = wallet_balance_element.inner_text()
    print(wallet_balance_text)
    wallet_balance_value = float(wallet_balance_text[2:].replace(',', '')) if wallet_balance_text else 0
    print(wallet_balance_value)
    assert wallet_balance_value >= 0, f"Wallet balance is not greater than or equal to 0: {wallet_balance_value}"

@pytest.mark.testrail(65453)
def test_Verify_the_Organization_name(page):
    expect(page.get_by_test_id(locators['YNTRAA_ORGNIZATION'])).to_be_visible()
    organization_name_heading = page.locator(locators['ORGANIZATION_NAME'])
    expect(organization_name_heading).to_be_visible()
    organizationname =  organization_name_heading.inner_text()
    assert organizationname != "", "Organization_name is not empty"


@pytest.mark.testrail(65454)
def test_verify_the_notifications_all_unread(page):
    expect(page.get_by_test_id(locators['NOTIFICATION_ICON'])).to_be_visible()
    page.get_by_test_id(locators['NOTIFICATION_ICON']).click()
    expect(page.get_by_test_id(locators['TOGGLE_BTN'])).to_be_visible()
    page.get_by_test_id(locators['TOGGLE_BTN']).click()
    all_notifications = page.query_selector_all('.notification')
    # assert len(all_notifications) > 0, "No notifications found for All"
    expect(page.get_by_test_id(locators['TOGGLE_BTN_UNREAD'])).to_be_visible()
    page.get_by_test_id(locators['TOGGLE_BTN_UNREAD']).click()
    unread_notifications = page.query_selector_all('.notification.unread')
    page.get_by_test_id(locators['CLOSE_NOTIFICATION']).click()

@pytest.mark.testrail(65455)
def test_User_Profile_popup_Verify_the_user_name(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    expect(page.get_by_test_id(locators['PROFIFLE_IMAGE'])).to_be_visible()
    profile_name = page.get_by_test_id(locators['PROFILE_USENAME'])
    username = profile_name.inner_text()
    profile_email = page.get_by_test_id(locators['PROFILE_EMAIL'])
    email = profile_email.inner_text()
    assert username, "Username is not displayed"
    assert email, "Email is not displayed"



"""Verify the User Profile Popup - User Email ID with Copy to Clipboard Icon"""

@pytest.mark.testrail(65456)
def test_user_profile_popup_verify_user_email_with_copy_to_clipboard_icon(page):
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    copy_to_clipboard_button = page.get_by_test_id(locators['COPY_TO_CLIPBOARD_BUTTON'])
    expect(email_element).to_be_visible()
    expect(copy_to_clipboard_button).to_be_visible()
    copy_mail = page.get_by_test_id(locators['COPY_TO_CLIPBOARD_BUTTON']).click()
    print(copy_mail)

@pytest.mark.testrail(65457)
def test_User_Profile_popup_Verify_the_user_role_label(page):
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    user_role_label = page.get_by_test_id(locators['PROFIFLE_IMAGE'])
    expect(user_role_label).to_be_visible()
    label_name = user_role_label.inner_text()
    print("........", label_name)
    assert label_name != "", "User role label is not empty"



# @pytest.mark.testrail(65458) #65459
# def test_user_redirected_to_yotta_environment(page):
#     expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
#     page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
#     email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
#     expect(email_element).to_be_visible()
#     copy_to_clipboard_button = page.get_by_test_id(locators['ONE_TOTTA_BTN'])
#     expect(copy_to_clipboard_button).to_be_visible()
#     page.get_by_test_id(locators['ONE_TOTTA_BTN']).click()
#     new_page = page.context.pages[-1]
#     time.sleep(2)
#     page.wait_for_timeout(50000)
#     if new_page.locator(locators['YOTTA_SCREEN']).to_be_visible():
#         print("Validation passed: Element found on the new page")
#     else:
#         print("Validation failed: Element not found on the new page")

@pytest.mark.testrail(65460)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_Orders_Listing_page_upon_clicking_Orders(page):
    # page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    # page.wait_for_timeout(1000)
    order_element = page.locator(locators['OREDER_TAB'])
    expect(order_element).to_be_visible()
    page.locator(locators['OREDER_TAB']).click()
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['ORDER_HEADING'])).to_be_visible()
    order_list = page.query_selector_all(f'[data-testid="resource-name-link"]')
    orderlist_count = len(order_list)
    logging.info("count",orderlist_count)
    if orderlist_count > 0:
        order_list_id = order_list[0].inner_text()
        logging.info("first_order_listId", order_list_id)
    else:
        logging.info("order list are not available")

@pytest.mark.testrail(65461)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_Quota_service_screen_upon_clicking_Orders(page):
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.wait_for_timeout(1000)
    page.locator(locators['QUOTA_BTN']).click()
    expect(page.get_by_test_id(locators['QUOTA_SERVICE_HEADER'])).to_be_visible()
    expect(page.get_by_test_id(locators['QUOTA_CREATE_BTN'])).to_be_visible()
    page.wait_for_timeout(10000)

    quota_service_list = page.query_selector_all(f'[data-testid="resource-name-link"]')
    quota_service_list_count = len(quota_service_list)
    logging.info("count",quota_service_list_count)
    if quota_service_list_count > 0:
        request_id = quota_service_list[0].inner_text()
        logging.info("first_equest_Id", request_id)
    else:
        logging.info("quota service request id's are not available")

@pytest.mark.testrail(65462)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_Upgrade_Quota_Request_and_view_existing_Quota_Request_listing(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    page.locator(locators['QUOTA_BTN']).click()
    expect(page.get_by_test_id(locators['QUOTA_SERVICE_HEADER'])).to_be_visible()
    page.get_by_test_id(locators['QUOTA_CREATE_BTN']).click()
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['QUOTA_SERVICE_HEADER'])).to_be_visible()
    page.locator(locators['QUOTA_INCREASE_VM']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_text("Request Upgrade")).to_be_visible()
    # page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    # page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    # toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    # assert toast_text == "Quota requested successfully."
    # toast_text = page.locator(locators['REQUEST_STATUS']).inner_text()
    # assert toast_text == "Submitted for approval"
    # quota_service_list = page.query_selector_all(f'[data-testid="resource-name-link"]')
    # quota_service_list_count = len(quota_service_list)
    # logging.info("count",quota_service_list_count)
    # if quota_service_list_count > 0:
    #     request_id = quota_service_list[0].inner_text()
    #     logging.info("first_equest_Id", request_id)
    # else:
    #     logging.info("quota service request id's are not available")

@pytest.mark.testrail(65463)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_project_listing_page_upon_clicking_project(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.get_by_test_id(locators['PROJECT_TAB']).click()
    expect(page.get_by_test_id(locators['PROJECT_HEADING'])).to_be_visible()
    project_page_heading = page.get_by_test_id(locators['PROJECT_HEADING'])
    page_heading = project_page_heading.inner_text()
    print(page_heading)
    assert page_heading == "Projects"
    project_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    project_list_count = len(project_List_elements)
    logging.info(project_list_count)
    print(project_list_count)

@pytest.mark.testrail(65464)
def test_User_Profile_Popup_Projects_Verify_Projects_Screen(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.get_by_test_id(locators['PROJECT_TAB']).click()
    expect(page.get_by_test_id(locators['PROJECT_HEADING'])).to_be_visible()
    page.get_by_test_id(locators['PROJECT_CREATE_BTN']).click()
    expect(page.get_by_test_id(locators['PROJECT_CREATE_HEADING'])).to_be_visible()
    clear_and_fill_field(page, locators['INPUT_NAME'], MACHINE_NAME)
    page.wait_for_timeout(10000)
    page.locator(locators['DISCRIPTION_FIELD']).click()
    clear_and_fill_field(page, locators['DISCRIPTION_FIELD'], "External create project for the manage and group resources")
    project_name_text =page.get_by_test_id(locators['INPUT_PROJECT']).inner_text()
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert  toast_text == "Initializing your project."
    page.wait_for_timeout(10000)
    # project_name_created = page.locator(locators['CREATED_PROJECT_NAME']).inner_text()
    # assert project_name_created == project_name_text

@pytest.mark.testrail(65465)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_keypair_listing_page_upon_clicking_project(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.get_by_test_id(locators['KEYPAIR_TAB']).click()
    expect(page.get_by_test_id(locators['KEYPAIR_HEADING'])).to_be_visible()
    project_page_heading = page.get_by_test_id(locators['KEYPAIR_HEADING'])
    page_heading = project_page_heading.inner_text()
    print(page_heading)
    assert page_heading == "Key Pairs"

@pytest.mark.testrail(65466)
def test_User_Profile_Popup_Key_Pairs_Verify_Actions(page, create_reservePublicIP):
    page.wait_for_timeout(1000)
    yes_button_element = page.get_by_test_id(locators['CONFIRM_BUTTON'])
    assert yes_button_element.is_visible(), "Yes button is not visible."
    yes_button_element.click()
    ip_addressvalue = page.query_selector_all(f'[data-testid="resource-name-link"]')
    ip_count = len(ip_addressvalue)
    if ip_count > 0:
        ip_address = ip_addressvalue[0].inner_text()
        print(ip_address)

    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.get_by_test_id(locators['KEYPAIR_TAB']).click()
    expect(page.get_by_test_id(locators['KEYPAIR_HEADING'])).to_be_visible()

    page.get_by_test_id(locators['CREATE_KEY_PAIR_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    clear_and_fill_field(page, locators['INPUT_NAME'], MACHINE_NAME)
    project_name_text =page.get_by_test_id(locators['INPUT_PROJECT']).inner_text()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    page.wait_for_timeout(1000)
    page.get_by_test_id(locators['IMPORT_PUBLIC_KEY_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()

    clear_and_fill_field(page, locators['INPUT_NAME'], MACHINE_NAME)
    clear_and_fill_field(page, locators['PUBLICK_KEY_FIELD'], ip_address)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    page.wait_for_timeout(1000)
   # page.get_by_test_id(locators['CANCEL_BUTTON']).click()

@pytest.mark.testrail(65467)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_user_listing_page_upon_clicking_project(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.get_by_test_id(locators['USERS_TAB']).click()
    expect(page.get_by_test_id(locators['USER_HEADING'])).to_be_visible()
    user_page_heading = page.get_by_test_id(locators['USER_HEADING'])
    page_heading = user_page_heading.inner_text()
    print(page_heading)
    assert page_heading == "Users"

@pytest.mark.testrail(65468)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_user_listing_page_upon_clicking_project(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.get_by_test_id(locators['USERS_TAB']).click()

    expect(page.get_by_test_id(locators['USER_HEADING'])).to_be_visible()
    expect(page.get_by_test_id(locators['USER_ADD_MEMBER'])).to_be_visible()
    expected_texts= ["Users", "Roles"]
    check_visibility(page,expected_texts)
    page.get_by_test_id(locators['USER_ADD_MEMBER']).click()
    expect(page.get_by_test_id(locators['PROJECT_CREATE_HEADING'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    project_dropdown_element = page.locator(locators['ADD_PRPJECT_FIELD'])
    project_dropdown_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="project-select-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
    page.wait_for_timeout(TIMEOUT)

    role_dropdown_element = page.locator(locators['ROLE_FIELD'])
    role_dropdown_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="role-select-option"]')
    for index, element in enumerate(Dropdown_elements, start=1):
        element_text = element.inner_text()
        if "Project_user" in element_text:
            element.click()
            print("Clicked on Project_user")
            break

    page.get_by_test_id(locators['ROW_CHEACKBOX']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print(toast_text)
    assert toast_text == "Project assigned successfully."


@pytest.mark.testrail(65469)
def test_User_Profile_popup_Verify_that_user_is_redirected_to_the_update_password_page_upon_clicking_change_password(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    page.get_by_test_id(locators['CHANGE_PASS_TAB']).click()
    page.wait_for_timeout(10000)
    update_passowrd_field = page.locator(locators['UPDATE_PASSWORD'])
    expect(update_passowrd_field).to_be_visible()
    page.locator(locators['CANCEL_BUTTON_LOGIN']).click()
    page.wait_for_timeout(10000)
    #expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()
@pytest.mark.testrail(65470)
def test_user_logged_out_upon_clicking_logout_button(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    expect(page.get_by_text("Logout", exact=True)).to_be_visible()
    page.wait_for_timeout(2000)
    page.get_by_text("Logout").click()
    page.wait_for_timeout(4000)
    verify_to_login_byusing_rolebased_credentials(page)

@pytest.mark.testrail(65471)# 65472
def test_Compute_Verify_user_is_redirected_to_Compute_home_page(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    compute_header_element = page.get_by_test_id(locators['COMPUTE_HEADER'])
    compute_header_value = compute_header_element.inner_text()
    assert compute_header_value == ComputeTextData.compute_header, "User could not be navigated to Compute module!!"
    logging.info("User has successfully navigated to Compute module!")

@pytest.mark.testrail(65473)
def test_Compute_verify_compute_description_displayed_on_page(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_DESCRP'])).to_be_visible()
    compute_discription_element = page.get_by_test_id(locators['COMPUTE_DESCRP'])
    compute_description_value = compute_discription_element.inner_text()
    assert compute_description_value == ComputeTextData.compute_description, f"The compute description value - {compute_description_value}, is different than expected!"
    logging.info("Description on Compute home screen is correct!")


def check_visibility(page,expected_texts):
    visibility_status = {}
    for text in expected_texts:
        elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
        if elements:
            visibility_status[text] = True
        else:
            visibility_status[text] = False
    all_visible = all(visibility_status.values())
    for text, visible in visibility_status.items():
        print(f"{text} is {'visible' if visible else 'not visible'}")
    print("All texts are visible:", all_visible)


@pytest.mark.testrail(65474)
def test_verify_compute_screen_Tejascompute_sanpshot_Autoscale_serverless(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_DESCRP'])).to_be_visible()
    expected_texts= ComputeTextData. compute_header_section
    check_visibility(page,expected_texts)

@pytest.mark.testrail(65475)# 65476
def test_Storage_Verify_user_is_redirected_to_storage_home_page(page):
    perform_click_on_compute_resource(page, locators['STORAGE_TAB'])
    storage_header_element = page.get_by_test_id(locators['STORAGE_HEADING'])
    storage_header_value = storage_header_element.inner_text()
    assert storage_header_value == ComputeTextData.storage_header, "User could not be navigated to Storage module!!"
    logging.info("User has successfully navigated to Storage module!")

@pytest.mark.testrail(65477)
def test_storage_verify_storage_description_displayed_on_page(page):
    perform_click_on_compute_resource(page, locators['STORAGE_TAB'])
    expect(page.get_by_test_id(locators['STORAGE_DISCRIPTION'])).to_be_visible()
    discription_element = page.get_by_test_id(locators['STORAGE_DISCRIPTION'])
    description_value = discription_element.inner_text()
    assert description_value == ComputeTextData.storage_description, f"The storage description value - {description_value}, is different than expected!"
    logging.info("Description on storage home screen is correct!")

@pytest.mark.testrail(65478)
def test_verify_storage_screen_block_storage_volumesnapshot_allfunction(page):
    perform_click_on_compute_resource(page, locators['STORAGE_TAB'])
    expect(page.get_by_test_id(locators['STORAGE_DISCRIPTION'])).to_be_visible()
    page.wait_for_timeout(4000)

    storage_sections = page.query_selector_all(locators['STORAGE_SECTIONS'])
    expected_texts= ComputeTextData. storage_header_section
    visibility_status = {}
    for text in expected_texts:
        visibility_status[text] = any(text in element.inner_text() for element in storage_sections)
    for text, visible in visibility_status.items():
        print(f"{text} is {'visible' if visible else 'not visible'}")
    all_visible = all(visibility_status.values())
    print("All texts are visible:", all_visible)


@pytest.mark.testrail(65479)# 65480
def test_network_Verify_user_is_redirected_to_networking_home_page(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    expect(page.get_by_test_id(locators['NETWORK_HEADER'])).to_be_visible()
    network_page_heading = page.get_by_test_id(locators['NETWORK_HEADER'])
    networking_header = network_page_heading.inner_text()
    assert networking_header == "Networking", "User could not be navigated to networking section!!"
    logging.info("User successfully navigated to networking  screen!")

@pytest.mark.testrail(65695)
def test_network_verify_network_description_displayed_on_page(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    expect(page.get_by_test_id(locators['NETWORK_DISCRIPTION'])).to_be_visible()
    network_discription_element = page.get_by_test_id(locators['NETWORK_DISCRIPTION'])
    network_description_value = network_discription_element.inner_text()
    assert network_description_value == ComputeTextData.network_discription, f"The network description value - {network_description_value}, is different than expected!"
    logging.info("Description on network header screen is correct!")

@pytest.mark.testrail(65481)
def test_verify_networking_screen_network_Security_LBaaS_IPAddress_Global_Cloud_Konnect_Internet_Peering_Services(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    expect(page.get_by_test_id(locators['NETWORK_HEADER'])).to_be_visible()
    expected_texts= ComputeTextData.network_header_section
    check_visibility(page,expected_texts)

@pytest.mark.testrail(65482)# 65483
def test_security_Verify_user_is_redirected_to_security_home_page(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    security_page_heading = page.get_by_test_id(locators['SECURITY_HEADER'])
    Security_header = security_page_heading.inner_text()
    assert Security_header == "Security", "User could not be navigated to Security section!!"
    logging.info("User successfully navigated to security  screen!")

@pytest.mark.testrail(65484)
def test_security_verify_security_description_displayed_on_page(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_DISCRIPTION'])).to_be_visible()
    security_discription_element = page.get_by_test_id(locators['SECURITY_DISCRIPTION'])
    secutity_discription_text = security_discription_element.inner_text()
    assert secutity_discription_text == ComputeTextData.security_discription, f"The security description value - {secutity_discription_text}, is different than expected!"
    logging.info("Description on security header screen is correct!")

@pytest.mark.testrail(65485)
def test_verify_security_screen__VPNaaS_SSL_Certificate_DDoS_VAPT_Service_PAM_Activitys(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    expected_texts= ComputeTextData.security_header_section
    check_visibility(page,expected_texts)

@pytest.mark.testrail(65486)# 65487
def test_Automation_Verify_user_is_redirected_to_automation_home_page(page):
    perform_click_on_compute_resource(page, locators['AUTOMATION_TAB'])
    expect(page.get_by_test_id(locators['AUTOMATION_HEADER'])).to_be_visible()
    network_page_heading = page.get_by_test_id(locators['AUTOMATION_HEADER'])
    networking_header = network_page_heading.inner_text()
    assert networking_header == "Automation", "User could not be navigated to automation section!!"
    logging.info("User successfully navigated to automation  screen!")

@pytest.mark.testrail(65488)
def test_automation_verify_automation_description_displayed_on_page(page):
    perform_click_on_compute_resource(page, locators['AUTOMATION_TAB'])
    expect(page.get_by_test_id(locators['AUTOMATION_DISCRIPTION'])).to_be_visible()
    automation_discription_element = page.get_by_test_id(locators['AUTOMATION_DISCRIPTION'])
    automation_description_value = automation_discription_element.inner_text()
    assert automation_description_value == ComputeTextData.automations_discription, f"The automation description value - {automation_description_value}, is different than expected!"
    logging.info("Description on automation header screen is correct!")

@pytest.mark.testrail(65489)
def test_verify_Automation_screen_stacks(page):
    perform_click_on_compute_resource(page, locators['AUTOMATION_TAB'])
    expect(page.get_by_test_id(locators['AUTOMATION_HEADER'])).to_be_visible()
    expected_texts= ComputeTextData.Automatation_header_section
    check_visibility(page,expected_texts)

"""My Edge Site - Verify user is redirected to My Edge Site home page """
@pytest.mark.testrail(65490)# 65491
def test_My_Edge_Site_Verify_user_is_redirected_to_My_Edge_Site_home_page(page):
    perform_click_on_compute_resource(page, locators['EDGE_SIDE_TAB'])
    expect(page.get_by_test_id(locators['EDGE_SIDE_HEADER'])).to_be_visible()
    Edge_Site_page_heading = page.get_by_test_id(locators['EDGE_SIDE_HEADER'])
    Edge_Site_header = Edge_Site_page_heading.inner_text()
    assert Edge_Site_header == "My Edge Site", "User could not be navigated to My_Edge_Site section!!"
    logging.info("User successfully navigated to My_Edge_Site  screen!")

"""My Edge Site - Verify that the description is displayed on the page."""
@pytest.mark.testrail(65492)
def test_My_Edge_Site_verify_My_Edge_Site_description_displayed_on_page(page):
    perform_click_on_compute_resource(page, locators['EDGE_SIDE_TAB'])
    expect(page.get_by_test_id(locators['EDGE_SIDE_DISCRIPTION'])).to_be_visible()
    Edge_Site_discription_element = page.get_by_test_id(locators['EDGE_SIDE_DISCRIPTION'])
    Edge_Site_description_value = Edge_Site_discription_element.inner_text()
    assert Edge_Site_description_value == ComputeTextData.edge_side_discription, f"The My_Edge_Site description value - {Edge_Site_description_value}, is different than expected!"
    logging.info("Description on My_Edge_Site header screen is correct!")

"""Verify My Edge Site screen - Edge Site"""
@pytest.mark.testrail(65493)
def test_verify_My_Edge_Site_screen_Edge_Sites(page):
    perform_click_on_compute_resource(page, locators['EDGE_SIDE_TAB'])
    expect(page.get_by_test_id(locators['EDGE_SIDE_HEADER'])).to_be_visible()
    expected_texts= ComputeTextData.edge_side_header_section
    check_visibility(page,expected_texts)

"""Manage_Database - Verify user is redirected to Manage_Database home page """
@pytest.mark.testrail(65495)# 65496
def test_Manage_Database_Verify_user_is_redirected_to_Manage_Database_home_page(page):
    perform_click_on_compute_resource(page, locators['MANAGED_DATABASE_TAB'])
    expect(page.get_by_test_id(locators['MANAGED_DATABASE_HEADER'])).to_be_visible()
    Manage_Database_heading = page.get_by_test_id(locators['MANAGED_DATABASE_HEADER'])
    Manage_Database_header = Manage_Database_heading.inner_text()
    assert Manage_Database_header == "Managed Database", "User could not be navigated to Manage_Database section!!"
    logging.info("User successfully navigated to Manage_Database  screen!")

"""Manage_Database - Verify that the description is displayed on the page."""
@pytest.mark.testrail(65497)
def test_Manage_Database_verify_Manage_Database_description_displayed_on_page(page):
    perform_click_on_compute_resource(page, locators['MANAGED_DATABASE_TAB'])
    expect(page.get_by_test_id(locators['MANAGED_DATABASE_DISCRIPTION'])).to_be_visible()
    Manage_Database_discription_element = page.get_by_test_id(locators['MANAGED_DATABASE_DISCRIPTION'])
    Manage_Database_description_value = Manage_Database_discription_element.inner_text()
    assert Manage_Database_description_value == ComputeTextData.database_discription, f"The Manage_Database description value - {Manage_Database_description_value}, is different than expected!"
    logging.info("Description on Manage_Database header screen is correct!")

"""Verify Manage_Database screen - Manage_Database"""
@pytest.mark.testrail(65498)
def test_verify_Manage_Databasee_screen_Manage_Database(page):
    perform_click_on_compute_resource(page, locators['MANAGED_DATABASE_TAB'])
    expect(page.get_by_test_id(locators['MANAGED_DATABASE_HEADER'])).to_be_visible()
    expected_texts= ComputeTextData.database_section
    check_visibility(page,expected_texts)


"""Support - Verify user is redirected to Support home page """
@pytest.mark.testrail(65499)# 65500
def test_Support_Verify_user_is_redirected_to_Support_home_page(page):
    perform_click_on_compute_resource(page, locators['SUPPORT_TAB'])
    expect(page.get_by_test_id(locators['SUPPORT_HEADER'])).to_be_visible()
    support_page_heading = page.get_by_test_id(locators['SUPPORT_HEADER'])
    support_header = support_page_heading.inner_text()
    assert support_header == "Support", "User could not be navigated to Support section!!"
    logging.info("User successfully navigated to Support  screen!")

"""Support - Verify that the description is displayed on the page."""
@pytest.mark.testrail(65501)
def test_Support_verify_Support_description_displayed_on_page(page):
    perform_click_on_compute_resource(page, locators['SUPPORT_TAB'])
    expect(page.get_by_test_id(locators['SUPPORT_DISRCIPTION'])).to_be_visible()
    support_discription_element = page.get_by_test_id(locators['SUPPORT_DISRCIPTION'])
    support_description_value = support_discription_element.inner_text()
    assert support_description_value == ComputeTextData.support_discription, f"The Support description value - {support_description_value}, is different than expected!"
    logging.info("Description on Support header screen is correct!")

"""Verify Support screen - Support"""
@pytest.mark.testrail(65502)
def test_verify_Supporte_screen_ticket(page):
    perform_click_on_compute_resource(page, locators['SUPPORT_TAB'])
    expect(page.get_by_test_id(locators['SUPPORT_HEADER'])).to_be_visible()
    expected_texts= ComputeTextData.support_section
    check_visibility(page,expected_texts)

@pytest.mark.testrail(65504)
def test_Verify_VM_Creation_with_different_Image_and_Version_combinations(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    verify_to_click_tejas_compute_tab(page)
    perform_click_on_create_vm_button(page, locators['CREATE_VM_BUTTON'])
    page.locator(locators['NAME_FIELD']).fill("")
    page.locator(locators['NAME_FIELD']).type(MACHINE_NAME)
    public_image_card = page.query_selector_all(f'[data-testid="tab-public-image-card"]')
    public_card_count = len(public_image_card)
    print("Number of elements matching the selector:", public_card_count)
    for index, element in enumerate(public_image_card, start=1):
        element_text = element.inner_text()
        print("Public_Images_Card", element_text)
    if public_card_count > 0:
        public_image_card[0].click()
        page.wait_for_timeout(TIMEOUT)
    page.wait_for_timeout(TIMEOUT)
    page.locator(locators['IMAGE_VERSION']).is_visible()
    selected_image_version = page.locator(locators['IMAGE_VERSION']).inner_text()
    logging.info("P_version:", selected_image_version)

@pytest.mark.testrail(65505)
def test_Verify_VM_Creation_with_different_flavor(page):
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    page.wait_for_timeout(1000)
    compute_flavor_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_flavor_count = len(compute_flavor_elements)
    if compute_flavor_count > 0:
        compute_flavor_elements[7].click()
        page.wait_for_timeout(1000)
        # selected_flavor_text = page.get_by_test_id(locators['SELECTED_FLAVOR_ELEMENT']).inner_text()
        # logging.info(selected_flavor_text)

@pytest.mark.testrail(65506)
def test_Verify_VM_Creation_with_machine_creds_keypair(page):
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.wait_for_timeout(1000)
    page.locator(locators['KEY_PAIR_PLACEHOLDER']).click()
    key_pair_elements1 = page.query_selector_all(f'[data-testid="keypair-id-select-option"]')
    compute_keypair_count = len(key_pair_elements1)
    if compute_keypair_count > 0:
        key_pair_elements1[0].click()
    page.wait_for_timeout(1000)
@pytest.mark.testrail(65507)
def test_Verify_VM_Creation_with_machine_creds_username_password(page):
    page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).click()
    page.locator(locators['NAME_FIELD_MACHINE']).fill("ATULTAYADE")
    page.locator(locators['PASSWORD_FIELD_MACHINE']).fill("India@143")
    page.locator(locators['CONF_PASSWORD_FIELD_MACHINE']).fill("India@143")
    page.wait_for_timeout(1000)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Creating virtual machine."
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)

@pytest.mark.testrail(65508)
def test_Verify_VM_detail_page_onVM(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    print("Status:", status_text)
    vmcreation = page.query_selector_all(f'[data-testid="resource-name-link"]')
    name_count = len(vmcreation)
    if name_count > 0:
        VM_name = vmcreation[0].inner_text()
        print("created em name:", VM_name)
    else:
        print("No VM names found.")

"""Verify Documenation """
#65503,65504,65505,65506,65507,65508
@pytest.mark.testrail(65509)
def test_Verify_VM_detail_page_for_Overview_section_Basic_Details_Security_Groups_Volumes_Attached(page, tejas_setup):

    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(VM_List_elements)
    print("cont",count)
    if count > 0:
        VM_List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['CONFIGURATION_HEADING_NAME'])).to_be_visible()
    overview_field = page.locator(locators['OVERVIEW_TAB'])
    expect(overview_field).to_be_visible()
    expect(page.get_by_test_id(locators['BASIC_DETAIL'])).to_be_visible()
    expect(page.get_by_test_id(locators['SECURITY_GROUPS_OVE'])).to_be_visible()
    expect(page.get_by_test_id(locators['VOLUME_ATTACH_OVE'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)


@pytest.mark.testrail(65511)
def test_Verify_VM_detail_page_snapshots_section_user_can_take_snapshot_and_able_to_delete_the_same(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(VM_List_elements)
    print("cont",count)
    if count > 0:
        VM_List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    size_element = page.locator(locators['SNAPSHOT_SCREEN'])
    expect(size_element).to_be_visible()
    page.locator(locators['SNAPSHOT_SCREEN']).click()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()
    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], MACHINE_NAME)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
    created_snapshot = page.query_selector_all(f'[data-testid="resource-name-link"]')
    snapshot_count = len(created_snapshot)
    if snapshot_count > 0:
        Snapshot_creation_name = created_snapshot[0].inner_text()
        print(Snapshot_creation_name)
        logging.info("displayed the created_snapshot name:", Snapshot_creation_name)
    else:
        logging.info("snapshot is not created.")
    items_to_verify = ["Delete"]
    delete_the_action_for_selected_feture(page, items_to_verify)

@pytest.mark.testrail(65512)
def test_Verify_VM_storage_section_as_user_can_attach_detach_Volume(page, tejas_setup):
    size_element = page.locator(locators['STORAGE_SCREEN'])
    expect(size_element).to_be_visible()
    page.locator(locators['STORAGE_SCREEN']).click()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    publicIp_dropdown_element = page.locator(locators['ATTACHVOLUME_DRPDOWN'])
    publicIp_dropdown_element.click()
    page.wait_for_timeout(10000)
    ZoneDropdown_elements = page.query_selector_all(f'[data-testid="volume-id-select-option"]')
    count = len(ZoneDropdown_elements)
    print("test",count)
    if count > 0:
        ZoneDropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
        page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    else:
        page.get_by_test_id(locators['CLOSE_BTN']).click()

    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65513)
def test_Verify_VM_Network_section_as_user_can_attach_detach_network(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(VM_List_elements)
    print("cont",count)
    if count > 0:
        VM_List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    networkscreen = page.locator(locators['NETWORK_SCREN'])
    expect(networkscreen).to_be_visible()
    page.locator(locators['NETWORK_SCREN']).click()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()

    network_dropdown_element = page.locator(locators['NETWORKS'])
    network_dropdown_element.click()
    page.wait_for_timeout(10000)
    Dropdown_elements = page.query_selector_all(f'[data-testid="network-id-select-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
        page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    else:
        page.get_by_test_id(locators['CLOSE_BTN']).click()

    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65514)
def test_Verify_VM_security_group_as_user_can_attach_detach_security_group(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(VM_List_elements)
    print("cont",count)
    if count > 0:
        VM_List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    page.wait_for_timeout(10000)
    security_grp_screen = page.locator(locators['SECURITY_SCREEN'])
    expect(security_grp_screen).to_be_visible()
    page.locator(locators['SECURITY_SCREEN']).click()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()

    security_dropdown_element = page.locator(locators['SG_GROUP_SCREEN'])
    security_dropdown_element.click()
    page.wait_for_timeout(10000)
    Dropdown_elements = page.query_selector_all(f'[data-testid="security-group-id-select-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
        page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    else:
        page.get_by_test_id(locators['CLOSE_BTN']).click()

    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()


@pytest.mark.testrail(65515)
def test_verify_VM_detail_page_for_Backup_feature_user_can_create_schedule_and_delete_backup(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(VM_List_elements)
    print("cont",count)
    if count > 0:
        VM_List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    page.wait_for_timeout(10000)
    security_grp_screen = page.locator(locators['BACKUP_SCRENN'])
    expect(security_grp_screen).to_be_visible()
    page.locator(locators['BACKUP_SCRENN']).click()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()

    clear_and_fill_field(page, locators['BACKUP_NAME_FIELD'], MACHINE_NAME)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    page.wait_for_timeout(1000)
    page.get_by_test_id(locators['SCHEDULED_BACKUP_BTN']).click()
    clear_and_fill_field(page, locators['BACKUP_NAME_FIELD'], MACHINE_NAME)
    frequency_dropdown_element = page.locator(locators['FREQUENCY_TYPE'])
    frequency_dropdown_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="frequency-type-select-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
        page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    else:
        page.get_by_test_id(locators['CLOSE_BTN']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Backup scheduled successfully."
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65516)
def test_verify_VM_detail_page_for_Console_logs_feature_logs_should_display(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(VM_List_elements)
    print("cont",count)
    if count > 0:
        VM_List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    page.wait_for_timeout(1000)
    console_log_screen = page.locator(locators['CONSOLELOG_SCREEN'])
    expect(console_log_screen).to_be_visible()
    page.locator(locators['CONSOLELOG_SCREEN']).click()
    page.wait_for_timeout(1000)
    log_content = page.locator(locators['LOG_TEXT'])
    expect(log_content).to_be_visible()
    log_dispaly= page.locator(locators['LOG_TEXT']).inner_text()
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65517)
def test_verify_VM_detail_page_for_Monitoring_feature_graph_data_should_display_for_Network_CPU_utilization_andmemory_utilization(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(VM_List_elements)
    print("cont",count)
    if count > 0:
        VM_List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    page.wait_for_timeout(1000)
    monitoring_screen = page.locator(locators['MONITORING_SCREEN'])
    expect(monitoring_screen).to_be_visible()
    page.locator(locators['MONITORING_SCREEN']).click()
    page.wait_for_timeout(1000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()


@pytest.mark.testrail(65510)
def test_verify_VM_detail_page_for_Resize_section_user_shouldbe_able_to_resize_the_VM_with_increased_flavor_only_and_not_decreased_current_flavor(page, tejas_setup):
    size_element = page.locator(locators['RESIZE'])
    expect(size_element).to_be_visible()
    page.locator(locators['RESIZE']).click()
    expect(page.get_by_test_id(locators['MEMORY_GENARAL_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['COMPUTE_GENERAL_TAB'])).to_be_visible()
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count1:", compute_header_count)
    if compute_header_count > 0:
        compute_header_elements[3].click()

    page.get_by_test_id(locators['RESIZE_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Resizing virtual machine."
    page.wait_for_timeout(10000)
    #
    # verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    to_create_virtual_Compute_machine(page)
    page.wait_for_timeout(10000)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)

def verify_to_headersection(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count:", compute_header_count)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)

def item_is_displayed(page, item_to_verify):
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    if VM_List_elements:
        VM_List_elements[0].click()
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
    for item in ellipsis_items:
        text_value = item.inner_text()
        print(text_value)
        if item.inner_text() == item_to_verify:
            return True
    return False

@pytest.mark.testrail(65518)
def test_Verify_the_VM_Shutoff_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Shutoff":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Stop."
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65849)
def test_Verify_the_VM_Start_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ["Start", "Hard Reboot", "Lock" ,"Suspend", "Install Antivirus", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Start":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
            page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()


@pytest.mark.testrail(65519)
def test_Verify_the_VM_Pause_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Pause":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Pause."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65851)
def test_Verify_the_VM_Unpause_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ["Unpause", "Lock" ,"Suspend", "Install Antivirus", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Unpause":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Unpause."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65520)
def test_Verify_the_VM_Reboot_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Reboot":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Reboot."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65521)
def test_Verify_the_VM_Hard_Reboot_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Hard Reboot":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Hard Reboot."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65522)
def test_Verify_the_VM_Lock_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Lock":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Lock."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
##unable Attach Public IP
@pytest.mark.testrail(65852)
def test_Verify_the_VM_Unlock_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ["Shutoff", "Pause", "Reboot", "Hard Reboot", "Unlock", "Suspend", "Resize", "Install Antivirus", "Enable Backup", "Attach Public IP", "Manage Labels", "Take Snapshot", "Attach Volume", "Attach Network", "Attach Security Groups", "Console", "Console logs", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Unlock":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Unlock."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()


@pytest.mark.testrail(65523)
def test_Verify_the_VM_Suspend_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Suspend":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Suspend."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()


@pytest.mark.testrail(65853)
def test_Verify_the_VM_Resume_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ["Lock", "Resume", "Install Antivirus", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Resume":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Resume."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()



@pytest.mark.testrail(65525)
def test_Verify_the_VM_Enable_Backup_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Enable Backup":
            click_ellipsis_item(page, item_to_click)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    Enable_Backup_popup = page.get_by_test_id(locators['CONFIRMATION_TEXT']).inner_text()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Backup state updated successfully."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65855)
def test_Verify_the_VM_disable_Backup_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ["Shutoff", "Pause", "Reboot", "Hard Reboot", "Unlock", "Suspend", "Resize", "Install Antivirus", "Disable Backup", "Attach Public IP", "Manage Labels", "Take Snapshot", "Attach Volume", "Attach Network", "Attach Security Groups", "Console", "Console logs", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Disable Backup":
            click_ellipsis_item(page, item_to_click)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    disable_Backup_popup = page.get_by_test_id(locators['CONFIRMATION_TEXT']).inner_text()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Backup state updated successfully."
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65526)
def test_Verify_the_VM_Attach_Public_IP_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Attach Public IP":
            click_ellipsis_item(page, item_to_click)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    public_ip_heading = page.get_by_test_id(locators['CONFIRMATION_TEXT']).inner_text()
    assert public_ip_heading == "Attach Public IP"
    publicIp_dropdown_element = page.locator(locators['FLOATING_IP_DROPDOWN'])
    publicIp_dropdown_element.click()
    ZoneDropdown_elements = page.query_selector_all(f'[data-testid="floating_ip_address-option"]')
    count = len(ZoneDropdown_elements)
    if count > 0:
        ZoneDropdown_elements[0].click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Public IP attached successfully."
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65857)
def test_Verify_the_VM_detach_Public_IP_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ["Shutoff", "Pause", "Reboot", "Hard Reboot", "Unlock", "Suspend", "Resize", "Install Antivirus", "Disable Backup", "Detach Public IP", "Manage Labels", "Take Snapshot", "Attach Volume", "Attach Network", "Attach Security Groups", "Console", "Console logs", "Delete"]

    for item_to_click in items_to_verify:
        if item_to_click == "Detach Public IP":
            click_ellipsis_item(page, item_to_click)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    public_ip_heading = page.get_by_test_id(locators['CONFIRMATION_TEXT']).inner_text()
    assert public_ip_heading == "Detach Public IP"
    publicIp_dropdown_element = page.locator(locators['FLOATING_IP_DROPDOWN'])
    publicIp_dropdown_element.click()
    ZoneDropdown_elements = page.query_selector_all(f'[data-testid="floating_ip_address-option"]')
    count = len(ZoneDropdown_elements)
    if count > 0:
        ZoneDropdown_elements[0].click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Public IP detached successfully."
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65527)
def test_Verify_the_VM_Manage_Labels_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    fill_the_manage_label_for_selected_feature(page, items_to_verify)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65528)
def test_Verify_the_VM_Take_Snapshot_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Take Snapshot":
            click_ellipsis_item(page, item_to_click)
    size_element = page.locator(locators['SNAPSHOT_SCREEN'])
    expect(size_element).to_be_visible()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()
    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], MACHINE_NAME)

    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Creating compute snapshot."
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()


@pytest.mark.testrail(65529)
def test_Verify_the_VM_Attach_Volume_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Attach Volume":
            click_ellipsis_item(page, item_to_click)
    size_element = page.locator(locators['STORAGE_SCREEN'])
    expect(size_element).to_be_visible()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()

    publicIp_dropdown_element = page.locator(locators['ATTACHVOLUME_DRPDOWN'])
    publicIp_dropdown_element.click()
    page.wait_for_timeout(10000)
    ZoneDropdown_elements = page.query_selector_all(f'[data-testid="volume-id-select-option"]')
    count = len(ZoneDropdown_elements)
    print("test",count)
    if count > 0:
        ZoneDropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
        page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    else:
        page.get_by_test_id(locators['CLOSE_BTN']).click()

    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65530)
def test_Verify_the_VM_Attach_Network_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Attach Network":
            click_ellipsis_item(page, item_to_click)
    networkscreen = page.locator(locators['NETWORK_SCREN'])
    expect(networkscreen).to_be_visible()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()

    network_dropdown_element = page.locator(locators['NETWORKS'])
    network_dropdown_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="network-id-select-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
        page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    else:
        page.get_by_test_id(locators['CLOSE_BTN']).click()

    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65531)
def test_Verify_the_VM_Attach_Security_Groups_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Attach Security Groups":
            click_ellipsis_item(page, item_to_click)
    networkscreen = page.locator(locators['SECURITY_SCREEN'])
    expect(networkscreen).to_be_visible()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()

    network_dropdown_element = page.locator(locators['SG_GROUP_SCREEN'])
    network_dropdown_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="security-group-id-select-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
        page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    else:
        page.get_by_test_id(locators['CLOSE_BTN']).click()

    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65532)
def test_Verify_the_VM_Console_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    console_visible = item_is_displayed(page, "Console")
    assert console_visible, "Console item is not visible"
    assert "Console" in items_to_verify, "Console item is not in the list of expected items"

@pytest.mark.testrail(65533)
def test_Verify_the_VM_Console_logs_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Console logs":
            click_ellipsis_item(page, item_to_click)
    console_log_screen = page.locator(locators['CONSOLELOG_SCREEN'])
    expect(console_log_screen).to_be_visible()
    page.locator(locators['CONSOLELOG_SCREEN']).click()
    page.wait_for_timeout(1000)
    log_content = page.locator(locators['LOG_TEXT'])
    expect(log_content).to_be_visible()
    log_dispaly= page.locator(locators['LOG_TEXT']).inner_text()
    page.wait_for_timeout(10000)

@pytest.mark.testrail(65534)
def test_Verify_the_VM_delete_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    delete_the_action_for_selected_feture(page, items_to_verify)


@pytest.mark.testrail(65524)
def test_Verify_the_VM_Resize_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ComputeTextData.ellipse_section
    for item_to_click in items_to_verify:
        if item_to_click == "Resize":
            click_ellipsis_item(page, item_to_click)
    size_element = page.locator(locators['RESIZE'])
    expect(size_element).to_be_visible()
    expect(page.get_by_test_id(locators['MEMORY_GENARAL_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['COMPUTE_GENERAL_TAB'])).to_be_visible()
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count1:", compute_header_count)
    if compute_header_count > 0:
        compute_header_elements[3].click()

    page.get_by_test_id(locators['RESIZE_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Resizing virtual machine."
    page.wait_for_timeout(10000)
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()


@pytest.mark.testrail(65854)
def test_Verify_the_VM_unpauseresize_action(page, tejas_setup):
    verify_to_headersection(page)
    items_to_verify = ["Unpause", "Lock", "Suspend", "Stop Antivirus service", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Unpause":
            click_ellipsis_item(page, item_to_click)
            page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()

    assert toast_text == "Performing action: Unpause."
    page.wait_for_timeout(10000)
    verify_to_setup(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65535)
def test_Verify_Compute_Snapshots_creation_for_VM(page, snapshots_setup):
    perform_click_on_create_vm_button(page, locators['SNAPSHOTE_CREATE_COMPUTE'])
    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], MACHINE_NAME)
    dropdown_element = page.locator(locators['SNAPSHOTS_DROPDOWN'])
    expect(dropdown_element).to_be_visible()
    assert dropdown_element.is_visible(), "Dropdown menu is not displayed"
    dropdown_element.click()
    page.wait_for_timeout(10000)
    vm_elements = page.query_selector_all(f'[data-testid="compute-id-select-option"]')
    compute_header_count = len(vm_elements)
    if compute_header_count > 0:
        first_vm_name = vm_elements[0].inner_text()
        vm_elements[0].click()
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], MACHINE_NAME)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
    created_snapshot = page.query_selector_all(f'[data-testid="resource-name-link"]')
    snapshot_count = len(created_snapshot)
    if snapshot_count > 0:
        Snapshot_creation_name = created_snapshot[0].inner_text()
        print(Snapshot_creation_name)
        logging.info("displayed the created_snapshot name:", Snapshot_creation_name)
    else:
        logging.info("snapshot is not created.")

@pytest.mark.testrail(65536)
def test_Verify_Compute_Snapshots_manage_label_action(page, snapshots_setup):
    items_to_verify = ["Manage Labels", "Delete"]
    fill_the_manage_label_for_selected_feature(page, items_to_verify)


@pytest.mark.testrail(65537)
def test_Verify_Compute_Snapshots_manage_label_action(page, snapshots_setup):
    items_to_verify = ["Manage Labels", "Delete"]
    delete_the_action_for_selected_feture(page, items_to_verify)

@pytest.mark.testrail(65538)
def test_Verify_Block_storage_creation(page, storage_setup):
    perform_click_on_create_vm_button(page, locators['VOLUME_CREATE_BTN'])
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    clear_and_fill_field(page, locators['VOLUME_CREATE_NAME'], MACHINE_NAME)
    dropdown_element = page.locator(locators['VOLUME_CREATE_TYPE'])
    expect(dropdown_element).to_be_visible()
    assert dropdown_element.is_visible(), "Dropdown menu is not displayed"
    dropdown_element.click()
    vm_elements = page.query_selector_all(f'[data-testid="volume_type-option"]')
    compute_header_count = len(vm_elements)
    if compute_header_count > 0:
        first_vm_name = vm_elements[0].inner_text()
        vm_elements[0].click()
    page.wait_for_timeout(TIMEOUT)

    page.get_by_test_id(locators['VOL_SWIPE_BUTTON']).click()
    page.get_by_test_id(locators['ARROWBTN']).click()

    dropdown_elements = page.query_selector_all(f'[data-testid="compute-id-select-option"]')
    c_count = len(dropdown_elements)
    if c_count > 0:
        first_vm_name = dropdown_elements[0].inner_text()
        print("test", first_vm_name)
        dropdown_elements[0].click()
    page.wait_for_timeout(TIMEOUT)
    
    clear_and_fill_field(page, locators['VOLUME_CREATE_SIZE'], "50")
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    expect(page.get_by_test_id(locators['VOLUME_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
    created_volume = page.query_selector_all(f'[data-testid="resource-name-link"]')
    volume_count = len(created_volume)
    if volume_count > 0:
        volume_creation_name = created_volume[0].inner_text()
        print(volume_creation_name)
        logging.info("displayed the created_volume name:", volume_creation_name)
    else:
        logging.info("volume is not created.")

@pytest.mark.testrail(65539)
def test_Verify_Block_Storage_Attach_from_Virtual_Machine_action(page, storage_setup):
    items_to_verify = ["Take Snapshot", "Attach with Virtual Machine","Extend Size","Manage Labels", "Delete Volume"]
    for item_to_click in items_to_verify:
        if item_to_click == "Attach with Virtual Machine":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    dropdown_element = page.locator(locators['SNAPSHOTS_DROPDOWN'])
    expect(dropdown_element).to_be_visible()
    assert dropdown_element.is_visible(), "Dropdown menu is not displayed"
    dropdown_element.click()
    vm_elements = page.query_selector_all(f'[data-testid="compute-id-select-option"]')
    compute_header_count = len(vm_elements)
    if compute_header_count > 0:
        first_vm_name = vm_elements[0].inner_text()
        vm_elements[0].click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Attaching."
    page.wait_for_timeout(10000)

@pytest.mark.testrail(65540)
def test_Verify_Block_Storage_extend_size_action(page, storage_setup):
    items_to_verify = ["Detach from Virtual Machine", "Extend Size","Manage Labels"]
    for item_to_click in items_to_verify:
        if item_to_click == "Extend Size":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_text("Size (in GiB)")).to_be_visible()
    sizeGB_before_change = page.locator(locators['VOLUME_CREATE_SIZE']).inner_text()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['ROOT_VOLUME_INCREASE']).click()
    page.wait_for_timeout(TIMEOUT)
    sizeGB_after_change = page.locator(locators['VOLUME_CREATE_SIZE']).inner_text()
    size_changed = sizeGB_after_change != sizeGB_before_change
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Updating volume."
    page.wait_for_timeout(1000)


@pytest.mark.testrail(65541)
def test_Verify_Block_Storage_manage_label_action(page, storage_setup):
    items_to_verify = ["Detach from Virtual Machine", "Extend Size","Manage Labels"]
    fill_the_manage_label_for_selected_feature(page, items_to_verify)

@pytest.mark.testrail(65542)
def test_Verify_volume_snapshot_creation(page, volumeSnapshot_setup):
    perform_click_on_create_vm_button(page, locators['VOLUME_CREATE_SNAPSHOT'])
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()

    dropdown_element = page.locator(locators['ATTACHVOLUME_DRPDOWN'])
    expect(dropdown_element).to_be_visible()
    assert dropdown_element.is_visible(), "Dropdown menu is not displayed"
    dropdown_element.click()
    page.wait_for_timeout(TIMEOUT)
    vm_elements = page.query_selector_all(f'[data-testid="volume-id-select-option"]')
    compute_header_count = len(vm_elements)
    if compute_header_count > 0:
        first_vm_name = vm_elements[0].inner_text()
        print(first_vm_name)
        vm_elements[0].click()
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], MACHINE_NAME)
    #page.locator(locators['ADD_LABEL_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Volume snapshot created successfully."
    page.wait_for_timeout(10000)

    expect(page.get_by_test_id(locators['VOLUME_SNAPSHOT_HEADER'])).to_be_visible()
    created_volume = page.query_selector_all(f'[data-testid="resource-name-link"]')
    volume_count = len(created_volume)
    if volume_count > 0:
        volume_creation_name = created_volume[0].inner_text()
        print(volume_creation_name)
        logging.info("displayed the created_volume Sanpshot name:", volume_creation_name)
    else:
        logging.info("volume shotshot is not created.")

@pytest.mark.testrail(65543)
def test_Verify_Volume_Snapshots_Create_Volume_action(page, volumeSnapshot_setup):
    items_to_verify = ["Create Volume","Manage Labels", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Create Volume":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    clear_and_fill_field(page, locators['VOLUME_CREATE_NAME'], MACHINE_NAME)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Creating volume."
    page.wait_for_timeout(10000)

@pytest.mark.testrail(65544)
def test_Verify_Volume_Snapshots_managelabel_action(page, volumeSnapshot_setup):
    items_to_verify = ["Create Volume","Manage Labels", "Delete"]
    fill_the_manage_label_for_selected_feature(page, items_to_verify)

@pytest.mark.testrail(65545)
def test_Verify_Volume_Snapshots_delete_action(page, volumeSnapshot_setup):
    items_to_verify = ["Create Volume","Manage Labels", "Delete"]
    delete_the_action_for_selected_feture(page, items_to_verify)

@pytest.mark.testrail(65546)
def test_Verify_Object_Storage_creation_creation(page, volumeObject_storage):
    perform_click_on_create_vm_button(page, locators['OBJECT_CREATE_BTN'])
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    clear_and_fill_field(page, locators['INPUT_NAME'], MACHINE_NAME)
    page.get_by_test_id(locators['VERSION_CHECKBOX']).click()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Bucket created successfully."
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['OBJECT_STORAGE_HEADER'])).to_be_visible()
    created_volume = page.query_selector_all(f'[data-testid="resource-name-link"]')
    volume_count = len(created_volume)
    if volume_count > 0:
        volume_creation_name = created_volume[0].inner_text()
        print(volume_creation_name)
        logging.info("displayed the created_object storage name:", volume_creation_name)
    else:
        logging.info("created_object storage is not created.")

@pytest.mark.testrail(65696)
def test_Verify_Object_Storage_Extend_Bucket_Size_action(page, volumeObject_storage):
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Share Bucket", "Make Bucket Public", "Manage Labels", "Empty bucket", "Delete bucket"]
    for item_to_click in items_to_verify:
        if item_to_click == "Extend Bucket Size":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_text("Size (in GiB)")).to_be_visible()
    sizeGB_before_change = page.locator(locators['BUCKET_SIZE']).inner_text()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['BUCKET_SIZE_INCREASE']).click()
    page.wait_for_timeout(TIMEOUT)
    sizeGB_after_change = page.locator(locators['BUCKET_SIZE']).inner_text()
    size_changed = sizeGB_after_change != sizeGB_before_change
    print(size_changed)
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    # assert toast_text == "Bucket size extended successfully."
    # page.wait_for_timeout(10000)

@pytest.mark.testrail(65547)
def test_Verify_Object_Storage_download_config_action(page, volumeObject_storage):
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Share Bucket", "Make Bucket Public", "Manage Labels", "Empty bucket", "Delete bucket"]
    for item_to_click in items_to_verify:
        if item_to_click == "Download S3 config":
            downloaded_file_path = click_ellipsis_item(page, item_to_click)

    page.wait_for_timeout(10000)
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Bucket size extended successfully."
    page.wait_for_timeout(10000)

    config_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(config_directory)
    download_folder = "downloaded_files"
    downloads_path = os.path.join(project_root, "test_helper",download_folder)
    os.makedirs(downloads_path, exist_ok=True)
    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)

    if downloaded_file_path:
                file_name = os.path.basename(downloaded_file_path)
                destination_path = os.path.join(download_folder, file_name)
                os.rename(downloaded_file_path, destination_path)


@pytest.mark.testrail(65548)
def test_Verify_Object_Storage_Make_Bucket_Private_Public_action(page, volumeObject_storage):
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Share Bucket", "Make Bucket Public", "Manage Labels", "Empty bucket", "Delete bucket"]
    for item_to_click in items_to_verify:
        if item_to_click == "Make Bucket Public":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print(toast_text)
    page.wait_for_timeout(10000)
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Make Bucket Private", "Manage Labels", "Empty bucket", "Delete bucket"]
    for item_to_click in items_to_verify:
        if item_to_click == "Make Bucket Private":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print(toast_text)
    page.wait_for_timeout(10000)


@pytest.mark.testrail(65549)
def test_Verify_Object_storage_managelabel_action(page, volumeObject_storage):
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Share Bucket", "Make Bucket Public", "Manage Labels", "Empty bucket", "Delete bucket"]

    fill_the_manage_label_for_selected_feature(page, items_to_verify)

@pytest.mark.testrail(65550)
def test_Verify_Object_storage_emptyBucket_action(page, volumeObject_storage):
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Share Bucket", "Make Bucket Public", "Manage Labels", "Empty bucket", "Delete bucket"]
    for item_to_click in items_to_verify:
        if item_to_click == "Empty bucket":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    copy_to_clipboard_and_paste_value_function(page)
    page.wait_for_timeout(1000)

@pytest.mark.testrail(65551)
def test_Verify_object_storage_delete_action(page, volumeObject_storage):
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Share Bucket", "Make Bucket Public", "Manage Labels", "Empty bucket", "Delete bucket"]
    for item_to_click in items_to_verify:
        if item_to_click == "Delete bucket":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    copy_to_clipboard_and_paste_value_function(page)
    page.wait_for_timeout(1000)

@pytest.mark.testrail(65554)
def test_Verify_object_storage_share_bucket_action(page, volumeObject_storage):
    items_to_verify = ["Extend Bucket Size", "Download S3 config", "Share Bucket", "Make Bucket Public", "Manage Labels", "Empty bucket", "Delete bucket"]
    for item_to_click in items_to_verify:
        if item_to_click == "Share Bucket":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CLOSE_BTN']).click()
    page.wait_for_timeout(10000)

@pytest.mark.testrail(65555)
def test_Verify_file_Storage_creation(page):
    perform_click_on_compute_resource(page, locators['STORAGE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.volume_file_storage in element_text:
            element.click()
    expect(page.get_by_test_id(locators['FILE_STORAGE_HEADING'])).to_be_visible()
    perform_click_on_create_vm_button(page, locators['FILE_STORAGE_CREATE_BTN'])
    clear_and_fill_field(page, locators['FILE_STORAGE_INPUT_FIELD'], MACHINE_NAME)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()

    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['FILE_STORAGE_HEADING'])).to_be_visible()
    created_volume = page.query_selector_all(f'[data-testid="resource-name-link"]')
    volume_count = len(created_volume)
    if volume_count > 0:
        volume_creation_name = created_volume[0].inner_text()
        print(volume_creation_name)
        logging.info("displayed the created_file storage name:", volume_creation_name)
    else:
        logging.info("created_file storage is not created.")


@pytest.mark.testrail(65556)
def test_Verify_Archival_Storage_creation(page ,volume_Archival_storage):
    expect(page.get_by_test_id(locators['ARCHIVAL_STORAGE_HEADER'])).to_be_visible()
    perform_click_on_create_vm_button(page, locators['ARCHIVAL_STORAGE_CREATE_BTN'])
    clear_and_fill_field(page, locators['INPUT_NAME'], "testarchival")
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Container created successfully."
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['ARCHIVAL_STORAGE_HEADER'])).to_be_visible()
    created_volume = page.query_selector_all(f'[data-testid="resource-name-link"]')
    volume_count = len(created_volume)
    if volume_count > 0:
        volume_creation_name = created_volume[0].inner_text()
        print(volume_creation_name)
        logging.info("displayed the created_archival_storage name:", volume_creation_name)
    else:
        logging.info("archival_storage is not created.")

@pytest.mark.testrail(65557)
def test_Verify_Archival_Storage_download_S3storage(page ,volume_Archival_storage):
    items_to_verify = ["Download S3 config", "Manage Labels", "Empty container", "Delete container"]
    for item_to_click in items_to_verify:
        if item_to_click == "Download S3 config":
            #click_ellipsis_item(page, item_to_click)
            downloaded_file_path = click_ellipsis_item(page, item_to_click)
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Downloaded successfully."
    page.wait_for_timeout(10000)

    config_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(config_directory)
    download_folder = "downloaded_files"
    downloads_path = os.path.join(project_root, "test_helper",download_folder)
    os.makedirs(downloads_path, exist_ok=True)
    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)

    if downloaded_file_path:
                file_name = os.path.basename(downloaded_file_path)
                destination_path = os.path.join(download_folder, file_name)
                os.rename(downloaded_file_path, destination_path)

@pytest.mark.testrail(65558)
def test_Verify_Archival_Storage_create_and_delete_folder(page ,volume_Archival_storage):
    page.wait_for_timeout(TIMEOUT)
    List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(List_elements)
    print("cont",count)
    if count > 0:
        List_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    page.locator(locators['ARCHIVAL_TAB']).is_visible()
    expect(page.get_by_test_id(locators['ARCHIVAL_CREATE_FOLDER'])).to_be_visible()
    page.get_by_test_id(locators['ARCHIVAL_CREATE_FOLDER']).click()
    clear_and_fill_field(page, locators['INPUT_NAME'], "testarchival")
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Folder created."
    page.wait_for_timeout(10000)
    expect(page.locator(locators['REQUEST_ID'])).to_be_visible()
    createdfolder_name = page.locator(locators['REQUEST_ID']).inner_text()
    logging.info("......",createdfolder_name)
    page.locator(locators['ELLIPSE_ICON']).click()
    page.locator(locators['DELETE_FOLDER']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Storage deleted successfully."
    page.wait_for_timeout(TIMEOUT)
    expect(page.locator(locators['REQUEST_ID'])).not_to_be_visible()
    page.get_by_test_id(locators['BACK_BTN']).click()
    page.wait_for_timeout(10000)



@pytest.mark.testrail(65559)
def test_Verify_Archival_Storage_empty_and_delete_action(page ,volume_Archival_storage):
    items_to_verify = ["Download S3 config", "Manage Labels", "Empty container", "Delete container"]
    for item_to_click in items_to_verify:
        if item_to_click == "Empty container":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    copy_to_clipboard_and_paste_value_function(page)
    page.wait_for_timeout(1000)
    for item_to_click in items_to_verify:
        if item_to_click == "Delete container":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(10000)
    copy_to_clipboard_and_paste_value_function(page)
    page.wait_for_timeout(1000)
    # Container emptied successfully.
    # Container deleted successfully.

@pytest.mark.testrail(65560)
def test_Verify_Backup_Recovery_creation(page):
    perform_click_on_compute_resource(page, locators['STORAGE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.backup_recovery_tab in element_text:
            element.click()
    expect(page.get_by_test_id(locators['BACKUP_RECOVER_HEADER'])).to_be_visible()
    page_heading = page.get_by_test_id(locators['BACKUP_RECOVER_HEADER'])
    backup_header = page_heading.inner_text()
    assert backup_header == "Suraksha Store", "User could not be navigated to Suraksha Store page header!!"
    logging.info("User successfully navigated to Suraksha Store homepage  screen!")

# @pytest.mark.testrail(65561)
@pytest.mark.testrail(65562)
def test_Verify_RAS_form_creation(page):
    perform_click_on_compute_resource(page, locators['STORAGE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.ras_tab in element_text:
            element.click()
    expect(page.get_by_test_id(locators['RAS_HEADER'])).to_be_visible()
    page_heading = page.get_by_test_id(locators['RAS_HEADER'])
    ras_heading = page_heading.inner_text()
    assert ras_heading == "Resiliency Assurance Service", "User could not be navigated to Resiliency Assurance Service page header!!"
    logging.info("User successfully navigated to Resiliency Assurance Service homepage  screen!")

@pytest.mark.testrail(65563)
def test_Verify_Networkcreation(page, create_kshetra_network):
    NETWORK_ADDRESS = "192.168.1.0/24"
    page.locator(locators['CREATE_NAME']).is_visible()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    clear_and_fill_field(page, locators['CREATE_NAME'], MACHINE_NAME)
    clear_and_fill_field(page, locators['NETWORK_CIDR'], NETWORK_ADDRESS)
    yes_button_element = page.get_by_test_id(locators['CONFIRM_BUTTON'])
    assert yes_button_element.is_visible(), "confirm button is not visible."
    yes_button_element.click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print(toast_text)
    page.wait_for_timeout(10000)
    expected_toast_msg = "Network created successfully."
    if toast_text != ComputeTextData.kshetra_create_network_toast_msg:
        cancel_button_element = page.get_by_test_id("btn-cancel")
        assert cancel_button_element.is_visible(), "Cancel button is not visible."
        cancel_button_element.click()
    else:
        assert toast_text == ComputeTextData.kshetra_create_network_toast_msg, f"The toast message '{toast_text}' is different than expected: '{expected_toast_msg}'"
        expect(page.get_by_test_id(locators['KSHETRA_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)

@pytest.mark.testrail(65564)
def test_Verify_Network_manageLabel_action(page ,kshetra_setup):
    items_to_verify = ["Manage Labels", "Delete"]
    fill_the_manage_label_for_selected_feature(page, items_to_verify)

@pytest.mark.testrail(65565)
def test_Verify_Network_delete_action(page ,kshetra_setup):
    items_to_verify = ["Manage Labels", "Delete"]
    delete_the_action_for_selected_feture(page, items_to_verify)


#
@pytest.mark.testrail(65566)
def test_Verify_security_group_creation(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.port_security in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    perform_click_on_compute_resource(page, locators['CREATE_PORT_SEC_BTN'])
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    clear_and_fill_field(page, locators['CREATE_SEC_NAME'], MACHINE_NAME)
    yes_button_element = page.get_by_test_id(locators['CONFIRM_BUTTON'])
    assert yes_button_element.is_visible(), "confirm button is not visible."
    yes_button_element.click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    page.wait_for_timeout(10000)
    assert toast_text == "Security group created successfully."
    expect(page.get_by_test_id(locators['PORT_SEC_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
    created_list = page.query_selector_all(f'[data-testid="resource-name-link"]')
    volume_count = len(created_list)
    if volume_count > 0:
        volume_creation_name = created_list[0].inner_text()
        print(volume_creation_name)
        logging.info("displayed the created_port_security name:", volume_creation_name)
    else:
        logging.info("created_port_security is not created.")

@pytest.mark.testrail(65567)
def test_Verify_security_Security_Rules_action(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    page.wait_for_timeout(TIMEOUT)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.port_security in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    items_to_verify = ["Security Rules", "Delete"]
    for item_to_click in items_to_verify:
        if item_to_click == "Security Rules":
            click_ellipsis_item(page, item_to_click)
    page.wait_for_timeout(1000)
    size_element = page.locator(locators['PORT_SECURITY_SCREEN'])
    expect(size_element).to_be_visible()
    expect(page.get_by_test_id(locators['CREATE_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_BUTTON']).click()
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()

    protocol_element = page.locator(locators['SECURITY_PROTOCOL'])
    protocol_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="protocol-select-option"]')
    for element in Dropdown_elements:
        element_text = element.inner_text()
        if "All UDP" in element_text:
            element.click()
            break
    else:
        pytest.fail(f"Protocol 'All UDP' not found in dropdown options.")

    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['NETWORK_CLICK']).click()
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Security group rule created successfully."
    VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    VM_list_count = len(VM_List_elements)
    logging.info(VM_list_count)

    page.get_by_test_id(locators['BACK_BTN']).click()
    page.wait_for_timeout(10000)



@pytest.mark.testrail(65568)
def test_Verify_securitygrp_delete_action(page ,kshetra_setup):
    items_to_verify = ["Security Rules", "Delete"]
    delete_the_action_for_selected_feture(page, items_to_verify)

@pytest.mark.testrail(65569)
def test_Verify_LbaaS_creation(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    page.wait_for_timeout(TIMEOUT)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.lbass_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['LBASS_HEADING'])).to_be_visible()
    perform_click_on_compute_resource(page, locators['LBASS_CREATE_BTN'])
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['LBASS_HEADING'])).to_be_visible()
    clear_and_fill_field(page, locators['INPUT_NAME'], MACHINE_NAME)

    protocol_element = page.locator(locators['LBASS_SELECT_VM'])
    protocol_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="backendBindIP-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)

    page.get_by_test_id(locators['ADD_MEMBER_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    yes_button_element = page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON'])
    assert yes_button_element.is_visible(), "confirm button is not visible."
    yes_button_element.click()

    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    # toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    # page.wait_for_timeout(10000)
    # assert toast_text == "Creating load balancer."
    expect(page.get_by_test_id(locators['LBASS_HEADING'])).to_be_visible()
    page.wait_for_timeout(10000)
    created_list = page.query_selector_all(f'[data-testid="resource-name-link"]')
    volume_count = len(created_list)
    if volume_count > 0:
        volume_creation_name = created_list[0].inner_text()
        print(volume_creation_name)
        logging.info("displayed the created_port_security name:", volume_creation_name)
    else:
        logging.info("created_port_security is not created.")


@pytest.mark.testrail(65570)
def test_Verify_Lbass_manage_Label_action(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    page.wait_for_timeout(TIMEOUT)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.lbass_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    items_to_verify = ["Manage Labels", "Delete"]
    fill_the_manage_label_for_selected_feature(page, items_to_verify)


@pytest.mark.testrail(65864)
def test_Verify_Lbass_delete_action(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    page.wait_for_timeout(TIMEOUT)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.lbass_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    items_to_verify = ["Manage Labels", "Delete"]
    delete_the_action_for_selected_feture(page, items_to_verify)


@pytest.mark.testrail(65571)
def test_Reserve_Public_IP_feature(page, create_reservePublicIP):
    page.wait_for_timeout(1000)
    yes_button_element = page.get_by_test_id(locators['CONFIRM_BUTTON'])
    assert yes_button_element.is_visible(), "Yes button is not visible."
    yes_button_element.click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == ComputeTextData.ip_address_toast_msg, f"The toast message '{toast_text}' is different than expected: '{expected_toast_msg}'"
    expect(page.get_by_test_id(locators['IP_ADDRESS_HEADER'])).to_be_visible()

@pytest.mark.testrail(65572)
def test_Verify_the_Global_Cloud_Konnect_form_creation(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    page.wait_for_timeout(TIMEOUT)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.gck_network in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['GCK_HEADER'])).to_be_visible()
    gck_page_heading = page.get_by_test_id(locators['GCK_HEADER'])
    page_heading = gck_page_heading.inner_text()
    assert page_heading == "Global Cloud Konnect", "User could not be navigated to Global Cloud Konnect page header!!"
    logging.info("User successfully navigated to Global Cloud Konnect homepage  screen!")

@pytest.mark.testrail(65573)
def test_Verify_the_Internet_sevice_peering_form_creation(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    page.wait_for_timeout(TIMEOUT)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.isp_network in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['IPS_HEADER'])).to_be_visible()
    ips_page_heading = page.get_by_test_id(locators['IPS_HEADER'])
    page_heading = ips_page_heading.inner_text()
    assert page_heading == "Internet Peering Services", "User could not be navigated to Internet Peering Services page header!!"
    logging.info("User successfully navigated to Internet Peering Services homepage  screen!")


@pytest.mark.testrail(65574)
def test_verify_Firewall_creation(page):
    # to_create_virtual_Compute_machine(page)
    # page.wait_for_timeout(10000)
    # test_Verify_the_VM_Attach_Public_IP_action(page, tejas_setup)
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    security_page_heading = page.get_by_test_id(locators['SECURITY_HEADER'])
    Security_header = security_page_heading.inner_text()
    page.wait_for_timeout(1000)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.firewall_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    perform_click_on_compute_resource(page, locators['FIREWALL_CREATE_BTN'])
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['FIREWALL_HEADER'])).to_be_visible()
    yes_button_element = page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON'])
    assert yes_button_element.is_visible(), "Create button is not visible."
    yes_button_element.click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    expect(page.get_by_test_id(locators['FIREWALL_RESULT'])).to_be_visible()



@pytest.mark.testrail(65575)
def test_verify_VPNaaS_creation(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    security_page_heading = page.get_by_test_id(locators['SECURITY_HEADER'])
    Security_header = security_page_heading.inner_text()
    page.wait_for_timeout(1000)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.vpnass_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['VPN_HEADER'])).to_be_visible()
    perform_click_on_compute_resource(page, locators['CREATE_VPN'])
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['VPN_HEADER'])).to_be_visible()
    clear_and_fill_field(page, locators['VPN_NAME_FIELD'], MACHINE_NAME)

    save_config_element = page.get_by_test_id(locators['VPN_BTN_SAVE'])
    assert save_config_element .is_visible(), "Save Config is not visible."
    page.get_by_test_id(locators['CANCEL_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    expect(page.get_by_test_id(locators['VPN_HEADER'])).to_be_visible()


@pytest.mark.testrail(65576)
def test_verify_SSL_Certificate_creation(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    security_page_heading = page.get_by_test_id(locators['SECURITY_HEADER'])
    Security_header = security_page_heading.inner_text()
    page.wait_for_timeout(1000)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.sslcertificate_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['SSL_CERT_HEADER'])).to_be_visible()
    perform_click_on_compute_resource(page, locators['SSL_CERT_CREATE_BTN'])
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page_heading = page.get_by_test_id(locators['CONFIRMATION_TEXT'])
    heading_text = page_heading.inner_text()
    assert heading_text == "Upload SSL Certificate", "User could not be navigated to Upload SSL Certificate header!!"
    logging.info("User successfully navigated to Upload SSL Certificate  screen!")
    page.get_by_test_id(locators['CLOSE_BTN']).click()
    expect(page.get_by_test_id(locators['SSL_CERT_HEADER'])).to_be_visible()


@pytest.mark.testrail(65577)
def test_verify_DDos_form_creation(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    security_page_heading = page.get_by_test_id(locators['SECURITY_HEADER'])
    Security_header = security_page_heading.inner_text()
    page.wait_for_timeout(1000)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.ddos_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['DDOS_HEADER'])).to_be_visible()
    ddos_page_heading = page.get_by_test_id(locators['DDOS_HEADER'])
    page_heading = ddos_page_heading.inner_text()
    assert page_heading == "DDoS", "User could not be navigated to DDoS page header!!"
    logging.info("User successfully navigated to DDoS page  screen!")

@pytest.mark.testrail(65697)
def test_verify_VAPT_Service_form_creation(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    security_page_heading = page.get_by_test_id(locators['SECURITY_HEADER'])
    Security_header = security_page_heading.inner_text()
    page.wait_for_timeout(1000)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.vapt_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['VPAT_SERVICE_HEADER'])).to_be_visible()
    vapt_service_page_heading = page.get_by_test_id(locators['VPAT_SERVICE_HEADER'])
    page_heading = vapt_service_page_heading.inner_text()
    assert page_heading == "VAPT Service", "User could not be navigated to VAPT Service page header!!"
    logging.info("User successfully navigated to VAPT Servicepage  screen!")


@pytest.mark.testrail(65578)
def test_verify_PAM_form_creation(page):
    perform_click_on_compute_resource(page, locators['SECURITY_TAB'])
    expect(page.get_by_test_id(locators['SECURITY_HEADER'])).to_be_visible()
    security_page_heading = page.get_by_test_id(locators['SECURITY_HEADER'])
    Security_header = security_page_heading.inner_text()
    page.wait_for_timeout(1000)
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.pam_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['PAM_HEADER'])).to_be_visible()
    pam_page_heading = page.get_by_test_id(locators['PAM_HEADER'])
    page_heading = pam_page_heading.inner_text()
    assert page_heading == "PAM", "User could not be navigated to PAMService page header!!"
    logging.info("User successfully navigated to PAM page  screen!")

def select_file(file_path):
    print(f"Manually select the file from the dialog: {file_path}")

@pytest.mark.testrail(65580)
def test_verify_Stack_creation(page):
    perform_click_on_compute_resource(page, locators['AUTOMATION_TAB'])
    expect(page.get_by_test_id(locators['AUTOMATION_HEADER'])).to_be_visible()
    network_page_heading = page.get_by_test_id(locators['AUTOMATION_HEADER'])
    networking_header = network_page_heading.inner_text()
    assert networking_header == "Automation", "User could not be navigated to automation section!!"

    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.stack_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['STACK_HEADER'])).to_be_visible()
    pam_page_heading = page.get_by_test_id(locators['STACK_HEADER'])
    page_heading = pam_page_heading.inner_text()
    assert page_heading == "Stacks", "User could not be navigated to STACK_HEADER header!!"
    logging.info("User successfully navigated to STACK_HEADER page  screen!")

    page.get_by_test_id(locators['STACK_CREATE_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['STACK_NAME_FIELD'], "Tejas Compute")
    page.get_by_test_id(locators['UPLOAD_FILE']).click()
    time.sleep(1)
    #pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('file_dialog.png')))
    #file_path = "/Users/atultayade/Documents/Git/yntraa_test_automation/test_helper/downloadFile/volume_template.yaml"
    file_path = "/test_helper/downloadFile/volume_template.yaml"
    # yaml_file = "downloadFile/volume_template.yaml"
    # file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), yaml_file)
    for char in file_path:
        pyautogui.write(char)
    #pyautogui.write(file_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    page.wait_for_timeout(10000)
    page.get_by_test_id(locators['SELECTED_FILE']).inner_text()

@pytest.mark.testrail(65581)
def test_Verify_the_Edge_Sites(page):
    perform_click_on_compute_resource(page, locators['EDGE_SIDE_TAB'])
    expect(page.get_by_test_id(locators['EDGE_SIDE_HEADER'])).to_be_visible()
    Edge_Site_page_heading = page.get_by_test_id(locators['EDGE_SIDE_HEADER'])
    Edge_Site_header = Edge_Site_page_heading.inner_text()
    assert Edge_Site_header == "My Edge Site", "User could not be navigated to My_Edge_Site section!!"
    logging.info("User successfully navigated to My_Edge_Site  screen!")
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.edge_side_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['EDGE_SIDE_HEADER'])).to_be_visible()

#@pytest.mark.testrail(65582)
#Verify that user is redirected to Orbiter portal upon clicking CaaS feature

@pytest.mark.testrail(65583)
def test_verify_the_database_cluster_creation(page):
    perform_click_on_compute_resource(page, locators['MANAGED_DATABASE_TAB'])
    expect(page.get_by_test_id(locators['MANAGED_DATABASE_HEADER'])).to_be_visible()
    Edge_Site_page_heading = page.get_by_test_id(locators['MANAGED_DATABASE_HEADER'])
    Edge_Site_header = Edge_Site_page_heading.inner_text()
    assert Edge_Site_header == "Managed Database", "User could not be navigated to Managed Database section!!"
    logging.info("User successfully navigated to Managed Database screen!")
    page.locator(locators['DATABASE_TABB']).click()
    expect(page.get_by_test_id(locators['DATABASE_HEADER'])).to_be_visible()
    expect(page.get_by_test_id(locators['DATABASE_CREATE_BTN'])).to_be_visible()
    page.get_by_test_id(locators['DATABASE_CREATE_BTN']).click()
    expect(page.get_by_test_id(locators['DATABASE_HEADER'])).to_be_visible()
    clear_and_fill_field(page, locators['DATABASE_INPUT_FIELD'], MACHINE_NAME)
    clear_and_fill_field(page, locators['DATABASE_CREADS_FIELD'], MACHINE_NAME)
    clear_and_fill_field(page, locators['DB_PASS_FIELD'], "India@143")
    clear_and_fill_field(page, locators['DB_CNF_PASS_FIELD'], "India@143")
    
    
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    page.get_by_test_id(locators['CONFIRMATION_TEXT']).click()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    List_elements = page.query_selector_all(f'[data-testid="list-card"]')
    list_count = len(List_elements)
    logging.info(list_count)


@pytest.mark.testrail(65584)
def test_Verify_that_user_is_able_to_raise_ticket(page):
    perform_click_on_compute_resource(page, locators['SUPPORT_TAB'])
    expect(page.get_by_test_id(locators['SUPPORT_HEADER'])).to_be_visible()
    support_page_heading = page.get_by_test_id(locators['SUPPORT_HEADER'])
    support_header = support_page_heading.inner_text()
    assert support_header == "Support", "User could not be navigated to Support section!!"
    logging.info("User successfully navigated to Support  screen!")
    page.locator(locators['TICKET_E']).click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['TICKET_BTN_CREATE'])).to_be_visible()
    page.get_by_test_id(locators['TICKET_BTN_CREATE']).click()
    expect(page.get_by_test_id(locators['HEADING_SUPPORT'])).to_be_visible()
    page.wait_for_timeout(10000)

    expect(page.locator(locators['TICKET_CATEGORY'])).to_be_visible()
    page.locator(locators['TICKET_CATEGORY']).click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="category-select-option"]')
    count = len(Dropdown_elements)
    other_option_found = False
    for index, element in enumerate(Dropdown_elements, start=1):
        element_text = element.inner_text()
        if "Other" in element_text:
            other_option_found = True
            element.click()
            print("Clicked on Other")
            break
    page.wait_for_timeout(TIMEOUT)

    page.locator(locators['TICKET_SUBCATEGORY']).click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="sub-category-select-option"]')
    count = len(Dropdown_elements)
    for index, element in enumerate(Dropdown_elements, start=1):
        element_text = element.inner_text()
        if "Other" in element_text:
            element.click()
            print("Clicked on Other")
            break
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['TICKET_SUBJECT'], "Unable to create VM")
    clear_and_fill_field(page, locators['TICKET_MESSAGE'], "Unable to create VM")

    expect(page.get_by_test_id(locators['TICKET_ATTCHED'])).to_be_visible()
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    page.get_by_test_id(locators['CONFIRMATION_TEXT']).click()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Ticket raised successfully."

@pytest.mark.testrail(65585)
def test_Verify_Quota_Request(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    page.locator(locators['QUOTA_BTN']).click()
    expect(page.get_by_test_id(locators['QUOTA_SERVICE_HEADER'])).to_be_visible()
    page.get_by_test_id(locators['QUOTA_CREATE_BTN']).click()
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['QUOTA_SERVICE_HEADER'])).to_be_visible()
    page.locator(locators['QUOTA_INCREASE_VM']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_text("Request Upgrade")).to_be_visible()
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Quota requested successfully."
    toast_text = page.locator(locators['REQUEST_STATUS']).inner_text()
    assert toast_text == "Submitted for approval"

@pytest.mark.testrail(65586)
def test_Verify_Cancellation_Quota_Request(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    page.locator(locators['QUOTA_BTN']).click()
    expect(page.get_by_test_id(locators['QUOTA_SERVICE_HEADER'])).to_be_visible()
    expect(page.locator(locators['REQUEST_ID'])).to_be_visible()

    createdId = page.locator(locators['REQUEST_ID']).inner_text()
    page.locator(locators['REQUEST_ID']).click()
    createdId_afterclick = page.locator(locators['CREATED_R_ID']).inner_text()
    #assert createdId == createdId_afterclick
    expect(page.get_by_test_id(locators['QUOTA_CANCEL_BTN'])).to_be_visible()
    page.get_by_test_id(locators['QUOTA_CANCEL_BTN']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    copy_to_clipboard_and_paste_value_function(page)
    # assert toast_text == "Quota request cancellation in progress."
    page.wait_for_timeout(10000)
    toast_text = page.locator(locators['REQUEST_STATUS']).inner_text()
    assert toast_text == "Cancelled"
    page.get_by_test_id(locators['BACK_BTN']).click()
    expect(page.get_by_test_id(locators['QUOTA_SERVICE_HEADER'])).to_be_visible()

