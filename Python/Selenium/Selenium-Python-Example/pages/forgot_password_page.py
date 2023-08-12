from typing import Tuple

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ForgotPassWordPage(BasePage):
    EMAIL_FIELD: Tuple[By, str] = (By.CSS_SELECTOR = "[name=email]")
    SEND_PASSWORD_RESET_LINK_BUTTON: Tuple[By, str] = (By.CSS_SELECTOR, "[type=submit]")
    ERROR_MSG: Tuple[By, str] = (By.CSS_SELECTOR, '.alert-danger')
    SUCESS_MSG: Tuple[By, str] = (By.CSS_SELECTOR, '.alert-success')
    PAGE_TITLE: Tuple[By, str] = (By.CSS_SELECTOR, '.e-form.heading')

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Send password reset link to email address: {email}")
    def send_password_sreset_link(self, email: str) -> None:
        self.fill_text(self.EMAIL_FIELD, email)
        self.click(self.SEND_PASSWORD_RESET_LINK_BUTTON)

    @allure.step("Get invalid email message")
    def get_invalid_email_message(self) -> str:
        return self.get_text(self.ERROR_MSG)
    
    @allure.step("Get succes message")
    def get_success_message(self) -> str:
        return self.get_text(self.SUCESS_MSG)
    
    @allure.step("Get Forgot password page title")
    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)