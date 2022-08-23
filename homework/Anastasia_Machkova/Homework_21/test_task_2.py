import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope='function')
def driver():
    print('\nTest start\n')
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    print('\nTest end\n')
    driver.quit()


@pytest.fixture(scope='session')
def all_tests():
    print('\nNow all tests will run\n')
    yield ""
    print('\nTesting is finished\n')


#task_1
def test_check_inscription(driver, all_tests):
    driver.get('http://automationpractice.com/index.php')
    inscription = driver.find_element(By.CSS_SELECTOR, 'section.bottom-footer.col-xs-12')
    assert inscription.text == '© 2014 Ecommerce software by PrestaShop™'


#task_2
def test_logo_women(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[1]/a').click()
    logo_women = driver.find_element(By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo_women


def test_logo_dress(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a').click()
    logo_dress = driver.find_element(By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo_dress


def test_logo_tshirt(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[3]/a').click()
    logo_tshirt = driver.find_element(By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo_tshirt


#test_3
def test_email_alert(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.CLASS_NAME, 'header_user_info').click()
    input_email = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    input_email.send_keys('soup')
    driver.find_element(By.NAME, 'SubmitCreate').click()
    invalid_message = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    invalid_message_text = invalid_message.find_element(By.TAG_NAME, 'li')
    assert invalid_message_text.text == 'Invalid email address.'


#task_4
def test_sort_alphabetically(driver):
    driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    number = driver.find_element(By.CLASS_NAME, 'product-count')
    sorting = Select(driver.find_element(By.ID, 'selectProductSort'))
    sorting.select_by_value('name:asc')
    number_after_sorting = driver.find_element(By.CLASS_NAME, 'product-count')
    assert number.text == number_after_sorting.text


#task_5
def test_add_to_cart(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.CSS_SELECTOR, "a[data-id-product='2']").click()
    assert driver.find_element(By.CLASS_NAME, 'ajax_cart_quantity') != "empty"


#task_6
def test_simple_buttons_clicked(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    driver.find_element(By.ID, 'button00').click()
    driver.find_element(By.ID, 'button01').click()
    driver.find_element(By.ID, 'button02').click()
    driver.find_element(By.ID, 'button03').click()
    all_clicked = driver.find_element(By.ID, 'buttonmessage')
    assert all_clicked.is_displayed()


#task_7
def test_dynamic_buttons_clicked(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html')
    driver.find_element(By.ID, 'button00').click()
    button_1 = driver.find_element(By.ID, 'button01')
    button_2 = driver.find_element(By.ID, 'button02')
    button_3 = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_1))
    button_1.click()
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_2))
    button_2.click()
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_3))
    button_3.click()
    all_buttons_clicked = driver.find_element(By.ID, 'buttonmessage')
    assert all_buttons_clicked.text == 'All Buttons Clicked'
