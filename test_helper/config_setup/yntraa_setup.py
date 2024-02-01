
from test_helper.library.required_library import *

""" Defining all the unique locators for web elements across the entire Compute Resource module."""

current_directory = os.path.dirname(os.path.abspath(__file__))
test_helper_directory = os.path.abspath(os.path.join(current_directory,'..', '..', 'test_helper'))
testdata_directory = os.path.join(test_helper_directory, 'testdata')
locator_yaml_file = os.path.join(testdata_directory, 'locators.yaml')

with open(locator_yaml_file, 'r') as file:
    locators = yaml.safe_load(file)


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

@staticmethod
def verify_to_login_byusing_rolebased_credentials(page):
    page.get_by_role("button", name="Login").click()
    username_input = page.query_selector("input#username")
    username_input.fill("pankaj.tech@yopmail.com")
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
    page.wait_for_timeout(8000)
    page.get_by_text("Logout").click()
    page.wait_for_timeout(8000)
    page.wait_for_timeout(8000)
