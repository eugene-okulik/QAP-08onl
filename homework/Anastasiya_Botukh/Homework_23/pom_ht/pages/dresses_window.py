from selenium.webdriver.common.by import By
from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.base_page import BasePage
from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.locators import page_locators as loc


logo = (By.ID, 'header_logo')
sort_field = (By.CSS_SELECTOR, 'select[id="selectProductSort"]')
search_field = (By.CSS_SELECTOR, 'input[class="search_query form-control ac_input"]')


class DressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def logo(self):
        return self.find_element(logo)

    def find_logo(self):
        return self.find_element(logo).is_displayed()

    @property
    def sort_field(self):
        return self.find_element(loc.sort_field)

    def sort_field_is_clickable(self):
        return self.find_element(loc.sort_field).is_enabled()

    @property
    def cart_button(self):
        return self.find_element(loc.cart_button)

    def cart_button_is_clickable(self):
        return self.cart_button.is_enabled()

    @property
    def search_field(self):
        return self.find_element(search_field)

    def search_field_is_clickable(self):
        return self.find_element(search_field).is_enabled()
