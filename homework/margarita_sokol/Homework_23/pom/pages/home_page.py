from pages.base_page import BasePage
from pages.locators import home_page_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?controller=best-sales')

    def cart_button(self):
        return self.find_element(home_page_locators.cart)

    def contact_us_button(self):
        return self.find_element(home_page_locators.contact_us)

    def women_button(self):
        return self.find_element(home_page_locators.women_pages)

    def cart_is_clickable(self):
        return self.find_element(home_page_locators.cart).is_enabled()

    def women_is_clickable(self):
        return self.find_element(home_page_locators.women_pages).is_enabled()

    def contact_us_is_clickable(self):
        return self.find_element(home_page_locators.contact_us).is_enabled()

    def cart_is_displayed(self):
        return self.find_element(home_page_locators.cart).is_displayed()

    def women_is_displayed(self):
        return self.find_element(home_page_locators.women_pages).is_displayed()

    def contact_us_is_displayed(self):
        return self.find_element(home_page_locators.contact_us).is_displayed()
