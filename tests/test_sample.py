from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.groups_page import GroupsPage
from pages.main_admin_page import MainAdminPage
from helpers.db_helper import add_db_group, connect_db, delete_db_group
from helpers.general_helpers import generate_string


def test_db_group_added_and_displayed(browser):
    db = connect_db()
    group_name = generate_string(8)
    add_db_group(db, group_name)
    bp = BasePage(browser)
    bp.open_base_page()
    lg = LoginPage(browser)
    lg.open_login_page()
    lg.login_as_admin()
    mp = MainAdminPage(browser)
    mp.should_be_main_page()
    mp.open_groups_page()
    gp = GroupsPage(browser)
    gp.check_group_exist(group_name)

