from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePage

email_field = (By.ID, 'email')
passwd_field = (By.ID, 'passwd')


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def email_field(self):
        return self.find_element(email_field)

    @property
    def passwd_field(self):
        return self.find_element(passwd_field)

    def is_displayed_email_field(self):
        return self.email_field.is_displayed()
