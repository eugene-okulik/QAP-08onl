import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope='function')
def driver_1() -> None:
    #service = Service(executable_path='chromedriver.exe')
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('http://automationpractice.com')


def test_check():
    driver_1.get('http://automationpractice.com')
    page_women = driver_1.find_element(By.XPATH, '//a[@title="Women"]')
    page_women.click()
    logo = driver_1.find_element(By.XPATH,
                                 '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo


def test_page_dresses():
    driver_1.get('http://automationpractice.com')
    page_dresses = driver_1.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a')
    page_dresses.click()
    logo = driver_1.find_element(By.XPATH,
                                 '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo


def test_shirts():
    driver_1.get('http://automationpractice.com')
    page_dresses = driver_1.find_element(By.XPATH,
                                         '//div[@id="block_top_menu"]/ul/li[3]/a')
    page_dresses.click()
    logo = driver_1.find_element(By.XPATH,
                                 '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo

def test_email():
    driver_1.get('http://automationpractice.com/')
    sing_in = driver_1.find_element(By.XPATH, '//a[@class="login"]')
    sing_in.click()
    email_addres = driver_1.find_element(By.ID, 'email_create')
    email_addres.send_keys('email')
    button = driver_1.find_element(By.ID, 'SubmitCreate')
    button.click()
    alert_danger = driver_1.find_element(By.CLASS_NAME, 'alert-danger')
    alert_danger_text = alert_danger.find_element(By.TAG_NAME, 'li')
    assert "Invalid email address." in alert_danger_text.text

def test_quality_control():
    driver_1.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    quantity = driver_1.find_element(By.CLASS_NAME, 'product-count')
    sort_alphabetically = Select(driver_1.find_element(By.ID, 'selectProductSort'))
    sort_alphabetically.select_by_value('name:asc')
    quantity_after_sort = driver_1.find_element(By.CLASS_NAME, 'product-count')
    assert quantity_after_sort.text == quantity.text

def test_cart():
    driver_1.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    search_product = driver_1.find_element(By.LINK_TEXT, 'Printed Dress')
    actions = ActionChains(driver_1)
    actions.move_to_element(search_product)
    actions.perform()
    add_product_1 = driver_1.find_element(By.XPATH, '//a[@data-id-product="3"]')
    add_product_1.click()
    close_window = driver_1.find_element(By.XPATH, '//span[@class="cross"]')
    close_window.click()
    cart_after_add = driver_1.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
    assert 'Cart 1 Product' in cart_after_add.text

def test_but_click():
    driver_1.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    button_start = driver_1.find_element(By.ID, 'button00')
    button_start.click()
    button_one = driver_1.find_element(By.ID, 'button01')
    button_one.click()
    button_two = driver_1.find_element(By.ID, 'button02')
    button_two.click()
    button_three = driver_1.find_element(By.ID, 'button03')
    button_three.click()
    button_check = driver_1.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in button_check.text

def test_button_click_2():
    driver_1.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    button_start = driver_1.find_element(By.ID, 'button00')
    WebDriverWait(driver_1, 10).until(ec.element_to_be_clickable(button_start))
    button_start.click()
    button_one = driver_1.find_element(By.ID, 'button01')
    WebDriverWait(driver_1, 10).until(ec.element_to_be_clickable(button_one))
    button_one.click()
    button_two = driver_1.find_element(By.ID, 'button02')
    WebDriverWait(driver_1, 10).until(ec.element_to_be_clickable(button_two))
    button_two.click()
    button_three = driver_1.find_element(By.ID, 'button03')
    WebDriverWait(driver_1, 10).until(ec.element_to_be_clickable(button_three))
    button_three.click()
    button_check = driver_1.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in button_check.text
