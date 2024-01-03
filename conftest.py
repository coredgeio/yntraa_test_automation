import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="module", autouse=True)
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()

@pytest.fixture(scope="class", autouse=True)
def login_func(browser):
    page = browser
    page.goto("https://console-dev.yntraa.com/")
    page.wait_for_selector("//button[contains(text(),'Login')]").click()
    page.wait_for_selector("//input[@id='username']").type("archana-qa-user01@yopmail.com")
    page.wait_for_selector("//input[@id='password']").type("India@143")
    page.wait_for_selector("//input[@id='kc-login']").click()
    page.wait_for_load_state("load")


# def filedownloader_path(text_content):
#     config_directory = os.path.dirname(os.path.abspath(__file__))
#     project_root = os.path.dirname(config_directory)
#     download_folder = "downloadFile"
#     downloads_path = os.path.join(project_root, "helper", download_folder)
#     os.makedirs(downloads_path, exist_ok=True)
#     file_name = "test.txt"  # Change the file extension to txt
#     file_path = os.path.join(downloads_path, file_name)
#     with open(file_path, "w+") as file:
#         file.write(text_content)
#
# sample_text_content = "Hello, this is a sample text file!"
# filedownloader_path(sample_text_content)
