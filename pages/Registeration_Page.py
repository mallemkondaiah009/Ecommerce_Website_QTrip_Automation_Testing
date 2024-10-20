# pages/registration_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.email_input = (By.ID, "floatingInput")
        self.password_input = (By.NAME, "password")
        self.confirm_password_input = (By.NAME, "confirmpassword")
        self.register_button = (By.XPATH, "//button[normalize-space()='Register Now']")

    def enter_email(self, email: str):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_confirm_password(self, confirm_password: str):
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()
