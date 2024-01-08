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
        logging.info("Header on Tejas Compute screen is correct!")


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
        page.wait_for_timeout(3000)
        expect(page.locator(TejasComputeLocators.MACHINE_DETAILS_HEADER)).to_be_visible()
        expect(page.locator(TejasComputeLocators.AVAILABILITY_ZN_DROPDOWN)).to_be_enabled()
        expect(page.locator(TejasComputeLocators.CHOOSE_IMAGE)).to_be_visible()
        expect(page.locator(TejasComputeLocators.PUBLIC_IMAGE)).to_be_visible()
        expect(page.locator(TejasComputeLocators.SNAPSHOT)).to_be_visible()
        expect(page.locator(TejasComputeLocators.ROOT_VOLUME_TYPE)).to_be_visible()
        expect(page.locator(TejasComputeLocators.CREATE_VM_SUMMARY)).to_be_visible()
        expect(page.locator(TejasComputeLocators.CANCEL_BUTTON)).to_be_enabled()

    @pytest.mark.testrail(27301)
    def test_to_verify_create_vm_header(self, page, tejas_create_vm_setup):
        create_vm_header = page.locator(TejasComputeLocators.CREATE_VM_HEADER).inner_text()
        assert create_vm_header == "Create Virtual Machine", f"The Create Virtual Machine header value - {create_vm_header}, is different than expected!"
        logging.info("Header on Create Virtual Machine screen is correct!")

    @pytest.mark.testrail(27302)
    def test_to_verify_create_vm_description(self, page, tejas_create_vm_setup):
        create_vm_description = page.locator(TejasComputeLocators.CREATE_VM_DESCRP).inner_text()
        expected_create_vm_description = "Virtual machines (VMs) are software-based emulations of physical computers. VMs allows to run multiple operating systems and applications on a single physical machine, providing isolation, flexibility and efficient utilization of computing resources."
        assert create_vm_description == expected_create_vm_description, f"The Create Virtual Machine description value - {create_vm_description}, is different than expected!"
        logging.info("Description on Create Virtual Machine screen is correct!")

    @pytest.mark.testrail(27303)
    def test_to_verify_machine_detail_description(self, page, tejas_create_vm_setup):
        machine_detail_description = page.locator(TejasComputeLocators.MACHINE_DETAILS_DESCRP).inner_text()
        assert machine_detail_description == "Choose a friendly name for your virtual machine.", f"The Machine details description value - {machine_detail_description}, is different than expected!"
        logging.info("Description on Machine details section is correct!")

    @pytest.mark.testrail(27304)
    def test_to_verify_machine_name_input_field(self, page, tejas_create_vm_setup):
        page.wait_for_timeout(2000)
        name_field_visibility = page.locator(TejasComputeLocators.NAME_FIELD).is_visible()
        # print("is visible - ", name_field_visibility)
        if name_field_visibility == True:
            page.locator(TejasComputeLocators.NAME_FIELD).type("TestingVM1")
        else:
            logging.info("Name field is not yet visible on create virtual machine screen!")

    @pytest.mark.testrail(27305)
    @pytest.mark.skip(reason="Need to recheck logic!")
    def test_to_verify_machine_name_field_has_required_label(self, page, tejas_create_vm_setup):
        # expect(page.locator(TejasComputeLocators.NAME_FIELD_LABEL)).to_have_attribute()
        placeholderText = page.get_by_placeholder('Please enter a name').inner_text()
        # print(placeholderText)
        expect(placeholderText).to_have_text('Please enter a name')

    @pytest.mark.skip(reason="Need to recheck logic!")
    def test_to_verify_choose_availability_zone_description(self, page, tejas_create_vm_setup):
        availability_zone_description = page.locator(TejasComputeLocators.AVAILABILITY_ZN_DROPDOWN).inner_text()
        expected_availability_zone_description = ""
        assert availability_zone_description == expected_availability_zone_description, f"The Machine details description value - {expected_availability_zone_description}, is different than expected!"
        logging.info("Description on Machine details section is correct!")








    # #testrail id C27299
    # def test_clicking_on_create_virtual_machine(self, browser):
    #         page = browser
    #         page.wait_for_timeout(3000)
    #         page.wait_for_selector(TejasComputeLocators.CREATE_VM_BUTTON).click()
    #         virtual_machine_heading = page.locator(TejasComputeLocators.CREATE_VM_HEADER).text_content()
    #         assert virtual_machine_heading == "Create Virtual Machine", "User could not be navigated to Tejas Compute section!!"
    #         logging.info("User successfully redirected to Create Virtual Machine screen!")
    #



