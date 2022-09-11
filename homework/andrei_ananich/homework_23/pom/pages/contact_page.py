"""modules"""
from selenium.webdriver.common.by import By
from .home_page import HomePage

email_field = (By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
order_reference = (By.ID, 'id_order')
message_field = (By.NAME, 'message')
send_button = (By.ID, 'submitMessage')
alert_message = (By.XPATH, '//div[@class="alert alert-danger"]/p')


class ContactPage(HomePage):
    """modules"""
    def __init__(self, driver):
        """modules"""
        super().__init__(driver)
        self.driver = driver

    def email_address(self):
        """modules"""
        email = self.find_element(email_field)
        email.click()
        email.send_keys('andrei.ananich@gmail.com')
        return email_field

    def order_reference(self):
        """modules"""
        order = self.find_element(order_reference)
        order.click()
        order.send_keys('12345')
        return order_reference

    def message(self):
        """modules"""
        text = self.find_element(message_field)
        text.send_keys('Test')
        return message_field

    def submit_message(self):
        """modules"""
        return self.find_element(send_button).click()

    def alert(self):
        """modules"""
        return self.find_element(alert_message).is_displayed()
