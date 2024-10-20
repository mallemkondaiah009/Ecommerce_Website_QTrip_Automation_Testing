# tests/test_navigation.py

import pytest
from pages.Navigation_Page import NavigationPage


@pytest.mark.usefixtures("login")
class TestNavigation:

    def test_navigation_buttons(self):
        self.driver.get("https://qtripdynamic-qa-frontend.vercel.app/")

        # Initialize the navigation page object
        navigation_page = NavigationPage(self.driver)

        # Click the Reservation button
        navigation_page.click_reservation_button()

        # Assertion for navigating to the Reservations page (adjust based on actual URL or page content)
        assert "Reservations" in self.driver.page_source, "Failed to navigate to Reservations page"

        # Click the Home button
        navigation_page.click_home_button()

        # Assertion for navigating back to the Home page (adjust based on actual URL or page content)
        assert "Home" in self.driver.page_source, "Failed to navigate back to Home page"
