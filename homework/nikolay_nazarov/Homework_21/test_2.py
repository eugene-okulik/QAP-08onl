from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_blank_text(driver):
    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    blank_text = driver.find_element(By.CLASS_NAME, "_blank").text
    assert blank_text == "Ecommerce software by PrestaShop™", \
        "В самом низу главной страницы нет текста " \
        "Ecommerce software by PrestaShop™"


def test_logo_is_visible(driver):
    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    logo = driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на главной странице"
    driver.find_element(By.CSS_SELECTOR, "[title = 'Women']").click()
    logo = driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на странице 'Women'"
    driver.find_element(By.CSS_SELECTOR, "ul.sf-menu > li:nth-child(2) > a").click()
    logo = driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на странице 'Dresses'"
    driver.find_element(By.CSS_SELECTOR, "ul.sf-menu > li:nth-child(3) > a").click()
    logo = driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на странице 'T-shirts'"


def test_invalid_email_error_is_visible(driver):
    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    driver.find_element \
        (By.CSS_SELECTOR, "[title = 'Log in to your customer account']").click()
    email_input = driver.find_element(By.CSS_SELECTOR, "#email_create")
    email_input.send_keys("Мыло")
    email_input.send_keys(Keys.ENTER)
    error_text = driver.find_element(By.CSS_SELECTOR, ".alert-danger > ol > li").text
    assert error_text == "Invalid email address.", "Нет текста 'Invalid email address'"


def test_alphabetical_sorting_and_quality_control(driver):
    driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    driver.maximize_window()
    quantity = driver.find_element(By.CLASS_NAME, 'product-count')
    sort = Select(driver.find_element(By.ID, 'selectProductSort'))
    sort.select_by_value('name:asc')
    quantity_after_sort = driver.find_element(By.CLASS_NAME, 'product-count')
    assert quantity_after_sort.text == quantity.text


def test_add_to_cart(driver):
    driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    search_product = driver.find_element(By.LINK_TEXT, 'Printed Dress')
    actions = ActionChains(driver)
    actions.move_to_element(search_product)
    actions.perform()
    add_product_1 = driver.find_element(By.XPATH, '//a[@data-id-product="3"]')
    add_product_1.click()
    close_window = driver.find_element(By.XPATH, '//span[@class="cross"]')
    close_window.click()
    cart_after_add = driver.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
    assert 'Cart 1 Product' in cart_after_add.text


def test_button_click(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    start_button = driver.find_element(By.ID, 'button00')
    start_button.click()
    first_button = driver.find_element(By.ID, 'button01')
    first_button.click()
    second_button = driver.find_element(By.ID, 'button02')
    second_button.click()
    third_button = driver.find_element(By.ID, 'button03')
    third_button.click()
    check_button = driver.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in check_button.text


def test_button_click_task_2(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    start_button = driver.find_element(By.ID, 'button00')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start_button))
    start_button.click()
    first_button = driver.find_element(By.ID, 'button01')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(first_button))
    first_button.click()
    second_button = driver.find_element(By.ID, 'button02')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(second_button))
    second_button.click()
    third_button = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(third_button))
    third_button.click()
    check_button = driver.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in check_button.text
