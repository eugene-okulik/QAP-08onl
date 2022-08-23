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

    def open_journal(self):
        self.find_element(loc.journal_button).click()

    def switch_to_handle(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def callme_button(self):
        self.find_element(loc.callme_button)

    def test_pass_button(self):
        self.find_element(loc.pass_test_button)
