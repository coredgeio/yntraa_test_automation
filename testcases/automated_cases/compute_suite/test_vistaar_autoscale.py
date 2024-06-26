import traceback

from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from test_helper.testdata.compute_testdata import ComputeTextData

@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "vini-sdet@yopmail.com",
        "password": "India@143"
    }


"""Constant and Global Tejas Compute VM Name!"""
MACHINE_NAME = generate_random_machine_name()
def verify_to_session_logout(page):
    verify_to_logout_function(page)

# @pytest.fixture(autouse=True)
# def logout_after_test(request, page):
#     yield
#     verify_to_session_logout(page)

"""Perform a click operation on Compute Resource and verify the header on the resulting landing page."""
@pytest.mark.testrail(27291)
def test_to_verify_clicking_on_compute_screen(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    compute_page_heading = page.locator(locators['COMPUTE_HEADER']).text_content()
    assert compute_page_heading == ComputeTextData.compute_header, "User could not be navigated to Compute module!!"
    logging.info("User has successfully navigated to Compute module!")
    #verify_to_logout_function(page)

@pytest.mark.testrail(27292)
def test_verify_UI_of_compute_home_screen(page, compute_setup):
    expect(page.locator(locators['COMPUTE_HEADER'])).to_be_visible()
    expect(page.locator(locators['COMPUTE_DESCRP'])).to_be_visible()
    expect(page.locator(locators['COMPUTE_CREATE_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['STORAGE_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['NETWORKING_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['SECURITY_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['AUTOMATION_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['MY_EDGE_SITE_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['CAAS_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['MANAGED_DATABASE_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['SUPPORT_TAB'])).to_be_visible()
    #verify_to_logout_function(page)


