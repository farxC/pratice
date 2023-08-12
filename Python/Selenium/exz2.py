from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def setUp(self):
    self.driver = webdriver.Edge()

def search_in_google(self):
    driver = self.driver
    driver.get("http://www.google.com")
