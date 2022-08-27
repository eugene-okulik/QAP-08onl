from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.contact_page import HomePage
from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.send_message import Message


def test_subject_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.contact_us_button.click()
    message_page = Message(driver)
    assert message_page.subject_field.is_displayed()


def test_email_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.contact_us_button.click()
    message_page = Message(driver)
    assert message_page.email_field().is_displayed()


def test_order_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.contact_us_button.click()
    message_page = Message(driver)
    assert message_page.order_field().is_displayed()


def test_file(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.contact_us_button.click()
    message_page = Message(driver)
    assert message_page.file().is_displayed()


def test_message_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.contact_us_button.click()
    message_page = Message(driver)
    assert message_page.message_field().is_displayed()


def test_submit_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.contact_us_button.click()
    home_page.submit_button()
    message_page = Message(driver)
    assert message_page.submit_button_is_clickable()
