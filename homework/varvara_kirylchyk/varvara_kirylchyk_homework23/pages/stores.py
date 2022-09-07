from pages.base_page import BasePage
from locators import locators_stores as loc


class StoresPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def search(self):
        return self.find_element(loc.big_map)

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?controller=stores')

    def big_map_field(self):
        return self.find_element(loc.big_map)

    def logo_field(self):
        return self.find_element(loc.logo)

    def address_field(self):
        return self.find_element(loc.address)

    def is_displayed_search_field(self):
        return self.big_map_field.is_displayed()

    def is_displayed_phone_field(self):
        return self.logo_field.is_displayed()

    def is_displayed_footer_field(self):
        return self.address_field.is_displayed()
