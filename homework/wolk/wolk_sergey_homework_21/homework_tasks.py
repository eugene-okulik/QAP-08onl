import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope='function')
def driver():
    #service = Service(executable_path='chromedriver.exe')
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('http://automationpractice.com')


def test_check():
    driver.get('http://automationpractice.com')
    page_women = driver.find_element(By.XPATH, '//a[@title="Women"]')
    page_women.click()
    logo = driver.find_element(By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo


def test_page_dresses():
    driver.get('http://automationpractice.com')
    page_dresses = driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a')
    page_dresses.click()
    logo = driver.find_element(By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo


def test_shirts():
    driver.get('http://automationpractice.com')
    page_dresses = driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[3]/a')
    page_dresses.click()
    logo = driver.find_element(By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo

def test_email():
    driver.get('http://automationpractice.com/')
    sing_in = driver.find_element(By.XPATH, '//a[@class="login"]')
    sing_in.click()
    email_addres = driver.find_element(By.ID, 'email_create')
    email_addres.send_keys('email')
    button = driver.find_element(By.ID, 'SubmitCreate')
    button.click()
    alert_danger = driver.find_element(By.CLASS_NAME, 'alert-danger')
    alert_danger_text = alert_danger.find_element(By.TAG_NAME, 'li')
    assert "Invalid email address." in alert_danger_text.text

def test_quality_control():
    driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    quantity = driver.find_element(By.CLASS_NAME, 'product-count')
    sort_alphabetically = Select(driver.find_element(By.ID, 'selectProductSort'))
    sort_alphabetically.select_by_value('name:asc')
    quantity_after_sort = driver.find_element(By.CLASS_NAME, 'product-count')
    assert quantity_after_sort.text == quantity.text

def test_cart():
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

def test_but_click():
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    button_start = driver.find_element(By.ID, 'button00')
    button_start.click()
    button_one = driver.find_element(By.ID, 'button01')
    button_one.click()
    button_two = driver.find_element(By.ID, 'button02')
    button_two.click()
    button_three = driver.find_element(By.ID, 'button03')
    button_three.click()
    button_check = driver.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in button_check.text

def test_button_click_2():
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    button_start = driver.find_element(By.ID, 'button00')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_start))
    button_start.click()
    button_one = driver.find_element(By.ID, 'button01')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_one))
    button_one.click()
    button_two = driver.find_element(By.ID, 'button02')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_two))
    button_two.click()
    button_three = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_three))
    button_three.click()
    button_check = driver.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in button_check.text
