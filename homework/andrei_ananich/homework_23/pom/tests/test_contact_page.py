"""modules"""
from ..pages.home_page import HomePage
from ..pages.contact_page import ContactPage


def test_contact_link_alert_error(driver):
    """modules"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_contact_us()
    cont_page = ContactPage(driver)
    cont_page.email_address()
    cont_page.order_reference()
    cont_page.message()
    cont_page.submit_message()
    cont_page.alert()
    assert cont_page.alert()
