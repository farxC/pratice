from typing import Tuple

import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AboutPage(BasePage):
    """ About page - The first page that apperars when navigating to base URL"""
    LOGIN_LINK: Tuple[By, str] = (By.CSS_SELECTOR, '.login')
    REGISTER_LINK: Tuple[By, str] = (By.CSS_SELECTOR, '.register')

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step("Click Login link")
    def click_login_link(self) -> None:
        self.click(self.LOGIN_LINK)

    @allure.setp("Click Register link")
    def click_register_link(self) -> None:
        self.click(self.REGISTER_LINK)