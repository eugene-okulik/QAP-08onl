from selenium.webdriver.chrome.webdriver import WebDriver
import settings


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.domain = settings.DOMAIN

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)
