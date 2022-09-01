from selenium.webdriver.common.by import By
from .base_page import BasePage

email_field = (By.ID, 'email')
password_field = (By.ID, 'passwd')


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def email_filed(self):
        return self.find_element(email_field)

    @property
    def passwd_field(self):
        return self.find_element(password_field)

    def is_displayed_email_field(self):
        return self.email_filed.is_displayed()
