import logging
import pytest
from test_helper.library.required_library import *
from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from test_helper.testdata.compute_testdata import ComputeTextData
import asyncio

@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://console-revamp-sbx.yntraa.com",
        "username": "atul159@yopmail.com",
        "password": "India@143"
    }

"""Constant and Global Tejas Compute VM Name!"""
MACHINE_NAME = generate_random_machine_name()

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

"""Verify user is able to redirect to Snapshots screen in Compute section """
@pytest.mark.testrail(27421)
def test_Verify_user_is_able_to_redirect_to_Snapshots_screen_in_Compute_section(page, snapshots_setup):
    change_project_details(page)
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.compute_snapshot_tab in element_text:
            element.click()
    perform_click_on_create_vm_button(page, locators['SNAPSHOTE_CREATE_COMPUTE'])

    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    snapshot_compute_page_heading = page.get_by_test_id(locators['SNAPSHOT_HEADER'])
    snapshot_page_heading = snapshot_compute_page_heading.inner_text()
    assert snapshot_page_heading == ComputeTextData.compute_snapshot_tab, "User could not be navigated to Compute snapshot section!!"
    logging.info("User successfully navigated to Compute snapshot screen!")
    page.wait_for_timeout(10000)

"""Verify header on Compute Snapshot screen """
@pytest.mark.testrail(27422)
def test_verify_header_on_compute_snapshot_screen(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    snapshot_compute_page_heading = page.get_by_test_id(locators['SNAPSHOT_HEADER'])
    snapshot_page_heading = snapshot_compute_page_heading.inner_text()
    assert snapshot_page_heading == ComputeTextData.compute_snapshot_tab, "User could not be navigated to Compute snapshot section!!"
    logging.info("User successfully navigated to Compute snapshot screen!")


"""Verify description under Header part """
@pytest.mark.testrail(27423)
def test_to_verify_snapshot_discription_under_header_part(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_DISCRIPTION'])).to_be_visible()
    snapshot_discription_element = page.get_by_test_id(locators['SNAPSHOT_DISCRIPTION'])
    snapshot_description_value = snapshot_discription_element.inner_text()
    assert snapshot_description_value == ComputeTextData.snapshot_discription, f"The snapshots description value - {snapshot_description_value}, is different than expected!"
    logging.info("Description on snapshot header screen is correct!")

"""Verify Learn More section on Compute Snapshots screen """
@pytest.mark.testrail(27424)
def test_to_verify_learn_more_section_oncompute_snapshots_screen(page, snapshots_setup):
    page.wait_for_timeout(TIMEOUT)
    VM_field_visibility = page.locator(locators['SNAPSHOT_NOT_FOUND']).is_visible()
    if VM_field_visibility == True:
        expect(page.get_by_test_id(locators['LEARN_MORE_VM'])).to_be_visible()
        learn_more_value = page.get_by_test_id(locators['LEARN_MORE_VM'])
        text = learn_more_value.inner_text()
        assert text == "Learn more", "Learn More button is not present when no Snapshots found"
        page.get_by_test_id("btn-learn-more").click()
        expected_url = "https://console-revamp-sbx.yntraa.com/compute/snapshots"
        page.wait_for_timeout(TIMEOUT)
        assert page.url == expected_url, f"Expected URL: {expected_url}, Actual URL: {page.url}"
    else:
        logging.info("Test case failed as snapshots found in the list.")
        VM_List_elements = page.query_selector_all(f'[data-testid="list-card"]')
        VM_list_count = len(VM_List_elements)
        logging.info(VM_list_count)
    to_create_virtual_Compute_machine(page)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.compute_snapshot_tab in element_text:
            element.click()
    #perform_click_on_create_vm_button(page, locators['SNAPSHOTE_CREATE_COMPUTE'])



"""Verify user is able to redirect to Create Compute Snapshot screen by clicking on Create Compute Snapshot button"""
@pytest.mark.testrail(27425)
def test_to_verify_create_compute_Snapshotst(page, create_compute_sanpshots):
    expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
    create_snapshots_header = page.get_by_test_id(locators['CONFIRMATION_TEXT'])
    snapshots_header_text = create_snapshots_header.inner_text()
    assert snapshots_header_text == ComputeTextData.create_snapshot_header_text, f"The Create compute Snapshots header value - {snapshots_header_text}, is different than expected!"
    logging.info("Header on Create compute Snapshots screen is correct!")

"""Verify Create Compute Snapshot screen UI """
@pytest.mark.testrail(27426)
def test_to_verify_create_compute_snapshots_screenUI(page, create_compute_sanpshots):
    create_snapshots_header = page.get_by_test_id(locators['CONFIRMATION_TEXT'])
    snapshots_header_text = create_snapshots_header.inner_text()
    assert snapshots_header_text == ComputeTextData.create_snapshot_header_text, f"The Create compute Snapshots header value - {snapshots_header_text}, is different than expected!"
    expect(page.get_by_test_id(locators['CLOSE_BTN'])).to_be_visible()
    page.get_by_text(locators['SNAPSHOT_NAME_FIELD']).is_visible()
    page.get_by_text(locators['SNAPSHOTS_DROPDOWN']).is_visible()
    expect(page.get_by_test_id(locators['ESTIMATE_COST'])).to_be_visible()
    page.get_by_text("(Max. 5)").is_visible()
    expect(page.get_by_test_id("label-input")).to_be_visible()
    page.get_by_text(locators['ADD_LABEL_BTN']).is_visible()
    expect(page.get_by_test_id(locators['CANCEL_BUTTON'])).to_be_visible()
    expect(page.get_by_test_id(locators['CONFIRM_BUTTON'])).to_be_visible()
    #page.get_by_test_id(locators['CLOSE_BTN']).click()


"""Verify Create button is present and displayed disabled till all required field have values"""
@pytest.mark.testrail(27432)
def test_verify_Create_button_is_present_and_displayed_disabled_till_all_required_field_have_values(page, create_compute_sanpshots):
    expect(page.get_by_test_id(locators['SECTION_HEADER_NAME'])).to_be_visible()
    create_button= page.get_by_test_id("btn-confirm")
    if create_button:
        assert create_button.is_visible(), "Create button is not visible"
        assert not create_button.is_enabled(), "Create button should be disabled initially"
    else:
        pytest.fail("Create button not found on the page")


"""Verify that Create Compute Snapshot header is displayed on top of page """
@pytest.mark.testrail(27427)
def test_to_verify_create_compute_Snapshots_header_displayed_on_top_page(page, create_compute_sanpshots):
    header_element = page.get_by_test_id(locators['SECTION_HEADER_NAME'])
    assert header_element.is_visible(), "Create Compute Snapshot header is not visible on the page"
    expected_header_text = "Create Compute Snapshot"
    actual_header_text = header_element.inner_text()
    assert actual_header_text == expected_header_text, f"Expected header text: '{expected_header_text}', Actual header text: '{actual_header_text}'"
    logging.info("Create Compute Snapshot header is displayed on the top of the page")

@pytest.mark.testrail(27428)
def test_verify_snapshot_name_text_field_for_regex_validation(page, create_compute_sanpshots):
    page.get_by_text(locators['SNAPSHOT_NAME_FIELD']).is_visible()
    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], "qw")
    snapshot_helpertext1 = page.locator(locators['SNAPSHOT_HELPER']).inner_text()
    assert snapshot_helpertext1 == "Name must be at least 3 characters long."

    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], "aq/ka")
    snapshot_helpertext2 = page.locator(locators['SNAPSHOT_HELPER']).inner_text()
    assert snapshot_helpertext2 == "Name can have alphanumeric characters, hyphens, underscores and spaces only."

    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], "qw/")
    snapshot_helpertext3 = page.locator(locators['SNAPSHOT_HELPER']).inner_text()
    assert snapshot_helpertext3 == "Name must start and end with an alphanumeric character."

    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], "asdfghjklasdfghjklaswertyuiohbs")
    snapshot_helpertext4 = page.locator(locators['SNAPSHOT_HELPER']).inner_text()
    assert snapshot_helpertext4 == "Name cannot exceed 30 characters."

    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], "Snap_test")
    #page.wait_for_timeout(10000)

