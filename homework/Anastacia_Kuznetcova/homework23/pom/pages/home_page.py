from homework.Anastacia_Kuznetcova.homework23.pom.pages.base_page import BasePage
from homework.Anastacia_Kuznetcova.homework23.pom.pages.locators import home_page_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        return self.driver.get('http://automationpractice.com/index.php?controller=best-sales')

    def t_shirt_btn(self):
        return self.find_element(home_page_locators.t_shirts_page)

    def contact_us_btn(self):
        return self.find_element(home_page_locators.contact_us)

    def cart_btn(self):
        return self.find_element(home_page_locators.cart)

    def t_shirt_btn_is_clickable(self):
        return self.find_element(home_page_locators.t_shirts_page).is_enabled()

    def test_contact_us_is_clickable(self):
        return self.find_element(home_page_locators.contact_us).is_enabled()

    def cart_is_clickable(self):
        return self.find_element(home_page_locators.cart).is_enabled()

    def test_contact_us_is_displayed(self):
        return self.find_element(home_page_locators.contact_us).is_displayed()

    def cart_is_displayed(self):
        return self.find_element(home_page_locators.cart).is_displayed()

    def t_shirt_is_displayed(self):
        return self.find_element(home_page_locators.t_shirts_page).is_displayed()
