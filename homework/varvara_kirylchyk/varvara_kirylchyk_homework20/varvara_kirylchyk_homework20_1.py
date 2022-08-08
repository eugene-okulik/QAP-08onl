# Задание 1
# Кликнуть все чекбоксы на странице.
# Их там 17. Открываются по клику на >
# https://demoqa.com/checkbox

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get('https://demoqa.com/checkbox')
toggle = driver.find_element(By.CLASS_NAME, 'rct-checkbox')
toggle.click()
