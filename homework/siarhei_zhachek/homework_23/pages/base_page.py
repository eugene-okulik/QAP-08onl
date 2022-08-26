from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def move_to_element(self, *args):
        by = args[0]
        return ActionChains(self.driver).move_to_element(by)



