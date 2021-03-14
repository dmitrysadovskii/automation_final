from pages.base_page import BAsePage
from time import sleep
import allure


#@allure.story("Check that main page opens")
def test_base_page_opens(browser):
    bp = BAsePage(browser)
    #with allure.step("Open main page"):
    bp.open_base_page()
    sleep(4)
