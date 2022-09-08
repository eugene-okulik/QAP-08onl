from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        by_element, val = args[0]
        return self.driver.find_element(by_element, val)

    def find_elements(self, *args):
        by_element, val = args[0]
        return self.driver.find_element(by_element, val)
