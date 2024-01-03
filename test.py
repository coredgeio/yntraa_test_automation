from playwright.sync_api import sync_playwright
import pytest
import time
import random


@pytest.mark.testrail(20933)
def test_yantra_connection():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://console-revamp-sbx.yntraa.com")
        #print("Main page Title: ", page.title())

        #login button
        page.wait_for_selector("//button[contains(text(),'Login')]").click()

        #enter username and pass
        page.wait_for_selector("//input[@id='username']").type("priti.ltd@yopmail.com")
        page.wait_for_selector("//input[@id='password']").type("India@143")

        #login to next page
        page.wait_for_selector("//input[@id='kc-login']").click()
        page.wait_for_load_state("load")  # Wait for the page to load
        time.sleep(4)

        # Wait for the title to contain the expected title
        act_title = "Yntraa"
        #page.wait_for_function(lambda: act_title in page.title())

        # Print and assert the title
        pg_title = page.title()
        act_text = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
    #    print(type(act_text))

    #    act_text_ele = act_text.element_handle()
        print("Heading present on the home page:    ",act_text)
        assert act_text == "Enabling Possibilities. Empowering Ideas.", "User could not be logged in!!"
        print("User Successfully Logged in!!!!!!")
    #    expect(act_text).to_have_text("Enabling Possibilities. Empowering Ideas.")

    #    page.wait_for_timeout(2000)

        #Go to Compute
        time.sleep(3)
        page.wait_for_selector("//a[contains(text(),'Compute')]").click()
        under_compute_text = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
        print("Heading in the Compute section:  ", under_compute_text)
        assert under_compute_text == "Compute", "User could not be navigated to Compute module!!"
        print("User has successfully navigated to Compute module!")

        #Go to Tejas Compute
        page.wait_for_selector("//p[contains(text(),'Tejas Compute')]").click()
        under_tejas_compute = page.locator("//div[@class='MuiStack-root css-1lpqru0']/h3").text_content()
        print("Heading in the Tejas Compute section:    ",under_tejas_compute)
        assert under_tejas_compute == "Tejas Compute", "User could not be navigated to Tejas Compute section!!"
        print("User successfully navigated to Tejas Compute module!")

        #Create VM
        page.wait_for_selector("//button[contains(text(),'Create Virtual Machine')]").click()
        time.sleep(3)
        vm_username = "TestingVM1"
        page.get_by_placeholder("Please enter a name").type(vm_username)
        page.wait_for_timeout(3000)
        page.wait_for_selector("//input[@value='Mum1']").click()


        #choose an image
        #Public Image option
        page.wait_for_selector("//p[contains(text(),'Public Image')]").click()
        #Selecting Ubuntu
        page.wait_for_selector("//div[@class='MuiStack-root css-xx6efg']/h6[contains(text(),'Ubuntu')]").click()
        #Version
        page.wait_for_selector("//input[@value='20.04 x64 ( ₹100.0/Month )']").click()

        #Choose flavor
        #General Compute
        page.wait_for_selector("//p[normalize-space()='General Compute']").click()
        #select options
        page.wait_for_selector("//span[contains(text(),'CGI_large')]").click()

        #volume type
        page.wait_for_selector("//input[@value='RBD']").click()
        page.wait_for_selector("//div[@class='MuiBox-root css-u4p24i']/button[2]").click() #to increase root volume

        #Machine credentials
        page.wait_for_timeout(3000)
        page.wait_for_selector("//p[normalize-space()='Username / Password']").click()

        page.wait_for_selector("//input[@id='vm_username']").type("vinisharma")
        page.wait_for_selector("//input[@id='vm_password']").type("India@1435")
        page.wait_for_selector("//input[@id='vm_confirm_password']").type("India@1435")

        #add Labels
        page.wait_for_timeout(3000)
        no_of_labels = 4
        for no in range(no_of_labels):
            randm_num = random.randint(1,500)
            final_nm = f"VM{randm_num}"
            page.wait_for_selector("//input[@name='label']").type(final_nm)
            page.wait_for_selector("//div[contains(text(),'Add Label')]").click()


        #create VM
        page.wait_for_timeout(3000)
        page.wait_for_selector("//div[contains(text(),'Create')]").click()

        #confirmation
        page.wait_for_selector("//div[contains(text(),'Yes')]").click()

        validate_new_vm = page.locator(f"//span[contains(text(),'{vm_username}')]").text_content()
    #    expect(validate_new_vm).to_have_text(vm_username)
        print(validate_new_vm)
    #    rn = "xyz"
        assert validate_new_vm == vm_username, "VM could not be created due to some issue!!"
        print("VM successfully created!!!")





    #    availability_zone_drpdwn =page.locator("[name='availability_zone']")
    #    availability_zone_drpdwn.select_option(value="Mum1")



        page.wait_for_timeout(20000)
        browser.close()

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


