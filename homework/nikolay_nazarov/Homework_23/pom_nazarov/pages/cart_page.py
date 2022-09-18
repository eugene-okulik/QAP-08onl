from selenium.common import NoSuchElementException

from ..pages.base_page import BasePage

from ..pages.locators import cart_page_locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_item_in_cart(self):
        return self.find_element(cart_page_locators.item_in_cart).text

    def delete_item_from_cart(self):
        self.find_element(cart_page_locators.delete_item_button).click()

    def should_be_empty_cart(self):
        try:
            assert "Ваша корзина пока пуста" in \
                   self.find_element(cart_page_locators.your_cart_is_empty).text
        except NoSuchElementException:
            return False
        except AssertionError:
            return False
        return True
