# Задание 7:
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки (появляются последовательно)
# В результате теста проверить, что текст
# “All Buttons Clicked” появился на экране
# здесь понадобится WebDriverWait, и нужно
# будет найти подходящее условие


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


@pytest.fixture(scope='session')
def _setup():
    print('Открытие браузера')
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html')
    sleep(5)
    yield driver
    print('Закрытие браузера')
    driver.quit()


def test_12(_setup):
    driver.find_element(By.ID, 'button00').click()
    sleep(5)
    button_1 = driver.find_element(By.ID, 'button01')
    button_2 = driver.find_element(By.ID, 'button02')
    button_3 = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_1))
    button_1.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_2))
    button_2.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_3))
    button_3.click()
    assert driver.find_element(By.ID, "buttonmessage").text == \
           'All Buttons Clicked'
    sleep(5)
    driver.quit()
