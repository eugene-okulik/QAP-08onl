from ..pages.base_page import BasePage
from ..pages.locators import home_page_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://apteka.magnit.ru/')

    def confirm_address(self):
        self.find_element(home_page_locators.confirm_address_button).click()

    def go_to_login_screen(self):
        self.find_element(home_page_locators.go_to_login_screen_button).click()

    def fill_login_inputs_valid_data_and_submit(self):
        self.find_element(home_page_locators.login_input).send_keys("+79964410394")
        self.find_element(home_page_locators.password_input).send_keys("R911t68901")
        self.find_element(home_page_locators.submit_button).click()

    def add_item_to_cart(self):
        self.find_element(home_page_locators.buy_button).click()

    def get_item_that_i_added(self):
        return self.find_element(home_page_locators.item_name).text

    def go_to_cart(self):
        self.find_element(home_page_locators.my_cart_button).click()
