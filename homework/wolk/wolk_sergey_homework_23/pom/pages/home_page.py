from selenium.webdriver.chrome.webdriver import WebDriver
from pom.pages.locators import page_locators as loc


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get('http://automationpractice.com/index.php')

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def sign_in_button(self):
        return self.find_element(loc.sign_in_button)

    def open_sign_in(self):
        self.find_element(loc.sign_in_button).click()
