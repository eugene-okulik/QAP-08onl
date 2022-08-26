from ..pages.home_page import HomePage
from ..pages.enter_email_page import EnterEmailPage
import pytest
import allure


@allure.feature('Log in')
def test_press_to_enter(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Open login page"):
        home_page.press_entry()
        log_in = EnterEmailPage(driver)
    with allure.step('Enter invalid email'):
        log_in.enter_email()
    with allure.step('Enter invalid password'):
        log_in.enter_password()
    with allure.step('Press button to submit'):
        log_in.press_submit()
    error = log_in.find_error()
    assert error.is_displayed


@allure.feature('Log in')
def test_empty_fields(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step("Open login page"):
        home_page.press_entry()
    with allure.step('Press button to submit with empty fields'):
        log_in = EnterEmailPage(driver)
        log_in.press_submit()
    error = log_in.find_error()
    assert error.is_displayed
