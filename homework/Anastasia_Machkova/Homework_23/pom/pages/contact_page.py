from selenium.webdriver.common.by import By
from .home_page import HomePage

email_field = (By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
order_reference = (By.ID, 'id_order')
message_field = (By.NAME, 'message')
send_button = (By.ID, 'submitMessage')
alert_message = (By.XPATH, '//div[@class="alert alert-danger"]/p')


class ContactPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def email_address(self):
        email = self.find_element(email_field)
        email.click()
        email.send_keys('nastya.machkova@gmail.com')
        return email_field

    def order_reference(self):
        order = self.find_element(order_reference)
        order.click()
        order.send_keys('245')
        return order_reference

    def message(self):
        text = self.find_element(message_field)
        text.send_keys('Hello')
        return message_field

    def submit_message(self):
        return self.find_element(send_button).click()

    def alert(self):
        return self.find_element(alert_message).is_displayed()
