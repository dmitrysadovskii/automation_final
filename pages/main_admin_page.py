from pages.base_page import BasePage
from locators.locators_main_admin_page import MainAdminLOcators


class MainAdminPage(BasePage, MainAdminLOcators):

    def should_be_main_page(self):
        self.find_element(self.LOCATOR_MAIN_TITLE)

    def open_groups_page(self):
        groups_link = self.find_element(self.LOCATOR_GROUPS)
        groups_link.click()

    def open_users_page(self):
        users_link = self.find_element(self.LOCATOR_USERS)
        users_link.click()

    def open_add_user_page(self):
        add_user_link = self.find_element(self.LOCATOR_ADD_USER)
        add_user_link.click()
