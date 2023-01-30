import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Фикстуры
@pytest.fixture(scope="function") # функция расширяет возможности написанной вами функции
def browser():
    browser_service = Service(ChromeDriverManager().install()) # установка DriverManager
    browser = webdriver.Chrome(service=browser_service) # создается сам драйвер
    browser.maximize_window() # отрытие драйвера на всю ширину экрана
    yield browser # вернуть драйвер - до yield: выполнится перед тестом, после yield: закрывается браузер
    browser.quit()
