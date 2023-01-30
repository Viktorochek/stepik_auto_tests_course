from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

# Вспомогательные методы для работы с WebDriver - будут постоянно использоваться
class BasePage():
    def __init__(self, browser, url): # при открытии страны нужно, чтобы был создан драйвер и url
        self.browser = browser
        self.url = url

    def open(self):                  # функция открытия страницы
        self.browser.get(self.url)

