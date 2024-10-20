# pages/navigation_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NavigationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.reservation_button = (By.XPATH, "//a[normalize-space()='Reservations']")
        self.home_button = (By.XPATH, "//a[@class='nav-link']")

    def click_reservation_button(self):
        self.driver.find_element(*self.reservation_button).click()

    def click_home_button(self):
        self.driver.find_element(*self.home_button).click()