@pytest.mark.testrail(27429)
def test_Select_Virtual_Machine_dropdown_is_displayed_and_user_can_select_option_from_it(page, create_compute_sanpshots):
    page.get_by_text(locators['SNAPSHOTS_DROPDOWN']).is_visible()
    dropdown_element = page.locator(locators['SNAPSHOTS_DROPDOWN'])
    expect(dropdown_element).to_be_visible()
    assert dropdown_element.is_visible(), "Dropdown menu is not displayed"
    dropdown_element.click()
    page.wait_for_timeout(10000)
    vm_elements = page.query_selector_all(f'[data-testid="compute-id-select-option"]')
    compute_header_count = len(vm_elements)
    if compute_header_count > 0:
        first_vm_name = vm_elements[0].inner_text()
        vm_elements[0].click()
    page.wait_for_timeout(TIMEOUT)
    selected_vm_text = page.locator(locators['SNAPSHOTS_DROPDOWN']).inner_text()
    #assert selected_vm_text == first_vm_name, "Selected virtual machine option is not displayed"

@pytest.mark.testrail(27430)
def test_verify_add_lable_tagging_functionlaity(page, create_compute_sanpshots):
    page.get_by_text("(Max. 5)").is_visible()
    expect(page.get_by_test_id("label-input")).to_be_visible()
    page.get_by_test_id('label-input').click()
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


