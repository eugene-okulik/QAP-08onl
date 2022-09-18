from pom.pages.base_page import BasePage
from pom.pages.locators import page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def contact_us_button(self):
        return self.find_element(loc.contact_us_button)

    def open(self):
        self.driver.get('http://http://automationpractice.com/index.php?controller=best-sales')

    def open_contact_us(self):
        self.find_element(loc.contact_us_button).click()

    def submit_button(self):
        self.find_element(loc.submit_button).click()
