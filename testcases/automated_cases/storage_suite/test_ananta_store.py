from test_helper.testdata.storage_testdata import StorageTextData
from pages.resources.storage.storage_page import *
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *


@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "vini-sdet@yopmail.com",
        "password": "India@143"
    }

@pytest.mark.testrail(27651)
def test_redirecting_to_home_page_screen_by_clicking_on_storage(page):
    perform_click_on_storage_resource(page, locators['STORAGE_TAB'])
    storage_header_element = page.get_by_test_id(locators['STORAGE_HEADER']).inner_text()
    assert storage_header_element == StorageTextData.storage_header, "User could not be navigated to Compute module!!"
    logging.info("User has successfully navigated to Storage module!")

@pytest.mark.testrail(27652)
def test_verify_UI_of_storage_home_screen(page, storage_setup):
    expect(page.get_by_test_id(locators['STORAGE_HEADER'])).to_be_visible()
    expect(page.get_by_test_id(locators['STORAGE_DESCRP'])).to_be_visible()
    for text in StorageTextData.storage_all_tabs:
        assert text == page.query_selector_all(f'[data-testid="{locators["STORAGE_FEATURES"]}"]')
