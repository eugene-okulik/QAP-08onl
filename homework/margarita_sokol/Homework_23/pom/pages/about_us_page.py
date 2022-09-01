from pages.base_page import BasePage
from pages.locators import about_us_page_locators


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?id_cms=4&controller=cms')

    def t_shirts_button(self):
        return self.find_element(about_us_page_locators.t_shirts_page)

    def t_shirts_is_displayed(self):
        return self.find_element(about_us_page_locators.t_shirts_page).is_displayed()

    def t_shirts_is_clickable(self):
        return self.find_element(about_us_page_locators.t_shirts_page).is_enabled()

    def dresses_button(self):
        return self.find_element(about_us_page_locators.dresses_page)

    def dresses_is_displayed(self):
        return self.find_element(about_us_page_locators.dresses_page).is_displayed()

    def dresses_is_clickable(self):
        return self.find_element(about_us_page_locators.dresses_page).is_enabled()

    def logo_field(self):
        return self.find_element(about_us_page_locators.logo)

    def logo_is_clickable(self):
        return self.find_element(about_us_page_locators.logo).is_enabled()

    def logo_is_displayed(self):
        return self.find_element(about_us_page_locators.logo).is_displayed()
