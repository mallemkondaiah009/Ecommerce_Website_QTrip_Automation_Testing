# tests/test_search.py

import pytest
from pages.Search_Bar import SearchPage


@pytest.mark.usefixtures("login")
class TestSearch:

    def test_search_functionality(self):
        # Navigate to the homepage
        self.driver.get("https://qtripdynamic-qa-frontend.vercel.app/")

        # Initialize the search page object
        search_page = SearchPage(self.driver)

        # Perform search operation
        search_page.enter_search_query("goa")
        search_page.clear_search_query()
        search_page.enter_search_query("goa")

        # Wait for search results to appear and click on one
        search_page.wait_for_search_results_and_click()


