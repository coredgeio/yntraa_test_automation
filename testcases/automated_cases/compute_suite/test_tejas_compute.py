import logging
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from test_helper.testdata.compute_testdata import ComputeTextData
import asyncio

@pytest.fixture(scope="module")
def user_credentials():
    return {
        #"url": "https://console.yntraa.com",
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "vini-sdet@yopmail.com",
        "password": "India@143"
    }

# def pytest_runtest_makereport(item, call):
#     if call.when == "call" and call.excinfo is not None:
#         page = item.funcargs["page"]
#         page.screenshot(path="failure_screenshot.png")

# @pytest.fixture(autouse=True)
# def logout_after_test(request, page):
#     yield
#     verify_to_logout_function(page)

"""Constant and Global Tejas Compute VM Name!"""
MACHINE_NAME = generate_random_machine_name()


"""Perform a click operation on Compute Resource and verify the header on the resulting landing page."""
#@pytest.mark.testrail(27291)
@pytest.mark.testrail(65137)
def test_to_verify_clicking_on_compute_screen(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    compute_header_element = page.get_by_test_id(locators['COMPUTE_HEADER'])
    compute_header_value = compute_header_element.inner_text()
    assert compute_header_value == ComputeTextData.compute_header, "User could not be navigated to Compute module!!"
    logging.info("User has successfully navigated to Compute module!")


"""Verify the Compute page UI."""
#@pytest.mark.testrail(27292)
@pytest.mark.testrail(65138)
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

"""Verify the header on the Compute page."""
#@pytest.mark.testrail(27293)
@pytest.mark.testrail(65139)
def test_to_verify_header_on_compute_home_screen(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_HEADER'])).to_be_visible()
    compute_header_element = page.get_by_test_id(locators['COMPUTE_HEADER'])
    compute_header_value = compute_header_element.inner_text()
    assert compute_header_value == ComputeTextData.compute_header, f"The compute header value - {compute_header_value}, is different than expected!"
    logging.info("Header on Compute home screen is correct!")

"""Verify the description on the Compute page."""
#@pytest.mark.testrail(27294)
@pytest.mark.testrail(65140)
def test_to_verify_compute_home_screen_description(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_DESCRP'])).to_be_visible()
    compute_discription_element = page.get_by_test_id(locators['COMPUTE_DESCRP'])
    compute_description_value = compute_discription_element.inner_text()
    assert compute_description_value == ComputeTextData.compute_description, f"The compute description value - {compute_description_value}, is different than expected!"
    logging.info("Description on Compute home screen is correct!")

"""Perform a click operation on Tejas Compute and validate the header on the resulting landing page."""
#@pytest.mark.testrail(27295)
@pytest.mark.testrail(65141)
def test_to_verify_clicking_on_tejas_compute(page, compute_setup):
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count:", compute_header_count)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    tejas_compute_page_heading = page.get_by_test_id(locators['TEJAS_HEADER'])
    tejas_compute_page_heading = tejas_compute_page_heading.inner_text()
    #assert tejas_compute_page_heading == ComputeTextData.tejas_compute_header, "User could not be navigated to Tejas Compute section!!"
    assert tejas_compute_page_heading == ComputeTextData.tejas_compute_tab, "User could not be navigated to Tejas Compute section!!"
    logging.info("User successfully navigated to Tejas Compute screen!")

"""Verify the header on the Tejas Compute page."""
#@pytest.mark.testrail(27296)
@pytest.mark.testrail(65142)
def test_to_verify_header_on_tejas_compute_screen(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    tejas_compute_header = page.get_by_test_id(locators['TEJAS_HEADER'])
    tejas_compute_header = tejas_compute_header.inner_text()
    assert tejas_compute_header == ComputeTextData.tejas_compute_tab, f"The Tejas Compute header value - {tejas_compute_header}, is different than expected!"
    logging.info("Header on Tejas Compute screen is correct!")


"""Verify the description on the Tejas Compute page."""
#@pytest.mark.testrail(27297)
@pytest.mark.testrail(65143)
def test_to_verify_tejas_compute_screen_description(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_DESCRP'])).to_be_visible()
    tejas_description_value = page.get_by_test_id(locators['TEJAS_DESCRP'])
    tejas_description_value = tejas_description_value.inner_text()
    #assert tejas_compute_header == ComputeTextData.tejas_compute_header, f"The Tejas Compute header value - {tejas_compute_header}, is different than expected!"
    assert tejas_description_value == ComputeTextData.tejas_description, f"The Tejas Compute header value - {tejas_description_value}, is different than expected!"
    logging.info("Description on Tejas Compute home screen is correct!")


#@pytest.mark.testrail(27298)
@pytest.mark.testrail(65144)
def test_verify_learn_more_section_on_tejas_compute_screen(page, tejas_setup):
    page.wait_for_timeout(TIMEOUT)
    VM_field_visibility = page.locator(locators['VM_NOT_FOUND']).is_visible()
    if VM_field_visibility == True:
        expect(page.get_by_test_id(locators['LEARN_MORE_VM'])).to_be_visible()
        learn_more_value = page.get_by_test_id(locators['LEARN_MORE_VM'])
        text = learn_more_value.inner_text()
        assert text == "Learn More", "Learn More button is not present when no Tejas Compute found"
        page.click("btn-learn-more")
        expected_url = "https://docs-revamp-sbx.yntraa.com//docs/Computes/Compute"
        page.wait_for_timeout(TIMEOUT)
        assert page.url == expected_url, f"Expected URL: {expected_url}, Actual URL: {page.url}"
    else:
        logging.info("Test case failed as Tejas Compute found in the list.")
        VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
        VM_list_count = len(VM_List_elements)
        logging.info(VM_list_count)
        #pytest.skip("Test case skipped as Tejas Compute found in the list.")



"""Perform a click operation on the Create Virtual Machine button and and verify the header on the resulting landing page."""
#@pytest.mark.testrail(27299)
@pytest.mark.testrail(65145)
def test_to_verify_click_on_create_virtual_machine(page, tejas_setup):
    perform_click_on_create_vm_button(page, locators['CREATE_VM_BUTTON'])
    expect(page.get_by_test_id(locators['CREATE_VM_HEADER'])).to_be_visible()
    create_vm_header = page.get_by_test_id(locators['CREATE_VM_HEADER'])
    create_vm_header = create_vm_header.inner_text()
    assert create_vm_header == ComputeTextData.create_vm_header, f"User could not be navigated to {create_vm_header}!!"
    logging.info("User successfully navigated to Create Virtual Machine screen!")


"""Verify the UI of Create Virtual Machine page."""
#@pytest.mark.testrail(27300)
@pytest.mark.testrail(65146)
def test_verify_create_virtual_machine_homescreen(page, tejas_create_vm_setup):
    page.wait_for_timeout(TIMEOUT)
    expect(page.locator(locators['MACHINE_DETAILS_HEADER'])).to_be_visible()
    expect(page.locator(locators['AVAILABILITY_ZN_DROPDOWN'])).to_be_enabled()
    expect(page.locator(locators['CHOOSE_IMAGE'])).to_be_visible()
    page.get_by_text(locators['CHOOSE_FLAVOR']).is_visible()
    page.get_by_text("Machine Credentials").is_visible()
    page.get_by_text("Choose Networks").is_visible()
    page.get_by_text("Choose Security Groups").is_visible()
    expect(page.locator(locators['ROOT_VOLUME_TYPE'])).to_be_visible()
    page.get_by_text("ANTIVIRUS_FIELD").is_visible()
    page.get_by_text("MACHINE_BACKUP").is_visible()

    expect(page.get_by_test_id(locators['PUBLIC_IMAGE'])).to_be_visible()
    expect(page.get_by_test_id(locators['SNAPSHOT'])).to_be_visible()
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON'])).to_be_visible()

#@pytest.mark.testrail(27353)
# @pytest.mark.testrail(65147)
def test_verify_create_button_is_present_and_displyed_the_disable_till_All_required_fillvalue(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    create_button= page.get_by_test_id("confirm")
    if create_button:
        assert create_button.is_visible(), "Create button is not visible"
        assert not create_button.is_enabled(), "Create button should be disabled initially"
    else:
        pytest.fail("Create button not found on the page")

"""Verify the header on Create Virtual Machine page."""
@pytest.mark.testrail(65147)
@pytest.mark.testrail(27301)
def test_to_verify_create_vm_header(page, tejas_create_vm_setup):
    expect(page.get_by_test_id(locators['CREATE_VM_HEADER'])).to_be_visible()
    create_vm_header = page.get_by_test_id(locators['CREATE_VM_HEADER'])
    create_vm_header = create_vm_header.inner_text()
    assert create_vm_header == ComputeTextData.create_vm_header, f"The Create Virtual Machine header value - {create_vm_header}, is different than expected!"
    logging.info("Header on Create Virtual Machine screen is correct!")

"""Verify the description on Create Virtual Machine page."""
@pytest.mark.testrail(27302)
def test_to_verify_create_vm_description(page, tejas_create_vm_setup):
    expect(page.get_by_test_id(locators['CREATE_VM_DESCRP'])).to_be_visible()
    create_vm_description = page.get_by_test_id(locators['CREATE_VM_DESCRP'])
    create_vm_description = create_vm_description.inner_text()
    assert create_vm_description == ComputeTextData.create_vm_description, f"The Create Virtual Machine description value - {create_vm_description}, is different than expected!"
    logging.info("Description on Create Virtual Machine screen is correct!")

"""Verify the description under Machine Details Label."""
@pytest.mark.testrail(27303)
def test_to_verify_machine_detail_description(page, tejas_create_vm_setup):
    machine_detail_description = page.locator(locators['MACHINE_DETAILS_DESCRP']).inner_text()
    assert machine_detail_description ==  ComputeTextData.machine_detail_description, f"The Machine details description value - {machine_detail_description}, is different than expected!"
    logging.info("Description on Machine details section is correct!")

@pytest.mark.testrail(27305)
def test_Verify_Machine_Name_displays_label_inside_the_text_area(page, tejas_create_vm_setup):
    input_box_locator = page.locator('//input[@placeholder="Please enter a name"]')
    expect(input_box_locator).to_be_visible()
    input_box_text = input_box_locator.inner_text()
    assert input_box_text == "", "Input box text is not empty"
    page.wait_for_timeout(TIMEOUT)

"""Verify Machine Name text field is properly displayed and accepts input from user."""
@pytest.mark.testrail(27304)
def test_to_verify_machine_name_input_field(page, tejas_create_vm_setup):
    page.wait_for_timeout(TIMEOUT)
    name_field_visibility = page.locator(locators['NAME_FIELD']).is_visible()
    if name_field_visibility == True:
        page.locator(locators['NAME_FIELD']).type(MACHINE_NAME)
        page.wait_for_timeout(TIMEOUT)
    else:
        logging.info("Name field is not yet visible on create virtual machine screen!")

@pytest.mark.testrail(27308)
def test_to_verify_availability_zone_dropdown(page, tejas_create_vm_setup):
    expect(page.locator(locators['AVAILABILITY_ZONE_DROPDOWN'])).to_be_visible()
    page.locator(locators['AVAILABILITY_ZONE_DROPDOWN']).click()
    ZoneDropdown_elements = page.query_selector_all(f'[data-testid="availability-zone-select-option"]')
    count = len(ZoneDropdown_elements)
    for index, element in enumerate(ZoneDropdown_elements, start=1):
        element_text = element.inner_text()
        print("Selected availability zone:", element_text)
        if "compute-nova" in element_text.lower():
            element.click()
            print("Clicked on compute-nova")
            break
    page.wait_for_timeout(TIMEOUT)


@pytest.mark.testrail(27310)
def test_to_verify_image_section_is_divided_into_two_sub_sections(page, tejas_create_vm_setup):
    expect(page.locator(locators['CHOOSE_IMAGE'])).to_be_visible()
    choose_image_text = page.locator(locators['CHOOSE_IMAGE']).inner_text()
    assert "Choose an Image" in choose_image_text, f"Unexpected text in Choose Image section: {choose_image_text}"
    public_image_tab = page.get_by_test_id(locators['PUBLIC_IMAGE']).is_visible()
    assert public_image_tab, "Public Image section is not visible"
    public_image_text = page.get_by_test_id(locators['PUBLIC_IMAGE']).inner_text()
    assert "Public Image" in public_image_text, f"Unexpected text in Public Image section: {public_image_text}"
    snapshot_tab = page.get_by_test_id(locators['SNAPSHOT']).is_visible()
    assert snapshot_tab, "Snapshot section is not visible"
    snapshot_text = page.get_by_test_id(locators['SNAPSHOT']).inner_text()
    assert "Snapshots" in snapshot_text, f"Unexpected text in Snapshot section: {snapshot_text}"


@pytest.mark.testrail(27313)
def test_Verify_Public_Images_are_displayed_and_user_is_able_to_select_an_image(page, tejas_create_vm_setup):
    expect(page.locator(locators['CHOOSE_IMAGE'])).to_be_visible()
    choose_image_text = page.locator(locators['CHOOSE_IMAGE']).inner_text()
    assert "Choose an Image" in choose_image_text, f"Unexpected text in Choose Image section: {choose_image_text}"
    public_image_tab = page.get_by_test_id(locators['PUBLIC_IMAGE']).is_visible()
    assert public_image_tab, "Public Image section is not visible"
    public_image_text = page.get_by_test_id(locators['PUBLIC_IMAGE']).inner_text()
    assert "Public Image" in public_image_text, f"Unexpected text in Public Image section: {public_image_text}"
    public_image_card = page.query_selector_all(f'[data-testid="{locators["PUBLIC_IMAGE_CARD"]}"]')
    public_card_count = len(public_image_card)
    print("card_count:", public_card_count)
    for index, element in enumerate(public_image_card, start=1):
        element_text = element.inner_text()
        print("Public_Images_Card",element_text)

@pytest.mark.testrail(27314)
def test_Verify_version_dropdown_is_displayed_and_user_can_select_option_from_it(page, tejas_create_vm_setup):
    test_Verify_Public_Images_are_displayed_and_user_is_able_to_select_an_image
    element = page.wait_for_selector('text="Version"')
    assert element.is_visible(), "Version dropdown is not visible"
    version_dropdown_element = page.wait_for_selector(locators['VERSION_DRPDWN'])
    expect(page.locator(locators['VERSION_DRPDWN'])).to_be_visible()
    assert version_dropdown_element.is_visible(), "Version dropdown is not visible"

@pytest.mark.testrail(27315)
def test_Verify_that_Search_box_under_Snapshots_is_accepting_all_types_of_data(page, tejas_create_vm_setup):
    expect(page.locator(locators['CHOOSE_IMAGE'])).to_be_visible()
    choose_image_text = page.locator(locators['CHOOSE_IMAGE']).inner_text()
    assert "Choose an Image" in choose_image_text, f"Unexpected text in Choose Image section: {choose_image_text}"
    snapshot_tab = page.get_by_test_id(locators['SNAPSHOT']).is_visible()
    assert snapshot_tab, "Snapshot section is not visible"
    snapshot_text = page.get_by_test_id(locators['SNAPSHOT']).inner_text()
    assert "Snapshots" in snapshot_text, f"Unexpected text in Snapshot section: {snapshot_text}"
    page.get_by_test_id(locators['SNAPSHOT']).click()
    #search_field_locator = page.locator('input[placeholder="Search "]')
    search_field_locator = page.locator('(//input[@placeholder="Search "])[1]')
    if search_field_locator.is_visible():
        search_field_locator.click()
        search_field_locator.fill("test")
    else:
        print("Search field is not visible")

@pytest.mark.testrail(27317)
def test_Verify_user_is_able_to_select_Root_Volume_size(page, tejas_create_vm_setup):
    page.get_by_test_id(locators['ROOT_VOLUME_HEADER']).is_visible()
    page.get_by_text("Root Volume (in GiB)").is_visible()
    page.get_by_test_id("volume_size").is_visible()
    initial_value = page.locator('#volume_size').get_attribute("value")
    page.get_by_test_id("volume-size-count").click()
    updated_value = page.locator('#volume_size').get_attribute("value")
    assert int(updated_value) >= 50, "Volume size is not updated to at least 50"
    assert updated_value == "100", "Volume size is not updated to 100"
    page.locator('//button[@data-testid="-count"]').click()
    final_value = page.locator('#volume_size').get_attribute("value")
    assert final_value == "50", "Volume size is not set to 50 after selection"


@pytest.mark.testrail(27318)
def test_choose_flavor_description(page, tejas_create_vm_setup):
    page.get_by_text("Choose Flavor").is_visible()
    page.get_by_text(locators['CHOOSE_FLAVOR']).is_visible()
    choose_flavor_description_value = page.locator(locators['CHOOSE_FLAVOR']).inner_text()
    print(choose_flavor_description_value)
    assert choose_flavor_description_value == ComputeTextData.FLAVOUR_DESCRIPTION

@pytest.mark.testrail(27319)
def test_Verify_Flavors_are_displayed_and_user_is_able_to_select_a_flavor(page, tejas_create_vm_setup):
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_text("Choose Flavor").is_visible()
    expect(page.get_by_test_id("tab-compute-intensive")).to_be_visible()
    expect(page.get_by_test_id("tab-general-compute")).to_be_visible()
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count1:", compute_header_count)
    if compute_header_count > 0:
        compute_header_elements[5].click()

@pytest.mark.testrail(27320)
def test_Verify_Your_Machine_Credentials_description(page, tejas_create_vm_setup):
    page.get_by_text("Machine Credentials").is_visible()
    page.get_by_text(locators['MACHINE_CREDENTIALS_DESCRP']).is_visible()
    machine_description_value = page.locator(locators['MACHINE_CREDENTIALS_DESCRP']).inner_text()
    print(machine_description_value)
    assert machine_description_value == ComputeTextData.YOUR_MACHINE_DISCRIPTION

@pytest.mark.testrail(27321)
def test_Verify_Your_Machine_Credentials_is_divided_in_two_groups(page, tejas_create_vm_setup):
    public_image_tab = page.get_by_test_id(locators['PUBLIC_IMAGE']).is_visible()
    public_image_text = page.get_by_test_id(locators['PUBLIC_IMAGE']).inner_text()
    assert "Public Image" in public_image_text, f"Unexpected text in Public Image section: {public_image_text}"
    public_image_card = page.query_selector_all(f'[data-testid="tab-public-image-card"]')
    public_card_count = len(public_image_card)
    print("Number of elements matching the selector:", public_card_count)
    for index, element in enumerate(public_image_card, start=1):
        element_text = element.inner_text()
        print("Public_Images_Card", element_text)
    if public_card_count > 0:
        public_image_card[0].click()
        page.wait_for_timeout(TIMEOUT)
    machine_credentials_visible = page.get_by_text("Machine Credentials").is_visible()
    key_pair_tab = page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).is_visible()
    keypair_text = page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).inner_text()
    assert keypair_text == "Key Pair"
    password_tab = page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).is_visible()
    password_text = page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).inner_text()
    assert password_text == "Username / Password"


@pytest.mark.testrail(27323)
def test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa(page, tejas_create_vm_setup):
    machine_credentials_visible = page.get_by_text("Machine Credentials").is_visible()
    key_pair_tab = page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).is_visible()
    keypair_text = page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).inner_text()
    assert keypair_text == "Key Pair"
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.wait_for_timeout(TIMEOUT)

    page.locator(locators['KEY_PAIR_PLACEHOLDER']).click()
    compute_header_elements1 = page.query_selector_all(f'[data-testid="keypair-id-select-option"]')
    compute_header_count = len(compute_header_elements1)
    if compute_header_count > 0:
        compute_header_elements1[1].click()
    page.wait_for_timeout(TIMEOUT)

    page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).click()
    password_tab = page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).is_visible()
    username_password_visible = page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).inner_text()
    assert username_password_visible == "Username / Password"
    username_password_visible = page.get_by_text("Username / Password").is_visible()
    assert username_password_visible, "Username / Password section is not visible"

