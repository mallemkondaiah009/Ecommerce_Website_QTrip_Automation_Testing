# tests/test_registration.py

import pytest
from pages.Registeration_Page import RegistrationPage


@pytest.mark.usefixtures("init_driver")
class TestRegistration:

    def test_register(self):
        self.driver.get("https://qtripdynamic-qa-frontend.vercel.app/pages/register/")
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_email("roronoa@zoro")
        registration_page.enter_password("123456789")
        registration_page.enter_confirm_password("123456789")
        registration_page.click_register()
