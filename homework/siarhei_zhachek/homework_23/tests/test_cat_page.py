from ..pages.home_page import HomePage
from ..pages.search_page import SearchPage
from ..pages.cat_page import CatPage


def test_add_an_item_to_the_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.move_to_catalog()
    home_page.computers_and_accessories()
    home_page.power_supplies()
    search_page = SearchPage(driver)
    search_page.move_to_power_supplies()
    search_page.add_to_cat()
    search_page.cat_link()
    home_page.go_to_cat()
    cate_page = CatPage(driver)
    assert cate_page.element_cat.is_displayed()


def test_remove_an_item_from_the_shopping_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.move_to_catalog()
    home_page.computers_and_accessories()
    home_page.power_supplies()
    search_page = SearchPage(driver)
    search_page.move_to_power_supplies()
    search_page.add_to_cat()
    search_page.cat_link()
    home_page.go_to_cat()
    cate_page = CatPage(driver)
    cate_page.delete_product_in_cat()
    cate_page.delete_product.click()
    assert cate_page.element_is_not_to_cat.is_displayed()
