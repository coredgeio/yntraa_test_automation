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
import pyautogui



@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "atul_srsdet@yopmail.com",
        "password": "India@143"
    }

"Verify Documentation Screen - Clicking on same should redirect the user to the Yntraa Documentation page - Link : https://docs-revamp-sbx.yntraa.com/"
@pytest.mark.testrail(65503)
def test_user_redirected_to_yntraa_documentation_page(page):
    with page.expect_popup() as page1_info:
        expect(page.get_by_test_id(locators['DOCUMENTATION_SIDEBAR'])).to_be_visible()
        page.get_by_test_id(locators['DOCUMENTATION_SIDEBAR']).click()
        page.wait_for_timeout(10000)
    page1 = page1_info.value
    page1.wait_for_timeout(10000)
    page1.locator(locators['YNTRAA_DOCUMENT_SCREEN']).is_visible()
    page1.locator(locators['YNTRAA_DOCUMENT_DESC_SCREEN']).is_visible()
    document_screen = page1.locator(locators['YNTRAA_DOCUMENT_SCREEN']).inner_text()
    logging.info("document_screen:", document_screen)
    page1.close()
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()

"Verify CaaS screen - Clicking on same should redirect to Orbitor screen with same loggedin user profile. "
@pytest.mark.testrail(65494)
def test_caas_screen_redirects_to_orbitor_screen_with_same_profile(page):
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    profile_name = page.get_by_test_id(locators['PROFILE_USENAME'])
    Yntraa_profile_name = profile_name.inner_text()
    page.locator("body > div:nth-child(7) > .MuiBackdrop-root").click()
    page.get_by_test_id(locators['YNTRAA_PROJECT']).click()
    page.wait_for_timeout(1000)
    with page.expect_popup() as page1_info:
        expect(page.get_by_test_id(locators['CAAS_TAB'])).to_be_visible()
        page.get_by_test_id(locators['CAAS_TAB']).click()
        page.wait_for_timeout(10000)
    page1 = page1_info.value
    page1.wait_for_timeout(10000)
    if page.get_by_role("button", name="Sign In").is_visible():
        page.get_by_role("button", name="Sign In").click()
        username_input = page.query_selector("input#username")
        username_input.fill("atul_srsdet@yopmail.com")
        password_input = page.query_selector("input#password")
        password_input.fill("India@143")
        login_button = page.query_selector("input#kc-login")
        login_button.click()
        page.wait_for_load_state("load")
    else:
        expect(page1.get_by_test_id(locators['ORBITER_DASHBOARD'])).to_be_visible()
        page1.locator(locators['ORBITER_CLUSTER_TAB']).is_visible()
        page1.locator(locators['ORBITER_INSTANCES_TAB']).is_visible()
        dashboard_screen = page1.get_by_test_id(locators['ORBITER_DASHBOARD']).inner_text()
        logging.info("orbiter dashboard_screen:", dashboard_screen)
        caas_profile_name = page1.locator(locators['ORBITER_PROFILE_NAME']).inner_text()
        logging.info("orbiter profile_name:", caas_profile_name)
        assert caas_profile_name == Yntraa_profile_name
    page1.close()
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()




@pytest.mark.testrail(65582)
def test_redirect_to_orbiter_upon_clicking_caas(page):
    with page.expect_popup() as page1_info:
        expect(page.get_by_test_id(locators['CAAS_TAB'])).to_be_visible()
        page.get_by_test_id(locators['CAAS_TAB']).click()
        page.wait_for_timeout(10000)
    page1 = page1_info.value
    page1.wait_for_timeout(10000)
    expect(page1.get_by_test_id(locators['ORBITER_DASHBOARD'])).to_be_visible()
    page1.locator(locators['ORBITER_CLUSTER_TAB']).is_visible()
    page1.locator(locators['ORBITER_INSTANCES_TAB']).is_visible()
    dashboard_screen = page1.get_by_test_id(locators['ORBITER_DASHBOARD']).inner_text()
    logging.info("orbiter dashboard_screen:", dashboard_screen)

    page1.get_by_test_id(locators['ORBITER_OVERVIEWTAB']).click()
    page1.wait_for_timeout(10000)
    expect(page1.get_by_test_id(locators['ORBITER_OVERVIEW_HEADER'])).to_be_visible()
    expect(page1.get_by_test_id(locators['ORBITER_OVERVIEW_HEADER'])).to_be_visible()
    orbiter_welcome_screen = page1.locator(locators['ORBITER_WELCOME_SCREEN']).inner_text()
    logging.info("You are now flying through default-project zone:", orbiter_welcome_screen)
    page1.close()
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()

