from time import sleep
from ..pages.cart_page import CartPage
from ..pages.home_page import HomePage
from ..pages.profile_page import ProfilePage


def test_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()
    home_page.go_to_login_screen()
    home_page.fill_login_inputs_valid_data_and_submit()
    profile_page = ProfilePage(driver)
    assert profile_page.check_for_my_orders_tab_on_page(), "Вы не авторизовались"


def test_add_item(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()
    item_that_was_added = home_page.get_item_that_i_added()
    home_page.add_item_to_cart()
    sleep(5)
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    item_that_is_in_cart = cart_page.get_item_in_cart()
    assert item_that_was_added in item_that_is_in_cart, \
        "В корзине не тот товар который вы ранее добавили"


def test_delete_item_from_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()
    home_page.add_item_to_cart()
    sleep(5)
    home_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.delete_item_from_cart()
    cart_page.should_be_empty_cart()
