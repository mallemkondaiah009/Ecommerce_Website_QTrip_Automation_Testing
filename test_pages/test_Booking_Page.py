# tests/test_booking.py

import pytest
from pages.Booking_Page import BookingPage


@pytest.mark.usefixtures("init_driver")
class TestBooking:

    def test_place_booking(self):
        # Navigate to the homepage
        self.driver.get("https://qtripdynamic-qa-frontend.vercel.app/")

        # Initialize the booking page object
        booking_page = BookingPage(self.driver)

        # Select the Bengaluru tile
        booking_page.select_bengaluru()

        # Clear any selected duration
        booking_page.clear_duration()

        # Select a duration and category
        booking_page.select_duration("6-12 Hours")
        booking_page.select_category("Cycling Routes")

        # Click on the activity image
        booking_page.click_image()

        # Fill in the booking details
        booking_page.fill_booking_details(name="roronoa zoro", date="05252025", price="9")

        # Submit the booking
        booking_page.submit_booking()

        # Add assertion to verify successful booking (adjust this based on actual conditions)
        assert "Booking Confirmed" in self.driver.page_source, "Booking failed or confirmation not shown"
