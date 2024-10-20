# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_link = (By.XPATH, "//a[normalize-space()='Login Here']")
        self.email_input = (By.ID, "floatingInput")
        self.password_input = (By.ID, "floatingPassword")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()

    def enter_email(self, email: str):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.submit_button).click()
