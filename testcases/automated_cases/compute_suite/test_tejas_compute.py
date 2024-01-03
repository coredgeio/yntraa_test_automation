import pytest
from helper.config_setup.login import login_setup
from playwright.sync_api import sync_playwright
import time
import random

class TestExample:
    @pytest.fixture(scope="module")
    def browser(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            yield page
            context.close()

    @pytest.fixture(scope="module", autouse=True)
    def login_setup(self, browser):
        page = browser
        login = login_setup(url="https://console-revamp-sbx.yntraa.com", username="priti.ltd@yopmail.com", password="India@143")
        login.perform_login(page)
        return login

    @staticmethod
    @pytest.mark.testrail(16510)
    def test_something(browser):
        page = browser
        act_text = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
        print("Heading present on the home page:    ", act_text)
        assert act_text == "Enabling Possibilities. Empowering Ideas.", "User could not be logged in!!"
        print("User Successfully Logged in!!!!!!")
        return page
