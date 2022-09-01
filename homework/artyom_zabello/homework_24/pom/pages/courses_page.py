from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ..pages.base_page_dev_by import BasePage


DIRECTIONS = (By.CSS_SELECTOR, 'button[class="navbar__select"]')
PROGRAMMING = (By.XPATH, '//a[@href="/courses?area%5Bid%5D=13036779"]')
PROGRAMMING_QA = (By.XPATH, '//a[@class="custom-dropdown__link" and @href="/courses?'
                            'area%5Bid%5D=13036779&specialization%5Bids%5D%5B%5D=18506791"]')
TITLE_PAGE_QA_COURSES = (By.CSS_SELECTOR, 'h1[class="island__title island__title_h1"]')
SEARCH = (By.CSS_SELECTOR, 'input[type="search"]')
PYTHON_QA_COURSE = (By.CSS_SELECTOR, 'a[title="Дистанционный курс по '
                                     'автоматизированному тестированию на Python"]')


class CoursesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_direction(self):
        self.find_element(DIRECTIONS).click()

    def move_to_programming(self):
        self.move_to_element(self.find_element(PROGRAMMING))

    def find_qa_courses(self):
        self.find_element(PROGRAMMING_QA).click()

    def return_title_courses_qa(self):
        return self.find_element(TITLE_PAGE_QA_COURSES)

    def search_topic_to_learn(self, topic):
        search = self.find_element(SEARCH)
        search.send_keys(topic, Keys.ENTER)

    def find_python_qa_course(self):
        return self.find_element(PYTHON_QA_COURSE)
