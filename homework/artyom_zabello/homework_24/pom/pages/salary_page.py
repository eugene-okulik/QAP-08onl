from ..pages.base_page_dev_by import BasePage
from selenium.webdriver.common.by import By

POSITION = (By.CSS_SELECTOR, 'a[data-type="salary_position_id"]')
QA_TEAM_LEADER = (By.CSS_SELECTOR, 'a[data-id="127"]')
AVG_SALARY_QA_TEAM_LEADER = (By.XPATH, '//table[@class="style-table"]/tbody/tr[10]')


class SalaryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_position(self):
        self.find_element(POSITION).click()

    def select_qa_team_leader(self):
        return self.find_element(QA_TEAM_LEADER)

    def get_salary_qa_team_leader(self):
        return self.find_element(AVG_SALARY_QA_TEAM_LEADER)
