from pages.base_page import BasePage
from pages.locators import stores_page_locators


class StoresPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?controller=stores')

    def address_field(self):
        return self.find_element(stores_page_locators.address)

    def address_is_displayed(self):
        return self.find_element(stores_page_locators.address).is_displayed()

    def address__is_clickable(self):
        return self.find_element(stores_page_locators.address).is_enabled()

    def card_field(self):
        return self.find_element(stores_page_locators.card)

    def card_is_displayed(self):
        return self.find_element(stores_page_locators.card).is_displayed()

    def card_is_clickable(self):
        return self.find_element(stores_page_locators.card).is_enabled()

    def search_field(self):
        return self.find_element(stores_page_locators.address)

    def search_is_clickable(self):
        return self.find_element(stores_page_locators.search_field).is_enabled()

    def search_is_displayed(self):
        return self.find_element(stores_page_locators.search_field).is_displayed()
