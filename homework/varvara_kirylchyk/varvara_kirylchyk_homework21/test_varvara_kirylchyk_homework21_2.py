# Написать автотесты для сайта
# http://automationpractice.com/
#
# Тесты должны запускаться с помощью Pytest
# (т.е. их названия (тестов, файла(ов))
# должны быть такими, чтобы Pytest понял, что это тесты)
#
# Задание 1:
# Проверить, что в самом низу главной страницы есть текст
# “© 2014 Ecommerce software by PrestaShop™”

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("http://automationpractice.com/")
time.sleep(3)

def test1():
    assert driver.find_element(By.CSS_SELECTOR,
                               "#footer > div > section.bottom-footer.col-xs-12 > div").text == \
           "© 2014 Ecommerce software by PrestaShop™"