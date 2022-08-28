import allure
from ..pages.home_page import HomePage
from ..pages.companies_page import CompaniesPage
from ..pages.andersen_page import AndersenPage


@allure.suite('From home page')
@allure.feature('Find Andersen company')
def test_find_andersen(driver):
    with allure.step('open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open page with companies'):
        home_page.click_page_companies()
        comp_page = CompaniesPage(driver)
    with allure.step("Enter into search field 'Andersen'"):
        comp_page.enter_company_to_search('Andersen')
    with allure.step('Open Andersen page'):
        comp_page.open_andersen_page()
    andersen_page = AndersenPage(driver)
    label = andersen_page.get_label()
    assert label.is_displayed
