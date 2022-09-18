from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePage
from pom.pages.locators import page_locators as loc

subject_field = (By.ID, 'uniform-id_contact')
email_field = (By.ID, 'email')
order_field = (By.ID, 'id_order')
file = (By.CLASS_NAME, 'filename')
message_field = (By.ID, 'message')


class Message(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def subject_field(self):
        return self.find_element(subject_field)

    def email_field(self):
        return self.find_element(email_field)

    def order_field(self):
        return self.find_element(order_field)

    def file(self):
        return self.find_element(file)

    def message_field(self):
        return self.find_element(message_field)

    def is_displayed_subject_field(self):
        return self.subject_field.is_displayed()

    def submit_button(self):
        return self.find_element(loc.submit_button)

    def submit_button_is_clickable(self):
        return self.find_element(loc.submit_button).is_enabled()
