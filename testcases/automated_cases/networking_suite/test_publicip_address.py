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
        "username": "atul_srsdet@yopmail.com",
        "password": "India@143"
    }


"""Verify user is able to redirect to Networking screen by clicking on Networking  """
@pytest.mark.testrail(27267)
def test_verify_user_is_able_to_redirect_to_networking_screen_by_clicking_on_networking(page, network_setup):
    # change_project_details(page)
    # perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    # compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    # for index, element in enumerate(compute_header_elements, start=1):
    #     element_text = element.inner_text()
    #     if ComputeTextData.ip_address_section in element_text:
    #         element.click()
    # perform_click_on_create_vm_button(page, locators['IP_CREATE_BTN'])
    #

    page.wait_for_timeout(TIMEOUT)
    to_create_virtual_Compute_machine(page)
    page.wait_for_timeout(10000)
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    expect(page.get_by_test_id(locators['NETWORK_HEADER'])).to_be_visible()
    network_page_heading = page.get_by_test_id(locators['NETWORK_HEADER'])
    networking_header = network_page_heading.inner_text()
    assert networking_header == "Networking", "User could not be navigated to networking section!!"
    logging.info("User successfully navigated to networking  screen!")


@pytest.mark.testrail(27268)
def test_verify_UI_networking_screen(page, network_setup):
    expect(page.get_by_test_id(locators['NETWORK_HEADER'])).to_be_visible()
    expected_texts= ComputeTextData.network_header_section
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
    expect(page.get_by_test_id(locators['NETWORK_DISCRIPTION'])).to_be_visible()
    network_discription_element = page.get_by_test_id(locators['NETWORK_DISCRIPTION'])
    network_description_value = network_discription_element.inner_text()
    assert network_description_value == ComputeTextData.network_discription, f"The network description value - {network_description_value}, is different than expected!"

    expect(page.get_by_test_id(locators['COMPUTE_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['DEPLOY_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['DATABASE_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['PLATFORM_OPERATION'])).to_be_visible()
    expect(page.get_by_test_id(locators['QUICK_LINK'])).to_be_visible()
    expect(page.get_by_test_id(locators['LEARN_MORE_TAB'])).to_be_visible()

@pytest.mark.testrail(27269)
def test_verify_header_on_networking_screen(page, network_setup):
    expect(page.get_by_test_id(locators['NETWORK_HEADER'])).to_be_visible()
    network_page_heading = page.get_by_test_id(locators['NETWORK_HEADER'])
    networking_header = network_page_heading.inner_text()
    assert networking_header == "Networking", "User could not be navigated to networking section!!"
    logging.info("User successfully navigated to networking  screen!")

"""Verify description under Header part """
@pytest.mark.testrail(27270)
def test_to_verify_network_discription_under_header_part(page, network_setup):
    expect(page.get_by_test_id(locators['NETWORK_DISCRIPTION'])).to_be_visible()
    network_discription_element = page.get_by_test_id(locators['NETWORK_DISCRIPTION'])
    network_description_value = network_discription_element.inner_text()
    assert network_description_value == ComputeTextData.network_discription, f"The network description value - {network_description_value}, is different than expected!"
    logging.info("Description on network header screen is correct!")

@pytest.mark.testrail(27272)
def test_to_verify_header_on_IP_address_screen(page, ip_address_setup):
    expect(page.get_by_test_id(locators['IP_ADDRESS_HEADER'])).to_be_visible()
    ip_address_element = page.get_by_test_id(locators['IP_ADDRESS_HEADER'])
    ip_address_value = ip_address_element.inner_text()
    assert ip_address_value == "IP Address", f"The IP address header value - {ip_address_value}, is different than expected!"
    logging.info("ip address header screen is correct!")

@pytest.mark.testrail(27273)
def test_description_under_header_part_on_IP_Address_screen(page, ip_address_setup):
    expect(page.get_by_test_id(locators['IP_ADDRESS_HEADER_DISCRIPTION'])).to_be_visible()
    ip_address_discription = page.get_by_test_id(locators['IP_ADDRESS_HEADER_DISCRIPTION'])
    IP_discription_value = ip_address_discription.inner_text()
    assert IP_discription_value == ComputeTextData.ip_address_discription, f"The Ip address description value - {IP_discription_value}, is different than expected!"
    logging.info("Description on Ip address header screen is correct!")


"""Learn More section on IP Address screen"""
@pytest.mark.testrail(27274)
def test_Learn_More_section_on_IP_Address_screen(page, ip_address_setup):
    page.wait_for_timeout(TIMEOUT)
    ip_address_field_visibility = page.locator(locators['IP_ADDRESS_NOT']).is_visible()
    if ip_address_field_visibility == True:
        expect(page.get_by_test_id(locators['LEARN_MORE_VM'])).to_be_visible()
        learn_more_value = page.get_by_test_id(locators['LEARN_MORE_VM'])
        text = learn_more_value.inner_text()
        assert text == "Learn more", "Learn More button is not present when no public ip found"
        page.click("btn-learn-more")
        expected_url = "https://docs-revamp-sbx.yntraa.com//docs/Computes/Compute"
        page.wait_for_timeout(TIMEOUT)
        assert page.url == expected_url, f"Expected URL: {expected_url}, Actual URL: {page.url}"
        logging.info("Learn More section on IP Address screen verified successfully!")

    else:
        logging.info("Test case failed as ip_address found in the list.")
        ipaddress_list_elements = page.query_selector_all(f'[data-testid="list-card"]')
        count = len(ipaddress_list_elements)

@pytest.mark.testrail(27275)
def test_redirect_to_reserve_public_ip_screen_by_clicking_on_button(page, create_reservePublicIP):
    section_header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert section_header_element.is_visible(), "Section header is not visible."
    Reserve_Public_IP_screen = section_header_element.inner_text()
    assert Reserve_Public_IP_screen == ComputeTextData.reserve_screen, f"The header screen value - {Reserve_Public_IP_screen}, is different than expected!"
    logging.info("User successfully redirected to Reserve Public IP screen by clicking on the button.")

@pytest.mark.testrail(27276)
def test_Verify_Reserve_Public_IP_screen_UI(page, create_reservePublicIP):
    page.wait_for_timeout(TIMEOUT)
    section_header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert section_header_element.is_visible(), "Section header is not visible."
    rate_text_element = page.get_by_text("Rate:")
    assert rate_text_element.is_visible(), "Rate text is not visible."
    yes_button_element = page.get_by_test_id(locators['CONFIRM_BUTTON'])
    assert yes_button_element.is_visible(), "Yes button is not visible."
    no_button_element = page.get_by_test_id(locators['CANCEL_BUTTON'])
    assert no_button_element.is_visible(), "No button is not visible."

@pytest.mark.testrail(27277)
def test_Verify_that_Reserve_Public_IP_header_is_displayed_ontop_of_page(page, create_reservePublicIP):
    section_header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert section_header_element.is_visible(), "Section header is not visible."
    Reserve_Public_IP_screen = section_header_element.inner_text()
    assert Reserve_Public_IP_screen == ComputeTextData.reserve_screen, f"The header screen value - {Reserve_Public_IP_screen}, is different than expected!"
    logging.info("User successfully redirected to Reserve Public IP screen by clicking on the button.")

@pytest.mark.testrail(27278)
def test_Verify_Rate_funtionality(page, create_reservePublicIP):
    page.wait_for_timeout(TIMEOUT)
    rate_text_element = page.get_by_text("Rate:")
    assert rate_text_element.is_visible(), "Rate text is not visible."
    estimate_cost_withlabel = page.get_by_test_id(locators['ESTIMATE_COST'])
    assert estimate_cost_withlabel.is_visible(), "ip amount os not visble"
    ip_amount = estimate_cost_withlabel.inner_text()
    rate_label = ip_amount.split(':')[0].strip()
    print("IP Amount:", rate_label)
    # monthly_label = page.get_by_text(locators['MONTHLY_TAB'])
    # assert monthly_label.is_visible(), "monthly label is not displayed"
    # hour_label = page.get_by_text(locators['HOURLY_TAB'])
    # assert hour_label.is_visible(), "Hourly label is not displayed"

@pytest.mark.testrail(27279)
def test_verify_statement_mentioned_under_Rate(page, create_reservePublicIP):
    page.locator(locators['STATEMENT_PUBLIC_IP']).is_visible()
    rate_stetement = page.locator(locators['STATEMENT_PUBLIC_IP']).inner_text()
    assert rate_stetement == ComputeTextData.ip_address_statement, f"ip address statement is not visble"

@pytest.mark.testrail(27281)
def test_verify_Yes_button_functionality_for_reserving_Public_IP(page, create_reservePublicIP):
    page.wait_for_timeout(10000)
    yes_button_element = page.get_by_test_id(locators['CONFIRM_BUTTON'])
    assert yes_button_element.is_visible(), "Yes button is not visible."
    yes_button_element.click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == ComputeTextData.ip_address_toast_msg, f"The toast message '{toast_text}' is different than expected: '{expected_toast_msg}'"
    expect(page.get_by_test_id(locators['IP_ADDRESS_HEADER'])).to_be_visible()

    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(10000)
    verify_to_click_tejas_compute_tab(page)
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Attach Public IP":
                item.click()
                print("Clicked on Attach Public IP")
                publicIp_dropdown_element = page.locator(locators['FLOATING_IP_DROPDOWN'])
                publicIp_dropdown_element.click()
                ZoneDropdown_elements = page.query_selector_all(f'[data-testid="floating_ip_address-option"]')
                count = len(ZoneDropdown_elements)
                if count > 0:
                    ZoneDropdown_elements[0].click()
                page.wait_for_timeout(TIMEOUT)
                page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
                page.wait_for_timeout(10000)
                perform_the_network_homeTab(page)
                break

def perform_the_network_homeTab(page):
    perform_click_on_compute_resource(page, locators['NETWORKING_TAB'])
    ip_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(ip_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.ip_address_section in element_text:
            element.click()

@pytest.mark.testrail(27282)
def test_Verify_user_is_able_to_view_the_listings_of_Public_IP(page, ip_address_setup):
    page.wait_for_timeout(10000)
    ipaddress_list_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(ipaddress_list_elements)
    assert count > 0, "No IP address listings found."
    first_ip_value = ipaddress_list_elements[0].inner_text()
    ip_addressvalue = page.query_selector_all(f'[data-testid="resource-name-link"]')
    ip_count = len(ip_addressvalue)
    if ip_count > 0:
        ip_address = ip_addressvalue[0].inner_text()
        print(ip_address)
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    assert status_text in ["available", "in-use"], f"Unexpected VM status: {status_text}"
    print("Status:", status_text)
    attached_text = page.query_selector_all(locators["ATTACHED_WITH"])
    attached_count = len(attached_text)
    if attached_count > 0:
        text = attached_text[0].inner_text()


@pytest.mark.testrail(27284)
def test_Verify_Reserved_Public_IP_configuration_info_for_IP(page, ip_address_setup):
    page.wait_for_timeout(10000)
    ipaddress_list_elements = page.query_selector_all(f'[data-testid="list-card"]')
    count = len(ipaddress_list_elements)
    assert count > 0, "No IP address listings found."
    first_ip_value = ipaddress_list_elements[0].inner_text()
    ip_addressvalue = page.query_selector_all(f'[data-testid="resource-name-link"]')
    ip_address_element = ip_addressvalue[0].inner_text()
    assert ip_address_element, "IP address element not found."
    logging.info("IP Address:",  ip_address_element)

@pytest.mark.testrail(27285)
def test_verify_reserved_ip_configuration_info_for_available_option(page, ip_address_setup):
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    if status_text == "available":
        logging.info("Reserved IP status: Available")
    elif status_text == "in-use":
        logging.info("Reserved IP status: In-use")
    else:
        assert False, f"Unexpected Reserved IP status: {status_text}"
    logging.info("Status:", status_text)

@pytest.mark.testrail(27286)
def test_verify_reserved_public_ip_configuration_info_for_attached_with_option(page, ip_address_setup):
    attached_with_element = page.query_selector(locators["ATTACHED_WITH_VALUE"])
    assert attached_with_element, "Attached with element not found."
    attached_with_text = attached_with_element.inner_text()
    if not attached_with_text:
        logging.info("Reserved public IP is not attached to any VM")
    else:
        logging.info("Reserved public IP is attached to a VM:", attached_with_text)
        assert attached_with_text.strip(), "Attached with text is empty or contains only whitespace"

@pytest.mark.testrail(27287)
def test_Verify_Reserved_Public_IP_configuration_info_for_Created(page, ip_address_setup):
    expect(page.get_by_test_id(locators['IP_ADDRESS_HEADER'])).to_be_visible()
    creation_info_element = page.query_selector(locators['VM_CREATION_INFO'])
    page.wait_for_timeout(1000)
    created_info = page.query_selector_all(f'[data-testid="created"]')
    info_count = len(created_info)
    if info_count > 0:
        vm_created_info = created_info[0].inner_text()
    assert vm_created_info, "Creation info element not found."

@pytest.mark.testrail(27288)
def test_Reserved_Public_IP_configuration_info_for_Last_update(page, ip_address_setup):
    expect(page.get_by_test_id(locators['IP_ADDRESS_HEADER'])).to_be_visible()
    creation_info_element = page.query_selector(locators['VM_UPDATION_INFO'])
    page.wait_for_timeout(1000)
    updated_info = page.query_selector_all(f'[data-testid="updated"]')
    update_count = len(updated_info)
    if update_count > 0:
        vm_updated_info = updated_info[0].inner_text()
    assert vm_updated_info, "updated info element not found."

@pytest.mark.testrail(27289)
def test_verify_attach_reserved_public_ip_to_vm(page, ip_address_setup):
    status_elements = page.query_selector_all(f'[data-testid="{locators["VM_STATUS"]}"]')
    status_count = len(status_elements)
    print("Number of status elements found:", status_count)

    for status_element in status_elements:
        status_text = status_element.inner_text().lower()
        if status_text == "available":
            logging.info("Reserved IP status: Available")
        elif status_text == "in-use":
            logging.info("Reserved IP status: In-use")
            # ip_addressvalue = page.query_selector_all(locators['ATTACHED_RESERVE_IP'])
            # assert ip_addressvalue, "IP address element not found."
            # ip_address_element = ip_addressvalue[0].inner_text()
            ip_address_elements = page.query_selector_all(locators['ATTACHED_RESERVE_IP'])
            if not ip_address_elements:
                logging.error("IP address element not found.")
                continue
            ip_address_element = ip_address_elements[0].inner_text()
            attached_with_elements = page.query_selector_all(locators['ATTACHED_WITH_VALUE'])
            update_count = len(attached_with_elements)
            logging.info("Number of attached with elements found:", update_count)
            page.wait_for_timeout(10000)
            if update_count > 0:
                for index, element in enumerate(attached_with_elements):
                    vm_updated_info = element.inner_text()
                    logging.info("VM Updated Info:", vm_updated_info)
                    if vm_updated_info.strip():
                        attached_with_elements[index].click()
                        logging.info("Clicked on attached_with_element:", vm_updated_info)
                        page.wait_for_timeout(10000)
                        vm_public_ip = page.get_by_test_id(locators['PUBLIC_IP_SECTION'])
                        assert vm_public_ip.is_visible(), "public is not visible"
                        public_ip = vm_public_ip.inner_text()
                        assert ip_address_element == public_ip
        else:
            assert False, f"Unexpected Reserved IP status: {status_text}"
    logging.info("Status verification completed")

@pytest.mark.testrail(27290)
def test_Verify_user_is_able_to_detach_public_IP_from_a_VM(page, ip_address_setup):
    perform_the_network_homeTab(page)
    test_verify_attach_reserved_public_ip_to_vm(page, ip_address_setup)
    #perform_the_network_homeTab(page)
    logging.info("Status verification completed")
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Detach Public IP":
                item.click()
                print("Clicked on Detach Public IP")
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()

    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    assert toast_text == "Public IP detached successfully"
    perform_the_network_homeTab(page)
    page.wait_for_timeout(TIMEOUT)
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    print("Status:", status_text)
    valid_statuses = ["available", "in-use"]
    assert status_text in valid_statuses, f"Unexpected status: {status_text}"
    assert status_text == "available", "The public ip is in still in-use status"
