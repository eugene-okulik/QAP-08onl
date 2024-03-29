from time import sleep
import allure
from ..pages.home_page import HomePage
from ..pages.salary_page import SalaryPage


@allure.suite('From home page')
@allure.feature('Search QA team leader salary')
def test_find_qa_teamleader_salary(driver):
    with allure.step('open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('open page salary'):
        home_page.click_salary()
    with allure.step('Find QA team leader position'):
        salary_page = SalaryPage(driver)
        sleep(1)
        driver.execute_script("window.scrollTo(500, 600)")
        salary_page.find_position()
    q_a = salary_page.select_qa_team_leader()
    avg = salary_page.get_salary_qa_team_leader()
    assert 'QA Team Leader' in q_a.text and '3165' in avg.text
