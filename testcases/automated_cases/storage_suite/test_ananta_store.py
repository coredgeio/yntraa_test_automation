import logging
import pytest
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from pages.resources.storage.ananta_store_page import *
from test_helper.testdata.storage_testdata import StorageTextData
from pages.resources.storage.storage_page import *
from pages.resources.compute.compute_page import *



@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "techiee@yopmail.com",
        "password": "India@143"
    }

"""Constant and Global Volume Name!"""
VOLUME_NAME = generate_random_machine_name()

"""Perform a click operation on Storage Resource and verify the header on the resulting landing page."""
@pytest.mark.testrail(27651)
def test_redirecting_to_home_page_screen_by_clicking_on_storage(page):
    perform_click_on_storage_resource(page, locators['STORAGE_TAB'])
    storage_header_element = page.get_by_test_id(locators['STORAGE_HEADER'])
    storage_header_value = storage_header_element.inner_text()
    assert storage_header_value == StorageTextData.storage_header, "User could not be navigated to storage page!!"
    logging.info("User has successfully navigated to Storage page!")

"""Verify the header on the Storage page."""
@pytest.mark.testrail(27653)
def test_verify_header_of_storage_home_screen(page, storage_setup):
    expect(page.get_by_test_id(locators['STORAGE_HEADER'])).to_be_visible()
    storage_header = page.get_by_test_id(locators['STORAGE_HEADER']).inner_text()
    assert storage_header == StorageTextData.storage_header, "User could not found the Storage Header"
    logging.info("Header on Storage home screen is correct!")

"""Verify the description under the Storage header."""
@pytest.mark.testrail(27654)
def test_verify_description_under_storage_header(page, storage_setup):
    expect(page.get_by_test_id(locators['STORAGE_DESCRP'])).to_be_visible()
    storage_descp = page.get_by_test_id(locators['STORAGE_DESCRP']).inner_text()
    assert storage_descp == StorageTextData.storage_description, "User could not found the Description under Storage Header"
    logging.info("Description under Storage header is correct!")

"""Verify user is redirected to ananta store screen."""
@pytest.mark.testrail(27655)
def test_redirecting_to_ananta_store_screen_by_clicking_on_ananta_store(page, storage_setup):
    tab = page.query_selector_all(f'[data-testid="{locators["STORAGE_FEATURES"]}"]')
    for feature in tab:
        text = feature.inner_text()
        if text == StorageTextData.storage_all_tabs[1]:
            feature.click()
            header = page.get_by_test_id(locators['ANANTA_HEADER']).inner_text()
            assert header == StorageTextData.ananta_header, "User could not redirected to Ananta Store Screen!!"
    logging.info("User is successfully redirected to ananta store screen!")

"""Verify the Header of ananta store screen."""
@pytest.mark.testrail(65130)
def test_verify_header_of_ananta_store_page(page,ananta_setup):
    expect(page.get_by_test_id(locators['ANANTA_HEADER'])).to_be_visible()
    header = page.get_by_test_id(locators['ANANTA_HEADER']).inner_text()
    assert header == StorageTextData.ananta_header, "User could not found the Ananta Store page Header!!"
    logging.info("Ananta store screen Header is correct!")

"""Verify the description under ananta store header ."""
@pytest.mark.testrail(65131)
def test_verify_desc_of_ananta_store_page(page,ananta_setup):
    expect(page.get_by_test_id(locators['ANANTA_DESCRP'])).to_be_visible()
    descp = page.get_by_test_id(locators['ANANTA_DESCRP']).inner_text()
    assert descp == StorageTextData.ananta_description, "User could not found the Ananta Store page Description!!"
    logging.info("Description under Ananta store header is correct!")

