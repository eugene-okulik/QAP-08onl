"""System module."""
# Написать автотесты для сайта
# http://automationpractice.com/
# Тесты должны запускаться с помощью Pytest
# (т.е. их названия (тестов, файла(ов))
# должны быть такими, чтобы Pytest понял, что это тесты)

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    """A dummy docstring."""
    print("Opening Browser")
    options = Options()
    options.add_argument('window-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    print("Closing Browser")
    chrome_driver.quit()


# Задание 1:
# Проверить, что в самом низу главной страницы есть текст
# “© 2014 Ecommerce software by PrestaShop™”


def test1(driver):
    """A dummy docstring."""
    driver.get("http://automationpractice.com/")
    bottom_text = driver.find_element(By.CSS_SELECTOR,
                                      "#footer > div > section.bottom-footer.col-xs-12 > div")
    assert bottom_text.text == "© 2014 Ecommerce software by PrestaShop™"


# Задание 2:
# Проверить, что логотип отображается во всех трех
# категориях сайта (woman, dresses, t-shirts)


def test2(driver):
    """A dummy docstring."""
    driver.get("http://automationpractice.com/")
    driver.find_element(By.XPATH, '//a[@title="Women"]').click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()
    driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()
    driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a').click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()


# Задание 3:
# Проверить, что сообщение “Invalid email address.”
# появляется если ввести слово “мыло”
# в поле емейл и попытаться создать аккаунт

def test_check_alert(driver):
    """A dummy docstring."""
    driver.get("http://automationpractice.com/")
    driver.find_element(By.ID, 'contact-link').click()
    email = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email.click()
    email.send_keys('мыло')
    submit_button = driver.find_element(By.NAME, "submitMessage")
    submit_button.click()
    alert_block_header = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    li_header = alert_block_header.find_element(By.TAG_NAME, 'li')
    assert li_header.text == 'Invalid email address.'


# Задание 4
# На сайте http://automationpractice.com/index.php
# на странице women
# (http://automationpractice.com/index.php?id_category=3&controller=category):
# Отсортировать товары по алфавиту
# (над списком товаров на странице есть дропдаун "Sort by")
# После сортировки проверить,
# что товаров на странице столько же сколько было до сортировки.

def test_sorting(driver):
    """A dummy docstring."""
    driver.get("http://automationpractice.com/")
    driver.find_element(By.XPATH, "//a[@title='Women']").click()
    quantity_text_start = driver.find_element(By.CLASS_NAME, "product-count").text
    sorting = Select(driver.find_element(By.ID, "selectProductSort"))
    sorting.select_by_index(3)
    quantity_text_end = driver.find_element(By.CLASS_NAME, "product-count").text
    assert quantity_text_start == quantity_text_end, "Error"


# Задание 5
# На том же сайте добавить товар в корзину
# и проверить, что товар появился в корзине


def test_busket(driver):
    """A dummy docstring."""
    driver.get("http://automationpractice.com/")
    driver.find_element(By.CLASS_NAME, "logo").click()
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, "a[data-id-product='1']").click()
    assert driver.find_element(By.CLASS_NAME,
                               "ajax_cart_no_product").text != "empty"
