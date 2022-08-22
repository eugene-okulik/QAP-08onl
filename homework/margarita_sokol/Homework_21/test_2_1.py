# Написать автотесты для сайта http://automationpractice.com/
# Задание 1:
# Проверить, что в самом низу главной страницы есть текст
# “© 2014 Ecommerce software by PrestaShop™”
#
# Задание 2:
# Проверить, что логотип отображается во всех трех
# категориях сайта (woman, dresses, t-shirts)
#
# Задание 3:
# Проверить, что сообщение “Invalid email address.”
# появляется если ввести слово “мыло” в поле емейл
# и попытаться создать аккаунт
#
# Задание 4:
# На сайте http://automationpractice.com/index.php
# на странице women
# (http://automationpractice.com/index.php?id_category=3&controller=category):
# Отсортировать товары по алфавиту
# (над списком товаров на странице есть дропдаун "Sort by")
# После сортировки проверить, что товаров на
# странице столько же сколько было до сортировки.
#
# Задание 5:
# На том же сайте добавить товар в корзину
# и проверить, что товар появился в корзине


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


@pytest.fixture(scope='session')
def _setup():
    print('Открытие браузера')
    driver.get('http://automationpractice.com/')
    sleep(5)
    yield driver
    print('Закрытие браузера')
    driver.quit()


# Задание 1.


def test1(_setup):
    bottom_text = driver.find_element(By.CSS_SELECTOR,
                                      "#footer > div > section.bottom-footer.col-xs-12 > div")
    assert bottom_text.text == "© 2014 Ecommerce software by PrestaShop™"


# Задание 2.


def test2():
    driver.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[1]/a").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()


def test_3():
    driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()


def test_4():
    driver.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[3]/a").click()
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()


# Задание 3.


def test_5():
    driver.find_element(By.ID, 'contact-link').click()
    email = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email.click()
    email.send_keys('мыло')
    submit = driver.find_element(By.NAME, "submitMessage")
    submit.click()
    sleep(5)
    alert = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    li_header = alert.find_element(By.TAG_NAME, 'li')
    assert li_header.text == 'Invalid email address.'


# Задание 4.


def test_6():
    driver.find_element(By.XPATH, "//a[@title='Women']").click()
    text_start = driver.find_element(By.CLASS_NAME, "product-count").text
    sorting = Select(driver.find_element(By.ID, "selectProductSort"))
    sorting.select_by_index(3)
    text_end = driver.find_element(By.CLASS_NAME, "product-count").text
    assert text_start == text_end, "Error"


# Задание 5.


def test_7():
    driver.find_element(By.CLASS_NAME, "logo").click()
    sleep(5)
    driver.find_element(By.CSS_SELECTOR, "a[data-id-product='1']").click()
    assert driver.find_element(By.CLASS_NAME,
                               "ajax_cart_no_product").text != "empty"
