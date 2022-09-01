from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.cart_page import HomePage
from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.cart_window import CartPage


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
