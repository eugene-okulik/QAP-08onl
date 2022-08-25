# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки (появляются последовательно)
# В результате теста проверить, что текст “All Buttons Clicked” появился на экране
# здесь понадобится WebDriverWait, и нужно будет найти подходящее условие

""" module """
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)


@pytest.fixture(scope='function')
def _follow_click():
    """module"""
    chrome_driver.maximize_window()
    chrome_driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.quit()


def test_follow_button(_follow_click):
    """module"""
    chrome_driver.find_element(By.ID, 'button00').click()
    sleep(5)
    button_start = chrome_driver.find_element(By.ID, 'button01')
    button_one = chrome_driver.find_element(By.ID, 'button02')
    button_two = chrome_driver.find_element(By.ID, 'button03')
    WebDriverWait(chrome_driver, 7).until(EC.element_to_be_clickable(button_start))
    button_start.click()
    WebDriverWait(chrome_driver, 7).until(EC.element_to_be_clickable(button_one))
    button_one.click()
    WebDriverWait(chrome_driver, 7).until(EC.element_to_be_clickable(button_two))
    button_two.click()
    assert chrome_driver.find_element(By.ID, "buttonmessage").text == \
           'All Buttons Clicked'
    chrome_driver.quit()
