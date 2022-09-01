from ..pages.home_page import HomePage
from ..pages.authentification import AuthPage


def test_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.is_displayed_email_field()


def test_passwd(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.passwd_field.is_displayed()
