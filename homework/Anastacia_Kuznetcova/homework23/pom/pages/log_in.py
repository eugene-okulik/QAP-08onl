from homework.Anastacia_Kuznetcova.homework23.pom.pages.base_page import BasePage
from homework.Anastacia_Kuznetcova.homework23.pom.pages.locators import contact_us_locators as ml


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        return self.driver.get('http://automationpractice.com/index.php?controller=contact')

    def mail_field(self):
        return self.find_element(ml.mail).click()

    def order_num(self):
        return self.find_element(ml.order).click()

    def message_field(self):
        return self.find_element(ml.message).click()

    def submit_btn(self):
        return self.find_element(ml.submit).click()

    def alert(self):
        return self.find_element(ml.alert_msg).text

    def mail_inp(self):
        return self.find_element(ml.mail).send_keys("stassia92@no.ru")

    def order_inp(self):
        return self.find_element(ml.order).send_keys("5893272")

    def message_inp(self):
        return self.find_element(ml.message).send_keys("Homework23")

    def search_form(self):
        return self.find_element(ml.search).click()

    def search_input(self):
        return self.find_element(ml.search).send_keys("dress")

    def search_btn(self):
        return self.find_element(ml.search_sub).click()

    def search_res_txt(self):
        return self.find_element(ml.search_res).text

    def cart_check(self):
        return self.find_element(ml.cart).click()

    def cart_alert_check(self):
        return self.find_element(ml.alert_cart).text
