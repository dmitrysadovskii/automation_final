from pages.base_page import BasePage
from locators.locators_login_page import LoginLocators


class LoginPage(BasePage, LoginLocators):

    def should_be_login_page(self):
        self.find_element(self.LOCATOR_USERNAME)
        self.find_element(self.LOCATOR_PASSWORD)

    def open_login_page(self):
        go_admin = self.find_element(self.LOCATOR_GO_TO_ADMIN)
        go_admin.click()

    def login_as_admin(self):
        username = self.find_element(self.LOCATOR_USERNAME)
        passwd = self.find_element(self.LOCATOR_PASSWORD)
        submit = self.find_element(self.LOCATOR_LOG_IN)
        submit.click()
        username.send_keys("admin")
        passwd.send_keys('password')
        submit.click()

    def check_logged_in(self):
        self.find_element(self.LOCATOR_LOG_OUT)
