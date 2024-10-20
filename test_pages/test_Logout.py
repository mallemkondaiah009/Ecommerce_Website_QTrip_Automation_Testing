# test_side_click.py or test_logout.py
import pytest
from pages.Logout import Logout


@pytest.mark.usefixtures("login")
class TestLogout:
    def test_logout(self):
        page = Logout(self.driver)

        # Perform the logout action
        page.logout()

