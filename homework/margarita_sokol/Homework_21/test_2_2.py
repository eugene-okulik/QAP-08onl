# Задание 6:
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки (появляются последовательно)
# В результате теста проверить, что текст
# “All Buttons Clicked” появился на экране


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


@pytest.fixture(scope='session')
def _setup():
    print('Открытие браузера')
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    sleep(5)
    yield driver
    print('Закрытие браузера')
    driver.quit()


def test_8(_setup):
    driver.find_element(By.ID, "button00").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button01").is_displayed()
    driver.implicitly_wait(5)


def test9():
    driver.find_element(By.ID, "button01").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button02").is_displayed()
    driver.implicitly_wait(5)


def test10():
    driver.find_element(By.ID, "button02").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button03").is_displayed()
    driver.implicitly_wait(5)


def test11():
    driver.find_element(By.ID, "button03").click()
    sleep(3)
    assert driver.find_element(By.ID, "buttonmessage").text == \
        'All Buttons Clicked'