@pytest.mark.testrail(27324)
def test_verify_Username_text_field_is_properly_displayed_and_accept_input_from_user(page, tejas_create_vm_setup):
    test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa
    username_input_field = page.get_by_test_id("vm-username-input")
    assert username_input_field.is_visible(), "Username input field is not visible"
    machine_name_field = page.locator(locators['NAME_FIELD_MACHINE'])
    if machine_name_field.is_visible():
        machine_name_field.type("atul-tayade@yopmail.com")
        page.wait_for_timeout(TIMEOUT)
    else:
        pytest.fail("Machine name field is not visible")
        #assert machine_name_field.get_attribute("value") == "atul-tayade@yopmail.com", "Username input was not accepted correctly"

@pytest.mark.testrail(27327)
def test_verify_password_field_is_properly_displayed_and_accept_input_from_user(page, tejas_create_vm_setup):
    test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa
    expect(page.get_by_test_id("vm-password-input")).to_be_visible()
    Machine_name_field_visibility = page.locator(locators['PASSWORD_FIELD_MACHINE']).is_visible()
    if Machine_name_field_visibility == True:
        page.locator(locators['PASSWORD_FIELD_MACHINE']).type("India@143")
        page.wait_for_timeout(TIMEOUT)


@pytest.mark.testrail(27334)
def test_verify_confirm_password_field_is_properly_displayed_and_accept_input_from_user(page, tejas_create_vm_setup):
    test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa
    confirmpassword_visible = page.get_by_text("Confirm Password").is_visible()
    expect(page.get_by_test_id("vm-confirm-password-input")).to_be_visible()
    Machine_name_field_visibility = page.locator(locators['CONF_PASSWORD_FIELD_MACHINE']).is_visible()
    if Machine_name_field_visibility == True:
        page.locator(locators['CONF_PASSWORD_FIELD_MACHINE']).type("India@143")
        page.wait_for_timeout(TIMEOUT)


