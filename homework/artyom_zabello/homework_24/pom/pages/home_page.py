from selenium.webdriver.common.by import By
from ..pages.base_page_dev_by import BasePage


ENTRY_BUTTON = (By.LINK_TEXT, 'Вход')
COMPANIES = (By.LINK_TEXT, 'Компании')
JOBS = (By.XPATH, '//div[@class="navbar__row"]/nav/a[3]')
SALARY = (By.LINK_TEXT, 'Зарплаты')
HOME_BUTTON = (By.CSS_SELECTOR, 'img[class="navbar__brand-img"]')
LIST_BUTTON = (By.CSS_SELECTOR, 'div[class="navbar__toggler"]')
COURSES = (By.LINK_TEXT, 'Курсы')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://devby.io/')

    def press_entry(self):
        self.find_element(ENTRY_BUTTON).click()

    def click_page_companies(self):
        self.find_element(COMPANIES).click()

    def click_jobs(self):
        self.find_element(JOBS).click()

    def click_list_button(self):
        self.find_element(LIST_BUTTON).click()

    def click_courses(self):
        self.find_element(COURSES).click()
        window = self.driver.window_handles[1]
        self.driver.switch_to.window(window)

    def click_salary(self):
        self.find_element(SALARY).click()
