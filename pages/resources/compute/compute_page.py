
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
    random_char = random.choice(string.ascii_lowercase)
    random_number = random.randint(1, 99)
    random_name = f"testmachine{random_number}"

    # allowed_characters = string.ascii_letters + string.digits + "-_ "
    # min_length = 3
    # max_length = 30
    # name_length = random.randint(min_length, max_length)
    # random_name = ''.join(random.choice(allowed_characters) for _ in range(name_length))
    # if not random_name[0].isalnum():
    #     random_name = random.choice(string.ascii_letters + string.digits) + random_name[1:]
    # if not random_name[-1].isalnum():
    #     random_name = random_name[:-1] + random.choice(string.ascii_letters + string.digits)
    return random_name
