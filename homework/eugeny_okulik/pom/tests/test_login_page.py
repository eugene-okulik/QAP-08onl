import pytest

from pages.home_page import HomePage
from pages.authentication import AuthPage
from allure_commons.types import AttachmentType
from tests.test_data import data
import allure


@allure.feature('Authentication')
@allure.story('Login')
@pytest.mark.parametrize('user', data.users)
def test_login(driver, user):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    with allure.step('Click Sign In button'):
        home_page.open_sign_in()
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    auth_page = AuthPage(driver)
    email, passw = user
    auth_page.email_field.send_keys(email)
    auth_page.passwd_field.send_keys(passw)

    assert auth_page.is_displayed_email_field()


@allure.feature('Authentication')
@allure.story('Registration')
def test_passwd(driver):
    with allure.step('Open Home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click Sign In button'):
        home_page.sign_in_button.click()
    # home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.passwd_field.is_displayed()
