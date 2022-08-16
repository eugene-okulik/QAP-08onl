"""System module."""
# Задание 7
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html
# Нужно кликнуть на все 4 кнопки (активируются последовательно)
# В результате теста проверить,
# что текст “All Buttons Clicked” появился на экране
# Подсказка: здесь понадобится WebDriverWait,
# и нужно будет найти подходящее условие

import time
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')


@pytest.fixture(scope='session')
def setup():
    """A dummy docstring."""
    print("Opening Browser")
    driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")
    time.sleep(3)
    yield driver
    print("Closing Browser")
    driver.quit()


def test9(setup):
    """A dummy docstring."""
    driver.find_element(By.ID, 'button00').click()
    time.sleep(5)
    one = driver.find_element(By.ID, 'button01')
    two = driver.find_element(By.ID, 'button02')
    three = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(one))
    one.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(two))
    two.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(three))
    three.click()
    assert driver.find_element(By.ID, "buttonmessage").text == \
       'All Buttons Clicked'
    time.sleep(5)
    driver.quit()
