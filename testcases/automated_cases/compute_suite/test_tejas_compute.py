
# import pytest
# from test_helper.config_setup.login import login_setup
# from test_helper.config_setup.conftest import browser
# from test_helper.config_setup.conftest import login_setup_fixture
# from playwright.sync_api import sync_playwright, expect
# from test_helper.yantra_element_locators.compute_element import ComputePageLocators, TejasComputeLocators
# import time
# import random
# import logging

# class TestExample:
#     @pytest.fixture(scope="module")
#     def browser(self):
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
#             context = browser.new_context()
#             page = context.new_page()
#             yield page
#             context.close()
#
#     @pytest.fixture(scope="module", autouse=True)
#     def login_setup(self, browser):
#         login = login_setup(page = browser,url="https://console-revamp-sbx.yntraa.com", username="priti.ltd@yopmail.com", password="India@143")
#        login.perform_login()
        #return login
# @pytest.fixture(scope='module')
# def setUp(browser):
#     page = browser
#     page.locator(ComputePageLocators.COMPUTE_TAB).click()
#     page.wait_for_timeout(2000)
#
#
# @pytest.mark.testrail(27291)
# def test_something(browser):
#     page = browser
#     act_text = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
#     print("Heading present on the home page:    ", act_text)
#     assert act_text == "Enabling Possibilities. Empowering Ideas.", "User could not be logged in!!"
#     print("User Successfully Logged in!!!!!!")
#    # return page
#
# @pytest.mark.testrail(27292)
# def test_clicking_on_compute(browser):
#     page = browser
#     # page.locator(ComputePageLocators.COMPUTE_TAB).click()
#     # expect(ComputePageLocators.COMPUTE_TAB).to_be_visible()
#     page.locator(ComputePageLocators.COMPUTE_TAB).click()
#     page.wait_for_timeout(120)
#     compute_page_heading = page.locator(ComputePageLocators.COMPUTE_HEADER).text_content()
#     assert compute_page_heading == "Compute", "User could not be navigated to Compute module!!"
#     logging.info("User has successfully navigated to Compute module!")
#
# def test_verify_header_on_compute_home_screen(browser,setUp):
#     page = browser
#     # expect(page.locator(ComputePageLocators.COMPUTE_HEADER)).to_have_text("Compute")
#     compute_header_value = page.locator(ComputePageLocators.COMPUTE_HEADER).inner_text()
#     print("data",compute_header_value)
#     assert compute_header_value=="Compute", f"compute name is not visible in {compute_header_value}"
#     #expect(compute_header_value).to_equal("Compute")
#
# import pytest
# from test_helper.config_setup.login import login_setup
# from test_helper.config_setup.conftest import browser
# from test_helper.config_setup.conftest import login_setup_fixture

