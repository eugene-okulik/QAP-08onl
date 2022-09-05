import pytest

from ..pages.home_page import HomePage
from ..pages.authentification import AuthPage
import allure
from ..tests.test_data import data


@allure.feature('Authentification')
@allure.story('Login')
@pytest.mark.parametrize('user', data.users)
def test_login(driver, user):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click buton'):
        home_page.open_sign_in()
    auth_page = AuthPage(driver)
    email, passwd = user
    auth_page.email_filed.send_keys(email)
    auth_page.passwd_field.send_keys(passwd)
    assert auth_page.is_displayed_email_field()


@allure.feature('Authentification')
@allure.story('Registration')
def test_passwd(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click buton'):
        home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.passwd_field.is_displayed()
