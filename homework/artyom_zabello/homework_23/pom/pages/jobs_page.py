from selenium.webdriver.common.by import By
from ..pages.base_page_dev_by import BasePage

QA_AUTO_SELECTOR = (By.XPATH, '//div[@class="form-group radio_buttons '
                              'optional filter_specialization_title"]/span[10]/label')
CHECKBOXES = (By.CLASS_NAME, 'collection_check_boxes')
LEVEL_CHECKBOXES = CHECKBOXES[0:4]
QUANTITY_JOBS = (By.CLASS_NAME, 'vacancies-list__header-title')
SELECTED_JOBS_QA_AUTO = (By.CSS_SELECTOR, 'div[data-value="QA Automation"]')
SELECTED_LEVEL_MIDDLE = (By.CSS_SELECTOR, 'div[data-value="middle"]')
CLOSE_POP_UP = (By.XPATH, '//form[@class="button_to"]/button')


class JobsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_qa_auto(self):
        self.find_element(QA_AUTO_SELECTOR).click()

    def select_level(self, level_num):
        var = self.find_elements(LEVEL_CHECKBOXES)
        var[level_num].click()

    def return_jobs_quantity(self):
        return self.find_element(QUANTITY_JOBS)

    def return_selected_job(self):
        return self.find_element(SELECTED_JOBS_QA_AUTO)

    def return_selected_level(self):
        return self.find_element(SELECTED_LEVEL_MIDDLE)

    def close_pop_up(self):
        self.find_element(CLOSE_POP_UP).click()
