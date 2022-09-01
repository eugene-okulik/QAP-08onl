from pom.pages.cart_window import CartPage
from pom.pages.cart_page import HomePage

def test_open_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_cart()
    cart_window = CartPage(driver)
    assert cart_window.cart_open()


def test_alert_message(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_cart()
    cart_window = CartPage(driver)
    assert cart_window.alert_message.is_enabled()
