# Задание 7:
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки (появляются последовательно)
# В результате теста проверить, что текст
# “All Buttons Clicked” появился на экране
# здесь понадобится WebDriverWait, и нужно
# будет найти подходящее условие


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='function')
def _driver_chrome():
    print('Открытие браузера')
    service = Service(executable_path='C:/Users/Марго/Desktop/TMS/chromedriver.exe')
    _driver = webdriver.Chrome(service=service)
    _driver.maximize_window()
    _driver.implicitly_wait(10)
    yield _driver_chrome
    print('Закрытие браузера')
    _driver_chrome.quit()


def test_button_click_task_2(_driver_chrome):
    _driver_chrome.get('https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html')
    _driver_chrome.find_element(By.ID, 'button00').click()
    _driver_chrome.implicitly_wait(5)
    button_1 = _driver_chrome.find_element(By.ID, 'button01')
    button_2 = _driver_chrome.find_element(By.ID, 'button02')
    button_3 = _driver_chrome.find_element(By.ID, 'button03')
    WebDriverWait(_driver_chrome, 10).until(ec.element_to_be_clickable(button_1))
    button_1.click()
    WebDriverWait(_driver_chrome, 10).until(ec.element_to_be_clickable(button_2))
    button_2.click()
    WebDriverWait(_driver_chrome, 10).until(ec.element_to_be_clickable(button_3))
    button_3.click()
    assert _driver_chrome.find_element(By.ID, "buttonmessage").text == \
           'All Buttons Clicked'
