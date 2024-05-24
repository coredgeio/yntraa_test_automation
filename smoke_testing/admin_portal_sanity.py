import logging
import pytest
from test_helper.library.required_library import *
#from test_helper.fixture.login_fixture import *
from pages.resources.compute.tejas_page import *
from pages.resources.networking.ip_address_page import *
from test_helper.testdata.compute_testdata import ComputeTextData
from test_helper.testdata.sanity_testdata import SanityTextData
from pages.sanity_service_provider import *

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium", help="Specify the browser to use for testing (chromium, firefox, webkit)")

@pytest.fixture(scope="module", autouse=True)
def page(browser):
    page_value = browser
    return page_value

@pytest.fixture(scope="module", autouse=True)
def admin_login_setup(browser, user_credentials):
    login = admin_login_setup_yntraa(page=browser, url=user_credentials["url"], username=user_credentials["username"], password=user_credentials["password"])
    login.admin_perform_login()
    return browser

@pytest.fixture(scope="module")
def user_credentials():
    return {
        "url": "https://admin-revamp-sbx.yntraa.com/organisations",
        "username": "test-qa-user01@yopmail.com",
        "password": "India@143"
    }



"""Verify the header on CCP home page - "Enabling Possibilities. Empowering Ideas." """
@pytest.mark.testrail(67117)
def test_Verify_the_header_on_Yntraa_home_page(page):
    page.wait_for_timeout(10000)

@pytest.mark.testrail(67118)
def test_verify_admin_portal_url(page):
    admin_url = "https://admin-revamp-sbx.yntraa.com/"
    page.wait_for_timeout(10000)
    page.goto(admin_url)
    current_url = page.url
    assert current_url == admin_url, f"Expected URL to be {admin_url} but got {current_url}"

@pytest.mark.testrail(67119)
def test_verify_organisations_page(page):
    organisations_header = page.get_by_role("heading", name="Organisations")
    expect(organisations_header).to_be_visible()
    expect(page.get_by_test_id(locators['ORGANISATION_SIDEBAR'])).to_be_visible()
    header_text = organisations_header.inner_text()
    assert header_text == "Organisations", f"Expected header text to be 'Organisations', but got '{header_text}'"

@pytest.mark.testrail(67120)
def test_Verify_the_logo_present_on_Admin_portal(page):
    organisations_header = page.get_by_role("heading", name="Organisations")
    expect(organisations_header).to_be_visible()
    yntraa_logo = page.locator("img")
    expect(yntraa_logo).to_be_visible()
    logging.info("yntraa_admin_portal_logo is visible")

@pytest.mark.testrail(67121)
def test_verify_the_Welcome_username_label(page):
    expect(page.get_by_text("Welcome")).to_be_visible()
    welcome_element = page.locator("text=Welcome")
    expect(welcome_element).to_be_visible()
    welcome_text = welcome_element.inner_text()
    welcome_text_stripped = welcome_text.strip().split(',')[0]
    print(welcome_text_stripped)
    assert welcome_text_stripped == "Welcome", f"Expected text to be 'Welcome', but got '{welcome_text}'"

"Click on username initials - Verify the user profile displayed the options - *Username *Change Password *Logout "
@pytest.mark.testrail(67122)##Validation pending due to id
def test_verify_user_profile_options(page):
    expect(page.get_by_test_id(locators['PROFILE_AVTAR_BTN'])).to_be_visible()
    page.get_by_test_id(locators['PROFILE_AVTAR_BTN']).click()
    expect(page.get_by_test_id(locators['CHANGE_PASSWORD'])).to_be_visible()
    expect(page.get_by_test_id(locators['LOGOUT_BTN'])).to_be_visible()
    expect(page.get_by_text("Change Password")).to_be_visible()
    expect(page.get_by_text("Logout")).to_be_visible()
    expect(page.get_by_text("test-qa-user01@yopmail.com")).to_be_visible()
    expect(page.get_by_text("Tim Dunbur").nth(1)).to_be_visible()


