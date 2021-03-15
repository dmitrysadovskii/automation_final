from pages.base_page import BasePage
from locators.locators_groups_page import GroupsLOcators


class GroupsPage(BasePage, GroupsLOcators):

    def check_group_exist(self, group):
        groups = self.find_elements(self.LOCATOR_GROUP_ROW)
        exist = False
        for i in groups:
            if group in i.text:
                exist = True
        assert exist is True, f"{group} not found"
        print(f"{group} exist")
