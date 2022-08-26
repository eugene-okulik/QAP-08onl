from ..pages.home_page import HomePage


def test_search_field(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.search_field_is_displayed()


def test_dropdown(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.move_to_catalog()
    driver.execute_script("window.scrollTo(document.body.scrollHeight, 200);")
    home_page.move_laptops_und_computer()
    home_page.move_to_notebooks()
    assert home_page.notebooks.is_displayed()





