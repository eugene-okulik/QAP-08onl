from time import sleep
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


@pytest.mark.hard
def test_main_page_text(driver):
    driver.get('http://automationpractice.com/')
    footer = driver.find_element(By.XPATH, '//section[@class="bottom-footer col-xs-12"]/div')
    assert footer.text == '© 2014 Ecommerce software by PrestaShop™'


@pytest.mark.hard
def test_categories(driver):
    result = 0
    driver.get('http://automationpractice.com/index.php')

    women_page = driver.find_element(By.XPATH, '//a[@title="Women"]')
    women_page.click()
    footer1 = driver.find_element(By.XPATH, '//section[@class="bottom-footer col-xs-12"]/div')
    if footer1.is_displayed():
        result += 1

    dresses = driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]')
    dresses.click()
    footer2 = driver.find_element(By.XPATH, '//section[@class="bottom-footer col-xs-12"]/div')
    if footer2.is_displayed():
        result += 1

    t_shirts_page = driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]')
    t_shirts_page.click()
    footer3 = driver.find_element(By.XPATH, '//section[@class="bottom-footer col-xs-12"]/div')
    if footer3.is_displayed():
        result += 1
    assert result == 3


@pytest.mark.hard
def test_invalid_email(driver):
    driver.get('http://automationpractice.com/index.php?'
               'controller=authentication&back=my-account')
    input_email = driver.find_element(By.CSS_SELECTOR, 'input[id="email_create"]')
    input_email.send_keys('Мыло')
    driver.find_element(By.CSS_SELECTOR, 'button[name="SubmitCreate"]').click()
    alert_message = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    WebDriverWait(driver, 5).until(EC.visibility_of(alert_message))
    assert alert_message.is_displayed()


@pytest.mark.hard
def test_of_products_count(driver):
    driver.get('http://automationpractice.com/index.php?'
               'id_category=3&controller=category#/')
    products_before = driver.find_elements(By.CLASS_NAME, 'product-container')
    count_before = len(products_before)
    sort_by = Select(driver.find_element(By.ID, 'selectProductSort'))
    sort_by.select_by_value('name:asc')
    sleep(3)
    products_after = driver.find_elements(By.CLASS_NAME, 'product-container')
    count_after = len(products_after)
    assert count_before == count_after


@pytest.mark.hard
def test_cart(driver2):
    driver2.get('http://automationpractice.com/index.php')
    driver2.execute_script("window.scrollTo(500, 600)")
    container = driver2.find_element(By.XPATH, '//*[@id="homefeatured"]/li[1]/div')
    container.find_element(By.CSS_SELECTOR, 'a[title="Add to cart"]').click()
    driver2.find_element(By.CSS_SELECTOR, 'a[title="Proceed to checkout"]').click()
    orders_container = driver2.find_element(By.XPATH, '//td[@class="cart_description"]/p/a')
    assert orders_container.is_displayed()


@pytest.mark.hard
def test_click_buttons1(driver):
    driver.get('https://testpages.herokuapp.com/styled/'
               'dynamic-buttons-simple.html')
    driver.find_element(By.ID, 'button00').click()
    driver.find_element(By.ID, 'button01').click()
    driver.find_element(By.ID, 'button02').click()
    driver.find_element(By.ID, 'button03').click()
    clicked = driver.find_element(By.ID, 'buttonmessage')
    assert clicked.is_displayed()


@pytest.mark.hard
def test_click_buttons_wait(driver):
    driver.get('https://testpages.herokuapp.com/'
               'styled/dynamic-buttons-disabled.html')
    driver.find_element(By.ID, 'button00').click()
    sleep(4)
    one = driver.find_element(By.ID, 'button01')
    two = driver.find_element(By.ID, 'button02')
    three = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(one))
    one.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(two))
    two.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(three))
    three.click()
    clicked = driver.find_element(By.ID, 'buttonmessage')
    assert clicked.is_displayed()
