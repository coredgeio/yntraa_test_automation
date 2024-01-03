import time
import pytest
import asyncio
from playwright.sync_api import sync_playwright
import os
import requests

# username= "priti.ltd@yopmail.com"
# password ="India@143"
# url="https://console-revamp-sbx.yntraa.com"
class login_setup:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def perform_login(self, page):
        page.goto(self.url)
        page.wait_for_selector("//button[contains(text(),'Login')]").click()
        page.wait_for_selector("//input[@id='username']").type(self.username)
        page.wait_for_selector("//input[@id='password']").type(self.password)
        page.wait_for_selector("//input[@id='kc-login']").click()
        page.wait_for_load_state("load")  # Wait for the page to load
        time.sleep(4)


