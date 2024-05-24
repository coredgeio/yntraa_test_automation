
from test_helper.library.required_library import *
from test_helper.config_setup.yntraa_setup import *


""" Common fixtures and methods for Compute section of the application. """
@pytest.fixture(scope='module')
def compute_setup(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
    page.wait_for_timeout(TIMEOUT)

def perform_click_on_compute_resource(page, selector):
    page.wait_for_timeout(TIMEOUT)
    page.get_by_test_id(selector).click()


def generate_random_machine_name():
    current_time = int(time.time())
    random_char = random.choice(string.ascii_lowercase)
    random_number = random.randint(1, 999)
    random_name = f"testmachine_{current_time}_{random_char}{random_number}"
    return random_name
    #testmachine_1715573630_a704
