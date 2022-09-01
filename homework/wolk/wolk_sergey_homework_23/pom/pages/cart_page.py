from pom.pages.base_page import BasePage
from pom.pages.locators import page_locators as loc


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?controller=best-sales')

    def cart(self):
        return self.find_element(loc.cart_button)

    def open_cart(self):
        return self.find_element(loc.cart_button).click()

    def sort_is_clickable(self):
        self.find_element(loc.sort_field).click()

    def cart_button(self):
        self.find_element(loc.cart_button).click()

    def search_field(self):
        return self.find_element(loc.search_field).click()

    def contact_us_button(self):
        return self.find_element(loc.contact_us_button).click()

    def submit_button(self):
        self.find_element(loc.submit_button).click()

    def open_dressed(self):
        self.find_element(loc.dresses).click()
