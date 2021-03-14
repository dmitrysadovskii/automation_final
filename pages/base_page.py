from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BAsePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = "http://localhost:8000"

    def open_base_page(self):
        self.driver.get(self.base_page)
