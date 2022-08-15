import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html")
time.sleep(3)

# Задание 6
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки
# (появляются последовательно)
# В результате теста проверить,
# что текст “All Buttons Clicked” появился на экране
# Подсказка: здесь достаточно implicitly_wait

def test5():
    driver.find_element(By.ID, "button00").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button01").is_displayed()
    driver.implicitly_wait(5)

def test6():
    driver.find_element(By.ID, "button01").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button02").is_displayed()
    driver.implicitly_wait(5)

def test7():
    driver.find_element(By.ID, "button02").click()
    time.sleep(5)
    assert driver.find_element(By.ID, "button03").is_displayed()
    time.sleep(3)

def test8():
    driver.find_element(By.ID, "button03").click()
    time.sleep(3)
    assert driver.find_element(By.ID, "buttonmessage").text == \
        'All Buttons Clicked'
    time.sleep(3)
