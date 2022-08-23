from ..pages.best_sales import BestSalesPage

def test_top_search(driver):
    page = BestSalesPage(driver)
    page.open()
    assert page.search_field().is_displayed()


def test_phone(driver):
    page = BestSalesPage(driver)
    page.open()
    assert page.phone_field().is_displayed()


def test_footer(driver):
    page = BestSalesPage(driver)
    page.open()
    assert page.footer_field().is_displayed()
