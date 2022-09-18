from ..pages.home_page import HomePage
from ..pages.authentification import AuthPage


def test_username(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    home_page.switch_to_the_handle()
    auth_page = AuthPage(driver)
    assert auth_page.username_field_is_displayed()


def test_passwrd(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    home_page.switch_to_the_handle()
    auth_page = AuthPage(driver)
    assert auth_page.passwd_field_is_displayed()


def test_want_to_try(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    home_page.switch_to_the_handle()
    auth_page = AuthPage(driver)
    assert auth_page.want_to_try_is_displayed
