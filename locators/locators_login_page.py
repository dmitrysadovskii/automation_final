from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_GO_TO_ADMIN = (By.XPATH, "//a[@href='/admin']")
    LOCATOR_USERNAME = (By.XPATH, "//input[@name='username']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOCATOR_LOG_IN = (By.XPATH, "//input[@type='submit']")
    LOCATOR_LOG_OUT = (By.XPATH, "//a[@href='/admin/logout/']")
