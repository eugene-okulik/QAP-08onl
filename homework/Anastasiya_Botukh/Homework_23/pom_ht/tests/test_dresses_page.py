from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.dresses_page import HomePage
from homework.Anastasiya_Botukh.Homework_23.pom_ht.pages.dresses_window import DressPage


def test_dresses(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_dressed()
    dresses_window = DressPage(driver)
    assert dresses_window.logo.is_displayed()


def test_sort_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_dressed()
    driver.execute_script("window.scrollTo(600, 700)")
    home_page.sort_is_clickable()
    dresses_window = DressPage(driver)
    assert dresses_window.sort_field_is_clickable()


def test_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_dressed()
    home_page.cart_button()
    dresses_window = DressPage(driver)
    assert dresses_window.cart_button_is_clickable()


def test_search_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_dressed()
    home_page.search_field()
    dresses_window = DressPage(driver)
    assert dresses_window.search_field_is_clickable()