@pytest.mark.testrail(27335)
def test_verify_password_and_confirm_password_text_field_validate_for_the_same(page, tejas_create_vm_setup):
    test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa
    expect(page.get_by_test_id("vm-password-input")).to_be_visible()
    page.locator(locators['PASSWORD_FIELD_MACHINE']).fill("")
    password_value = "India@143"
    page.fill(locators['PASSWORD_FIELD_MACHINE'], password_value)
    page.wait_for_timeout(TIMEOUT)

    expect(page.get_by_test_id("vm-confirm-password-input")).to_be_visible()
    page.locator(locators['CONF_PASSWORD_FIELD_MACHINE']).fill("")
    confirm_password_value = "India@143"
    page.fill(locators['CONF_PASSWORD_FIELD_MACHINE'], confirm_password_value)
    page.wait_for_timeout(TIMEOUT)

    password_field_value = page.get_by_test_id(locators['PASSWORD_FIELD_MACHINE'])
    confirm_password_field_value = page.get_by_test_id(locators['CONF_PASSWORD_FIELD_MACHINE'])


@pytest.mark.testrail(27338)
def test_verify_Username_password_and_confirm_password_text_field_valid_input(page, tejas_create_vm_setup):
    test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa
    expect(page.get_by_test_id("vm-username-input")).to_be_visible()
    Machine_name_field_visibility = page.locator(locators['NAME_FIELD_MACHINE']).is_visible()
    if Machine_name_field_visibility:
        page.locator(locators['NAME_FIELD_MACHINE']).fill("")
        page.wait_for_timeout(TIMEOUT)
        page.locator(locators['NAME_FIELD_MACHINE']).fill("atul-tayade@yopmail.com")

    expect(page.get_by_test_id("vm-password-input")).to_be_visible()
    password_field_visibility = page.locator(locators['PASSWORD_FIELD_MACHINE']).is_visible()
    if password_field_visibility:
        page.locator(locators['PASSWORD_FIELD_MACHINE']).fill("")
        page.wait_for_timeout(TIMEOUT)
        page.locator(locators['PASSWORD_FIELD_MACHINE']).fill("India@143")

    expect(page.get_by_test_id("vm-confirm-password-input")).to_be_visible()
    conf_password_field_visibility = page.locator(locators['CONF_PASSWORD_FIELD_MACHINE']).is_visible()
    if conf_password_field_visibility:
        page.locator(locators['CONF_PASSWORD_FIELD_MACHINE']).fill("")
        page.wait_for_timeout(TIMEOUT)
        page.locator(locators['CONF_PASSWORD_FIELD_MACHINE']).fill("India@143")


