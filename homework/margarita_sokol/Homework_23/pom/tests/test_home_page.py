from pages.home_page import HomePage


def test_cart_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.cart_is_displayed()


def test_contact_us_clickable(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.contact_us_is_clickable()


def test_women_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.women_is_displayed()
