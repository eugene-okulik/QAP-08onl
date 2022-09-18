import allure
from pytest_bdd import scenario, given, when, then
from ..pages.home_page import HomePage
from ..pages.jobs_page import JobsPage



@allure.feature('Test BDD')
@scenario('bdd_tests.feature', 'Jobs for QA Auto middle exist')
def test_jobs_bdd():
    pass


@given('I am at home page')
def open_home_page(driver):
    home = HomePage(driver)
    home.open()


@when('I switch to page with jobs')
def open_jobs_page(driver):
    home = HomePage(driver)
    home.click_jobs()


@when('Select job as QA Auto')
def select_job(driver):
    jobs = JobsPage(driver)
    jobs.close_pop_up()
    jobs = JobsPage(driver)
    jobs.select_qa_auto()


@when('Select level as middle')
def select_level(driver):
    jobs = JobsPage(driver)
    jobs.select_level(2)


@then('Jobs were selected')
def find_job(driver):
    jobs = JobsPage(driver)
    job = jobs.return_selected_job()
    level = jobs.return_selected_level()
    quant = jobs.return_jobs_quantity()
    assert job.is_displayed() and level.is_displayed() and '3' in quant.text
