from test_helper.library.required_library import *
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

""" Defining all the unique locators for web elements across the entire Compute Resource module."""

current_directory = os.path.dirname(os.path.abspath(__file__))
test_helper_directory = os.path.abspath(os.path.join(current_directory,'..', '..', 'test_helper'))
testdata_directory = os.path.join(test_helper_directory, 'testdata')
locator_yaml_file = os.path.join(testdata_directory, 'locators.yaml')

with open(locator_yaml_file, 'r') as file:
    locators = yaml.safe_load(file)

"""Constant and Global Timeout!"""
TIMEOUT = 1000

""" Login Method. """
class login_setup_yntraa:
    def __init__(self, page, url, username, password):
        self.page = page
        self.url = url
        self.username = username
        self.password = password

    # def perform_login(self):
    #     self.page.goto(self.url, timeout=80000)
    #     self.page.get_by_role("button", name="Login").click()
    #     self.page.wait_for_timeout(10000)
    #     username_input = self.page.query_selector("input#username")
    #     self.page.wait_for_timeout(TIMEOUT)
    #     username_input.fill(self.username)
    #     password_input = self.page.query_selector("input#password")
    #     password_input.fill(self.password)
    #     login_button = self.page.query_selector("input#kc-login")
    #     login_button.click()
    #     self.page.wait_for_load_state("load")
    #     self.page.wait_for_timeout(20000)
    #     expect(self.page.get_by_test_id("btn-yntraa")).to_be_visible()
    #     expect(self.page.get_by_test_id("btn-project")).to_be_visible()

    def perform_login(self):
        try:
            self.page.goto(self.url, timeout=10000)
            login_button = self.page.get_by_role("button", name="Login")
            if login_button.is_visible():
                login_button.click()
            else:
                username_input = self.page.query_selector("input#username")
                self.page.wait_for_timeout(TIMEOUT)
                username_input.fill(self.username)
                password_input = self.page.query_selector("input#password")
                password_input.fill(self.password)
                login_button = self.page.query_selector("input#kc-login")
                login_button.click()
                self.page.wait_for_load_state("load")
                expect(self.page.get_by_test_id("btn-yntraa")).to_be_visible()
                expect(self.page.get_by_test_id("btn-project")).to_be_visible()
        except TimeoutError:
            print("Timeout error occurred during login process.")
        except Exception as e:
            print(f"An error occurred during login process: {e}")


