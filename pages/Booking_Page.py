# pages/booking_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BookingPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.bengaluru_tile = (
        By.XPATH, "//a[@id='bengaluru']//div[contains(@class, 'tile-text') and contains(@class, 'text-center')]")
        self.clear_duration_button = (By.XPATH, "//div[@onclick='clearDuration(event)']")
        self.duration_select = (By.XPATH, "//select[@id='duration-select']")
        self.category_select = (By.XPATH, "//select[@id='category-select']")
        self.image_click = (By.XPATH, "//img[@class='img-responsive']")
        self.name_input = (By.NAME, "name")
        self.date_input = (By.XPATH, "//input[@name='date']")
        self.price_input = (By.XPATH, "//input[@name='person']")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

    def select_bengaluru(self):
        wait = WebDriverWait(self.driver, 15)
        bengaluru_element = wait.until(EC.element_to_be_clickable(self.bengaluru_tile))

        # Scroll into view to avoid overlays blocking it
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bengaluru_element)

        # Click using JavaScript to avoid interception
        self.driver.execute_script("arguments[0].click();", bengaluru_element)

    def clear_duration(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.clear_duration_button)).click()

    def select_duration(self, duration: str):
        Select(self.driver.find_element(*self.duration_select)).select_by_visible_text(duration)

    def select_category(self, category: str):
        Select(self.driver.find_element(*self.category_select)).select_by_visible_text(category)

    def click_image(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.image_click)).click()

    def fill_booking_details(self, name: str, date: str, price: str):
        wait = WebDriverWait(self.driver, 10)

        # Fill the name
        name_input = wait.until(EC.visibility_of_element_located(self.name_input))
        name_input.send_keys(name)

        # Fill the date
        date_input = wait.until(EC.visibility_of_element_located(self.date_input))
        date_input.send_keys(date)

        # Fill the price (number of people)
        price_input = wait.until(EC.visibility_of_element_located(self.price_input))
        price_input.clear()
        price_input.send_keys(price)

    def submit_booking(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button)).click()
