from ..pages.base_page import BasePage
from ..pages.locators import seach_page_locators as loc


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def all_elements(self):
        return self.find_element(loc.all_element)

    @property
    def no_product(self):
        return self.find_element(loc.no_product)

    def move_to_power_supplies(self):
        power_suppl = self.find_element(loc.power_supplies)
        return self.move_to_element(power_suppl).perform()

    def add_to_cat(self):
        return self.find_element(loc.add_to_cat).click()

    def cat_link(self):
        return self.find_element(loc.cat_link).click()

    @property
    def laptops_in_page(self):
        return self.find_element(loc.laptops_in_page)
