""" Common fixtures and methods for Tejas Compute section of the application. """
import pytest
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

@pytest.fixture(scope='module')
def snapshots_setup(page, compute_setup):
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.compute_snapshot_tab in element_text:
            element.click()
@pytest.fixture(scope='module')
def create_compute_sanpshots(page, snapshots_setup):
    create_snapshot_button = page.get_by_test_id(locators['SNAPSHOTE_CREATE_COMPUTE'])
    if create_snapshot_button.is_visible():
        perform_click_on_create_vm_button(page, locators['SNAPSHOTE_CREATE_COMPUTE'])
    else:
        create_vm_header = page.locator(locators['CONFIRMATION_TEXT'])
        if create_vm_header.is_visible():
            logging.info("Header on the next page is visible. Performing next operation.")
        else:
            logging.info("Neither 'Create SNAPSHOTS' button nor expected header found.")

""" Method to perform click on Create VM Button. """
def perform_click_on_create_vm_button(page, selector):
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(selector).click()

def verify_to_click_tejas_compute_tab(page):
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        print(element_text)
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)

"""Constant and Global Tejas Compute VM Name!"""
MACHINE_NAME = generate_random_machine_name()

def to_create_virtual_Compute_machine(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    verify_to_click_tejas_compute_tab(page)
    perform_click_on_create_vm_button(page, locators['CREATE_VM_BUTTON'])
    page.locator(locators['NAME_FIELD']).fill("")
    page.locator(locators['NAME_FIELD']).type(MACHINE_NAME)
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    page.wait_for_timeout(1000)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    if compute_header_count > 0:
        compute_header_elements[5].click()
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.wait_for_timeout(1000)
    page.locator(locators['KEY_PAIR_PLACEHOLDER']).click()
    compute_header_elements1 = page.query_selector_all(f'[data-testid="keypair-id-select-option"]')
    compute_header_count = len(compute_header_elements1)
    if compute_header_count > 0:
        compute_header_elements1[0].click()
    page.wait_for_timeout(1000)
    page.get_by_test_id('label-input').click()
    valid_label = f"atul-sdet"
    page.fill(locators['INPUT_LABEL'], valid_label)
    page.locator(locators['ADD_LABEL_BTN']).click()
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Creating virtual machine"
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
def to_delete_the_created_virtual_machine(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    verify_to_click_tejas_compute_tab(page)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Delete":
                item.click()
                print("Clicked on delete")
                break
    page.wait_for_timeout(10000)
    button_locator = "(//button[@data-testid='btn-copy-clipboard'])[last()]"
    page.locator(button_locator).click()
    input_locator = "//input[@id='name']"
    input_element = page.locator(input_locator)
    input_element.focus()
    page.keyboard.down("Meta")
    page.keyboard.press("V")
    page.keyboard.up("Meta")
    page.wait_for_timeout(1000)
    pasted_text = input_element.evaluate('(el) => el.value')
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    page.wait_for_timeout(1000)
    #assert toast_text == "Deleting virtual machine"
    page.wait_for_timeout(10000)

def clear_and_fill_field(page, locator, value):
    page.locator(locator).fill("")  # Clear the field
    page.fill(locator, value)
