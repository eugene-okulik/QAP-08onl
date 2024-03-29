from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        element, value = args[0]
        return self.driver.find_element(element, value)

    def move_to_element(self, element):
        return ActionChains(self.driver).move_to_element(element)
