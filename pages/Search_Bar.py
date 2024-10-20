# pages/search_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_bar = (By.ID, "autocomplete")
        self.search_results = (By.ID, "results")

    def enter_search_query(self, query: str):
        self.driver.find_element(*self.search_bar).send_keys(query)

    def clear_search_query(self):
        self.driver.find_element(*self.search_bar).clear()

    def wait_for_search_results_and_click(self):
        wait = WebDriverWait(self.driver, 20)
        result_element = wait.until(EC.visibility_of_element_located(self.search_results))
        result_element.click()
