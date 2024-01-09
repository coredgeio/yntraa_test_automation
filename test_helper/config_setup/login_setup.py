import pytest
import logging
from playwright.sync_api import sync_playwright, expect, Error
from test_helper.yantra_element_locators.compute_element import ComputePageLocators, TejasComputeLocators, LoginRequirements
from test_helper.config_setup.yntraa_setup import login_setup_yntraa
from modules.resources.compute.tejas_page import perform_click_on_tejas_tab, perform_click_on_create_vm_button
import time

""" Fixtures for Login operation on Yntraa. """
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page

@pytest.fixture(scope="module", autouse=True)
def page(browser):
    page_value = browser
    return page_value

@pytest.fixture(scope="module", autouse=True)
def login_setup(browser):
    login = login_setup_yntraa(page = browser, url= LoginRequirements.URL, username= LoginRequirements.USERNAME, password= LoginRequirements.PASSWORD)
    login.perform_login()



