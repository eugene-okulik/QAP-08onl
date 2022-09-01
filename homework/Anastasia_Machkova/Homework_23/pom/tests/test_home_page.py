from ..pages.home_page import HomePage


def test_search_field_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.search_field().is_displayed()


def test_alert(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.enter_word("soup")
    home_page.click_on_the_search_button()
    home_page.alert()
    assert home_page.alert()


def test_blouse_in_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.move_to_blouse()
    home_page.add_blouse_to_cart()
    home_page.blouse_in_cart()
    assert home_page.blouse_in_cart() != "empty"
