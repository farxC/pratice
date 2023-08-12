from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()


    # Navegar até a URL
driver.get("https://www.example.com")
    # Obtém todos os elementos disponíveis com o nome
elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)