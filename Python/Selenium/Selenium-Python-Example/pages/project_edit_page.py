from typing import Tuple
import allure 
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProjectEditPage(BasePage):
    """Project Edit Page - The page where adding to and editing projects is done"""

    _PROJECT_NAME_FIELD: Tuple[By, str] = (By.CSS_SELECTOR, "input#project-name")
    _THANK_YOU_PAGE_TYPE_BUTTON: Tuple[By, str] = (By.CSS_SELECTOR, "[for=select-single-outcome]")
    _OUTCOME_PAGES_TYPE_BUTTON: Tuple[By, str] = (By.CSS_SELECTOR, "[for=select-outcomes]")
    _START_EDITING_BUTTON: Tuple[By, str] = (By.CSS_SELECTOR, ".swal-button.swal-button--confirm")
    _SAVE_AND_EXIT_BUTTON: Tuple[By, str] = (By.CSS_SELECTOR, ".e-close.nav-link")

    def __init__(self,driver, wait):
        super().__init__(driver,wait)

    @allure.step("Click SAVE & EXIT button")
    def click_save_and_exit(self) -> None:
        self.click(self.__SAVE_AND_EXIT_BUTTON)
    
    @allure.step("Open new project for editing - project name {project_name}, project type: {project_type}")
    def edit_project_prep(self, project_name: str, project_type: str) -> None:
        self.fill_text(self._PROJECT_NAME_FIELD, project_name)
        if project_type == "thank you page" or project_type != "outcome":
            self.click(self._THANK_YOU_PAGE_TYPE_BUTTON)
        else:
            self.click(self.OUTCOME_PAGES_TYPE_BUTTON)
        self.click(self._START_EDITING_BUTTON)