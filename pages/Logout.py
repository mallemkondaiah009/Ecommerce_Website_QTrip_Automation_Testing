# side_click_page.py or another relevant page object file
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class Logout:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    logout_button_locator = (By.XPATH, "//div[@class='nav-link login register']")

    # Methods
    def logout(self):
        logout_button = self.wait.until(EC.element_to_be_clickable(self.logout_button_locator))
        logout_button.click()

