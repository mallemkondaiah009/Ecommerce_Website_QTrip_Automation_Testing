# tests/test_login.py

import pytest
from pages.Login_Page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login(self):
        self.driver.get("https://qtripdynamic-qa-frontend.vercel.app/")
        login_page = LoginPage(self.driver)

        # Perform login
        login_page.click_login_link()
        login_page.enter_email("roronoa@zoro")
        login_page.enter_password("123456789")
        login_page.click_login()
