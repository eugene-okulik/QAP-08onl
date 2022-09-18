# Написать автотесты для сайта http://automationpractice.com/
# Тесты должны запускаться с помощью Pytest
# (т.е. их названия (тестов, файла(ов)) должны быть такими,
# чтобы Pytest понял, что это тесты)

# На сайте http://automationpractice.com/index.php
# добавить товар в корзину и проверить, что товар появился в корзине

"""System module."""
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)
chrome_driver.implicitly_wait(10)
chrome_driver.maximize_window()
chrome_driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")

@pytest.fixture(scope='function')
def test_alpha_sort():
    """module"""
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_add_to_cart():
    """module"""
    chrome_driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")
    search_product = chrome_driver.find_element(By.LINK_TEXT, 'Printed Dress')
    actions = ActionChains(chrome_driver)
    actions.move_to_element(search_product)
    actions.perform()
    chrome_driver.find_element(By.XPATH, '//a[@data-id-product="3"]').click()
    chrome_driver.find_element(By.XPATH, '//span[@class="cross"]').click()
    chrome_driver.implicitly_wait(10)
    cart_after_add = chrome_driver.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
    assert 'Cart 1 Product' in cart_after_add.text
    chrome_driver.quit()
