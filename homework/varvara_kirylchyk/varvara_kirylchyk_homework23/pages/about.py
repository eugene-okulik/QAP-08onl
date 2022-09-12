from pages.base_page import BasePage
from locators import locators_about as loc


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def search(self):
        return self.find_element(loc.team)

    def open(self):
        self.driver.get('http://automationpractice.com/index.php?id_cms=4&controller=cms')


    def company_field(self):
        return self.find_element(loc.company)

    def team_field(self):
        return self.find_element(loc.team)

    def testimonials_field(self):
        return self.find_element(loc.testimonials)

    def is_displayed_search_field(self):
        return self.company_field.is_displayed()

    def is_displayed_phone_field(self):
        return self.team_field.is_displayed()

    def is_displayed_footer_field(self):
        return self.testimonials_field.is_displayed()
