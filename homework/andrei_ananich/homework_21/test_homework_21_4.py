# Написать автотесты для сайта http://automationpractice.com/
# Тесты должны запускаться с помощью Pytest
# (т.е. их названия (тестов, файла(ов)) должны быть такими,
# чтобы Pytest понял, что это тесты)

# Задание 4
# На сайте http://automationpractice.com/index.php на странице women
# (http://automationpractice.com/index.php?id_category=3&controller=category):
# Отсортировать товары по алфавиту (над списком товаров на странице есть дропдаун "Sort by")
# После сортировки проверить, что товаров на странице столько же сколько было до сортировки.

"""Module providingFunction printing python version."""
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)


@pytest.fixture(scope='function')
def test_alpha_sort():
    """module"""
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield
    chrome_driver.quit()


def test_sorting():
    """module"""
    chrome_driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    quantity = chrome_driver.find_element(By.CLASS_NAME, 'product-count')
    sort_alphabetically = Select(chrome_driver.find_element(By.ID, 'selectProductSort'))
    sort_alphabetically.select_by_value('name:asc')
    quantity_after_sort = chrome_driver.find_element(By.CLASS_NAME, 'product-count')
    assert quantity_after_sort.text == quantity.text
    chrome_driver.quit()
