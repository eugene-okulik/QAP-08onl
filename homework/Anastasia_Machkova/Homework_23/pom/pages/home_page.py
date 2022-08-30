from selenium.webdriver.common.by import By
from .base_page import BasePage


search_field = (By.ID, 'search_query_top')
search_button = (By.NAME, 'submit_search')
alert_field = (By.CLASS_NAME, 'alert-warning')
add_blouse = (By.CSS_SELECTOR, 'a[data-id-product="2"]')
container = (By.CLASS_NAME, 'product-container')
empty_text = (By.CLASS_NAME, 'ajax_cart_no_product')
contact = (By.ID, 'contact-link')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('http://automationpractice.com/index.php')

    def contact_us(self):
        return self.find_element(contact).click()

    def move_to_blouse(self):
        product = self.find_element(container)
        return self.move_to_element(product).perform()

    def add_blouse_to_cart(self):
        return self.find_element(add_blouse).click()

    def blouse_in_cart(self):
        return self.find_element(empty_text).text

    def search_field(self):
        return self.find_element(search_field)

    def enter_word(self, word):
        search = self.find_element(search_field)
        search.click()
        search.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(search_button).click()

    def alert(self):
        return self.find_element(alert_field).is_displayed()
