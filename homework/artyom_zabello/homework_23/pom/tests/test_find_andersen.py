from ..pages.home_page import HomePage
from ..pages.companies_page import CompaniesPage
from ..pages.andersen_page import AndersenPage


def test_find_andersen(driver):
    """Selection of the Andersen company page"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_page_companies()
    comp_page = CompaniesPage(driver)
    comp_page.enter_company_to_search('Andersen')
    comp_page.open_andersen_page()
    andersen_page = AndersenPage(driver)
    label = andersen_page.get_label()
    assert label.is_displayed
