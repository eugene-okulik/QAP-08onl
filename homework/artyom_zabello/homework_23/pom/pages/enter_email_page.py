from selenium.webdriver.common.by import By
from ..pages.base_page_dev_by import BasePage


EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
ERROR_MESSAGE = (By.XPATH, '//span[@class="message message_error"]')


class EnterEmailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email(self):
        self.find_element(EMAIL_FIELD).send_keys('test')

    def enter_password(self):
        self.find_element(PASSWORD_FIELD).send_keys('test')

    def press_submit(self):
        self.find_element(SUBMIT_BUTTON).click()

    def find_error(self):
        return self.find_element(ERROR_MESSAGE)
