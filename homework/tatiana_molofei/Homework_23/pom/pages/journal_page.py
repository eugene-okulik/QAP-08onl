from selenium.webdriver.common.by import By
from .base_page import BasePage


subscription_button = (By.XPATH, '//button[@class="btn btn-default"]')
journal_button = (By.XPATH, '//a[@href="zhurnal"]')


class JournalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://dsvd.by/')

    def open_journal(self):
        self.find_element(journal_button).click()

    @property
    def find_subscription_button(self):
        return self.find_element(subscription_button)

    def test_subscription_button_is_displayed(self):
        return self.find_subscription_button.is_displayed()