import time
import random
import pytest
from conftest import *
from playwright.sync_api import sync_playwright, expect, Error
import logging
from modules.resources.compute.compute_page import perform_click_on_compute_resource
from modules.resources.compute.tejas_page import perform_click_on_tejas_tab, perform_click_on_create_vm_button
from test_helper.yantra_element_locators.compute_element import ComputePageLocators, TejasComputeLocators
class TestComputeValidations:
    @pytest.mark.testrail(27291)
    def test_to_verify_clicking_on_compute_screen(self, page):
        perform_click_on_compute_resource(page, ComputePageLocators.COMPUTE_TAB)
        compute_page_heading = page.locator(ComputePageLocators.COMPUTE_HEADER).text_content()
        assert compute_page_heading == "Compute", "User could not be navigated to Compute module!!"
        logging.info("User has successfully navigated to Compute module!")

    @pytest.mark.testrail(27292)
    def test_verify_UI_of_compute_home_screen(self, page, compute_setup):
        expect(page.locator(ComputePageLocators.COMPUTE_HEADER)).to_be_visible()
        expect(page.locator(ComputePageLocators.COMPUTE_DESCRP)).to_be_visible()
        expect(page.locator(ComputePageLocators.COMPUTE_CREATE_BUTTON)).to_be_visible()
        expect(page.locator(ComputePageLocators.STORAGE_TAB)).to_be_visible()
        expect(page.locator(ComputePageLocators.NETWORKING_TAB)).to_be_visible()
        expect(page.locator(ComputePageLocators.SECURITY_TAB)).to_be_visible()
        expect(page.locator(ComputePageLocators.AUTOMATION_TAB)).to_be_visible()

    @pytest.mark.testrail(27293)
    def test_to_verify_header_on_compute_home_screen(self, page, compute_setup):
        compute_header_value = page.locator(ComputePageLocators.COMPUTE_HEADER).inner_text()
        assert compute_header_value == "Compute", f"The compute header value - {compute_header_value}, is different than expected!"
        logging.info("Header on Compute home screen is correct!")

    @pytest.mark.testrail(27294)
    def test_to_verify_compute_home_screen_description(self, page, compute_setup):
        compute_description_value = page.locator(ComputePageLocators.COMPUTE_DESCRP).inner_text()
        expected_compute_description = "Compute refers to virtual machines that provide cloud-based processing power. Users can deploy and manage these scalable, customizable instances to run applications, websites and other workloads on the cloud."
        assert compute_description_value == expected_compute_description, f"The compute description value - {compute_description_value}, is different than expected!"
        logging.info("Description on Compute home screen is correct!")

    #testrail id C27294
    @pytest.mark.testrail(27295)
    def test_to_verify_clicking_on_tejas_compute(self, page, compute_setup):
        perform_click_on_tejas_tab(page, TejasComputeLocators.TEJAS_COMPUTE_TAB)
        tejas_compute_page_heading = page.locator(TejasComputeLocators.TEJAS_HEADER).text_content()
        assert tejas_compute_page_heading == "Tejas Compute", "User could not be navigated to Tejas Compute section!!"
        logging.info("User successfully navigated to Tejas Compute screen!")

    #testrail id C27296
    @pytest.mark.testrail(27296)
    def test_to_verify_header_on_tejas_compute_screen(self, page, tejas_setup):
        tejas_compute_header = page.locator(TejasComputeLocators.TEJAS_HEADER).inner_text()
        assert tejas_compute_header == "Tejas Compute", f"The Tejas Compute header value - {tejas_compute_header}, is different than expected!"
        logging.info("Header on Tejas Compute screen is successfully correct!")


    #testrail id C27297
    @pytest.mark.testrail(27297)
    def test_to_verify_tejas_compute_screen_description(self, page, tejas_setup):
        tejas_description_value = page.locator(TejasComputeLocators.TEJAS_DESCRP).inner_text()
        expected_tejas_description =  "Virtual Machines are virtualized computing instances that allow users to run applications and services in a cloud environment. They provide scalable, isolated and customizable computing resources, enabling users to deploy and manage their software efficiently."
        assert tejas_description_value == expected_tejas_description, f"The Tejas Compute description value - {tejas_description_value}, is different than expected!"
        logging.info("Description on Tejas Compute home screen is correct!")


    #testrail id C27298
    @pytest.mark.testrail(27298)
    @pytest.mark.skip(reason = "After clicking on Learn More link it was found that the documentation page is broken!")
    def test_verify_learn_more_section_on_tejas_compute_screen(self, page):
        pass
        #documentation page is broken


    #testrail id C27299
    @pytest.mark.testrail(27299)
    def test_to_verify_click_on_create_virtual_machine(self, page, tejas_setup):
        perform_click_on_create_vm_button(page, TejasComputeLocators.CREATE_VM_BUTTON)
        create_vm_header = page.locator(TejasComputeLocators.CREATE_VM_HEADER).text_content()
        assert create_vm_header == "Create Virtual Machine", f"User could not be navigated to {create_vm_header}!!"
        logging.info("User successfully navigated to Create Virtual Machine screen!")

    #testrail id C27299
    @pytest.mark.testrail(27300)
    def test_verify_create_virtual_machine_homescreen(self, page, tejas_create_vm_setup):
        page.wait_for_timeout(200)
        expect(page.locator(TejasComputeLocators.MACHINE_DETAILS_HEADER)).to_be_visible()
        expect(page.locator(TejasComputeLocators.AVAILABILITY_ZN_DROPDOWN)).to_be_enabled()
        expect(page.locator(TejasComputeLocators.CHOOSE_IMAGE)).to_be_visible()
        expect(page.locator(TejasComputeLocators.PUBLIC_IMAGE)).to_be_visible()
        expect(page.locator(TejasComputeLocators.SNAPSHOT)).to_be_visible()
        expect(page.locator(TejasComputeLocators.ROOT_VOLUME_TYPE)).to_be_visible()
        expect(page.locator(TejasComputeLocators.CREATE_VM_SUMMARY)).to_be_visible()
        expect(page.locator(TejasComputeLocators.CANCEL_BUTTON)).to_be_enabled()
