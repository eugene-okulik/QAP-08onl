from ..pages.home_page import HomePage
# from ..pages.authentification import AuthPage


def test_callme(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.callme_is_clickable()


def test_pass_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    driver.implicitly_wait(60)
    assert home_page.test_pass_field_is_clickable()
