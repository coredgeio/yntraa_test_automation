import pytest
from plugins import TestRailPlugin
import logging

def pytest_addoption(parser):
    """ Add custom parameters to cmd line
    """
    logging.info("inside pytest add-option")
    parser.addoption('--ids', action='store', metavar='id1,id2,id3...', help='only run tests with the specified IDs')
    parser.addoption('--publish', action='store_true', default=True,
                     help='If set, create a new test run and publish results')

    parser.addoption('--include_all', action='store_true', default=False,
                     help='Used with --publish. If set, the test run will\
                     contain all test cases.')

    parser.addoption('--tr_name', action='store', metavar='<run name>',
                     help='Used with --publish to configure run name.')

    parser.addoption('--tr_id', action='store', metavar='run_id', help='If set, run tests in the test run and publish')


def pytest_configure(config):
    """ Configure marker
        Register plugin
    """
    logging.info("inside pytest configure")
    config.addinivalue_line('markers',
                            'testrail(id): mark test with the case id')
    if config.getoption('--publish') or config.getoption('--tr_id'):
        config.pluginmanager.register(
            TestRailPlugin(
                config.getoption('--tr_id'),
                config.getoption('--include_all'),
                config.getoption('--tr_name')))


def pytest_runtest_setup(item):
    """ This handle test case skipping when
        plugin is not available
    """
    logging.info("inside pytest runtest setup")
    logging.info('runtest setup called')
    ids = item.config.getoption('--ids')
    if not ids:
        return
    ids = set([int(x) for x in ids.split(',')])

    idmarker = item.get_closest_marker('testrail')
    logging.info("idmarker -> ")
    logging.info(idmarker.args[1])
    logging.info(idmarker)
    if idmarker is None:
        pytest.skip('skip')
    else:
        tid = idmarker.args[0]
        logging.info(tid)

        if tid not in ids:
            pytest.skip('skip')

# import pytest
# import logging
# from playwright.sync_api import sync_playwright, expect, Error
# from test_helper.yantra_element_locators.compute_element import ComputePageLocators, TejasComputeLocators
# from test_helper.config_setup.login import login_setup_yntraa
# from modules.resources.compute.compute_page import perform_click_on_compute_resource
# from modules.resources.compute.tejas_page import perform_click_on_tejas_tab, perform_click_on_create_vm_button
#
#
# @pytest.fixture(scope="module")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#
# @pytest.fixture(scope="module", autouse=True)
# def page(browser):
#     page_value = browser
#     return page_value
#
# @pytest.fixture(scope="module", autouse=True)
# def login_setup(browser):
#     login = login_setup_yntraa(page = browser, url="https://console-revamp-sbx.yntraa.com", username="priti.ltd@yopmail.com", password="India@143")
#     login.perform_login()
#
# @pytest.fixture(scope='module')
# def compute_setup(page):
#     perform_click_on_compute_resource(page, ComputePageLocators.COMPUTE_TAB)
#     page.wait_for_timeout(2000)
#
# @pytest.fixture(scope='module')
# def tejas_setup(page, compute_setup):
#     perform_click_on_tejas_tab(page, TejasComputeLocators.TEJAS_COMPUTE_TAB)
#     page.wait_for_timeout(2000)
#
# @pytest.fixture(scope='module')
# def tejas_create_vm_setup(page, tejas_setup):
#     create_vm_button_locator = page.locator(TejasComputeLocators.CREATE_VM_BUTTON)
#     if create_vm_button_locator.is_visible():
#         perform_click_on_create_vm_button(page, TejasComputeLocators.CREATE_VM_BUTTON)
#     else:
#         create_vm_header = page.locator(TejasComputeLocators.CREATE_VM_HEADER)
#         if create_vm_header.is_visible():
#             logging.info("Header on the next page is visible. Performing next operation.")
#         else:
#             logging.info("Neither 'Create VM' button nor expected header found.")
#
#     #
#     # create_vm_button_visibility = page.locator(TejasComputeLocators.CREATE_VM_BUTTON).is_visible()
#     # max_retries = 3
#     # for _ in range(max_retries):
#     #     try:
#     #             if create_vm_button_visibility == True:
#     #                 perform_click_on_create_vm_button(page, TejasComputeLocators.CREATE_VM_BUTTON)
#     #                 break  # Exit the loop if click is successful
#     #     except Exception as e:
#     #         print(f"Click failed: {e}")
#     #         page.wait_for_timeout(1000)
#     # else:
#     #     logging.info("Button not visible after maximum retries")
#     #
#



