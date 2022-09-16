"""modules"""
from ..pages.home_page import HomePage


def test_search_field_is_displayed(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.search_field().is_displayed()


def test_alert(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.enter_word("soup")
    home_page.click_on_the_search_button()
    home_page.alert()
    assert home_page.alert()


def test_printed_dress_in_cart(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.move_to_printed_dress()
    home_page.add_printed_dress_to_cart()
    home_page.printed_dress_in_cart()
    assert home_page.printed_dress_in_cart() != "empty"
