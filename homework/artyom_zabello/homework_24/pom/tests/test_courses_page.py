from pytest_bdd import scenario, given, when, then
import allure
from ..pages.home_page import HomePage
from ..pages.courses_page import CoursesPage


@allure.suite('From home page')
@allure.feature('User agreement')
def test_find_user_agreement(driver):
    with allure.step('Open home page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Open page courses'):
        home_page.click_courses()
    with allure.step('Select direction'):
        courses = CoursesPage(driver)
        courses.find_direction()
        courses.move_to_programming()
    with allure.step('Select QA courses'):
        courses.find_qa_courses()
        assert courses.return_title_courses_qa().is_displayed()


@allure.feature('Test BDD')
@allure.suite('From home page')
@scenario('bdd_tests.feature', 'Qa auto courses exist')
def test_jobs_bdd():
    pass


with allure.step('open_home_page'):
    @given('I am at home page')
    def open_home_page(driver):
        home = HomePage(driver)
        home.open()


with allure.step('switch_to_courses_page'):
    @when('I switch to courses page')
    def switch_to_courses_page(driver):
        home = HomePage(driver)
        home.click_courses()

with allure.step('find_python_courses'):
    @when('I will find Python courses using the search bar')
    def find_python_courses(driver):
        courses = CoursesPage(driver)
        courses.search_topic_to_learn('Python')

with allure.step('find_qa_auto_courses'):
    @then('Qa auto courses is displayed')
    def find_qa_auto_courses(driver):
        courses = CoursesPage(driver)
        assert courses.find_python_qa_course().is_displayed()
