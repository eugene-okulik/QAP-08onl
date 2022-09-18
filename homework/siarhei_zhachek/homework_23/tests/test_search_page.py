from ..pages.home_page import HomePage
from ..pages.search_page import SearchPage


def test_dropdown_is_work(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.move_to_catalog()
    driver.execute_script("window.scrollTo(document.body.scrollHeight, 200);")
    home_page.move_laptops_und_computer()
    home_page.notebooks.click()
    search_page = SearchPage(driver)
    assert search_page.laptops_in_page.is_displayed()


def test_leave_an_empty_search_field_and_press_enter(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.search_button_press()
    search_page = SearchPage(driver)
    assert search_page.no_product.is_displayed()


def test_the_search_bar_is_working(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.enter_text_search()
    home_page.search_button_press()
    search_page = SearchPage(driver)
    assert search_page.all_elements.is_displayed()
