import pytest
import logging
import time
from playwright.sync_api import sync_playwright, expect, Error
from test_helper.config_setup.yntraa_setup import login_setup_yntraa
from pages.resources.compute.tejas_page import *

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
def login_setup(browser, user_credentials):
    login = login_setup_yntraa(page=browser, url=user_credentials["url"], username=user_credentials["username"], password=user_credentials["password"])
    login.perform_login()

