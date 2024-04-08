import logging
import pytest
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from pages.resources.storage.ananta_store_page import *
from test_helper.testdata.storage_testdata import StorageTextData
from pages.resources.storage.storage_page import *


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


@pytest.mark.testrail(27653)
def test_verify_header_of_storage_home_screen(page, storage_setup):
    expect(page.get_by_test_id(locators['STORAGE_HEADER'])).to_be_visible()
    storage_header = page.get_by_test_id(locators['STORAGE_HEADER']).inner_text()
    assert storage_header == StorageTextData.storage_header, "User could not found the Storage Header"

@pytest.mark.testrail(27654)
def test_verify_description_under_storage_header(page, storage_setup):
    expect(page.get_by_test_id(locators['STORAGE_DESCRP'])).to_be_visible()
    storage_descp = page.get_by_test_id(locators['STORAGE_DESCRP']).inner_text()
    assert storage_descp == StorageTextData.storage_description, "User could not found the Description under Storage Header"

@pytest.mark.testrail(27654)
def test_redirecting_to_ananta_store_screen_by_clicking_on_ananta_store(page, storage_setup):
    tab = page.query_selector_all(f'[data-testid="{locators["STORAGE_FEATURES"]}"]')
    for feature in tab:
        text = feature.inner_text()
        if text == StorageTextData.storage_all_tabs[1]:
            feature.click()
            header = page.get_by_test_id(locators['ANANTA_HEADER']).inner_text()
            print(header)
            assert header == StorageTextData.ananta_header, "User could not redirected to Ananta Store Screen!!"

@pytest.mark.testrail(65130)
def test_verify_header_of_ananta_store_page(page,ananta_setup):
    expect(page.get_by_test_id(locators['ANANTA_HEADER'])).to_be_visible()
    header = page.get_by_test_id(locators['ANANTA_HEADER']).inner_text()
    assert header == StorageTextData.ananta_header, "User could not found the Ananta Store page Header!!"

@pytest.mark.testrail(65131)
def test_verify_desc_of_ananta_store_page(page,ananta_setup):
    expect(page.get_by_test_id(locators['ANANTA_DESCRP'])).to_be_visible()
    descp = page.get_by_test_id(locators['ANANTA_DESCRP']).inner_text()
    assert descp == StorageTextData.ananta_description, "User could not found the Ananta Store page Description!!"

@pytest.mark.testrail(27656)
def test_redirecting_to_create_volume_screen_by_clicking_on_create_volume(page,ananta_setup):
     expect(page.get_by_test_id(locators['CREATE_VOL_BUTTON'])).to_be_visible()
     page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
     page.wait_for_timeout(TIMEOUT)
     vol_create_page = page.get_by_test_id(locators['CREATE_VOL_HEADER']).inner_text()
     assert vol_create_page == StorageTextData.create_vol_header, "User could not found the Volume Creation page Header!!"


