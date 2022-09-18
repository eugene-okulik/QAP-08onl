from ..pages.home_page import HomePage
from ..pages.enter_email_page import EnterEmailPage


def test_press_to_enter(driver):
    """ Test.Log in with incorrect data """
    home_page = HomePage(driver)
    home_page.open()
    home_page.press_entry()
    log_in = EnterEmailPage(driver)
    log_in.enter_email()
    log_in.enter_password()
    log_in.press_submit()
    error = log_in.find_error()
    assert error.is_displayed


def test_empty_fields(driver):
    """Test. Log in with empty fields """
    home_page = HomePage(driver)
    home_page.open()
    home_page.press_entry()
    log_in = EnterEmailPage(driver)
    log_in.press_submit()
    error = log_in.find_error()
    assert error.is_displayed