@pytest.mark.testrail(27433)
def test_Verify_Create_button_becomes_enable_once_input_are_there_in_all_requried_fields(page, create_compute_sanpshots):
    clear_and_fill_field(page, locators['SNAPSHOT_NAME_FIELD'], "Snap_test")
    create_compute_snapshot_button = locators['CONFIRM_BUTTON']
    create_button_element = page.get_by_test_id(create_compute_snapshot_button)
    assert create_button_element, f"Unable to find Create button using locator: {create_compute_snapshot_button}"
    create_button = create_button_element.is_enabled() if create_button_element else False
    assert create_button, "Create button should be enabled after filling all required fields"
    page.wait_for_timeout(1000)

@pytest.mark.testrail(27434)
def test_Verify_Create_button_functionality_for_creating_virtual_machine(page, create_compute_sanpshots):
    page.get_by_test_id(locators['CONFIRM_BUTTON']).click()
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print("Toast Text:", toast_text)
    assert toast_text == "Creating compute snapshot."
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    created_snapshot = page.query_selector_all(f'[data-testid="resource-name-link"]')
    snapshot_count = len(created_snapshot)
    if snapshot_count > 0:
        Snapshot_creation_name = created_snapshot[0].inner_text()
        print("displayed the created_snapshot:", Snapshot_creation_name)
    else:
        print("snapshot is not created.")

"""Verify user is able to view the listings of compute snapshots """
@pytest.mark.testrail(27435)
def test_Verify_user_is_able_to_view_the_listings_of_compute_snapshots(page, create_compute_sanpshots):
    #page.get_by_test_id(locators['CLOSE_BTN']).click()
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    created_snapshot = page.query_selector_all(f'[data-testid="resource-name-link"]')
    snapshot_count = len(created_snapshot)
    print(snapshot_count)
    snapshot_ellipse_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    snapshot_list_count = len(snapshot_ellipse_elements)
    if snapshot_list_count > 0:
        snapshot_ellipse_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            print("Text value of ellipsis-item:", text_value)
            items_to_verify = ["Manage Labels", "Delete"]
            assert text_value in items_to_verify, f"Item {text_value} not found in {items_to_verify}"
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Manage Labels":
                item.click()
                break
        page.get_by_test_id(locators['CLOSE_BTN']).click()
    else:
        logging.info("No Ellipsis item found.")

