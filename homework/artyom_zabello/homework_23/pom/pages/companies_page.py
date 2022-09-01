from selenium.webdriver.common.by import By
from ..pages.base_page_dev_by import BasePage

ENTER_COMPANY_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Название"]')
ANDERSEN_PAGE = (By.LINK_TEXT, 'Andersen')


class CompaniesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_company_to_search(self, value):
        self.find_element(ENTER_COMPANY_FIELD).send_keys(f'{value}')

    def open_andersen_page(self):
        self.find_element(ANDERSEN_PAGE).click()
