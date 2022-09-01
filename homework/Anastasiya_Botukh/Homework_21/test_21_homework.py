import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


# task_1
def test_check_text(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    presta_text = driver.find_element(By.CSS_SELECTOR, 'section[class="bottom-footer col-xs-12"]')
    assert presta_text.text == '© 2014 Ecommerce software by PrestaShop™'


# task_2
def test_logo_women(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[1]/a').click()
    assert driver.find_element(By.ID, 'header_logo').is_displayed()


def test_logo_dresses(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a').click()
    assert driver.find_element(By.ID, 'header_logo').is_displayed()


def test_logo_t_shirts(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[3]/a').click()
    assert driver.find_element(By.ID, 'header_logo').is_displayed()


# test_3
def test_email_message(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.CLASS_NAME, 'header_user_info').click()
    input_email = driver.find_element(By.CSS_SELECTOR, 'input[id="email_create"]')
    input_email.send_keys('soup')
    driver.find_element(By.CSS_SELECTOR, 'button[id="SubmitCreate"]').click()
    alert_header = driver.find_element(By.CLASS_NAME, 'alert-danger')
    alert_text = alert_header.find_element(By.TAG_NAME, 'li')
    assert alert_text.text == 'Invalid email address.'


# test_4
def test_sorted(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[1]/a').click()
    start_count_products = driver.find_element(By.CLASS_NAME, 'compare_product_count').text
    sort = Select(driver.find_element(By.CSS_SELECTOR, 'select[id="selectProductSort"]'))
    sort.select_by_value("name:asc")
    end_count_products = driver.find_element(By.CLASS_NAME, 'compare_product_count').text
    assert start_count_products == end_count_products


# test_5
def test_add_to_cart(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.execute_script("window.scrollTo(600, 700)")
    container = driver.find_element(By.CLASS_NAME, 'product-container')
    ActionChains(driver).move_to_element(container).perform()
    driver.find_element(By.CSS_SELECTOR, 'a[data-id-product="1"]').click()
    assert driver.find_element(By.CLASS_NAME, 'ajax_cart_no_product').text != 'empty'


# test_6
def test_buttons_click(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    driver.find_element(By.ID, 'buttons').click()
    driver.find_element(By.ID, 'button01').click()
    driver.find_element(By.ID, 'button02').click()
    driver.find_element(By.ID, 'button03').click()
    clicked = driver.find_element(By.ID, 'buttonmessage')
    assert clicked.is_displayed()


# test_7
@pytest.mark.skip
def test_dynamic_buttons_click(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html')
    driver.find_element(By.ID, 'button00').click()
    button_1 = driver.find_element(By.ID, 'button01')
    button_2 = driver.find_element(By.ID, 'button02')
    button_3 = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_1))
    button_1.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_2))
    button_2.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_3))
    button_3.click()
    assert driver.find_element(By.ID, "buttonmessage").text == 'All Buttons Clicked'
