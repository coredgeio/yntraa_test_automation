import random
import string
import pytest
from test_helper.yantra_element_locators.compute_element import ComputePageLocators

""" Common fixtures and methods for Compute section of the application. """
@pytest.fixture(scope='module')
def compute_setup(page):
    perform_click_on_compute_resource(page, ComputePageLocators.COMPUTE_TAB)
    page.wait_for_timeout(2000)

def perform_click_on_compute_resource(page, selector, timeout=1000):
    page.wait_for_timeout(timeout)
    page.wait_for_selector(selector).click()

def generate_random_machine_name():
    allowed_characters = string.ascii_letters + string.digits + "-_ "
    min_length = 3
    max_length = 30
    name_length = random.randint(min_length, max_length)
    random_name = ''.join(random.choice(allowed_characters) for _ in range(name_length))
    if not random_name[0].isalnum():
        random_name = random.choice(string.ascii_letters + string.digits) + random_name[1:]
    if not random_name[-1].isalnum():
        random_name = random_name[:-1] + random.choice(string.ascii_letters + string.digits)

    return random_name


# random_machine_name = generate_random_machine_name()
# print(random_machine_name)
