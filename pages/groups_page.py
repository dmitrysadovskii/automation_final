from pages.base_page import BasePage
from locators.locators_groups_page import GroupsLOcators


class GroupsPage(BasePage, GroupsLOcators):

    def check_group_exist(self, group):
        groups = self.find_elements(self.LOCATOR_GROUP_ROW)
        group_list = [i.text for i in groups]
        assert group in group_list, f'{group} not found in {group_list}'
        print(f'{group} found in {group_list}')