@pytest.mark.testrail(27339)
def test_verify_Choose_Networks_description(page, tejas_create_vm_setup):
    page.get_by_text("Choose Networks").is_visible()
    page.get_by_text(locators['CHOOSE_NET_DESC']).is_visible()
    choose_network_description_value = page.locator(locators['CHOOSE_NET_DESC']).inner_text()
    print(choose_network_description_value)
    assert choose_network_description_value == ComputeTextData.NETWORK_DISCRIPTION

@pytest.mark.testrail(27340)
def test_Verify_Networks_dropdown_is_displayed_and_user_can_select_multiple_options_from_it(page, tejas_create_vm_setup):
    networks_dropdown = page.locator(locators['NETWORKS']).click()
    #elements = page.query_selector_all(f'[data-testid="network_id-listbox"]')
    elements = page.query_selector_all(f'[data-testid="network-id-multi-select"]')
    count = len(elements)
    print("Number of options in the dropdown:", count)
    if count > 0:
        elements[0].click()
    else:
        print("No options found in the dropdown")
    page.wait_for_timeout(10000)


@pytest.mark.testrail(27341)
def test_verify_Choose_securty_description(page, tejas_create_vm_setup):
    page.get_by_text("Choose Security Groups").is_visible()
    page.get_by_text(locators['CHOOSE_SEC_DESC']).is_visible()
    choose_sec_description_value = page.locator(locators['CHOOSE_SEC_DESC']).inner_text()
    print(choose_sec_description_value)
    assert choose_sec_description_value == ComputeTextData.SECURITY_DISCRIPTION

@pytest.mark.testrail(27342)
def test_verify_security_dropdown(page, tejas_create_vm_setup):
    name_field_visibility = page.locator(locators['NAME_FIELD']).is_visible()
    if name_field_visibility == True:
        page.locator(locators['NAME_FIELD']).type(MACHINE_NAME)
        page.wait_for_timeout(TIMEOUT)
    else:
        logging.info("Name field is not yet visible on create virtual machine screen!")
    expect(page.locator(locators['SECURITY_DROPDOWN_BTN'])).to_be_visible()
    page.locator(locators['SECURITY_DROPDOWN_BTN']).click()
    ZoneDropdown_elements = page.query_selector_all(f'[data-testid="sec-group-id-multi-select-option"]')
    count = len(ZoneDropdown_elements)
    for index, element in enumerate(ZoneDropdown_elements, start=1):
        element_text = element.inner_text()
        if "default" in element_text.lower():
            element.click()
            break
    page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(27346)
def test_verify_Add_Labels_functionality(page, tejas_create_vm_setup):
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
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

@pytest.mark.testrail(27347)
def test_Verify_the_Monthly_switch_functionality(page, tejas_create_vm_setup):

    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    monthly_rate_visible = page.locator(locators['MONTHLY_TAB']).is_visible()
    assert monthly_rate_visible , "Monthly  rate options are not visible"
    initial_estimated_cost = page.locator(locators['PRICE_VALUE']).inner_text()
    cost_split = initial_estimated_cost.split("/")
    assert cost_split[-1] == "month", f"Expected 'month', but got '{cost_split[-1]}'"
    print(cost_split)
