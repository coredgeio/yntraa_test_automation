import pytest
import logging
from playwright.sync_api import expect
from test_helper.yantra_element_locators.compute_element import ComputePageLocators, TejasComputeLocators

#testrail id C27291
def test_clicking_on_compute(page):
        page.wait_for_timeout(3000)
        page.wait_for_selector(ComputePageLocators.COMPUTE_TAB).click()
        compute_page_heading = page.locator(ComputePageLocators.COMPUTE_HEADER).text_content()
        assert compute_page_heading == "Compute", "User could not be navigated to Compute module!!"
        logging.info("User has successfully navigated to Compute module!")

#testrail id C27292
def test_verify_UI_of_compute_home_screen(page):
        expect(ComputePageLocators.COMPUTE_HEADER).to_be_visible()
        expect(ComputePageLocators.COMPUTE_DESCRP).to_be_visible()
        expect(ComputePageLocators.COMPUTE_CREATE_BUTTON).to_be_visible()
        expect(ComputePageLocators.STORAGE_TAB).to_be_visible()
        expect(ComputePageLocators.NETWORKING_TAB).to_be_visible()
        expect(ComputePageLocators.SECURITY_TAB).to_be_visible()
        expect(ComputePageLocators.AUTOMATION_TAB).to_be_visible()

#testrail id C27293
def test_verify_header_on_compute_home_screen(page):
        expect(ComputePageLocators.COMPUTE_HEADER).to_have_text("Compute")


#testrail id C27294
def test_verify_compute_home_screen_description(page):
        expect(ComputePageLocators.COMPUTE_DESCRP).to_have_text("Compute refers to virtual machines that provide cloud-based processing power. Users can deploy and manage these scalable, customizable instances to run applications, websites and other workloads on the cloud.")

#testrail id C27294
def test_clicking_on_tejas_compute(page):
        page.wait_for_timeout(3000)
        page.wait_for_selector(TejasComputeLocators.TEJAS_COMPUTE_TAB).click()
        tejas_compute_page_heading = page.locator(ComputePageLocators.COMPUTE_HEADER).text_content()
        assert tejas_compute_page_heading == "Tejas Compute", "User could not be navigated to Tejas Compute section!!"
        logging.info("User successfully navigated to Tejas Compute module!")

#testrail id C27296
def test_verify_header_on_tejas_compute_screen(page):
        expect(TejasComputeLocators.TEJAS_HEADER).to_have_text("Tejas Compute")

#testrail id C27297
def test_verify_tejas_compute_screen_description(page):
        expect(TejasComputeLocators.TEJAS_DESCRP).to_have_text("Virtual Machines are virtualized computing instances that allow users to run applications and services in a cloud environment. They provide scalable, isolated and customizable computing resources, enabling users to deploy and manage their software efficiently.")


#testrail id C27298
@pytest.mark.skip
def test_verify_learn_more_section_on_tejas_compute_screen(page):
        pass
        #documentation page is broken


#testrail id C27299
def test_clicking_on_create_virtual_machine(page):
        page.wait_for_timeout(3000)
        page.wait_for_selector(TejasComputeLocators.CREATE_VM_BUTTON).click()
        virtual_machine_heading = page.locator(TejasComputeLocators.CREATE_VM_HEADER).text_content()
        assert virtual_machine_heading == "Create Virtual Machine", "User could not be navigated to Tejas Compute section!!"
        logging.info("User successfully redirected to Create Virtual Machine screen!")
