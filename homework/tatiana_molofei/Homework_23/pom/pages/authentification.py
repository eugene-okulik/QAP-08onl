from selenium.webdriver.common.by import By
from .base_page import BasePage
# from .locators import home_page_locators as loc

want_to_try_button = (By.XPATH, '//span[@class="ng-scope"]')
user_name_field = (By.ID, 'username')
password_field = (By.ID, 'password')
journal_button = (By.XPATH, '//a[@href="zhurnal"]')


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def username_field(self):
        return self.find_element(user_name_field)

    @property
    def passwd_field(self):
        return self.find_element(password_field)

    @property
    def want_to_try_field(self):
        return self.find_element(want_to_try_button)

    @property
    def test_journal_button(self):
        return self.find_element(journal_button)

    def want_to_try_is_displayed(self):
        return self.want_to_try_field.is_displayed()

    def username_field_is_displayed(self):
        return self.username_field.is_displayed()

    def passwd_field_is_displayed(self):
        return self.passwd_field.is_displayed()

    def test_journal_is_clickable(self):
        return self.test_journal_button.is_enabled()
