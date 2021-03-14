from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