@pytest.mark.testrail(67123)###check with team
def test_User_profile_verify_user_is_redirecting_to_Change_Password_page_upon_clicking_Change_Password(page):
    # expect(page.get_by_test_id(locators['PROFILE_AVTAR_BTN'])).to_be_visible()
    # page.get_by_test_id(locators['PROFILE_AVTAR_BTN']).click()
    # expect(page.get_by_test_id(locators['CHANGE_PASSWORD'])).to_be_visible()
    # expect(page.get_by_text("Change Password")).to_be_visible()
    page.get_by_test_id(locators['CHANGE_PASSWORD']).click()
    page.wait_for_timeout(10000)
    login_screen = page.get_by_role("heading", name="Welcome to One Yotta")
    expect(login_screen).to_be_visible()
    welcome_screen = login_screen.inner_text()
    assert welcome_screen == "Welcome to One Yotta"
    expect(page.locator("#errorMessage")).to_be_visible()
    page.get_by_placeholder("Email").fill("test-qa-user01@yopmail.com")
    page.get_by_placeholder("Password").fill("India@143")
    login_button = page.query_selector("input#kc-login")
    login_button.click()
    page.wait_for_load_state("load")
    organisations_header = page.get_by_role("heading", name="Organisations")
    expect(organisations_header).to_be_visible()

"User profile - Verify upon clicking on logout button, logs out the user from admin portal"
@pytest.mark.testrail(67124)
def test_User_profile_verify_upon_clicking_on_logout_button_logs_out_the_user_from_admin_portal(page):
    expect(page.get_by_test_id(locators['PROFILE_AVTAR_BTN'])).to_be_visible()
    page.get_by_test_id(locators['PROFILE_AVTAR_BTN']).click()
    expect(page.get_by_test_id(locators['LOGOUT_BTN'])).to_be_visible()
    expect(page.get_by_text("Change Password")).to_be_visible()
    page.get_by_test_id(locators['LOGOUT_BTN']).click()
    page.wait_for_timeout(10000)
    login_screen = page.get_by_role("heading", name="Welcome to One Yotta")
    expect(login_screen).to_be_visible()
    welcome_screen = login_screen.inner_text()
    assert welcome_screen == "Welcome to One Yotta"
    page.get_by_placeholder("Email").fill("test-qa-user01@yopmail.com")
    page.get_by_placeholder("Password").fill("India@143")
    login_button = page.query_selector("input#kc-login")
    login_button.click()
    page.wait_for_load_state("load")
    organisations_header = page.get_by_role("heading", name="Organisations")
    expect(organisations_header).to_be_visible()

# @pytest.mark.testrail(67125)
# def test_Search_menu_Verify_user_is_able_to_search_the_menu_by_search_menu_option(page):
#     expect(page.get_by_test_id(locators['ADMIN_SEARCH_BAR'])).to_be_visible()
#     page.get_by_test_id(locators['ADMIN_SEARCH_BAR']).click()
#     expect(page.get_by_text("Select columns to apply search")).to_be_visible()
#     expect(page.get_by_role("button", name="Organisation Code")).to_be_visible()
#     page.get_by_role("button", name="Organisation Code").click()
#     page.get_by_test_id(locators['ADMIN_SEARCH_INPUT']).click()
#     page.get_by_placeholder("Search (min 3 chars)").fill("001")
#     expect(page.get_by_test_id(locators['ADMIN_SEARCH_BTN'])).to_be_visible()
#     page.get_by_test_id(locators['ADMIN_SEARCH_BTN']).click()
#     page.wait_for_timeout(10000)
#     expect(page.get_by_text("Showing 1 to 20 of 41 records")).to_be_visible()
#     page.get_by_test_id("btn-clear-search").click()
#     page.wait_for_timeout(10000)

