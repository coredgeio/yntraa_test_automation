import pytest
import logging
from test_helper.yantra_element_locators.compute_element import TejasComputeLocators
from modules.resources.compute.compute_page import *

@pytest.fixture(scope='module')
def tejas_setup(page, compute_setup):
    perform_click_on_tejas_tab(page, TejasComputeLocators.TEJAS_COMPUTE_TAB)
    page.wait_for_timeout(2000)

@pytest.fixture(scope='module')
def tejas_create_vm_setup(page, tejas_setup):
    create_vm_button_locator = page.locator(TejasComputeLocators.CREATE_VM_BUTTON)
    if create_vm_button_locator.is_visible():
        perform_click_on_create_vm_button(page, TejasComputeLocators.CREATE_VM_BUTTON)
    else:
        create_vm_header = page.locator(TejasComputeLocators.CREATE_VM_HEADER)
        if create_vm_header.is_visible():
            logging.info("Header on the next page is visible. Performing next operation.")
        else:
            logging.info("Neither 'Create VM' button nor expected header found.")

def perform_click_on_tejas_tab(page, selector, timeout=1000):
    page.wait_for_timeout(timeout)
    page.wait_for_selector(selector).click()

def perform_click_on_create_vm_button(page, selector, timeout=1000):
    page.wait_for_timeout(timeout)
    page.wait_for_selector(selector).click()
