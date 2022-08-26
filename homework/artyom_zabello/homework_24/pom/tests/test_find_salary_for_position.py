from time import sleep
from ..pages.home_page import HomePage
from ..pages.salary_page import SalaryPage
import allure
import pytest


def test_find_qa_teamleader_salary(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_salary()
    salary_page = SalaryPage(driver)
    sleep(1)
    driver.execute_script("window.scrollTo(500, 600)")
    salary_page.find_position()
    qa = salary_page.select_qa_team_leader()
    avg = salary_page.get_salary_qa_team_leader()
    assert 'QA Team Leader' in qa.text and '3165' in avg.text
