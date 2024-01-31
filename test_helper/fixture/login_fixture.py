from test_helper.library.required_library import *
from test_helper.config_setup.yntraa_setup import *
from pages.resources.compute.tejas_page import *

""" Fixtures for Login operation on Yntraa. """

# @pytest.fixture(scope="module")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page

@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if isinstance(browser_name, list):
        browser_name = browser_name[0]
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
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
def login_setup(browser, user_credentials):
    login = login_setup_yntraa(page=browser, url=user_credentials["url"], username=user_credentials["username"], password=user_credentials["password"])
    login.perform_login()