@pytest.mark.testrail(67125)
def test_Search_menu_Verify_user_is_able_to_search_the_menu_by_search_menu_option(page):
    search_menu = page.locator(locators['ADMIN_SEARCH_MENU'])
    expect(search_menu).to_be_visible()
    input_box_text = search_menu.inner_text()
    assert input_box_text == "", "search menu Input box text is not empty"
    page.wait_for_timeout(TIMEOUT)
    clear_and_fill_field(page, locators['ADMIN_SEARCH_MENU'], "Compute")
    expect(page.get_by_role("button", name="Compute", exact=True)).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['ADMIN_CLEAR_SEARCH']).click()
    page.screenshot(path="screenshot.png", full_page=True)
    page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(67126)
def test_verify_the_tab_under_Organisation(page):
    expect(page.get_by_test_id(locators['ORGANISATION_SIDEBAR'])).to_be_visible()
    page.get_by_test_id(locators['ORGANISATION_SIDEBAR']).click()
    organisations_header = page.get_by_role("button", name="Organisations")
    expect(organisations_header).to_be_visible()
    header_text = organisations_header.inner_text()
    assert header_text == "Organisations", f"Expected header text to be 'Organisations', but got '{header_text}'"
    project_tab = page.get_by_role("button", name="Projects")
    expect(project_tab).to_be_visible()
    project_header = project_tab.inner_text()
    assert project_header == "Projects", f"Expected header text to be 'Projects', but got '{project_header}'"
    page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(67127)
def test_verify_clicking_on_Organisations_redirects_to_Organisations_page(page):
    organisation_sidebar = page.get_by_test_id(locators['ORGANISATION_SIDEBAR'])
    expect(organisation_sidebar).to_be_visible()
    organisation_sidebar.click()
    organisations_button = page.get_by_role("button", name="Organisations")
    expect(organisations_button).to_be_visible()
    organisations_button.click()
    organisations_header = page.get_by_role("heading", name="Organisations")
    expect(organisations_header).to_be_visible()
    page.wait_for_timeout(TIMEOUT)

@pytest.mark.testrail(67128)
def test_Verify_the_UI_of_Organization(page):
    page.wait_for_timeout(8000)
    organisations_header = page.get_by_role("heading", name="Organisations")
    expect(organisations_header).to_be_visible()
    header_text = organisations_header.inner_text()
    assert header_text == "Organisations", f"Expected header text to be 'Organisations', but got '{header_text}'"
    Page_navigation= page.locator(locators['NAV_BAR'])
    expect(Page_navigation).to_be_visible()
    expected_texts= SanityTextData.organisation_tab
    visibility_status = {}
    for text in expected_texts:
        elements = page.query_selector_all(f'[data-testid="{locators["ADMIN_BTN_SORT"]}"]')
        if elements:
            visibility_status[text] = True
        else:
            visibility_status[text] = False
    all_visible = all(visibility_status.values())
    for text, visible in visibility_status.items():
        print(f"{text} is {'visible' if visible else 'not visible'}")
    logging.info("All texts are visible:", all_visible)
    expect(page.get_by_test_id(locators['ADMIN_SEARCH_BAR'])).to_be_visible()

    expect(page.get_by_text("Records per page:")).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    page.screenshot(path="screenshot.png", full_page=True)

@pytest.mark.testrail(67129)#need to check
def test_Verify_the_listed_records_on_Organization_page_with_respect_to_columns(page):
    organisations_header = page.get_by_role("heading", name="Organisations")
    expect(organisations_header).to_be_visible()


def click_checkbox_and_apply(page, checkbox_locator, apply_button_locator):
    checkbox = page.get_by_test_id(checkbox_locator)
    if not checkbox.is_checked():
        checkbox.click()
    apply_button = page.locator(apply_button_locator)
    apply_button.click()

