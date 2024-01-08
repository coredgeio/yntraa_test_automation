# import pytest
# from playwright.sync_api import sync_playwright
# from test_helper.config_setup.login import login_setup
#
# @pytest.fixture(scope="module")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         context.close()
#
# @pytest.fixture(scope="module", autouse=True)
# def login_setup_fixture(browser):
#     login = login_setup(page=browser, url="https://console-revamp-sbx.yntraa.com", username="priti.ltd@yopmail.com", password="India@143")
#     login.perform_login()
#     return login


import pytest
from playwright.sync_api import sync_playwright, expect, Error
from test_helper.yantra_element_locators.compute_element import ComputePageLocators, TejasComputeLocators
from test_helper.config_setup.login import login_setup_yntraa
from modules.resources.compute.compute_page import perform_click_on_compute_resource
from modules.resources.compute.tejas_page import perform_click_on_tejas_tab, perform_click_on_create_vm_button


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page

@pytest.fixture(scope="module", autouse=True)
def login_setup(browser):
    login = login_setup_yntraa(page=browser, url="https://console-revamp-sbx.yntraa.com", username="priti.ltd@yopmail.com", password="India@143")
    login.perform_login()

@pytest.fixture(scope='module')
def compute_setup(browser):
    page = browser
    perform_click_on_compute_resource(page, ComputePageLocators.COMPUTE_TAB)
    page.wait_for_timeout(2000)


@pytest.fixture(scope='module')
def tejas_setup(browser, compute_setup):
    page = browser
    perform_click_on_tejas_tab(page, TejasComputeLocators.TEJAS_COMPUTE_TAB)
    page.wait_for_timeout(2000)

@pytest.fixture(scope="module", autouse=True)
def page(browser):
    page_value = browser
    return page_value
@pytest.fixture(scope='module')
def tejas_create_vm_setup(browser, tejas_setup):
    page = browser
    # page.locator(TejasComputeLocators.CREATE_VM_BUTTON).click(timeout=50000)
    # page.wait_for_timeout(2000)
    # create_vm_button = page.locator(TejasComputeLocators.CREATE_VM_BUTTON)
    max_retries = 5
    for _ in range(max_retries):
        try:
            perform_click_on_create_vm_button(page, TejasComputeLocators.CREATE_VM_BUTTON)
            break  # Exit the loop if click is successful
        except Exception as e:
            print(f"Click failed: {e}")
            page.wait_for_timeout(1000)

