from homework.Anastacia_Kuznetcova.homework23.pom.pages.home_page import HomePage


def test_contact_us_clickable(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.contact_us_is_clickable()


def test_cart_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.cart_is_displayed()


def test_t_shirt_txt(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.t_shirt_is_displayed()
