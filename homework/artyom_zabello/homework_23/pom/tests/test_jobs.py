from ..pages.home_page import HomePage
from ..pages.jobs_page import JobsPage


def test_find_qa_auto_middle(driver):
    """Job selection test"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_jobs()
    jobs_page = JobsPage(driver)
    jobs_page.close_pop_up()
    jobs_page.select_qa_auto()
    jobs_page.select_level(2)
    job = jobs_page.return_selected_job()
    level = jobs_page.return_selected_level()
    quant = jobs_page.return_jobs_quantity()
    assert job.is_displayed() and level.is_displayed() and '3' in quant.text