@pytest.mark.testrail(59828)
def test_Verify_the_Hour_switch_functionality(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    hourly_rate_visible = page.get_by_text("Hourly").is_visible()
    assert hourly_rate_visible , "Hourly rate options are not visible"
    page.get_by_test_id(locators['SWITCH_COST']).click()
    hour_estimated_cost = page.locator(locators['PRICE_VALUE']).inner_text()
    print(hour_estimated_cost)
    #assert hour_estimated_cost.split("/")[-1] == "hour", f"Expected 'month', but got '{hour_estimated_cost}'"
    cost_split = hour_estimated_cost.split("/")
    assert cost_split[-1] == "hour", f"Expected 'hour', but got '{cost_split[-1]}'"


@pytest.mark.testrail(27348)
def test_verify_Summary_section_is_displayed_on_screen(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    summary_button_text = page.get_by_test_id(locators['BTN_SUMMERY']).inner_text()
    logging.info(summary_button_text)
    assert summary_button_text == "View Summary", f"Expected 'View Summary', but got '{summary_button_text}'"
    page.get_by_test_id(locators['BTN_SUMMERY']).click()
    page.wait_for_timeout(1000)
    #page.get_by_text("CREATE_VM_SUMMARY").is_visible()
    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()

@pytest.mark.testrail(27349)
def test_verify_Summary_popup_UI(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    summary_button_text = page.get_by_test_id(locators['BTN_SUMMERY']).inner_text()
    logging.info(summary_button_text)
    assert summary_button_text == "View Summary", f"Expected 'View Summary', but got '{summary_button_text}'"
    page.get_by_test_id(locators['BTN_SUMMERY']).click()
    #page.get_by_text("CREATE_VM_SUMMARY").is_visible()
    expect(page.get_by_test_id(locators['CLOSE_BTN_SUMMARY'])).to_be_visible()
    summery_elements_key = page.query_selector_all(f'[data-testid="summary-field-key"]')
    summery_fild_value = page.query_selector_all(f'[data-testid="summary-field-value"]')
    expected_keys = ["Machine Name", "Image", "Flavor", "Key Pair", "Availability Zone", "Volume Type", "Networks", "Security Groups", "Antivirus", "Backup"]

    if len(summery_elements_key) == len(summery_fild_value):
        for index, (key_element, value_element) in enumerate(zip(summery_elements_key, summery_fild_value), start=1):
            key_text = key_element.inner_text().strip()
            value_text = value_element.inner_text().strip()
            formatted_key = f"{index}. {key_text}"
            print(f"{formatted_key}: {value_text}")
            if key_text in expected_keys:
                print(f"Key: {formatted_key}, Value: {value_text}, Status: Pass")
            else:
                logging.info(f"Key: {formatted_key}, Value: {value_text}, Status: Fail - Unexpected key")
    else:
        logging.info("Error: Lengths of key and value lists do not match.")

    expect(page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT'])).to_be_visible()
    estimated_price_label = page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT']).inner_text()
    Price_value = page.locator(locators['ESTIMATE_PRICE_VALUE']).inner_text()
    logging.info("price:",Price_value)

    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()
    page.wait_for_timeout(1000)

def test_create_virtual_machine(page, tejas_create_vm_setup):
    page.locator(locators['NAME_FIELD']).fill("")
    page.locator(locators['NAME_FIELD']).type(MACHINE_NAME)
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    if compute_header_count > 0:
        compute_header_elements[5].click()
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.locator(locators['KEY_PAIR_PLACEHOLDER']).click()
    compute_header_elements1 = page.query_selector_all(f'[data-testid="keypair-id-select-option"]')
    compute_header_count = len(compute_header_elements1)
    if compute_header_count > 0:
        compute_header_elements1[1].click()
    page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(27350)
def test_Verify_that_changes_on_VM_form_fields_are_reflected_on_Summary_popup(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    summary_button_text = page.get_by_test_id(locators['BTN_SUMMERY']).inner_text()
    logging.info(summary_button_text)
    assert summary_button_text == "View Summary", f"Expected 'View Summary', but got '{summary_button_text}'"
    page.get_by_test_id(locators['BTN_SUMMERY']).click()
    #page.get_by_text("CREATE_VM_SUMMARY").is_visible()
    summary_name = page.locator(locators['SUMMERY_MACHINE_NAME']).inner_text()
    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()
    page.wait_for_timeout(10000)
    test_create_virtual_machine(page, tejas_create_vm_setup)
    page.get_by_test_id(locators['BTN_SUMMERY']).click()
    changes_summary_name = page.locator(locators['SUMMERY_MACHINE_NAME']).inner_text()
    assert changes_summary_name != summary_name, "Summary name is not updated after changes"
    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()
    page.wait_for_timeout(1000)

@pytest.mark.testrail(59906)
def test_verify_estimated_price_label_on_summary_popup_with_monthly_switch(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    summary_button_text = page.get_by_test_id(locators['BTN_SUMMERY']).inner_text()
    logging.info(summary_button_text)
    assert summary_button_text == "View Summary", f"Expected 'View Summary', but got '{summary_button_text}'"
    page.get_by_test_id(locators['BTN_SUMMERY']).click()
    #page.get_by_text("CREATE_VM_SUMMARY").is_visible()
    expect(page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT'])).to_be_visible()
    estimated_price_label = page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT']).inner_text()
    assert estimated_price_label == "Estimated price per month:", f"Expected 'Estimated price per month:', but got '{estimated_price_label}'"
    Price_value = page.locator(locators['ESTIMATE_PRICE_VALUE']).inner_text()
    print("price:",Price_value)
    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()
    page.wait_for_timeout(1000)


@pytest.mark.testrail(59907)
def test_verify_estimated_price_label_on_summary_popup_with_hourly_switch(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    page.get_by_test_id(locators['SWITCH_COST']).click()
    summary_button_text = page.get_by_test_id(locators['BTN_SUMMERY']).inner_text()
    logging.info(summary_button_text)
    assert summary_button_text == "View Summary", f"Expected 'View Summary', but got '{summary_button_text}'"
    page.get_by_test_id(locators['BTN_SUMMERY']).click()
    #page.get_by_text("CREATE_VM_SUMMARY").is_visible()
    expect(page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT'])).to_be_visible()
    estimated_price_label = page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT']).inner_text()
    assert estimated_price_label == "Estimated price per hour:", f"Expected 'Estimated price per hour:', but got '{estimated_price_label}'"
    Price_value = page.locator(locators['ESTIMATE_PRICE_VALUE']).inner_text()
    print("price:",Price_value)
    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()
    page.wait_for_timeout(1000)
    page.get_by_test_id(locators['SWITCH_COST']).click()

@pytest.mark.testrail(27351)
def test_verify_price_value_on_summary_popup_with_monthly_switch(page, tejas_create_vm_setup):
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    monthly_rate_visible = page.locator(locators['MONTHLY_TAB']).is_visible()
    assert monthly_rate_visible , "Monthly  rate options are not visible"
    initial_estimated_cost = page.locator(locators['PRICE_VALUE']).inner_text()
    print(initial_estimated_cost)
    initial_estimated_cost_value = initial_estimated_cost.split("/")[0].strip()
    assert initial_estimated_cost.split("/")[-1] == "month", f"Expected 'month', but got '{initial_estimated_cost}'"

    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    summary_button_text = page.get_by_test_id(locators['BTN_SUMMERY']).inner_text()
    logging.info(summary_button_text)
    assert summary_button_text == "View Summary", f"Expected 'View Summary', but got '{summary_button_text}'"
    page.get_by_test_id(locators['BTN_SUMMERY']).click()

   # page.get_by_text("CREATE_VM_SUMMARY").is_visible()

    estimated_price_label = page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT']).inner_text()
    assert estimated_price_label == "Estimated price per month:", f"Expected 'Estimated price per month:', but got '{estimated_price_label}'"
    estimated_price_value = page.locator(locators['ESTIMATE_PRICE_VALUE']).inner_text()
    print("price:",estimated_price_value)
    assert estimated_price_value == initial_estimated_cost_value, f"Estimated price value doesn't match initial estimated cost: {estimated_price_value} vs {initial_estimated_cost}"
    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()
    page.wait_for_timeout(10000)

@pytest.mark.testrail(59940)
def test_verify_price_value_on_summary_popup_with_hourly_switch(page, tejas_create_vm_setup):
    page.get_by_test_id(locators['SWITCH_COST']).click()
    page.wait_for_timeout(1000)
    initial_estimated_cost = page.locator(locators['PRICE_VALUE']).inner_text()
    initial_estimated_cost_value = initial_estimated_cost.split("/")[0].strip()
    summary_button_text = page.get_by_test_id(locators['BTN_SUMMERY']).inner_text()
    logging.info(summary_button_text)
    assert summary_button_text == "View Summary", f"Expected 'View Summary', but got '{summary_button_text}'"
    page.get_by_test_id(locators['BTN_SUMMERY']).click()
    page.wait_for_timeout(1000)
   # page.get_by_text("CREATE_VM_SUMMARY").is_visible()

    hourly_switch_selected = page.get_by_text("Hourly").is_visible()
    assert hourly_switch_selected, "Hourly switch is not selected"
    estimated_price_label = page.get_by_test_id(locators['ESTIMATE_PRICE_TEXT']).inner_text()
    assert estimated_price_label == "Estimated price per hour:", f"Expected 'Estimated price per month:', but got '{estimated_price_label}'"
    estimated_price_value = page.locator(locators['ESTIMATE_PRICE_VALUE']).inner_text()
    print("price:",estimated_price_value)
    assert estimated_price_value == initial_estimated_cost_value, f"Estimated price value doesn't match initial estimated cost: {estimated_price_value} vs {initial_estimated_cost_value}"
    page.get_by_test_id(locators['CLOSE_BTN_SUMMARY']).click()
    page.wait_for_timeout(10000)
    page.get_by_test_id(locators['SWITCH_COST']).click()

@pytest.mark.testrail(27352)
def test_Verify_Cancel_button_functionality(page, tejas_create_vm_setup):
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CANCEL_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    discard_popup = page.get_by_test_id(locators['CONFIRMATION_TEXT']).inner_text()
    assert discard_popup == "Discard changes", f"Cancel button should be present '{discard_popup}'"
    page.locator(locators['CANCEL_POPUP']).click()
    page.wait_for_timeout(1000)

@pytest.mark.testrail(59942)
def test_verify_cancel_button_functionality_on_Cancel_popup(page, tejas_create_vm_setup):
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CANCEL_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    discard_popup = page.get_by_test_id(locators['CONFIRMATION_TEXT']).inner_text()
    assert discard_popup == "Discard changes", f"Cancel button should be present '{discard_popup}'"
    page.get_by_text("CANCEL_POPUP").is_visible()
    page.locator(locators['CANCEL_POPUP']).click()
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    expect(page.get_by_test_id(locators['CREATE_VM_HEADER'])).to_be_visible()

@pytest.mark.testrail(27354)
def test_create_button_enabled_after_required_fields_filled(page, tejas_create_vm_setup):
    test_create_virtual_machine(page, tejas_create_vm_setup)
    final_create_vm_button_locator = locators['FINAL_CREATE_VM_BUTTON']
    create_button_element = page.get_by_test_id(final_create_vm_button_locator)
    assert create_button_element, f"Unable to find Create button using locator: {final_create_vm_button_locator}"
    create_button = create_button_element.is_enabled() if create_button_element else False
    assert create_button, "Create button should be enabled after filling all required fields"

@pytest.mark.testrail(27355)
def test_Create_button_functionality_for_creating_virtual_machine(page, tejas_create_vm_setup):
    test_create_virtual_machine(page, tejas_create_vm_setup)
    create_button = page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON'])
    assert create_button, f"Final Create VM button not found using locator: {locators['FINAL_CREATE_VM_BUTTON']}"
    expect(create_button).to_be_visible()
    create_button.click()
    confirmation_text = page.get_by_test_id(locators['CONFIRMATION_TEXT'])
    assert confirmation_text, f"Confirmation text not found using locator: {locators['CONFIRMATION_TEXT']}"
    expect(confirmation_text).to_be_visible()
    page.get_by_text(locators['CONFIRM_DETAILS_POPUP'])
    confirm_details_popup = page.locator(locators['CONFIRM_DETAILS_POPUP']).inner_text()
    assert confirm_details_popup, f"Confirm Details popup not found using locator: {locators['CONFIRM_DETAILS_POPUP']}"
    page.get_by_test_id(locators['CLOSE_BTN']).click()
@pytest.mark.testrail(59821)
def test_confirm_detail_popup_UI(page, tejas_create_vm_setup):
    test_create_virtual_machine(page, tejas_create_vm_setup)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_text(locators['CONFIRM_DETAILS_POPUP'])
    Cnfirmation_Discription = page.get_by_test_id(locators['CONFIRM_DISCRIPTION']).inner_text()
    assert Cnfirmation_Discription == ComputeTextData.CONFIRM_HEADER_DISCRIPTION
    summery_elements_key = page.query_selector_all(f'[data-testid="summary-field-key"]')
    summery_fild_value = page.query_selector_all(f'[data-testid="summary-field-value"]')
    expected_keys = ["Machine Name", "Image", "Flavor", "Key Pair", "Availability Zone", "Volume Type", "Networks", "Security Groups", "Antivirus", "Backup"]

    if len(summery_elements_key) == len(summery_fild_value):
        for index, (key_element, value_element) in enumerate(zip(summery_elements_key, summery_fild_value), start=1):
            key_text = key_element.inner_text().strip()
            value_text = value_element.inner_text().strip()
            formatted_key = f"{index}. {key_text}"
            print(f"{formatted_key}: {value_text}")
            if key_text in expected_keys:
                print(f"Key: {formatted_key}, Value: {value_text}, Status: Pass")
            else:
                logging.info(f"Key: {formatted_key}, Value: {value_text}, Status: Fail - Unexpected key")
    else:
        logging.info("Error: Lengths of key and value lists do not match.")

    expect(page.get_by_test_id(locators['TOTAL_ESTIMATE_PRICE'])).to_be_visible()
    estimated_price_label = page.get_by_test_id(locators['TOTAL_ESTIMATE_PRICE']).inner_text()
    logging.info("price:",estimated_price_label)
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['PRICE_DISCRIPTION'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    page.get_by_text("CANCEL_POPUP").is_visible()
    page.get_by_test_id(locators['CLOSE_BTN']).click()

@pytest.mark.testrail(59822)
def test_Verify_the_Tejas_Compute_VM_information_over_Confirm_Details_popup(page, tejas_create_vm_setup):
    page.locator(locators['NAME_FIELD']).fill("")
    page.wait_for_timeout(10000)
    page.locator(locators['NAME_FIELD']).type(MACHINE_NAME)
    name = page.get_by_test_id(locators['MACHINE_NAME_VALUE']).inner_text()
    print("test",name)
    created_machine_name = page.locator(locators['NAME_FIELD']).inner_text()
    print("value",created_machine_name)
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    if compute_header_count > 0:
        compute_header_elements[5].click()
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.locator(locators['KEY_PAIR_PLACEHOLDER']).click()
    compute_header_elements1 = page.query_selector_all(f'[data-testid="keypair-id-select-option"]')
    compute_header_count = len(compute_header_elements1)
    if compute_header_count > 0:
        compute_header_elements1[1].click()
    page.wait_for_timeout(TIMEOUT)

    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_text(locators['CONFIRM_DETAILS_POPUP'])
    Cnfirmation_Discription = page.get_by_test_id(locators['CONFIRM_DISCRIPTION']).inner_text()
    assert Cnfirmation_Discription == ComputeTextData.CONFIRM_HEADER_DISCRIPTION
    summery_elements_key = page.query_selector_all(f'[data-testid="summary-field-key"]')
    summery_fild_value = page.query_selector_all(f'[data-testid="summary-field-value"]')
    expected_keys = ["Machine Name", "Image", "Flavor", "Key Pair", "Availability Zone", "Volume Type", "Networks", "Security Groups", "Antivirus", "Backup"]

    if len(summery_elements_key) == len(summery_fild_value):
        for index, (key_element, value_element) in enumerate(zip(summery_elements_key, summery_fild_value), start=1):
            key_text = key_element.inner_text().strip()
            value_text = value_element.inner_text().strip()
            formatted_key = f"{index}. {key_text}"
            print(f"{formatted_key}: {value_text}")
            if key_text in expected_keys:
                print(f"Key: {formatted_key}, Value: {value_text}, Status: Pass")
            else:
                logging.info(f"Key: {formatted_key}, Value: {value_text}, Status: Fail - Unexpected key")
    else:
        logging.info("Error: Lengths of key and value lists do not match.")

    expect(page.get_by_test_id(locators['TOTAL_ESTIMATE_PRICE'])).to_be_visible()
    estimated_price_label = page.get_by_test_id(locators['TOTAL_ESTIMATE_PRICE']).inner_text()
    logging.info("price:",estimated_price_label)
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['PRICE_DISCRIPTION'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    page.get_by_text("CANCEL_POPUP").is_visible()
    page.get_by_test_id(locators['CLOSE_BTN']).click()

@pytest.mark.testrail(59823)
def test_Verify_the_Cancel_button_over_Confirm_Details_popup(page, tejas_create_vm_setup):
    test_create_virtual_machine(page, tejas_create_vm_setup)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_text(locators['CONFIRM_DETAILS_POPUP'])
    Cnfirmation_Discription = page.get_by_test_id(locators['CONFIRM_DISCRIPTION']).inner_text()
    assert Cnfirmation_Discription == ComputeTextData.CONFIRM_HEADER_DISCRIPTION
    page.locator(locators['CANCEL_POPUP']).click()
    expect(page.get_by_test_id("btn-summary")).to_be_visible()
    expect(page.get_by_test_id(locators['CREATE_VM_HEADER'])).to_be_visible()


@pytest.mark.testrail(59824)
def test_Verify_the_Confirm_button_over_Confirm_Details_popup(page, tejas_create_vm_setup):
    test_create_virtual_machine(page, tejas_create_vm_setup)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_text(locators['CONFIRM_DETAILS_POPUP'])
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    page.get_by_text("CANCEL_POPUP").is_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Creating virtual machine"
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(28018)
def test_verify_duplicity_for_Virtual_Machine_name_functionality(page, tejas_create_vm_setup):
    page.locator(locators['NAME_FIELD']).type("COMPUTE_1")
    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    #compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_INTENSIVE_CARD"]}"]')
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    if compute_header_count > 0:
        compute_header_elements[5].click()

    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.locator(locators['KEY_PAIR_PLACEHOLDER']).click()
    compute_header_elements1 = page.query_selector_all(f'[data-testid="keypair-id-select-option"]')
    compute_header_count = len(compute_header_elements1)
    if compute_header_count > 0:
        compute_header_elements1[1].click()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_text(locators['CONFIRM_DETAILS_POPUP'])
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    page.get_by_text("CANCEL_POPUP").is_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    page.wait_for_timeout(20000)
    page.get_by_test_id(locators['CREATE_VM_BUTTON']).click()
    page.locator(locators['NAME_FIELD']).type("COMPUTE_1")

    page.get_by_test_id(locators['COMPUTE_GENERAL_TAB']).click()
    #compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_INTENSIVE_CARD"]}"]')
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_GENERAL_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    if compute_header_count > 0:
        compute_header_elements[5].click()
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.locator(locators['KEY_PAIR_PLACEHOLDER']).click()
    compute_header_elements1 = page.query_selector_all(f'[data-testid="keypair-id-select-option"]')
    compute_header_count = len(compute_header_elements1)
    if compute_header_count > 0:
        compute_header_elements1[1].click()
    page.wait_for_timeout(3000)
    page.get_by_test_id(locators['FINAL_CREATE_VM_BUTTON']).click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    page.get_by_text(locators['CONFIRM_DETAILS_POPUP'])
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    page.get_by_text("CANCEL_POPUP").is_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    assert toast_text == "VM with name 'Compute_1' alreday exist"


@pytest.mark.testrail(27357)
def test_Verify_search_functionality(page, tejas_setup):
    verify_to_logout_function(page)
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count:", compute_header_count)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    VM_Name_elements = page.query_selector_all(f'[data-testid="resource-name-link"]')
    VM_name_count = len(VM_Name_elements)
    print("VM_List_elements:", VM_name_count)
    if VM_name_count > 0:
        first_VM_name = VM_Name_elements[0].inner_text()
        print("First VM name:", first_VM_name)
    else:
        print("No VM names found.")
    page.locator(locators['SEARCH_FIELD']).fill(first_VM_name)
    page.wait_for_timeout(1000)
    found_match = False
    for element in VM_Name_elements:
        if element.inner_text() == first_VM_name:
            found_match = True
            break

    assert found_match, f"No match found for {first_VM_name} in VM names"


@pytest.mark.testrail(27358)
def test_Verify_Virtual_Machine_configuration_info_for_name(page, tejas_setup):
    verify_to_logout_function(page)
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count:", compute_header_count)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    VM_Name_elements = page.query_selector_all(f'[data-testid="resource-name-link"]')
    VM_name_count = len(VM_Name_elements)
    if VM_name_count > 0:
        first_VM_name = VM_Name_elements[0].inner_text()
        VM_Name_elements[0].click()
        configuration_name = page.get_by_test_id(locators['CONFIGURATION_HEADING_NAME']).inner_text()
        assert configuration_name == first_VM_name, f"Configuration name '{configuration_name}' does not match first VM name '{first_VM_name}'"
    else:
        print("No VM names found.")
    page.get_by_test_id(locators['BACK_BTN']).click()
    page.wait_for_timeout(10000)



@pytest.mark.testrail(27359)
def test_Verify_Virtual_Machine_onfiguration_info_for_vCPU_GiB_Ram_and_GiB_Disk(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    vCPU_elements = page.query_selector_all(f'[data-testid="vcpu"]')
    cpu_count = len(vCPU_elements)
    if cpu_count > 0:
        cpu_value = vCPU_elements[0].inner_text()
        print("vCPU:", cpu_value)
    else:
        print("vCPU element not found.")

    GiB_Ram_elements = page.query_selector_all(f'[data-testid="ram"]')
    ram_count = len(GiB_Ram_elements)
    if ram_count > 0:
        ram_value = GiB_Ram_elements[0].inner_text()
        print("GiB Ram:", ram_value)
    else:
        print("GiB RAM element not found.")

    GiB_Disk_elements = page.query_selector_all(f'[data-testid="disk"]')
    disk_count = len(GiB_Disk_elements)
    if disk_count > 0:
        disk_value = GiB_Disk_elements[0].inner_text()
        print("GiB Disk:", disk_value)
    else:
        print("GiB Disk element not found.")


@pytest.mark.testrail(27360)
def test_Verify_VM_Status(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    print("Status:", status_text)
    valid_statuses = ["active", "running", "processing", "inactive"]
    assert status_text in valid_statuses, f"Unexpected status: {status_text}"
    assert status_text == "active", "The VM is not in running state"


@pytest.mark.testrail(27368)
def test_virtual_machine_configuration_info_for_lable(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    label_element = page.query_selector_all(f'[data-testid="{locators["LABEL_TAG"]}"]')
    label_elemnt_count = len(label_element)
    if label_elemnt_count > 0:
        label_name = label_element[0].inner_text()
        logging.info("labels",label_name)

@pytest.mark.testrail(27367)
def test_Verify_Public_IP_Configuration(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    public_ip_section = page.query_selector(f'[data-testid="{locators["PUBLIC_IP_SECTION"]}"]')
    if public_ip_section:
        public_ip_address = public_ip_section.inner_text()
        attached_public_ip = "10.80.24.111"
        if public_ip_address:
            assert public_ip_address == attached_public_ip, "Public IP address mismatch"
        else:
            print("Public IP address is empty.")
    else:
        print("Public IP element not found.")


@pytest.mark.testrail(27369)
def test_Verify_VM_Configuration_created_Info(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    creation_info_element = page.query_selector(locators['VM_CREATION_INFO'])
    page.wait_for_timeout(1000)
    created_info = page.query_selector_all(f'[data-testid="created"]')
    info_count = len(created_info)
    if info_count > 0:
        vm_created_info = created_info[0].inner_text()
    assert vm_created_info, "Creation info element not found."

@pytest.mark.testrail(27370)
def test_Verify_VM_Configuration_updated_Info(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    creation_info_element = page.query_selector(locators['VM_UPDATION_INFO'])
    page.wait_for_timeout(1000)
    updated_info = page.query_selector_all(f'[data-testid="updated"]')
    update_count = len(updated_info)
    if update_count > 0:
        vm_updated_info = updated_info[0].inner_text()
    assert vm_updated_info, "updated info element not found."

@pytest.mark.testrail(27932)
def test_verify_Active_status_against_created_virtual_machine(page, tejas_create_vm_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    print("Status:", status_text)
    valid_statuses = ["active", "running", "processing", "inactive"]
    assert status_text in valid_statuses, f"Unexpected status: {status_text}"
    assert status_text == "active", "The VM is not in running state"

@pytest.mark.testrail(27356)
def test_Verify_user_is_able_to_view_the_listings_of_virtual_machines(page, tejas_setup):
    verify_to_logout_function(page)
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(TIMEOUT)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count:", compute_header_count)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)

    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)

    if VM_list_count > 0:
        VM_List_elements[0].click()

        page.wait_for_selector(f'[data-testid="ellipsis-item"]')

        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            print("Text value of ellipsis-item:", text_value)
            items_to_verify = ["Shutoff", "Pause", "Reboot", "Hard Reboot", "Lock", "Suspend", "Resize",
                               "Install Antivirus", "Enable Backup", "Attach Public IP","Manage Labels",
                               "Take Snapshot", "Attach Volume", "Attach Network", "Attach Security Groups",
                               "Console", "Console logs", "Delete"]
            assert text_value in items_to_verify, f"Item {text_value} not found in {items_to_verify}"

        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Pause":
                item.click()
                print("Clicked on Pause")
                break
        page.locator(locators['OK_BTN']).click()
    else:
        print("No Ellipsis item found.")

@pytest.mark.testrail(59943)
def test_verify_description_under_Anti_Virus_Protection_heading(page, tejas_create_vm_setup):
    perform_click_on_create_vm_button(page, locators['CREATE_VM_BUTTON'])
    page.get_by_text("ANTIVIRUS_FIELD").is_visible()
    page.get_by_text(locators['ANTIVIRUS_FIELD_DESC']).is_visible()
    antivirus_description_value = page.locator(locators['ANTIVIRUS_FIELD_DESC']).inner_text()
    assert antivirus_description_value == ComputeTextData.ANTIVIRUS_DISCRIPTION, f"Unexpected description: {antivirus_description_value}"


@pytest.mark.testrail(59944)
def test_select_and_unselect_antivirus_protection_checkbox(page, tejas_create_vm_setup):
    page.get_by_text("ANTIVIRUS_FIELD").is_visible()
    antivirus_checkbox = page.locator(locators['ANTIVIRUS_CHECKBOX_tab'])
    antivirus_checkbox.click()
    expect(page.get_by_test_id(locators['ANTIVIRUS_PORT_DETAIL'])).to_be_visible()
    #expect(antivirus_checkbox).to_have_attribute('checked', True)
    page.wait_for_timeout(10000)
    antivirus_checkbox.click()
    expect(page.get_by_test_id(locators['ANTIVIRUS_PORT_DETAIL'])).not_to_be_visible()
    #expect(antivirus_checkbox).not_to_have_attribute('checked')

@pytest.mark.testrail(59945)
def test_verify_antivirus_price_display(page, tejas_create_vm_setup):
    expect(page.get_by_test_id(locators['ANTIVIRUS_PRICE'])).to_be_visible()
    page.wait_for_timeout(10000)
    antivirus_price = page.get_by_test_id(locators['ANTIVIRUS_PRICE']).inner_text()
    print("prise",antivirus_price)
    expected_price_pattern = r'₹\d+(\.\d+)? / (Month|Hour)'
    assert re.match(expected_price_pattern, antivirus_price), \
        f"Unexpected Anti-Virus price format: {antivirus_price}. Expected format: ₹X.XX / Month or ₹X.XX / Hour"
@pytest.mark.testrail(59946)
def test_verify_cloud_init_description_display(page, tejas_create_vm_setup):
    page.get_by_text("CLOUD_INTIT_STAGE").is_visible()
    page.get_by_text(locators['CLOUD_INIT_DESCRIPTION']).is_visible()
    cloud_init_description = page.locator(locators['CLOUD_INIT_DESCRIPTION']).inner_text()
    assert cloud_init_description == ComputeTextData.CLOUD_INIT_DISCR, f"Unexpected description: {cloud_init_description}"

@pytest.mark.testrail(59947)
def test_Verify_the_add_initialization_script_checkbox_functionality(page, tejas_create_vm_setup):
    page.get_by_text("CLOUD_INTIT_STAGE").is_visible()
    page.get_by_text("INITIALIZATION_SCRIPTS").is_visible()
    antivirus_checkbox = page.locator(locators['INITIALIZATION_SCRIPTS_CHECKBOX'])
    antivirus_checkbox.click()
    expect(page.get_by_test_id(locators['INITIALIZATION_SCRIPTS_COMMENT'])).to_be_visible()
    page.wait_for_timeout(10000)
    antivirus_checkbox.click()
    expect(page.get_by_test_id(locators['INITIALIZATION_SCRIPTS_COMMENT'])).not_to_be_visible()

@pytest.mark.testrail(59948)
def test_Verify_input_box_is_visible_when_user_has_selected_the_Add_initialization_script_checkbox(page, tejas_create_vm_setup):
    page.get_by_text("CLOUD_INTIT_STAGE").is_visible()
    page.get_by_text("INITIALIZATION_SCRIPTS").is_visible()
    antivirus_checkbox = page.locator(locators['INITIALIZATION_SCRIPTS_CHECKBOX'])
    antivirus_checkbox.click()
    expect(page.get_by_test_id(locators['INITIALIZATION_SCRIPTS_COMMENT'])).to_be_visible()
    page.wait_for_timeout(10000)
    input_box_locator = page.locator('//textarea[@placeholder="Enter your data here..."]')
    expect(input_box_locator).to_be_visible()
    input_box_text = input_box_locator.inner_text()
    assert input_box_text == "", "Input box text is not empty"


@pytest.mark.testrail(59949)
def test_input_box_functionality_for_Add_initialization_script_checkbox(page, tejas_create_vm_setup):
    #page.get_by_text("CLOUD_INTIT_STAGE").is_visible()
    page.get_by_text("INITIALIZATION_SCRIPTS").is_visible()
    antivirus_checkbox = page.locator(locators['INITIALIZATION_SCRIPTS_CHECKBOX'])
    antivirus_checkbox.click()
    expect(page.get_by_test_id(locators['INITIALIZATION_SCRIPTS_COMMENT'])).to_be_visible()
    page.wait_for_timeout(1000)
    input_box_locator = page.locator('//textarea[@placeholder="Enter your data here..."]')
    expect(input_box_locator).to_be_visible()
    sample_commands = """
    #cloud-config
    users:
    - name: myuser
      ssh_authorized_keys:
        - ssh-rsa <your-public-key>
    packages:
      - nginx
    runcmd:
      - systemctl start nginx
    """
    input_box_locator.fill(sample_commands)
    entered_text = input_box_locator.get_attribute("value")
    logging.info("Entered text:", entered_text)
    # assert entered_text.strip(), "Entered text should not be empty"

def change_project_details(page):
    page.get_by_test_id(locators['PROJECT_CHANGE']).click()
    page.locator(locators['PROJECT_SELECTION_PLACEHOLDER']).click()
    change_project_elements = page.query_selector_all(f'[data-testid="project-id-select-option"]')
    compute_header_count = len(change_project_elements)
    print(compute_header_count)
    for index, element in enumerate(change_project_elements):
        element_text = element.inner_text()
        print("text", element_text)
        if "automation_project" in element_text.lower():
            element.click()
            break
    page.get_by_test_id(locators['BTN_SELECT']).click()

def verify_to_setup(page):

    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    compute_header_count = len(compute_header_elements)
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        print(element_text)
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()




@pytest.mark.testrail(64980)
def test_verify_shutoff_feature(page ,tejas_create_vm_setup):
    change_project_details(page)
    verify_to_setup(page)
    VM_Name_elements = page.query_selector_all(f'[data-testid="resource-name-link"]')
    VM_name_count = len(VM_Name_elements)
    if VM_name_count > 0:
        first_VM_name = VM_Name_elements[0].inner_text()
        VM_Name_elements[0].click()
        configuration_name = page.get_by_test_id(locators['CONFIGURATION_HEADING_NAME']).inner_text()
        assert configuration_name == first_VM_name, f"Configuration name '{configuration_name}' does not match first VM name '{first_VM_name}'"
    else:
        print("No VM names found.")

    action_elements = page.query_selector_all(f'[data-testid="btn-action"]')
    action_count = len(action_elements)
    print(action_count)
    if action_count > 0:
        action_elements[0].click()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Performing Action: Stop"
    page.wait_for_timeout(10000)
    page.get_by_test_id(locators['BACK_BTN']).click()
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    print("Status:", status_text)
    valid_statuses = ["active", "running", "processing", "inactive", "shutoff"]
    assert status_text in valid_statuses, f"Unexpected status: {status_text}"
    assert status_text == "shutoff", "The VM is not in running state"

@pytest.mark.testrail(64981)
def test_Verify_the_Start_action_for_VM_that_is_in_shutoff_state(page, tejas_setup):
    verify_to_setup(page)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')

        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            print("Text value of ellipsis-item:", text_value)
            items_to_verify = ["Start", "Hard Reboot", "Lock", "Suspend", "Install Antivirus" ,"Delete"]
            assert text_value in items_to_verify, f"Item {text_value} not found in {items_to_verify}"

        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Start":
                item.click()
                print("Clicked on Start")
                break
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Performing Action: Start"
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(64982)
def test_Verify_the_Hard_Reboot_action_for_VM_that_isin_shutoff_state(page, tejas_setup):
    verify_to_setup(page)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Hard Reboot":
                item.click()
                print("Clicked on Hard Reboot")
                break
    expect(page.get_by_text("Are you sure you want to hard reboot virtual machine?")).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Performing Action: Hard Reboot"
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(64983)
def test_Verify_the_Lock_action_for_VM_that_shutoff_state(page, tejas_setup):
    verify_to_setup(page)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')

        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Lock":
                item.click()
                print("Clicked on Lock")
                break
    expect(page.get_by_text("Are you sure you want to lock virtual machine?")).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Performing Action: Lock"
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(64984)
def test_Verify_the_Unlock_action_for_VM_that_shutoff_state(page, tejas_setup):
    verify_to_setup(page)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')

        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Unlock":
                item.click()
                print("Clicked on Lock")
                break
    expect(page.get_by_text("Are you sure you want to unlock virtual machine?")).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Performing Action: Unlock"
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(64985)
def test_Verify_the_Suspend_action_for_VM_that_shutoff_state(page, tejas_setup):
    verify_to_setup(page)
    page.wait_for_timeout(10000)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    VM_List_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    VM_list_count = len(VM_List_elements)
    if VM_list_count > 0:
        VM_List_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')

        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Suspend":
                item.click()
                print("Clicked on Suspend")
                break
    expect(page.get_by_text("Are you sure you want to suspend virtual machine?")).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator('//div[@role="alert"]').inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Performing Action: Suspend"
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()

@pytest.mark.testrail(64986)
def test_Verify_the_Delete_action_for_VM_that_shutoff_state(page, tejas_setup):
    change_project_details(page)
    verify_to_setup(page)
    page.wait_for_timeout(10000)
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
    print("Toast Text:", toast_text)
    page.wait_for_timeout(1000)
    assert toast_text == "Deleting virtual machine"

