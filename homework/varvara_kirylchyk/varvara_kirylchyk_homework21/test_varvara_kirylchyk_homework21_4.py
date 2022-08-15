# Задание 7
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html
# Нужно кликнуть на все 4 кнопки (активируются последовательно)
# В результате теста проверить,
# что текст “All Buttons Clicked” появился на экране
# Подсказка: здесь понадобится WebDriverWait,
# и нужно будет найти подходящее условие

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")
time.sleep(3)


def test9():
    driver.find_element(By.ID, "button00").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button01").is_displayed()
    driver.implicitly_wait(5)


def test10():
    driver.find_element(By.ID, "button01").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button02").is_displayed()
    driver.implicitly_wait(5)


def test11():
    driver.find_element(By.ID, "button02").click()
    time.sleep(10)
    assert driver.find_element(By.ID, "button03").is_displayed()
    time.sleep(5)


def test12():
    button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "button03")))
    button.click()
    time.sleep(5)
    assert driver.find_element(By.ID, "buttonmessage").text == \
        'All Buttons Clicked'
    time.sleep(3)
