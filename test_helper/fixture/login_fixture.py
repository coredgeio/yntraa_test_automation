from test_helper.library.required_library import *
from test_helper.config_setup.yntraa_setup import *
from pages.resources.compute.tejas_page import *
from selenium import webdriver
""" Fixtures for Login operation on Yntraa. """

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page


# @pytest.fixture(scope="module")
# def browser(request):
#     browser_name = request.config.getoption("--browser")
#     if isinstance(browser_name, list):
#         browser_name = browser_name[0]
#     with sync_playwright() as p:
#         if browser_name == "chromium":
#             browser = p.chromium.launch(headless=False)
#         elif browser_name == "firefox":
#             browser = p.firefox.launch(headless=False)
#         elif browser_name == "webkit":
#             browser = p.webkit.launch(headless=False)
#         else:
#             raise ValueError(f"Unsupported browser: {browser_name}")
#         context = browser.new_context()
#         page = context.new_page()
#         yield page

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium", help="Specify the browser to use for testing (chromium, firefox, webkit)")

@pytest.fixture(scope="module", autouse=True)
def page(browser):
    page_value = browser
    return page_value

@pytest.fixture(scope="module", autouse=True)
def login_setup(browser, user_credentials):
    login = login_setup_yntraa(page=browser, url=user_credentials["url"], username=user_credentials["username"], password=user_credentials["password"])
    login.perform_login()

# @pytest.fixture(scope="module")
# def admin_login_setup(browser, user_credentials):
#     login = login_setup_yntraa(page=browser, url=user_credentials["url"], username=user_credentials["username"], password=admin_user_credentials["password"])
#     login.admin_login_setup_yntraa()
#     return browser

@staticmethod
def verify_to_login_byusing_rolebased_credentials(page):
    #page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Login").click()
    username_input = page.query_selector("input#username")
    username_input.fill("atul_srsdet@yopmail.com")
    password_input = page.query_selector("input#password")
    password_input.fill("India@143")
    login_button = page.query_selector("input#kc-login")
    login_button.click()
    page.wait_for_load_state("load")
    expect(page.get_by_test_id("btn-yntraa")).to_be_visible()
    expect(page.get_by_test_id("btn-project")).to_be_visible()

@staticmethod
def click_operation(page, selector, timeout=1000):
    page.wait_for_timeout(timeout)
    page.wait_for_selector(selector).click()

@staticmethod
def verify_to_logout_function(page):
    expect(page.locator(locators['LOGOUT'])).to_be_visible()
    click_operation(page, locators['LOGOUT'])
    page.wait_for_timeout(2000)
    expect(page.get_by_text("Logout", exact=True)).to_be_visible()
    page.wait_for_timeout(2000)
    page.get_by_text("Logout").click()
    page.wait_for_timeout(4000)
    verify_to_login_byusing_rolebased_credentials(page)

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
        #print(element_text)
        if ComputeTextData.tejas_compute_tab in element_text:
            element.click()
    page.wait_for_timeout(TIMEOUT)
    expect(page.get_by_test_id(locators['TEJAS_HEADER'])).to_be_visible()
