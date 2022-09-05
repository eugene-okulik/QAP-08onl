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


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import pytest


@pytest.fixture(scope='function')
def _driver_chrome():
    print('Открытие браузера')
    service = Service(executable_path='C:/Users/Марго/Desktop/TMS/chromedriver.exe')
    _driver_chrome = webdriver.Chrome(service=service)
    _driver_chrome.maximize_window()
    _driver_chrome.implicitly_wait(10)
    yield _driver_chrome
    print('Закрытие браузера')
    _driver_chrome.quit()


# Задание 1.


def test_main_page_text(_driver_chrome):
    _driver_chrome.get('http://automationpractice.com/')
    bottom_text = _driver_chrome.find_element(By.CSS_SELECTOR,
                                      "#footer > div > section.bottom-footer.col-xs-12 > div")
    assert bottom_text.text == "© 2014 Ecommerce software by PrestaShop™"


# Задание 2.


def test_check_logo(_driver_chrome):
    _driver_chrome.get('http://automationpractice.com/')
    _driver_chrome.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[1]/a").click()
    _driver_chrome.implicitly_wait(5)
    assert _driver_chrome.find_element(By.CLASS_NAME, "logo").is_displayed()
    _driver_chrome.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()
    _driver_chrome.implicitly_wait(5)
    assert _driver_chrome.find_element(By.CLASS_NAME, "logo").is_displayed()
    _driver_chrome.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[3]/a").click()
    _driver_chrome.implicitly_wait(5)
    assert _driver_chrome.find_element(By.CLASS_NAME, "logo").is_displayed()


# Задание 3.


def test_check_alert(_driver_chrome):
    _driver_chrome.get('http://automationpractice.com/')
    _driver_chrome.find_element(By.ID, 'contact-link').click()
    email = _driver_chrome.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email.click()
    email.send_keys('мыло')
    submit = _driver_chrome.find_element(By.NAME, "submitMessage")
    submit.click()
    alert = _driver_chrome.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    li_header = alert.find_element(By.TAG_NAME, 'li')
    assert li_header.text == 'Invalid email address.'


# Задание 4.


def test_sorting(_driver_chrome):
    _driver_chrome.get('http://automationpractice.com/')
    _driver_chrome.find_element(By.XPATH, "//a[@title='Women']").click()
    text_start = _driver_chrome.find_element(By.CLASS_NAME, "product-count").text
    sorting = Select(_driver_chrome.find_element(By.ID, "selectProductSort"))
    sorting.select_by_index(3)
    text_end = _driver_chrome.find_element(By.CLASS_NAME, "product-count").text
    assert text_start == text_end, "Error"


# Задание 5.


def test_add_goods_in_basket(_driver_chrome):
    _driver_chrome.get('http://automationpractice.com/index.php')
    goods_button = _driver_chrome.find_element(By.LINK_TEXT, 'Blouse')
    action = ActionChains(_driver_chrome)
    action.move_to_element(goods_button)
    action.perform()
    add_goods = _driver_chrome.find_element(By.XPATH, '//a[@data-id-product="2"]')
    add_goods.click()
    close_new_window = _driver_chrome.find_element(By.XPATH, '//span[@class="cross"]')
    close_new_window.click()
    basket_text = _driver_chrome.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
    assert basket_text.text != 'empty'
