from pytest_bdd import scenario, given, when, then
from pom.pages.home_page import HomePage
from pom.pages.authentication import AuthPage


@scenario('login.feature', 'login field exists')
def test_login_field():
    pass


@scenario('login.feature', 'password field exists')
def test_passwd_field():
    pass


@given('Я на главной странице')
def open_main_page(driver):
    # driver.get('http://automationpractice.com/')
    home_page = HomePage(driver)
    home_page.open()


@when('I click login button')
def click_login_button(driver):
    HomePage(driver).open_sign_in()

@when('click login field')
def click_field(driver):
    AuthPage(driver).email_field.click()


@then('I see login field')
def check_login_field(driver):
    print('Asserting email field exists')
    assert AuthPage(driver).is_displayed_email_field()


@then('I see password field')
def check_passwd_field(driver):
    assert AuthPage(driver).passwd_field.is_displayed()