@pytest.mark.testrail(27436)
def test_verify_search_functionality(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(10000)
    created_snapshot = page.query_selector_all(f'[data-testid="resource-name-link"]')
    snapshot_count = len(created_snapshot)
    if snapshot_count > 0:
        Snapshot_creation_name = created_snapshot[0].inner_text()
        print("displayed the created_snapshot:", Snapshot_creation_name)
    else:
        print("snapshot is not created.")
    page.locator(locators['SEARCH_FIELD']).fill(Snapshot_creation_name)
    page.wait_for_timeout(1000)
    found_match = False
    for element in created_snapshot:
        if element.inner_text() == Snapshot_creation_name:
            found_match = True
            break

    assert found_match, f"No match found for {Snapshot_creation_name} in VM names"

@pytest.mark.testrail(27437)
def test_verify_compute_snapshot_configartion_info_for_name(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    created_snapshot = page.query_selector_all(f'[data-testid="resource-name-link"]')
    snapshot_count = len(created_snapshot)
    if snapshot_count > 0:
        Snapshot_creation_name = created_snapshot[0].inner_text()
        print(Snapshot_creation_name)
        logging.info("displayed the created_snapshot name:", Snapshot_creation_name)
    else:
        logging.info("snapshot is not created.")

@pytest.mark.testrail(27438)
def test_verify_compute_snapshot_configartion_info_forName(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    valid_statuses = ["created", "running", "processing", "deleting"]
    assert status_text in valid_statuses, f"Unexpected status: {status_text}"
    assert status_text == "created", "The VM is not in running state"

@pytest.mark.testrail(27440)
def test_verify_compute_snapshot_configartion_info_attached_virtual_machine(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    snapshot_name_element = page.locator(locators['SNAPSHOTS_NAME'])
    assert snapshot_name_element.is_visible(), "Snapshot name element is not visible"
    snapshot_name = snapshot_name_element.inner_text()
    assert snapshot_name, "Snapshot name is empty"

@pytest.mark.testrail(27441)
def test_Verify_Compute_Name_present_on_the_snapshot_listcard(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    created_snapshot = page.query_selector_all(locators['SNAPSHOTS_NAME'])
    snapshot_count = len(created_snapshot)
    if snapshot_count > 0:
        Snapshot_creation_name = created_snapshot[0].inner_text()
        print(Snapshot_creation_name)
        created_snapshot[0].click()
        configuration_name = page.get_by_test_id(locators['CONFIGURATION_HEADING_NAME']).inner_text()
        assert configuration_name == Snapshot_creation_name, f"Configuration name '{configuration_name}' does not match first VM name '{Snapshot_creation_name}'"
        logging.info("displayed the created_snapshot name:", Snapshot_creation_name)
    else:
        logging.info("snapshot is not created.")
@pytest.mark.testrail(27442)
def test_Verify_Compute_Snapshots_configuration_info_for_Labels(page, snapshots_setup):
    page.get_by_test_id(locators['BACK_BTN']).click()
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.compute_snapshot_tab in element_text:
            element.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    label_element = page.query_selector_all(f'[data-testid="{locators["LABEL_TAG"]}"]')
    label_elemnt_count = len(label_element)
    if label_elemnt_count > 0:
        label_name = label_element[0].inner_text()
        logging.info("labels_details",label_name)

@pytest.mark.testrail(27642)
def test_Verify_Manage_Labels_functionality(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    snapshot_ellipse_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    snapshot_list_count = len(snapshot_ellipse_elements)
    if snapshot_list_count > 0:
        snapshot_ellipse_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            print("Text value of ellipsis-item:", text_value)
            items_to_verify = ["Manage Labels", "Delete"]
            assert text_value in items_to_verify, f"Item {text_value} not found in {items_to_verify}"
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Manage Labels":
                item.click()
                expect(page.get_by_test_id(locators['CONFIRMATION_TEXT'])).to_be_visible()
                page.get_by_test_id(locators['CLOSE_BTN']).click()
                break

@pytest.mark.testrail(27443)
def test_delete_snapshot_functionality(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    snapshot_ellipse_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    snapshot_list_count = len(snapshot_ellipse_elements)
    if snapshot_list_count > 0:
        snapshot_ellipse_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            print("Text value of ellipsis-item:", text_value)
            items_to_verify = ["Manage Labels", "Delete"]
            assert text_value in items_to_verify, f"Item {text_value} not found in {items_to_verify}"
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Delete":
                item.click()
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
    page.get_by_test_id(locators['CANCEL_BUTTON']).click()
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()


@pytest.mark.testrail(27447)
def test_verify_enable_Delete_Permanently_button_functionality_on_Delete_popup_window(page, snapshots_setup):
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    snapshot_ellipse_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    snapshot_list_count = len(snapshot_ellipse_elements)
    if snapshot_list_count > 0:
        snapshot_ellipse_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            print("Text value of ellipsis-item:", text_value)
            items_to_verify = ["Manage Labels", "Delete"]
            assert text_value in items_to_verify, f"Item {text_value} not found in {items_to_verify}"
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == "Delete":
                item.click()
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
    toast_text = page.locator(locators['TOAST_ALERT']).inner_text()
    print("Toast Text:", toast_text)
    page.wait_for_timeout(1000)
    #assert toast_text == "Deleting compute snapshot."
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    status_element = page.query_selector(f'[data-testid="{locators["VM_STATUS"]}"]')
    assert status_element, "Status element not found."
    status_text = status_element.inner_text().lower()
    valid_statuses = ["created", "running", "processing", "deleting"]
    assert status_text in valid_statuses, f"Unexpected status: {status_text}"
    assert status_text == "deleting", "The VM is not in running state"

@pytest.mark.testrail(27448)
def test_verify_Snapshots_for_deleted_virtual_machines(page, snapshots_setup):
    to_delete_the_created_virtual_machine(page)
    compute_header_elements = page.query_selector_all(f'[data-testid="{locators["TEJAS_COMPUTE_TAB"]}"]')
    for index, element in enumerate(compute_header_elements, start=1):
        element_text = element.inner_text()
        if ComputeTextData.compute_snapshot_tab in element_text:
            element.click()
    expect(page.get_by_test_id(locators['SNAPSHOT_HEADER'])).to_be_visible()
    page.wait_for_timeout(1000)
    created_snapshots = page.query_selector_all(locators['SNAPSHOTS_NAME'])
    snapshot_count = len(created_snapshots)
    if snapshot_count > 0:
        snapshot_name = created_snapshots[0].inner_text()
        print(snapshot_name)
        logging.info("Displayed the created snapshot name:", snapshot_name)
        vm_link = created_snapshots[0].get_attribute('href')
        assert vm_link is None, "Virtual machine name is clickable, which is unexpected"
    else:
        logging.info("Snapshot is not created.")

