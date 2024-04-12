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
        #"username": "vini-sdet@yopmail.com",
        "password": "India@143"
    }

"""Verify header on Networking screen """
@pytest.mark.testrail(29500)
def test_verify_header_on_Networking_screen(page, network_setup):
    expect(page.get_by_test_id(locators['NETWORK_HEADER'])).to_be_visible()
    snapshot_compute_page_heading = page.get_by_test_id(locators['NETWORK_HEADER'])
    snapshot_page_heading = snapshot_compute_page_heading.inner_text()
    assert snapshot_page_heading == "Networking", "User could not be navigated to Compute snapshot section!!"
    logging.info("User successfully navigated to Compute snapshot screen!")
    #page.wait_for_timeout(10000)

"""Verify description under Header part """
@pytest.mark.testrail(29501)
def test_to_verify_network_discription_under_header_part(page, network_setup):
    expect(page.get_by_test_id(locators['NETWORK_DISCRIPTION'])).to_be_visible()
    network_discription_element = page.get_by_test_id(locators['NETWORK_DISCRIPTION'])
    network_description_value = network_discription_element.inner_text()
    assert network_description_value == ComputeTextData.network_discription, f"The network description value - {network_description_value}, is different than expected!"
    logging.info("Description on network header screen is correct!")

"""Verify user is able to redirect to Kshetra Network screen by clicking on Networking """

@pytest.mark.testrail(29498)
def test_Verify_user_is_able_to_redirect_to_Kshetra_Network_screenby_clicking_on_Networking(page, kshetra_setup):
    expect(page.get_by_test_id(locators['KSHETRA_HEADER'])).to_be_visible()
    snapshot_compute_page_heading = page.get_by_test_id(locators['KSHETRA_HEADER'])
    snapshot_page_heading = snapshot_compute_page_heading.inner_text()
    assert snapshot_page_heading == ComputeTextData.kshetra_network, "User could not be navigated to Kshetra network screen!!"
    logging.info("User successfully navigated to Kshetra network screen!")
    #page.wait_for_timeout(10000)

@pytest.mark.testrail(29502) #503 same
def test_Verify_user_is_redirect_to_Keshtra_Network_screen(page, kshetra_setup):
    expect(page.get_by_test_id(locators['KSHETRA_HEADER'])).to_be_visible()
    snapshot_compute_page_heading = page.get_by_test_id(locators['KSHETRA_HEADER'])
    snapshot_page_heading = snapshot_compute_page_heading.inner_text()
    assert snapshot_page_heading == ComputeTextData.kshetra_network, "User could not be navigated to Kshetra network screen!!"
    logging.info("User successfully navigated to Kshetra network screen!")
    #page.wait_for_timeout(10000)


"""Verify description under header part on Kshetra Network screen """
@pytest.mark.testrail(29504)
def test_to_verify_discription_under_header_part_on_kshetra_network(page, kshetra_setup):
    kshetra_description_element = page.get_by_test_id(locators['KSHETRA_DISCRIPTION'])
    assert kshetra_description_element.is_visible(), "kshetra description element is not visible"
    kshetra_description_value = kshetra_description_element.inner_text()
    expected_description = ComputeTextData.kshetra_discription
    assert kshetra_description_value == expected_description, f"The kshetra description value '{kshetra_description_value}' is different than expected '{expected_description}'"
    logging.info("Description on the kshtetra header screen is correct!")

"""Verify user is able to redirect to Create Network screen by clicking on Create Network button"""
@pytest.mark.testrail(29506)
def test_Verify_user_is_able_to_redirect_to_Create_Network_screen_by_clicking_on_Create_Network_button(page, create_kshetra_network):
    section_header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert section_header_element.is_visible(), "Section header is not visible."
    create_network_section = section_header_element.inner_text()
    logging.info(f"User redirected to the Create Network screen after clicking on the Create Network button {create_network_section} !")

