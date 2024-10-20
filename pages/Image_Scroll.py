# side_click_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time

class SideClickPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    bengaluru_link_locator = (By.XPATH, "//a[@id='bengaluru']//div[contains(@class, 'tile-text') and contains(@class, 'text-center')]")
    clear_duration_locator = (By.XPATH, "//div[@onclick='clearDuration(event)']")
    duration_dropdown_locator = (By.XPATH, "//select[@id='duration-select']")
    category_dropdown_locator = (By.XPATH, "//select[@id='category-select']")
    image_locator = (By.XPATH, "//a[@id='0355034513']//img[@class='img-responsive']")
    next_arrow_locator = (By.XPATH, "//span[@class='carousel-control-next-icon']")

    # Methods
    def click_bengaluru(self):
        element = self.wait.until(EC.element_to_be_clickable(self.bengaluru_link_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def clear_duration(self):
        clear_duration_element = self.wait.until(EC.element_to_be_clickable(self.clear_duration_locator))
        clear_duration_element.click()

    def select_duration(self, duration_text):
        duration_select_element = self.wait.until(EC.presence_of_element_located(self.duration_dropdown_locator))
        Select(duration_select_element).select_by_visible_text(duration_text)

    def select_category(self, category_text):
        category_select_element = self.wait.until(EC.presence_of_element_located(self.category_dropdown_locator))
        Select(category_select_element).select_by_visible_text(category_text)

    def click_image(self):
        image_element = self.wait.until(EC.element_to_be_clickable(self.image_locator))
        image_element.click()

    def click_next_arrow(self, times=3):
        next_arrow = self.wait.until(EC.element_to_be_clickable(self.next_arrow_locator))
        for _ in range(times):
            self.driver.execute_script("arguments[0].click();", next_arrow)
            time.sleep(1)  # Optional wait between clicks

