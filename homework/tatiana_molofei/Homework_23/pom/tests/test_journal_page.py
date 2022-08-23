from ..pages.home_page import HomePage
from ..pages.authentification import AuthPage


def test_journal(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_journal()
    auth_page = AuthPage(driver)
    assert auth_page.test_subscription_button_is_displayed()
