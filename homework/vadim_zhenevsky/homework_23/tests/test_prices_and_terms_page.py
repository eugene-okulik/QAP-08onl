from homework_23.pages.home_page import HomePage
from selenium.webdriver.common.by import By


def test_open_prices_and_terms_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_prices_and_terms_page()
    check_prices_and_terms_page = driver.find_element(By.CLASS_NAME,
                                                      'services-work__title')
    print(check_prices_and_terms_page.text)
    assert check_prices_and_terms_page.text == 'Виды работ'


def test_from_prices_and_terms_to_course_work(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_prices_and_terms_page()
    driver.find_element(By.CLASS_NAME, 'popular-link').click()
    driver.switch_to.window(driver.window_handles[1])
    check_course_page = driver.find_element(By.ID, 'intro_title')
    print(check_course_page.text)
    assert check_course_page.text == 'Курсовые работы на заказ в срок'


def test_search_by_type_of_work(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_prices_and_terms_page()
    search_line = driver.find_element(By.CLASS_NAME, 'services-search__input')
    search_line.send_keys('реферат')
    check_search_line_with_request = driver.find_element(By.CLASS_NAME,
                                                         'services-table-body__link_title')
    print(check_search_line_with_request.text)
    assert check_search_line_with_request.text == 'Реферат'
