from .base_page import BasePage
from ..pages.locators import home_page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://kst.by/')

    @property
    def search_field(self):
        return self.find_element(loc.search_field)

    @property
    def search_button(self):
        return self.find_element(loc.search_button)

    def search_field_is_displayed(self):
        return self.search_field.is_displayed()

    def enter_text_search(self):
        return self.find_element(loc.search_field).send_keys('ноутбук')

    def search_button_press(self):
        return self.find_element(loc.search_button).click()

    def move_to_catalog(self):
        catalog_field = self.find_element(loc.catalog)
        return self.move_to_element(catalog_field).perform()

    def computers_and_accessories(self):
        computers_accessories = self.find_element(loc.computers_and_accessories)
        return self.move_to_element(computers_accessories).perform()

    def power_supplies(self):
        return self.find_element(loc.power_supplies).click()

    def go_to_cat(self):
        return self.find_element(loc.cat_link).click()

    def move_laptops_und_computer(self):
        laptops_und_computers = self.find_element(loc.laptops_und_computer)
        return self.move_to_element(laptops_und_computers).perform()

    @property
    def notebooks(self):
        return self.find_element(loc.notebooks)

    def move_to_notebooks(self):
        notebooks_to = self.find_element(loc.notebooks)
        return self.move_to_element(notebooks_to).perform()
