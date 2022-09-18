"""modules"""
from ..pages.home_page import HomePage
from ..pages.authentification import AuthPage


def test_login(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.is_displayed_email_field()


def test_passwd(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.passwd_field.is_displayed()


def test_contact_us(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_contact_us()
    auth_page = AuthPage(driver)
    assert auth_page.contact_us.is_displayed()
