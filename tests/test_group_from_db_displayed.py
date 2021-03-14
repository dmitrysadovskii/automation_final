from pages.base_page import BAsePage
from time import sleep
import allure


@allure.story("Check that main page opens")
def test_base_page_opens(browser):
    bp = BAsePage(browser)
    with allure.step("Open main page"):
        bp.open_base_page()
        sleep(4)


@allure.story("Check something")
def test_something():
    with allure.step("Step 1"):
        assert 1 == 1

@allure.story("Check something2")
def test_something_2():
    with allure.step("Step 33"):
        assert 1 == 1
        print('123')