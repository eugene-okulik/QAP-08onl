from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePage
from pom.pages.locators import page_locators as loc


alert = (By.TAG_NAME, 'p')


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def cart(self):
        return self.find_element(loc.cart_button)

    def cart_open(self):
        return self.find_element(loc.cart_button).is_enabled()

    @property
    def alert_message(self):
        return self.find_element(alert)

    def alert_message_check(self):
        return self.alert_message.is_enabled()