@pytest.mark.testrail(65699)
def test_user_is_able_to_navigate_to_yntraa_documentation_page(page):
    with page.expect_popup() as page1_info:
        expect(page.get_by_test_id(locators['DOCUMENTATION_SIDEBAR'])).to_be_visible()
        page.get_by_test_id(locators['DOCUMENTATION_SIDEBAR']).click()
        page.wait_for_timeout(10000)
    page1 = page1_info.value
    page1.wait_for_timeout(10000)
    page1.locator(locators['YNTRAA_DOCUMENT_SCREEN']).is_visible()
    page1.locator(locators['YNTRAA_DOCUMENT_DESC_SCREEN']).is_visible()
    document_screen = page1.locator(locators['YNTRAA_DOCUMENT_SCREEN']).inner_text()
    logging.info("document_screen:", document_screen)
    page1.close()
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()

@pytest.mark.testrail(65458)
def test_user_redirected_to_yotta_environment(page):
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    copy_to_clipboard_button = page.get_by_test_id(locators['ONE_TOTTA_BTN'])
    expect(copy_to_clipboard_button).to_be_visible()
    with page.expect_popup() as page1_info:
        page.get_by_test_id("btn-one-yotta").click()
    page1 = page1_info.value
    page1.wait_for_timeout(200000)
    page1.wait_for_timeout(10000)

    expect(page.get_by_test_id("heading-dashboard")).to_be_visible()
    page1.locator(locators['BILLING_PAGE_INFO']).is_visible()
    page1.locator(locators['BILLING_PAGE_TICKET']).is_visible()
    page1.locator(locators['BILLING_PAGE_SERVVICE']).is_visible()
    page1.close()
    page.wait_for_timeout(1000)
    page.locator("body > div:nth-child(7) > .MuiBackdrop-root").click()
    page.get_by_test_id(locators['YNTRAA_PROJECT']).click()
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()


@pytest.mark.testrail(65459)
def test_user_profile_poupup_redirected_to_billing_screen_upon_cliking_billing(page):
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['YNTRAA_USERPROFILE'])).to_be_visible()
    page.get_by_test_id(locators['YNTRAA_USERPROFILE']).click()
    email_element = page.get_by_test_id(locators['PROFILE_EMAIL'])
    expect(email_element).to_be_visible()
    copy_to_clipboard_button = page.get_by_test_id(locators['BILLING_BTN'])
    expect(copy_to_clipboard_button).to_be_visible()
    with page.expect_popup() as page1_info:
        page.get_by_test_id("btn-billing").click()
    page1 = page1_info.value
    page1.wait_for_timeout(200000)
    page1.wait_for_timeout(10000)

    expect(page.get_by_test_id("heading-dashboard")).to_be_visible()
    #expect(page.query_selector(".brand-logo")).to_be_visible()
    page1.locator(locators['BILLING_PAGE_INFO']).is_visible()
    page1.locator(locators['BILLING_PAGE_TICKET']).is_visible()
    page1.locator(locators['BILLING_PAGE_SERVVICE']).is_visible()
    page1.locator(locators['BILLING_PAGE_INFO']).click()
    page1.locator(locators['BILLING_INVOICE_INFORMATION']).is_visible()
    page1.locator(locators['BILLING_INVOICE']).is_visible()
    page1.close()
    page.wait_for_timeout(1000)
    page.locator("body > div:nth-child(7) > .MuiBackdrop-root").click()
    page.get_by_test_id(locators['YNTRAA_PROJECT']).click()
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()


@pytest.mark.testrail(65561)
def test_verify_the_yotta_safe(page):
    with page.expect_popup() as page1_info:
        perform_click_on_compute_resource(page, locators['STORAGE_TAB'])
        page.wait_for_timeout(TIMEOUT)
        compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
        for index, element in enumerate(compute_header_elements, start=1):
            element_text = element.inner_text()
            if ComputeTextData.yotta_safe_tab in element_text:
                element.click()
    page1 = page1_info.value
    page1.wait_for_timeout(10000)
    #expect(page.get_by_test_id("YOTTA_SAFE_LOGO")).to_be_visible()
    page1.locator(locators['WEB_CONSOLE']).is_visible()
    page1.close()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['YNTRAA_PROJECT']).click()
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['YNTRAA_HEADER_PAGE'])).to_be_visible()

