"""modules"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import home_page_locators as loc


search_field = (By.ID, 'search_query_top')
search_button = (By.NAME, 'submit_search')
alert_field = (By.CLASS_NAME, 'alert-warning')
add_printed_dress = (By.CSS_SELECTOR, 'a[data-id-product="2"]')
container = (By.CLASS_NAME, 'product-container')
empty_text = (By.CLASS_NAME, 'ajax_cart_no_product')
contact = (By.ID, 'contact-link')


class HomePage(BasePage):
    """modules"""
    def __init__(self, driver):
        """modules"""
        super().__init__(driver)
        self.driver = driver

    def open(self):
        """modules"""
        self.driver.get('http://automationpractice.com/index.php')

    def open_sign_in(self):
        """modules"""
        self.find_element(loc.sign_in_button).click()

    def open_contact_us(self):
        """modules"""
        return self.find_element(loc.contact_us_button).click()

    def move_to_printed_dress(self):
        """modules"""
        product = self.find_element(container)
        return self.move_to_element(product).perform()

    def add_printed_dress_to_cart(self):
        """modules"""
        return self.find_element(add_printed_dress).click()

    def printed_dress_in_cart(self):
        """modules"""
        return self.find_element(empty_text).text

    def search_field(self):
        """modules"""
        return self.find_element(search_field)

    def enter_word(self, word):
        """modules"""
        search = self.find_element(search_field)
        search.click()
        search.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        """modules"""
        return self.find_element(search_button).click()

    def alert(self):
        """modules"""
        return self.find_element(alert_field).is_displayed()
