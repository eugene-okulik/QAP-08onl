from selenium.webdriver.chrome.webdriver import WebDriver
import allure


allure.feature("UI Testing")
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    def find_element(self, *args):
        search, val = args[0]
        return self.driver.find_element(search, val)


    def dummy_element(self, *args):
        search, val = args[0]
        return self.driver.find_element(search, val)
