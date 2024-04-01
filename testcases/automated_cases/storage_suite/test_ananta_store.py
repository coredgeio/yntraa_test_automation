from test_helper.testdata.storage_testdata import StorageTextData
from pages.resources.storage.storage_page import *
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from pages.resources.storage.ananta_store_page import *


@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "vini-sdet@yopmail.com",
        "password": "India@143"
    }


"""Perform a click operation on Storage Resource and verify the header on the resulting landing page."""
@pytest.mark.testrail(27651)
def test_redirecting_to_home_page_screen_by_clicking_on_storage(page):
    perform_click_on_storage_resource(page, locators['STORAGE_TAB'])
    storage_header_element = page.get_by_test_id(locators['STORAGE_HEADER'])
    storage_header_value = storage_header_element.inner_text()
    assert storage_header_value == StorageTextData.storage_header, "User could not be navigated to storage page!!"
    logging.info("User has successfully navigated to Storage page!")

@pytest.mark.testrail(27652)
def test_verify_UI_of_storage_home_screen(page, storage_setup):
    expect(page.get_by_test_id(locators['STORAGE_HEADER'])).to_be_visible()
    expect(page.get_by_test_id(locators['STORAGE_DESCRP'])).to_be_visible()
    expect(page.locator(locators['COMPUTE_CREATE_BUTTON'])).to_be_visible()

    tabs = page.query_selector_all('#tab-id')
    for text in StorageTextData.storage_all_tabs:
        assert text == page.query_selector_all(f'[data-testid="{locators["STORAGE_FEATURES"]}"]')

@pytest.mark.testrail(27292)
def test_verify_UI_of_compute_home_screen(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_DESCRP'])).to_be_visible()
    expected_texts = ["Tejas Compute", "Snapshots", "Vistaar", "Swayam Run"]
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
    expect(page.locator(locators['COMPUTE_CREATE_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['COMPUTE_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['DEPLOY_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['DATABASE_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['PLATFORM_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['MANAGED_DATABASE_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['QUICK_LINK'])).to_be_visible()
    expect(page.get_by_test_id(locators['LEARN_MORE_TAB'])).to_be_visible()
    # expect(page.get_by_test_id(locators['MY_EDGE_SITE_TAB'])).to_be_visible()