#     def test_goto_compute(self, page) -> None:
#         expected_text = "Compute"
#         actual_text = perform_click_compute_resource(page, "//a[contains(text(),'Compute')]")
#         assert actual_text == expected_text, f"User could not be navigated to {expected_text} module!!"
#         print(f"User has successfully navigated to {expected_text} module!")
#
#     def test_goto_tejas_compute(self, page) -> None:
#         page.wait_for_selector("//p[contains(text(),'Tejas Compute')]").click()
#         under_tejas_compute = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
#         print("Heading in the Tejas Compute section:    ", under_tejas_compute)
#         assert under_tejas_compute == "Tejas Compute", "User could not be navigated to Tejas Compute section!!"
#         print("User successfully navigated to Tejas Compute module!")
#
#     # Create VM
#     def test_vm_creation(self, page) -> None:
#         page.wait_for_selector("//button[contains(text(),'Create Virtual Machine')]").click()
#         page.wait_for_timeout(3000)
#         vm_username = "TestingVM1"
#         page.get_by_placeholder("Please enter a name").type(vm_username)
#         page.wait_for_timeout(3000)
#         page.wait_for_selector("//input[@value='Mum1']").click()
#
#         # choose an image
#         # Public Image option
#         page.wait_for_selector("//p[contains(text(),'Public Image')]").click()
#         # Selecting Ubuntu
#         page.wait_for_selector("//div[@class='MuiStack-root css-xx6efg']/h6[contains(text(),'Ubuntu')]").click()
#         # Version
#         page.wait_for_selector("//input[@value='20.04 x64 ( ₹100.0/Month )']").click()
#
#         # Choose flavor
#         # General Compute
#         page.wait_for_selector("//p[normalize-space()='General Compute']").click()
#         # select options
#         page.wait_for_selector("//span[contains(text(),'CGI_large')]").click()
#
#         # volume type
#         page.wait_for_selector("//input[@value='RBD']").click()
#         page.wait_for_selector("//div[@class='MuiBox-root css-u4p24i']/button[2]").click()  # to increase root volume
#
#         # Machine credentials
#         page.wait_for_timeout(3000)
#         page.wait_for_selector("//p[normalize-space()='Username / Password']").click()
#
#         page.wait_for_selector("//input[@id='vm_username']").type("vinisharma")
#         page.wait_for_selector("//input[@id='vm_password']").type("India@1435")
#         page.wait_for_selector("//input[@id='vm_confirm_password']").type("India@1435")
#
#         # add Labels
#         page.wait_for_timeout(3000)
#         no_of_labels = 4
#         for no in range(no_of_labels):
#             randm_num = random.randint(1, 500)
#             final_nm = f"VM{randm_num}"
#             page.wait_for_selector("//input[@name='label']").type(final_nm)
#             page.wait_for_selector("//div[contains(text(),'Add Label')]").click()
#
#         # create VM
#         page.wait_for_timeout(3000)
#         page.wait_for_selector("//div[contains(text(),'Create')]").click()
#
#         # confirmation
#         page.wait_for_selector("//div[contains(text(),'Yes')]").click()
#
#         validate_new_vm = page.locator(f"//span[contains(text(),'{vm_username}')]").text_content()
#         #    expect(validate_new_vm).to_have_text(vm_username)
#         print(validate_new_vm)
#         #    rn = "xyz"
#         assert validate_new_vm == vm_username, "VM could not be created due to some issue!!"
#         print("VM successfully created!!!")
#
#
# #    availability_zone_drpdwn =page.locator("[name='availability_zone']")
# #    availability_zone_drpdwn.select_option(value="Mum1")
#
#
# '''
#     #Click QT
#     page.wait_for_selector("//div[contains(text(),'QT')]/self::div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-oeknvt']").click()
#
#     #Click Key pair
#     page.wait_for_selector("//div[@class='MuiBox-root css-0']/li[5]//div[2]/p[contains(text(),'Key Pairs')]").click()
#
#     #Click create key pair
#     page.wait_for_selector("//button[contains(text(),'Create Key Pair')]").click()
#
#     #send some value to name field
#     page.wait_for_selector("//input[@id='name']").type("TestingVS1")
#
#     #click create
#     page.wait_for_selector("//div[@class='MuiStack-root css-1qftbaz']/div[contains(text(),'Create')]").click()
#
# '''
#
#
#     def test_goto_compute(self, page) -> None:
#         expected_text = "Compute"
#         actual_text = perform_click_compute_resource(page, "//a[contains(text(),'Compute')]")
#         assert actual_text == expected_text, f"User could not be navigated to {expected_text} module!!"
#         print(f"User has successfully navigated to {expected_text} module!")
#
#     def test_goto_tejas_compute(self, page) -> None:
#         page.wait_for_selector("//p[contains(text(),'Tejas Compute')]").click()
#         under_tejas_compute = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
#         print("Heading in the Tejas Compute section:    ", under_tejas_compute)
#         assert under_tejas_compute == "Tejas Compute", "User could not be navigated to Tejas Compute section!!"
#         print("User successfully navigated to Tejas Compute module!")
#
#     # Create VM
#     def test_vm_creation(self, page) -> None:
#         page.wait_for_selector("//button[contains(text(),'Create Virtual Machine')]").click()
#         page.wait_for_timeout(3000)
#         vm_username = "TestingVM1"
#         page.get_by_placeholder("Please enter a name").type(vm_username)
#         page.wait_for_timeout(3000)
#         page.wait_for_selector("//input[@value='Mum1']").click()
#
#         # choose an image
#         # Public Image option
#         page.wait_for_selector("//p[contains(text(),'Public Image')]").click()
#         # Selecting Ubuntu
#         page.wait_for_selector("//div[@class='MuiStack-root css-xx6efg']/h6[contains(text(),'Ubuntu')]").click()
#         # Version
#         page.wait_for_selector("//input[@value='20.04 x64 ( ₹100.0/Month )']").click()
#
#         # Choose flavor
#         # General Compute
#         page.wait_for_selector("//p[normalize-space()='General Compute']").click()
#         # select options
#         page.wait_for_selector("//span[contains(text(),'CGI_large')]").click()
#
#         # volume type
#         page.wait_for_selector("//input[@value='RBD']").click()
#         page.wait_for_selector("//div[@class='MuiBox-root css-u4p24i']/button[2]").click()  # to increase root volume
#
#         # Machine credentials
#         page.wait_for_timeout(3000)
#         page.wait_for_selector("//p[normalize-space()='Username / Password']").click()
#
#         page.wait_for_selector("//input[@id='vm_username']").type("vinisharma")
#         page.wait_for_selector("//input[@id='vm_password']").type("India@1435")
#         page.wait_for_selector("//input[@id='vm_confirm_password']").type("India@1435")
#
#         # add Labels
#         page.wait_for_timeout(3000)
#         no_of_labels = 4
#         for no in range(no_of_labels):
#             randm_num = random.randint(1, 500)
#             final_nm = f"VM{randm_num}"
#             page.wait_for_selector("//input[@name='label']").type(final_nm)
#             page.wait_for_selector("//div[contains(text(),'Add Label')]").click()
#
#         # create VM
#         page.wait_for_timeout(3000)
#         page.wait_for_selector("//div[contains(text(),'Create')]").click()
#
#         # confirmation
#         page.wait_for_selector("//div[contains(text(),'Yes')]").click()
#
#         validate_new_vm = page.locator(f"//span[contains(text(),'{vm_username}')]").text_content()
#         #    expect(validate_new_vm).to_have_text(vm_username)
#         print(validate_new_vm)
#         #    rn = "xyz"
#         assert validate_new_vm == vm_username, "VM could not be created due to some issue!!"
#         print("VM successfully created!!!")
#
#
# #    availability_zone_drpdwn =page.locator("[name='availability_zone']")
# #    availability_zone_drpdwn.select_option(value="Mum1")
#
#
# '''
#     #Click QT
#     page.wait_for_selector("//div[contains(text(),'QT')]/self::div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-oeknvt']").click()
#
#     #Click Key pair
#     page.wait_for_selector("//div[@class='MuiBox-root css-0']/li[5]//div[2]/p[contains(text(),'Key Pairs')]").click()
#
#     #Click create key pair
#     page.wait_for_selector("//button[contains(text(),'Create Key Pair')]").click()
#
#     #send some value to name field
#     page.wait_for_selector("//input[@id='name']").type("TestingVS1")
#
#     #click create
#     page.wait_for_selector("//div[@class='MuiStack-root css-1qftbaz']/div[contains(text(),'Create')]").click()
#
# '''
