from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.base_page import BasePage
from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.locators import page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def cart(self):
        return self.find_element(loc.cart_button)

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?controller=best-sales')

    def open_cart(self):
        return self.find_element(loc.cart_button).click()
