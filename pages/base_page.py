from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Вспомогательные методы для работы с WebDriver - будут постоянно использоваться
class BasePage():
    def __init__(self, browser, url, timeout=10): # при открытии страны нужно, чтобы был создан драйвер и url
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):                  # функция открытия страницы
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True



