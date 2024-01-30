import pytest
from playwright.sync_api import sync_playwright, expect, Error

""" Login Method. """
class login_setup_yntraa:
    def __init__(self, page, url, username, password):
        self.page = page
        self.url = url
        self.username = username
        self.password = password

    def perform_login(self):
        self.page.goto(self.url, timeout = 10000)
        self.page.get_by_role("button", name="Login").click()
        username_input = self.page.query_selector("input#username")
        username_input.fill(self.username)
        password_input = self.page.query_selector("input#password")
        password_input.fill(self.password)
        login_button = self.page.query_selector("input#kc-login")
        login_button.click()
        self.page.wait_for_load_state("load")
        expect(self.page.get_by_test_id("btn-yntraa")).to_be_visible()
        expect(self.page.get_by_test_id("btn-project")).to_be_visible()

