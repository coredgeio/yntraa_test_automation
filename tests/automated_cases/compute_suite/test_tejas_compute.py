import pytest
from helper.config_setup.login import login_setup
from playwright.sync_api import sync_playwright
import time
import random

class TestExample:
    @pytest.fixture(scope="module")
    def browser(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            yield page
            context.close()

    @pytest.fixture(scope="module", autouse=True)
    def login_setup(self, browser):
        page = browser
        login = login_setup(url="https://console-revamp-sbx.yntraa.com", username="priti.ltd@yopmail.com", password="India@143")
        login.perform_login(page)
        return login

    @staticmethod
    @pytest.mark.testrail(16510)
    def test_something(browser):
        page = browser
        act_text = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
        print("Heading present on the home page:    ", act_text)
        assert act_text == "Enabling Possibilities. Empowering Ideas.", "User could not be logged in!!"
        print("User Successfully Logged in!!!!!!")
        return page
#

    def test_goto_compute(self, page) -> None:
        expected_text = "Compute"
        actual_text = perform_click_compute_resource(page, "//a[contains(text(),'Compute')]")
        assert actual_text == expected_text, f"User could not be navigated to {expected_text} module!!"
        print(f"User has successfully navigated to {expected_text} module!")

    def test_goto_tejas_compute(self, page) -> None:
        page.wait_for_selector("//p[contains(text(),'Tejas Compute')]").click()
        under_tejas_compute = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
        print("Heading in the Tejas Compute section:    ", under_tejas_compute)
        assert under_tejas_compute == "Tejas Compute", "User could not be navigated to Tejas Compute section!!"
        print("User successfully navigated to Tejas Compute module!")

    # Create VM
    def test_vm_creation(self, page) -> None:
        page.wait_for_selector("//button[contains(text(),'Create Virtual Machine')]").click()
        page.wait_for_timeout(3000)
        vm_username = "TestingVM1"
        page.get_by_placeholder("Please enter a name").type(vm_username)
        page.wait_for_timeout(3000)
        page.wait_for_selector("//input[@value='Mum1']").click()

        # choose an image
        # Public Image option
        page.wait_for_selector("//p[contains(text(),'Public Image')]").click()
        # Selecting Ubuntu
        page.wait_for_selector("//div[@class='MuiStack-root css-xx6efg']/h6[contains(text(),'Ubuntu')]").click()
        # Version
        page.wait_for_selector("//input[@value='20.04 x64 ( ₹100.0/Month )']").click()

        # Choose flavor
        # General Compute
        page.wait_for_selector("//p[normalize-space()='General Compute']").click()
        # select options
        page.wait_for_selector("//span[contains(text(),'CGI_large')]").click()

        # volume type
        page.wait_for_selector("//input[@value='RBD']").click()
        page.wait_for_selector("//div[@class='MuiBox-root css-u4p24i']/button[2]").click()  # to increase root volume

        # Machine credentials
        page.wait_for_timeout(3000)
        page.wait_for_selector("//p[normalize-space()='Username / Password']").click()

        page.wait_for_selector("//input[@id='vm_username']").type("vinisharma")
        page.wait_for_selector("//input[@id='vm_password']").type("India@1435")
        page.wait_for_selector("//input[@id='vm_confirm_password']").type("India@1435")

        # add Labels
        page.wait_for_timeout(3000)
        no_of_labels = 4
        for no in range(no_of_labels):
            randm_num = random.randint(1, 500)
            final_nm = f"VM{randm_num}"
            page.wait_for_selector("//input[@name='label']").type(final_nm)
            page.wait_for_selector("//div[contains(text(),'Add Label')]").click()

        # create VM
        page.wait_for_timeout(3000)
        page.wait_for_selector("//div[contains(text(),'Create')]").click()

        # confirmation
        page.wait_for_selector("//div[contains(text(),'Yes')]").click()

        validate_new_vm = page.locator(f"//span[contains(text(),'{vm_username}')]").text_content()
        #    expect(validate_new_vm).to_have_text(vm_username)
        print(validate_new_vm)
        #    rn = "xyz"
        assert validate_new_vm == vm_username, "VM could not be created due to some issue!!"
        print("VM successfully created!!!")


#    availability_zone_drpdwn =page.locator("[name='availability_zone']")
#    availability_zone_drpdwn.select_option(value="Mum1")


'''
    #Click QT
    page.wait_for_selector("//div[contains(text(),'QT')]/self::div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-oeknvt']").click()

    #Click Key pair
    page.wait_for_selector("//div[@class='MuiBox-root css-0']/li[5]//div[2]/p[contains(text(),'Key Pairs')]").click()

    #Click create key pair
    page.wait_for_selector("//button[contains(text(),'Create Key Pair')]").click()

    #send some value to name field
    page.wait_for_selector("//input[@id='name']").type("TestingVS1")

    #click create
    page.wait_for_selector("//div[@class='MuiStack-root css-1qftbaz']/div[contains(text(),'Create')]").click()

'''