"""Verify Create Network screen UI"""
@pytest.mark.testrail(29507)
def test_verify_UI_networking_screen(page, create_kshetra_network):
    section_header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert section_header_element.is_visible(), "Section header is not visible."
    page.locator(locators['CREATE_NETWORK_DISCRIPTION']).is_visible()
    discription = page.locator(locators['CREATE_NETWORK_DISCRIPTION']).inner_text()
    assert discription == ComputeTextData.create_network_discription, f"create network discription is not visble"
    expect(page.get_by_test_id(locators['CLOSE_BTN'])).to_be_visible()
    page.get_by_text(locators['CREATE_NAME']).is_visible()
    Name_element = page.locator(locators['CREATE_NAME'])
    assert  Name_element.is_visible(), "Name input field is not visible."
    IP_dropdown_element = page.locator(locators['IP_VERSION_DROPDOWN'])
    assert  IP_dropdown_element.is_visible(), "IP version dropdown is not visible."
    CIDR_element = page.locator(locators['NETWORK_CIDR'])
    assert  CIDR_element.is_visible(), "Network CIDR field is not visible."
    assert page.get_by_text("(Max. 5)").is_visible(), "Max label is not visible."
    expect(page.get_by_test_id("label-input")).to_be_visible()
    page.get_by_text(locators['ADD_LABEL_BTN']).is_visible()
    assert page.get_by_test_id(locators['CANCEL_BUTTON']).is_visible(), "Cancel button is not visible."
    assert page.get_by_test_id(locators['CONFIRM_BUTTON']).is_visible(), "Confirm button is not visible."
    #page.get_by_test_id(locators['CLOSE_BTN']).click()
#
@pytest.mark.testrail(29508)
def test_Verify_that_Create_Network_header_is_displayed_on_top_of_page(page, create_kshetra_network):
    section_header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert section_header_element.is_visible(), "Section header is not visible."
    create_network_section = section_header_element.inner_text()
    assert  create_network_section == "Create Network"
    logging.info(f"User redirected to the Create Network screen after clicking on the Create Network button {create_network_section} !")


@pytest.mark.testrail(29509)
def test_Verify_statement_mentioned_under_header(page, create_kshetra_network):
    section_header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert section_header_element.is_visible(), "Section header is not visible."
    page.locator(locators['CREATE_NETWORK_DISCRIPTION']).is_visible()
    discription = page.locator(locators['CREATE_NETWORK_DISCRIPTION']).inner_text()
    assert discription == ComputeTextData.create_network_discription, f"create kshetra discription is not visble"
    logging.info("Description on kshetra network address header screen is correct!")

@pytest.mark.testrail(29510)
def test_verify_Network_Name_text_field_is_properly_displayed_and_accept_input_from_user(page, create_kshetra_network):
    page.get_by_text(locators['CREATE_NAME']).is_visible()
    clear_and_fill_field(page, locators['CREATE_NAME'], "")
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['NETWORK_CIDR'], "")
    required_field_text = page.locator(locators['NETWORK_NAME_HELPER_TEXT']).inner_text()
    assert required_field_text == "Name is required.", "Expected helper text not found for the empty Network Name field."
    input_box_locator = page.locator(locators['KSHETRANAME_FIELD'])
    expect(input_box_locator).to_be_visible()
    input_box_text = input_box_locator.inner_text()
    assert input_box_text == "", "Input box text is not empty"
    page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(29511)
def test_verfy_label_inside_network_name_text_field_displays_label_inside_the_text_area(page, create_kshetra_network):
    page.locator(locators['CREATE_NAME']).is_visible()
    input_box_locator = page.locator('input#network_name')
    placeholder_text = input_box_locator.get_attribute('placeholder')
    expected_label = "Please enter name"
    assert placeholder_text == expected_label, f"The label inside the Network Name text field is '{placeholder_text}', but it should display '{expected_label}'"

@pytest.mark.testrail(29512)
def test_Verify_Network_Name_text_field_for_regex_validation(page, create_kshetra_network):
    invalid_characters_name = "Test$%123"
    non_alphanumeric_name = "-Test1234-"
    long_name = "Test1234567890123456789012345678901"
    clear_and_fill_field(page, locators['CREATE_NAME'], "ab")
    helper_text_element = page.locator(locators['NETWORK_NAME_HELPER_TEXT'])
    helper_text = helper_text_element.inner_text()
    assert "Name must be at least 3 characters long." in helper_text, "Minimum character requirement not met"

    clear_and_fill_field(page, locators['CREATE_NAME'], invalid_characters_name)
    helper_text_element = page.locator(locators['NETWORK_NAME_HELPER_TEXT'])
    helper_text = helper_text_element.inner_text()
    assert "Name can have alphanumeric characters, hyphens, underscores and spaces only." in helper_text, "Invalid characters present"

    clear_and_fill_field(page, locators['CREATE_NAME'], non_alphanumeric_name)
    helper_text_element = page.locator(locators['NETWORK_NAME_HELPER_TEXT'])
    helper_text = helper_text_element.inner_text()
    assert "Name must start and end with an alphanumeric character." in helper_text, "Does not start or end with alphanumeric character"
    
    clear_and_fill_field(page, locators['CREATE_NAME'], long_name)
    helper_text_element = page.locator(locators['NETWORK_NAME_HELPER_TEXT'])
    helper_text = helper_text_element.inner_text()
    assert "Name cannot exceed 30 characters." in helper_text, "Exceeds maximum character limit"

    # clear_and_fill_field(page, locators['CREATE_NAME'], MACHINE_NAME)
    # helper_text_element = page.locator(locators['NETWORK_NAME_HELPER_TEXT'])
    # helper_text = helper_text_element.inner_text()
    # assert not helper_text, "Unexpected error message for valid name"


