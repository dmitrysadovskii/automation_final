from pages.base_page import BAsePage
from time import sleep
def test_1(browser):
    bp = BAsePage(browser)
    bp.open_base_page()
    sleep(4)