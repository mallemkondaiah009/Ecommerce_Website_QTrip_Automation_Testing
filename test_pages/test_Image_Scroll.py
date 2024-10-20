# test_side_click.py
import pytest
from pages.Image_Scroll import SideClickPage


@pytest.mark.usefixtures("login")
class TestSideClick:
    def test_side_click_flow(self):
        page = SideClickPage(self.driver)

        # Perform actions
        page.click_bengaluru()
        page.clear_duration()
        page.select_duration("6-12 Hours")
        page.select_category("Serene Beaches")
        page.click_image()
        page.click_next_arrow(times=3)

