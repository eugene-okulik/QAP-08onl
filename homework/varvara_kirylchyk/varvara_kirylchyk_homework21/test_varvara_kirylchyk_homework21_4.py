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

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")
time.sleep(3)