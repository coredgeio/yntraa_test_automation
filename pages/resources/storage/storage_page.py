from test_helper.config_setup.yntraa_setup import *

@pytest.fixture(scope='module')
def storage_setup(page):
    perform_click_on_storage_resource(page, locators['STORAGE_TAB'])
    page.wait_for_timeout(TIMEOUT)

def perform_click_on_storage_resource(page, selector):
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(selector).click()

