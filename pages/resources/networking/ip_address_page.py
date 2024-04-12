""" Common fixtures and methods for Network section of the application. """
import pytest
from test_helper.library.required_library import *
from pages.resources.compute.compute_page import *
from test_helper.testdata.compute_testdata import ComputeTextData

""" Fixture to click on Networking tab."""
@pytest.fixture(scope='module')
def ip_address_setup(page, network_setup):
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.ip_address_section in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)

""" Fixture to click on Kshetra tab."""
@pytest.fixture(scope='module')
def kshetra_setup(page, network_setup):
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.kshetra_network in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)

@pytest.fixture(scope='module')
def create_kshetra_network(page, kshetra_setup):
    create_vm_button_locator = page.get_by_test_id(locators['CREATE_NETWORK_BTN'])
    if create_vm_button_locator.is_visible():
        perform_click_on_compute_resource(page, locators['CREATE_NETWORK_BTN'])
    else:
        create_vm_header = page.locator(locators['SECTION_HEADER_NAME'])
        if create_vm_header.is_visible():
            logging.info("Header on the next page is visible. Performing next operation.")
        else:
            logging.info("Neither 'create network' button nor expected header found.")



""" Common fixtures and methods for Network of the application. """
@pytest.fixture(scope='module')
def network_setup(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    page.wait_for_timeout(TIMEOUT)

""" Fixture to click on reserve_public_ip_button."""
@pytest.fixture(scope='module')
def create_reservePublicIP(page, ip_address_setup):
    create_vm_button_locator = page.get_by_test_id(locators['IP_CREATE_BTN'])
    if create_vm_button_locator.is_visible():
        perform_click_on_compute_resource(page, locators['IP_CREATE_BTN'])
    else:
        create_vm_header = page.locator(locators['SECTION_HEADER_NAME'])
        if create_vm_header.is_visible():
            logging.info("Header on the next page is visible. Performing next operation.")
        else:
            logging.info("Neither 'Create Reserved Ip' button nor expected header found.")
