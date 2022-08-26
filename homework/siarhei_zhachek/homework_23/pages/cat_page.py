from ..pages.base_page import BasePage
from ..pages.locators import cat_page_locators as loc


class CatPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_product_in_cat(self):
        product = self.find_element(loc.element_to_cat)
        return self.move_to_element(product).perform()

    def element_to_cat(self):
        return self.find_element(loc.element_to_cat).is_displayed()

    @property
    def element_cat(self):
        return self.find_element(loc.element_to_cat)

    def delete_product_in_cat(self):
        delete_button = self.find_element(loc.element_to_cat)
        return self.move_to_element(delete_button).perform()

    @property
    def delete_product(self):
        return self.find_element(loc.delete_product)

    @property
    def element_is_not_to_cat(self):
        return self.find_element(loc.element_is_not_to_cat)

