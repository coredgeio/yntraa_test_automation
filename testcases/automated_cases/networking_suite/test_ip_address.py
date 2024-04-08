import logging
import pytest
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from pages.resources.networking.ip_address_page import *
from test_helper.testdata.compute_testdata import ComputeTextData
import asyncio

@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "qa-test-user002@yopmail.com",
        "password": "India@143"
    }


"""Verify user is able to redirect to Networking screen by clicking on Networking  """
@pytest.mark.testrail(27421)
def test_verify_user_is_able_to_redirect_to_networking_screen_by_clicking_on_networking(page, network_setup):
    expect(page.get_by_test_id(locators['NETWORK_HEADER'])).to_be_visible()
    snapshot_compute_page_heading = page.get_by_test_id(locators['NETWORK_HEADER'])
    snapshot_page_heading = snapshot_compute_page_heading.inner_text()
    assert snapshot_page_heading == "Networking", "User could not be navigated to Compute snapshot section!!"
    logging.info("User successfully navigated to Compute snapshot screen!")
    page.wait_for_timeout(10000)

