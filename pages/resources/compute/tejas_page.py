""" Common fixtures and methods for Tejas Compute section of the application. """
from test_helper.library.required_library import *
from pages.resources.compute.compute_page import *
from test_helper.testdata.compute_testdata import ComputeTextData


""" Fixture to click on Tejas Compute tab."""
@pytest.fixture(scope='module')
def tejas_setup(page, compute_setup):
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)


""" Fixture to click on Create Virtual Machine button."""
@pytest.fixture(scope='module')
def tejas_create_vm_setup(page, tejas_setup):
    create_vm_button_locator = page.get_by_test_id(locators['CREATE_VM_BUTTON'])
    if create_vm_button_locator.is_visible():
        perform_click_on_create_vm_button(page, locators['CREATE_VM_BUTTON'])
    else:
        create_vm_header = page.locator(locators['CREATE_VM_HEADER'])
        if create_vm_header.is_visible():
            logging.info("Header on the next page is visible. Performing next operation.")
        else:
            logging.info("Neither 'Create VM' button nor expected header found.")

""" Method to perform click on Tejas Compute. """
def perform_click_on_tejas_tab(page, selector):
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(selector).click()

""" Method to perform click on Create VM Button. """
def perform_click_on_create_vm_button(page, selector):
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(selector).click()
