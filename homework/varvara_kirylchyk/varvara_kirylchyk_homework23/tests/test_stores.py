from ..pages.stores import StoresPage

def test_big_map(driver):
    page = StoresPage(driver)
    page.open()
    assert page.big_map_field().is_displayed()


def test_logo(driver):
    page = StoresPage(driver)
    page.open()
    assert page.logo_field().is_displayed()


def test_address(driver):
    page = StoresPage(driver)
    page.open()
    assert page.address_field().is_displayed()
