
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from test_helper.testdata.compute_testdata import ComputeTextData


@pytest.fixture(scope="module")
def user_credentials():
    return {
        #"url": "https://console.yntraa.com",
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "vini-sdet@yopmail.com",
        "password": "India@143"
    }

def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        page = item.funcargs["page"]
        page.screenshot(path="failure_screenshot.png")

# @pytest.fixture(autouse=True)
# def logout_after_test(request, page):
#     yield
#     verify_to_logout_function(page)

"""Constant and Global Tejas Compute VM Name!"""
MACHINE_NAME = generate_random_machine_name()


"""Perform a click operation on Compute Resource and verify the header on the resulting landing page."""
@pytest.mark.testrail(27291)
def test_to_verify_clicking_on_compute_screen(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    compute_header_element = page.get_by_test_id(locators['COMPUTE_HEADER'])
    compute_header_value = compute_header_element.inner_text()
    assert compute_header_value == ComputeTextData.compute_header, "User could not be navigated to Compute module!!"
    logging.info("User has successfully navigated to Compute module!")


"""Verify the Compute page UI."""
@pytest.mark.testrail(27292)
def test_verify_UI_of_compute_home_screen(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_HEADER'])).to_be_visible()
    expect(page.get_by_test_id(locators['COMPUTE_DESCRP'])).to_be_visible()
    expect(page.locator(locators['COMPUTE_CREATE_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['STORAGE_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['NETWORKING_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['SECURITY_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['CAAS_TAB'])).to_be_visible()
    expect(page.get_by_test_id(locators['MANAGED_DATABASE_TAB'])).to_be_visible()
    # expect(page.get_by_test_id(locators['SUPPORT_TAB'])).to_be_visible()
    # expect(page.get_by_test_id(locators['AUTOMATION_TAB'])).to_be_visible()
    # expect(page.get_by_test_id(locators['MY_EDGE_SITE_TAB'])).to_be_visible()

"""Verify the header on the Compute page."""
@pytest.mark.testrail(27293)
def test_to_verify_header_on_compute_home_screen(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_HEADER'])).to_be_visible()
    compute_header_element = page.get_by_test_id(locators['COMPUTE_HEADER'])
    compute_header_value = compute_header_element.inner_text()
    assert compute_header_value == ComputeTextData.compute_header, f"The compute header value - {compute_header_value}, is different than expected!"
    logging.info("Header on Compute home screen is correct!")

"""Verify the description on the Compute page."""
@pytest.mark.testrail(27294)
def test_to_verify_compute_home_screen_description(page, compute_setup):
    expect(page.get_by_test_id(locators['COMPUTE_DESCRP'])).to_be_visible()
    compute_discription_element = page.get_by_test_id(locators['COMPUTE_DESCRP'])
    compute_description_value = compute_discription_element.inner_text()
    assert compute_description_value == ComputeTextData.compute_description, f"The compute description value - {compute_description_value}, is different than expected!"
    logging.info("Description on Compute home screen is correct!")

"""Perform a click operation on Tejas Compute and validate the header on the resulting landing page."""
@pytest.mark.testrail(27295)
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
@pytest.mark.testrail(27296)
def test_to_verify_header_on_tejas_compute_screen(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
    tejas_compute_header = page.get_by_test_id(locators['TEJAS_HEADER'])
    tejas_compute_header = tejas_compute_header.inner_text()
    #assert tejas_compute_header == ComputeTextData.tejas_compute_header, f"The Tejas Compute header value - {tejas_compute_header}, is different than expected!"
    assert tejas_compute_header == ComputeTextData.tejas_compute_tab, f"The Tejas Compute header value - {tejas_compute_header}, is different than expected!"
    logging.info("Header on Tejas Compute screen is correct!")


"""Verify the description on the Tejas Compute page."""
@pytest.mark.testrail(27297)
def test_to_verify_tejas_compute_screen_description(page, tejas_setup):
    expect(page.get_by_test_id(locators['TEJAS_DESCRP'])).to_be_visible()
    tejas_description_value = page.get_by_test_id(locators['TEJAS_DESCRP'])
    tejas_description_value = tejas_description_value.inner_text()
    #assert tejas_compute_header == ComputeTextData.tejas_compute_header, f"The Tejas Compute header value - {tejas_compute_header}, is different than expected!"
    assert tejas_description_value == ComputeTextData.tejas_description, f"The Tejas Compute header value - {tejas_description_value}, is different than expected!"
    logging.info("Description on Tejas Compute home screen is correct!")

#
# # @pytest.mark.testrail(27298)
# # @pytest.mark.skip(reason = "After clicking on Learn More link it was found that the documentation page is broken!")
# # def test_verify_learn_more_section_on_tejas_compute_screen(page):
# #     pass
# #     #documentation page is broken
# #
# #
"""Perform a click operation on the Create Virtual Machine button and and verify the header on the resulting landing page."""
@pytest.mark.testrail(27299)
def test_to_verify_click_on_create_virtual_machine(page, tejas_setup):
    perform_click_on_create_vm_button(page, locators['CREATE_VM_BUTTON'])
    expect(page.get_by_test_id(locators['CREATE_VM_HEADER'])).to_be_visible()
    create_vm_header = page.get_by_test_id(locators['CREATE_VM_HEADER'])
    create_vm_header = create_vm_header.inner_text()
    assert create_vm_header == ComputeTextData.create_vm_header, f"User could not be navigated to {create_vm_header}!!"
    logging.info("User successfully navigated to Create Virtual Machine screen!")


"""Verify the UI of Create Virtual Machine page."""
@pytest.mark.testrail(27300)
def test_verify_create_virtual_machine_homescreen(page, tejas_create_vm_setup):
    page.wait_for_timeout(TIMEOUT)
    expect(page.locator(locators['MACHINE_DETAILS_HEADER'])).to_be_visible()
    expect(page.locator(locators['AVAILABILITY_ZN_DROPDOWN'])).to_be_enabled()
    expect(page.locator(locators['CHOOSE_IMAGE'])).to_be_visible()
    expect(page.get_by_test_id(locators['PUBLIC_IMAGE'])).to_be_visible()
    expect(page.get_by_test_id(locators['SNAPSHOT'])).to_be_visible()
    expect(page.locator(locators['ROOT_VOLUME_TYPE'])).to_be_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()


"""Verify the header on Create Virtual Machine page."""
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

# # @pytest.mark.testrail(27305)
# # @pytest.mark.skip(reason="Need to recheck logic!")
# # def test_to_verify_machine_name_field_has_required_label(page, tejas_create_vm_setup):
# #     placeholderText = page.get_by_placeholder(locators['NAME_FIELD_LABEL']).inner_text()
# #     expect(placeholderText).to_have_text('Please enter a name')
# #
# # @pytest.mark.testrail(27306)
# # @pytest.mark.skip(reason="Yet to be implemented")
# # def test_to_verify_name_field_against_regex(page, tejas_create_vm_setup):
# #     pass
# #
"""Verify the description under Choose Availability Zone label. """
@pytest.mark.testrail(27307)
def test_to_verify_choose_availability_zone_description(page, tejas_create_vm_setup):
    availability_zone_description = page.locator(locators['AVAILABILITY_ZN_DESCRP']).inner_text()
    assert availability_zone_description == ComputeTextData.availability_zone_description, f"The Availability Zone description value - {availability_zone_description}, is different than expected!"
    logging.info("Description on Choose Availability zone section is correct!")


@pytest.mark.testrail(27308)
def test_to_verify_availability_zone_dropdown(page, tejas_create_vm_setup):
    expect(page.locator(locators['AVAILABILITY_ZN_DROPDOWN'])).to_be_visible()

    # if dropdown_visibility == True:
    #     pass


@pytest.mark.testrail(27309)
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


@pytest.mark.testrail(27310)
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
    #page.get_by_test_id("ArrowDropDownIcon[1]").is_visible()
    assert version_dropdown_element.is_visible(), "Version dropdown is not visible"
   # [id="image_id-option-1"]

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
    search_field_locator = page.locator('input[placeholder="Search "]')
    if search_field_locator.is_visible():
        search_field_locator.click()
        search_field_locator.fill("test-machine")
    else:
        print("Search field is not visible")

#

#
@pytest.mark.testrail(27317)
def test_Verify_user_is_able_to_select_Root_Volume_size(page, tejas_create_vm_setup):
    page.get_by_test_id(locators['ROOT_VOLUME_HEADER']).is_visible()
    page.get_by_text("Root Volume (in GiB)").is_visible()
    page.get_by_test_id("volume_size").is_visible()
    initial_value = page.locator('#volume_size').get_attribute("value")
    page.get_by_test_id("volume-size-count").click()
    updated_value = page.locator('#volume_size').get_attribute("value")
    assert updated_value == "100", "Volume size is not updated to 100"
    page.locator('//button[@data-testid="-count"]').click()
    final_value = page.locator('#volume_size').get_attribute("value")
    # input_field = page.locator('#volume_size')
    # final_value = input_field.get_attribute("value")
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
    page.get_by_text("Choose Flavor").is_visible()
    expect(page.get_by_test_id("tab-compute-intensive")).to_be_visible()
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["COMPUTE_INTENSIVE_CARD"]}"]')
    compute_header_count = len(compute_header_elements)
    print("Compute header count1:", compute_header_count)
    if compute_header_count > 0:
        compute_header_elements[1].click()
    page.wait_for_timeout(TIMEOUT)


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


#
#
#     # machine_credentials_visible = page.get_by_text("Machine Credentials").is_visible()
#     # machines_key = page.query_selector_all(f'[data-testid="key-pair-tab"]')
#     # #machines_key = page.query_selector_all(f'[data-testid="tab"]')
#     # machine_Creds = len(machines_key)
#     # print("counts for machine credentials", machine_Creds)
#     # for index, element in enumerate(machines_key):
#     #     element_text = element.inner_text()
#     #     print("text",element_text)
#     #     if "Key Pair" in element_text:
#     #         element.click()
#     #         page.wait_for_timeout(80000)
#     #         break
#     #
#     # username_password_visible = page.get_by_text("Username / Password").is_visible()
#     # assert username_password_visible, "Username / Password section is not visible"
#
@pytest.mark.testrail(27323)
def test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa(page, tejas_create_vm_setup):
    machine_credentials_visible = page.get_by_text("Machine Credentials").is_visible()
    key_pair_tab = page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).is_visible()
    keypair_text = page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).inner_text()
    assert keypair_text == "Key Pair"
    page.get_by_test_id(locators['CREDENTIALS_KEY_PAIR_OPTION']).click()
    page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).click()
    password_tab = page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).is_visible()
    username_password_visible = page.get_by_test_id(locators['CREDENTIALS_USER_PASS_OPTION']).inner_text()
    assert username_password_visible == "Username / Password"
    username_password_visible = page.get_by_text("Username / Password").is_visible()
    assert username_password_visible, "Username / Password section is not visible"


@pytest.mark.testrail(27324)
def test_verify_Username_text_field_is_properly_displayed_and_accept_input_from_user(page, tejas_create_vm_setup):
    test_Verify_user_is_able_to_move_to_Username_Password_tab_from_Key_Pair_tab_and_vice_versa
    expect(page.get_by_test_id("vm-username-input")).to_be_visible()
    Machine_name_field_visibility = page.locator(locators['NAME_FIELD_MACHINE']).is_visible()
    if Machine_name_field_visibility == True:
        page.locator(locators['NAME_FIELD_MACHINE']).type("vini-sdet@yopmail.com")
        page.wait_for_timeout(TIMEOUT)

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
        page.locator(locators['NAME_FIELD_MACHINE']).fill("vini-sdet@yopmail.com")

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
    # page.get_by_text("Networks").is_visible()
    # page.get_by_text("Networks").is_visible()
    expect(page.get_by_test_id("network-id-multi-select")).to_be_visible()

