import random
import string
import pytest
import yaml
import os

""" Defining all the unique locators for web elements across the entire Compute Resource module."""

current_directory = os.path.dirname(os.path.abspath(__file__))
test_helper_directory = os.path.abspath(os.path.join(current_directory, '..','..', '..', 'test_helper'))
testdata_directory = os.path.join(test_helper_directory, 'testdata')
locator_yaml_file = os.path.join(testdata_directory, 'locators.yaml')

with open(locator_yaml_file, 'r') as file:
    locators = yaml.safe_load(file)


""" Common fixtures and methods for Compute section of the application. """
@pytest.fixture(scope='module')
def compute_setup(page):
    perform_click_on_compute_resource(page, locators['COMPUTE_TAB'])
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
