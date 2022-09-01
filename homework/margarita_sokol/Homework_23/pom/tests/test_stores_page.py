from pages.stores_page import StoresPage


def test_address_is_displayed(driver):
    stores_page = StoresPage(driver)
    stores_page.open()
    assert stores_page.address_is_displayed()


def test_card_is_displayed(driver):
    stores_page = StoresPage(driver)
    stores_page.open()
    assert stores_page.address_is_displayed()


def test_search_is_displayed(driver):
    stores_page = StoresPage(driver)
    stores_page.open()
    assert stores_page.search_is_displayed()
