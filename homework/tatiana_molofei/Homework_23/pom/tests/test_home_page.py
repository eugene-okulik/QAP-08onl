from ..pages.home_page import HomePage
from ..pages.authentification import AuthPage


def test_callme(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.callme_button()
    auth_page = AuthPage(driver)
    assert auth_page.callme_is_clickable()


def test_pass_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    driver.implicitly_wait(60)
    home_page.test_pass_button()
    auth_page = AuthPage(driver)
    assert auth_page.test_pass_field_is_clickable()
