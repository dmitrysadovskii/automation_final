from pages.base_page import BasePage
from pages.login_page import LoginPage
import allure


@allure.story("Check that main page opens")
def test_base_page_opens(browser):
    bp = BasePage(browser)
    bp.open_base_page()
    lp = LoginPage(browser)
    lp.open_login_page()
    lp.login_as_admin()
    lp.check_logged_in()

@allure.story("Check something")
def test_something():
    with allure.step("Step 1"):
        assert 1 == 1

@allure.story("Check something2")
def test_something_2():
    with allure.step("Step 33"):
        assert 1 == 1
        print('123')