@pytest.mark.testrail(29513)
def test_verify_IP_Version_dropdown_is_displayed_and_user_can_select_option_from(page, create_kshetra_network):
    ip_version_dropdown_element = page.locator(locators['IP_VERSION_DROPDOWN'])
    ip_version_dropdown_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="ip_version-option"]')
    count = len(Dropdown_elements)
    for index, element in enumerate(Dropdown_elements, start=1):
        element_text = element.inner_text()
        print("Selected ip version:", element_text)
        if "IPv4" in element_text.lower():
            element.click()
            print("Clicked on IPv4 version")
            break

"""Network Address field should be present and user should be able to enter input value in same. This field should be a mandatory field"""
@pytest.mark.testrail(29514)
def test_Verify_Network_Address_text_field_is_properly_displayed_and_accept_input_from_user(page, create_kshetra_network):
    CIDR_element = page.locator(locators['NETWORK_CIDR'])
    assert  CIDR_element.is_visible(), "Network CIDR field is not visible."
    NETWORK_ADDRESS = "192.168.1.0/24"
    #page.wait_for_timeout(10000)
    ip_version_dropdown_element = page.locator(locators['NETWORK_CIDR'])
    ip_version_dropdown_element.click()
    clear_and_fill_field(page, locators['NETWORK_CIDR'], "")
    clear_and_fill_field(page, locators['NETWORK_CIDR'], NETWORK_ADDRESS)
    input_box_locator = page.locator(locators['NETWORK_CIDR'])
    expect(input_box_locator).to_be_visible()
    input_box_text = input_box_locator.inner_text()
    print(input_box_text)
    assert input_box_text == "", "Input box text is not empty"
    page.wait_for_timeout(10000)

    # if count > 0:
    #     ip_address = Dropdown_elements[0].click()
    #     print(ip_address)
    #     Dropdown_elements[0].click()
    # page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(29515)
def test_verfy_label_inside_network_address_text_field_displays_label_inside_the_text_area(page, create_kshetra_network):
    page.locator(locators['CREATE_NAME']).is_visible()
    clear_and_fill_field(page, locators['NETWORK_CIDR'], "")
    input_box_locator = page.locator(locators['CIDR_PLACEHOLEDR'])
    placeholder_text = input_box_locator.get_attribute('placeholder')
    logging.info(placeholder_text)
    expected_label = "Please enter network address in CIDR format (192.168.1.0/24)"
    assert placeholder_text == expected_label, f"The label inside the Network CIDR text field is '{placeholder_text}', but it should display '{expected_label}'"

@pytest.mark.testrail(29516)
def test_Verify_error_message_for_invalid_or_incorrect_ipv_input(page, create_kshetra_network):
    NETWORK_ADDRESS = "192.168.1.0/24"
    page.locator(locators['CREATE_NAME']).is_visible()
    clear_and_fill_field(page, locators['NETWORK_CIDR'], "")
    clear_and_fill_field(page, locators['NETWORK_CIDR'], "qwerty")
    helper_text_element = page.locator(locators['CIDR_HELPERTEXT'])
    helper_text = helper_text_element.inner_text()
    assert "Network address should be in CIDR format (192.168.1.0/24)" in helper_text, "Minimum character requirement not met"
    clear_and_fill_field(page, locators['NETWORK_CIDR'], NETWORK_ADDRESS)


@pytest.mark.testrail(29517)
def test_Verify_Add_Labels_functionality(page, create_kshetra_network):
    page.get_by_test_id('label-input').click()
    page.get_by_text("Add Labels").is_visible()
    page.get_by_text("(Max. 5)").is_visible()
    expect(page.get_by_test_id("label-input")).to_be_visible()
    for i in range(5):
        valid_label = f"atul-sdet{i + 1}"
        if i >= 5:
            break
        page.fill(locators['INPUT_LABEL'], valid_label)
        page.locator(locators['ADD_LABEL_BTN']).click()

    all_labels = page.query_selector_all("[data-testid='label-helper-text']")
    for label_element in all_labels:
        label_text = label_element.inner_text()
        assert 3 <= len(label_text) <= 15, f"Invalid tag length: {label_text}"
        assert re.match(r'^[a-zA-Z0-9_-]+$', label_text), f"Invalid character set: {label_text}"
    page.wait_for_timeout(10000)


