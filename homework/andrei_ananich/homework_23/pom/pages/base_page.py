"""modules"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """modules"""
    def __init__(self, driver: WebDriver):
        """modules"""
        self.driver = driver

    def find_element(self, *args):
        """modules"""
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        """modules"""
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def move_to_element(self, element):
        """modules"""
        return ActionChains(self.driver).move_to_element(element)
