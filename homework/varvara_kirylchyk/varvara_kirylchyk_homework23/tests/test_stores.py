from ..pages.stores import StoresPage
import allure

@allure.feature("Testing Stores Page")
@allure.story("UI")
def test_big_map(driver):
    with allure.step("Open Page"):
        page = StoresPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.big_map_field().is_displayed()


def test_logo(driver):
    with allure.step("Open Page"):
        page = StoresPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.logo_field().is_displayed()


@allure.feature("Testing Stores Page")
def test_address(driver):
    with allure.step("Open Page"):
        page = StoresPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.address_field().is_displayed()
