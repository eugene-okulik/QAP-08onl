from homework_23.pages.base_page import BasePage
from homework_23.pages.locators import home_page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://zaochnik.com/')

    def open_sing_in(self):
        self.find_element(loc.sing_in_button).click()

    def open_prices_and_terms_page(self):
        self.find_element(loc.prices_and_terms_button).click()

    def open_payment_methods_page(self):
        self.find_element(loc.payment_methods_button).click()

