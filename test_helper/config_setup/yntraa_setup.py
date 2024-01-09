from test_helper.yantra_element_locators.compute_element import LoginRequirements

class login_setup_yntraa:
    def __init__(self, page, url, username, password):
        self.page = page
        self.url = url
        self.username = username
        self.password = password

    def perform_login(self):
        self.page.goto(self.url, timeout = 10000)
        self.page.wait_for_selector(LoginRequirements.LOGIN_BUTTON).click()
        self.page.wait_for_selector(LoginRequirements.USERNAME_LOCATOR).type(self.username)
        self.page.wait_for_selector(LoginRequirements.PASSWORD_LOCATOR).type(self.password)
        self.page.wait_for_selector(LoginRequirements.SIGN_IN_BUTTON).click()
        self.page.wait_for_load_state("load")


