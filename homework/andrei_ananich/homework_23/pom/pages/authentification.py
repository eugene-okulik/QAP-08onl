"""modules"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


email_field = (By.ID, 'email')
password_field = (By.ID, 'passwd')
contact_us = (By.XPATH, '//*[@id="contact-link"]/a')


class AuthPage(BasePage):
    """modules"""
    def __init__(self, driver):
        """modules"""
        super().__init__(driver)
        self.driver = driver

    @property
    def email_filed(self):
        """modules"""
        return self.find_element(email_field)

    @property
    def passwd_field(self):
        """modules"""
        return self.find_element(password_field)

    def is_displayed_email_field(self):
        """modules"""
        return self.email_filed.is_displayed()

    @property
    def contact_us(self):
        """modules"""
        return self.find_element(contact_us)
