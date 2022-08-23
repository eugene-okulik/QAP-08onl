from .base_page import BasePage
from ..locators import locators_best_sales as loc


class BestSalesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?controller=best-sales')

    def search_field(self):
        return self.find_element(loc.top_search)

    def phone_field(self):
        return self.find_element(loc.phone)

    def footer_field(self):
        return self.find_element(loc.footer)

    def is_displayed_search_field(self):
        return self.search_field.is_displayed()

    def is_displayed_phone_field(self):
        return self.phone_field.is_displayed()

    def is_displayed_footer_field(self):
        return self.footer_field.is_displayed()
