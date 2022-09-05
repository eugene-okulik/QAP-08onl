# Задание 6:
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки (появляются последовательно)
# В результате теста проверить, что текст
# “All Buttons Clicked” появился на экране


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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


def test_button_click_task_1(_driver_chrome):
    _driver_chrome.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    _driver_chrome.find_element(By.ID, "button00").click()
    assert _driver_chrome.find_element(By.ID, "button01").is_displayed()
    _driver_chrome.find_element(By.ID, "button01").click()
    assert _driver_chrome.find_element(By.ID, "button02").is_displayed()
    _driver_chrome.find_element(By.ID, "button02").click()
    assert _driver_chrome.find_element(By.ID, "button03").is_displayed()
    _driver_chrome.find_element(By.ID, "button03").click()
    assert _driver_chrome.find_element(By.ID, "buttonmessage").text == \
        'All Buttons Clicked'
