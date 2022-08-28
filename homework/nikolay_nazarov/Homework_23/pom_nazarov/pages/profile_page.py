from selenium.common import NoSuchElementException

from ..pages.base_page import BasePage

from ..pages.locators import profile_page_locators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_for_my_orders_tab_on_page(self):
        try:
            self.find_element(profile_page_locators.my_data_tab)
        except NoSuchElementException:
            return False
        return True
