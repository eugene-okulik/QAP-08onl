import allure
from ..pages.home_page import HomePage
from ..pages.jobs_page import JobsPage


@allure.suite('From home page')
@allure.feature('Find QA AUTO middle level jobs')
def test_find_qa_auto_middle(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open jobs page'):
        home_page.click_jobs()
    with allure.step('Close pop-up'):
        jobs_page = JobsPage(driver)
        jobs_page.close_pop_up()
    with allure.step('Select qa auto middle'):
        jobs_page.select_qa_auto()
        jobs_page.select_level(2)
        job = jobs_page.return_selected_job()
        level = jobs_page.return_selected_level()
    quant = jobs_page.return_jobs_quantity()
    assert job.is_displayed() and level.is_displayed() and '3' in quant.text
