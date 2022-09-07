import allure
from pages.about import AboutPage

@allure.feature("Testing About Page")
@allure.story("UI")
def test_big_map(driver):
    with allure.step("Open Page"):
        page = AboutPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.company_field().is_displayed()


@allure.feature("Testing About Page")
def test_logo(driver):
    with allure.step("Open Page"):
        page = AboutPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.team_field().is_displayed()


@allure.feature("Testing About Page")
def test_address(driver):
    with allure.step("Open Page"):
        page = AboutPage(driver)
        page.open()
    with allure.step("Checking Element"):
        assert page.testimonials_field().is_displayed()