"""Verify user is redirected to create volume screen."""
@pytest.mark.testrail(27656)
def test_redirecting_to_create_volume_screen_by_clicking_on_create_volume(page,ananta_setup):
     expect(page.get_by_test_id(locators['CREATE_VOL_BUTTON'])).to_be_visible()
     page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
     page.wait_for_timeout(TIMEOUT)
     vol_create_page = page.get_by_test_id(locators['CREATE_VOL_HEADER']).inner_text()
     assert vol_create_page == StorageTextData.create_vol_header, "User could not found the Volume Creation page Header!!"
     logging.info("User is successfully redirected to Create Volume Screen!")

"""Verify UI of create volume screen."""
@pytest.mark.testrail(27657)
def test_verify_create_volume_screen_UI(page, ananta_setup):
    expect(page.get_by_test_id(locators['CREATE_VOL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    vol_create_page = page.get_by_test_id(locators['CREATE_VOL_HEADER']).inner_text()
    assert vol_create_page == StorageTextData.create_vol_header, "User could not  the Volume Creation page Header!!"
    vol_name = page.locator(locators['VOL_NAME_LABEL']).inner_text()
    assert vol_name == StorageTextData.volume_name, "Volume name is not present"
    vol_size = page.locator(locators['GIB_SIZE']).inner_text()
    assert vol_size == StorageTextData.size_in_gib, "Volume size is not present"
    default_size = page.locator(locators['VOL_SIZE']).input_value()
    assert default_size == StorageTextData.vol_default_size, "Default value for size is not present"
    vol_type = page.locator(locators['VOL_TYPE']).inner_text()
    assert vol_type == StorageTextData.volume_type, "Volume Type is not present"
    bill_rate = page.locator(locators['BILL_RATE']).inner_text()
    assert bill_rate == StorageTextData.bill_rate, "Billing Rate is not present"
    attach_vm = page.locator(locators['ATTACH_VM']).inner_text()
    assert attach_vm == StorageTextData.attach_vm_text, "Attach it to VM is is not present"
    rate = page.locator(locators['VOL_RATE']).inner_text()
    assert rate == StorageTextData.vol_price, "Volume price is not present"
    add_label = page.get_by_test_id(locators['ADD_LABEL']).inner_text()
    assert add_label == StorageTextData.label, "Add Label is not present"
    cancel_btn = page.get_by_test_id(locators['VOL_CANCEL_BTN']).inner_text()
    assert cancel_btn == StorageTextData.cancel, "Close button is not present"
    vol_create_btn = page.get_by_test_id(locators['V0L_CONFIRM_BTN']).inner_text()
    assert vol_create_btn == StorageTextData.create, "Create button is not present"
    vol_cross_btn = page.get_by_test_id(locators['VOL_CROSS_BTN'])
    if vol_cross_btn:
     vol_cross_btn.click()
    logging.info("The UI of Create Volume Screen is correct!")

"""Verify the header of create volume screen."""
@pytest.mark.testrail(27658)
def test_verify_header_of_create_volume_screen(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    vol_create_header = page.get_by_test_id(locators['CREATE_VOL_HEADER']).inner_text()
    assert vol_create_header == StorageTextData.create_vol_header, "User could not found the Volume Creation page Header!!"
    logging.info("The header on Create Volume Screen is correct!")

"""Verify the volume name text field functionality."""
@pytest.mark.testrail(27600)
def test_verify_volume_name_text_field_functionality(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    volume_name_field = page.locator(locators['VOL_NAME'])
    volume_name_field.is_visible()
    page.locator(locators['VOL_NAME']).type(VOLUME_NAME)
    page.locator(locators['VOL_NAME']).fill('')
    page.wait_for_timeout(TIMEOUT)
    vol_name_error = page.query_selector(locators['VOL_HELPER_TEXT']).inner_text()
    assert vol_name_error == StorageTextData.name_blank_error, "name field is not mandatory"
    logging.info("Name field is accepting input and is mandatory!")

"""Verify the volume name placeholder."""
@pytest.mark.testrail(27661)
def test_verify_volume_name_textfield_placeholder(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    vol_name_text_placeholder = page.locator(locators['VOL_NAME_PLACEHOLDER']).get_attribute("placeholder")
    assert vol_name_text_placeholder == StorageTextData.vol_placeholder, "name placeholder is not present "
    logging.info("Volume name textfield placeholder is correct!")

"""Verify the regex validation for volume name."""
@pytest.mark.testrail(27662)
def test_verify_regex_for_volume_name_textfield(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    volume_name_field = page.locator(locators['VOL_NAME'])
    volume_name_field.type('ab')
    vol_name_error = page.query_selector(locators['VOL_HELPER_TEXT']).inner_text()
    assert vol_name_error == StorageTextData.name_min_char, "no min char error"
    volume_name_field.type('!ab')
    page.wait_for_timeout(TIMEOUT)
    vol_name_error = page.query_selector(locators['VOL_HELPER_TEXT']).inner_text()
    assert vol_name_error == StorageTextData.name_text_error, "no error for start and end char"
    volume_name_field.type('!')
    page.wait_for_timeout(TIMEOUT)
    vol_name_error = page.query_selector(locators['VOL_HELPER_TEXT']).inner_text()
    assert vol_name_error == StorageTextData.name_start_end, "na text error"
    volume_name_field.fill('')
    page.wait_for_timeout(TIMEOUT)
    vol_name_error = page.query_selector(locators['VOL_HELPER_TEXT']).inner_text()
    assert vol_name_error == StorageTextData.name_blank_error, "no error on leaving field empty"
    logging.info("Volume name is as per regex validation!")

"""Verify the volume size in GiB."""
@pytest.mark.testrail(27663)
def test_verify_volume_size_in_GiB(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    vol_size = page.locator(locators['GIB_SIZE']).inner_text()
    assert vol_size == StorageTextData.size_in_gib, "volume size is not in GiB"
    logging.info("Volume size is in GiB!")

"""Verify the default volume size."""
@pytest.mark.testrail(27664)
def test_verify_default_volume_size_is_50(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    default_size = page.locator(locators['VOL_SIZE']).input_value()
    assert default_size == StorageTextData.vol_default_size, "default volume is not 50"
    logging.info("The default Volume size is correct!")

"""Verify the volume size is a multiple of 50."""
@pytest.mark.testrail(28023)
def test_verify_volume_size_is_a_multiple_of_50(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    if page.locator(locators['VOL_SIZE']).clear():
       vol_50 = page.locator(locators['VOL_50']).inner_text()
       assert vol_50 == StorageTextData.vol_size_50, "colume size is not multiple of 50"
       page.wait_for_timeout(TIMEOUT)
    logging.info("The Volume size is a multiple of 50!")

"""Verify the volume rate is displayed."""
@pytest.mark.testrail(27669)
def test_verify_volume_rate_is_displayed(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    val = page.locator(locators['VOL_RATE']).inner_text()
    assert val == StorageTextData.vol_price, "could not locate volume size"
    logging.info("The Volume rate is correct!")

#"""Verify the volume rate on selecting monthly and hourly."""
# @pytest.mark.testrail(27670)
# def test_Verify_volume_rate_upon_selecting_monthly_and_hourly(page, ananta_setup):
#     This functionality is yet to be implemented

"""Verify swipe button for attach it to a virtual machine."""
@pytest.mark.testrail(65132)
def test_Attach_it_to_a_Virtual_machine_swipe_button_functionality(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    swipe_btn = page.get_by_test_id(locators['VOL_SWIPE_BUTTON'])
    if swipe_btn.click():
        select_a_vm = page.locator(locators['SELECT_VM_TEXT']).inner_text()
        assert select_a_vm == StorageTextData.select_vm, "please select a VM"
    logging.info("The swipe button is working properly!")

"""Verify dropdown for virtual machine."""
@pytest.mark.testrail(27671)
def test_dropdown_is_displayed_and_user_can_select_virtual_machine(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['VOL_SWIPE_BUTTON']).click()
    page.get_by_test_id(locators['ARROW_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    Dropdown_elements = page.query_selector_all(f'[data-testid="compute-id-option"]')
    count = len(Dropdown_elements)
    if count > 0:
        Dropdown_elements[0].click()
        page.wait_for_timeout(TIMEOUT)
    logging.info("The dropdown is displayed and user is successfully able to select the virtual machine!")

"""Verify create button is displayed as disabled until all required fields have values."""
@pytest.mark.testrail(27674)
def test_Create_button_is_disbaled_till_all_required_field_have_values(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    volume_name_field = page.locator(locators['VOL_NAME'])
    volume_name_field.fill('')
    page.wait_for_timeout(TIMEOUT)
    create_button = page.get_by_test_id(locators['V0L_CONFIRM_BTN'])
    assert not create_button.is_enabled(), "Create button is enabled and is not working properly"
    logging.info("The create button is disabled until all required fields have values!")

"""Verify create button is displayed as disabled until all required fields have values."""
@pytest.mark.testrail(27675)
def test_create_button_becomes_enable_once_required_fields_have_values(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    volume_name_field = page.locator(locators['VOL_NAME'])
    vol_name_text_placeholder = page.locator(locators['VOL_NAME_PLACEHOLDER'])
    if volume_name_field == vol_name_text_placeholder:
        assert not page.get_by_test_id(locators['V0L_CONFIRM_BTN']).is_enabled()
    else:
        volume_name_field.type(VOLUME_NAME)
    expect(page.get_by_test_id(locators['V0L_CONFIRM_BTN'])).to_be_enabled()
logging.info("The create button becomes enabled once required fields have values!")


"""Verify Create button functionality for creating volume."""
@pytest.mark.testrail(27676)
def test_Create_button_functionality_for_creating_volume(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    page.locator(locators['VOL_NAME']).type(VOLUME_NAME)
    create_button = page.get_by_test_id(locators['V0L_CONFIRM_BTN'])
    expect(create_button).to_be_enabled(), "Create button is disabled"
    create_button.click()
    page.wait_for_timeout(TIMEOUT)
    toaster_msg = page.locator(locators['VOL_TOASTER_MSG']).inner_text()
    assert toaster_msg == StorageTextData.creating_msg, "Toaster msg is not appeared"
    logging.info("User should be able to click on Create button and volume should get created.")

"""Verify that volume name should not be same as existing ones."""
@pytest.mark.testrail(27676)
def test_volume_name_should_not_be_same_as_existing_ones(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    page.locator(locators['VOL_NAME']).type('volume')
    page.get_by_test_id(locators['V0L_CONFIRM_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(3000)
    page.locator(locators['VOL_NAME']).type('volume')
    page.get_by_test_id(locators['V0L_CONFIRM_BTN']).click()
    duplicate_msg = page.locator(locators['VOL_TOASTER_MSG']).inner_text()
    page.wait_for_timeout(TIMEOUT)
    assert duplicate_msg == StorageTextData.duplicate_name, "There is no volume with the same name"
    logging.info("Volume name is must be different from the existing ones")



"""Verify created status against volume"""
@pytest.mark.testrail(65133)
def test_created_status_against_volume(page, ananta_setup):
    page.get_by_test_id(locators['CREATE_VOL_BUTTON']).click()
    page.wait_for_timeout(TIMEOUT)
    page.locator(locators['VOL_NAME']).type(VOLUME_NAME)
    page.get_by_test_id(locators['V0L_CONFIRM_BTN']).click()
    page.wait_for_timeout(TIMEOUT)
    page.locator(locators['VOL_TOASTER_MSG']).inner_text()
    creating_status = page.locator(locators['VOl_STATUS']).inner_text()
    assert creating_status == StorageTextData.vol_status, "volume is not in creating state"
    page.locator(locators['VOl_STATUS']).click()
    page.wait_for_timeout(6000)
    page.get_by_test_id(locators['BACK_BTN']).click()
    created_status = page.locator(locators['CREATED_STATUS']).inner_text()
    page.wait_for_timeout(TIMEOUT)
    assert created_status == StorageTextData.created_status, "volume is not in created"
    logging.info("Volume is created")

