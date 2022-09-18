# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки (появляются последовательно)
# В результате теста проверить, что текст
# “All Buttons Clicked” появился на экране


""" module """
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)


@pytest.fixture(scope='function')
def _four_click():
    """module"""
    chrome_driver.maximize_window()
    chrome_driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html")
    chrome_driver.implicitly_wait(5)
    yield chrome_driver


def test_button_start(_four_click):
    """module"""
    chrome_driver.find_element(By.ID, "button00").click()
    chrome_driver.implicitly_wait(5)
    assert chrome_driver.find_element(By.ID, "button01").is_displayed()
    chrome_driver.implicitly_wait(5)


def test_button_one():
    """module"""
    chrome_driver.find_element(By.ID, "button01").click()
    chrome_driver.implicitly_wait(5)
    assert chrome_driver.find_element(By.ID, "button02").is_displayed()
    chrome_driver.implicitly_wait(5)


def test_button_two():
    """module"""
    chrome_driver.find_element(By.ID, "button02").click()
    chrome_driver.implicitly_wait(5)
    assert chrome_driver.find_element(By.ID, "button03").is_displayed()
    chrome_driver.implicitly_wait(5)


def test_button_three():
    """module"""
    chrome_driver.find_element(By.ID, "button03").click()
    sleep(5)
    assert chrome_driver.find_element(By.ID, "buttonmessage").text == \
        'All Buttons Clicked'
    chrome_driver.quit()
