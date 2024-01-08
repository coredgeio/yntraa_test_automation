import time
import pytest
import asyncio
from playwright.sync_api import sync_playwright
import os
import requests

class login_setup_yntraa:
    def __init__(self, page, url, username, password):
        self.page = page
        self.url = url
        self.username = username
        self.password = password

    def perform_login(self):
        self.page.goto(self.url)
        self.page.wait_for_selector("//button[contains(text(),'Login')]").click()
        self.page.wait_for_selector("//input[@id='username']").type(self.username)
        self.page.wait_for_selector("//input[@id='password']").type(self.password)
        self.page.wait_for_selector("//input[@id='kc-login']").click()
        self.page.wait_for_load_state("load")
        time.sleep(4)


