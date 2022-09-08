from .base_page import BasePage
from .locators import home_page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://dsvd.by/')

    def open_sign_in(self):
        self.find_element(loc.customer_login_button).click()

    def switch_to_the_handle(self):
        return self.switch_to_handle(1)

    @property
    def call_me_button(self):
        return self.find_element(loc.callme_button)

    def callme_is_clickable(self):
        return self.call_me_button.is_enabled()

    def pass_button(self):
        self.find_element(loc.pass_test_button)

    @property
    def pass_the_button(self):
        return self.find_element(loc.pass_test_button)

    def test_pass_field_is_clickable(self):
        return self.pass_the_button.is_enabled()
