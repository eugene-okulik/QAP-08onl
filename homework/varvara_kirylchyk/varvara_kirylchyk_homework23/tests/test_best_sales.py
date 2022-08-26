from ..pages.best_sales import BestSalesPage
import allure

@allure.feature("Testing Best Sales Page")
@allure.story("UI")
def test_top_search(driver):
    with allure.step("Open Page"):
        page = BestSalesPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.search_field().is_displayed()

@allure.feature("Testing Best Sales Page")
def test_phone(driver):
    with allure.step("Open Page"):
        page = BestSalesPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.phone_field().is_displayed()

@allure.feature("Testing Best Sales Page")
def test_footer(driver):
    with allure.step("Open Page"):
        page = BestSalesPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.footer_field().is_displayed()