@pytest.mark.testrail(29518)
def test_Verify_Close_button_functionality(page, create_kshetra_network):

    expect(page.get_by_test_id(locators['SECTION_HEADER_NAME'])).to_be_visible()
    no_button_element = page.get_by_test_id(locators['CANCEL_BUTTON'])
    assert no_button_element.is_visible(), "Cancel button is not visible."
    page.get_by_test_id(locators['CANCEL_BUTTON']).click()
    expect(page.get_by_test_id(locators['KSHETRA_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
    perform_click_on_compute_resource(page, locators['CREATE_NETWORK_BTN'])

@pytest.mark.testrail(29519)
def test_verify_Create_button_is_present_and_displayed_disabled_till_all_required_field_have_values(page, create_kshetra_network):
    clear_and_fill_field(page, locators['CREATE_NAME'], MACHINE_NAME)
    ip_version_dropdown_element = page.locator(locators['IP_VERSION_DROPDOWN'])
    ip_version_dropdown_element.click()
    Dropdown_elements = page.query_selector_all(f'[data-testid="ip_version-option"]')
    count = len(Dropdown_elements)
    for index, element in enumerate(Dropdown_elements, start=1):
        element_text = element.inner_text()
        print("Selected ip version:", element_text)
        if "IPv4" in element_text.lower():
            element.click()
            print("Clicked on IPv4 version")
            break
    NETWORK_ADDRESS = "192.168.1.0/24"
    ip_version_dropdown_element = page.locator(locators['NETWORK_CIDR'])
    ip_version_dropdown_element.click()
    clear_and_fill_field(page, locators['NETWORK_CIDR'], "")
    clear_and_fill_field(page, locators['NETWORK_CIDR'], NETWORK_ADDRESS)
    page.get_by_test_id('label-input').click()
    page.get_by_text("Add Labels").is_visible()
    page.get_by_text("(Max. 5)").is_visible()
    expect(page.get_by_test_id("label-input")).to_be_visible()
    for i in range(5):
        valid_label = f"atul-sdet{i + 1}"
        if i >= 5:
            break
        page.fill(locators['INPUT_LABEL'], valid_label)
        page.locator(locators['ADD_LABEL_BTN']).click()

    all_labels = page.query_selector_all("[data-testid='label-helper-text']")
    for label_element in all_labels:
        label_text = label_element.inner_text()
        assert 3 <= len(label_text) <= 15, f"Invalid tag length: {label_text}"
        assert re.match(r'^[a-zA-Z0-9_-]+$', label_text), f"Invalid character set: {label_text}"
    page.wait_for_timeout(10000)
    final_create_networkn_locator = locators['CONFIRM_BUTTON']
    create_button_element = page.get_by_test_id(final_create_networkn_locator)
    assert create_button_element, f"Unable to find Create button using locator: {final_create_networkn_locator}"
    create_button = create_button_element.is_enabled() if create_button_element else False
    assert create_button, "Create button should be enabled after filling all required fields"

@pytest.mark.testrail(29520)
def test_Create_button_becomes_enable_once_input_are_there_in_all_required_fields(page, create_kshetra_network):

    page.wait_for_timeout(10000)
    create_button= page.get_by_test_id(locators['CONFIRM_BUTTON'])
    if create_button:
        assert create_button.is_visible(), "Create button is not visible"
        assert create_button.is_enabled(), "Create button should be enabled once all required fields have values"
    else:
        pytest.fail("Create button not found on the page")

@pytest.mark.testrail(29521)
def test_Verify_Create_button_functionality_for_creating_network(page, create_kshetra_network):
    yes_button_element = page.get_by_test_id(locators['CONFIRM_BUTTON'])
    assert yes_button_element.is_visible(), "confirm button is not visible."
    yes_button_element.click()
    toast_element = page.locator('//div[@role="alert"]')
    toast_text = toast_element.inner_text()
    print(toast_text)
    page.wait_for_timeout(10000)
    assert toast_text == ComputeTextData.kshetra_create_network_toast_msg, f"The toast message '{toast_text}' is different than expected: '{expected_toast_msg}'"
    expect(page.get_by_test_id(locators['KSHETRA_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