"Organisation - Verify view column, apply filter export data functionality - user should be able to view selected columns, apply filter and export data "
@pytest.mark.testrail(67130)
def test_organisation_functionality_Verify_view_column_apply_filter_export_data_functionality(page):
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()

    page.get_by_test_id(locators['ADMIN_FILTER_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['VIEW_COLUMNS_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['EXPORT_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_EXPORT_BTN'])




@pytest.mark.testrail(67131)
def test_verify(page):
    page.wait_for_timeout(10000)
    item_to_click = "View Details"
    row_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    if row_elements:
        row_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == item_to_click:
                item.click()
                print(f"Clicked on {item_to_click}")
                break
        else:
            logging.info(f"Item '{item_to_click}' not found.")
    expect(page.get_by_role("heading", name="Quota")).to_be_visible()


@pytest.mark.testrail(67132)
def test_verify(page):
    organisations_button = page.get_by_role("button", name="Organisations")
    expect(organisations_button).to_be_visible()
    organisations_button.click()
    page.wait_for_timeout(10000)
    item_to_click = "Project Details"
    row_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    if row_elements:
        row_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == item_to_click:
                item.click()
                print(f"Clicked on {item_to_click}")
                break
        else:
            logging.info(f"Item '{item_to_click}' not found.")
    expect(page.get_by_role("heading", name="Projects")).to_be_visible()


@pytest.mark.testrail(67133)
def test_verify(page):
    organisations_button = page.get_by_role("button", name="Organisations")
    expect(organisations_button).to_be_visible()
    organisations_button.click()
    page.wait_for_timeout(10000)
    item_to_click = "User Details"
    row_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    if row_elements:
        row_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == item_to_click:
                item.click()
                print(f"Clicked on {item_to_click}")
                break
        else:
            logging.info(f"Item '{item_to_click}' not found.")
    expect(page.get_by_role("heading", name="Users")).to_be_visible()

@pytest.mark.testrail(67134)
def test_Verify_clicking_on_projects_redirects_to_projects_page_and_verify_the_UI_of_Projects_page(page):
    page.get_by_test_id(locators['ORGANISATION_SIDEBAR']).click()
    project_tab = page.get_by_role("button", name="Projects")
    expect(project_tab).to_be_visible()
    project_tab.click()
    page.wait_for_timeout(8000)
    organisations_header = page.get_by_role("heading", name="Projects")
    expect(organisations_header).to_be_visible()
    header_text = organisations_header.inner_text()
    assert header_text == "Projects", f"Expected header text to be 'Projects', but got '{header_text}'"
    Page_navigation= page.locator(locators['NAV_BAR'])
    expect(Page_navigation).to_be_visible()
    expected_texts= ["Project Name", "Project Code", "Organisation", "Created By", "Created On"]
    visibility_status = {}
    for text in expected_texts:
        elements = page.query_selector_all(f'[data-testid="{locators["ADMIN_BTN_SORT"]}"]')
        if elements:
            visibility_status[text] = True
        else:
            visibility_status[text] = False
    all_visible = all(visibility_status.values())
    for text, visible in visibility_status.items():
        print(f"{text} is {'visible' if visible else 'not visible'}")
    logging.info("All texts are visible:", all_visible)
    expect(page.get_by_test_id(locators['ADMIN_SEARCH_BAR'])).to_be_visible()

    expect(page.get_by_text("Records per page:")).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    page.screenshot(path="screenshot.png", full_page=True)


#@pytest.mark.testrail(67135)
#Verify the listed records on Project page with respect to columns
"Projects - Verify view column, apply filter export data functionality - user should be able to view selected columns, apply filter and export data "

@pytest.mark.testrail(67136)
def test_organisation_functionality_Verify_view_column_apply_filter_export_data_functionality(page):
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()

    page.get_by_test_id(locators['ADMIN_FILTER_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['VIEW_COLUMNS_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['EXPORT_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_EXPORT_BTN'])


def selction_for_ellipse_and_ellipseview(page, item_to_click):
    row_elements = page.query_selector_all(f'[data-testid="ellipsis"]')
    if row_elements:
        row_elements[0].click()
        page.wait_for_selector(f'[data-testid="ellipsis-item"]')
        ellipsis_items = page.query_selector_all(f'[data-testid="ellipsis-item"]')
        for item in ellipsis_items:
            text_value = item.inner_text()
            if text_value == item_to_click:
                item.click()
                print(f"Clicked on {item_to_click}")
                break
        else:
            logging.info(f"Item '{item_to_click}' not found.")
@pytest.mark.testrail(67137)
def test_verify(page):
    organisations_button = page.get_by_role("button", name="Organisations")
    expect(organisations_button).to_be_visible()
    organisations_button.click()
    page.wait_for_timeout(10000)
    item_to_click = "View Details"
    selction_for_ellipse_and_ellipseview(page, item_to_click)
    expect(page.get_by_role("heading", name="Projects Details")).to_be_visible()

@pytest.mark.testrail(67138)
def test_verify(page):
    organisations_button = page.get_by_role("button", name="Organisations")
    expect(organisations_button).to_be_visible()
    organisations_button.click()
    page.wait_for_timeout(10000)
    item_to_click = "Project Provider Mapping"
    selction_for_ellipse_and_ellipseview(page, item_to_click)
    expect(page.get_by_role("heading", name="Provider Mapping")).to_be_visible()

@pytest.mark.testrail(67139)
def test_verify(page):
    organisations_button = page.get_by_role("button", name="Organisations")
    expect(organisations_button).to_be_visible()
    organisations_button.click()
    page.wait_for_timeout(10000)
    item_to_click = "Project User Mapping"
    selction_for_ellipse_and_ellipseview(page, item_to_click)
    expect(page.get_by_role("heading", name="Users")).to_be_visible()

@pytest.mark.testrail(67140)
def test_verify(page):
    organisations_button = page.get_by_role("button", name="Organisations")
    expect(organisations_button).to_be_visible()
    organisations_button.click()
    page.wait_for_timeout(10000)
    item_to_click = "View Monitoring"
    selction_for_ellipse_and_ellipseview(page, item_to_click)
    with page.expect_popup() as page1_info:
        page.get_by_text("View Monitoring").click()
    page1 = page1_info.value
    expect(page1.get_by_test_id("data-testid Centralised Instance Monitoring breadcrumb")).to_be_visible()

   # expect(page.get_by_role("heading", name="Projects")).to_be_visible()
@pytest.mark.testrail(67141)
def test_Verify_the_tab_under_Compute(page):
    page.wait_for_timeout(1000)
    compute_tab = page.locator(locators['ADMIN_COMPUTE_SIDEBAR'])
    expect(compute_tab).to_be_visible()
    compute_tab.click()
    virtual_machine_tab = page.get_by_role("button", name="Virtual Machines")
    expect(virtual_machine_tab).to_be_visible()
    header_text = virtual_machine_tab.inner_text()
    assert header_text == "Virtual Machines", f"Expected header text to be 'Virtual Machines', but got '{header_text}'"
    page.get_by_test_id(locators['VIRTUAL_MACHINE_TAB']).click()
    expect(page.get_by_role("heading", name="Virtual Machines")).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    compute_snapshot_tab = page.get_by_role("button", name="Compute Snapshots")
    expect(compute_snapshot_tab).to_be_visible()
    snapshot_header = compute_snapshot_tab.inner_text()
    assert snapshot_header == "Compute Snapshots", f"Expected header text to be 'Compute Snapshots', but got '{snapshot_header}'"
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['COMPUTE_SNAPHOT_TAB']).click()
    expect(page.get_by_role("heading", name="Compute Snapshots")).to_be_visible()

@pytest.mark.testrail(67142)
def test_Verify_the_UI_of_Virtual_Machines_page(page):
    compute_tab = page.locator(locators['ADMIN_COMPUTE_SIDEBAR'])
    compute_tab.click()
    page.wait_for_timeout(2000)
    page.get_by_test_id(locators['VIRTUAL_MACHINE_TAB']).click()
    virtual_machine_header = page.get_by_role("heading", name="Virtual Machines")
    expect(virtual_machine_header).to_be_visible()
    header_text = virtual_machine_header.inner_text()
    assert header_text == "Virtual Machines", f"Expected header text to be 'Virtual Machines', but got '{header_text}'"
    Page_navigation= page.locator(locators['NAV_BAR'])
    expect(Page_navigation).to_be_visible()
    expected_texts= SanityTextData.virtual_machine_column
    visibility_status = {}
    for text in expected_texts:
        elements = page.query_selector_all(f'[data-testid="{locators["ADMIN_BTN_SORT"]}"]')
        if elements:
            visibility_status[text] = True
        else:
            visibility_status[text] = False
    all_visible = all(visibility_status.values())
    for text, visible in visibility_status.items():
        print(f"{text} is {'visible' if visible else 'not visible'}")
    logging.info("All texts are visible:", all_visible)
    expect(page.get_by_test_id(locators['ADMIN_SEARCH_BAR'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_text("Records per page:")).to_be_visible()
    page.screenshot(path="screenshot.png", full_page=True)

@pytest.mark.testrail(67144)
def test_Virtual_Machines_Verify_view_column_apply_filter_export_data_functionality_user_should_be_able_to_view_selected_columns_apply_filter_and_export_data(page):
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()

    page.get_by_test_id(locators['ADMIN_FILTER_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['VIEW_COLUMNS_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['EXPORT_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_EXPORT_BTN'])


@pytest.mark.testrail(67154)
def test_Verify_the_UI_of_compute_snapshot_page(page):
    compute_tab = page.locator(locators['ADMIN_COMPUTE_SIDEBAR'])
    compute_tab.click()
    page.wait_for_timeout(2000)
    page.get_by_test_id(locators['COMPUTE_SNAPHOT_TAB']).click()
    compute_snapshot_header = page.get_by_role("heading", name="Compute Snapshots")
    expect(compute_snapshot_header).to_be_visible()
    header_text = compute_snapshot_header.inner_text()
    assert header_text == "Compute Snapshots", f"Expected header text to be 'Compute Snapshots', but got '{header_text}'"
    Page_navigation= page.locator(locators['NAV_BAR'])
    expect(Page_navigation).to_be_visible()
    expected_texts= SanityTextData.compute_snapshot_column
    visibility_status = {}
    for text in expected_texts:
        elements = page.query_selector_all(f'[data-testid="{locators["ADMIN_BTN_SORT"]}"]')
        if elements:
            visibility_status[text] = True
        else:
            visibility_status[text] = False
    all_visible = all(visibility_status.values())
    for text, visible in visibility_status.items():
        print(f"{text} is {'visible' if visible else 'not visible'}")
    logging.info("All texts are visible:", all_visible)
    expect(page.get_by_test_id(locators['ADMIN_SEARCH_BAR'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_text("Records per page:")).to_be_visible()
    page.screenshot(path="screenshot.png", full_page=True)


@pytest.mark.testrail(67155)
def test_compute_snapshots_Verify_view_column_apply_filter_export_data_functionality_user_should_be_able_to_view_selected_columns_apply_filter_and_export_data(page):
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()

    page.get_by_test_id(locators['ADMIN_FILTER_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['VIEW_COLUMNS_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['EXPORT_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_EXPORT_BTN'])


@pytest.mark.testrail(67161)
def test_Verify_the_tab_under_Storage(page):
    page.wait_for_timeout(1000)
    storagee_tab = page.locator(locators['ADMIN_STORAGE_SIDEBAR'])
    expect(storagee_tab).to_be_visible()
    storagee_tab.click()

    blck_storage_tab = page.get_by_role("button", name="Block Storage")
    expect(blck_storage_tab).to_be_visible()
    header_text = blck_storage_tab.inner_text()
    assert header_text == "Block Storage", f"Expected header text to be 'Block Storage', but got '{header_text}'"
    page.get_by_test_id(locators['BLOCK_STORAGE_SIDEBAR']).click()
    expect(page.get_by_role("heading", name="Block Storage")).to_be_visible()

    page.wait_for_timeout(TIMEOUT)
    compute_snapshot_tab = page.get_by_role("button", name="File Storage")
    expect(compute_snapshot_tab).to_be_visible()
    snapshot_header = compute_snapshot_tab.inner_text()
    assert snapshot_header == "File Storage", f"Expected header text to be 'File Storage', but got '{snapshot_header}'"
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['STORAGE_FILE_SIDEBAR']).click()
    expect(page.get_by_role("heading", name="File Storage")).to_be_visible()

    compute_snapshot_tab = page.get_by_role("button", name="Volume Snapshots")
    expect(compute_snapshot_tab).to_be_visible()
    snapshot_header = compute_snapshot_tab.inner_text()
    assert snapshot_header == "Volume Snapshots", f"Expected header text to be 'Volume Snapshots', but got '{snapshot_header}'"
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(locators['STORAGE_VOLUME_SNAPSHOT_SIDEBAR']).click()
    expect(page.get_by_role("heading", name="Volume Snapshots")).to_be_visible()

@pytest.mark.testrail(67162)
def test_Verify_the_UI_of_block_storage_page(page):
    compute_tab = page.locator(locators['ADMIN_STORAGE_SIDEBAR'])
    compute_tab.click()
    page.wait_for_timeout(2000)
    page.get_by_test_id(locators['BLOCK_STORAGE_SIDEBAR']).click()
    block_storage_header = page.get_by_role("heading", name="Block Storage")
    expect(block_storage_header).to_be_visible()
    header_text = block_storage_header.inner_text()
    assert header_text == "Block Storage", f"Expected header text to be 'Block Storage', but got '{header_text}'"
    Page_navigation= page.locator(locators['NAV_BAR'])
    expect(Page_navigation).to_be_visible()
    expected_texts= SanityTextData.block_storage_column
    visibility_status = {}
    for text in expected_texts:
        elements = page.query_selector_all(f'[data-testid="{locators["ADMIN_BTN_SORT"]}"]')
        if elements:
            visibility_status[text] = True
        else:
            visibility_status[text] = False
    all_visible = all(visibility_status.values())
    for text, visible in visibility_status.items():
        print(f"{text} is {'visible' if visible else 'not visible'}")
    logging.info("All texts are visible:", all_visible)
    expect(page.get_by_test_id(locators['ADMIN_SEARCH_BAR'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_text("Records per page:")).to_be_visible()
    page.screenshot(path="screenshot.png", full_page=True)


@pytest.mark.testrail(67164)
def test_block_storage_Verify_view_column_apply_filter_export_data_functionality_user_should_be_able_to_view_selected_columns_apply_filter_and_export_data(page):
    expect(page.get_by_text("Columns:")).to_be_visible()
    expect(page.get_by_test_id(locators['VIEW_COLUMNS_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['ADMIN_FILTER_BTN'])).to_be_visible()
    expect(page.get_by_test_id(locators['EXPORT_BTN'])).to_be_visible()

    page.get_by_test_id(locators['ADMIN_FILTER_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['VIEW_COLUMNS_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_BUTTON'])

    page.get_by_test_id(locators['EXPORT_BTN']).click()
    expect(page.get_by_test_id(locators['SELECT_CHECKBOX_TAB'])).to_be_visible()
    click_checkbox_and_apply(page, locators['SELECT_CHECKBOX_TAB'], locators['APPLY_EXPORT_BTN'])
